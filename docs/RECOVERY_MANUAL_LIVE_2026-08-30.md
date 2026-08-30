# DSIR RECOVERY MANUAL — live 2026-08-30 overlay

This file is the active-state overlay to the stable historical `docs/RECOVERY_MANUAL.md`. Use the historical manual for derivations and long-lived methodology, then this overlay, `docs/RECOVERY_LATEST.md`, the DSIR cross-chat consolidation, and the newest recovery checkpoint.

## Active state

- Article-2 repository-for-writing readiness: **100%** for declared scope; this does not close global G7/G8/G9.
- Strict Article-3 scientific repository readiness: **52%**.
- G7/G8/G9 = OPEN.
- Layer A/B = OPEN.
- covariance/whitening = BLOCKED until real Layer A and real Layer B pass in frozen order.
- synthetic/infrastructure/governance QA adds **0 scientific-readiness points**.
- DSIR remains independent of RTK/RQIR.

## Frozen Article-3 boundaries

- `0.295 <= z <= 2.33` inclusive;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A `operator_f_invalid <= 0.05` inclusive;
- Layer-B invalid observation-row fraction `<=0.05` inclusive;
- minimum final retained observation dimension `15`;
- DES classifying route `NSIDE=4096`;
- positive absolute operator/window envelopes only for support bookkeeping; measured Wm remains signed;
- no effective ell/z/k shortcut;
- no fiducial-P weighting;
- no covariance/whitening, nuisance SVD/rank, quotient/relation/null or G8 during support selection;
- exact-threshold numerical ambiguity remains `numerically_unresolved`.

## Established Article-3 prerequisite chain

Retain all categories distinctly:

- Exp073R1 real hosted DES source-mask reproduction — PASS/non-classifying authority.
- Exp073U immutable 1410-row observation skeleton — PASS/non-classifying.
- Exp073V broad-row support schema — PASS/non-classifying.
- Exp073W BOSS k-compatibility — PASS/non-classifying; downstream `54/240` support mask cannot select pre-support rows.
- Exp073Y exact DES released n(z) inventory — PASS/non-classifying.
- Exp073Z v0.1 — numerical implementation failure, not science.
- Exp073Z2 stable-direct DES radial authority — PASS/non-classifying.
- Exp073AB row-to-operator mapping — PASS/non-classifying.
- Exp073AD exact 5%-boundary QA — hosted synthetic PASS/+0.
- Exp073X — `INCOMPLETE_INFRASTRUCTURE_RESOURCE_CANCELLED_NO_AUTHORITY_REUSE`; partial Wm_S0 reuse forbidden.

## X2 angular frontier

### P primary

- run `33300997298`;
- head `2403d9680e1d08a3853084034eb2878faa52b4e0`;
- replica jobs `99229007616`, `99229007666`.

### Q contingency/redundant

- run `33301058260`;
- head `730ae4951ab8cd8e1dd2c392e991c3120345678a`;
- replica jobs `99229177604`, `99229177540`.

At the latest audit all four jobs remained in exact real-DES workspace computation and neither run had artifacts. Do not launch a third X2.

Binding governance:

1. P PASS -> P canonical; Q cannot displace it.
2. P scientific/repeatability FAIL -> Q cannot rescue it.
3. P infrastructure-INCOMPLETE before classification -> Q may be fallback only if Q PASSes.
4. both PASS -> P canonical and canonical hashes must agree; disagreement blocks production.
5. both infrastructure-INCOMPLETE -> prospective repair required.
6. Exp073AF also blocks P PASS + Q PENDING until Q resolves.

No X2 result alone raises readiness.

## Exp073AE — future real pre-support join firewall

Hosted synthetic PASS:

- run `33301598268`, job `99230706936`;
- artifact `9729115927`;
- digest `sha256:57a16aa9d95b13278f7abb2497edb9f1c8d5a6714612b35c43c5cc214e632117`;
- token `PASS_EXP073AE_ARTICLE3_PRESUPPORT_AUTHORITY_JOIN_SCHEMA_SYNTHETIC_V0_1`.

Classification: synthetic/governance QA only, +0 readiness.

Future real join must bind exact 14-window angular authority to Exp073U + Exp073Z2 + Exp073AB + Exp073W without support/covariance/nuisance/G8 leakage.

## Exp073AF — X2 -> Exp073AA release control

Hosted synthetic PASS:

- run `33302029344`, job `99231856970`;
- artifact `9729246776`;
- digest `sha256:adae6a7c4688674f41e32a0865971b1e92b5fac452371684376c07f5463b77a2`;
- token `PASS_EXP073AF_X2_TO_EXP073AA_RELEASE_CONTROL_SYNTHETIC_V0_1`.

