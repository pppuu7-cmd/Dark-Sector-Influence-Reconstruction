# DSIR research log — C2 Delta_m interface freeze and Exp073FS watch

Date: 2026-09-07

## Heavy-chain guard state

Checked workflow run `34067352681` (`Exp073FS WW_S1_S2 autonomous audited home science v0.1`) after the earlier attempt-1 infrastructure interruption and attempt-2 restart.

Current attempt-2 jobs at this check:

- `hosted-launch-audit`, job `101592593435`: **completed / success**;
- `home-science`, job `101592579318`: **in_progress**;
- active step: `Run frozen WW_S1_S2 A/B gate with durable checkpoints`;
- terminal evidence collection and upload remain pending because the scientific compute is not terminal.

Guard action: **no duplicate heavy run launched, no rerun requested, no partial checkpoint interpreted**. There is no new terminal infrastructure failure to repair in this check.

The previous attempt-1 interruption remains classified as infrastructure/orchestration evidence `+0/+0`, not a scientific FAIL. This log does not infer a more specific cause from unavailable attempt-1 logs.

## Parallel frozen-order DSIR4 progress

Because the active heavy run required no intervention, work continued on the next safe C2 prerequisite.

Created:

`docs/dsir4/mappings/C2_IDE_DELTAM_EXTRACTION_CONTRACT_V0_1.md`

Commit:

`1c668d0dcea6382b403f313e7c7cf63432d7085b`

The new contract prospectively freezes the common `Delta_m` extraction interface for `C2_IDE_LOCAL_TANGENT_CONE` without reusing the historical CLASS `mPk` response as a proxy.

Key fail-closed decisions:

- pinned solver/tangent/baseline/precision provenance remains unchanged;
- synchronous source extraction only; unsupported Newtonian IDE is forbidden;
- the common coordinate remains `Delta_m = delta_m + 3(1+w_m) Hconf theta_m/k^2` under the already-frozen G1/G2 convention;
- model and C0 reference must use the same pinned solver lineage/settings and extraction code;
- source variables, units, signs, matter partition, branch diagnostics, generator identity and payload SHA256 are mandatory;
- historical `mPk` arrays cannot be relabelled as the common `Delta_m` prediction;
- the inherited physical k-grid is frozen to `[0.00067, 0.00201, 0.0067, 0.0201] Mpc^-1` because the recovered `0.067 Mpc^-1` node is outside the current DSIR4 bound `0.06664762008318016 Mpc^-1`;
- missing auditable source variables or provenance => `NOT_YET_TESTABLE`, not scientific FAIL;
- malformed artifact => invalid for science, not model rejection.

## Scientific status

C2 remains:

- `mapping_ready = true`;
- `prediction_ready = false`;
- `G_DOMAIN_MAPPING = NOT_YET_TESTABLE`;
- scientific contribution this iteration: `+0/+0`.

No frozen scientific threshold, hypothesis ID, branch criterion, or downstream acceptance rule was modified. No WW/observational result was consulted to choose the C2 extraction interface.

## Next safe step

1. Continue guarding run `34067352681` until terminal state; only then inspect terminal evidence and consumer/orchestration continuation.
2. In parallel, source-audit the pinned `class_iv` outputs/transfer variables needed to bind exact source names, signs and units to the frozen `delta_m`, `theta_m`, `w_m`, and `Hconf` fields.
3. Only after that source audit, implement deterministic C2 prediction generation and hosted/static provenance validation.
4. Do not advance C2 to `G_DOMAIN_MAPPING=PASS` until the dedicated immutable prediction artifact and admission procedure pass.