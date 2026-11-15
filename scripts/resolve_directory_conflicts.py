#!/usr/bin/env python3
"""Resolve mkdocs directory-URL conflicts for Zensical compatibility.

Zensical maps both ``X.md`` and ``X/README.md`` to the same destination
``X/index.html`` (directory URLs), which is a build error under ``--strict``.

For each conflicting pair, this script:
1. Copies the project frontmatter (status, environment, kind) from ``X.md``
   into ``X/README.md`` (replacing ``kind: index``).
2. Deletes ``X.md``.
3. Removes any self-reference link ``../X.md`` inside ``X/README.md``.

After running this, re-run link replacement (e.g. with sed) to update all
remaining ``X.md`` references to ``X/`` across the docs.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs" / "portfolio"

# Conflicts: directory name (contains both X.md and X/README.md)
CONFLICTS = [
    "data-engineering/airflow",
    "site-reliability-engineering/disaster-recovery",
    "devops/self-hosted-actions",
    "devops/cicd-terraform",
    "devops/actions-centralization",
    "devops/reloader",
    "databases/redis",
]

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def _parse_frontmatter(text: str) -> tuple[dict, str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, "", text
    import yaml

    meta = yaml.safe_load(match.group(1)) or {}
    return meta, match.group(1), text[match.end():]


def _build_frontmatter(meta: dict) -> str:
    lines = ["---"]
    for key in ("status", "environment", "kind"):
        if key in meta:
            lines.append(f"{key}: {meta[key]}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def main() -> int:
    import yaml

    for rel in CONFLICTS:
        md_path = DOCS_DIR / f"{rel}.md"
        readme_path = DOCS_DIR / rel / "README.md"

        if not md_path.is_file():
            print(f"skip {rel}: {md_path} not found", file=sys.stderr)
            continue
        if not readme_path.is_file():
            print(f"skip {rel}: {readme_path} not found", file=sys.stderr)
            continue

        # Read project frontmatter from X.md
        md_meta, _, md_body = _parse_frontmatter(md_path.read_text(encoding="utf-8"))
        project_meta = {
            k: md_meta[k]
            for k in ("status", "environment", "kind")
            if k in md_meta
        }
        if not project_meta:
            print(f"skip {rel}: no project frontmatter in {md_path}", file=sys.stderr)
            continue

        # Read index frontmatter from X/README.md
        readme_meta, readme_fm, readme_body = _parse_frontmatter(
            readme_path.read_text(encoding="utf-8")
        )

        # Merge: project frontmatter takes precedence
        merged_meta = {**readme_meta, **project_meta}
        # Ensure kind is project (not index)
        merged_meta["kind"] = "project"

        new_readme = _build_frontmatter(merged_meta) + readme_body

        # Remove self-reference link line ../X.md inside the README
        name = rel.split("/")[-1]
        self_ref_pattern = re.compile(
            r"^[ \t]*- \[.*\]\(\.\./" + re.escape(name) + r"\.md\)[ \t]*$",
            re.MULTILINE,
        )
        new_readme, n_subs = self_ref_pattern.subn("", new_readme)
        if n_subs:
            print(f"  removed self-reference line ../{name}.md in {readme_path}")

        readme_path.write_text(new_readme, encoding="utf-8")
        md_path.unlink()
        print(f"resolved {rel}: merged {md_path.name} into {readme_path}, deleted {md_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
