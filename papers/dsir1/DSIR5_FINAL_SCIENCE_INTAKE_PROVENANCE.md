# DSIR-I final DSIR5 science-intake provenance

**Date:** 2026-08-28  
**Purpose:** bind the final historical Paper-I science remainder — translator robustness and mixed C8/C9 prospective validation — to immutable evidence before release-candidate freeze.

This file supplements `PROVENANCE_MATRIX.md`. It does not alter any scientific status, threshold, or gate. The three records below have deliberately different evidence classes and must not be conflated.

## T1 — Cross-model translator robustness

**Manuscript-safe claim.** On the frozen C3 GDM-viscosity and C5 designer-`f(R)` amplitude rays, the sampled cross-model nearest-neighbour translator is local, multicoordinate, response-subspace conditional and non-bijective. Full-coordinate `C3 -> C5 -> C3` cycle closure is `2/5` for all `9/9` tested combinations of three common coordinate scalings and three standard `Lp` norms. Removing scale localization collapses the map to `1/5` closure in all `9/9` variants.

**Evidence class:** RETROSPECTIVE ROBUSTNESS AUDIT on immutable frozen summaries — **not prospective**.

**Canonical manuscript audit:**
- file: `papers/dsir1/CROSS_MODEL_TRANSLATOR_ROBUSTNESS_AUDIT_2026-08-28.md`;
- content blob SHA at intake: `37d30c008da42f54287db8e2ef24ebfcc7494534`.

**Immutable scientific inputs:**
- `data/derived/comparison_readiness/experiment_047a_finite_amplitude_interaction_curvature_v0_1_summary.json`;
- `data/derived/comparison_readiness/experiment_048b_finite_amplitude_localization_flow_v0_1_summary.json`;
- prior descriptive architecture record `docs/CROSS_MODEL_TRANSLATOR_LIGHTWEIGHT_AUDIT_2026-08-27.md`.

**Frozen coordinate:**

`q = [ln(k_geo), z_centroid, ln(chi_I)]`.

**Robustness family:**
- pooled z-score / pooled min-max / pooled median-MAD scaling;
- `L1` / `L2` / `Linf` norm;
- 9 full-coordinate variants and the corresponding coordinate-ablation controls.

**Key results:**
- full coordinate: exact `2/5` C3 cycle closure in `9/9` variants;
- `(ln k_geo, z_centroid)`: `2/5` in `9/9`;
- `(z_centroid, ln chi_I)`: `1/5` in `9/9`, all five C3 points map to `B0=1e-3`;
- `(ln k_geo, ln chi_I)`: `2/5` in `7/9`, `3/5` in `2/9`;
- large-amplitude `cv2=1e-4 -> B0=1e-3` endpoint stable in all `9/9` full-coordinate variants.

**Mandatory boundary:** no unique `cv2 <-> B0` identity; no universal scalar translator; no prospective observational validation; no covariance/nuisance quotient; no G7/G8/G9 evidence.

---

## T2 — C8 IDM-photon prospective half-transition FAIL

**Manuscript-safe claim.** A clean fresh C8 IDM-photon mechanism prospectively falsifies the endpoint-normalized half-transition sign relation that had only been qualified retrospectively on earlier families. All 35 model-redshift rows have a unique half-transition crossing, but two of four preregistered adjacent slopes have the wrong sign, and the same failed-pair pattern survives every one-redshift deletion.

**Evidence class:** HARD PROSPECTIVE FAIL.

**Preregistration / source-only ancestry:**
- Exp056A selected the C8 coupling grid from pinned CLASS source equations only, with no response contamination;
- complete Exp056B contract commit before first C8 matter-power response: `84d05ad72af1aea4fe3beadf071ee20cadf93c19`.

**Prospective science run:**
- workflow run: `32926084015`;
- workflow artifact: `9591561317`;
- artifact digest: `sha256:eb44e29725ace326e707d396158e7c4ed6fd4dccdd86d9ad18e67f42526750b1`;
- artifact head SHA: `7f4fcb38fa363bb980cf30d6211d5d66f64994ac`.

