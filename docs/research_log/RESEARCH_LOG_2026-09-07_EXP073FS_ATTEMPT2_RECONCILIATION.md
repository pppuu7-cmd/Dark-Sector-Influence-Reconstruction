# DSIR research log — Exp073FS attempt-2 reconciliation

Date: 2026-09-07. Scope: DSIR only.

Live GitHub reconciliation found that Exp073FS run `34067352681` is now `run_attempt=2`. Attempt 1 home job `101578366531` terminated `failure` on runner `DSIR-HOME-PC` (runner id 21) while GitHub still recorded the frozen compute step as `in_progress`; the always-evidence collection and artifact upload never executed, and provenance admission was skipped. No scientific result is inferred. Classification is infrastructure runner/orchestration failure `+0/+0`. The old job-log blob is no longer retrievable after rerun, so no shell-level numerical failure is invented.

Attempt 2 home job `101592579318` started on `DSIR-HOME-PC-2` (runner id 22) and is currently `IN_PROGRESS` in the same frozen `WW_S1_S2` A/B gate. Live repository Actions state at reconciliation: exactly one in-progress DSIR run and zero queued runs. No competing heavy job was launched and no partial numerical output/checkpoint content was inspected.

The runner-id transition is provenance-relevant. Until terminal evidence demonstrates a valid restore chain, attempt-1 checkpoints are not assumed to have been available to attempt 2. Terminal consumption must distinguish restored versus newly computed complete stages and fail closed on any checkpoint/source/contract mismatch.

Independent repository work from another DSIR process was also reconciled: commit `440a643917d56ecb4227b3f6eab88da9092521cf` freezes the source-bound C2 IDE six-component residual mapping. Its status is mapping-ready/prediction-not-yet-frozen; it creates no scientific model PASS and does not alter the active WW heavy frontier.
