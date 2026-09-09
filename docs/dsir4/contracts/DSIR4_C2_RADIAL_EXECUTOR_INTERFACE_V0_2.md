# DSIR-4 C2 radial executor interface v0.2 — broad-row compatibility correction

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVE INTERFACE FREEZE BEFORE ANY REAL EXP073IM OUTPUT IS INSPECTED.

This v0.2 supersedes only the row-level scalar `z`, scalar `k_Mpc^-1`, and row-level `final_response_abs_values` handoff clauses of `DSIR4_C2_RADIAL_EXECUTOR_INTERFACE_V0_1.md`. All upstream authority, DES-Y1 payload, observation semantics, fail-closed rules, downstream firewall, and scientific radial PASS/FAIL separation remain unchanged.

The correction is required by the earlier prospectively frozen Article-3 broad-row architecture in `docs/ARTICLE3_BROAD_ROW_LAYERB_SCHEMA_AMENDMENT_2026-08-30.md` and `docs/ARTICLE3_LAYERA_FACTORIZED_DES_SUPPORT_EVALUATOR_2026-08-30.md`, which explicitly forbid assigning one effective `ell`, `z`, or `k` to a broad DES pseudo-C_ell observation row.

## 1. Immutable upstream authority

Consume exactly the admitted C2 ordered angular authority and slot order:

`Wm_S0, Wm_S1, Wm_S2, Wm_S3, WW_S0_S0, WW_S0_S1, WW_S0_S2, WW_S0_S3, WW_S1_S1, WW_S1_S2, WW_S1_S3, WW_S2_S2, WW_S2_S3, WW_S3_S3`.

Authority file: `docs/dsir4/authority/EXP073IL_C2_ORDERED_JOIN_AUTHORITY_V0_1.json`.

The exact 14 angular byte authorities admitted by `EXP073IM_ANGULAR_BYTE_AUTHORITY_MATERIALIZATION_AUDIT_V0_1.md` must be verified before a classifying real run. Missing, substituted, duplicated, permuted, or recomputed authority is invalid-for-science rather than a scientific radial FAIL.

## 2. Exact radial authority

Bind the already-frozen Exp073Z2 stable-direct radial authority:

- run `33279208949`;
- job `99171355322`;
- artifact `9722468056`;
- artifact digest `sha256:3eb8b025711e8df6d5452a3a57002f36c9d7de2b9116734b71d15d6822dd20be`;
- positive token `PASS_EXP073Z2_DES_RADIAL_KERNEL_STABLE_DIRECT_V0_2`;
- `chi_Mpc` canonical SHA256 `e1f9a72fbe35140b984a56fc9e3b6f659082de9f9b45fc1a2e7e557e30783987`, shape `[2001]`;
- source-efficiency canonical SHA256 `a9b7b1b8c3e3f9f926e2d7786b13490109caf0aeff359dd3230f924955efd2ac`, shape `[4,2001]`;
- Wm radial canonical SHA256 `414f47620071c1df6c23abe25d45312796af53a37102c34e1d844308d915efe1`, shape `[20,2001]`;
- WW radial canonical SHA256 `56edaaf9ef6b03d00e7b83f158b204fc27171bef34a6a7bf3afbd8c71ed5cc0e`, shape `[10,2001]`.

The released DES-Y1 source/lens payload hashes and `dz=0` semantics remain exactly those frozen in v0.1 and Exp073IM preregistration. DES-Y3 substitution remains forbidden.

## 3. Observation-row expansion

The 14 angular slots are angular authorities, not the final count of DES observation rows.

Expand them deterministically as follows:

- each `Wm_Si` angular slot is reused across the five frozen DES-Y1 lens redshift bins, yielding `4 source bins x 5 lens bins x 39 released bandpowers = 780` Wm rows;
- each unordered `WW_Si_Sj` slot contributes `39` released bandpowers, yielding `10 x 39 = 390` WW rows;
- total DES broad observation rows: exactly `1170`.

This is the same Wm/WW block cardinality already frozen by Exp073U. The inherited block order is Wm first, then WW; inside each block use the already-frozen source/lens/pair identity and released bandpower order. No amplitude, covariance, nuisance, relation/null, or result-dependent ordering is allowed.

## 4. Broad-row radial handoff — no scalarization

A DES observation row is a broad finite survey coordinate. It MUST NOT receive row-level effective `ell`, effective `z`, effective `k`, weighted-mean `k`, midpoint `k`, centroid `k`, or any other scalar support proxy.

For each of the 1170 rows, emit a deterministic factorized broad-support descriptor containing at minimum:

