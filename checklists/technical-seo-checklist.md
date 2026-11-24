# Technical SEO audit checklist

A practical checklist for developers and site owners. Each item says what to check, how to check it, and what "good" looks like. Work through it for your home page and one example of each page template (article, product, category).

**Last verified:** 24 November 2026. No checklist guarantees rankings or AI citations; it removes the technical reasons a good page might not be found.

## 1. Crawling and indexing

- [ ] **robots.txt loads.** Open `/robots.txt`. Good: status 200, plain text, no `Disallow: /` under `User-agent: *` unless intended.
- [ ] **Important pages aren't blocked.** Test key URLs in the Search Console robots.txt report or URL Inspection. Good: "Allowed".
- [ ] **No accidental `noindex`.** View source and search for `noindex`, and check the `X-Robots-Tag` response header. Good: only on pages you want hidden.
- [ ] **Pages are indexed.** Check the Pages report in Search Console. Good: important pages listed as "Indexed"; read the reason for each excluded group.
- [ ] **Status codes are correct.** Crawl the site with any SEO crawler. Good: live pages return 200, moved pages 301 to the final URL in one hop, removed pages 404 or 410, no soft 404s.

## 2. XML sitemap

- [ ] **Sitemap exists and is declared** in robots.txt with a `Sitemap:` line.
- [ ] **Submitted** in Google Search Console and Bing Webmaster Tools.
- [ ] **Contains only canonical, indexable 200 URLs.** Good: no redirects, no `noindex` pages, no 404s.
- [ ] **`lastmod` is accurate.** Good: changes only when page content changes.

See [`sitemaps/`](../sitemaps/).

## 3. Canonical URLs

- [ ] **Every indexable page has a self-referencing canonical** with an absolute URL.
- [ ] **One version of the site.** `http`, `https`, `www`, and non-`www` all 301 to a single version.
- [ ] **Parameter and duplicate URLs** (sorting, tracking, print views) canonicalize to the main URL.
- [ ] **Google agrees.** URL Inspection shows "Google-selected canonical" matches yours.

## 4. Metadata

- [ ] **Unique `<title>` on every page**, describing the page first.
- [ ] **Unique meta description** that summarizes the page.
- [ ] **Open Graph tags** with a 1200×630 image for pages people share.
- [ ] **`lang` attribute** on `<html>`, and `hreflang` if you have translated versions.

See [`meta-tags/`](../meta-tags/).

## 5. Heading structure

- [ ] **One clear `<h1>`** that matches the page topic.
- [ ] **Headings in order** (`h2` under `h1`, `h3` under `h2`), used for structure, not styling.
- [ ] **Headings describe the section** in plain words, so a reader can scan them.

## 6. Internal linking

- [ ] **Every important page is linked from at least one other page.** Good: no orphan pages; key pages reachable within about three clicks from the home page.
- [ ] **Links are crawlable `<a href>` elements**, not JavaScript click handlers.
- [ ] **Anchor text describes the target** ("robots.txt guide", not "click here").
- [ ] **No internal links to redirects or 404s.**

## 7. Structured data

- [ ] **Organization and WebSite markup** on the home page.
- [ ] **Page-type markup** (Article, Product, BreadcrumbList) where it fits.
- [ ] **Markup matches visible content.** No hidden reviews, prices, or FAQs.
- [ ] **No errors** in the Rich Results Test or Schema.org Validator.

See [`structured-data/`](../structured-data/).

## 8. Mobile usability

- [ ] **Viewport meta tag** present.
- [ ] **Same content on mobile and desktop.** Google indexes the mobile version.
- [ ] **Readable without zooming;** tap targets not crowded.

## 9. Performance basics

- [ ] **Core Web Vitals** in the "Good" range: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1. Check field data in Search Console or PageSpeed Insights.
- [ ] **Images** compressed, sized to their display size, with `width` and `height` set, and lazy-loaded below the fold.
- [ ] **HTTPS** everywhere with a valid certificate.
- [ ] **Main content in the HTML**, or rendered reliably. Check the rendered HTML in URL Inspection.

## 10. AI-search readiness

- [ ] **Search crawlers allowed.** Googlebot, Bingbot, OAI-SearchBot, Claude-SearchBot, and PerplexityBot aren't blocked, unless that is your decision.
- [ ] **Training crawlers set deliberately.** GPTBot, ClaudeBot, and Google-Extended allowed or blocked on purpose. Blocking them doesn't remove you from search.
- [ ] **Firewall or CDN bot rules** don't block crawlers you allowed in robots.txt.
- [ ] **Content answers questions directly.** Clear headings, a direct answer near the top, facts with sources, and author and date information.
- [ ] **llms.txt considered.** Optional, with no confirmed effect on AI search.

See [`robots-txt/`](../robots-txt/) and [`llms-txt/`](../llms-txt/).

## Run it faster

The [SEOGlint SEO audit](https://www.seoglint.com/) checks many of these items for a single URL. Use it alongside Search Console, not instead of it.
