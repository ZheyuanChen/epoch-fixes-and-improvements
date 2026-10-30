#!/usr/bin/env python3
"""Check table links and build the source-only Overleaf archive."""

from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent
FILES = (
    "main.tex",
    "registry.tex",
    "items.tex",
    "improvements_registry.tex",
    "improvements.tex",
    "README.md",
    "CONTRIBUTING.md",
    "package.py",
)
OUTPUT = ROOT / "epoch_fixes_overleaf.zip"


def check_links(table: str, details: str, row_pattern: str, label_pattern: str) -> int:
    """Require one detail label for each table ID and no duplicate IDs."""
    rows = re.findall(row_pattern, (ROOT / table).read_text())
    labels = re.findall(label_pattern, (ROOT / details).read_text())
    if len(rows) != len(set(rows)) or len(labels) != len(set(labels)):
        raise SystemExit(f"Duplicate ID in {table} or {details}")
    if set(rows) != set(labels):
        missing = sorted(set(rows) - set(labels))
        extra = sorted(set(labels) - set(rows))
        raise SystemExit(
            f"{table} and {details} differ: missing={missing}, extra={extra}"
        )
    return len(rows)


bugs = check_links("registry.tex", "items.tex", r"\\BugRow\{(\d+)\}", r"\\label\{bug:(\d+)\}")
improvements = check_links(
    "improvements_registry.tex",
    "improvements.tex",
    r"\\ImprovementRow\{(I\d+)\}",
    r"\\label\{imp:(I\d+)\}",
)

with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as archive:
    for name in FILES:
        archive.write(ROOT / name, arcname=name)

print(
    f"{OUTPUT.name}: {bugs} bugs, {improvements} improvements, "
    f"{len(FILES)} source files"
)
