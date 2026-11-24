#!/usr/bin/env python3
"""Validate the examples in this repository.

Checks JSON-LD syntax and required keys, XML sitemap structure,
the HTML meta tag example, robots.txt line syntax, and llms.txt format.
Uses only the Python standard library. Run from the repository root:

    python3 scripts/validate.py
"""

import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def fail(path, message):
    errors.append(f"{path.relative_to(ROOT)}: {message}")


# Keys that each example type must have to be useful.
REQUIRED = {
    "Organization": ["name", "url"],
    "WebSite": ["name", "url"],
    "SoftwareApplication": ["name", "applicationCategory", "offers"],
    "Article": ["headline", "datePublished", "author", "image"],
    "BreadcrumbList": ["itemListElement"],
    "FAQPage": ["mainEntity"],
}


def check_json_ld(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(path, f"invalid JSON: {exc}")
        return
    if data.get("@context") != "https://schema.org":
        fail(path, '@context must be "https://schema.org"')
    kind = data.get("@type")
    if kind not in REQUIRED:
        fail(path, f"unexpected @type {kind!r}")
        return
    for key in REQUIRED[kind]:
        if key not in data:
            fail(path, f"{kind} is missing {key!r}")
    if kind == "BreadcrumbList":
        items = data["itemListElement"]
        for i, item in enumerate(items, start=1):
            if item.get("position") != i:
                fail(path, f"breadcrumb {i} has position {item.get('position')}")
            if "item" not in item and i != len(items):
                fail(path, f"breadcrumb {i} needs an item URL")
    if kind == "FAQPage":
        for q in data["mainEntity"]:
            if q.get("@type") != "Question" or not q.get("acceptedAnswer", {}).get("text"):
                fail(path, "each FAQ entry needs a Question with acceptedAnswer.text")


SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}(:\d{2})?([+-]\d{2}:\d{2}|Z))?$")


def check_sitemap(path):
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        fail(path, f"invalid XML: {exc}")
        return
    if root.tag not in (f"{SITEMAP_NS}urlset", f"{SITEMAP_NS}sitemapindex"):
        fail(path, f"root must be urlset or sitemapindex in the sitemaps.org namespace, got {root.tag}")
        return
    child = "url" if root.tag.endswith("urlset") else "sitemap"
    entries = root.findall(f"{SITEMAP_NS}{child}")
    if not entries:
        fail(path, "no entries")
    if len(entries) > 50000:
        fail(path, "more than 50,000 entries")
    for entry in entries:
        loc = entry.findtext(f"{SITEMAP_NS}loc")
        if not loc or not loc.startswith("https://"):
            fail(path, f"loc must be an absolute https URL: {loc!r}")
        lastmod = entry.findtext(f"{SITEMAP_NS}lastmod")
        if lastmod and not DATE_RE.match(lastmod):
            fail(path, f"lastmod is not W3C Datetime: {lastmod!r}")


class HeadParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found = set()
        self.in_title = False
        self.in_jsonld = False
        self.jsonld = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "html" and a.get("lang"):
            self.found.add("lang")
        elif tag == "meta":
            name = a.get("name") or a.get("property")
            if name:
                self.found.add(name)
        elif tag == "link" and a.get("rel") == "canonical":
            if (a.get("href") or "").startswith("https://"):
                self.found.add("canonical")
        elif tag == "script" and a.get("type") == "application/ld+json":
            self.in_jsonld = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "script":
            self.in_jsonld = False

    def handle_data(self, data):
        if self.in_title and data.strip():
            self.found.add("title")
        if self.in_jsonld:
            self.jsonld.append(data)


def check_html(path):
    parser = HeadParser()
    parser.feed(path.read_text(encoding="utf-8"))
    for tag in ["lang", "title", "description", "viewport", "canonical", "og:title", "og:image"]:
        if tag not in parser.found:
            fail(path, f"missing {tag}")
    if parser.jsonld:
        try:
            json.loads("".join(parser.jsonld))
        except json.JSONDecodeError as exc:
            fail(path, f"embedded JSON-LD is invalid: {exc}")


ROBOTS_RE = re.compile(r"^(user-agent|allow|disallow|sitemap|crawl-delay)\s*:\s*\S*", re.I)


def check_robots(path):
    group_open = False
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if not ROBOTS_RE.match(line):
            fail(path, f"line {n} is not a recognized directive: {raw!r}")
            continue
        field = line.split(":", 1)[0].strip().lower()
        if field == "user-agent":
            group_open = True
        elif field in ("allow", "disallow") and not group_open:
            fail(path, f"line {n} has a rule before any User-agent line")
        elif field == "sitemap" and not line.split(":", 1)[1].strip().startswith("https://"):
            fail(path, f"line {n} sitemap must be an absolute URL")


LINK_RE = re.compile(r"^- \[[^\]]+\]\(https?://[^)]+\)(: .+)?$")


def check_llms(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or not lines[0].startswith("# "):
        fail(path, "first line must be an H1 (# Name)")
    for n, line in enumerate(lines, start=1):
        if line.startswith("- ") and not LINK_RE.match(line):
            fail(path, f"line {n} is not a '- [Title](URL): description' link")


def main():
    checks = [
        (sorted((ROOT / "structured-data").glob("*.json")), check_json_ld),
        (sorted((ROOT / "sitemaps").glob("*.xml")), check_sitemap),
        (sorted((ROOT / "meta-tags").glob("*.html")), check_html),
        (sorted((ROOT / "robots-txt").glob("*.txt")), check_robots),
        ([ROOT / "llms-txt" / "llms.txt"], check_llms),
    ]
    count = 0
    for paths, check in checks:
        for path in paths:
            check(path)
            count += 1
            print(f"checked {path.relative_to(ROOT)}")
    if errors:
        print(f"\n{len(errors)} problem(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print(f"\nAll checks passed. ({count} files)")


if __name__ == "__main__":
    main()
