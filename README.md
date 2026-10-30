# EPOCH issue and improvement register

A community-editable register of bugs and incremental numerical improvements in
[official EPOCH](https://github.com/epochpic/epoch). The official `main` branch
is the reference point. Changes that exist only in
[`epoch_dev`](https://github.com/ZheyuanChen/epoch_dev) are labelled explicitly.

## Work on Overleaf

Upload [`epoch_fixes_overleaf.zip`](epoch_fixes_overleaf.zip) as a new Overleaf
project and set `main.tex` as the main file. The archive contains the registry,
detailed items and editing guide. Sharing that Overleaf project does not grant
GitHub write access or automatically synchronise edits with this repository.
The GitHub repository itself is public.

To add a bug, edit one short row in `registry.tex` and a matching entry in
`items.tex`. The table keeps descriptions brief and wraps them automatically;
long paths, links, reproduction steps and caveats belong in the detailed item.
See [CONTRIBUTING.md](CONTRIBUTING.md) for a copyable example.

## Snapshot and evidence

- Official `main` checked 30 October 2026:
  `f294c484f76dff0777d5cc0d50b38506a2b049ff`.
- `Fixed` requires inclusion in official `main`. A PR merged into a development
  branch is `Dev only` until its fix reaches `main`.
- `Open` describes a stock-code issue that remains at the checked tip.
- `Baseline` describes an existing method with a documented alternative;
  `N/A` identifies a correction to a feature absent from stock EPOCH.
- This source audit does not claim new EPOCH builds or simulations. Table
  generators currently untracked in the local fork are flagged in the item.

## Files

- `main.tex`: layout, status convention and registry macros.
- `registry.tex`: short, linked rows; the easiest file for contributors to edit.
- `items.tex`: sources, symptoms, fixes, tests and limitations.
- `CONTRIBUTING.md`: editing and status-update instructions.
- `package.py`: regenerates the Overleaf zip from these sources.
- `epoch_fixes_preview.pdf`: a compiled preview.

Run `python3 package.py` after editing the source files. The Overleaf zip
contains no Git history, EPOCH source code, manuscripts or local machine notes.
