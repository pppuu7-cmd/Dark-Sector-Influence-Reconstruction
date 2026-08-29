# Exp073W — Article 3 BOSS lower-k compatibility and broad-row authority audit v0.1

**Frozen:** 2026-08-30, after Exp073V and **before Exp073W execution or any current combined Layer-A output**.

## Why this gate is required

A pre-execution audit found a frozen-contract mismatch that must be resolved rather than silently ignored:

- historical Exp073J BOSS component used the domain
  `0.000704833374744468 <= k_phys <= 0.06664762008318016 Mpc^-1`;
- the later prospectively frozen Article-3 support contract and Exp073P specify
  `k_phys > 0` and `k_phys <= 0.06664762008318016 Mpc^-1`, with no positive lower cutoff;
- Exp073P nevertheless imports the already-frozen historical BOSS result `54/240`.

The two rules differ only at very low positive k, but they need not be mathematically identical for a broad finite matrix row. Exp073W therefore computes both masks from the same exact `C=W@M` operator and determines whether the historical 54/240 mask is actually invariant under removal of the obsolete positive lower cutoff.

No threshold is changed after output. Compatibility is defined prospectively as **exact retained-mask identity**.

## Frozen parent authorities

### Exp073U observation order

- full candidate order SHA256: `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`;
- BOSS block: ordinals `1170..1409`, 240 rows;
- order: `NGC P0 rows 0:39 -> NGC P2 rows 80:119 -> NGC P4 rows 160:199 -> SGC same`;
- BOSS ordered-ID SHA256: `7315944adea1a36c0bdb162d57c567330151018dd2058f80e2cb6cb20c153ea0`.

### Exp073I/Exp073J matrix authority

Use exactly:

- `W_BOSS_DR12_NGC_z3_V6C_1_1_1_1_1_10_200_2000_averaged_v1.matrix.gz`;
- `W_BOSS_DR12_SGC_z3_V6C_1_1_1_1_1_10_200_2000_averaged_v1.matrix.gz`;
- `M_BOSS_DR12_NGC_z3_V6C_1_1_1_1_1_1200_2000.matrix.gz`;
- `M_BOSS_DR12_SGC_z3_V6C_1_1_1_1_1_1200_2000.matrix.gz`.

Required decompressed SHA256:

- NGC W: `a308dc562d1a7224cefcf91d32580877929e0daa33806517e0d2d53710236827`;
- SGC W: `2a542a2d48f3e8c8299f58a885d5273238e4ade32c0f0de020d8b9f23afe7759`;
- both M files: `3ac30e68f79deee59963c5c52f7585e0cde495393963210a3922c1c62513a042`.

Semantics remain pinned to `fbeutler/pk_tools@707eb2a6a4691c34eae19d7f72047ca4892f528e`.

Composition and grid:

- `C = W @ M`;
- `W=(200,2000)`, `M=(2000,1200)`, `C=(200,1200)`;
- `k_h[i]=0.0005+0.001*i`, `i=0..399`;
- three consecutive copies for `(P0,P2,P4)`;
- `h_fid=0.676`;
- `k_phys=h_fid*k_h`.

## Frozen radial-support certificate

BOSS z3 is the already-bound sample `0.5<z<0.75`. The entire interval lies inside `0.295<=z<=2.33`.

Exp073W must represent this as an interval/subset certificate. `z_eff=0.61` or any other scalar effective-z value is forbidden for support classification.

## Two frozen k-domain evaluations

For every selected observed row use only

`w_r(j)=abs(C[r,j])`.

No P(k), covariance, nuisance, relation/null, G7/G8/G9 or post-hoc cutoff may enter the weights.

### Legacy rule L

`0.000704833374744468 <= k_phys <= 0.06664762008318016 Mpc^-1`.

This must reproduce the immutable Exp073J historical result:

- 240 candidates;
- 54 retained;
- 27 NGC + 27 SGC;
- 9 retained in every `(cap,P0/P2/P4)` block;
- retained ordered-ID SHA256 `29f7f0a724f7f4ff6b1b4b8933e43d9b08545a4056fdeb65e1c5fe831deda084`.

If this reproduction fails, classification is `INVALID_FOR_SCIENCE_EXP073W_BOSS_AUTHORITY`.

### Current Article-3 rule C

`0 < k_phys <= 0.06664762008318016 Mpc^-1`.

Use exactly the same full positive `abs(C)` denominator and the same inclusive leakage threshold `f_invalid<=0.05`.

## Prospectively frozen compatibility criterion

After the legacy reproduction succeeds:

- **PASS** iff the 240-element retained mask under rule C is exactly bit-for-bit identical to the legacy rule-L mask;
- **FAIL** iff at least one observation row changes retained/rejected status.

Positive token:

`PASS_EXP073W_BOSS_LOWER_K_COMPATIBILITY_V0_1`

Negative token:

`FAIL_EXP073W_BOSS_LOWER_K_COMPATIBILITY_V0_1`

A FAIL is a **contract-compatibility finding**, not evidence against a physical dark-sector model. It requires a new prospective architecture resolution before the combined Layer-A manifest; thresholds or rows may not be changed in response to the result.

## Required diagnostics independent of PASS/FAIL

Record:

- number and ordered IDs of changed rows;
- rule-L and rule-C retained counts;
- maximum absolute change in `f_invalid`;
- per-cap/per-multipole retained counts under both rules;
- contribution of the low-k region `0<k<0.000704833374744468` to each row's positive envelope;
- exact row with the smallest distance to the 0.05 threshold under either rule;
- no-effective-z and no-effective-k assertions.

## Broad-row authority arrays

The audit must also content-hash the BOSS Layer-A logical arrays in inherited Exp073U order:

- little-endian int64 `row_ptr`;
- little-endian float64 `k_phys_Mpc^-1` (1200 support columns);
- little-endian float64 `operator_abs_weight` with logical shape `[240,1200]`;
- little-endian int64 `ordinal=1170..1409`;
- rule-L and rule-C retained masks as uint8;
- ordered coordinate IDs and their SHA256.

NPZ is transport only; authority is the logical-array SHA256 plus dtype/shape metadata.

## Required controls

1. source SHA identities match;
2. matrix shapes and finite-value checks pass;
3. selected absolute row sums are positive and finite;
4. inherited BOSS ID/order digest matches Exp073U;
5. z3 interval is wholly inside the radial domain;
6. legacy rule reproduces the immutable 54/240 authority exactly;
7. current rule is evaluated without a positive lower cutoff;
8. comparison uses exact retained-mask identity;
9. repeated computation is deterministic;
10. covariance/nuisance/relation/G8 data are never read.

## Scientific accounting

Exp073W is an ambiguity-resolution and real-operator authority gate. It cannot by itself close the full 1410-row manifest or authorize Layer A globally. Article-3 scientific readiness remains **52%** until the complete real pre-support broad finite-operator manifest is frozen. The next headline checkpoint remains approximately **55–57%**.
