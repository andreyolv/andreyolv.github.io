# andreyolv.github.io

Personal CV and technical portfolio, published with GitHub Pages at
<https://andreyolv.github.io/>.

Built with [Zensical](https://github.com/zensical/zensical), a MkDocs-compatible
static site generator by the creators of Material for MkDocs.
The `docs/portfolio/` folder is a copy of the `pikakube` documentation library;
the rest of `docs/` contains the CV and the curated portfolio pages.

## Local development

```bash
pip install -r requirements.txt
zensical serve          # http://127.0.0.1:8000
zensical build          # static site in site/
```

Before building, regenerate the static portfolio catalog from page frontmatter:

```bash
python scripts/generate_portfolio_catalog.py
```

## Deployment

Pushing to `main` triggers `.github/workflows/deploy.yml`, which regenerates the
portfolio catalog, builds the site with Zensical and publishes it through
GitHub Pages.

In the repository settings, set **Pages → Build and deployment → Source** to
**GitHub Actions**.

## Notes on the migration from MkDocs

- The build tool changed from `mkdocs` (MkDocs Material) to `zensical`.
- `mkdocs.yml` is kept because Zensical is MkDocs-compatible.
- The MkDocs hook `hooks/portfolio.py` (status badges + dynamic catalog) is not
  supported by Zensical, which does not run arbitrary Python hooks. The catalog
  is now generated statically by `scripts/generate_portfolio_catalog.py` before
  each build. Per-page status badges are no longer injected; frontmatter metadata
  is preserved on each project page.
