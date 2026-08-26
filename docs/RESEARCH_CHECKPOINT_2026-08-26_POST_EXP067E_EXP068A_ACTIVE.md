# DSIR research checkpoint — post-Exp067E / Exp068A active

**Date:** 2026-08-26

## Immutable scientific state

- Exp067B remains `HARD FAIL` under its original preregistered raw-CAMB coherence threshold. Do not reclassify it.
- Exp067D causally identifies the pinned-CAMB float32-first transfer-product numerical floor.
- Exp067E is an independent prospective PASS on frozen R0/R1/R2 convention checks.
- G7, G8, G9 remain OPEN.

## Current barrier

Exp068A is the mandatory next barrier before any nuisance quotient or G7 law fit. Its frozen protocol is `experiments/068a_act_unwise_physical_forward_reproduction_v0_1.md`.

Scientific contract remains unchanged:

- pinned upstream `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`;
- pinned CAMB `fa3f097343fbbe427cc04b4f5f0041c22c6ec764`;
- official ACT×unWISE archive SHA256 `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`;
- physical linear/no-CLEFT R0 provider with independent `P_WW`, `P_Wm`, `P_mm`;
- released Blue/Green tracer kernels;
- `ell=0..6143`, `0<=z<=3`, projector `kmax=10 Mpc^-1`, Gauss-Legendre order 96;
- component tolerance `5e-13*max(1,max|reference|)`;
- no nuisance quotient, no G7 fit, no withheld-family inspection before the Exp068A outcome.

Allowed scientific outcomes are only the preregistered PASS or FAIL strings. Infrastructure failures before the science step are not scientific FAILs.

## Infrastructure chronology

The first Exp068A attempt failed before science because the GitHub-hosted runner could not establish HTTPS connectivity to the NERSC portal; all retries timed out and the frozen Python comparison never ran. This is infrastructure-only.

An infrastructure-only mirror fallback was then added: NASA LAMBDA first, NERSC second, while retaining the exact same immutable archive SHA256. No scientific parameter, tolerance, code path, data content, or acceptance criterion was changed.

Current PR: #71 `research/post-exp067e-recovery-and-exp068a-prereg`.

At this checkpoint, workflow run `33004136091` is active and is still in the official archive fetch/verification step. Therefore Exp068A has no scientific classification yet.

## Nuisance-quotient boundary already established

For the no-CLEFT branch, the four named `shift_cleft_*` directions are structurally absent/zero. Therefore a no-CLEFT nuisance Jacobian cannot legitimately be described as an 18-dimensional active tangent space; its maximum potentially active named-column count is 14 before numerical rank testing. Effective rank must be determined with a frozen SVD rule, not assumed from parameter count.

Do not build or fit this quotient until Exp068A passes.

## CLEFT solver-neutrality boundary

The public upstream CLEFT path uses a matter-to-Weyl conversion (`matter2weyl_factor`) appropriate to its baseline convention. DSIR's validated solver-neutral interface deliberately treats `P_WW`, `P_Wm`, and `P_mm` as independent inputs. Therefore the upstream CLEFT extension must not be generalized to modified-gravity/dark-sector models by silently reconstructing Weyl from matter.

Consequences:

1. Exp068A remains explicitly linear/no-CLEFT.
2. A later nonlinear/CLEFT bridge needs independent higher-order Weyl–matter ingredients or an explicitly scoped GR-only validity domain.
3. Missing nonlinear solver-neutral response remains masked, never zero-imputed.

## Exact continuation protocol

1. Inspect the active Exp068A run.
2. If infrastructure fails again before the Python comparison, repair only transport/cache infrastructure while preserving the archive SHA256 and all frozen science settings.
3. If the Python comparison executes, preserve its first scientific PASS/FAIL outcome exactly.
4. On scientific FAIL: diagnose in a separately preregistered experiment; do not alter Exp068A.
5. On PASS: only then preregister the selected 26D nuisance tangent quotient using the frozen Exp067A whitening/order. Freeze nuisance parameterization, derivative step rules, SVD rank threshold, null controls, and masks before any G7 relation is fitted.
