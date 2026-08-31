# Exp073CA attempt 3 — WSL recovery + heartbeat infrastructure preregistration v0.1

Date: 2026-09-01
Experiment: Exp073CA / Article 3 / Wm_S2 / Track-A
Classification effect of this document: infrastructure-only; +0/+0 by itself.

## Predecessor attempt-2 terminal diagnosis

- Workflow run: `33446800388`.
- Self-hosted replica-A job: `99667607114`.
- Replica A reached `Build fresh independent Wm_S2 mask PCL` and was interrupted before a complete PCL product existed.
- The GitHub job log records `The runner has received a shutdown signal` at 2026-08-31T22:45:40Z, followed by operation cancellation.
- Compile, exact checkpoint-boundary preflight, checkpoint restore, full-scale compact streaming, compact comparator, finalizers, and final comparator did not execute for a valid A/B pair.
- Replica B and all downstream jobs were subsequently explicitly cancelled after the WSL failure was diagnosed.
- Therefore attempt 2 is classified only as `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`; it is not a scientific FAIL and authorizes no readiness change.

The local Windows host reported WSL service failure `Wsl/Service/E_UNEXPECTED`. WSL was recovered by a full WSL shutdown/service restart and Ubuntu subsequently opened normally. This is an external execution-environment interruption, not evidence about Wm_S2.

## Attempt-3 scope

Attempt 3 is a prospective infrastructure-only retry of the already frozen Exp073CA scientific contract. The scientific payload, inputs, arithmetic, reduction order, thresholds, thread counts, chunking, checkpoint bytes, exact comparators, finalizer, pass/fail tokens, and authority rules remain unchanged.

The only permitted workflow change before attempt 3 is **nonclassifying observability**:

1. Add a side heartbeat process around long-running self-hosted stages.
2. Heartbeat interval must be no greater than 60 seconds while the observed child process is alive.
3. Heartbeat may read wall time and checkpoint `state.json` / completed-band metadata only; it must never access or modify scientific arrays.
4. For the PCL stage, where an exact fractional scientific progress counter is unavailable, heartbeat must explicitly report `intra_unit_progress=unknown`; it must not invent a percentage.
5. For full-scale band streaming, heartbeat may report only durable completed bands from the checkpoint state, `completed/39`, a corresponding persisted percentage/bar, elapsed wall time, thread count, and ETA only when it can be inferred from already completed checkpoint durations. While a chunk is running, intra-chunk progress remains `unknown`.
6. The heartbeat implementation must propagate the child command's exact exit status and terminate its own observer process cleanly.
7. No existing scientific source (`exp073ca_stream_general_coupling_range_v0_1.c`, `exp073ca_checkpoint_streaming_wm_s2_v0_1.py`, frozen BW helper, AZ PCL/finalizer implementation, checkpoint utility/sync utility) may be changed for attempt 3.

## Frozen scientific contract carried forward unchanged

- task `Wm_S2`; signature `(0,2,0,2)`; selected response `TE <- TE`.
- DES Y1 lens mask: 104595840 bytes, SHA-256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.
- `NSIDE=4096`, ell `0..12287`, 39 bands, selected output `<f8 [39,12288]`.
- two fresh independent replicas A and B; each recomputes its own Wm_S2 PCL.
- helper arithmetic and fixed ordering unchanged; maximum 4 bands per chunk; 8 OpenMP threads only across independent bands; BLAS-family thread counts remain 1; `OMP_DYNAMIC=FALSE`.
- checkpoint boundary remains complete-band-only; remote checkpoint restore/push semantics unchanged.
- mandatory lmax=127 exact BW-vs-range micro-preflight remains required.
- compact and final comparisons remain exact (`np.array_equal` plus canonical SHA); no tolerance, ULP, rounding, averaging, majority vote, or preferred-replica rescue.
- Exp073AQ remains historical scientific FAIL; Exp073BD remains forbidden downstream.
- no G8 jump; no readiness increment before separate frozen-ledger authorization after terminal authority.

## Attempt-3 outcome rules

- Infrastructure interruption before two valid comparator inputs: `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, +0/+0.
- Exact preflight mismatch: implementation mismatch; fail closed, no tolerance rescue.
- Complete compact A/B exact mismatch: `SCIENTIFIC_REPEATABILITY_FAIL_EXP073CA_WM_S2_COMPACT_EXACT_V0_1`.
- Complete final A/B exact mismatch: `SCIENTIFIC_REPEATABILITY_FAIL_EXP073CA_WM_S2_FINALIZER_EXACT_V0_1`.
- Success requires terminal `PASS_EXP073CA_WM_S2_CHECKPOINT_STREAMING_TRACK_A_EXACT_V0_1` and immutable run/artifact provenance; readiness may change only by a separate frozen ledger decision.

This preregistration is prospective: attempt 3 must not be triggered until the heartbeat-only workflow change and binding are committed and frozen.