**Canonical result record:**
- `docs/GATE_UPDATE_EXP056B_F29_2026-08-26.md`;
- preserving commit: `effce92ec6292a7abe47321d3dfc2defbfe47363`.

**Frozen key result:**

`k50_geo = [0.0161297511, 0.0495901203, 0.0181843976, 0.0397209153, 0.0158358347] h/Mpc`

and

`C50 = [-7.80810676, +4.94852776, -3.05902403, +5.46614189]`.

Pairs 1->2 and 3->4 violate the preregistered strict-positive criterion. The same failed-pair pattern remains under all seven leave-one-redshift deletions.

**No-retuning boundary:** no coupling replacement, k/z deletion, alternate crossing definition, normalization change, sign change, or post-output acceptance-rule modification may rescue Exp056B v0.1.

**Mandatory interpretation boundary:** F29 is a prospective FAIL of this specified scalar relation, not a failure of DSIR response geometry. G7/G8/G9 remain OPEN.

---

## T3 — C9 IDM-baryon genuinely withheld multicoordinate PASS

**Manuscript-safe claim.** A genuinely withheld C9 IDM-baryon source family passes the preregistered two-coordinate localization-plus-shape path criterion frozen from C3/C5/C7/C8 before the first C9 matter-power response. All four adjacent standardized steps are nonzero above the frozen floor, the path has no nonadjacent intersection, and every leave-one-redshift operator rebuild independently passes.

**Evidence class:** HARD PROSPECTIVE PASS for the specified F30 multicoordinate path gate.

**Immutable preregistration ancestry:**
- Exp058A preregistered the 2D localization+shape path hypothesis before C9 existed as response evidence;
- Exp059A selected C9 = IDM-baryon source-only with `cross_idm_b={1e-30,1e-29,1e-28,1e-27,1e-26} cm^2`, `n_index_idm_b=0`, `m_idm=1e9 eV`;
- Exp060A froze the exact `(ell,q)` operator from C3/C5/C7/C8 only and passed the no-C9 contamination guard.

**Prospective science run:**
- workflow run: `32957427686`;
- workflow head SHA: `d2f9a91f156de30c4795a8fb053f64132ea75f07`;
- artifact: `9602537353`;
- artifact digest: `sha256:560f1fe127bfee1cd6fc14b91c455c11babf211a0854a37f6db30d6e5bbea6ed`.

**Canonical result record:**
- `docs/GATE_UPDATE_EXP061A_F30_2026-08-26.md`;
- result commit: `6a4c17d03342e442d75d37401f3cdc7be62dd5c0`.

**Frozen prospective gate:**
1. all four adjacent standardized path-step norms `>1e-10`;
2. no two nonadjacent polyline segments intersect under the frozen tolerance;
3. all seven leave-one-redshift operator rebuilds independently satisfy the same two conditions.

**Key result:**

`[0.43867499476052313, 2.9102332589802873, 5.761860689614482, 0.04774833503993949]`.

All four exceed `1e-10`; there are no nonadjacent intersections; all seven leave-one-redshift rebuilds pass.

**Mandatory interpretation boundary:** this is positive out-of-family evidence for the specified multicoordinate representation, not a universal dark-sector law, not a universal cross-model translator, and not a post-G7 G8 validation. F27 and F29 remain failed; G7/G8/G9 remain OPEN.

---

## Paper-I intake verdict

These three records close the historical Paper-I science remainder at the intended strength:

- translator: **retrospective, robustly non-bijective and subspace conditional**;
- C8: **fresh prospective scalar-law FAIL**;
- C9: **genuinely withheld multicoordinate prospective PASS**.

The scientifically important feature is the mixed outcome: Paper I preserves both failed and successful prospective generalizations without retroactive repair.

`PAPER1_DSIR5_FINAL_SCIENCE_INTAKE_PROVENANCE_BOUND_V0_1`

`G7=OPEN`, `G8=OPEN`, `G9=OPEN`.
