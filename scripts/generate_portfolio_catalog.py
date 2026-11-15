"""Generate the static portfolio catalog for Zensical builds.

This replaces the MkDocs hook ``hooks/portfolio.py``, which Zensical does not
run (it does not execute arbitrary Python hooks/plugins).

The script reads the YAML frontmatter of every page under ``docs/portfolio/``,
validates the lifecycle metadata (status / environment / kind), and renders the
filterable project catalog HTML into ``docs/portfolio/catalog.md`` in place of
the ``<!-- portfolio-catalog -->`` placeholder.

Run it before ``zensical build``:

    python scripts/generate_portfolio_catalog.py
"""

from __future__ import annotations

import html
import posixpath
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
CATALOG_PATH = DOCS_DIR / "portfolio" / "catalog.md"
CATALOG_PLACEHOLDER = "<!-- portfolio-catalog -->"

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)

STATUS_LABELS = {
    "active": "Active",
    "poc": "POC",
    "deprecated": "Deprecated",
    "planned": "Planned",
}
STATUS_DESCRIPTIONS = {
    "active": "Current approach, in use and maintained.",
    "poc": "Validated in a proof of concept or lab, not adopted as the standard yet.",
    "deprecated": "No longer current; may be superseded by another project or discontinued.",
    "planned": "Design, RFC or roadmap only; not implemented yet.",
}
ENVIRONMENT_LABELS = {
    "production": "Production",
    "non-production": "Non-production",
    "local": "Local",
}
ENVIRONMENT_DESCRIPTIONS = {
    "production": "Runs in production with real workloads or users.",
    "non-production": "Runs in development, staging or another non-production environment.",
    "local": "Runs on a local cluster, home lab or learning environment.",
}
KIND_LABELS = {
    "project": "Project",
    "standard": "Standard",
    "rfc": "RFC",
    "guide": "Guide",
    "index": "Index",
    "subpage": "Subpage",
}
CATEGORY_LABELS = {
    "ai": "AI",
    "analytics-engineering": "Analytics Engineering",
    "cloud-engineering": "Cloud Engineering",
    "data-engineering": "Data Engineering",
    "data-governance": "Data Governance",
    "data-streaming": "Data Streaming",
    "databases": "Databases",
    "devops": "DevOps",
    "finops": "FinOps",
    "management": "Management",
    "mlops": "MLOps",
    "network": "Network",
    "observability": "Observability",
    "platform-engineering": "Platform Engineering",
    "security": "Security",
    "site-reliability-engineering": "Site Reliability Engineering",
    "software-engineering": "Software Engineering",
}

STATUS_ORDER = ("active", "poc", "deprecated", "planned")
ENVIRONMENT_ORDER = ("production", "non-production", "local")


