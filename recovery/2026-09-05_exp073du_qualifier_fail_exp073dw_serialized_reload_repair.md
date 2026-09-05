# Exp073DU qualifier FAIL consumed; Exp073DW serialized→reloaded repair armed

Date: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.

## Immutable Exp073DU v0.1 outcome
Hosted run/job `33955300558 / 101277450615` completed FAILURE and was consumed from raw logs plus artifact `9966167115`. GitHub artifact digest and independently recomputed ZIP SHA256 are both `34a90ebe024c53c1bb833465346bd0ef6ca3196184bb49a8ba18e543eca8bba1`.

Terminal qualifier receipt is `QUALIFIER_FAIL`, token `FAIL_EXP073DU_WW_S0_S1_CROSSFIELD_SMALLNSIDE_EXACT_ADAPTER_V0_1`, `science_gate_scored=false`, `ww_s0_s1_authority_created=false`, accounting `+0/+0`.

Passed checks included distinct deterministic S0/S1 masks, distinct field objects, ordered cross workspace differing exactly from both auto workspaces, exact expected shapes, finite direct/adapter arrays, ncls=4 and `no_tolerance_rescue=true`. The only failed required checks were adapter full-window exact equality, selected EE exact equality and selected EE SHA equality against the preregistered pre-serialization in-memory W01 reference.

## First causal defect
The production adapter consumes the serialized `w01.fits`. Exp073DU v0.1 compared that route against `get_bandpower_windows()` from the pre-serialization in-memory W01. Preserved Exp073EA support evidence had already established that the saved-LU production route is exact to official PyMaster serialized→reloaded state while pre-serialization and reloaded states may differ at last bits. Therefore the first causal defect is the qualifier reference-state contract, not WW scientific arithmetic. No tolerance or arithmetic criterion is weakened. Exp073DU v0.1 remains immutable historical qualifier FAIL `+0/+0`.

## Prospective minimal repair — Exp073DW
Before any Exp073DW numerical result, a new support-only qualifier was preregistered to retain the same deterministic S0→S1 geometry and production adapter but compare exact outputs only to official `NmtWorkspace.read_from(w01.fits)` state. Pre-serialization-vs-reloaded equality is recorded diagnostically and is not a PASS requirement.

Provenance:
- prereg commit `1128f33ccb5c0fd9cc70393812821ed88b7f9856`;
- qualifier implementation commit `619f138ba2405fd15527ad045244738955077ec5`;
- component freeze commit `32385f11f2b9461aab77beb9b7f5e22bf55c0e81`;
- final hosted workflow commit `1d9c7342f930d1674adb919d794fe4ef1ae955a7`;
- activation/research-log head `f2cda20023503b189977a05b2e482816c3e03f1d`.

Allowed PASS token only: `PASS_EXP073DW_WW_S0_S1_SERIALIZED_RELOAD_EXACT_ADAPTER_V0_1`; always `science_gate_scored=false`, `ww_s0_s1_authority_created=false`, accounting `+0/+0`. No tolerance/allclose/rounding/smoothing/averaging rescue is permitted.

At note creation, hosted Exp073DW run/job `33967669396 / 101310531746` is active. It uses GitHub-hosted infrastructure only and does not claim DSIR-HOME-PC.

## Heavy-run authority unchanged
Exp073DT attempt 4 remains the sole self-hosted heavy owner: run `33940588308`, self-hosted job `101288014666`, frozen head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`. DSIR-HOME-PC remains reserved while that job is queued/in_progress. No competing home task was created.

Full-resolution WW_S0_S1 remains blocked until WW_S0_S0 is validly admitted from Exp073DT raw evidence plus required Exp073EB provenance closure, Exp073DW is terminally consumed, and no competing self-hosted heavy process exists.
