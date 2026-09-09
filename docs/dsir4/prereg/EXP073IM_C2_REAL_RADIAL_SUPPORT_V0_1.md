# Exp073IM — C2 real radial-support execution preregistration v0.1

Date frozen: 2026-09-09. Scope: DSIR only.

Status: PROSPECTIVELY FROZEN BEFORE ANY EXP073IM REAL RADIAL OUTPUT IS READ.

## 1. Purpose

Score the first real `G_RADIAL_SUPPORT` result for `C2_IDE_LOCAL_TANGENT_CONE` after the admitted ordered angular join and after the complete synthetic radial-interface QA.

This gate asks only whether the frozen 14-slot angular authority can be combined with the exact DES-Y1 radial source/lens payloads under the pinned observation semantics to produce a deterministic, finite, non-empty radial/LOS handoff for every required slot. It does **not** perform the downstream Article-3 physical-domain selection, covariance whitening, nuisance quotient, relation/null test, or model-comparison conclusion.

## 2. Immutable upstream binding

Bind exactly:

- ordered-join authority: `docs/dsir4/authority/EXP073IL_C2_ORDERED_JOIN_AUTHORITY_V0_1.json`;
- admitted run/job: `34271954072 / 102215439354`;
- artifact ID: `10074157812`;
- artifact ZIP SHA256: `acaaf9c00a3654b5e59c190470325a92818e8f2f94296ee45bce1ecfd27baa9e`;
- exact token: `PASS_EXP073IL_C2_ORDERED_JOIN_STRUCTURAL_ADMISSION_V0_1`;
- radial interface: `docs/dsir4/contracts/DSIR4_C2_RADIAL_EXECUTOR_INTERFACE_V0_1.md`;
- synthetic QA receipt: `docs/dsir4/authority/DSIR4_C2_RADIAL_INTERFACE_SYNTHETIC_QA_PASS_V0_1.md`;
- synthetic QA run/job: `34391645930 / 102601119354`.

Ordered slots remain exactly:

`Wm_S0, Wm_S1, Wm_S2, Wm_S3, WW_S0_S0, WW_S0_S1, WW_S0_S2, WW_S0_S3, WW_S1_S1, WW_S1_S2, WW_S1_S3, WW_S2_S2, WW_S2_S3, WW_S3_S3`.

Any missing, duplicated, substituted, or permuted slot is `INVALID_FOR_SCIENCE_EXP073IM`, not a scientific FAIL.

## 3. Exact DES-Y1 radial payload binding

Source payload:

- `y1_redshift_distributions_v1.fits`;
- bytes `109440`;
- SHA256 `b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b`;
- source bridge `S0->BIN1`, `S1->BIN2`, `S2->BIN3`, `S3->BIN4`;
- source coordinate `Z_MID` from HDU 1.

Lens payload:

- `2pt_NG_mcal_1110.fits`;
- bytes `6600960`;
- SHA256 `114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca`;
- lens coordinate `Z_MID` and `BIN1..BIN5` from the pinned DES-Y1 lens extension used by the observation route.

DES-Y3 substitution is forbidden.

## 4. Frozen observation/radial semantics

Use the pinned DES-Y1 observation semantics already frozen in the radial interface:

- Cosmotheka authority `Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`;
- `photoz_shift_dz=0`;
- source/lens arrays are consumed in their released order;
- no DSIR-side rebinning, smoothing, interpolation, extrapolation, rounded/effective z, or effective ell/k substitution;
- any normalization internal to the pinned tracer/kernel implementation is recorded as runtime behavior; no new DSIR normalization is introduced;
- `Wm` remains signed galaxy-density x source-shear;
- `WW` remains source-shear x source-shear;
- raw `n_i(z)n_j(z)` multiplication is forbidden as a substitute for lensing-kernel construction;
- physical bookkeeping uses `k=(ell+1/2)/chi(z)` in `Mpc^-1` only where required to populate the frozen handoff schema;
- no fiducial `P(k)` weighting.

## 5. Required real output

For all 14 slots, the executor must produce a canonical pre-physical-support coordinate table whose rows contain the exact fields frozen in `DSIR4_C2_RADIAL_EXECUTOR_INTERFACE_V0_1.md`, including:

- immutable `coordinate_id`;
- unique inherited non-negative `ordinal`;
- slot and `band_index`;
- canonical float64 `z` and `k_Mpc^-1`;
- prospectively fixed `final_response_abs_values` component vector;
- exact angular/radial/code/runtime provenance.

The execution manifest must additionally record:

- input byte counts and SHA256 values;
- observation-code commit and numerical-library versions;
- total rows and rows per slot/band;
- per-slot kernel normalization/finite diagnostics;
- canonical ordered-table SHA256;
- exact list of any rejected rows and a frozen reason code;
- all anti-leakage assertions.

## 6. Scientific radial PASS/FAIL criterion

`PASS_EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_1` is emitted only if all of the following hold:

1. every provenance/interface/slot-order check passes;
2. all 14 required slots are represented in the real output;
3. every slot has a non-empty radial/LOS construction under the pinned DES-Y1 semantics;
4. all required kernel normalizations are finite and strictly positive where normalization is defined;
5. all emitted handoff coordinates required by the interface are canonical finite float64 values with `k_Mpc^-1 > 0`;
6. all coordinate IDs and ordinals are unique and deterministic;
7. canonical rerun/ordering controls demonstrate identical ordered-table digest under an input-row permutation or equivalent prospectively coded deterministic replay;
8. no forbidden interpolation/effective-coordinate/fiducial-P/downstream information is read;
9. the output is valid for the separately frozen Article-3 physical-support gate to classify next.

`FAIL_EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_1` may be emitted only when all provenance/interface checks are valid but the frozen real radial construction itself has a scientific support failure, such as an empty/zero/non-finite required radial kernel for one or more mandatory slots or no valid radial handoff rows for a mandatory slot.

The following are **not** scientific FAILs:

- payload/hash mismatch;
- parent mismatch;
- slot/schema/order mismatch;
- unit mismatch;
- nonzero `dz`;
- forbidden interpolation/smoothing/effective-coordinate metadata;
- downstream covariance/nuisance/relation leakage;
- execution interruption or dependency failure.

Those classify respectively as `INVALID_FOR_SCIENCE_EXP073IM` or `INCOMPLETE_EXP073IM`.

## 7. Downstream firewall

Exp073IM must not evaluate or read:

- Article-3 `f_invalid` or retained-count threshold;
- covariance, inverse covariance, Cholesky/whitening products;
- nuisance tangent/SVD/rank information;
- relation/null statistics;
- G7/G8 or article-selection results;
- any DSIR-4 full-model matrix outcome.

Only an admissible `PASS_EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_1` authorizes the next separately frozen `G_PHYSICAL_SUPPORT` execution.

## 8. Gate state before output

Before Exp073IM runs:

- `G_DOMAIN_MAPPING=PASS`;
- `G_ANGULAR_AUTHORITY=PASS`;
- `G_ORDERED_JOIN=PASS`;
- `G_RADIAL_SUPPORT=NOT_YET_TESTABLE`;
- `G_PHYSICAL_SUPPORT=NOT_YET_TESTABLE`;
- `G_COV_WHITENING=NOT_YET_TESTABLE`;
- `G_NUISANCE_QUOTIENT=NOT_YET_TESTABLE`;
- `G_RELATION_NULL=NOT_YET_TESTABLE`;
- `scientific_model_authority_created=false`.

No threshold or classification rule in this preregistration may be changed after a real Exp073IM output is inspected.
