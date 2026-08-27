# DSIR RECOVERY LATEST — live pointer

**Date:** 2026-08-27  
**Stable historical manual:** `docs/RECOVERY_MANUAL.md`  
**Prior late-stage overlays:** `docs/RECOVERY_POST_EXP067E_2026-08-26.md`, `docs/RECOVERY_POST_EXP069F_PUBLICATION_2026-08-27.md`  
**Current detailed overlay:** `docs/RECOVERY_POST_EXP069H_2026-08-27.md`  
**Current protocol:** `experiments/069i_exp069h_raw_k_unit_provenance_audit_prereg_v0_1.md`  
**Publication state:** `docs/publications/ARTICLE_READINESS_LEDGER_V0_1.md`

DSIR is independent of RTK. Preserve negative results, preregistration chronology and missing-domain masks. No RTK PASS can close a DSIR gate and no DSIR PASS can close an RTK gate. No hidden/common RTK↔DSIR dark-sector statistic is authorized.

## Current scientific state

- G1 PASS.
- G2 PASS.
- G3A/G3B PASS block-aware.
- G4 PASS synthetic recovery.
- C3 physical provider: **CERTIFIED** by Exp070C.
- C5 physical provider: **CERTIFIED** by Exp069H under Exp069G.
- common physical support-validity mask: **NOT YET APPLIED**.
- immediate barrier: Exp069I raw-k unit/provenance audit before any C5 raw coordinate enters support selection.
- G7 OPEN.
- G8 OPEN.
- G9 OPEN.

## Immutable newest C5 facts

- Exp069B remains permanent FAIL at its frozen `5e-6` q=1 exact-zero target criterion.
- Exp069F remains `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`; q=2 first formal target PASS, q=3 first tested point with target and raw both below `5e-6`.
- Exp069G minimum provider contract remains binding.
- Exp069H run `33024638764`, artifact `9628053962`, digest `sha256:fa61b504d31edeba2afcbed0f4b14bda688df82a96d2cba55eac034682b5382f`.
- Exp069H classification: `PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1`.
- exact-zero target/raw maxima: `1.7011186858522977e-6` / `2.8421302380756537e-6`, each below `5e-6`.
- tiny-positive `B0={1e-12,1e-10,1e-8}` continuity target/raw maxima are all `0.0` in the returned arrays.
- production `B0=1e-6` target signal: `0.013249122882007408 >= 1e-3`.
- independent zero rerun target/raw differences: `0.0` / `0.0`.
- signed-cross/accessor semantics PASS; every frozen target `P_Wm` cell is negative in every stored fresh case.

## Raw-k provenance barrier

Exp069H's historical raw-grid field is named `raw_k_Mpc^-1`, but its raw accessor omitted the `k_hunit` argument. In the pinned upstream source, that argument defaults to `True`, with `kh=ks/(H0/100)`; explicit physical k requires `k_hunit=False`.

The target-grid provider PASS is not affected because its interpolator explicitly used `k_hunit=False`. The same-node raw ratios are dimensionless on identical raw nodes, but the mislabeled coordinate must not enter physical support selection.

Exp069I prospectively freezes source/default binding, `k_default*h -> k_physical` closure at `5e-14`, exact raw-power/residual invariance, unchanged `5e-6` physical target/raw provider scales, and a corrected future schema. No support mask is authorized before Exp069I PASS.

## Current interpretation

Matter-only response geometry is a mechanism/transfer-shape taxonomy, not a unique dark-sector signature. Exp071C/071D show that a nearly one-dimensional response path can backtrack and that ordinary known-sector controls can satisfy the same normalized-path behavior. Stronger specificity requires independent matter/Weyl/slip/observational structure after covariance and nuisance treatment.

No universal residual law, no new fundamental law and no dark-sector discovery claim is currently authorized.

## Publication readiness

- **DSIR-1 observable-response geometry: READY_FOR_DRAFTING.**
- DSIR-2 remains NOT_READY because corrected physical-k provenance/common support binding is incomplete despite both C3 and C5 providers now being certified.
- DSIR-3 remains blocked by support/covariance/nuisance/G7.
- DSIR-4 remains blocked by fresh G8.
- RTK–DSIR synthesis remains blocked until independently mature records exist in both projects.

## Exact continuation order

1. Execute only the already-preregistered Exp069I unit/provenance audit.
2. Preserve PASS/FAIL/INCOMPLETE semantics exactly.
3. On PASS only: preregister common C3+C5 physical support-validity mask using explicit physical-k C5 semantics.
4. Apply the mask under its frozen rule.
5. Restrict/rebuild covariance/whitener only after support binding.
6. Freeze nuisance SVD/rank rule before quotienting.
7. Execute G7 quotient/relation/null.
8. Use a genuinely fresh family for G8 only after G7 is frozen.
9. In parallel, prepare DSIR-1 manuscript figures/tables from the existing evidence map without importing unresolved G7/G8 claims or RTK evidence.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_POST_EXP067E_2026-08-26.md`
3. `docs/RECOVERY_POST_EXP069F_PUBLICATION_2026-08-27.md`
4. `docs/RECOVERY_POST_EXP069H_2026-08-27.md`
5. `docs/publications/RESEARCH_CHRONOLOGY_V0_1.md`
6. `docs/publications/ARTICLE_READINESS_LEDGER_V0_1.md`
7. current experiment/result file
