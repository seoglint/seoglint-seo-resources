# llms.txt

llms.txt is a **proposed** convention, not a standard. It is a Markdown file at `https://your-domain/llms.txt` that gives language models a short summary of a site and links to its most useful pages, ideally as clean Markdown versions.

**Last verified:** 24 November 2026.

## Format

[`llms.txt`](llms.txt) follows the proposal at [llmstxt.org](https://llmstxt.org/):

1. `# Name` (required): an H1 with the site or project name
2. `> Summary` (optional): a one-paragraph blockquote
3. Free text (optional): any extra context
4. `## Section` headings, each with a list of `- [Title](URL): description` links
5. `## Optional` (optional): links that can be skipped when context is short

The proposal also suggests offering a Markdown copy of important pages at the same URL with `.md` added. That is what the example links point to. If you don't publish Markdown copies, link to the normal HTML pages instead.

## Adoption and limitations

Be clear about what this file does and doesn't do:

- **No major search engine or AI assistant has committed to using llms.txt** to decide what to crawl, index, rank, or cite. Google's Search guidance says you don't need it for AI features in Search. Separately, Chrome's Lighthouse has an experimental "agentic browsing" audit that checks for the file, which is about agents already on your site, not about search visibility.
- Publishing llms.txt does **not** guarantee AI discovery, ranking, or citation.
- It does **not** replace robots.txt. It doesn't grant or block access to anything. Use [robots.txt](../robots-txt/) for crawler access.
- Some developer tools and documentation sites do use it, so it can be useful for technical products whose docs are read by coding assistants.

It costs little to publish. Treat it as optional documentation, not an SEO lever.

## Installation

1. Write the file, using [`llms.txt`](llms.txt) as a template or the [SEOGlint llms.txt generator](https://www.seoglint.com/llms-txt-generator.html).
2. Upload it to the root of your site so it loads at `/llms.txt`.
3. Serve it as `text/plain` or `text/markdown` with status 200.
4. Check every link loads.

## Testing

`python3 scripts/validate.py` checks the file starts with an H1 and every list link uses the `- [Title](URL)` format.

## Sources

- [llms.txt proposal](https://llmstxt.org/)
