# DSIR research log — 2026-09-08 — Exp073GZ hosted PASS / FY active

Scope: DSIR only. RTK/RQIR excluded.

## Live heavy chain

Exp073FY namespace-repair V0.3 remains the only active home-heavy process.

- run `34160898921`
- head `b5c8a059a014bee5d318d6067f7a2fac37c5b173`
- hosted audit `101862362835`: SUCCESS
- home-science `101862390771`: IN_PROGRESS
- invalid S3-S3 checkpoint retirement: SUCCESS
- repaired `WW_S2_S3` A/B gate: IN_PROGRESS
- queued DSIR runs at reconciliation: 0
- competing heavy run launched: no
- partial numerical output inspected: no

`WW_S2_S3` remains NOT ADMITTED. Only Exp073FZ may create authority after a fully validated FY candidate.

## Newly consumed result: Exp073GZ

Workflow source commit `a4961a87432f53bc55a13c7f542a8775634b90bd` added the hosted-only static audit for the already-preregistered Exp073GZ contract.

Actions run `34168323933`, job `101883674574`, completed SUCCESS. Raw decoded job log was inspected and contains exact token:

`PASS_EXP073GZ_C2_RUNTIME_ADMISSION_RECEIPT_CONTRACT_STATIC_AUDIT_V0_1`

The audit verified exact contract blob `1c2e30e6563efe3976ee0b1825dfb250a902a529` plus the frozen requirements for 28 z-major/k-minor packets, 64 bytes each / 1792 aggregate bytes, aggregate SHA-256 before decoding/mapping, producer terminal run/job identity, artifact digest identity when transported through Actions, `decoded=false`, `mapped=false`, `prediction_ready=false`, and invalid-provenance classification as infrastructure/`INVALID_FOR_SCIENCE` rather than scientific FAIL.

Classification: `SUPPORT_PLUS_0_PLUS_0` only. No CLASS execution, runtime decoding, scientific mapping, prediction, or model authority occurred.

The previous GZ audit-execution-path block is closed. Next C2 step is a real frozen 28-packet runtime producer/admission under the audited contract, but it remains blocked by home-heavy exclusivity until FY releases the sole self-hosted runner.

## Scientific delta

- newly admitted scientific authorities: 0
- new scientific FAILs: 0
- new resource FAILs: 0
- new infrastructure FAILs: 0
- new support gate closure: Exp073GZ PASS `+0/+0`