Classification: synthetic/governance QA only, +0 readiness.

If valid release occurs, exactly these 13 tasks may run:

`Wm_S1, Wm_S2, Wm_S3, WW_S0_S0, WW_S0_S1, WW_S0_S2, WW_S0_S3, WW_S1_S1, WW_S1_S2, WW_S1_S3, WW_S2_S2, WW_S2_S3, WW_S3_S3`.

`Wm_S0` comes only from canonical X2.

## Exp073AG — exact 14-window authority aggregator schema

Prospectively frozen while both X2 chains remained in progress and before any remaining Exp073AA production task was released.

Frozen chain:

- prereg `2af44c322e03ce40882891a64c12e39b1e0a3564`;
- implementation `d49c8f43aa3ae3c6547864278fb9380720e61475`;
- workflow `61dded0fbd0cea8cc5218d6c46d570a873084c4d`;
- workflow freeze `80c381ccc2e16091a44649d475966244ca9cfe71`;
- trigger/head `1583760a13072628b307c216857dedc06748b19b`;
- hosted run `33303419856`, job `99235598024`;
- artifact `9729669260`;
- digest `sha256:71929dbc9eb77d59fbe5ad790d6c9cecfb236cefb457ab9a1dbd2e67d4a549c1`;
- token `PASS_EXP073AG_EXACT_14WINDOW_AUTHORITY_AGGREGATOR_SCHEMA_SYNTHETIC_V0_1`.

Classification:

`HOSTED_SYNTHETIC_PASS_NON_SCIENTIFIC_PLUS_0_READINESS`.

The future real authority must contain exactly in order:

`Wm_S0, Wm_S1, Wm_S2, Wm_S3, WW_S0_S0, WW_S0_S1, WW_S0_S2, WW_S0_S3, WW_S1_S1, WW_S1_S2, WW_S1_S3, WW_S2_S2, WW_S2_S3, WW_S3_S3`.

Rules:

- `Wm_S0 -> canonical_exp073x2` only;
- all other 13 -> `exp073aa` only;
- every entry requires positive hosted run/job/artifact identities;
- artifact digest exactly `sha256:<64 lowercase hex>`;
- selected window exactly canonical `<f8 [39,12288]` with 64-hex SHA256;
- no duplicate/missing/reordered tasks;
- no duplicate selected-window SHA across distinct tasks without a new prospective review;
- deterministic manifest SHA256 is computed from canonical sorted-key compact JSON metadata only;
- unknown fields, provenance/dtype/shape/hash drift, readiness/gate/firewall drift fail closed.

The 18-case hosted synthetic matrix passed and verified insertion-order-independent deterministic manifest hashing. Exp073AG did not read real angular artifacts, build a real 14-window authority, compute support, or read covariance/nuisance/G8.

## Authorized order from here

1. inspect real X2 P/Q jobs and artifacts;
2. classify immutable P/Q outcomes under frozen governance;
3. apply Exp073AF release control;
4. if released, execute exactly 13 remaining Exp073AA tasks;
5. build the real exact ordered 14-window authority under Exp073AG;
6. execute the real strict pre-support join under Exp073AE with Exp073U + Exp073Z2 + Exp073AB + Exp073W;
7. freeze the complete immutable 1410-row finite-operator candidate manifest;
8. only then execute real Layer A;
9. freeze `S_op` in inherited Exp073U order;
10. execute real Layer B;
11. only after both support layers PASS may covariance restriction and unrescued Cholesky whitening begin;
12. then nuisance representation/resolvability, signed SVD/rank, quotient/relation/null and fresh withheld-family G8 after G7 relation freeze.

No later-stage information may choose an earlier authority, threshold, representation, row set or support set. No scientific-readiness increase is authorized before the real complete pre-support finite-operator candidate manifest exists.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
3. `docs/RECOVERY_LATEST.md`
4. `docs/DSIR_CROSS_CHAT_AUTHORITY_CONSOLIDATION_2026-08-30.md`
5. `recovery/2026-08-30_exp073ag_14window_schema_hosted_pass_x2_still_running.md`
6. `experiments/073af_article3_x2_to_exp073aa_release_control_v0_1_prereg.md`
7. `experiments/073ag_article3_exact_14window_authority_aggregator_schema_v0_1_prereg.md`
8. `experiments/073ae_article3_presupport_authority_join_schema_v0_1_prereg.md`.
