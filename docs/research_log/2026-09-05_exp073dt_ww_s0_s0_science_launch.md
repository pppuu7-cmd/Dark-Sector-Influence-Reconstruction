# DSIR research log entry — 2026-09-05 — Exp073DT WW_S0_S0 science launch

DSIR only; RTK/RQIR excluded.

Repository reconciliation superseded a stale `RECOVERY_LATEST` state that still described Exp073DP as live. Raw Exp073DP artifact was independently rechecked: repaired run/job `33938446310 / 101230897808`, artifact `9960969007`, ZIP SHA256 `e34b545b21fc93f8948ad328084afd405885c1045313d7162b553a45583af7a8`, exact token `PASS_EXP073DP_WW_EXACT_ADAPTER_SMALLNSIDE_EQUIVALENCE_V0_1`, NaMaster v2.7 source commit `24365fa59a38c15732f4f37e8b29265b75c442d5`; all three synthetic controls have exact full and EE equality with max difference 0.0.

Newer repository authority had already closed Exp073DQ durable-driver static PASS and Exp073DR activation/resource PASS and identified Exp073DS v0.1 flock-scope invalidation. Exp073DS v0.2 run `33938789513` attempt 2 was consumed from raw artifact `9961211035`; independent ZIP SHA256 equals GitHub digest `d12693ce2b2ec17abfef7008e82eca2bf9f9a29b99f43b00c83e30b2313df53d`. Receipt proves continuous lock scope, affinity 8, PyMaster 2.7, actual OMP team 8, nested numerical-library threads 1, and no scientific workspace/payload. Classification: readiness PASS `+0/+0`.

With live Actions clear of competing home work, Exp073DT was prospectively frozen and launched as the first `WW_S0_S0` scientific authority gate. Prereg commit `946964121f12c67e053514109bf974050eeb0cc9`; activation head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`; contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`. Run `33940588308`; hosted preflight job `101237102962` PASS; self-hosted job `101237118421` IN_PROGRESS. DSIR-HOME-PC is reserved by Exp073DT.

Frozen science is unchanged from admitted DQ/DO arithmetic: S0×S0 spin-2 auto, no lens mask, NSIDE=4096, ell 0..12287, 39 bands, full `[4,39,4,12288]`, selected `EE<-EE`, canonical `<f8 [39,12288]`; durable A/B checkpoints and exact SHA + `numpy.array_equal` terminal comparator; no tolerance rescue. Expected scientific token is `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`.

Next action is terminal consumption of `33940588308 / 101237118421`; partial numerical values are not to be inspected while it runs. Exact PASS advances to `WW_S0_S1`; infrastructure failure triggers first-cause repair and checkpoint-preserving resume.
