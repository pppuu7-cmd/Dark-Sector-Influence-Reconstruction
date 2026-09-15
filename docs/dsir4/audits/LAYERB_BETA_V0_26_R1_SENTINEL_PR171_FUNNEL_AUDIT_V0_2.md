# DSIR Funnel Audit — V0.26 R1 pre-full sentinel PR #171, V0.2

Date: 2026-09-15  
Scope: DSIR only. Numerical/reproducibility funnel only.  
Reviewed candidate: PR #171 `Construct DSIR V0.26 R1 pre-full sentinel candidate`, exact head `973eea003e6e246b7e1853b5469cb0a7d90c8177`, base main `438ab2e6732512cf50c163719ade01575257b209`.

## Review target

This review audits only the prospective 32-lane sentinel implementation and its response-blind static evidence. It does not execute CLASS, read a scientific response, read covariance, or authorize the sentinel science run or the full 107-row replay.

The governing main authority is `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_PR169_FUNNEL_QUALIFICATION_V0_1.json`, git blob `cdbcea2622564d40aa9d1edc045a5808f8cdd1c4`. That terminal audit authority permits construction of the sentinel executor/workflow for response-blind static audit only after exact R1 promotion; it explicitly keeps sentinel science execution and the full 107-row replay closed.

## Authorization and prospective ordering

PR #169 was independently qualified before its exact R1 blobs were promoted to main. Main now contains the exact R1 preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and machine contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`. PR #171 branches from that promoted main and only constructs the already-preregistered sentinel implementation.

The scientific object, sentinel selections, power rule, technical threshold `<1e-5`, scientific numerical threshold `<1e-3`, requested-node binding `<=1e-12`, route-specific beta tolerance `1e-12`, GRID896 identity, source-plan identity, and 32-lane/14-construction-per-lane design were frozen in R1 before PR #171 implementation construction. I found no post-response threshold tuning because no sentinel scientific response has been executed.

The PR adds seven files only and modifies no historical result or terminal authority. The active science workflow `.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml`, sentinel launch authority, and launch descriptor are absent.

## Code and input identity

Final candidate implementation blobs are:

- executor `ci/layerb_beta_v026_r1_sentinel_v0_1.py`: `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`;
- decision finalizer `ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py`: `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`;
- inert workflow blueprint: `1ed36c850d80537646556a858204cac14eca852e`;
- sentinel implementation contract: `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`;
- response-blind static auditor V0.2: `ebb1db6b365560e9e4c8ab7e575d163bdab58cc4`.

The executor independently rebinds the exact R1 contract and promotion authority, verifies the exact source-plan bytes and call digests, reconstructs the frozen mixed/direct plans, verifies the exact NumPy-1.26.4 GRID896 binary64 SHA256 before any CLASS solve, and checks the frozen sentinel batch identities. The apparent absence of `NPY_DISABLE_CPU_FEATURES` from the inert workflow environment is not an implementation defect: the lane process obtains an unmasked native fingerprint, then launches the forced preflight and substantive child as fresh subprocesses with exactly the frozen non-AVX512 mask. The child checks the mask before NumPy/CLASS-dependent scientific work and revalidates the forced dispatch profile.

The child uses exactly 14 CLASS constructions, applies beta `tol_perturb_integration=1e-12`, preserves `h=1e-4`, reconstructs exact requested nodes, measures exact-node mismatch, and emits all primitive records for pure-common, mixed-common, exact-target, and direct responses. It explicitly records that full 107-row traversal, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 and downstream science were not opened.

The finalizer requires exactly 32 unique replicate documents, rejects missing/duplicate replicate identities, enforces frozen requested-node counts and solver count, requires one binary and one software-control identity across eligible lanes, enforces minimum 6 eligible with at least 3 native-AVX512-active and 3 native-AVX512-inactive, computes complete primitive-response reproducibility metrics, and evaluates the strict frozen numerical gates. Its output always leaves `full_replay_launch_authorized=false` and `full_107_row_execution_authorized=false` even if the sentinel classifies `SENTINEL_PASS`.

## Hosted response-blind static evidence and provenance

Hosted static run `34958187529` is terminal `success`, run number 1 / attempt 1, event `push`, exact execution head `510a7145bd5ea49e45db3ab53e56093567da746f`. Job `104345200819` completed successfully. The final candidate preserves the audited executor/decision/blueprint/contract blobs.

Artifact `10392400462` has Actions ZIP digest `sha256:2384436ee78a9a1ee4d55e5297e3b36f2dff9ffe53a243e20af0b2f7dfe729f0`. Independent download reproduced that ZIP SHA256. Members independently verified:

