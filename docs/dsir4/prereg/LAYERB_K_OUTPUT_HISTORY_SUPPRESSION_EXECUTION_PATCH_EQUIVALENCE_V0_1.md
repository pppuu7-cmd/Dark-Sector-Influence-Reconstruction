# Layer-B CLASS-IV k_output history suppression — execution-only equivalence prereg v0.1

Date frozen: 2026-09-11. Scope: DSIR Article III execution/resource repair only. Effect `+0/+0`. No scientific branch is activated by this test.

## Motivation observed before patch design
Canonical 16385 single-role telemetry on GitHub-hosted Ubuntu 24.04 shows CLASS Python RSS increasing to about 15.5–15.7 GB, `MemAvailable` reaching ~0 and swap being exhausted immediately before the process is killed. This establishes a hosted-memory ceiling rather than a model-role scientific failure.

Source audit of pinned CLASS-IV commit `ac627d54e9ce196a08878d1ba33999819925d19c` shows that `k_output_values` does two logically separable things:
1. adds every requested k value to the internal perturbation k list;
2. for each requested k, assigns `perhaps_print_variables = perturb_print_variables`, causing full perturbation-output histories to be repeatedly appended to `scalar_perturbations_data`/related arrays.

DSIR uses `k_output_values` only to force the canonical k nodes into the solver grid and then reads transfer functions through `get_transfer`. It never consumes the full per-k perturbation-history output arrays.

## Prospectively frozen execution-only patch
Patch only the unique pinned-source assignment inside `source/perturbations.c`:

`perhaps_print_variables = perturb_print_variables;`

into

`perhaps_print_variables = NULL;`

while preserving `ppw->index_ikout`, the insertion of all `k_output_values` into `ppt->k`, perturbation integration, source tables, transfer output, CLASS commit, cosmological parameters, native kpd20, canonical node bytes and all DSIR interpolation/finite-difference arithmetic.

No other CLASS source line may change except previously authorized compatibility/d_m/capacity patches.

## Required 8193 equivalence gate before any 16385 use
The history-suppression patch is acceptable only if a fresh canonical-8193 four-role resource pilot reproduces the already independently verified Exp073JO v0.1 receipts exactly.

Fixed baseline authority: run/job `34546569386 / 103100379621`, artifact `10179564259`, result JSON SHA256 `55f30427ddd867b30cd529ab6d954064d928dcf25b7fa35dfccd0012cb6092c9`.

Required exact raw operand payload SHA256 values, in role order `reference, alpha_minus, beta_plus, beta_minus`:

- reference A `56588d01bebb122926dddeca4fd0018272c487e34e2d72b262a7d74c3362bd1c`, B `5a8fee70676c7714b615ca2286b58384512bf0c3af3e4afae57c821e72997bdf`;
- alpha_minus A `e88565c3dde3f2d4b433b646481515018148d009cb1419238c9b5c26cf0f8eb3`, B `faae61cc48893ccce204259cfff64f29912c444aea9b9e2fa3324365fa484955`;
- beta_plus A `3871f805b7a5fcf0f01091e0659d6db7aea446667048f019b3ba72f1d8284bc5`, B `1f6e10545102bdb5e7031dc7c8deff41866670f1bd82aaa967306388cf8d55b1`;
- beta_minus A `8ed59764ebe0df88eda071bac55f9705bd962acb432fe58a7d4062100d5d3c8f`, B `a5ec5824968ae8e937d783f4133c98837a0e69a691da382c8b27295ce61c53cd`.

Required exact pilot-response payload SHA256: A `e5271068b6012bc3d2432c6ed767c696975fcb1987992535a1c07eb7f2584c59`, B `506ae1cf98f70ac33f8507754f99aacc2f61f9480b099e4c1ef94023a23f94c5`.

Also require canonical 8193 node SHA `6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515`, unsupported=0, lookup<=`1e-12`, exactly four sequential constructions/max-one-live, finite operands/responses and identical fixed A/B target hashes.

A mismatch in any raw operand or response SHA is execution non-equivalence and forbids using the patch for 16385 science/resource authority.

## Resource evidence
The equivalence workflow should collect memory telemetry. Reduced memory is useful but never sufficient: exact numerical-equivalence receipts are mandatory.

## Classification
Only exact equality on all frozen numerical receipts may produce:

`CLASSIV_K_OUTPUT_HISTORY_SUPPRESSION_8193_EXACT_EQUIVALENCE_PASS_PLUS_0_PLUS_0`.

Any difference is `CLASSIV_K_OUTPUT_HISTORY_SUPPRESSION_EQUIVALENCE_FAIL_PLUS_0_PLUS_0` and creates no science authority.

Even PASS is execution/process authority only. It does not change Article III readiness, does not open Wm_S3, does not authorize covariance restriction, and does not itself activate the dormant 8193->16385 branch.
