# DSIR recovery — Exp073DE v0.1 P2 production durability hook implementation FAIL

Date: 2026-09-04. Scope DSIR only; RTK/RQIR excluded.

## Authority
- Prereg commit/blob: `c348f3b8a662a1052345c518b2b9c0b902932c98 / 751459dfc3960f517fc529a0648629ad9ddef112`.
- Auditor commit/blob: `53732708961df277eb3cdaa207c828a9ad98ad0d / 441056a3f933133a299ad571728eca6a0ac0260c`.
- Activation/head: `a2bc5686969e7de44701cb45ca0d8cf7a3f92488`.
- Run/job: `33885148897 / 101062989940`.
- Artifact `9941509491`; Actions digest and independently downloaded ZIP SHA256 both `b110ea3c92e054e183d8c4ac574a6aff613f7f29bdcc9317fb08ef491eb2d0a1`.

## Raw classification
`P2_PRODUCTION_DURABILITY_HOOK_IMPLEMENTATION_FAIL +0/+0`. This is support/infrastructure, not a Wm_S3 scientific result. Raw receipt has `science_numerics_executed=false`, `wm_s3_authority_created=false`, `exp073bu_activated=false`.

The first causal production defect is exact and source-grounded: `full_window_complete` is loaded by the frozen production driver but is not independently resumable. If `selected_te_complete` is absent, control falls through to `execute_exact_adapter`, replaying the already verified full-window computation. Raw checks: `full_window_state_loaded=true`, `adapter_else_is_keyed_only_by_selected_te=true`, `full_window_resume_without_recompute=false`. The same receipt also confirms the expected not-yet-implemented remote-hook checks are false.

No scientific arithmetic, data, band edges, TE semantics or acceptance criteria were changed. The permitted successor is the prospectively frozen Exp073DE v0.2 exact resume-only helper gate, followed only after exact PASS by production remote durability-hook integration.
