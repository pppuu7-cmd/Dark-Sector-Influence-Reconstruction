# Exp073JR fine-4097 hosted peak-resource audit v0.1

Date: 2026-09-11. Scope: DSIR Article III process/support only. Effect `+0/+0`.

This audit is written while the corrected JR v0.2 matrix is still running. It uses only terminal process facts, not any partial or numerical equality output from still-running jobs.

## Observed execution contrast

Exp073JQ uses the same 4097-node fine lattice, same pinned CLASS-IV lineage, same one-thread BLAS/OpenMP settings and the same model family, but holds only one CLASS instance live at a time. For example JQ reference job `103053605850` entered its numerical triple-instance control at `2026-09-10T21:21:48Z` and completed PASS at `21:26:58Z`, approximately 5m10s later.

Exp073JR v0.2 beta-minus job `103062907332` passed identity/stack/build, entered its fine control at `2026-09-10T21:53:57Z`, and received an external runner shutdown signal at `21:56:27Z`, about 2m30s into the numerical step, before any numerical receipt existed. Its distinguishing execution property is that it constructs and retains all four 4097-node CLASS instances simultaneously before querying the selected role, then would construct one single-live comparison instance.

The earlier JR v0.1 fine job `103059792478` likewise required a four-live 4097 reference context and was externally shut down during numerical execution before a receipt. By contrast the 2049-node JR v0.1 coarse job `103059792169` completed the same four-live-vs-sequential architecture and independently verified exact equality.

## Classification ceiling

These facts do **not** prove an operating-system OOM mechanism and must not be reported as such without direct telemetry. They do establish a repeated hosted execution-feasibility association with the four-live 4097 context. Therefore another blind rerun of the identical four-live 4097 architecture on the same hosted runner class is not justified merely to seek a surviving VM.

Any successor process proof must either:

1. preserve the four-live reference semantics on an execution venue with prospectively adequate and auditable resources; or
2. prospectively replace the need for a 4097 four-live dynamic proof with an independent instance-locality/source-level proof plus already frozen dynamic controls, without changing any Exp073JL scientific arithmetic, grid, threshold or observational selection.

This audit does not authorize option 2 by itself and does not change readiness. It only records that repeated external termination is a process/resource blocker, not a valid numerical NOT_EXACT result.