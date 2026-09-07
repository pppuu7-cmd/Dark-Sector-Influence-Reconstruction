# DSIR research log — Exp073FS attempt 2 and C2 prediction-freeze step

Date: 2026-09-07

## Heavy-chain guard

Exp073FS run `34067352681` is currently `run_attempt=2`.

Attempt 1:
- hosted audit job `101578350681`: success;
- self-hosted `home-science` job `101578366531`: terminal `failure` while GitHub still recorded the frozen compute step as `in_progress`;
- evidence collection/upload did not execute;
- provenance admission was skipped;
- old job-log blob is no longer retrievable after rerun, so the shell-level cause is not invented.

Classification: **infrastructure runner/orchestration failure, +0/+0 scientific evidence**. This is not a model FAIL, `INVALID_FOR_SCIENCE`, or an observational result.

Attempt 2:
- self-hosted `home-science` job `101592579318`: `in_progress` on the same frozen `WW_S1_S2` A/B gate;
- hosted launch audit is success;
- no duplicate heavy run was launched;
- no partial checkpoint was interpreted;
- no run artifact is yet available from the active attempt.

The runner changed between attempts, so terminal admission must verify checkpoint/restore provenance rather than assume attempt-1 checkpoint continuity.

## Parallel DSIR-4 progress

C2 IDE is already `mapping_ready=true` through `docs/dsir4/mappings/C2_IDE_RESIDUAL_MAPPING_V0_1.md`, while `prediction_ready=false` and `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

To advance the next admissible step without tuning against downstream gates, added:

`docs/dsir4/mappings/C2_IDE_PREDICTION_FREEZE_CHECKLIST_V0_1.md`

Commit: `e6d9f411e3a758e96c075f5027b27650bfb69df3`.

The checklist freezes the mandatory common domain, branch-mask semantics, same-solver observable bridge, deterministic payload manifest, and fail-closed behavior. It explicitly forbids inventing alpha/beta tangent steps, solver settings, interpolation, or replacements if immutable provenance cannot be recovered.

Current scientific status remains:
- C2 `mapping_ready = true`;
- C2 `prediction_ready = false`;
- C2 `G_DOMAIN_MAPPING = NOT_YET_TESTABLE`;
- Exp073FS attempt-1 failure = infrastructure only;
- no scientific model FAIL introduced in this iteration.
