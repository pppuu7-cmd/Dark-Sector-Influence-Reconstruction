# DSIR recovery checkpoint — Exp073AM exact single-thread PASS + Exp073AN real cross-route authority shift

**Date:** 2026-08-30

## Scientific-accounting state

- Strict Article-3 scientific repository readiness: **52%**.
- Readiness increment from Exp073AI/AM/AN: **0**.
- Layer A/B: OPEN.
- covariance/whitening: BLOCKED.
- G7/G8/G9: OPEN.
- No scientific model PASS is claimed.
- Historical Exp073X2 Q `SCIENTIFIC_REPEATABILITY_FAIL` remains immutable.

## 1. Original Exp073AI terminal control-plane result

Run `33310888983` completed both expensive single-thread replicas successfully:

- A job `99255607805`, artifact `9734480133`, digest `sha256:aa9f09e3dc8812341ad049ed39f5dea6da9249cf849417c60e825a7e48f93bc7`;
- B job `99255607640`, artifact `9734849638`, digest `sha256:f965b7cc120359d41246eccaa3d70a711485e75641252afe4d79813a061e5aee`.

Original aggregator job `99282603397` failed **before any numerical comparison** with `FileNotFoundError` for the non-existent path:

`external/a/data/derived/g7/exp073ai_env_a_v0_1.json`.

The uploaded artifact actually places the environment receipt at artifact root. Therefore retain the original run permanently as:

`INCOMPLETE_INFRASTRUCTURE_AGGREGATOR_ENV_PATH_ERROR_BEFORE_REPEATABILITY_CLASSIFICATION`.

This classification follows the already-hosted-tested Exp073AK2 completion firewall; it is not repeatability FAIL.

## 2. Exp073AM prospective aggregator-only repair

Exp073AM was frozen after diagnosis but before repaired numerical comparison.

Prospective chain:

- prereg `3c18ea415f7fc5f4653cff5e241bdf0892140fde`;
- unchanged frozen comparator `98e1518c34e30b0a7e59724ae60b7586f8c52f9c`;
- workflow `090d4f48f9eba0974c704a3dde410f99af9a64f0`;
- workflow freeze `8a85aaf768486bfce492a3a331a68e4382f6a130`;
- trigger/head `598e6e632f24ea54d43888fdc6d9d98b96d9ae3c`.

Hosted repair:

- run `33321661835`;
- job `99284585530`;
- artifact `9735051043`;
- artifact digest `sha256:167c82d36266efc3b7bd058f0cc307ec636b6c8efdb6b39b6e88f52d6edb3d66`.

Sole repair: environment receipts bound at artifact-root paths `external/a/exp073ai_env_a_v0_1.json` and `external/b/exp073ai_env_b_v0_1.json`. No workspace recomputation and no comparator/tolerance change occurred.

### Hosted exact result

`PASS_EXP073AI_SINGLE_THREAD_EXACT_REPRODUCIBILITY_V0_1`

- A canonical SHA: `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`;
- B canonical SHA: `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`;
- exact canonical SHA equality: true;
- `numpy.array_equal(A,B)`: true;
- differing entries: `0/479232`;
- differing bands: `0/39`;
- max absolute difference: `0.0`;
- mean absolute difference: `0.0`;
- frozen metadata identical: true;
- single-thread controls verified: true.

This is a real hosted **non-classifying exact reproducibility PASS** for the controlled single-thread execution route. It adds 0 readiness and does not release production.

## 3. Strong cross-route result

Historical primary-P Wm_S0 canonical SHA remains:

`6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.

Controlled single-thread Exp073AI canonical SHA is:

`8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`.

Therefore the controlled route is internally bitwise deterministic but does **not** reproduce historical primary-P exact authority.

This state was already anticipated by Exp073AL, frozen before any real AI output. No new branch or tolerance was invented after observing the result.

## 4. Exp073AN — real binding to the already-frozen Exp073AL classifier

Binding chain:

- real binding note commit `9e0f586107e0b458d2e7f1a4a9378af2b7ed5257`;
- immutable input binding commit `0cd75c9566b37c0042d73e6a021c473ace896933`;
- unchanged Exp073AL classifier commit `a0ee0c5f37533093931c0495b4edd5967ce5a00c`;
- workflow `d1d3c33b242cd13d681616871820a093c3a526d6`;
- workflow freeze `591f7cc80fad513246b6344693722e66768b87a3`;
- trigger/head `c6e385d6e4051b6cf5d3f57d1074d12e63bf53fe`.

Hosted real binding:

- run `33321762778`;
- job `99284850109`;
- artifact `9735076794`;
- artifact digest `sha256:c93e50f2ac6b8f932d8dd9e2cc94b4a2304398549eb1ae033d195b989e8c780b`.

The unchanged pre-result Exp073AL classifier produced:

`DETERMINISTIC_SINGLE_THREAD_ROUTE_BUT_EXACT_AUTHORITY_SHIFT_FROM_PRIMARY_P`.

This is a real hosted governance classification, not a scientific model PASS. Production remains false and readiness remains 52%.

## 5. Interpretation boundary

What is now established:

1. the original multi/unspecified-thread historical route is not globally bitwise reproducible across all hosted runners (historical Q FAIL);
2. the controlled single-thread route **is** internally bitwise reproducible across two independent hosted runners under the frozen controls;
3. the controlled single-thread route converges exactly to SHA `8ac59fc0...9220`;
4. that exact authority differs from historical primary-P SHA `6ec29f6d...18d0f`;
5. hence exact workspace authority is execution-route-sensitive at the bit level even when each route can be internally deterministic.

What is **not** established:

- no tolerance-based physical equivalence criterion has been authorized;
- no new canonical production authority has been selected;
- no historical failure is erased;
- no Layer-A support result exists;
- no scientific dark-sector inference follows from this numerical reproducibility result.

## 6. Next scientifically admissible step

Production remains blocked. The next gate must be a new **prospectively frozen authority-succession decision protocol** that was not encoded in the old P/Q production release rule. It must decide, before any additional angular production is launched, whether exact bitwise authority is required across execution routes or whether a separately justified numerical-equivalence contract is scientifically admissible. Such a future protocol must not retroactively convert historical Q FAIL or cross-route SHA shift into PASS and must preserve current 52% readiness until a real immutable 14-window/pre-support manifest exists.
