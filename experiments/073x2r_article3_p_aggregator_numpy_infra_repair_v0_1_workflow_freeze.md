# Exp073X2R workflow freeze — primary P aggregator-only NumPy repair v0.1

**Frozen:** 2026-08-30 before the repair trigger, while Chain Q is still active and before this repair downloads or reads P replica contents.

- preregistration last-modifying commit: `abe894465bacca43a758b8082923d1e0dbe54dfa`
- unchanged comparator last-modifying commit: `8ec6f94ea9ddf3cc0a4c98e5af696d28d995b2b3`
- workflow_last_modifying_commit: `bfcbebced87c1c982158d7e3783e0c82c6f501cc`
- repaired chain: Exp073X2 primary P only
- source run: `33300997298`
- source replica A artifact: `9730411514`, digest `sha256:34530157cddf594c93728d5e092ab937d16a653665623f00513f4fd58df17555`
- source replica B artifact: `9730409129`, digest `sha256:36358663fb1980ad75cb71f7ca7149d06d357cf7de8b29feca4273f4f88c89e5`
- allowed runtime repair: install `numpy==2.1.3` only for the lightweight unchanged comparator
- trigger path: `ci/exp073x2r_article3_p_aggregator_numpy_infra_repair_v0_1.trigger`
- successful comparator token: `PASS_EXP073X2_DES_N4096_WM0_MASK_ONLY_REPEATABILITY_V0_1`

No workspace recomputation, numerical tolerance, comparator modification, artifact substitution, support calculation, covariance/nuisance/G8 read, scientific-readiness increment, or post-hoc alternative authority selection is permitted.

If comparator executes and detects a mismatch, preserve that mismatch as the primary P repeatability failure under the already-frozen governance. If the repair fails before comparator classification, preserve a new infrastructure-INCOMPLETE record instead.
