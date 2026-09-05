# DSIR immutable recovery — Exp073EG terminal / Exp073EH activated — 2026-09-05

Scope: DSIR only; RTK/RQIR excluded.

## Exp073EG terminal authority
Run/job `33986108360 / 101359768937` completed SUCCESS at the workflow level, but scientific interpretation is strictly the frozen support classification `BIN_ONLY_MISMATCH +0/+0`. Artifact `9975205491`; GitHub artifact digest `sha256:8e57af97dee144bdf2166f071245fba96e1de80a30c3f1f5d2bfbf5b574da917`; independently downloaded ZIP SHA256 is exactly the same.

Frozen receipt token: `COMPLETE_EXP073EG_BIN_ONLY_MISMATCH_V0_1`.

Exact checks: `p_array_equal=false`, `p_sha_equal=false`, `q_array_equal=true`, `q_sha_equal=true`, finite=true, distinct_masks=true, no_tolerance_rescue=true. Manual/public P hashes are `8748d0354ce52c2cf4c478423a2df819323e5d568768695a2eaa2ac8394a10c6` and `712ee840d17806d1724688caa6c0fd832c7e2201e08b18ac4b79cb7c8af3f63f`; Q hashes are identically `8811f2299bf04269e8af8783209dc3bc91b8ef1c4c50d62e14e344b3f33fa412`. Diagnostic-only P max absolute difference is `2.7755575615628914e-17`; it is not an acceptance criterion and cannot rescue exactness.

Therefore the mismatch is localized to the manual P/bin arithmetic/order before any solve. Q/unbin semantics are exact under the frozen probe. No science gate was scored and no WW authority was created.

## Exp073EH prospective continuation
Exp073EH is support-only `+0/+0` and was frozen only after Exp073EG terminal evidence was consumed. Its preregistration blob is `aac835594fcb29da9d85b0c4444e3a2b40481a59`; implementation blob is `1dde55ce90810cf1da82a9bc169ba2dc411dc65a`.

It replaces only the known-mismatched P operation with official PyMaster 2.7 `NmtBin.bin_cell`, builds Q only with official `NmtBin.unbin_cell`, and asks whether one frozen NumPy inverse/matmul reconstruction becomes bitwise identical to public serialized->reloaded `NmtWorkspace.get_bandpower_windows()`. No alternate layout, solver, arithmetic, tolerance, allclose, rounding, smoothing, averaging or result-dependent retry is permitted.

Activation head `a1b2c20e63deb002f384b5ec28caf7055dbf3800`; run/job `33988609203 / 101366649641` was QUEUED at this recovery write.

## Heavy authority preserved
Exp073DT attempt 4 remains the only authoritative self-hosted heavy process: run/job `33940588308 / 101288014666`, frozen head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`, source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`. It remains QUEUED and DSIR-HOME-PC remains reserved. No competing self-hosted task was launched.

## Next actions
Consume Exp073EH immediately when terminal. If exact, prospectively validate a production-safe official-bin adapter architecture; if still mismatched, isolate only remaining matrix-multiplication/solver arithmetic without revisiting bin/unbin semantics. Independently, when Exp073DT becomes terminal, consume raw A/B artifact evidence and required Exp073EB checkpoint-provenance closure before any WW_S0_S0 authority.