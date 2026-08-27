# Exp073E — C3 nonlinear-completion model-class boundary — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp073E DESIGN CLASSIFICATION

## Motivation

Exp073D classified the frozen C3/GDM family as non-identifiable beyond linear order while C5/f(R) remains a defined nonlinear theory in principle.

Because Exp073A already excludes the current ACT×unWISE linear/no-CLEFT route and Exp073D forbids hiding an arbitrary nonlinear closure inside “the C3 provider”, the next question is whether DSIR can enlarge C3 in a controlled way without destroying the model-agnostic meaning of the reconstruction.

Exp073E is a model-class design-boundary audit. It does not choose a completion using observational performance and does not certify a nonlinear provider.

## Frozen question

Can a finite, explicitly labelled nonlinear-completion ensemble be attached to the frozen C3 linear GDM family such that:

1. every completion reduces to the same frozen C3 background/linear semantics on the already-certified perturbative domain;
2. the completion identity and any new nonlinear parameters are explicit coordinates of the model class rather than hidden provider choices;
3. the ensemble spans materially distinct nonlinear stress/metric behavior rather than duplicate implementations;
4. no completion is selected or weighted using ACT covariance, G7 relation residuals, G8 performance or held-out data;
5. the resulting family remains suitable for DSIR influence reconstruction rather than collapsing into a single microphysical prior.

## Candidate completion classes to audit

The following classes are frozen as the minimum conceptual landscape; none is preselected as preferred:

A. **collisionless-initial-condition continuation** — nonlinear N-body evolution whose main GDM imprint is encoded in GDM-modified linear initial conditions, with explicit statement of which pressure/shear effects are subsequently neglected;

B. **halo/spherical-collapse GDM completion** — a phenomenological halo-model continuation based on GDM spherical-collapse/halo prescriptions;

C. **effective nonlinear stress-tensor/EFT completion** — a fluid/EFT extension in which nonlinear pressure, anisotropic stress and effective coefficients are explicitly specified;

D. **microphysical embedding completion** — one or more concrete dark-matter theories mapped onto the same frozen linear GDM response coordinates but carrying their own nonlinear dynamics.

A candidate class may be marked unavailable if primary theory/public implementation evidence is insufficient. Exp073E does not require that all four classes be numerically executable.

## Frozen compatibility tests

E1. **Linear-limit preservation.** Each admissible completion must have a definable limit reproducing the same C3 background and linear `D_m`, `phi`, `psi` / `P_mm,P_Wm,P_WW` semantics on the previously certified domain. A qualitatively similar matter spectrum is not sufficient.

E2. **Explicit completion identity.** Completion class and any additional nonlinear parameters must be visible in metadata/model coordinates and recoverable from artifacts. No provider-internal default may silently determine them.

E3. **No hidden GR Weyl closure.** A completion must specify how nonlinear metric/Weyl fields are obtained. Generic GR matter-to-Weyl closure is not permitted unless it follows from the completion's own stress-energy/gravity assumptions and is recorded as such.

E4. **Distinctness.** At least two admissible completion classes must differ in nonlinear physical assumptions, not merely numerical implementation, for an ensemble to represent completion uncertainty.

E5. **Prospective weighting.** Initial ensemble weights, if any, must be theory-defined (for example equal/discrete or separately justified priors) before ACT/G7/G8 output. Performance-based reweighting is forbidden at this stage.

E6. **Provider-certifiability.** Each admissible class must expose, in principle, a route to independent nonlinear `P_mm`, signed `P_Wm`, and `P_WW` with support and validation boundaries that could be tested in a later provider-certification experiment.

E7. **DSIR identifiability semantics.** The inverse reconstruction must be able to distinguish uncertainty due to dark-sector influence coordinates from uncertainty due to nonlinear completion identity; they may not be collapsed into one fitted response without bookkeeping.

E8. **No downstream leakage.** No covariance, whitening, nuisance rank/SVD, G7 relation/null, G8 response or article selection may be used.

## Frozen classifications

If at least two physically distinct completion classes satisfy E1–E8 in principle and can be represented explicitly as a completion ensemble, classify

`EXPLICIT_C3_NONLINEAR_COMPLETION_ENSEMBLE_FEASIBLE_EXP073E`.

If only one defensible nonlinear completion class can be formulated or all available choices necessarily replace rather than extend the frozen C3 semantics, classify

`C3_COMPLETION_ENSEMBLE_NOT_FEASIBLE_EXP073E`.

If primary theory evidence is insufficient to defend either conclusion, classify

`INCOMPLETE_C3_COMPLETION_DESIGN_EVIDENCE_EXP073E`.

## Downstream consequence

A FEASIBLE result does not authorize nonlinear provider use. The next step must separately freeze the smallest candidate completion set and provider-certification tests, including linear-limit recovery, native support, signed Weyl cross-power, PSD/coherence, repeatability and no extrapolation.

A NOT_FEASIBLE result means the current phenomenological C3 family cannot be carried into the required nonlinear ACT×unWISE domain without replacing its model definition; DSIR would then need microphysical training families or a different observational channel/domain.

No covariance restriction or later G7 stage is authorized by Exp073E itself.

G7 OPEN. G8 OPEN. G9 OPEN.
