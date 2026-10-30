# Add an EPOCH bug or improvement

Keep each table row short. Put the explanation, sources and test in its
detailed entry. Credit the author of the cited fix or improvement in
the last column; name multiple contributors where appropriate.
Record bugs in official EPOCH, including ones whose only fix is in a
fork. Do not register a bug in a feature that exists only in a fork.
Check the official
[EPOCH `main`](https://github.com/epochpic/epoch) branch before changing a
flag, and record the branch and date you checked.

## Add a bug

1. Choose a new **number**, leaving retired IDs unused. Add a row in `registry.tex`:

```tex
\BugRow{15}{Short description of the bug}{\NoFix}{Contributor Name}
```

2. Add a matching entry in `items.tex`:

```tex
\subsection*{15. Short description of the bug}
\phantomsection\label{bug:15}
\textbf{When it happens.} Give the smallest failing case.

\textbf{Fix.} Link the commit or PR and name its branch.

\textbf{Test.} State how to reproduce and check the result.
```

For a serious bug, add `\subsubsection{...}` headings inside its
numbered entry. Use these coloured flags in the bug table:

| Flag | Meaning |
| --- | --- |
| `\FixMain` | Green: the fix is in official `main`. |
| `\FixDevel{4.20-devel}` | Yellow: the fix is in the named official development branch, but not `main`. Use the actual branch name. |
| `\FixFork` | Purple: the fix is in the linked [epoch_dev fork](https://github.com/ZheyuanChen/epoch_dev). Link its commit in the detail. |
| `\NoFix` | Red: no fix is known. |

## Add an improvement

Choose a new **I** number, leaving retired IDs unused. Add a short row to
`improvements_registry.tex` and a matching entry to `improvements.tex`:

```tex
\ImprovementRow{I08}{Short description of the improvement}{\InFork}{Contributor Name}

\subsection*{I08. Short description of the improvement}
\phantomsection\label{imp:I08}
Explain the method, where it is available, and how it was checked.
```

The improvement table uses `\InMain` (green),
`\InDevel{4.20-devel}` (yellow), `\InFork` (purple), or
`\NotAvailable` (red). Keep claims about performance or accuracy
next to a test or source. An improvement that changes numerical results
should name the option and data files a user must record.

## Keep the status honest

A PR merged into an official development branch is yellow until the
change reaches official `main`. A fix in a fork is purple even if the
same bug is present in official EPOCH. For an improvement available only
in a fork, say this explicitly in the detailed entry. Check the
official branch tip again when changing a flag.

Overleaf compiles `main.tex` with pdfLaTeX. In a local checkout of
this GitHub repository, run pdfLaTeX twice, then run
`python3 package.py` to update the zip. Overleaf edits do not update
GitHub unless you separately synchronise or upload them.
