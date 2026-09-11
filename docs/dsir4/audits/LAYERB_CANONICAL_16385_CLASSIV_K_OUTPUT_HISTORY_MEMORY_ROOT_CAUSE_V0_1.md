# Layer-B canonical 16385 — CLASS-IV k_output history memory root-cause audit v0.1

Date: 2026-09-11. Scope: DSIR Article III execution/resource analysis only. Effect `+0/+0`. This audit changes no scientific threshold, lattice, estimator, physical support rule or branch outcome.

## Empirical resource evidence

Canonical-16385 telemetry on standard GitHub-hosted Ubuntu 24.04 independently reproduced memory exhaustion for all four finite-difference model roles. Python RSS grew to approximately 15.4–15.7 GB while `MemAvailable` and swap approached zero; the processes were then killed. Durable telemetry authority: `docs/dsir4/authority/LAYERB_CANONICAL_16385_GITHUB_HOSTED_MEMORY_EXHAUSTION_V0_1.json`.

This establishes a resource failure of the unmodified execution architecture, not a scientific CONVERGED/NOT_CONVERGED result and not a role-specific physical failure.

## Pinned CLASS-IV source audit

Source authority remains pinned CLASS-IV commit `ac627d54e9ce196a08878d1ba33999819925d19c`.

The `k_output_values` route has two separable effects in `source/perturbations.c`:

1. requested `ppt->k_output_values[index_k_output]` values are inserted into the internal perturbation k grid (`tmp_k_list[index_newk] = ppt->k_output_values[index_k_output]`) and mapped by `ppt->index_k_output_values[...] = index_newk`;
2. when integrating one of those requested k values, the source assigns `perhaps_print_variables = perturb_print_variables`.

The callback `perturb_print_variables` repeatedly allocates/reallocates full per-k perturbation-history storage, including `scalar_perturbations_data[ppw->index_ikout]` and corresponding size/time arrays. The header declares these storage pointers for every `_MAX_NUMBER_OF_K_FILES_` slot.

DSIR needs effect (1): exact canonical k values must be in the solver grid so `get_transfer()` can return native values at those nodes. DSIR does not consume the full time-history arrays created by effect (2).

## Prospectively frozen execution repair hypothesis

The minimal memory repair therefore suppresses only the history/printing callback for k-output integration by changing the unique active assignment

`perhaps_print_variables = perturb_print_variables;`

to

`perhaps_print_variables = NULL;`

while retaining exact k-grid insertion/indexing, CLASS integration, transfer/source generation, all canonical node bytes and every DSIR-side interpolation/finite-difference operation.

Patch implementation: `scripts/dsir4/classiv_k_output_history_suppression_patch_v0_1.py`.

## Falsification criterion

This repair is **not** accepted because it reduces memory. It is accepted only if two fresh independent canonical-8193 replicas reproduce exactly the previously verified Exp073JO numerical receipts: all eight raw A/B operand SHA256 values and both derived A/B pilot-response SHA256 values, together with canonical-node identity, lookup ceiling and lifecycle receipts.

Any one-bit numerical mismatch forbids the patch from being used for the 16385 support rung, irrespective of memory savings.

Only after exact 8193 equivalence may the same execution-only patch be tested on canonical 16385 for resource feasibility. Even a successful 16385 resource test creates no scientific convergence authority by itself.

## Scientific boundary

`REL_TOL=1e-3`, `h=1e-4`, native kpd20, canonical 8193/16385 bytes, centered-cubic interpolation, 107-row accounting and the already frozen next-rung classifier remain unchanged. Covariance restriction remains unauthorized and Wm_S3 remains unopened.
