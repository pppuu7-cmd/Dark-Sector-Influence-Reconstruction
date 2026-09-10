# Exp073JO Article III JL slot20 per-model sharded recovery V0.4

Status: PROSPECTIVELY FROZEN EXECUTION/RESOURCE REPAIR. DSIR only.

## Trigger and classification
JO v0.3 run 34512184648 repeatedly lost GitHub-hosted runners during the exact 4097-node numerical phase before any phase artifact was created. The third fresh-tail attempt, job 103026063803, passed all frozen guards/dependencies/pinned CLASS-IV build and then received an external runner shutdown at 2026-09-10T20:01:32Z. This is infrastructure INVALID_INFRA_PLUS_0_PLUS_0. It is not a scientific/history-control FAIL and does not modify any frozen acceptance criterion.

Blind repetition of the same monolithic hosted phase is forbidden.

## Frozen science retained exactly
This repair changes execution topology only. Preserve exactly: native CLASS k_per_decade_for_pk=20; base geometric lattice N=4096 plus the prospectively admitted single upper guard node, total 4097 requested nodes; centered-cubic ln(k) interpolation; h=1e-4; REL_TOL=1e-3; the same baseline and precision files; the same pre_z/tail_z and pre_targets/tail_targets; the same pinned CLASS-IV source commit ac627d54e9ce196a08878d1ba33999819925d19c; capacity 4608; parser argument capacity 131072; and the same response definition inherited from ci/exp073jj_article3_layerb_common_grid_resolution_refinement_convergence_v0_1.py.

No tolerance, rounding, smoothing, averaging, effective k/z/ell, fiducial-P shortcut, or scientific-domain change is permitted.

## Execution repair
The original ResolutionSuite owns four independent CLASS model instances in the fixed order:
0 = reference (alpha=0,beta=0)
1 = alpha-minus (alpha=-h,beta=0)
2 = beta-plus (alpha=0,beta=+h)
3 = beta-minus (alpha=0,beta=-h).

V0.4 executes each model in a separate hosted job. Each shard uses exactly the same class_params, requested_values and cubic_centered functions from the frozen JJ response engine. For slot20_fresh_tail, the shard performs only get_transfer/interpolation at tail_z. For slot20_after_history, the same shard/model instance first performs get_transfer/interpolation at pre_z and then performs tail_z. Thus the history intervention is preserved within each exact CLASS model while eliminating the monolithic four-model lifetime that repeatedly exceeded hosted-runner survivability.

Each shard emits exactly four little-endian float64 tail interpolants plus immutable model/phase/lattice/provenance metadata. It does NOT emit a scientific classification.

## Fail-closed reconstruction/equivalence guard
Aggregation is permitted only when exactly 8 unique receipts exist: 2 phases x 4 model roles. Every receipt must match phase, model parameters, node SHA256, target/z hex identity, CLASS source/capacity identities, and raw payload SHA256.

For each phase, reconstruct the original frozen response exactly as:
alpha_component = abs((alpha_minus - reference)/(-h))
beta_component = abs((beta_plus - beta_minus)/(2*h))
column_stack(alpha_component,beta_component), dtype <f8, shape [4,2].

A static/synthetic equivalence guard must demonstrate that this reconstruction is byte-identical to the frozen JJ response algebra for finite deterministic test vectors before any production receipt is accepted. Any missing/duplicate/mismatched shard is fail-closed infrastructure/BLOCKED, never a scientific result.

The two reconstructed 64-byte phase responses must then satisfy exact np.array_equal, identical finite masks and identical positive masks. Failure of this exact equality after all provenance guards is a valid frozen JO negative result. PASS remains support-only +0/+0 and creates no scientific model authority, no covariance authority and no Wm_S3 authority.

## Resource semantics
GitHub-hosted jobs remain single outer processes with OMP/OpenBLAS/MKL/NumExpr threads pinned to 1. No home/self-hosted runner is used by this gate. Complete model shard is the durable unit: successful shard artifacts are individually reusable; failed shards may be rerun individually without recomputing verified siblings.

## Authority boundary and next action
Only an independently verified V0.4 aggregate exact PASS may admit JO aggregate authority and unlock exactly one checkpointed JL recovery under its already-frozen source-bundle/topology guards. Valid recovered JL CONVERGED activates only JN; valid NOT_CONVERGED activates only JM; infrastructure failure activates neither.
