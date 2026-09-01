# 2026-09-01 — Exp073CF overnight-lock race guard

Classification: `PREMATURE_ACTIVATION_QUEUED_NO_EXECUTION_AUTHORITY_EXP073CF`; infrastructure/coordination only; `+0/+0`.

## Authority rule

The currently active user instruction keeps the DSIR home runner **OFFLINE/LOCKED** until the user explicitly returns and says the home computer/WSL runner may be used again. That explicit re-enable has not occurred in the current controlling instruction. Therefore no repository commit that labels itself `post-lock` or `activation_authorized=true` can override the active user-level overnight lock.

## Concurrent repository race discovered

During this audit, repository state changed concurrently after an initial snapshot of zero queued and zero in-progress runs.

A separate commit sequence appeared:

- active workflow shell commit `e91e3660ef91c120215dcdce1be8ee6e3a2eb95f`;
- activation-binding commit `42bd85c889462b9cb9d95123a37c325143aeeeaf`;
- trigger commit `28cd199b1b41450623fa3dba44ed1ac1ebf187b6`.

The trigger commit changed the previously inert seed from `SEED_NO_EXECUTION` to `ACTIVATE_FRESH_FULLSCALE` and created GitHub Actions run `33546929256`.

At the latest coordination snapshot:

- run `33546929256` status: `queued`;
- job `99986640839` `compact-replica (A)`: `queued`;
- job `99986641160` `compact-replica (B)`: `queued`;
- in-progress DSIR runs: `0`.

No PCL, compile, preflight, heavy calculation, comparator or finalizer has started in this run. It therefore has no scientific classification and no authority.

## Conflict in activation metadata

The concurrent activation binding claims `POST_LOCK_ACTIVATION_BINDING_FRESH_FULLSCALE_AUTHORIZED` and records a different observed home configuration (`processors=8`, `swap=16GB`) from the controlling overnight instruction (`processors=10`, `swap=8GB`, `memory=6GB`, ~7.7GB physical RAM). This is another reason not to use that binding as permission to execute while the current user lock remains in force.

The activation binding remains useful only as a provenance record of the concurrent repository mutation. It is not execution permission under the current controlling instruction.

## Safety handling

This audit did not start, rerun, trigger or revive run `33546929256`. The available GitHub connector does not expose a workflow-run cancel operation, so the queued run cannot be cancelled through the current tool surface. Safety therefore depends on keeping `DSIR-HOME-PC` offline; do **not** start `./run.sh` while this run remains queued.

Do not modify the trigger path merely to encode the lock: because the active workflow is path-filtered on that trigger, such a write could create another forbidden self-hosted run. Do not create a competing self-hosted workflow.

## Scientific authority preserved

- Exp073BJ remains terminal Track-A exact Wm_S1 PASS.
- Exp073AQ remains permanent historical scientific FAIL.
- Exp073BD remains provisional/incomplete and forbidden downstream.
- Exp073BV/BW/BZ authority is unchanged.
- Exp073CC/CD/CE remain nonclassifying methodology evidence only.
- Exp073CA remains infrastructure incomplete, not scientific FAIL.
- Exp073CF run `33546929256` is queued only and contributes `+0/+0`.

Article-3 readiness remains **Verified 52.0% | Draft/data 53.7%**.

## Exact next gate under overnight lock

Keep home runner offline. Do not touch the Exp073CF trigger. Hosted/read-only audits may continue only if independent of the queued run. On a later explicit user re-enable, first re-read the run state and current home configuration; if `33546929256` is still queued, it must not be allowed to start blindly. Reconcile/cancel stale activation state first, then perform a fresh memory/infrastructure preflight and only afterward authorize a scientifically valid fresh successor run.
