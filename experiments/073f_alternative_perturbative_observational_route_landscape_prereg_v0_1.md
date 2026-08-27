# Exp073F — alternative perturbative observational-route landscape — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY OBSERVATIONAL CANDIDATE RANKING

## Motivation

Exp073E established that the full frozen C3 phenomenological family cannot currently be transported into the nonlinear ACT×unWISE domain by a defensible finite completion ensemble without changing/refining the model class.

The highest-value route that preserves the existing model-agnostic C3 meaning is therefore to change the **observational realization**, not the C3 nonlinear physics: identify public observables whose kernels remain inside the already-certified perturbative C3/C5 support while retaining matter and Weyl sensitivity needed by DSIR.

Exp073F is a public-data/operator landscape audit only. It does not read covariance, fit relations, choose nuisance directions, or use G8 performance.

## Frozen physical support baseline

Use the already-certified common C3+C5 linear physical support from Exp071A as the reference domain:

- lower redshift boundary `z_min = 0.295`;
- upper redshift boundary `z_max = 2.33`;
- lower physical wavenumber boundary `k_min = 0.000704833374744468 Mpc^-1`;
- upper physical wavenumber boundary `k_max = 0.06664762008318016 Mpc^-1`.

The support-leakage acceptance threshold remains the established `5%` positive-weight invalid-support fraction. Exp073F may estimate or exactly reconstruct candidate operator geometry, but may not weaken this threshold.

## Target observable structure

A candidate route must offer, either within one public likelihood/data release or a prospectively composable set of public observables:

1. at least one matter-sensitive channel;
2. at least one Weyl/lensing-sensitive channel;
3. sufficient cross-channel structure to keep `P_mm`, signed `P_Wm`, and `P_WW` conceptually distinguishable rather than imposing a matter-to-Weyl closure;
4. public/versionable kernels, redshift distributions, scale cuts or window functions adequate for a later exact support audit.

Examples that may be searched include higher-redshift galaxy/quasar samples cross-correlated with CMB lensing, low-multipole lensing-galaxy observables, spectroscopic tracers, cosmic shear/lensing combinations, or other public two-point probes. No class is preselected.

## Frozen candidate tests

F1. **Public reproducibility.** Data, window functions/redshift distributions and scale definitions are publicly accessible and versionable.

F2. **Redshift support.** Candidate tracer/lensing kernels have sufficiently small positive weight below `z=0.295` and above `z=2.33` to make a later 5% support test plausible.

F3. **k support.** Using the candidate's angular/Fourier scale cuts and physical distance mapping, the positive-weight contribution above `k=0.06664762008318016 Mpc^-1` is plausibly small enough for a later exact 5% test. Merely quoting a nominal `k_max` is insufficient if broad windows leak beyond it.

F4. **Matter/Weyl complementarity.** The route contains physically distinct matter and lensing/Weyl sensitivity; a pure matter-only observable does not qualify as a complete G7 route.

F5. **Independent cross semantics.** The observable theory can in principle consume independent `P_mm`, signed `P_Wm`, `P_WW` or equivalent independent metric/matter responses without forcing GR closure.

F6. **Linear-domain consistency.** Published scale cuts or a defensible prospective restriction permit use of linear/perturbative theory without relying on nonlinear corrections to pass the route.

F7. **Minimum information architecture.** Candidate set has enough independent released coordinates/bins/channels that a later support-validity mask could plausibly retain a nontrivial quotient/relation space; Exp073F does not inspect covariance or rank itself.

F8. **No downstream selection.** Candidate ranking may use only physical support geometry, public reproducibility and channel structure—not covariance, nuisance SVD, G7 relation residual, G8 performance or held-out metrics.

## Frozen ranking labels

For each candidate assign one of:

- `PROMISING_FOR_EXACT_SUPPORT_AUDIT` — all F1–F8 are plausibly satisfiable and exact operator reconstruction is available or obtainable;
- `PARTIAL_MATTER_ONLY`;
- `PARTIAL_WEYL_ONLY`;
- `SUPPORT_LIKELY_TOO_NONLINEAR`;
- `REDSHIFT_SUPPORT_INCOMPATIBLE`;
- `INSUFFICIENT_PUBLIC_OPERATOR_DATA`;
- `INDEPENDENCE_SEMANTICS_INCOMPATIBLE`;
- `UNCLEAR`.

## Frozen experiment classifications

If at least one public candidate route is `PROMISING_FOR_EXACT_SUPPORT_AUDIT`, classify

`PERTURBATIVE_OBSERVATIONAL_ROUTE_CANDIDATE_FOUND_EXP073F`.

If the landscape can be defended but no candidate is plausibly compatible with the frozen common linear support and channel requirements, classify

`NO_PLAUSIBLE_PERTURBATIVE_OBSERVATIONAL_ROUTE_EXP073F`.

If evidence is insufficient for a defensible landscape conclusion, classify

`INCOMPLETE_OBSERVATIONAL_LANDSCAPE_EVIDENCE_EXP073F`.

A FOUND result is not a support PASS. It only authorizes a separate prospectively frozen exact operator/support audit for the selected candidate; covariance remains forbidden until that exact physical-support gate passes.

## Downstream boundary

No covariance restriction, whitening, nuisance rank/SVD, quotient/relation/null control or G8 selection is authorized by Exp073F.

G7 OPEN. G8 OPEN. G9 OPEN.
