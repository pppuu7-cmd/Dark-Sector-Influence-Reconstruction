# DSIR research log — 2026-09-07 — Exp073GK infrastructure repair and heavy-chain watch

## Scope

Automation guard audit of the active DSIR chain plus the next permitted DSIR4 C2 support step. No frozen scientific threshold, hypothesis ID, coordinate grid, model definition, or downstream gate logic was changed.

## Active heavy frontier

- Workflow run: `34067352681` — `Exp073FS WW_S1_S2 autonomous audited home science v0.1`.
- Current attempt: attempt 2.
- `hosted-launch-audit`: completed `success`.
- `home-science`: still active on the frozen `WW_S1_S2` A/B gate (attempt-2 job lineage; previously identified job `101592579318`).
- Guard action: **no duplicate heavy run dispatched** and no partial science checkpoint interpreted.

Scientific classification of the still-running heavy job: **no terminal scientific verdict yet**.

## Newly detected failed support workflow

Exp073GK hosted static audit run `34084884016`, job `101626888946`, completed `failure`.

Exact failing assertion from the terminal job log:

`AssertionError: 0.06664762008318016`

The workflow was prospectively checking that the already-frozen DSIR4 angular-domain ceiling appeared explicitly in either the generator implementation or its preregistration text. The C2 preregistration carried the exact four-node grid `[0.00067,0.00201,0.0067,0.0201] Mpc^-1` but omitted the literal inherited ceiling token. Therefore the failure occurred before the synthetic arithmetic fixture and was a static contract/document binding mismatch.

Classification: **INFRASTRUCTURE / IMPLEMENTATION-AUDIT FAILURE, scientific support +0/+0**. It is not `FAIL`, not `OUTSIDE_DOMAIN`, and not evidence against `C2_IDE_LOCAL_TANGENT_CONE`.

## Repair

Updated `experiments/073gk_c2_ide_delta_m_generator_static_audit_v0_1_prereg.md` to state explicitly:

`k_max=0.06664762008318016 Mpc^-1`

and to record that every already-frozen generator node lies strictly inside that inherited ceiling. No grid point, threshold, equation, solver pin, branch rule, or hypothesis was changed.

Repair commit: `7c399cdead1511b485575337ea9f368829fb5e49` (`Repair Exp073GK frozen k-max audit binding`).

The path-filtered push automatically launched replacement hosted audit run `34085009787`; job `101627249783` entered `in_progress`. This is a light hosted static audit, not a duplicate self-hosted heavy science run.

## C2 scientific status after repair

Exp073GK remains a support-only deterministic generator/static-audit layer. Even if the replacement hosted run passes, it cannot by itself create real C2 numerical authority.

Current fail-closed state remains:

- `mapping_ready=true` (from the separately audited C2 residual mapping lineage);
- real source-bound prediction payload: not yet admitted;
- `prediction_ready=false` for scientific authority;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE` until the mandatory numerical source-extraction/provenance payload and Gate-1 admission are completed.

No scientific model FAIL was created in this iteration.

## Next guard action

1. Poll `34085009787` to terminal state; if it fails, inspect the exact hosted log and repair only implementation/provenance defects without changing frozen science.
2. Independently poll heavy run `34067352681`; do not duplicate while active.
3. After Exp073GK static support is clean, proceed to the mandatory source-extraction/provenance step for the four prospectively frozen C2 points, then deterministic payload admission. Only after that may Gate-1 status be reconsidered.