- `sentinel_static_audit.json`: 1344 bytes, SHA256 `33972dc25eabb7a19097164234b5e336d4bc4bd3cfef37ff8a442443810b75a8`;
- `executor_static_preflight.json`: SHA256 `63429e12875545d0a3d0be01882c6bf9b71dd5e26a840fe739b969fa3f5be3bb`;
- `lane_without_authority.txt`: SHA256 `8ebb37d6a3d51d46e259f2eb66d5622162a5494cc94f085c52534d501208991d`.

The receipt reports no active science workflow, no launch authority, no launch descriptor, no CLASS solve, no scientific response read and no covariance read. The negative-control lane invocation without a launch authority fails before producing a lane artifact with `RuntimeError: sentinel science launch authority is required and absent`. This is a concrete fail-closed counterexample against accidental execution.

The source plan remains artifact `10298655751`, ZIP SHA256 `9b8bdcf03cb05bc979e8c72135acac92232864a74dc1d510b579d8efb5cbb2a7`, inner `plan.json` 3,953,984 bytes SHA256 `c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064`. Its inheritance remains scoped to the successful materialization job of the historically failed source run.

## Independent external funnel receipt and additional counterexample

A separate response-blind funnel audit run `34958540961` is terminal success, run number 1 / attempt 1, job `104346337918`. Artifact `10392755109` has Actions ZIP digest `sha256:8fade9139142e2ab3f6a99ef2696853d3f5dce026c6fa130a43d96bff6870edb`; independent download reproduced that digest. Its `funnel_audit.json` is 1848 bytes SHA256 `ac2c2cc9d2aa536207a8ee5121cb37d92665f521cb6e0ef41865540810ded333` and also returns `QUALIFIED`.

That external receipt correctly identifies a launch-binding hardening need, but one proposed requirement is itself overconstrained: it asks both that the future launch authority bind the exact launch-descriptor git blob and, via the current blueprint, that the launch descriptor bind the exact launch-authority git blob. Two files cannot in general contain each other's final cryptographic git-blob hashes without a hash fixed point. Treating both directions as mandatory would create an unrealizable circular provenance contract.

The required correction is an acyclic provenance DAG, not weaker provenance. Freeze the active workflow first. Then create a launch authority that binds the exact R1 contract, promotion authority, executor, decision finalizer, and active-workflow git blob and authorizes exactly one sentinel science execution while explicitly keeping full-107 false. Then create the launch descriptor after that authority; the descriptor binds the launch-authority git blob and active-workflow blob. The authority must not simultaneously require the descriptor's final blob. An equivalent reverse DAG is admissible only if it avoids mutual blob-hash binding. A separate static launch-package audit must verify the chosen DAG before science execution.

This counterexample does not invalidate PR #171's current static implementation because none of the circular launch objects exists in PR #171 and no science run has been authorized. It does qualify the next-stage wording and forbids mechanically copying the circular two-way hash requirement into a launch package.

## Alternative explanations and overclaim audit

No scientific sentinel value exists to interpret, so interpolation, solver tolerance, execution-order, host nondeterminism, look-elsewhere, nuisance, covariance or external-systematic explanations cannot yet be adjudicated as scientific outcomes. The present evidence only demonstrates implementation identity, fail-closed launch behavior and response-blind static consistency.

Green CI is not a scientific PASS. The static audit PASS is not sentinel numerical PASS. A later sentinel PASS would still be numerical/reproducibility evidence only and would require a separate independent sentinel-result audit plus explicit full-replay launch authority before any full 107-row execution. No covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537, statistical/model gate or physical dark-sector inference is opened here.

## Verdict

**QUALIFIED**.

PR #171's exact implementation blobs and hosted response-blind static evidence are consistent with the prior construction authority and may be promoted as a pre-full sentinel implementation candidate. The qualification is prospective launch-governance only: future launch-package provenance must use an acyclic exact-hash DAG and receive a separate static launch-package audit before any sentinel CLASS solve.

Scientific effect remains `+0/+0`; repository readiness remains 68%; scientific frontier remains 67%.

## Authorized next stage

Promote only the exact qualified PR #171 implementation blobs after this audit authority is durable. After promotion, construct an **inactive** active-workflow/launch-authority/launch-descriptor package with acyclic exact hash bindings, then independently audit that launch package response-blind. Do not run a sentinel CLASS solve from this audit. Do not run the full 107-row replay from this audit.