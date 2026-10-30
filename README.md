# EPOCH bugs and improvements

A shared record of bugs and small improvements in
[official EPOCH](https://github.com/epochpic/epoch). Each entry says where
its fix or improvement is available. Changes in a separate
[EPOCH fork](https://github.com/ZheyuanChen/epoch_dev) are labelled as such.

## Use in Overleaf

Upload [`epoch_fixes_overleaf.zip`](epoch_fixes_overleaf.zip) as a new
Overleaf project and set `main.tex` as the main file. The archive contains
both short tables, the detailed entries and an editing guide. Sharing the
Overleaf project does not itself grant GitHub write access or synchronise
edits. This GitHub repository is public.

To add a bug, add one short `\BugRow` to `registry.tex` and a matching
numbered entry to `items.tex`. To add an improvement, add an
`\ImprovementRow` to `improvements_registry.tex` and a matching `I01`
entry to `improvements.tex`. The table descriptions wrap automatically;
keep long paths, links and tests in the detailed entries.
See [CONTRIBUTING.md](CONTRIBUTING.md) for examples.

## Colours and check date

- Green: fix or improvement is in official `main`.
- Yellow: fix or improvement is in the named official development branch.
- Purple: fix or improvement is in a separate EPOCH fork.
- Red: no fix is known, or an improvement is unavailable.
- Official `main` checked 30 October 2026 at
  `f294c484f76dff0777d5cc0d50b38506a2b049ff`.

These are code and Git-history checks, not new EPOCH simulation results.
The numerical NBW table generator is currently uncommitted in the local
fork; this limitation is recorded in improvement I01.

## Files and local build

- `main.tex`: page layout and coloured status flags.
- `registry.tex`, `items.tex`: short bug list and detailed bugs.
- `improvements_registry.tex`, `improvements.tex`: improvement list and details.
- `CONTRIBUTING.md`: copyable editing examples.
- `package.py`: checks that all table IDs have details, then builds the zip.
- `epoch_fixes_preview.pdf`: compiled preview.

After editing locally, compile `main.tex` with pdfLaTeX twice and run
`python3 package.py`. The zip contains no Git history, EPOCH source code,
manuscripts or local machine notes.
