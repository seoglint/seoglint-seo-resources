# Meta tags

[`example.html`](example.html) is a complete `<head>` for an article page. Each tag has a comment explaining what it's for.

**Last verified:** 24 November 2026.

## The tags that matter most

| Tag | Why |
|---|---|
| `<title>` | Usually shown as the headline in search results. Make it unique per page. Google may rewrite it. |
| `meta name="description"` | Often used as the snippet. Write a plain summary of the page; there is no fixed length rule, but long text gets cut off. |
| `link rel="canonical"` | Tells search engines which URL is the main version when several URLs show the same content. Use an absolute URL. |
| `meta name="viewport"` | Needed for mobile rendering. |
| `meta name="robots"` | Leave it out unless you need `noindex`, `nofollow`, `nosnippet`, or a preview limit. The default is index and follow. |
| Open Graph (`og:*`) | Controls the title, description, and image in social and chat link previews. Use a 1200×630 image. |
| `hreflang` | Only for sites with translated or regional versions. Every version must link to all others, including itself. |

## What to skip

- `meta name="keywords"`: Google ignores it.
- `noindex` and a robots.txt `Disallow` on the same URL: if crawling is blocked, Google never sees the `noindex`.

## Testing

1. `python3 scripts/validate.py` checks the HTML parses and the key tags are present.
2. Check a live page with the [SEOGlint SEO audit](https://www.seoglint.com/) or the [Open Graph preview tool](https://www.seoglint.com/open-graph-preview.html).
3. Use URL Inspection in Google Search Console to see the canonical Google selected.

## Official sources

- [Google: Title links](https://developers.google.com/search/docs/appearance/title-link)
- [Google: Snippets and meta descriptions](https://developers.google.com/search/docs/appearance/snippet)
- [Google: Canonicalization](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google: Robots meta tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
- [The Open Graph protocol](https://ogp.me/)
