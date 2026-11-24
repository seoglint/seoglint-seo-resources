# XML sitemaps

An XML sitemap lists the URLs you want search engines to find. It helps discovery, especially for new or large sites. It doesn't force indexing.

**Last verified:** 24 November 2026.

## Files

| File | Use it when |
|---|---|
| [`example-sitemap.xml`](example-sitemap.xml) | Your site has fewer than 50,000 URLs |
| [`example-sitemap-index.xml`](example-sitemap-index.xml) | You split URLs across several sitemap files |

## Rules

- Use absolute, canonical URLs only: same protocol, same host, no redirects, no `noindex` pages.
- One sitemap file can hold at most 50,000 URLs and 50 MB uncompressed. Use an index file beyond that.
- Encode the file as UTF-8 and escape `&` as `&amp;` (see the last URL in the example).
- `lastmod` should be the date the page's main content last changed, in W3C Datetime format (`2026-11-20` or `2026-11-20T14:30:00+05:00`). Don't set it to today on every build.
- Google ignores `<priority>` and `<changefreq>`, so these examples leave them out.

## Submitting

1. Reference the sitemap in robots.txt: `Sitemap: https://www.example.com/sitemap.xml`
2. Submit it in Google Search Console and Bing Webmaster Tools.

## Testing

1. `python3 scripts/validate.py` checks the XML is well-formed and every URL has a `<loc>`.
2. After deploying, check the live file with the [SEOGlint Sitemap Checker](https://www.seoglint.com/sitemap-checker.html) and the Sitemaps report in Search Console.

## Official sources

- [sitemaps.org protocol](https://www.sitemaps.org/protocol.html)
- [Google: Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
