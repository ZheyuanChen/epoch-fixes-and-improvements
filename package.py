#!/usr/bin/env python3
"""Check registry links and build the source-only Overleaf archive."""

from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent
FILES = ("main.tex", "registry.tex", "items.tex", "README.md", "CONTRIBUTING.md", "package.py")
OUTPUT = ROOT / "epoch_fixes_overleaf.zip"

registry = (ROOT / "registry.tex").read_text()
items = (ROOT / "items.tex").read_text()
row_ids = re.findall(r"\\RegistryRow\{([EF]\d+)\}", registry)
detail_ids = re.findall(r"\\label\{item:([EF]\d+)\}", items)
detail_ids += re.findall(r"\\ForkItem\{([EF]\d+)\}", items)

if len(row_ids) != len(set(row_ids)):
    raise SystemExit("Duplicate registry ID")
if len(detail_ids) != len(set(detail_ids)):
    raise SystemExit("Duplicate detail ID")
if set(row_ids) != set(detail_ids):
    missing = sorted(set(row_ids) - set(detail_ids))
    extra = sorted(set(detail_ids) - set(row_ids))
    raise SystemExit(f"Registry/detail mismatch: missing={missing}, extra={extra}")

with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as archive:
    for name in FILES:
        archive.write(ROOT / name, arcname=name)

print(f"{OUTPUT.name}: {len(row_ids)} linked entries, {len(FILES)} source files")
