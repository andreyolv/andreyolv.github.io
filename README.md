# andreyolv.github.io

Personal CV and technical portfolio, published with GitHub Pages at
<https://andreyolv.github.io/>.

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).
The `docs/portfolio/` folder is a copy of the `pikakube` documentation library;
the rest of `docs/` contains the CV and the curated portfolio pages.

## Local development

```bash
pip install -r requirements.txt
mkdocs serve          # http://127.0.0.1:8000
mkdocs build          # static site in site/
```

## Deployment

Pushing to `main` triggers `.github/workflows/deploy.yml`, which builds the site
and publishes it through GitHub Pages.

In the repository settings, set **Pages → Build and deployment → Source** to
**GitHub Actions**.
