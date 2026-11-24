# robots.txt examples

robots.txt is a plain text file at the root of a host (`https://example.com/robots.txt`). It tells well-behaved crawlers which paths they may fetch. It is a request, not access control: it does not hide pages, and it does not remove pages that are already indexed.

**Last verified:** 24 November 2026, against each operator's own documentation (linked below).

## Files

| File | Use it when |
|---|---|
| [`basic.txt`](basic.txt) | You want every crawler allowed, with a private area blocked and the sitemap declared |
| [`ai-crawlers.txt`](ai-crawlers.txt) | You want to stay visible in search and AI answers, but opt out of AI model training |

## Three kinds of bot, three different decisions

AI companies now run separate bots for separate jobs. Blocking one does not block the others.

| Kind | What it does | Examples |
|---|---|---|
| **Search crawler** | Builds an index that answers are drawn from. Blocking it can remove you from that product's results. | Googlebot, Bingbot, OAI-SearchBot, Claude-SearchBot, PerplexityBot |
| **Training crawler or token** | Collects content that may be used to train AI models. Blocking it does not affect search inclusion. | GPTBot, ClaudeBot, Google-Extended |
| **User-triggered fetcher** | Fetches one page because a person asked an assistant to look at it. It does not crawl automatically. | ChatGPT-User, Claude-User, Perplexity-User |

## User-agent reference

| robots.txt token | Operator | Kind | Notes |
|---|---|---|---|
| `Googlebot` | Google | Search | Crawls for Google Search, including AI Overviews and AI Mode. Use Googlebot rules, `noindex`, and `nosnippet` to manage those. |
| `Google-Extended` | Google | Training / Gemini control | Not a separate crawler and has no HTTP user-agent string. It controls whether content fetched by Google's crawlers may be used for Gemini model training and grounding. Google states it does not affect inclusion or ranking in Google Search, so it does **not** control AI Overviews. |
| `Bingbot` | Microsoft | Search | Crawls for Bing, which also supplies results to other products. |
| `OAI-SearchBot` | OpenAI | Search | Used to surface sites in ChatGPT search. OpenAI says robots.txt changes can take about 24 hours to apply. |
| `GPTBot` | OpenAI | Training | Controlled independently of OAI-SearchBot. |
| `ChatGPT-User` | OpenAI | User-triggered | OpenAI says robots.txt rules may not apply because a user starts the request. It is not used to decide search inclusion. |
| `ClaudeBot` | Anthropic | Training | Blocking it signals that the site's future content should be excluded from training. |
| `Claude-SearchBot` | Anthropic | Search | Blocking it may reduce visibility in Claude's search results. |
| `Claude-User` | Anthropic | User-triggered | Anthropic says its bots, including Claude-User, honor robots.txt. |
| `PerplexityBot` | Perplexity | Search | Used to surface sites in Perplexity search results. |
| `Perplexity-User` | Perplexity | User-triggered | Perplexity says it generally ignores robots.txt because a user requested the fetch. |

If a bot ignores robots.txt and you must block it, use your firewall or CDN with the operator's published IP ranges.

## Rules that catch people out

- A crawler obeys only the most specific group that matches its name. A `User-agent: GPTBot` group overrides the `User-agent: *` group entirely for GPTBot. It does not add to it.
- Each host and subdomain needs its own robots.txt. `blog.example.com` does not read `example.com/robots.txt`.
- Disallowing a page does not remove it from Google. To keep a page out of search results, allow crawling and use `<meta name="robots" content="noindex">` instead.
- Don't block CSS or JavaScript files that your pages need to render.
- Paths are case-sensitive.

## Testing

1. Run `python3 scripts/validate.py` from the repository root to check line syntax.
2. After deploying, open `https://your-domain/robots.txt` in a browser and confirm it returns status 200 as plain text.
3. Use the robots.txt report in Google Search Console, or the [SEOGlint robots.txt tester](https://www.seoglint.com/robots-txt-generator.html).

## Official sources

- Google: [robots.txt introduction](https://developers.google.com/search/docs/crawling-indexing/robots/intro), [Google's common crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers), [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- OpenAI: [Overview of OpenAI crawlers](https://developers.openai.com/api/docs/bots)
- Anthropic: [Does Anthropic crawl data from the web?](https://support.claude.com/en/articles/8896518)
- Perplexity: [Perplexity crawlers](https://docs.perplexity.ai/guides/bots)
- Standard: [RFC 9309, Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309)
