# DSIR publication architecture

**Established:** 2026-08-27  
**Purpose:** make the research repository directly usable for a staged series of manuscripts without changing scientific gate semantics.

This directory is a manuscript-engineering layer over the scientific record. It does **not** replace `experiments/`, `data/derived/`, `docs/RESEARCH_LOG*`, `docs/RECOVERY*`, provenance files, or G1–G9.

## Directory contract

- `ARTICLE_SERIES_ROADMAP_V0_1.md` — proposed manuscript sequence and dependency graph.
- `ARTICLE_READINESS_LEDGER_V0_1.md` — explicit readiness criteria and current status for each paper.
- `ARTICLE_01_EVIDENCE_MAP_V0_1.md` — claim → experiment → machine-readable evidence map for the first DSIR paper.
- `RTK_DSIR_PUBLICATION_BOUNDARY_V0_1.md` — hard separation rules between the sibling RTK and DSIR research programs and the later comparative-paper interface.
- `RESEARCH_CHRONOLOGY_V0_1.md` — publication-facing chronology keyed to immutable commits/runs/artifacts.

Future manuscript directories should use

`docs/publications/article_XX/`

and may contain outlines, figure manifests, table manifests, bibliography notes and draft text. They must never become the primary location for raw scientific evidence.

## Scientific-source rule

Every manuscript-level quantitative statement must resolve to at least one of:

1. a preregistered numbered experiment plus result artifact;
2. a hard source/provenance theorem with pinned upstream code;
3. an explicitly labelled retrospective/descriptive analysis;
4. an observational data product with immutable provenance.

Publication notes may summarize those objects, but may not silently change their status.

## Failure semantics

Permanent FAIL, null and incomplete results stay visible in manuscript evidence maps. A paper may discuss why a route failed, but a publication document may not reclassify it.

## Discovery boundary

A paper may be ready for drafting before G7/G8/G9 if its claims are methodological/descriptive and explicitly avoid a dark-sector discovery claim. G7/G8/G9 remain the controlling gates for any claimed new residual law, withheld-family discovery or corresponding strong new-physics interpretation.
