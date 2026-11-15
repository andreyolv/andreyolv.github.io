"""Portfolio status metadata, badges and catalog generation.

Project pages opt in with YAML frontmatter:

    ---
    status: active
    environment: production
    kind: project
    ---

The hook validates the metadata, injects a status badge below the page title and
builds the filterable catalog at docs/portfolio/catalog.md.
"""

from __future__ import annotations

import html
import posixpath
import re
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

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

CATALOG_PATH = "portfolio/catalog.md"
CATALOG_PLACEHOLDER = "<!-- portfolio-catalog -->"
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def _read_page(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    try:
        meta = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"{path}: invalid YAML frontmatter: {exc}") from exc
    if not isinstance(meta, dict):
        raise ValueError(f"{path}: frontmatter must be a mapping")
    return meta, text[match.end() :]


def _page_title(body: str, path: Path) -> str:
    match = H1_RE.search(body)
    if match:
        return match.group(1).strip()
    return path.stem.replace("-", " ").title()


def _resolve_docs_path(source_rel: str, target: str) -> str:
    if target.startswith("/"):
        return posixpath.normpath(target.lstrip("/"))
    return posixpath.normpath(posixpath.join(posixpath.dirname(source_rel), target))


def _url_for(docs_rel: str) -> str:
    """Return the public URL for a docs-relative page path."""
    if docs_rel.endswith("/README.md"):
        docs_rel = docs_rel[: -len("README.md")]
    elif docs_rel.endswith(".md"):
        docs_rel = docs_rel[: -len(".md")] + "/"
    return "/" + docs_rel.lstrip("/")


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
            raise ValueError(f"{rel}: kind {kind!r} must not declare status")
        if meta.get("environment"):
            raise ValueError(f"{rel}: kind {kind!r} must not declare environment")
        return
    if not has_status or not has_kind:
        raise ValueError(f"{rel}: status and kind must be declared together")
    status = meta.get("status")
    if status not in STATUS_LABELS:
        raise ValueError(
            f"{rel}: invalid status {status!r}; expected one of {', '.join(STATUS_ORDER)}"
        )
    if kind not in KIND_LABELS:
        raise ValueError(
            f"{rel}: invalid kind {kind!r}; expected one of {', '.join(KIND_LABELS)}"
        )
    environment = meta.get("environment")
    if environment is not None and environment not in ENVIRONMENT_LABELS:
        raise ValueError(
            f"{rel}: invalid environment {environment!r}; expected one of "
            f"{', '.join(ENVIRONMENT_ORDER)}"
        )
    if kind != "project" and environment:
        raise ValueError(f"{rel}: environment is only allowed for kind: project")
    if kind == "project" and status in {"active", "poc"} and not environment:
        raise ValueError(f"{rel}: active and POC projects require an environment")
    if meta.get("superseded_by") and status != "deprecated":
        raise ValueError(f"{rel}: superseded_by is only allowed for status: deprecated")
    if meta.get("superseded_by_label") and not meta.get("superseded_by"):
        raise ValueError(f"{rel}: superseded_by_label requires superseded_by")


def _check_superseded(rel: str, meta: dict[str, Any], docs_dir: Path) -> str | None:
    target = meta.get("superseded_by")
    if not target:
        return None
    target_rel = _resolve_docs_path(rel, str(target))
    if target_rel.startswith("../") or target_rel == "..":
        raise ValueError(f"{rel}: superseded_by must stay inside docs/")
    if not (docs_dir / target_rel).is_file():
        raise ValueError(f"{rel}: superseded_by target not found: {target_rel}")
    return target_rel


def _title_for(docs_dir: Path, rel: str) -> str:
    path = docs_dir / rel
    if not path.is_file():
        return rel
    meta, body = _read_page(path)
    return str(meta.get("title") or _page_title(body, path))


def _collect_projects(docs_dir: Path) -> list[dict[str, Any]]:
    projects: list[dict[str, Any]] = []
    for path in sorted((docs_dir / "portfolio").rglob("*.md")):
        rel = path.relative_to(docs_dir).as_posix()
        if rel == CATALOG_PATH:
            continue
        meta, body = _read_page(path)
        if not meta:
            continue
        _validate_meta(rel, meta)
        if meta.get("kind") != "project":
            continue
        target_rel = _check_superseded(rel, meta, docs_dir)
        parts = rel.split("/")
        category_key = parts[1] if len(parts) > 2 else "portfolio"
        category = CATEGORY_LABELS.get(
            category_key, category_key.replace("-", " ").title()
        )
        label = meta.get("superseded_by_label")
        if target_rel and not label:
            label = _title_for(docs_dir, target_rel)
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


def _badge_html(
    status: str, environment: str | None, kind: str, legend_url: str
) -> str:
    parts = [
        f'<span class="portfolio-badge portfolio-badge--{html.escape(status)}" '
        f'title="{html.escape(STATUS_DESCRIPTIONS[status], quote=True)}">'
        f"{html.escape(STATUS_LABELS[status])}</span>"
    ]
    if environment:
        parts.append(
            f'<span class="portfolio-badge portfolio-badge--env-{html.escape(environment)}" '
            f'title="{html.escape(ENVIRONMENT_DESCRIPTIONS[environment], quote=True)}">'
            f"{html.escape(ENVIRONMENT_LABELS[environment])}</span>"
        )
    if kind != "project":
        parts.append(
            f'<span class="portfolio-badge portfolio-badge--kind">'
            f"{html.escape(KIND_LABELS[kind])}</span>"
        )
    parts.append(
        f'<a class="portfolio-page-status__legend" '
        f'href="{html.escape(legend_url, quote=True)}">Status guide</a>'
    )
    return '<div class="portfolio-page-status">' + "".join(parts) + "</div>"


def _deprecated_html(meta: dict[str, Any], rel: str, docs_dir: Path) -> str:
    target = meta.get("superseded_by")
    if not target:
        return ""
    target_rel = _resolve_docs_path(rel, str(target))
    label = meta.get("superseded_by_label") or _title_for(docs_dir, target_rel)
    link = posixpath.relpath(target_rel, posixpath.dirname(rel))
    return (
        '!!! warning "Deprecated"\n'
        f"    This project was superseded by [{label}]({link}). "
        "The page is kept for historical context.\n"
    )


def _insert_after_h1(markdown: str, block: str) -> str:
    match = H1_RE.search(markdown)
    if not match:
        return block + "\n\n" + markdown
    return (
        markdown[: match.end()]
        + "\n\n"
        + block
        + "\n\n"
        + markdown[match.end() :].lstrip("\n")
    )


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


def _build_catalog_html(docs_dir: Path) -> str:
    projects = _collect_projects(docs_dir)
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


def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri
    if not src.startswith("portfolio/"):
        return markdown

    docs_dir = Path(config["docs_dir"])
    meta = page.meta or {}

    if src == CATALOG_PATH:
        if CATALOG_PLACEHOLDER not in markdown:
            raise ValueError(f"{src}: missing {CATALOG_PLACEHOLDER}")
        return markdown.replace(CATALOG_PLACEHOLDER, _build_catalog_html(docs_dir))

    if not meta:
        return markdown

    _validate_meta(src, meta)
    if meta.get("superseded_by"):
        _check_superseded(src, meta, docs_dir)
    status = meta.get("status")
    kind = meta.get("kind")
    if not status or not kind:
        return markdown

    block = _badge_html(status, meta.get("environment"), kind, _url_for(CATALOG_PATH))
    if status == "deprecated":
        warning = _deprecated_html(meta, src, docs_dir)
        if warning:
            block += "\n\n" + warning

    return _insert_after_h1(markdown, block)