- immutable `coordinate_id`;
- inherited unique non-negative `ordinal`;
- `block` = `Wm` or `WW`;
- angular `slot`;
- `band_index` in `0..38`;
- for Wm, exact `lens_bin` in `0..4` and `source_bin` in `0..3`;
- for WW, exact unordered `(source_bin_i, source_bin_j)` with `i<=j`;
- angular logical-array authority SHA256;
- radial logical-array authority SHA256 and exact radial row index;
- `z_fine`/geometry authority identity and `chi_Mpc` SHA256;
- exact observation-code/runtime provenance;
- explicit `representation = FACTORIZED_BROAD_SUPPORT_V0_2`.

The scientific broad support represented by a DES row is

`A_q(ell,z) = abs(W_q[band,ell]) * B_q(z)`

for support bookkeeping, with the measured Wm observable remaining signed. The physical-support stage may evaluate this representation directly using the already-frozen factorized Layer-A evaluator; materializing the enormous ell-by-z Cartesian product is not required.

## 5. Separation from physical-support stages

Exp073IM scores radial/LOS constructibility only. It does not score Layer A or Layer B.

Therefore Exp073IM MUST NOT:

- calculate `operator_f_invalid` or compare it to `0.05`;
- filter rows by the Article-3 physical rectangle;
- invent row-level `z`/`k` labels;
- require or score Layer-B `final_response_abs_values`;
- read covariance/whitening, nuisance/SVD/rank, relation/null, G7/G8, or article-selection information.

After a radial PASS, the next physical-support execution uses the frozen dual hierarchy:

1. Layer A broad operator leakage on the factorized support, threshold `f_op <= 0.05`;
2. Layer B common-response validity on the inherited Layer-A-retained broad rows, invalid-row fraction `<=0.05`, minimum retained observation-row dimension `15`.

No threshold is changed by this v0.2 correction.

## 6. Real G_RADIAL_SUPPORT PASS criterion

A real `PASS_EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_2` may be emitted only if all of the following hold:

1. all 14 admitted angular byte authorities verify exactly;
2. Exp073Z2 radial authority verifies exactly, including logical array dtype/shape/SHA identities;
3. deterministic expansion produces exactly 780 Wm + 390 WW = 1170 unique rows;
4. every Wm row binds one finite, non-empty, non-negative radial kernel from the frozen `[20,2001]` Wm authority and every WW row binds one from `[10,2001]` WW authority;
5. every required radial-kernel normalization is finite and strictly positive;
6. the frozen 2001-node radial/geometry representation is finite, ordered, and compatible with the pinned `k=(ell+1/2)/chi(z)` bookkeeping without evaluating the downstream physical cut;
7. all coordinate IDs and ordinals are unique and deterministic;
8. canonical replay or input-container permutation produces an identical ordered broad-row manifest digest;
9. no forbidden scalarization, interpolation/smoothing/rebinning, fiducial-P weighting, or downstream information is read;
10. the output is sufficient for the already-frozen factorized Article-3 Layer-A evaluator without rebuilding or outcome-conditioned narrowing.

A scientific radial FAIL is allowed only when exact provenance/interface checks pass but a mandatory frozen radial kernel is genuinely empty, zero-normalization, or non-finite such that the corresponding mandatory broad observation rows cannot be constructed.

Payload/hash/schema/provenance mismatch, missing artifacts, dependency interruption, or unauthorized substitution remain `INVALID_FOR_SCIENCE_EXP073IM` or `INCOMPLETE_EXP073IM`, not scientific FAIL.

## 7. Required pre-real QA additions

In addition to the v0.1 synthetic fail-closed QA, v0.2 must prove:

- exact `14 angular slots -> 1170 broad rows` expansion;
- exact `20 Wm radial rows` and `10 WW radial rows` index coverage;
- rejection of any attempted row-level effective `z`, `k`, or `ell` metadata;
- equivalence of a small synthetic factorized calculation to explicit support-atom expansion;
- manifest digest invariance under input-container permutation;
- unchanged downstream firewall.

Synthetic QA remains implementation evidence only and earns no scientific gate PASS.

## 8. State before the first v0.2 real output

Unchanged scientific state:

- `G_DOMAIN_MAPPING=PASS`;
- `G_ANGULAR_AUTHORITY=PASS`;
- `G_ORDERED_JOIN=PASS`;
- `G_RADIAL_SUPPORT=NOT_YET_TESTABLE` until the v0.2 real executor runs;
- downstream physical/covariance/nuisance/relation gates remain blocked.

This correction is frozen before any Exp073IM real radial output is inspected and therefore cannot use an observed radial/support outcome to choose the representation.