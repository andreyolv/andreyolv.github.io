# Agent Instructions — andreyolv.github.io

## Workflow rule

**Work directly on the `main` branch. Do not create branches or pull requests for this repository.** All changes are committed and pushed directly to `main`, which triggers the GitHub Pages deployment. You can always commit and push without asking first.

## Language rule

**All documentation in `docs/` must be written in English.**

This includes:
- Markdown pages (`.md`)
- Navigation labels in `mkdocs.yml`
- Button text and UI strings inside Markdown
- Any new portfolio or CV pages added to `docs/`

Do not add new documentation in Portuguese. If you need to translate existing Portuguese pages, do it to English.

## Project context

- Static site built with [Zensical](https://github.com/zensical/zensical), a MkDocs-compatible
  static site generator by the creators of Material for MkDocs.
- Source docs live in `docs/`.
- Built and deployed to GitHub Pages via `.github/workflows/deploy.yml` on push to `main`.
- Local dev: `pip install -r requirements.txt && zensical serve` (preview at http://127.0.0.1:8000)
- Build: `pip install -r requirements.txt && zensical build` (static site in `site/`)
- The portfolio catalog (`docs/portfolio/catalog.md`) is generated statically before each
  build by `scripts/generate_portfolio_catalog.py`, which reads the lifecycle frontmatter
  of every page under `docs/portfolio/`. The MkDocs hook (`hooks/portfolio.py`) is no longer
  used because Zensical does not run arbitrary Python hooks.

## Tech Stack page

The page `docs/tech-stack.md` lists tools and skills by domain with levels 1–4. When editing it, keep the English labels and the level legend in English.
