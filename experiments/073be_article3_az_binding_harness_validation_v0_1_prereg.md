# Exp073BE — Article-3 AZ binding harness validation v0.1 — prospective preregistration

**Date frozen:** 2026-08-31
**Track:** A infrastructure/provenance prerequisite only
**Scientific authority:** false
**Scientific readiness increment:** +0
**Draft/data readiness increment:** +0

## Motivation

Exp073BA run `33342137113` terminated before compact/finalize scientific computation. Both replica jobs stopped at `Bind exact admitted AZ PCL`; downstream comparison/authority jobs were skipped. Therefore BA-1 is retained immutably as an infrastructure/provenance binding failure, not a scientific repeatability failure.

Static inspection identifies a deterministic harness mismatch. Exp073BA searches downloaded AZ authority content using:

`external/az/**/*canonical*pcl*.npy`

whereas the frozen Exp073AZ authority workflow publishes the canonical array as:

`data/derived/g7/exp073az_wm_s1_pcl_canonical_v0_1.npy`

The token order is `pcl` then `canonical`, so the BA glob cannot select that file. No scientific threshold, array value, numerical tolerance, or downstream result is involved in this failure.

## Frozen input authority

Exp073BE may inspect only Exp073AZ hosted run `33339663991`, head SHA `0a9581e19f7f010e13bf9aa88307b1940d0105de`, terminal success, authority artifact `9740703849`, digest `sha256:3cecacff76169dd968e458db0ae70563cf8c3cb0b30d0dff4038a2c792dd3d75`, terminal token `PASS_EXP073AZ_WM_S1_MASK_PCL_EXACT_V0_1`, canonical SHA `2a990b06defbe9922f82b4b85ae26df09bc7881508a85b003648cb23907a5888`, shape `[12288]`, dtype `<f8`.

## Validation contract

The hosted validation must:

1. download the exact frozen AZ authority artifact from run `33339663991`;
2. require exactly one file named `exp073az_wm_s1_pcl_exact_authority_v0_1.json` and exactly one file named `exp073az_wm_s1_pcl_canonical_v0_1.npy` anywhere under the download root;
3. reject wildcard token-order substitution as the production binding rule;
4. verify authority token, canonical shape `[12288]`, dtype `<f8`, `array_equal=true`, and canonical SHA from the authority JSON;
5. independently load the canonical NPY, canonicalize it to contiguous `<f8`, and verify shape, finite values, and SHA-256 over canonical bytes;
6. emit only an infrastructure/provenance validation receipt.

The only successful terminal token is:

`PASS_EXP073BE_AZ_BINDING_HARNESS_VALIDATION_V0_1`

This token is **not** a scientific PASS and cannot admit Wm_S1. It only authorizes a later prospectively frozen BA successor to use the exact-basename binding rule.

## Anti-leakage firewall

Exp073BE must not inspect or use Layer-A/B classifications, covariance/whitening, nuisance/quotient geometry, relation tests, G8/G9 outcomes, manuscript-favorability, or any Wm_S2/WW result. It must not modify numerical arrays, round values, introduce ULP/tolerance rescue, average replicas, choose a preferred replica, or reinterpret Exp073AQ.

## Accounting

- Article-3 scientific authority readiness remains exactly `52.0%` regardless of Exp073BE outcome.
- Article-3 draft/data readiness remains `53.714285714285715%` regardless of Exp073BE outcome.
- Synthetic/infrastructure/provenance QA earns no readiness credit.

## Prospective consequence

If and only if the hosted Exp073BE validation succeeds, a **new** BA successor may be frozen prospectively with only the input-file binding mechanism corrected to the exact canonical basename. The original Exp073BA run and code remain historical and are never rewritten or reclassified. All scientific production criteria of BA must remain unchanged.