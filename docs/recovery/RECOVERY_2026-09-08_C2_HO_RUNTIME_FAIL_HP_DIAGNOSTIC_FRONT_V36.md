# DSIR immutable recovery — HO runtime FAIL, HP diagnostic front — V36

Date: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

All scientific authority preserved by V35 remains unchanged, including admitted `WW_S3_S3`. No C2 scientific/model authority is created here.

## Exp073HO terminal result

Exp073HO run `34229170304`, authoritative job `102070681656`, head checkout `841e431d55aadbdc0ea972902be6da5ffa0125bf`, terminal `FAILURE`.

Raw job log verification:
- frozen runtime binding PASS;
- exact post-HM source reconstruction and full solver build PASS;
- first failure occurs in step `Execute frozen 28-request raw producer` immediately at the first solver invocation, before any endpoint extraction/serialization/aggregate/receipt/artifact step can complete;
- the original workflow redirected first-request stdout/stderr to ephemeral files, so Actions exposed only solver exit code 1 and not the causal solver diagnostic;
- provenance receipt, artifact upload and producer PASS boundary were skipped;
- therefore no 28-packet/1792-byte candidate exists and no raw record set is admitted.

Classification: **infrastructure/runtime implementation FAIL `+0/+0`**, not scientific FAIL. No frozen model/grid/config/ABI/scientific criterion is changed.

## Prospectively frozen diagnostic — Exp073HP

Because blindly rerunning HO would violate self-healing discipline, Exp073HP was prospectively frozen solely to expose the first causal diagnostic without revealing endpoint values.

- prereg `docs/dsir4/prereg/EXP073HP_C2_HO_FIRST_REQUEST_FAILURE_DIAGNOSTIC_V0_1.md`, blob `5b924127b67870a23f0e5aa055d26c12115a6d63`;
- prereg creation commit `4a528649f9cd6256239239b1d57315825900b662`;
- workflow `.github/workflows/exp073hp-c2-ho-first-request-failure-diagnostic-v0-1.yml`, blob `498d647e0aa783c410c2bd08652a95d7b5b36536`;
- binding commit `9b89d7b50fcac3f6f65aa1bd3ba1ecb560a081d8`;
- run `34229746056`, job `102072618086`;
- runner ownership GitHub-hosted only; home/self-hosted heavy owner none;
- current state at note creation: **IN_PROGRESS**;
- exact request is unchanged first HO request only: reference `(0,0)`, `z=0.295`, `k=0.00067 Mpc^-1`, same pinned parent/post-HM source/baseline/p8;
- endpoint record lines are explicitly removed from diagnostic output;
- no serialization, raw packet artifact, decode, mapping or science is permitted.

On HP terminal result, consume raw log immediately. If it exposes a deterministic parser/runtime/configuration defect, repair only that smallest causal defect prospectively and rebind HO. If the same request unexpectedly succeeds, classify the discrepancy as runtime/infrastructure and diagnose environment/execution differences before any HO rerun. Never alter frozen coordinates, model, baseline physics, p8 precision, packet ABI, or admission criteria.
