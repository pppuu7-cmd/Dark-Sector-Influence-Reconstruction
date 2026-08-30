# Exp073AQ workflow freeze — controlled twin Wm_S1 production v0.1

**Frozen:** 2026-08-30 before trigger and before any Exp073AQ real Wm_S1 output exists.

- preregistration last-modifying commit: `2794ed0a48e8e7f8019584461296661d1a83ae08`
- unchanged physical/angular runner last-modifying commit: `45ed8d8d1e90cdaf314e0384b6f3cdfef369925b`
- pre-freeze comparator repair last-modifying commit: `8772ff5550351d53dfa47aeb05cd83bd6f673750`
- workflow_last_modifying_commit: `42b6241dc90a253cc4d4e8f8dbf72a6a71b46c18`
- trigger path: `ci/exp073aq_article3_controlled_twin_wm_s1_production_v0_1.trigger`

The earlier comparator file commit `64ae1eae3fc8902c0ec4368c2b7209be4fcbc67e` contained a pre-freeze harness error in JSON selection and is not executable authority. It was detected and superseded before this workflow freeze and before any real Wm_S1 output. The exact-equality scientific/reproducibility criterion was unchanged.

Frozen real classifications after both valid complete replicas reach the comparator:

- `PASS_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`, or
- `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

Any failure before valid comparator classification remains infrastructure-INCOMPLETE and must not be called repeatability FAIL.

No tolerance, rounding, ULP allowance, majority vote, preferred replica, support/covariance/nuisance/G8 leakage, scientific model PASS, or readiness increment is authorized.
