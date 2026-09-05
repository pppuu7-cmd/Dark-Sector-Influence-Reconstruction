# DSIR current-process ledger

Updated: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.

## Preserved authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical Exp073CM resource/performance FAIL `+0/+0` and Exp073BU/Exp073DT runner-loss infrastructure results remain immutable and are never rewritten as science.

Validated WW support remains preserved: Exp073DP exact-equivalence PASS `+0/+0`; Exp073DQ durable A/B driver static PASS `+0/+0`; Exp073DR activation/resource PASS `+0/+0`; Exp073DS v0.2 readiness PASS `+0/+0`; Exp073EA saved-LU official-reload-state exactness PASS `+0/+0`. Exp073EC hosted static audit is also PASS `+0/+0`: run/job `33962004169 / 101295382699`, raw token `PASS_EXP073EC_EXP073EB_STATIC_GOVERNANCE_AUDIT_V0_1`.

## Authoritative live process — Exp073DT WW_S0_S0 attempt 4
- run `33940588308`, attempt `4`;
- hosted preflight `101288015425`: SUCCESS;
- self-hosted science `101288014666`: **QUEUED** at latest reconciliation;
- frozen activation head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`;
- frozen source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- durable root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`;
- namespaces `checkpoints/exp073dq-ww-s0-s0-a-v0-1`, `checkpoints/exp073dq-ww-s0-s0-b-v0-1`;
- expected science token `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`;
- runner ownership: **DSIR-HOME-PC RESERVED BY Exp073DT attempt 4**.

Attempts 1–3 remain `INFRASTRUCTURE_INCOMPLETE +0/+0` external runner shutdowns. No competing heavy process may be launched while attempt 4 is queued/in_progress. Frozen science remains `WW_S0_S0`, DES NSIDE=4096, ell 0..12287, 39 bands, full `[4,39,4,12288]`, selected `EE<-EE`, canonical `<f8 [39,12288]`, OpenMP=8, nested numerical-library threads=1, no tolerance rescue.

## Prospective provenance closure — Exp073EB
A source audit performed before any attempt-4 terminal output found that the frozen DQ `validated_finished()` fast path verifies the final receipt and selected-EE SHA but does not itself reread every earlier stage manifest; Exp073DT terminal evidence also does not export the full six-stage manifest chain. The frozen Exp073DT preregistration nevertheless requires all checkpoint provenance and stage-order checks before authority admission. Therefore workflow SUCCESS or the PASS token alone is not sufficient authority evidence.

Exp073EB was prospectively preregistered in commit `664aab881b898cef2b0e4eebf2043aed2bc28138`; event-driven workflow commit `00d2a3c94511486af56867a6218192f28866ee5c`. It is support-only `+0/+0`, bound to exact upstream run/head `33940588308 / c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd` and only upstream conclusion `success`. It acquires the same flock, performs no workspace/window computation, does not modify durable checkpoints, and independently verifies the ordered A/B chain:

`fresh_s0_mask_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete`.

Exp073EB can emit only `PASS_EXP073EB_EXP073DT_FULL_CHECKPOINT_PROVENANCE_AUDIT_V0_1` with `science_gate_scored=false` and `ww_s0_s0_authority_created=false`. It cannot rescue scientific FAIL.

Hosted static regression Exp073EC (commit `c9014c2763e542f22aa5c01583e5e8011ccdf7b7`) completed PASS from raw log, validating Exp073EB's support-only/fail-closed/no-recompute structure.

Immutable recovery authority includes `recovery/2026-09-05_exp073dt_terminal_provenance_gap_exp073eb_armed.md`; research log `docs/RESEARCH_LOG_EXP073EB_2026-09-05.md`.

## Independent next-front preparation — Exp073DV
While Exp073DT attempt 4 remains queued, `experiments/073dv_ww_s0_s1_full_resolution_activation_design_v0_1.md` was added prospectively in commit `1dc7d3f1838856890ba0b04515d6ae275fbc02cf`. It is design/readiness only: no workflow activation, no full-resolution `WW_S0_S1` output, `science_gate_scored=false`, `ww_s0_s1_authority_created=false`.

The design fixes the future cross-field invariants before any `WW_S0_S1` full-resolution result exists: ordered distinct `(S0,S1)` spin-2 fields, exact authoritative reconstruction of both source maps, full `[4,39,4,12288]`, selected `wins[0,:,0,:]=EE<-EE`, canonical `<f8 [39,12288]`, dual-map SHA-bound checkpoints, full ordered manifest-chain reread on terminal fast-path, and exact A/B SHA plus `numpy.array_equal` with no tolerance rescue. Activation remains blocked on terminal Exp073DT classification, required Exp073EB provenance closure on DT PASS, consumed Exp073DU qualifier, and zero competing self-hosted DSIR heavy work.

## Exact terminal action
On Exp073DT terminal SUCCESS: consume raw artifact/digest, receipt, A/B selected payloads and comparator; independently recompute exact SHA and `numpy.array_equal`; then consume Exp073EB full checkpoint-provenance evidence. Only the frozen science token plus exact A/B equality plus full provenance closure may create `WW_S0_S0` authority. Exact A/B inequality is scientific repeatability FAIL. Infrastructure/checkpoint/provenance/artifact failures are `+0/+0`.

## Frozen frontier
`Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.
