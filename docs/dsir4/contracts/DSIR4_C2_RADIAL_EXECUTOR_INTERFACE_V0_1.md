# DSIR-4 C2 radial executor interface v0.1

Date frozen: 2026-09-09. Scope: DSIR only.

Status: PROSPECTIVE INTERFACE FREEZE. This document does not score `G_RADIAL_SUPPORT`, does not create a scientific model PASS/FAIL, and does not authorize covariance, nuisance or relation/null access.

## 1. Upstream authority

The executor must consume only the admitted C2 ordered-join authority:

- hypothesis: `C2_IDE_LOCAL_TANGENT_CONE`;
- authority file: `docs/dsir4/authority/EXP073IL_C2_ORDERED_JOIN_AUTHORITY_V0_1.json`;
- admitted run/job: `34271954072 / 102215439354`;
- artifact ID: `10074157812`;
- artifact ZIP SHA256: `acaaf9c00a3654b5e59c190470325a92818e8f2f94296ee45bce1ecfd27baa9e`;
- exact admission token: `PASS_EXP073IL_C2_ORDERED_JOIN_STRUCTURAL_ADMISSION_V0_1`;
- ordered slots exactly:
  `Wm_S0, Wm_S1, Wm_S2, Wm_S3, WW_S0_S0, WW_S0_S1, WW_S0_S2, WW_S0_S3, WW_S1_S1, WW_S1_S2, WW_S1_S3, WW_S2_S2, WW_S2_S3, WW_S3_S3`.

Any missing, duplicated, permuted or substituted slot is `INVALID_FOR_SCIENCE_RADIAL_INTERFACE`, not a scientific support FAIL.

## 2. DES-Y1 radial payloads

Source-side payload:

- file: `y1_redshift_distributions_v1.fits`;
- exact bytes: `109440`;
- SHA256: `b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b`;
- source read convention from pinned Cosmotheka: HDU 1, `Z_MID`, `BIN{zbin+1}`;
- exact source bridge: `S0->BIN1`, `S1->BIN2`, `S2->BIN3`, `S3->BIN4`.

Lens-side payload:

- file: `2pt_NG_mcal_1110.fits`;
- exact bytes: `6600960`;
- SHA256: `114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca`;
- lens read convention from pinned Cosmotheka: HDU 7, `Z_MID`, `BIN1..BIN5`;
- redMaGiC lens-bin definitions exactly `[0.15,0.30)`, `[0.30,0.45)`, `[0.45,0.60)`, `[0.60,0.75)`, `[0.75,0.90)`.

No DES-Y3 radial object is admissible in this C2 route.

## 3. Pinned observation semantics

Observation-code authority:

`Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`.

The pinned theory path obtains both galaxy-density and galaxy-shear redshift distributions through `mapper.get_nz(dz=0)`. Therefore the current interface freezes:

- `photoz_shift_dz = 0`;
- no DSIR-side interpolation, smoothing, rebinning, effective-z replacement or node shift before tracer/kernel construction;
- raw released `Z_MID` and `BINi` arrays are passed through the pinned observation semantics;
- no independent DSIR renormalization is introduced. If the pinned tracer library performs an internal normalization, that is part of the pinned observation implementation and the exact runtime/library version must be recorded in the execution manifest.

Changing `dz`, normalizing by a new DSIR rule, or replacing the stored coordinates with effective coordinates requires a new prospectively versioned interface.

## 4. Physical field semantics

`Wm_Si` is the signed DES-Y1 galaxy-density x source-shear route, not an unspecified matter kernel.

`WW_Si_Sj` is the DES-Y1 source-shear x source-shear route.

For radial/LOS construction the executor must reproduce the pinned tracer/kernel semantics. Direct raw multiplication `n_i(z)n_j(z)` is forbidden as a substitute for weak-lensing kernel construction.

Historical Exp073P fixes the physical bookkeeping convention `k=(ell+1/2)/chi(z)` in `Mpc^-1`, with no fiducial `P(k)`, covariance, nuisance, relation/null or withheld-gate weighting.

