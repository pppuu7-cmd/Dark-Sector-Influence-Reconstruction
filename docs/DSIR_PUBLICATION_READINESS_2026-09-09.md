# DSIR publication readiness ledger — 2026-09-09

Status: PROJECT-LEVEL TRACKING LEDGER. Scope: DSIR only.

This document operationalizes `docs/DSIR_PUBLICATION_ARCHITECTURE_2026-09-06.md` into explicit closure conditions for DSIR-1..DSIR-5.

## Meaning of 100%

`100% repository-ready for Article N` means the scientific/reproducibility evidence bundle required by the frozen scope of that article is complete enough to freeze a manuscript without relying on a downstream article's unresolved result. It does **not** mean the prose manuscript, figures, journal formatting, referee response, or publication process is complete.

Percentages below are deterministic checklist-closure indices, not confidence levels and not fractional scientific PASS. Scientific model gates continue to use only the frozen categorical statuses `PASS`, `FAIL`, `OUTSIDE_DOMAIN`, `NOT_YET_TESTABLE`, `NUMERICALLY_UNRESOLVED`.

## DSIR-1 — Framework

Frozen scope: model-agnostic framework and common residual/source representation; no complete-model PASS/FAIL claim required.

Closure checklist (5/5):

1. model-agnostic objective and three-layer architecture — CLOSED (`README.md`, `docs/DSIR_METHOD.md`);
2. common residual/source representation `X_munu=M0^2 G_munu-T_known_munu` — CLOSED (`docs/dsir4/DSIR4_COMMON_RESIDUAL_CONVENTION_V0_1.md`);
3. conservation/Bianchi/gauge bookkeeping — CLOSED for v0.1.1 scope (`G1=PASS` in `docs/GATES.md`);
4. response basis/conventions — CLOSED (`G2=PASS v0.1.1`);
5. claim hierarchy/publication separation and non-circularity boundary — CLOSED (`docs/DSIR_METHOD.md`, frozen publication architecture).

**Repository science-bundle readiness: 5/5 = 100%.**

Boundary: this does not claim that G0 is globally solver-independent, that the full observational funnel is complete, or that any cosmological model passes DSIR. Those are outside DSIR-1's frozen core claim.

## DSIR-2 — Inverse reconstruction / mathematical machinery

Frozen scope: inverse machinery, operators, validity/domain gates, representation rules, and mathematical infrastructure.

Closure checklist (5/6):

1. response representation and two-rank distinction (`R_obs`, `R_model`) — CLOSED;
2. covariance-whitened rank formalism and theory-prior sensitivity — CLOSED at method/implementation level;
3. quotient-before-law-discovery machinery — CLOSED at method level;
4. synthetic low-rank recovery — CLOSED (`G4=PASS`);
5. validity masks/common-subspace, missing-channel and family-balanced rules — CLOSED/IMPLEMENTED;
6. full G5 robustness program including data-whitened cross-family rank stress tests — OPEN (`G5=PARTIAL`).

**Repository science-bundle readiness: 5/6 = 83.3%.**

100% condition: close the remaining G5 data-whitened cross-family rank stress tests under frozen covariance/mask/family-prior rules and add a durable closure audit establishing that no required machinery claim depends on an untested coordinate/unit artifact.

## DSIR-3 — Observational implementation and complete funnel

For deterministic closure tracking, use the nine mandatory observational/model-comparison gates frozen in `DSIR4_MODEL_FUNNEL_MATRIX_CONTRACT_V0_1.md`. A representative mapped hypothesis may be used to validate funnel mechanics, but DSIR-3 is not a model-comparison paper.

Current C2 gate closure (3/9):

1. `G_DOMAIN_MAPPING` — PASS;
2. `G_ANGULAR_AUTHORITY` — PASS;
3. `G_ORDERED_JOIN` — PASS;
4. `G_RADIAL_SUPPORT` — NOT_YET_TESTABLE;
5. `G_PHYSICAL_SUPPORT` — downstream/unavailable;
6. `G_COV_WHITENING` — downstream/unavailable;
7. `G_NUISANCE_QUOTIENT` — downstream/unavailable;
8. `G_RELATION_NULL` — downstream/unavailable;
9. `G_FINAL_MODEL` — downstream/unavailable for full model comparison; for DSIR-3 closure the corresponding final observational/instrument validation must be frozen without turning the paper into DSIR-4.

**Mandatory-gate closure index: 3/9 = 33.3%.**

