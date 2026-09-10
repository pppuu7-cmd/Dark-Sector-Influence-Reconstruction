# Exp073JL — two hosted-runner shutdowns retrospective v0.1

Date: 2026-09-11. Scope: DSIR Article III execution history only. Effect `+0/+0`.

This retrospective creates no scientific authority and does not change the prospectively frozen Exp073JL classifier. Its purpose is to close an execution-history gap before any recovered one-live JL is designed.

## Attempt 1

Workflow/run: `exp073jl-article3-layerb-common-grid-third-refinement-convergence-v0-1 / 34497160814`, attempt 1, job `102938434376`, head `d556db87763637dd90ed919dbe5d85ef95b4beb1`.

All deterministic setup/input gates had passed and the frozen numerical step was active when the GitHub-hosted runner reported a shutdown signal at `2026-09-10T15:56:49Z`. No JL result artifact was emitted. Existing recovery V79 correctly classifies this as infrastructure failure `+0/+0`, neither CONVERGED nor NOT_CONVERGED.

## Attempt 2

The exact same frozen run was rerun as attempt 2, job `102944693569`, same workflow/head. Contract/authority gate, numerical stack, frozen CAMB checkout/install, pinned capacity-patched CLASS-IV build, DES payloads, Layer-A/angular/Exp073IM authorities and BOSS z3 operators all completed successfully.

The frozen numerical command entered at approximately `2026-09-10T15:59:22.65Z`. At `2026-09-10T16:10:29.64Z`, while that numerical step was still active, the GitHub-hosted runner again reported: `The runner has received a shutdown signal`, followed by operation cancellation. Artifact upload was skipped and no scientific JL result was produced.

Therefore attempt 2 is also infrastructure failure `+0/+0`, neither CONVERGED nor NOT_CONVERGED.

## What can and cannot be inferred

Two shutdowns during the numerical step establish that simply repeating the historical execution architecture is operationally unreliable on the observed hosted-runner path. They do **not** by themselves prove out-of-memory, a CLASS numerical defect, or any particular causal resource mechanism: GitHub's emitted condition is a runner shutdown signal, not a scientific/numerical classifier.

Independent source audit shows that the historical common-grid parent constructs four CLASS instances per `ResolutionSuite` and the full parent instantiates the suite three times: coarse DES+GL64, fine DES+GL64, then fine GL128. The corresponding historical lifecycle is 12 solver constructions with up to four live simultaneously.

The subsequently established JQ/JR/JS/JT/JU/JV execution/canonicalization lineage and prospectively frozen JW eight-build one-live resource pilot are therefore the appropriate route for testing a lower-lifetime execution architecture without changing scientific content. A third blind rerun of the historical 12-build/4-live JL architecture is not justified by these records.

## Scientific boundary

Nothing in this retrospective changes `REL_TOL=1e-3`, `h=1e-4`, native kpd20, canonical 2049->4097 science, domain, masks, 107-row traversal/accounting, estimator, interpolation, covariance restriction status or Wm_S3 status. `ARTICLE3_REPOSITORY_READINESS` remains 68% and funnel-freeze readiness remains 67% until a terminal frozen gate supplies new scientific/process authority according to the ledger.
