# DSIR self-hosted Wigner scaling benchmark trigger v0.1

Performance QA only. Requires frozen Exp073BW helper lineage `9fb0ecb79986cf5f542760377533a685745b31e2`, whose hosted exact-equivalence result is `BW_Q1_FULL_AND_STREAM_COMPRESSED_EXACT_EQUIVALENCE_PASS` (run `33435082122`, artifact `9774112002`).

Benchmark the actual Wm streaming general-coupling kernel on the connected `DSIR-HOME-PC` at thread counts 1,2,4,6,8,10 using lmax=308 and real prefix band edges `[0,30,60,90,120,150,180,210,240,272,309]`. No scientific readiness credit; purpose is selecting the full-scale home-run execution policy.

Benchmark implementation commit `5574f1e17c8f91c8268f0d21bb3546bb5c572916`; workflow creation commit `9ce4e52db16c66cee3fb1f2055b2e418636f0da6`.
