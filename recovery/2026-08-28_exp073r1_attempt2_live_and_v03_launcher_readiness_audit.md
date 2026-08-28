# DSIR G7 — Exp073R1 attempt-2 live state and v0.3 launcher readiness audit

Date: 2026-08-28
Scope: G7 validated physical forward/power-input bridge only. This record does not score Exp073P, does not read covariance, does not perform whitening/nuisance SVD/quotient/null analysis, and does not access G8.

## Live parent state

Parent workflow run: `33135622749`
Workflow: `Exp073R1 sharded deterministic full weak-lensing mask v0.2`
Head SHA: `70be4d35199d4132a2ca9da912689519e40bcc84`
Attempt: 2

At this audit snapshot:
- shard 0: `in_progress`, step `Execute deterministic disjoint shard` active;
- shards 1–7: `completed/failure`;
- therefore the parent workflow is still non-terminal and no v0.3 dispatch is admissible yet.

The already-observed failures remain infrastructure/reproduction failures unless a later log establishes otherwise. No scientific support-validity classification has been executed.

## One-shot v0.3 launcher audit

Launcher: `.github/workflows/exp073r1-launch-v0-3-after-v0-2-terminal.yml`
Target: `.github/workflows/exp073r1-desy1-low-concurrency-microshards-v0-3.yml`

The launcher enforces all of the following before dispatch:
1. exact parent run id `33135622749`;
2. parent state `completed`;
3. exact parent workflow path `.github/workflows/exp073r1-desy1-sharded-mask-v0-2.yml`;
4. exact parent head SHA `70be4d35199d4132a2ca9da912689519e40bcc84`;
5. exact target workflow blob `12e15177bd389d603af04c89ec815ba6c94c749c`;
6. exact merger blob `0fb99998ad1a15acaa4223ea7d6d47fbd8d93080`;
7. refusal to dispatch if any prior `workflow_dispatch` run of the v0.3 target already exists.

This is sufficient to prevent a second autonomous dispatch from this recovery path and prevents post-audit mutation of the pre-registered v0.3 implementation from being silently used.

## v0.3 topology audit

The target workflow preserves the previously frozen/reproduced physical input and mapping semantics while changing only transport/reproduction topology:
- deterministic `nshards=32` partition;
- `max-parallel: 1` to remove concurrent pressure on the DES public range endpoint;
- each microshard is explicitly asserted non-science (`science_gate_scored=false`, `f_invalid_computed=false`, covariance/G8 unread);
- R0 genuine PASS is rebound before transport;
- merge requires the complete shard set and reconstitutes the full row universe before claiming Exp073R1 reproduction PASS;
- merged result remains non-science and keeps G7/G8/G9 open.

No frozen Exp073P acceptance threshold, support rectangle, minimum retained coordinate count, covariance rule, nuisance rule, quotient/null rule, or G8 definition is modified here.

## Gate decision

Current state: **Exp073R1 infrastructure/reproduction INCOMPLETE** while shard 0 remains active.

Allowed next action:
- do nothing heavy while parent run `33135622749` is non-terminal;
- when it becomes terminal without a genuine Exp073R1 PASS, allow the already-bound one-shot launcher to dispatch v0.3 exactly once;
- only a genuine full-universe Exp073R1 reproduction PASS may unblock the frozen Exp073P physical support-validity classification.

Scientific ordering remains:
`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`.
