# DSIR-I JCAP LaTeX source provenance

**Date:** 2026-08-27  
**Status:** deterministic source-rendering baseline established; PDF compilation is a separate pending technical gate.

## First green JCAP `.tex` baseline

- paper source commit: `be5a649471e785eecc716ef17ca246c6c8411637`
- workflow: `DSIR-I paper build v0.2`
- workflow run: `33115618272`
- job: `98669380319`
- conclusion: `SUCCESS`
- build artifact: `9664364094`
- artifact digest: `sha256:493d57409a316250a9b6bfbd1e7aaa011cf44319142ff6d470368dc92d90c152`

The successful run established all of the following simultaneously:

1. deterministic `manuscript_v0_2.md` assembly;
2. JCAP front-matter audit;
3. formula/reference-free JCAP abstract candidate;
4. canonical AI-assisted-technology disclosure injection;
5. bibliography key-integrity audit;
6. deterministic Markdown-to-JCAP-LaTeX source rendering;
7. all scientific/support/provenance audits;
8. Figures 1--7 regeneration;
9. SHA256 build manifest and artifact packaging.

## Renderer contract

`papers/dsir1/build_jcap_latex.py` treats `manuscript_jcap_candidate.md` as the scientific text source and generates `papers/dsir1/jcap/dsir1_jcap.tex` in CI. It is deliberately not a general Markdown implementation. Unsupported syntax causes a FAIL instead of being guessed or silently dropped.

The renderer currently handles only syntax actually present in DSIR-I:

- section/subsection/subsubsection headings;
- display and inline LaTeX mathematics;
- Pandoc-style citation groups -> `\cite{...}`;
- inline code and bold emphasis;
- ordered/unordered lists;
- the three frozen main-manuscript Markdown tables, with column-count validation;
- all seven main figures, with captions sourced from `FIGURE_CAPTIONS.md` and stable semantic labels.

## Figure numbering rule

The original Markdown figure IDs reflect the historical generation sequence and are not in first-reference order. The JCAP rendering uses labels/references so journal figure numbers follow actual first appearance without changing the scientific identity of the source figure:

- historical Figure 1 -> `fig:operator`;
- historical Figure 4 -> `fig:channel`;
- historical Figure 2 -> `fig:additive`;
- historical Figure 3 -> `fig:hierarchy`;
- historical Figures 5--7 -> `fig:curvature`, `fig:failure`, `fig:support`.

The generated publication numbering is therefore sequential even though historical filenames remain unchanged for provenance.

## Table rendering rule

Exactly three Markdown tables are currently allowed in the main manuscript source:

1. family atlas -> `tab:atlas`;
2. representative `chi_I` values -> `tab:chiI`;
3. finite-amplitude `chi_I` envelopes -> `tab:chiI-envelopes`.

Any unexpected additional table, malformed separator, or inconsistent column count makes the renderer fail closed.

## Bibliography integrity at the baseline

The successful source-rendering run reported:

- 7 unique cited BibTeX keys;
- 12 citation-key occurrences;
- 24 unique entries in `references.bib`;
- no duplicate keys;
- no missing cited keys.

Bibliographic metadata completeness remains an editorial task distinct from citation-key integrity. The WDM Bode--Ostriker--Turok and Viel et al. records were subsequently upgraded to journal-grade metadata and will be included in the next green baseline.

## JCAP style boundary

The generated `.tex` expects:

```tex
\documentclass[11pt,a4paper]{article}
\pdfoutput=1
\usepackage{jcappub}
\usepackage{booktabs}
```

The JCAP/SISSA `jcappub.sty` source is redistributable under LPPL 1.3+ according to its header. **The current baseline proves source generation only. It does not yet prove that the submission archive compiles with a pinned JCAP style and bibliography style.**

A separate compile gate must therefore be completed before arXiv/JCAP release. That future gate must record the exact `jcappub.sty`, bibliography-style source or `.bbl`, TeX-engine identity, PDF hash, page count, and first-page abstract fit.

## Scientific boundary

JCAP rendering changes presentation only. It does not change:

- any response value;
- any scientific threshold;
- any PASS/FAIL/INCOMPLETE classification;
- any support/operator eligibility state;
- `G7=OPEN`, `G8=OPEN`, `G9=OPEN`.

Exp073R1 remains outside article claims until a completed frozen result exists and a deliberate first-paper scope decision is made.
