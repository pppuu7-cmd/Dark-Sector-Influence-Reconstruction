# DSIR recovery checkpoint — all-chat reconciliation extended through Exp067E

**Date:** 2026-08-30  
**Classification:** recovery/provenance synchronization only; no scientific gate change; +0 readiness.

## Reconciliation extension

After the first all-chat reconciliation checkpoint, the historical Exp065–067 block was re-audited directly against GitHub because old chat summaries partially conflated it with later nuisance-SVD work.

Authoritative correction:

`Exp065B selected covariance eligibility PASS`

`-> Exp066B selected-bandpower closure FAIL`

`-> Exp066C exact shot-noise template corrective PASS`

`-> Exp067A direct covariance whitening PASS`

`-> Exp067B CAMB<->CLASS physical power-convention HARD FAIL`

`-> Exp067C native-CAMB coherence localization`

`-> Exp067D float32-first multiplication causal diagnosis`

`-> Exp067E preregistered out-of-sample physical power-convention PASS`.

The previous chat-derived interpretation that Exp067B/C/D/E was primarily a nuisance-SVD/rank repair sequence is rejected as non-authoritative. Later nuisance-rank work belongs to different experiments, including current Exp073AW.

## Durable addendum

Created:

`docs/RECOVERY_MANUAL_ADDENDUM_EXP065B_EXP067E_2026-08-30.md`

creation commit:

`744868ecc7df803438d496ddeb1127c4a54d5b4e`.

The addendum records exact hosted runs, jobs, artifacts/digests where available, operator hashes, frozen thresholds, numerical mechanism, and immutable FAIL/PASS separation.

## Key immutable records

### Exp065B

- status `PASS_ACT_UNWISE_SELECTED_COVARIANCE_ELIGIBLE_V0_1`;
- result commit `11f49105cbfba77a5a64aff5201d37a207806d96`;
- run `32980117716`, job `98214421282`;
- selected ACT x unWISE covariance dimension 26;
- direct Cholesky eligible with no regularization.

### Exp066B

- immutable status `FAIL_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1`;
- preservation commit `d278d25142bba87bd157bf80f770546d8c628602`;
- frozen constant-mode white-noise shortcut failed;
- later Exp066C does not reclassify this FAIL.

### Exp066C

- status `PASS_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1`;
- integrated result commit `d46fcd97624380422358e16466adb7aafc091e5b`;
- run `32989328863`, job `98242896864`;
- artifact `9614063228`;
- artifact ZIP SHA256 `2409cd974691f09d80893d8d64f7f61ac5bccff4e28d4eb4251a5a21baf80baf`;
- exact nonconstant shot-noise template repairs only the forward operator while preserving Exp066B FAIL.

### Exp067A

- status `PASS_ACT_UNWISE_OBSERVATIONAL_COVARIANCE_WHITENING_V0_1`;
- result commit `0e04eda9d996a48b6f4b497c0b5d360952f81499`;
- run `32994782105`, job `98261038810`;
- 26-dimensional raw selected covariance;
- direct Cholesky and whitening passed without covariance rescue;
- whitening identity residual `1.0425503003180775e-15`;
- selected-covariance SHA `df7e285c40009e0ba20cc5d920342e1066ceff69d277fdf3233ac63463ffddb9`;
- whitener SHA `b32e59a98b6910427ac5026bc3f882ea8b0934b65de9abe44c599e1c7ec66822`.

### Exp067B

- immutable status `FAIL_CAMB_CLASS_PHYSICAL_POWER_CONVENTION_BRIDGE_V0_1`;
- preservation commit `abdc8c7746589c5f9a3a7e1d965108a0e14afeb3`;
- run `32995950843`, job `98265107213`;
- source contracts and cross-solver log statistics passed;
- preregistered raw-CAMB coherence threshold `5e-8` was exceeded;
- no retuning/reclassification.

### Exp067C

- classification `NATIVE_CAMB_COHERENCE_DEFECT_V0_1`;
- result commit `13334b6f66da1e2a35ad5257e34bd8f84853691f`;
- run `32997216952`, job `98269515280`;
- artifact `9617073194`;
- SHA256 `836c6f0306a34a52af3b4948d525b08e3cb892f5a2dc06b923fb1dc30c5d1bfa`;
- official native CAMB `E_max=1.616012643701481e-7`;
- defect exists on native powers and is not created by interpolation.

### Exp067D

- classification `FLOAT32_TRANSFER_PRODUCT_CAUSALLY_CONFIRMED_V0_1`;
- result commit `b37a1697fa8dd55b048e5b872cac670b71e93778`;
- run `32998129409`, job `98272608213`;
- artifact `9617429413`;
- SHA256 `b0377ab357f751d4703526cfb4c9aa0e925dc58c3f9f4b19662fc662f932a6d9`;
- float32-first reproduction `E_max=1.616012642591258e-7`;
- official-vs-reconstructed residual field max difference `6.661338147750939e-16`;
- promotion before multiplication removes the defect (`E_max=0`).

### Exp067E

- status `PASS_CAMB_CLASS_OUT_OF_SAMPLE_POWER_CONVENTION_V0_1`;
- preservation commit `502af6dc9789665d373868536ff5282af8d446bf`;
- run `32998659859`, job `98274406590`;
- artifact `9617676816`;
- SHA256 `6e6419040b7295dfe4b1b4c126a5cfeaa6e1e24a76a7e29c05ccd7c706f65ee2`;
- R0 regression anchor plus two prospectively frozen fresh references R1/R2;
- inherited cross-solver, CLASS-internal, missing-k2 and CAMB precision-signature controls all passed;
- Exp067B remains `HARD_FAIL_UNCHANGED`.

## Why this matters for current DSIR

This chain is a methodological precedent for Article-3:

- exact released operator/covariance binding;
- no covariance rescue before direct Cholesky;
- immutable failed frozen criteria;
- causal numerical-floor diagnosis;
- separately preregistered corrected successor;
- out-of-sample validation;
- later PASS never erases earlier FAIL.

It does not authorize importing historical ACT x unWISE support/covariance into the current Article-3 1410-row support route.

## Current scientific state

Unchanged:

- Article-2 repository-for-writing readiness = 100% for declared scope only;
- Article-3 strict scientific readiness = 52%;
- Layer A = OPEN;
- Layer B = OPEN;
- covariance/whitening = BLOCKED;
- G7 = OPEN;
- G8 = OPEN;
- G9 = OPEN.

## Active production

Exp073AQ run `33327372191` remains the sole authorized heavy Wm_S1 gate until rechecked at resume time.

Before any next production action, inspect both AQ replica jobs and artifacts. Do not launch Wm_S2 unless a valid exact AQ comparator PASS exists.
