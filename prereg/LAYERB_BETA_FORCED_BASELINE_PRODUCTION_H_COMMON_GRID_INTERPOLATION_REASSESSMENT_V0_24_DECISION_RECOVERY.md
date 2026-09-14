# DSIR V0.24 decision-only recovery preregistration

Status: **PROSPECTIVELY FROZEN BEFORE RECOVERY EXECUTION**. Date: 2026-09-14. Scope: DSIR V0.24 infrastructure recovery only.

## Source execution

- Source workflow run: `34884436750`.
- Source head SHA: `3a655cf12614955716898c7943e5d638d6a1cf1f`.
- Frozen scientific preregistration: `prereg/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_V0_24.md` at the source head SHA.
- Frozen classifier/executor: `ci/layerb_beta_forced_baseline_production_h_common_grid_interpolation_reassessment_v0_24.py` at the source head SHA.
- Frozen contract: `docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_V0_24.json` at the source head SHA.

The source run completed the invariant audit and all 32 hosted interpolation lanes and uploaded their artifacts. The terminal `decision` job failed before scientific classification because it invoked the frozen V0.24 Python executor with the runner system Python, while that executor imports NumPy at module import time and the decision job had not installed NumPy. This is an orchestration dependency failure, not a scientific classifier outcome.

## Recovery scope

The recovery SHALL:

1. execute no CLASS solve and no V0.24 lane;
2. consume only the source-run invariant artifact and the 32 source-run lane artifacts;
3. checkout the exact source head SHA for the contract, executor and inherited source identities;
4. install only the Python dependency required to import and execute the already-frozen decision classifier (`numpy==1.26.4`);
5. re-run the frozen V0.23 provenance check used by the original decision job;
6. invoke the exact V0.24 executor in `--mode decision` over the 32 recovered lane JSON files;
7. preserve every V0.24 threshold, hierarchy, parent cell, power requirement, source identity, runtime-class requirement and interpretation ceiling unchanged;
8. emit a separate recovery provenance record binding the result to source run `34884436750`, source head SHA, source artifact IDs/digests, and this recovery execution.

## Forbidden

The recovery SHALL NOT rerun or substitute any scientific lane, regenerate responses, retune thresholds, change parent cells, change the direct-node or mixed-node semantics, change production h, change the forced NumPy mask, edit lane JSON, import historical numeric values as classifier inputs, or reinterpret the frozen decision hierarchy.

If any required source artifact is absent, expired, duplicated, or not bound to the source run, recovery MUST fail rather than reconstruct or replace it.

The scientific interpretation remains exactly that of V0.24. Effect remains `+0/+0`; no covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537, or full Layer-B traversal is authorized by recovery itself.
