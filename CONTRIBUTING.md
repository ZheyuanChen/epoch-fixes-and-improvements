# Contributing an EPOCH issue

Please check the official [`epochpic/epoch` `main`](https://github.com/epochpic/epoch)
branch before adding or changing a status. Record the commit and date used.
An item about a feature implemented only in another fork belongs in the
fork-specific group and must say so explicitly.

## Add a row and its detail

1. Choose the next unused `E` ID for stock EPOCH or `F` ID for a fork-only
   feature. Copy a single row in `registry.tex`, for example:

```tex
\RegistryRow{E10}{Short description of the new issue}{Open}
```

2. Add a matching detail in `items.tex`:

```tex
\subsection{E10: Short description of the new issue}
\label{item:E10}
\textbf{Trigger and failure.} State the smallest failing configuration.

\textbf{Status and evidence.} Link the official commit, PR or issue;
give the main tip checked and any fork-only correction.

\textbf{Verification.} Record a reproducible test and its result.
```

For a short fork-only entry, use `\ForkItem{F11}{Short title}` in `items.tex`
and add an `F11` row in `registry.tex`. Use subsections and subsubsections
for serious failures. Keep the registry row short; detailed URLs and paths
belong only in the item, so the table does not overflow.

## Status values

| Value | Meaning |
| --- | --- |
| `Fixed` | The correction is present in official `main`. |
| `Dev only` | The correction is in an official development branch, but absent from `main`. |
| `Open` | A stock-code defect or hazardous behaviour remains in `main`. |
| `Baseline` | Stock EPOCH intentionally uses an existing method; an improvement is documented. |
| `N/A` | The affected feature is absent from stock `main`; this is fork-specific work. |

Do not infer `Fixed` from a merged PR badge without checking its target branch
and whether that commit reached `main`. Prefer a direct reproducer or
source-level explanation over an unsupported claim of numerical impact.

## Build

Overleaf compiles `main.tex` with pdfLaTeX. In a local checkout of this
GitHub repository, run pdfLaTeX twice from the repository root, then run
`python3 package.py` to update the zip.
Commit the changed `.tex` files, zip and preview together if you maintain
those generated artefacts in GitHub. Overleaf edits do not update GitHub
unless you separately synchronise or upload them.
