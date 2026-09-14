# Independent DSIR Funnel Audit — V0.25 interpolation-remedy benchmark

Date: 2026-09-15. Scope: DSIR only. Role: independent Funnel Auditor / Critic.

Reviewed terminal result: `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED` from V0.25 run `34896282790`, terminal authority `docs/dsir4/authority/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REMEDY_BENCHMARK_V0_25.json`.

## Scope and gate-chain audit

V0.25 was correctly authorized by terminal V0.24 authority `LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_V0_24.json`, whose encoded next stage exactly matched the V0.25 remedy benchmark. V0.25 preregistration was committed at `4a1247c56cfbe293a5203ca0b44968ae13aacade`, executor at `03cbd910774aa365859abaff18496b01b22bc24d`, frozen contract at `876b56589d61b263a569583e7cb69e887d68d326`, workflow at `f63156fa1adaeb61e496cc5259cf77a584496612`, and launch only afterward at `05c87c85093142cfca4d0a432269d5f2440a6e88`. No post-result threshold/candidate/panel retuning was found.

The launch-head workflow has the required `remedy-lane: needs: invariant-audit` barrier and `decision: needs: [invariant-audit, remedy-lane]`. The terminal run is `run_number=1`, `run_attempt=1`, push-triggered from the frozen launch head. A head-SHA run query returned exactly one workflow run for the launch commit. Thus no favorable rerun selection was found.

The run has 34 terminal jobs: invariant, 32 substantive lanes, decision. The decision job downloaded exactly 33 prerequisite artifacts (invariant + 32 lanes) before executing the frozen classifier. The terminal decision artifact is ID `10370496892`; its Actions ZIP digest is `sha256:7fcb329027fad04425802f4a90b7874baa2a25e949fbc1057db1a3ed70546562`, matching the producer authority.

## Independent artifact inspection

The terminal Actions artifact was downloaded independently from artifact ID `10370496892` and inspected byte-for-byte.

- ZIP SHA256: `7fcb329027fad04425802f4a90b7874baa2a25e949fbc1057db1a3ed70546562` — matches Actions metadata and the producer authority.
- ZIP contains exactly `decision.json`.
- `decision.json` byte length: `11082`.
- Actual artifact-internal `decision.json` SHA256: `5bcc9d93c22d32ace5d97f78ff9ce89b399cc4c7e4377b174c5fe882869dd71f`.
- Producer authority, recovery, current-process ledger and Researcher handoff instead record `f3d0f47c02c20f39da0fcd71e28665308d53ab8386c876776d3f64da6a7d4bb8` as the inner decision SHA256.

This is a direct hash/provenance contradiction.

The repository file presented as the raw V0.25 decision, `results/dsir4/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REMEDY_BENCHMARK_V0_25_DECISION.json`, is also not the complete artifact decision. The frozen executor emits `primitive_response_metrics`; the actual artifact contains 36 top-level keys and a 24-entry `primitive_response_metrics` array, whereas the persisted repository decision has 35 top-level keys and omits exactly `primitive_response_metrics`. All shared top-level fields inspected agree; the missing object is therefore a provenance/completeness defect rather than evidence that the classifier was altered.

## Independent classifier / numerical audit

The actual terminal artifact contains all 24 preregistered primitive-response reproducibility metrics. Every one has `reproducible=true`, cross-host maximum pairwise relative spread `0.0`, and native-class mean relative separation `0.0`. This independently supports the technical reproducibility predicate encoded in the frozen classifier.

The six-cell frozen panel is consistent with the preregistered decision logic. `EXACT_TARGET_UNION` has relative difference `0.0` to the fresh direct reference on every one of the six panel cells and passes the frozen mixed-node-set safety criterion. `ONE_STEP_GRID_REFINEMENT` is an explicit negative-control/counterexample to generic grid-refinement sufficiency: original `GRID768/T3` remains at `0.001136253405249066`, above the unchanged `<1e-3` remedy threshold. Both parent gating violations reproduce. Therefore the terminal numerical classification itself is not refuted by this audit.

The result remains strictly numerical/reproducibility scoped. Exact-target/direct agreement does not establish statistical/model validity, nuisance removal, physical identifiability, or a dark-sector signal. The six-cell panel does not establish full 107-row Layer-B behavior. The common direct and exact-target-union CLASS implementation also means their agreement is not an independent physical/model cross-check; it specifically tests the interpolation construction under the frozen solver state.

## Alternative explanations and successor risks

The V0.24/V0.25 evidence strongly rejects cubic common-grid interpolation as harmless at the two parent cells and supports exact requested-node extraction as the local remedy. It does not establish that all retained Layer-B rows are free of other resolution, tolerance, target-binding, boundary-stencil, or solver-state pathologies. The successor must therefore remain a numerical replay gate, not a science gate.

The successor must also freeze exact-target-union semantics prospectively. V0.25 tested union of each common grid with all three frozen benchmark target k values. A future 107-row replay must not silently substitute target-local unions, post-result row selection, or a different global node construction. The existing `1025 + 107 = 1132 < 1152` statement is only a static capacity bound, not validation of a 107-row construction.

The workflow installs `scipy` without an exact version pin. Within V0.25, the software-control identity is constant and the measured responses are exactly reproducible, so this does not invalidate the executed benchmark. It should nevertheless be hardened in any successor contract to reduce future environmental ambiguity.

## Verdict

`INVALID_PROVENANCE`

This verdict applies to the producer authority's artifact-to-repository provenance binding, not to the frozen numerical classifier. The numerical result is semantically supported by the actual terminal artifact, but the current terminal authority cannot serve as a clean provenance anchor for a successor while it asserts an incorrect inner SHA256 and points to an incomplete file as the raw decision.

Do not overwrite or erase the historical V0.25 authority or result. Preserve them and add a corrective provenance authority/reconciliation that binds the exact terminal artifact bytes (or an exact durable byte-identical materialization) to artifact ID `10370496892`, ZIP digest `7fcb329027fad04425802f4a90b7874baa2a25e949fbc1057db1a3ed70546562`, and actual inner `decision.json` SHA256 `5bcc9d93c22d32ace5d97f78ff9ce89b399cc4c7e4377b174c5fe882869dd71f`.

Until that repair is terminal and recovery/process are reconciled, the encoded full-Layer-B successor is suspended. No 107-row traversal, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537, or downstream science gate is admissible.
