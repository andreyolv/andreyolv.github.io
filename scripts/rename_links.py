#!/usr/bin/env python3
"""Replace old ``X.md`` links with directory URLs ``X/`` across docs.

After merging conflicting ``X.md`` pages into ``X/README.md`` (and deleting
``X.md``), every remaining link ``[text](...X.md)`` must become
``[text](...X/)`` so Zensical resolves them to the same destination the
``README.md`` now occupies.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"

# Names whose .md page was merged into a same-named README.md directory.
RENAMED = [
    "airflow",
    "self-hosted-actions",
    "cicd-terraform",
    "actions-centralization",
    "reloader",
]


def main() -> None:
    total_files = 0
    total_replacements = 0
    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        original = text
        for name in RENAMED:
            # Match ] ( optional/path/ )name.md  inside Markdown links
            pattern = re.compile(
                r"\]\(((?:[^)]*\/)?)" + re.escape(name) + r"\.md\)"
            )
            text, n = pattern.subn(lambda m: f"]({m.group(1)}{name}/)", text)
            total_replacements += n
        if text != original:
            md_file.write_text(text, encoding="utf-8")
            total_files += 1
            print(f"updated {md_file.relative_to(REPO_ROOT)}")
    print(f"\n{total_files} files updated, {total_replacements} link replacements.")


if __name__ == "__main__":
    main()
