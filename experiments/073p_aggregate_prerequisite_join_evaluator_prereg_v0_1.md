# Exp073P aggregate prerequisite join evaluator — preregistration v0.1

**Frozen:** 2026-08-29 (EEST), before implementation or synthetic evaluator output and while canonical Exp073R1 v0.6 run `33212521957` is still queued.

## Purpose

Implement the already-preregistered, non-science split-provenance join defined by
`docs/METHOD_EXP073P_SPLIT_PROVENANCE_JOIN_V0_1.md`.  This evaluator may decide
only whether every immutable prerequisite for the separately frozen Exp073P
physical-support calculation is present and mutually consistent.  It must not
calculate a support fraction, retained dimension, covariance quantity, nuisance
rank, relation/null statistic, held-out result, or G8 quantity.

This preregistration does not modify the Exp073P physical rectangle, threshold,
coordinate definition, classification labels, or gate ordering.

## Exact canonical R1 authority

The only R1 execution admitted by this evaluator version is:

- run `33212521957`;
- job `98988824629`, `metacal-map-longrun`;
- workflow `.github/workflows/exp073r1-desy1-selfhosted-longrun-stageb-v0-6.yml`;
- workflow head `79abf2a9694e57e7a2ba1fbb563a0f6413e891f9`;
- workflow name `Exp073R1 DESY1 self-hosted long-run Stage-B v0.6`;
- expected artifact name `exp073r1-v06-selfhosted-longrun-79abf2a9694e57e7a2ba1fbb563a0f6413e891f9`.

At freeze time the run is queued and has no terminal artifact.  No output from
that run has been inspected.  The join must refuse authorization unless the run
later reaches `completed/success`, the named artifact is unique, non-expired and
digest-bound, and its internal summary passes the exact R1 interlock in
`ci/exp073p_r1_admissibility_interlock_v0_1.py`.

If this run ends without a genuine internal R1 PASS, evaluator v0.1 cannot be
repointed.  Any later replacement authority requires an explicit superseding
preregistration before its output is inspected.

## Frozen parent registry

The join must bind all of the following parents.  A committed summary is not a
substitute for a required Actions artifact unless explicitly listed as the
canonical record below.

| Parent | Immutable execution binding | Required record |
|---|---|---|
| Cosmotheka/public-input preflight | run `33076320686`, head `a23843376ac4301327d23f3844b7fa658d9492c1`, artifact `9648001733`, digest `sha256:7ca856e24a1c03b11101cca278e6f631c86ba8ab28c744ef352c77dbe4b55266` | exact Cosmotheka pin `7bde066626f66cd7bbe79cc46224d2342840e463`, exact four source-file hashes, frozen six release names; the legacy aggregate READY flag must remain false |
| Large DES whole-object identity | run `33081571259`, head `372997bf1240a224c2a915fd0d1a5ae50476ba7a` | source artifact `9650284556`, digest `sha256:0eb1fdc7bc2d9f5816e0a003418a41b540cd7281af1f5ceb24a37af82187f5d4`; metacal artifact `9650627630`, digest `sha256:5a80c70568a6ed114e4e32990c5399bc8109df10f4d2910abd73441edb122a2b` |
| Remaining DES objects / P2 | run `33086291753`, head `fbcd8eb0a46a566b2510081f7f90714b534e7252`, artifact `9652278804`, digest `sha256:3eaed2f182b885c360a73ad3a6bfefac088a000acd05bef07bdfe5a852a246b9` | `PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2`, four exact object byte counts and SHA256 values |
| redMaGiC mask + released n(z) / S0 | run `33086762750`, head `82c5804b1fcbbdc100f09a9878643ddc51975d8e`, artifact `9652504743`, digest `sha256:c6f84c35e7ade17a6054ad77d4117b64a6c69fbbefe0d0f89e6491bbe88b358e` | `PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0`, exact mask and lens/source n(z) hashes |
| Weak-lensing mask / R1 | canonical authority above; artifact identity becomes bindable only after terminal success | `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` and every R1 interlock hard control |
| BOSS finite mm component / J | run `33042052616`, head `1bd022ffca543361d265a72b782ef96fe069d2ce`, artifact `9634226231`, digest `sha256:239b198c1adfc21333779ef1efb597885710bddd593b380a67ac6dd1399daa65` | exact committed key-metrics SHA256 `dfe8861cd62e82297d9ce733d79585f7c5eca93d9bdbcef445b9f578105b2029`, `54/240`, `27/120` per cap, `9/40` in every P0/P2/P4 block |
| Frozen Exp073P support contract | workflow run `33132472587`, head `637ecc89422fa1eb02a4254044ce57b45de7df51`, successful self-test | evaluator source SHA256 `ae8c4000af46c30ffb1059dab8f01758d2b21471cb7eac93fefba2f4d8093eeb` and unchanged constants below |
| Split-join contract | workflow run `33166411136`, head `d4e0ba1b9a9e0342e763a715cd9b1db9b906affc`, successful self-test | `PASS_SPLIT_PROVENANCE_JOIN_PREREG_SELFTEST_EXP073P` semantics |
| R1-to-P interlock | workflow run `33215180917`, head `7be369dec4469dd9f6390eb5225ff4366ded9488`, successful self-test | exact R1 summary validation; no support scoring |
| v0.6 protocol guard | workflow run `33215131178`, head `e92d40f8aabe636414827655bfd165b093f2073e`, successful self-test | exactly one active heavy v0.6 executor and unchanged frozen evaluator blob |