def _read_page(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    try:
        meta = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        print(f"error: {path}: invalid YAML frontmatter: {exc}", file=sys.stderr)
        sys.exit(1)
    if not isinstance(meta, dict):
        print(f"error: {path}: frontmatter must be a mapping", file=sys.stderr)
        sys.exit(1)
    return meta, text[match.end():]


def _page_title(body: str, path: Path) -> str:
    match = H1_RE.search(body)
    if match:
        return match.group(1).strip()
    return path.stem.replace("-", " ").title()


def _validate_meta(rel: str, meta: dict[str, Any]) -> None:
    if not meta:
        return
    has_status = "status" in meta
    has_kind = "kind" in meta
    if not has_status and not has_kind:
        return
    kind = meta.get("kind")
    if kind in {"index", "subpage"}:
        if has_status:
            print(f"error: {rel}: kind {kind!r} must not declare status", file=sys.stderr)
            sys.exit(1)
        if meta.get("environment"):
            print(f"error: {rel}: kind {kind!r} must not declare environment", file=sys.stderr)
            sys.exit(1)
        return
    if kind == "standard":
        if has_status:
            print(f"error: {rel}: kind standard must not declare status", file=sys.stderr)
            sys.exit(1)
        if meta.get("environment"):
            print(f"error: {rel}: kind standard must not declare environment", file=sys.stderr)
            sys.exit(1)
        return
    if not has_status or not has_kind:
        print(f"error: {rel}: status and kind must be declared together", file=sys.stderr)
        sys.exit(1)
    status = meta.get("status")
    if status not in STATUS_LABELS:
        print(
            f"error: {rel}: invalid status {status!r}; expected one of {', '.join(STATUS_ORDER)}",
            file=sys.stderr,
        )
        sys.exit(1)
    if kind not in KIND_LABELS:
        print(
            f"error: {rel}: invalid kind {kind!r}; expected one of {', '.join(KIND_LABELS)}",
            file=sys.stderr,
        )
        sys.exit(1)
    environment = meta.get("environment")
    if environment is not None and environment not in ENVIRONMENT_LABELS:
        print(
            f"error: {rel}: invalid environment {environment!r}; expected one of "
            f"{', '.join(ENVIRONMENT_ORDER)}",
            file=sys.stderr,
        )
        sys.exit(1)
    if kind != "project" and environment:
        print(f"error: {rel}: environment is only allowed for kind: project", file=sys.stderr)
        sys.exit(1)
    if kind == "project" and status in {"active", "poc"} and not environment:
        print(f"error: {rel}: active and POC projects require an environment", file=sys.stderr)
        sys.exit(1)
    if meta.get("superseded_by") and status != "deprecated":
        print(f"error: {rel}: superseded_by is only allowed for status: deprecated", file=sys.stderr)
        sys.exit(1)
    if meta.get("superseded_by_label") and not meta.get("superseded_by"):
        print(f"error: {rel}: superseded_by_label requires superseded_by", file=sys.stderr)
        sys.exit(1)


def _resolve_docs_path(source_rel: str, target: str) -> str:
    if target.startswith("/"):
        return posixpath.normpath(target.lstrip("/"))
    return posixpath.normpath(posixpath.join(posixpath.dirname(source_rel), target))


def _check_superseded(rel: str, meta: dict[str, Any]) -> str | None:
    target = meta.get("superseded_by")
    if not target:
        return None
    target_rel = _resolve_docs_path(rel, target)
    if target_rel.startswith("../") or target_rel == "..":
        print(f"error: {rel}: superseded_by must stay inside docs/", file=sys.stderr)
        sys.exit(1)
    if not (DOCS_DIR / target_rel).is_file():
        print(f"error: {rel}: superseded_by target not found: {target_rel}", file=sys.stderr)
        sys.exit(1)
    return target_rel


def _title_for(rel: str) -> str:
    path = DOCS_DIR / rel
    if not path.is_file():
        return rel
    meta, body = _read_page(path)
    return str(meta.get("title") or _page_title(body, path))


def _collect_projects() -> list[dict[str, Any]]:
    projects: list[dict[str, Any]] = []
    for path in sorted((DOCS_DIR / "portfolio").rglob("*.md")):
        rel = path.relative_to(DOCS_DIR).as_posix()
        if rel == "portfolio/catalog.md":
            continue
        meta, body = _read_page(path)
        if not meta:
            continue
        _validate_meta(rel, meta)
        if meta.get("kind") != "project":
            continue
        target_rel = _check_superseded(rel, meta)
        parts = rel.split("/")
        category_key = parts[1] if len(parts) > 2 else "portfolio"
        category = CATEGORY_LABELS.get(
            category_key, category_key.replace("-", " ").title()
        )
        label = meta.get("superseded_by_label")
        if target_rel and not label:
            label = _title_for(target_rel)
        projects.append(
            {
                "rel": rel,
                "title": str(meta.get("title") or _page_title(body, path)),
                "status": meta["status"],
                "environment": meta.get("environment"),
                "category": category,
                "superseded_by": target_rel,
                "superseded_by_label": label,
            }
        )
    return projects


def _url_for(docs_rel: str) -> str:
    if docs_rel.endswith("/README.md"):
        docs_rel = docs_rel[: -len("README.md")]
    elif docs_rel.endswith(".md"):
        docs_rel = docs_rel[: -len(".md")] + "/"
    return "/" + docs_rel.lstrip("/")


def _filter_chips(
    group: str,
    labels: dict[str, str],
    counts: Counter[str],
    order: tuple[str, ...],
    total: int,
) -> str:
    buttons = [
        '<button type="button" class="portfolio-filter__chip is-active" '
        'data-filter-value="all" aria-pressed="true">'
        f'All <span class="portfolio-filter__count">{total}</span></button>'
    ]
    for value in order:
        count = counts.get(value, 0)
        if not count:
            continue
        buttons.append(
            f'<button type="button" class="portfolio-filter__chip" '
            f'data-filter-value="{html.escape(value)}" aria-pressed="false">'
            f"{html.escape(labels[value])} "
            f'<span class="portfolio-filter__count">{count}</span></button>'
        )
    return (
        f'<div class="portfolio-filter" data-filter-group="{html.escape(group)}" '
        f'role="group" aria-label="Filter by {html.escape(group)}">'
        f'<span class="portfolio-filter__label">{html.escape(group.title())}</span>'
        + "".join(buttons)
        + "</div>"
    )


def _build_catalog_html() -> str:
    projects = _collect_projects()
    if not projects:
        return '<div class="portfolio-empty">No projects have status metadata yet.</div>'

    status_counts = Counter(project["status"] for project in projects)
    environment_counts = Counter(
        project["environment"]
        for project in projects
        if project["environment"]
    )
    status_chips = _filter_chips(
        "status", STATUS_LABELS, status_counts, STATUS_ORDER, len(projects)
    )
    environment_chips = _filter_chips(
        "environment",
        ENVIRONMENT_LABELS,
        environment_counts,
        ENVIRONMENT_ORDER,
        len(projects),
    )
    discipline_counts = Counter(project["category"] for project in projects)
    discipline_order = tuple(
        sorted(discipline_counts, key=lambda item: item.casefold())
    )
    discipline_chips = _filter_chips(
        "discipline",
        {value: value for value in discipline_order},
        discipline_counts,
        discipline_order,
        len(projects),
    )

    status_rank = {status: index for index, status in enumerate(STATUS_ORDER)}
    rows = []
    for project in sorted(
        projects,
        key=lambda item: (
            item["category"].casefold(),
            status_rank[item["status"]],
            item["title"].casefold(),
        ),
    ):
        replaced = "&mdash;"
        if project["superseded_by"]:
            url = _url_for(project["superseded_by"])
            label = html.escape(
                str(project["superseded_by_label"] or project["superseded_by"])
            )
            replaced = f'<a href="{html.escape(url, quote=True)}">{label}</a>'
        environment = project["environment"]
        environment_cell = (
            f'<span class="portfolio-badge portfolio-badge--env-{html.escape(environment)}">'
            f"{html.escape(ENVIRONMENT_LABELS[environment])}</span>"
            if environment
            else "&mdash;"
        )
        rows.append(
            f'<tr data-status="{html.escape(project["status"])}" '
            f'data-environment="{html.escape(environment or "")}" '
            f'data-discipline="{html.escape(project["category"])}">'
            f'<td><a href="{html.escape(_url_for(project["rel"]), quote=True)}">'
            f'{html.escape(project["title"])}</a></td>'
            f'<td>{html.escape(project["category"])}</td>'
            f'<td><span class="portfolio-badge portfolio-badge--{html.escape(project["status"])}" '
            f'title="{html.escape(STATUS_DESCRIPTIONS[project["status"]], quote=True)}">'
            f'{html.escape(STATUS_LABELS[project["status"]])}</span></td>'
            f"<td>{environment_cell}</td>"
            f"<td>{replaced}</td>"
            "</tr>"
        )

    return (
        '<div id="portfolio-catalog">'
        "<noscript><style>.portfolio-filters{display:none}</style></noscript>"
        '<div class="portfolio-filters">'
        f"{status_chips}{environment_chips}{discipline_chips}"
        "</div>"
        '<div class="portfolio-table-wrapper">'
        '<table class="portfolio-table">'
        "<thead><tr>"
        '<th scope="col">Project</th><th scope="col">Discipline</th>'
        '<th scope="col">Status</th><th scope="col">Environment</th>'
        '<th scope="col">Replaced by</th>'
        "</tr></thead>"
        f"<tbody>{''.join(rows)}</tbody>"
        "</table>"
        "</div>"
        '<p class="portfolio-no-results" role="status" aria-live="polite" hidden>'
        "No projects match the selected filters.</p>"
        "</div>"
    )


def main() -> None:
    catalog_text = CATALOG_PATH.read_text(encoding="utf-8")
    if CATALOG_PLACEHOLDER not in catalog_text:
        print(f"portfolio catalog already generated (no placeholder in {CATALOG_PATH})")
        return

    catalog_html = _build_catalog_html()
    new_text = catalog_text.replace(CATALOG_PLACEHOLDER, catalog_html)
    CATALOG_PATH.write_text(new_text, encoding="utf-8")
    print(f"generated portfolio catalog: {CATALOG_PATH}")


if __name__ == "__main__":
    main()
