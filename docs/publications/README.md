# DSIR publication architecture

**Established:** 2026-08-27  
**Updated:** 2026-08-28  
**Purpose:** make the research repository directly usable for a staged series of manuscripts without changing scientific gate semantics.

This directory is a manuscript-engineering layer over the scientific record. It does **not** replace `experiments/`, `data/derived/`, `docs/RESEARCH_LOG*`, `docs/RECOVERY*`, provenance files, or G1–G9.

## Directory contract

- `ARTICLE_SERIES_ROADMAP_V0_1.md` — proposed manuscript sequence and dependency graph.
- `ARTICLE_READINESS_LEDGER_V0_1.md` — original explicit readiness criteria and 2026-08-27 status snapshot.
- `ARTICLE_01_EVIDENCE_MAP_V0_1.md` — claim → experiment → machine-readable evidence map for the first DSIR paper.
- `RTK_DSIR_PUBLICATION_BOUNDARY_V0_1.md` — hard separation rules between the sibling RTK and DSIR research programs and the later comparative-paper interface.
- `RESEARCH_CHRONOLOGY_V0_1.md` — publication-facing chronology keyed to immutable commits/runs/artifacts.

## DSIR-2 active manuscript package

For a fresh chat/session continuing Article 2, read in this order:

1. `DSIR2_RECOVERY_AND_CONTINUATION_V0_2_2026-08-28.md`
2. `DSIR2_MANUSCRIPT_V0_2.md`
3. `../ARTICLE2_CLAIM_MATRIX_V0_2.md`
4. `DSIR2_FIGURE_SOURCE_MANIFEST_V0_1.md`
5. `ARTICLE2_READINESS_UPDATE_2026-08-28.md`
6. `../ARTICLE2_TOTAL_VELOCITY_PROVIDER_CONTRACT_2026-08-28.md`

Historical Article-2 v0.1 files are deliberately retained. They record the earlier interpretation before Exp071J/K/L, especially the later two-sided Exp071L falsification that narrowed the velocity-specificity claim.

### DSIR-2 active title

*Dark-Sector Influence Reconstruction II: Falsifying Channel-Conditioned Specificity Across Static, Temporal, and Velocity Response Spaces*

### DSIR-2 current drafting boundary

DSIR-2 is `READY_FOR_DRAFTING`, not ready for submission. The central paper is a falsification hierarchy: known-sector matter morphology defeats a dark-specific F30 interpretation; richer static channels retain a sound-speed-like ambiguity; positive/oriented temporal and velocity tangents strongly separate; positive velocity separation survives amplitude/support controls; but a fresh negative K2 displacement makes the physically two-sided velocity nuisance line overlap both tested GDM directions. No dark-sector detection, unique fingerprint, tracer-RSD claim, survey distinguishability claim, or G7/G8/G9 promotion is permitted.

The highest-value open Article-2 specificity control is a prospectively frozen **negative-K2/two-sided temporal analogue of Exp071H**. Until it exists, the current temporal result must remain labelled positive/oriented.

## Manuscript location convention

Future larger manuscript subpackages may use `docs/publications/article_XX/`. Existing top-level publication files remain valid and should not be moved merely for cosmetic consistency if moving them would break recovery references or provenance history.

## Scientific-source rule

Every manuscript-level quantitative statement must resolve to at least one of:

1. a preregistered numbered experiment plus result artifact;
2. a hard source/provenance theorem with pinned upstream code;
3. an explicitly labelled retrospective/descriptive analysis;
4. an observational data product with immutable provenance.

Publication notes may summarize those objects, but may not silently change their status.

## Failure semantics

Permanent FAIL, null and incomplete results stay visible in manuscript evidence maps. A paper may discuss why a route failed, but a publication document may not reclassify it. `INVALID_FOR_SCIENCE` must remain distinct from a physical FAIL.

## Discovery boundary

A paper may be ready for drafting before G7/G8/G9 if its claims are methodological/descriptive and explicitly avoid a dark-sector discovery claim. G7/G8/G9 remain the controlling gates for any claimed new residual law, withheld-family discovery or corresponding strong new-physics interpretation.
