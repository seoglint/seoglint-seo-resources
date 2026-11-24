# JSON-LD structured data examples

Structured data describes what a page is about in a format machines can read. These examples use [schema.org](https://schema.org/) vocabulary in JSON-LD, the format Google recommends.

**Last verified:** 24 November 2026.

## How to use

Put the JSON inside a script tag in the page's `<head>` or `<body>`:

```html
<script type="application/ld+json">
{ ...paste the example here... }
</script>
```

Then replace every `example.com` value, name, and date. Only mark up content that a visitor can actually see on the page.

## Files

| File | Type | Put it on | Google rich result? |
|---|---|---|---|
| [`organization.json`](organization.json) | Organization | Home page or About page | Can inform the logo and knowledge panel. No guaranteed display. |
| [`website.json`](website.json) | WebSite | Home page only | Helps Google choose the site name shown in results. |
| [`software-application.json`](software-application.json) | SoftwareApplication | The page for one app or tool | Google's software app rich result also needs a review or `aggregateRating`. This example leaves those out on purpose: add them only if you have genuine reviews shown on the page. |
| [`article.json`](article.json) | Article | Blog posts, guides, news | Eligible for article enhancements. Supply images in 16:9, 4:3, and 1:1. |
| [`breadcrumbs.json`](breadcrumbs.json) | BreadcrumbList | Any page with a breadcrumb trail | Eligible for breadcrumb display. The last item may omit `item`. |
| [`faq-page.json`](faq-page.json) | FAQPage | A page that shows these exact questions and answers | **No.** Google stopped showing FAQ rich results on 7 May 2026. The markup is still valid schema.org, Google says it can keep using it to understand the page, and other consumers may still read it. |

## Linking entities with `@id`

`organization.json` and `website.json` give each entity an `@id`. Other examples refer to the publisher with `{"@id": "https://www.example.com/#organization"}` so you describe the organization once and reference it everywhere. If you use a reference, the organization markup must be published on your site too.

## Testing

1. `python3 scripts/validate.py` checks JSON syntax and required keys.
2. [Google Rich Results Test](https://search.google.com/test/rich-results) shows which Google features a live URL or code snippet is eligible for.
3. [Schema.org Validator](https://validator.schema.org/) checks the markup against the full vocabulary.
4. [SEOGlint Schema Markup Validator](https://www.seoglint.com/schema-markup-validator.html), or build new markup with the [SEOGlint Schema Generator](https://www.seoglint.com/schema-generator.html).

## Limitations

- Valid markup makes a page eligible for a rich result. It doesn't guarantee one, and it isn't a ranking factor on its own.
- Markup that doesn't match visible content can lead to a manual action from Google.
- No evidence shows that adding structured data guarantees citations in AI answers.

## Official sources

- [Google: Introduction to structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Google: Structured data search gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery)
- [Google: FAQ structured data](https://developers.google.com/search/docs/appearance/structured-data/faqpage)
- [Google: Site names](https://developers.google.com/search/docs/appearance/site-names)
- [schema.org](https://schema.org/)
