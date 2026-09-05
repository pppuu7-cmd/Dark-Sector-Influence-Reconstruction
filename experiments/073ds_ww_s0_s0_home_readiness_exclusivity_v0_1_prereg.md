# Exp073DS — WW_S0_S0 home readiness/exclusivity v0.1

Frozen 2026-09-05 after independently validated Exp073DR hosted activation/resource PASS and before any full-resolution `WW_S0_S0` workspace or selected payload exists.

Scope: self-hosted environment/readiness support `+0/+0` only. This gate must not compute `NmtWorkspace.compute_coupling_matrix` at NSIDE=4096 and cannot create WW scientific authority.

Parent Exp073DR: run/job `33938637212 / 101231459805`, artifact `9961019381`, GitHub + independent ZIP SHA256 `eb7b74adabedc01a2f0212bc04fe612c0ae53d8156d2c904f02bc02e58d5a6c6`, raw token `PASS_EXP073DR_WW_S0_S0_HOSTED_ACTIVATION_RESOURCE_PREFLIGHT_V0_1`, durable driver SHA256 `0b7a0a2336a89dcea63060d4049d09fabacc9c5e75fad870d2599efd27d0e63b`.

## Hosted noncompetition preflight

Before requesting the home runner, inspect all queued/in-progress Actions jobs and fail closed if any other run owns a self-hosted job or runner `DSIR-HOME-PC`. This workflow itself is exempt only after its hosted job passes. No competing home control plane may exist.

## Tiny self-hosted readiness job

Use `runs-on: [self-hosted, Linux, X64]`. It must:

1. require CPU affinity count exactly 8;
2. acquire a dedicated nonblocking flock for the entire readiness section;
3. re-run live noncompetition against all other queued/in-progress runs after lock acquisition;
4. reuse/install the canonical `$HOME/.cache/dsir-nmt27` conda environment and require PyMaster `2.7` or `2.7.*`; no 2.6/3.x fallback;
5. stage exact frozen Exp073R1 artifact from run `33270843577`, artifact lineage/digest already frozen by Exp073AA, and execute only `validate_r1(...)`; do not reconstruct the dense S0 count map in this readiness gate;
6. require the committed Exp073DQ durable driver SHA256 `0b7a0a2336a89dcea63060d4049d09fabacc9c5e75fad870d2599efd27d0e63b` and Exp073DO adapter SHA256 `ab85f76e724a9861837299ce29c0961e4adcd09954b9522d678d5e610267f641`;
7. compile `ci/exp073by_mmap_full_mcm_downstream_omp10_v0_2.c` with exactly `DSIR_WORKERS=8` using the canonical NaMaster conda compiler/runtime;
8. execute only a tiny synthetic ncls=4, nb=1, L=1 identity-matrix probe and require runtime stderr `DSIR_OMP_TEAM=8` and successful output;
9. require `OMP_NUM_THREADS=8`, `OMP_DYNAMIC=FALSE`, and nested `OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=NUMEXPR_NUM_THREADS=BLIS_NUM_THREADS=VECLIB_MAXIMUM_THREADS=1`;
10. prove a dedicated readiness path under `$HOME/.cache/dsir/readiness/exp073ds-ww-s0-s0-v0-1` is writable using create/fsync/rename/read/delete, but create no science checkpoint manifest;
11. emit a receipt with `science_gate_scored=false`, `ww_authority_created=false`, `full_workspace_computed=false`, `selected_ww_payload_created=false`, plus environment/provenance evidence.

PASS token: `PASS_EXP073DS_WW_S0_S0_HOME_READINESS_EXCLUSIVITY_V0_1`.

A raw-artifact PASS authorizes only prospectively freezing and activating the **separate** full-resolution A/B scientific workflow with dedicated science checkpoint root/namespaces, exact source-head/contract/component-blob binding, durable stages, and exact terminal comparator. It does not itself score science.

Any runner loss, missing R1 artifact, environment mismatch, lock conflict, competing home job, source mismatch, compiler/runtime failure or 8-thread proof failure is infrastructure/BLOCKED `+0/+0`; never alter scientific arithmetic or criteria.