## 5. Separation of radial and physical-support stages

This executor constructs the radial/LOS representation and the pre-physical-support coordinate table. It must not classify the later Article-3 physical-support gate.

Legacy Exp073P `operator_f_invalid` and later Article-3 coordinate-count `f_invalid` are different quantities and must never be aliased.

The radial executor may retain diagnostic positive-envelope numerator/denominator quantities needed for provenance, but it must not copy a legacy Exp073P PASS into `G_PHYSICAL_SUPPORT`.

## 6. Output handoff schema

The output table passed to the already-frozen Article-3 physical-support stage must contain, for every candidate row:

- `coordinate_id`: non-empty immutable string;
- `ordinal`: unique non-negative integer inherited deterministically from the full pre-support ordering;
- `slot`: exactly one of the 14 ordered slot labels;
- `band_index`: integer `0..38`;
- `z`: finite canonical float64 radial coordinate;
- `k_Mpc^-1`: finite canonical float64 physical wavenumber;
- `final_response_abs_values`: non-empty finite-or-explicitly-invalid vector in a prospectively fixed component order;
- provenance fields identifying angular authority, radial payload SHA256, observation-code commit and runtime versions.

Rows must be emitted in increasing inherited `ordinal`. Input permutation must not alter the ordered output digest.

The next physical-support stage remains governed by `docs/ARTICLE3_PHYSICAL_SUPPORT_GATE_CONTRACT_2026-08-28.md` and therefore independently applies the exact physical rectangle, positivity/envelope validity, `f_invalid<=0.05`, and retained-count `>=15` rules.

## 7. Fail-closed prohibitions

The radial executor must reject before science classification if any of the following occurs:

- ordered-slot mismatch or permutation;
- radial payload byte/SHA mismatch;
- source `zbin_mcal`/`BINi` mapping mismatch;
- nonzero photo-z shift;
- unit mixing between `h/Mpc` and `Mpc^-1`;
- non-finite coordinates or kernel normalization;
- implicit interpolation/extrapolation/smoothing/rounding/effective-ell/effective-z/effective-k substitution;
- fiducial `P(k)` weighting;
- covariance/inverse-covariance/whitening access;
- nuisance/SVD/rank access;
- relation/null/G7/G8/article-selection access.

Taxonomy:

- interface/provenance/schema violation -> `INVALID_FOR_SCIENCE_RADIAL_INTERFACE`;
- infrastructure interruption -> `INCOMPLETE_RADIAL_INTERFACE`;
- only a separately preregistered real `G_RADIAL_SUPPORT` scorer may emit a scientific radial PASS/FAIL.

## 8. Required synthetic QA before real scoring

The interface implementation must pass fail-closed tests for at least:

1. exact 14-slot order and permutation rejection;
2. source-bin bridge `0..3 -> BIN1..BIN4`;
3. payload SHA mismatch rejection;
4. `dz=0` enforcement;
5. unit-mixing rejection;
6. non-finite/zero invalid normalization rejection;
7. duplicate `coordinate_id` and duplicate `ordinal` rejection;
8. input-row permutation invariance of the canonical output order/digest;
9. forbidden interpolation/effective-coordinate metadata rejection;
10. downstream leakage rejection.

Synthetic QA is implementation evidence only and earns no scientific gate PASS.

## 9. Scientific state after this freeze

Unchanged:

- `G_DOMAIN_MAPPING=PASS`;
- `G_ANGULAR_AUTHORITY=PASS`;
- `G_ORDERED_JOIN=PASS`;
- `G_RADIAL_SUPPORT=NOT_YET_TESTABLE`;
- `G_PHYSICAL_SUPPORT=NOT_YET_TESTABLE`;
- `scientific_model_authority_created=false`.

This freeze closes the executor-interface design prerequisite; the next admissible implementation task is the synthetic fail-closed interface QA, followed by a separately preregistered real radial execution.