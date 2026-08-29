# DSIR checkpoint — replacement R1 active; aggregate join v0.2 ready

**Date:** 2026-08-29 07:30 EEST  
**Scope:** non-science recovery and downstream execution-integrity preparation
while the sole heavy mapper remains active.

## Active R1 authority

The PEP 668 failure of run `33212521957`, job `98988824629`, is preserved as
`INCOMPLETE_EXP073R1`.  It emitted no result artifact and remains permanently
inadmissible to aggregate join v0.1.

The isolated-venv repair changed only dependency installation.  The current
sole replacement execution is:

- run `33222848695`, attempt 1;
- job `99020389131`, `metacal-map-longrun`;
- head `98c4b8783a95932949947d9e214706c4ec7eaf8c`;
- workflow
  `.github/workflows/exp073r1-desy1-selfhosted-longrun-stageb-v0-6.yml`;
- workflow blob `2cdcb0c60f464c0c65c3bafdde23daec7732215e`;
- unchanged evaluator blob `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`;
- runner `DSIR-HOME-PC` / `win-ws338`.

At this checkpoint, setup, checkout, unchanged-evaluator verification,
immutable Stage-A/R0 metadata binding, venv installation, both artifact
downloads and downloaded-parent re-binding are `completed/success`.  The
ordinary whole-object 84 GB mapper step is `in_progress`; the terminal R1
assertion is pending; no result artifact exists.

The only current classification is reproduction `INCOMPLETE`.  No duplicate
heavy execution is authorized.

## Prospective downstream binding

Before any terminal summary or artifact existed, commit `0f85b7c` froze

`experiments/073p_aggregate_prerequisite_join_superseding_r1_authority_prereg_v0_2.md`.

It binds the exact replacement run/job/head/workflow/artifact name and retains
all nine non-R1 parents and every v0.1 semantic/byte check.  The failed v0.1 R1
run, job and artifact name are explicit mutation cases that must be rejected.

Implementation adds, without modifying v0.1 files:

- `ci/exp073p_aggregate_prerequisite_join_v0_2.py`;
- `ci/exp073p_actions_metadata_bundle_v0_2.py`;
- `.github/workflows/exp073p-aggregate-prerequisite-join-actual-v0-2.yml`;
- `.github/workflows/exp073p-aggregate-prerequisite-join-v0-2-selftest.yml`.

The v0.2 adapters privately load and hash-check the byte-frozen v0.1 semantic
validators, replacing only R1 Actions identity and receipt version.  The real
route remains `workflow_dispatch` only, requires an independently API-checked
future artifact ID/digest, and cannot run before R1 termination.

Local validation at this checkpoint:

- aggregate evaluator v0.2 synthetic mutation suite: PASS;
- metadata-route v0.2 synthetic mutation suite: PASS;
- superseded run/job/artifact mutations rejected: PASS;
- production trigger/firewall inspection: PASS;
- workflow YAML parsing: PASS;
- repository regression: `44 passed`;
- `git diff --check`: PASS.

Hosted synthetic CI completed after implementation commit `fb2efe4`:

- run `33234248213`;
- job `99052307444`, `synthetic-v02-selftest`;
- artifact `9709418334`;
- digest
  `sha256:84a6a8c2740ad539c6a48a59e47b876122f6fd5bf4b5665e9653ecfc7c1debfc`,
  independently verified against the downloaded ZIP;
- evaluator status
  `PASS_EXP073P_AGGREGATE_JOIN_SYNTHETIC_SELFTEST_V0_2`;
- metadata-route status
  `PASS_EXP073P_ACTIONS_METADATA_ROUTE_SYNTHETIC_SELFTEST_V0_2`.

No real join was dispatched and `support_executor_authorized=false`.
Machine-readable readiness audit:
`data/derived/g7/exp073p_aggregate_join_v0_2_readiness_audit.json`.

## Exact continuation

1. Do not launch another metacal mapper while run `33222848695` is active.
2. On terminal state, capture exact Python/numpy/healpy/pip versions under the
   already-frozen runtime-provenance follow-up.
3. Require Actions success, unique non-expired artifact and exact internal
   `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` with every frozen
   byte/hash/row/mapper/repeatability/no-leakage check.
4. Only after genuine R1 PASS, record the artifact ID/digest and manually run
   the actual aggregate join v0.2 route.
5. Require `PASS_EXP073P_PREREQUISITE_BINDING_V0_2` before the separately
   frozen physical-support executor may start.
6. Covariance/whitening remains closed until explicit Exp073P physical-support
   PASS; then preserve nuisance SVD/rank -> quotient/relation/null -> fresh G8.

G7, G8 and G9 remain OPEN.
