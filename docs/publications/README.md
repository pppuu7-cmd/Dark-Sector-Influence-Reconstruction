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

1. `DSIR2_RECOVERY_AND_CONTINUATION_V0_4_2026-08-28.md`
2. `DSIR2_MANUSCRIPT_V0_4.md`
3. `../ARTICLE2_CLAIM_MATRIX_CURRENT.md` on `main`
4. `../ARTICLE2_CLAIM_MATRIX_V0_3_K1_REPRESENTATION_CONSOLIDATION.md` on `main`
5. `../ARTICLE2_FINAL_SCIENCE_CLOSURE_AUDIT_2026-08-28.md` on `main`
6. `../ARTICLE2_FINAL_FIGURE_TABLE_SPEC_V0_1.md` on `main`
7. `../DSIR_RAY_LINE_SUBSPACE_EQUIVALENCE_GEOMETRY_V0_1.md` on `main`
8. `DSIR2_TABLE_T2_ANGLE_HIERARCHY_V0_1.md` — historical K2-oriented/line table retained for audit.
9. `DSIR2_FIGURE_SOURCE_MANIFEST_V0_1.md` — earlier figure/provenance source map.
10. `DSIR2_LITERATURE_SCAFFOLD_V0_1.md` — bibliography/novelty starting point.

Historical Article-2 v0.1–v0.3 files are deliberately retained. They record the evolution from an initially stronger dynamic-separation interpretation, through Exp071L's two-sided K2 falsification, to Exp071M/N's representation-resolvability boundary and independent K1 nuisance-line falsification.

### DSIR-2 active title

*Dark-Sector Influence Reconstruction II: Falsifying Channel-Conditioned Specificity Across Static, Temporal, and Velocity Response Spaces*

### DSIR-2 current scientific status

Canonical main-branch verdict:

`ARTICLE2_SCIENTIFIC_EVIDENCE_CHAIN_CLOSED_FOR_DECLARED_SCOPE_V0_1`.

No additional K1/K2 or near-duplicate response-angle experiment is scientifically required before writing under the declared Article-2 scope unless a concrete audit defect is found.

This is a repository-for-writing closure, not submission readiness. Remaining work is manuscript assembly, verified bibliography/novelty audit, figures, provenance tables, sentence-level claim audit and exact release-candidate reproducibility audit.

### DSIR-2 current scientific boundary

The paper is a falsification hierarchy:

- K2 falsifies a dark-specific F30 matter-morphology interpretation;
- static Weyl/slip and matter+Weyl+slip add information but retain a GDM sound-speed-like ambiguity;
- positive K2 temporal/velocity rays are strongly separated under their preregistered oriented tests;
- positive K2 velocity separation survives amplitude and support controls;
- Exp071L restores K2 overlap when the physically two-sided nuisance line is used;
- Exp071M shows that K1 primordial tilt is exactly unresolved in transfer-only `t_tot`, so no angle exists there;
- Exp071N restores the missing primordial-power response and makes K1 resolvable, but its two-sided velocity-power nuisance line still overlaps both tested GDM directions at `36.06/37.85 deg`;
- theory/provider response geometry remains distinct from observational admissibility and covariance/nuisance quotienting.

The final hierarchy is:

`representation -> resolvability -> ray/line/subspace -> channel-conditioned equivalence -> physical support -> observational quotient`.

No dark-sector detection, unique fingerprint, tracer-RSD claim, survey distinguishability claim, covariance-whitened/nuisance-marginalized claim, or G7/G8/G9 promotion is permitted.

The previously suggested negative-K2 temporal analogue of Exp071H is now optional extension work, not a mandatory Article-2 science gate. Exp071H remains an oriented-ray result exactly as preregistered.

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