## Exact release-object identities

The join must reproduce this complete six-object identity table exactly:

| Object | Bytes | SHA256 |
|---|---:|---|
| `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits` | `104595840` | `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55` |
| `DES_Y1A1_3x2pt_redMaGiC_zerr_CATALOG.fits` | `31383360` | `4a0ed31a128c34aa0da17e1d826c76b5ac829ba1c2c2087b965977b89d43a177` |
| `2pt_NG_mcal_1110.fits` | `6600960` | `114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca` |
| `y1_redshift_distributions_v1.fits` | `109440` | `b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b` |
| `y1_source_redshift_binning_v1.fits` | `2738626560` | `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5` |
| `mcal-y1a1-combined-riz-unblind-v4-matched.fits` | `84075649920` | `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8` |

The obsolete source hash beginning `491f4bb7` must be rejected.

## Evaluator inputs and output

The classifying join evaluator must receive:

1. a machine-readable Actions metadata bundle obtained from the repository API
   in the same workflow execution;
2. the exact preflight, large-source, large-metacal, P2, S0, R1 and BOSS JSON
   records downloaded or checked out under the bindings above;
3. the unchanged local frozen-contract and R1-interlock modules.

It must hash every consumed record byte-for-byte, validate every semantic field,
and emit one immutable JSON receipt.  The sole prerequisite PASS label is

`PASS_EXP073P_PREREQUISITE_BINDING_V0_1`.

That PASS may set `support_executor_authorized=true`; this means only that the
separately preregistered physical-support executor is eligible to start.  It is
not an Exp073P physical-support PASS and does not authorize covariance.

A deterministic identity/schema/semantic mismatch is
`REJECTED_EXP073P_PREREQUISITE_BINDING_V0_1`.  Missing, expired or unavailable
artifacts and interrupted metadata retrieval are
`INCOMPLETE_EXP073P_PREREQUISITE_BINDING_V0_1`.  Neither state authorizes the
support executor.

## Mandatory no-leakage receipt fields

Every output, including PASS, must state:

- `support_fraction_evaluated=false`;
- `f_invalid_computed=false`;
- `retained_dimension_evaluated=false`;
- `covariance_read=false`;
- `whitening_read=false`;
- `nuisance_svd_read=false`;
- `relation_null_read=false`;
- `heldout_read=false`;
- `G8_read=false`;
- `gate_state={G7: OPEN, G8: OPEN, G9: OPEN}`.

## Frozen downstream scientific contract

The join copies but never evaluates:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05` with an inclusive boundary;
- minimum retained full-coordinate dimension `15`;
- classifying `nside=4096`;
- positive absolute support envelope, while the production Wm response remains signed;
- no crop-before-normalization, fiducial-P/model weighting, effective-ell cut,
  post-hoc cut, covariance/SVD/relation/held-out leakage.

Only a later genuine
`PASS_COSMOTHEKA_DESY1_BOSS_COMMON_PHYSICAL_SUPPORT_EXP073P` may open covariance
restriction/whitening.  G7, G8 and G9 remain OPEN after prerequisite-join PASS.

## Permitted pre-output tests

Synthetic self-tests may be run before R1 completes, but they must use fabricated
records, exercise both the exact valid bundle and fail-closed mutations of every
parent, and always report `support_executor_authorized=false`.  Synthetic PASS
must never reuse the real prerequisite PASS label.
