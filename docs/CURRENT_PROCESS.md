# DSIR current-process ledger

Updated: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.

## Preserved authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical negative/infrastructure results remain immutable. Current scientific target is `WW_S0_S0`.

## Authoritative heavy process — Exp073DT WW_S0_S0 attempt 4
- run `33940588308`, attempt `4`;
- hosted preflight job `101288015425`: SUCCESS;
- self-hosted science job `101288014666`: **QUEUED** at latest heavy reconciliation;
- head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`;
- source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- durable root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`;
- namespaces `checkpoints/exp073dq-ww-s0-s0-a-v0-1`, `checkpoints/exp073dq-ww-s0-s0-b-v0-1`;
- expected token `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`;
- next on SUCCESS: independently validate raw A/B exact equality and consume Exp073EB full six-stage provenance before any WW_S0_S0 authority;
- next on infrastructure/BLOCKED: diagnose first causal failure and preserve verified checkpoints;
- **DSIR-HOME-PC RESERVED BY Exp073DT attempt 4**.

No competing self-hosted heavy process may launch.

## Newly consumed support results
### Exp073EG — `BIN_ONLY_MISMATCH +0/+0`
Run/job `33986108360 / 101359768937`; artifact `9975205491`; independently verified ZIP SHA256 `8e57af97dee144bdf2166f071245fba96e1de80a30c3f1f5d2bfbf5b574da917`. Manual/public P exact equality fails; Q/unbin exact equality passes. Mismatch localized to manual P/bin arithmetic/order; no science authority.

### Exp073EH — `OFFICIAL_BIN_SUBSTITUTION_STILL_MISMATCH +0/+0`
Run/job `33988609203 / 101366649641`; artifact `9975933668`; independently verified ZIP SHA256 `638c2e76fc0ff8cfa91623c9c8356d10de63c2519ef17e468450b5f38053ef93`. Replacing P/Q with official PyMaster operations still does not make reconstructed BPW bitwise equal to public BPW. Public/reconstructed SHA `70df69ed48c7fb4b8706cc69dbc08a56272c791892394b357e14111f813681b7` / `580445fd4c0d5a590885680df3b9864fdd935e5d0c6aa8926b6f35281cfe5f77`. No tolerance rescue.

### Exp073EI — `SOLVER_OPERATOR_MISMATCH +0/+0`
Run/job `33988714617 / 101366943002`; artifact `9975963572`; independently verified ZIP SHA256 `52a77c087744e941bc27efb271cdf3047099aa1f5e7092f5296dda9733459def`. NumPy inverse SHA `0e5ac1d0a224ced720219fce5b92bcedd3eac61a1de0d30eecb3df554e2ee7f9`; official decoupling-operator SHA `a7f161423662197eb7f7b9d751e54292f74348d11b6a76a705037d62782186c0`; exact mismatch. Remaining algebraic reconstruction exactness gap is localized to solver/backend semantics under the frozen EI construction. No science authority.

## Active hosted support process — Exp073EJ
Exp073EJ is prospectively frozen support-only `+0/+0`. It applies only official PyMaster 2.7 `NmtWorkspace.decouple_cell` to every serialized->reloaded coupling-matrix column and compares the composed operator bitwise to public `get_bandpower_windows()`.

- prereg commit/blob `416842ddba0984da77b56fad2f98f9e0a44da266 / 79b42e2fc2a7307a02f1fe6eb06808f60e50521a`;
- implementation commit/blob `eb05c9e47b33f1bbe419f01caf80e821d1122e13 / 4451cfd7c35234303e7de9bc93e5d7a079626ecf`;
- workflow commit `8825af889f5e16b7e940b4fc5684d6b126c67562`;
- activation head `d9584a23874a93e59f7580325352565d222d0fdb`;
- run/job `33988827671 / 101367245475`: **QUEUED** at latest reconciliation;
- frozen outcomes `PUBLIC_DECOUPLE_BPW_EXACT` or `PUBLIC_DECOUPLE_BPW_MISMATCH`, both `+0/+0`;
- next on exact: prospectively validate a production-safe adapter architecture delegating decoupling to official PyMaster;
- next on mismatch: inspect only official public BPW construction versus public decouple semantics.

## Distinct-field frontier
Exp073DV full-resolution WW_S0_S1 remains `PREPARED_NOT_ACTIVATED`, blocked on valid WW_S0_S0 authority/provenance closure plus a prospectively validated exact cross-workspace adapter architecture.

Frozen frontier: `Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.
