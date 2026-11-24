# SEOGlint SEO Resources

Free technical SEO templates, examples, and checklists for developers and site owners. Every file is meant to be copied, edited for your own site, and checked before you deploy it.

Maintained by [SEOGlint](https://www.seoglint.com/).

## Who this is for

- Developers shipping or maintaining a website
- SEO specialists who need a clean starting template
- Site owners who want to understand what each file does before they change it

## What's inside

| Folder | Contents |
|---|---|
| [`robots-txt/`](robots-txt/) | robots.txt examples, including search crawlers, AI training crawlers, and user-triggered fetchers |
| [`structured-data/`](structured-data/) | JSON-LD for Organization, WebSite, SoftwareApplication, Article, BreadcrumbList, FAQPage |
| [`sitemaps/`](sitemaps/) | A valid XML sitemap and a sitemap index |
| [`meta-tags/`](meta-tags/) | An HTML `<head>` with title, description, canonical, Open Graph, and JSON-LD |
| [`llms-txt/`](llms-txt/) | An example llms.txt file and its limitations |
| [`checklists/`](checklists/) | A practical technical SEO audit checklist |
| [`scripts/`](scripts/) | A validation script used to test every example in this repository |

## Requirements

None to read or copy the files. To run the validation script you need Python 3.9 or newer (standard library only).

## Usage

1. Pick the file you need.
2. Replace every `example.com` URL, name, and date with your own values.
3. Delete properties that do not truthfully describe your page or business. Do not keep placeholder data.
4. Test the result (see [Testing](#testing)).
5. Deploy.

## Testing

Check that the examples parse:

```bash
python3 scripts/validate.py
```

Expected output ends with:

```text
All checks passed.
```

The script checks JSON syntax and required JSON-LD keys, XML well-formedness and sitemap structure, the HTML example, and robots.txt line syntax. It does not check whether Google will show a rich result. For that, test your live page with:

- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)
- [SEOGlint Schema Markup Validator](https://www.seoglint.com/schema-markup-validator.html)

## Limitations

- These are templates, not guarantees. Valid markup and a clean robots.txt do not guarantee rankings, rich results, AI citations, or traffic.
- Search engines and AI providers change their crawlers and rules. Each folder lists the official sources it was checked against and the date of the check.
- Valid structured data does not guarantee a rich result. For example, Google stopped showing FAQ rich results entirely on May 7, 2026, although FAQPage is still valid schema.org markup. See [`structured-data/README.md`](structured-data/README.md).

## Related SEOGlint tools

- [Schema generator](https://www.seoglint.com/schema-generator.html)
- [Robots.txt generator](https://www.seoglint.com/robots-txt-generator.html)
- [Sitemap checker](https://www.seoglint.com/sitemap-checker.html)
- [llms.txt generator](https://www.seoglint.com/llms-txt-generator.html)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE). The SEOGlint website and tools are not part of this repository and are not open source.