This low gate fraction should not be confused with code/infrastructure maturity: extensive angular-production authority and theory machinery already exist. The index intentionally measures only final prospectively admissible funnel closure.

Immediate blocker: `G_RADIAL_SUPPORT`. The exact DES-Y3 source payload is now immutably identified, including mirror commit/blob/size/SHA256, and a candidate WW weak-lensing LOS operator has been located. Exact DSIR source-bin provenance, WW compatibility, Wm physical radial identity/operator and exact coordinate coupling remain open.

100% condition: all observational stages required by the frozen DSIR-3 scope must have durable authority: ordered join; radial support; physical-support admissibility; covariance/whitening; nuisance quotient; relation/null machinery; final observational validation, with provenance and anti-shortcut rules intact.

## DSIR-4 — Existing-Model Funnel Matrix

Frozen scope: prospectively compare representative existing model classes through the same complete funnel before claiming a new model is required.

Project-level closure checklist (2/6):

1. matrix status semantics, mandatory gates and aggregation rule — CLOSED (`DSIR4_MODEL_FUNNEL_MATRIX_CONTRACT_V0_1.md`);
2. common residual/mapping contract and initial pilot inventory — CLOSED;
3. representative inventory mappings/prediction artifacts complete for the frozen target set — OPEN; C0/C1 analytic and extensive C2 mapping work exist, but the full representative inventory is not yet converted;
4. complete DSIR-3 observational funnel authority available — OPEN;
5. every frozen hypothesis/equivalence class evaluated through every mandatory admissible gate — OPEN;
6. final matrix interpretation/equivalence-class conclusion frozen without post-hoc threshold tuning — OPEN.

**Repository project-closure index: 2/6 = 33.3%.**

100% condition: complete DSIR-3 first, freeze and map the full representative existing-model inventory, run all mandatory gates for each frozen hypothesis, and freeze the final matrix/equivalence-class interpretation. `NOT_YET_TESTABLE` may remain a scientifically valid per-hypothesis outcome only when dictated by the frozen domain, but unavailable funnel machinery itself may not remain unresolved at publication closure.

## DSIR-5 — DSIR-derived new dark-sector model

Frozen scope: conditional new-model construction only if DSIR-4 demonstrates an empirically constrained gap or surviving equivalence class that requires new dynamics/discriminants.

Final-model eligibility checklist (0/6):

1. DSIR-4 scientific need/gap established — OPEN;
2. provenance-linked constraint skeleton `C1...Cn` frozen from DSIR results — NOT YET ELIGIBLE for final freeze;
3. evidence-specific `G_design` / `G_blind` split prospectively frozen — NOT YET ELIGIBLE;
4. minimal equations/action and parameterization frozen — NOT YET ELIGIBLE;
5. allowed fitting/calibration procedure frozen — NOT YET ELIGIBLE;
6. blind/external validation completed without model rescue — NOT YET ELIGIBLE.

**Final-model publication eligibility: 0/6 = 0%.**

This does not mean that conceptual/theory exploration has zero value. It means the frozen DSIR publication architecture deliberately forbids counting a final new-model paper as publication-ready before DSIR-4 answers whether a new model is scientifically needed. Constraint-skeleton and anti-circularity design work may proceed, but they do not close final-model eligibility.

100% condition: DSIR-4 must first establish the target residual/gap; then freeze a provenance-linked constraint skeleton, reserve blind evidence, construct/freeze the minimal dynamics and fitting rule, and pass the reserved blind/external validation without post-hoc rescue.

## Current dependency chain to 100%

The critical path is:

`DSIR-2 G5 closure` (independent machinery cleanup)

and

`DSIR-3 G_RADIAL_SUPPORT -> G_PHYSICAL_SUPPORT -> G_COV_WHITENING -> G_NUISANCE_QUOTIENT -> G_RELATION_NULL -> final observational validation`

then

`DSIR-4 complete model mappings -> all-model funnel runs -> matrix conclusion`

then, only if scientifically warranted,

`DSIR-5 constraint skeleton -> G_design/G_blind freeze -> minimal dynamics -> blind validation`.

## Rule for future progress reports

Every future DSIR iteration should report separately:

- DSIR-1 repository readiness;
- DSIR-2 repository readiness;
- DSIR-3 mandatory-gate closure;
- DSIR-4 project-closure readiness;
- DSIR-5 final-model eligibility;
- current task completion.

Do not replace scientific gate statuses by these percentages; the percentages are project-management closure indices only.
