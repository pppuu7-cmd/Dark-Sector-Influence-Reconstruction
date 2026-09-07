# Exp073GO — C2 IDE perturbations translation-unit ABI equivalence v0.1

Status: PROSPECTIVELY FROZEN after Exp073GN baseline full-build BLOCKED. Scope: DSIR only. Scientific contribution ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Why this is a new gate, not a rescue of GN

Exp073GN run `34098746873`, job `101668107470`, failed while building the **uninstrumented pinned baseline**, before any instrumented compilation. The first causal errors are pre-existing syntax errors in pinned `source/background.c` (`case IDM_IV` outside a switch and consequent parse failures). Therefore GN full-executable build equivalence is `BLOCKED_UPSTREAM_BASELINE_BUILD_PLUS_0_PLUS_0`; it is not scored PASS and is not rewritten.

The GM hook changes only `source/perturbations.c` plus a diagnostic header. GO asks the narrower prospective implementation question that is actually identifiable without modifying the pinned upstream baseline: do the uninstrumented and exact GM-instrumented `perturbations.c` translation units both compile under the same hosted compiler flags, with only the frozen no-op observer ABI added to the instrumented tree?

No source repair to `background.c` or any other upstream file is permitted.

## Frozen procedure

1. Clone two exact checkouts of `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.
2. Apply the exact committed GM transformer only to the instrumented `source/perturbations.c` and copy the exact GN no-op observer header.
3. Re-run the GM source-equivalence auditor.
4. Compile only target `perturbations.o` in the baseline tree with the pinned Makefile/toolchain.
5. Compile only target `perturbations.o` in the instrumented tree under exactly the same flags plus `DSIR_C2_PRETRANSFORM_HOOK`.
6. Require both object files to exist and be non-empty; record SHA256 identities. Object SHA equality is **not** required because the diagnostic call is intentionally present in the instrumented translation unit.
7. No executable link, cosmological run, prediction generation, or scientific output is allowed.

## Classification

Exact PASS token: `PASS_EXP073GO_C2_IDE_PERTURBATIONS_TU_ABI_EQUIVALENCE_V0_1`.

PASS is only `SUPPORT_PLUS_0_PLUS_0`: `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`. It may authorize a separately prospectively frozen recorder implementation/audit. It does not authorize C2 numerical prediction generation.

Any compile/ABI/source/dependency failure is implementation/infrastructure `+0/+0` or invalid-for-science, never scientific model FAIL.
