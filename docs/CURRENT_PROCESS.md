# DSIR current-process ledger

Updated: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.

## Preserved authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical negative/infrastructure results remain immutable.

## Authoritative heavy process — Exp073DT WW_S0_S0 attempt 4
- run `33940588308`, attempt `4`;
- hosted preflight `101288015425`: SUCCESS;
- self-hosted science `101288014666`: **QUEUED** at latest live reconciliation;
- frozen head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`;
- source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- durable root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`;
- A/B namespaces `checkpoints/exp073dq-ww-s0-s0-a-v0-1` and `checkpoints/exp073dq-ww-s0-s0-b-v0-1`;
- expected token `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`;
- last durable checkpoint: verify live durable root/manifests when runner starts; only complete hash/identity-verified stages may restore;
- on SUCCESS: independently consume raw A/B exact equality and Exp073EB six-stage provenance before any WW_S0_S0 authority;
- on scientific FAIL: preserve negative result and advance only as frozen contract permits;
- on infrastructure/BLOCKED: diagnose first causal failure and preserve verified checkpoints;
- **DSIR-HOME-PC RESERVED BY Exp073DT attempt 4**.

No competing self-hosted heavy process may launch.

## Newly terminal support result — Exp073EG
Run/job `33986108360 / 101359768937`; workflow SUCCESS but frozen classification **`BIN_ONLY_MISMATCH +0/+0`**. Artifact `9975205491`; GitHub digest and independently downloaded ZIP SHA256 are exactly `8e57af97dee144bdf2166f071245fba96e1de80a30c3f1f5d2bfbf5b574da917`. Frozen token `COMPLETE_EXP073EG_BIN_ONLY_MISMATCH_V0_1`.

Exact result: manual/public P/bin SHA and `numpy.array_equal` fail; manual/public Q/unbin SHA and `numpy.array_equal` pass. P hashes `8748d0354ce52c2cf4c478423a2df819323e5d568768695a2eaa2ac8394a10c6` / `712ee840d17806d1724688caa6c0fd832c7e2201e08b18ac4b79cb7c8af3f63f`; Q hash on both paths `8811f2299bf04269e8af8783209dc3bc91b8ef1c4c50d62e14e344b3f33fa412`. Diagnostic-only P max difference `2.7755575615628914e-17`; no tolerance rescue. No science gate and no WW authority.

This prospectively localizes the pre-solve exact mismatch to manual binning arithmetic/order; Q/unbin semantics are excluded under the frozen probe.

## Active hosted support process — Exp073EH
Exp073EH is prospectively frozen support-only `+0/+0`. It replaces only P with official PyMaster 2.7 `NmtBin.bin_cell`, generates Q only with official `NmtBin.unbin_cell`, then performs one frozen NumPy `K=RQ`, `inv(K)@R` reconstruction and compares bitwise with serialized->reloaded public `get_bandpower_windows()`.

- prereg commit/blob `9674b330a3f6514127cc8781e3e68aac8478f6a2 / aac835594fcb29da9d85b0c4444e3a2b40481a59`;
- implementation commit/blob `b9abc653e0035d17fbce8bde05822e8b07d86928 / 1dde55ce90810cf1da82a9bc169ba2dc411dc65a`;
- workflow commit `c75103dbb45e63d81650a20748d6484944aa5d8b`;
- activation head `a1b2c20e63deb002f384b5ec28caf7055dbf3800`;
- run/job `33988609203 / 101366649641`: **QUEUED** at latest reconciliation;
- expected frozen outcomes: `OFFICIAL_BIN_SUBSTITUTION_FULL_EXACT` or `OFFICIAL_BIN_SUBSTITUTION_STILL_MISMATCH`, both `+0/+0`;
- next on exact: prospectively validate production-safe official-bin adapter architecture;
- next on mismatch: isolate only remaining matrix-multiplication/solver arithmetic without revisiting P/Q semantics.

## Distinct-field frontier
Exp073DU/DW remain historical qualifier FAIL `+0/+0`; Exp073DX excludes FITS orientation; Exp073ED excludes low-level/public BPW layout; Exp073EE establishes formula mismatch; Exp073EF localizes mismatch before solve to K/R; Exp073EG now localizes it specifically to manual P/bin while Q/unbin is exact. Exp073EH tests the single official-bin substitution closure. Exp073DV full-resolution WW_S0_S1 remains PREPARED_NOT_ACTIVATED and blocked on valid WW_S0_S0 authority/provenance closure plus a prospectively validated exact cross-workspace adapter architecture.

## Frozen frontier
`Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.
