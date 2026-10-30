# EPOCH fixes and incremental improvements

This standalone public repository contains an editable status register and
its Overleaf package. Source-commit links point to the separate EPOCH fork
for provenance; this repository has its own history.

Upload `epoch_fixes_overleaf.zip` to Overleaf as a new project, then set
`main.tex` as the main file if Overleaf does not select it automatically.
The source uses pdfLaTeX and standard TeX Live packages. The separate
`epoch_fixes_preview.pdf` is a locally compiled preview, not required by
Overleaf.

## Scope and status method

- Checked on 30 October 2026 against official `epochpic/epoch` `main`
  `f294c484f76dff0777d5cc0d50b38506a2b049ff` and fork `spin`
  `b908c85911b314f6e07ed9a31caf0396612ffd83`.
- Verified the remote heads with `git ls-remote upstream refs/heads/main
  refs/heads/4.20-devel refs/heads/4.21-devel`.
- Used `git merge-base --is-ancestor <commit> upstream/main` for the
  official merge and inspected the named source, table or switch for
  fork-only corrections. A matching function name alone is not proof
  that the fix is equivalent.
- Official `4.20-devel` includes PR #906, but official `main` does not.
  Official `main` includes PR #896 through release v4.20.1.
- The register does not claim a fresh EPOCH build or simulation. Local
  uncommitted tests and table generator scripts are not part of this
  package; the generator scripts need committing for reproducibility.

The package contains no manuscript material or machine-specific notes.
Update the date, branch tips, and individual status entries together
when refreshing it.
