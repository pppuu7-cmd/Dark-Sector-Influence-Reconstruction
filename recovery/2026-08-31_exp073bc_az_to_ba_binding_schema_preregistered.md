# Exp073BC — prospective AZ-to-BA binding schema

DSIR only. Article-3 readiness remains 52%; increment +0. This is a nonclassifying prerequisite and cannot declare scientific PASS.

Exp073AQ remains permanent FAIL. Exp073AZ run 33339663991 is the sole admissible predecessor for Exp073BA.

A future BA-binding receipt is admissible only after hosted Exp073AZ terminal token exactly `PASS_EXP073AZ_WM_S1_MASK_PCL_EXACT_V0_1`.

The receipt must freeze: AZ run id 33339663991; exact comparator job; exact authority artifact id and sha256 digest; canonical PCL member and SHA256; dtype `<f8`; shape `[12288]`; exact A/B array equality true; exact AZ PASS token; BA prereg commit b445066a36c838b18e4cea2ca56f2f6abee56406; BA comparator commit a0b5bd8065c590e20c648215b8d993452fb7339c; BA workflow commit fc0ca8b4c0e31673c1470418060a95ac507b3759; BA workflow-freeze commit f9f19f80ed62090b22d69e6a667ea96fc7cf1f82; authority class `low_memory_general_coupling_deterministic_v1`; frozen thread controls; scientific_pass_claimed=false; readiness_increment=0; article3_scientific_readiness_percent=52.

Fail closed on any other source run/token, missing exact equality, malformed or missing digest/SHA, wrong dtype/shape, BA commit mismatch, readiness change, scientific PASS claim, preferred-replica/tolerance/ULP/rounding/averaging/majority rescue, or downstream Layer-A/support/covariance/whitening/nuisance/relation/G8 input.

Unknown future AZ comparator/artifact/PCL identifiers may be filled only after terminal hosted AZ PASS. Filling those metadata values does not change this prospectively frozen admissibility predicate. A valid receipt only authorizes the already-frozen BA execution; it creates no support result and no readiness increment.