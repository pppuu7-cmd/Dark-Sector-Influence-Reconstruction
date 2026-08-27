# DSIR RECOVERY LATEST — live pointer

**Date:** 2026-08-27  
**Stable historical manual:** `docs/RECOVERY_MANUAL.md`  
**Prior late-stage overlay:** `docs/RECOVERY_POST_EXP067E_2026-08-26.md`  
**C5 publication-era overlay:** `docs/RECOVERY_POST_EXP069F_PUBLICATION_2026-08-27.md`  
**Current active experiment:** `experiments/073o_public_realdata_finite_harmonic_wm_replacement_prereg_v0_1.md`

DSIR is independent of RTK. Preserve negative results, preregistration chronology and missing-domain masks. No RTK PASS can close a DSIR gate and no DSIR PASS can close an RTK gate.

## Current G7 scientific state

- C3 physical provider: certified by Exp070C.
- C5 physical provider: certified by Exp069H; raw-k provenance corrected/closed by Exp069I.
- Exp071A common physical provider support: PASS.
- The original ACT×unWISE observational route did not yield an admissible complete low-z/high-k linear route; later audits established the need for a different finite-support observational realization.
- BOSS finite true-k matrix mm component: 54/240 coordinates retained in the non-classifying component audit.
- KiDS configuration-space transformed Wm/WW route: absolute-response asymptotics supported non-normalizability in Exp073L.
- Exp073M identified a finite harmonic operator class candidate.
- Exp073N = `FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE`; no support fraction was computed.
- Exp073O is prospectively frozen and **ACTIVE / UNCLASSIFIED**.
- G7 OPEN.
- G8 OPEN.
- G9 OPEN.

## Exp073O current candidate audit

The preferred DES Y1 real-data harmonic GGL lineage was audited at

`hocamachoc/3x2hs_measurements@21e589a3cfc3e30f1b06a4636ccc2da8aceda5ab`.

Candidate-level outcome:

`REJECT_DES_Y1_CANDIDATE_ON_O3_EXACT_PUBLIC_INPUT_BINDING`

What is established:

- an explicit `y1metacal` real-data galaxy-shear path exists in the pinned source;
- it uses finite NaMaster ell bins, finite mode-coupling workspaces and `get_bandpower_windows()`;
- the Wm measurement remains signed through the direct galaxy-density × shear cross measurement;
- no GR closure or model/covariance weighting is required to make the angular operator finite.

Decisive blocker:

- the real-data Y1 branch reads site-local derived redMaGiC products `wcountsmap_zbin{i}.fits` and `maskmap.fits`;
- the audited pinned source contains readers but no public deterministic producer that reproduces those exact maps with frozen catalogue cuts, weights, mask semantics and pixelization;
- the exact source redshift-binning realization also must be prospectively checksum-bound.

Therefore O3 fails for this candidate. Public availability of the underlying catalogues is not sufficient under the frozen Exp073O contract.

This candidate rejection is **not** the global Exp073O classification. Do not declare `NO_PUBLIC_REALDATA...` until the frozen landscape search is completed sufficiently to support that statement.

Detailed record: `docs/EXP073O_DES_Y1_REALDATA_WM_SOURCE_AUDIT_2026-08-27.md`  
Machine-readable record: `data/derived/g7/exp073o_des_y1_realdata_wm_source_audit_v0_1.json`

## Frozen boundaries that remain unchanged

- common physical rectangle: `0.295 <= z <= 2.33`, `k <= 0.06664762008318016 Mpc^-1`;
- future physical-support threshold: `f_invalid <= 0.05`;
- future minimum retained dimension: `15`;
- Exp073N reproduction/provenance FAIL remains permanent;
- no support fractions may be computed inside Exp073O;
- covariance restriction/whitening is still closed;
- nuisance SVD/rank is still closed;
- quotient/relation/null is still closed;
- fresh G8 is still closed.

## Exact continuation order

1. Continue the already-frozen Exp073O public operator landscape search.
2. First priority: find a publicly immutable checksum-bindable realization or deterministic generator for the exact DES Y1 redMaGiC lens count/mask products and source redshift-bin inputs.
3. In parallel, audit another public real-data harmonic/pseudo-`C_ell` galaxy-shear release with finite bandpower windows/workspaces and exact public masks/binning/n(z).
4. For any candidate, apply O1–O8 exactly as frozen; reject candidate-level failures without changing thresholds.
5. Only if one candidate passes all O1–O8 may Exp073O be classified FOUND and a new support experiment be preregistered.
6. Only that later support experiment may compute `f_invalid` in the unchanged common rectangle.
7. Covariance/whitening remains forbidden until a full physical-support PASS.
8. Nuisance tangent rank/SVD, quotient/relation/null and then fresh G8 follow only in the established G7 order.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_POST_EXP067E_2026-08-26.md`
3. `docs/RECOVERY_POST_EXP069F_PUBLICATION_2026-08-27.md`
4. `docs/RECOVERY_LATEST.md`
5. `experiments/073o_public_realdata_finite_harmonic_wm_replacement_prereg_v0_1.md`
6. `docs/EXP073O_DES_Y1_REALDATA_WM_SOURCE_AUDIT_2026-08-27.md`
7. `data/derived/g7/exp073o_des_y1_realdata_wm_source_audit_v0_1.json`
