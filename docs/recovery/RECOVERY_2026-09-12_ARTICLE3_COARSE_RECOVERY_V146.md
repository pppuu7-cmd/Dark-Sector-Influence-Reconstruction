# DSIR Article III coarse-recovery front V146

Updated 2026-09-12. Scope: DSIR only.

## Frozen scientific frontier before terminal recovery result

The independently verified 8193->16385 result remains `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` against unchanged strict `<1e-3`.

No independently verified terminal 16385->32769 convergence result exists yet. `h=1e-4`, native kpd20, centered-cubic interpolation, lookup `<=1e-12`, 107-row parent accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0, covariance closed and Wm_S3 closed remain frozen.

## Initial production run 34695347893

The one-shot V144 production run completed without a terminal science classification. Authorization and exact response-blind plan materialization passed. All four fine-32769 operands completed successfully and were retained with exact artifact and operand hashes. All four coarse-16385 jobs were interrupted by hosted-runner shutdown during acquisition, before a final classifier could run.

Durable initial failure authority: `docs/dsir4/authority/LAYERB_16385_32769_INITIAL_PRODUCTION_INFRA_FAILURE_V0_1.json`. This is infrastructure/resource evidence only, not a scientific FAIL.

The four successful fine operands are frozen and are not to be recomputed in recovery.

## Why coarse recovery uses history suppression

The previously independently verified authority `docs/dsir4/authority/CLASSIV_HISTORY_SUPPRESSED_16385_DUAL_RESOURCE_PILOT_V0_1.json` established resource feasibility of canonical 16385 on the same hosted class when applying `scripts/dsir4/classiv_k_output_history_suppression_patch_v0_1.py`.

That exact patch changes only the perturbation-history callback from `perhaps_print_variables = perturb_print_variables;` to `perhaps_print_variables = NULL;`; `k_output_values` remain inserted into the solver grid and the patch receipt fixes `scientific_parameters_changed=false`. Frozen post-patch perturbations.c SHA256 is `4e9a419d46471ffab74df3d14239e000bf92f2e198edad4d2c7b82f1335f7a4b`.

## V145 recovery V0.1 — control-path fail before science

V0.1 recovery run `34702716166` passed preflight, built all coarse CLASS envelopes with the exact history-suppression patch, then all four coarse jobs failed before `Class.compute` because the downloaded control artifact preserved the plan as `inputs/control/plan/plan.json` while the worker argument used `inputs/control/plan.json`.

Reference causal exception: `FileNotFoundError: [Errno 2] No such file or directory: 'inputs/control/plan.json'`.

Final classifier and independent verifier were skipped. No terminal science classification was created. Durable authority: `docs/dsir4/authority/LAYERB_16385_32769_COARSE_RECOVERY_V01_CONTROL_PATH_FAILURE_V0_1.json`.

Silent rerun was not used.

## V146 recovery V0.2 — active

Prospectively frozen repair contract: `docs/dsir4/contracts/LAYERB_16385_32769_COARSE_RECOVERY_CONTRACT_V0_2.json`, creation commit `91cd509cb0d46726b173a33b8a6a1aefb0957531`, contract blob `732fa2668bfc7af66131cc1cab5e6db793637e5e`.

Recovery workflow: `.github/workflows/layerb-16385-32769-coarse-recovery-v0-2.yml`, creation commit `7db695b726d4365b03db31cf8515e099a0722092`, workflow blob at launch `52ebb19ef4c6cff894336258e76489101f0ee9b1`.

One-shot launch sentinel commit: `5e9adb306a3f9541afed236553926229ecc09ca9`.

Active recovery run: `34702943923`.

Preflight job `103577799082` is PASS. Four coarse roles are running in parallel:
- beta_plus `103577831090`
- reference `103577831101`
- alpha_minus `103577831124`
- beta_minus `103577831283`

Each coarse role uses canonical 16385, point capacity 16385, parser capacity 524288, pinned CLASS commit `ac627d54e9ce196a08878d1ba33999819925d19c`, and the exact independently validated history-suppression patch. Fine recomputation is forbidden.

The V0.2 repair changes only the control plan path from `inputs/control/plan.json` to `inputs/control/plan/plan.json` plus retry-run guard semantics. Frozen response worker, adapter, recovery classifier, terminal consumer and scientific thresholds remain bound.

Independent V0.2 static audit run `34703048335` is terminal PASS after one audit-harness-only assertion repair. Final successful run head `4671539e43339afddfaedf91e487063d3e793b4b`; aggregate artifact `10301255917`, ZIP SHA256 `1cca5ae736c90e9ebf6f1630dfc4c892c18cbb73f9245622f27ce084a3cce899`, raw `static.json` SHA256 `bd2d0a2009179eed8f6e80a81847ba1de8d4d15cb994be342ea9da6f1f0a8b03`, missing receipts `[]`.

Durable static authority: `docs/dsir4/authority/LAYERB_16385_32769_COARSE_RECOVERY_V02_STATIC_AUDIT_V0_1.json`, creation commit `05a4d8391a0d61c70d5e9aec0d5117fe3a4b1a4a`.

## Required next order

1. Continue run `34702943923`; do not launch another recovery/science run.
2. Require all four coarse role operands to finish successfully and inspect their raw artifacts/resource telemetry.
3. Let the same workflow provenance-rebind the four retained fine operands without changing response/valid-mask payload hashes.
4. Run exactly one frozen classifier with strict `<1e-3`.
5. Require the fresh-runner independent terminal verifier PASS.
6. Download and independently inspect terminal science artifacts before creating durable scientific authority or changing publication/scientific readiness.
7. No silent retry after V0.2. Any infrastructure failure requires a new prospective contract.
8. Covariance and Wm_S3 remain closed regardless of the convergence outcome until their own gates.

## Readiness before terminal V146 result

`ARTICLE3_REPOSITORY_READINESS: 68%`

Scientific/funnel frontier: `67%`

Operational roadmap: `95%` (recovery path and independent static authority are closed; terminal 16385->32769 science remains pending).

## Automation state

`DSIR Continuous Research` remains disabled because all five account automation slots are occupied by other active research tasks. GitHub Actions run `34702943923` is the active DSIR computation mechanism.
