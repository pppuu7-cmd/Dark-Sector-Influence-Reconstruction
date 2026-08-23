# DSIR research log

Scientific claims are controlled by `docs/GATES.md`.

## 2026-08-24 — repository separation and baseline gates
Dedicated DSIR repository initialized; RTK excluded. Experiments 001–006 cover synthetic rank, R_obs/R_model separation, identity quotient, DESI DR2 AP, relative expansion, and background equivalence.

## 2026-08-24 — G3B and real multi-channel response
Linear controls added. Incorrect per-model D(1)=1 power normalization was rejected. Corrected DESI DR1 ShapeFit erratum data were used for G6B after detecting the superseded Appendix-A growth values. Stable AP-growth covariance is classified as measurement identifiability, not physics. Conditional innovations show no significant aggregate residual; G7 remains open.

## 2026-08-24 — Experiment 011
Across 30 rank-3 synthetic cases with n_models=90/180/360 and strongly anisotropic/correlated feature transforms, covariance whitening recovered rank 3 in 30/30 and preserved the singular spectrum to 1.564e-15. Invalid unwhitened calibration produced ranks 20–35.

## 2026-08-24 — Experiment 012
Three independent response modes were represented by model-family counts 900/90/10. The catalog-multiplicity prior detected only 2 modes; an equal-family prior, with the exact same weights included in null calibration, recovered all 3. The third-to-first singular-value ratio rose from 0.259 to 0.853. DSIR therefore treats `R_model` as a prior-sensitivity profile `R_model(pi)`. Equal-family weighting is not assumed uniquely correct; stability across defensible priors/stratified bootstraps is the gate.

## 2026-08-24 — Recovery manual
Added `docs/RECOVERY_MANUAL.md` as the chat-independent restoration entry point. It records the DSIR architecture, formulas and derivations, response/rank methodology, failure modes, data provenance, solver pins, numbered experiments, exact next steps, and the hard boundary excluding RTK from DSIR development.

## 2026-08-24 — Experiment 013: interacting-vacuum source regression
Pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c` was audited at source level. The implementation convention is `Q/H = alpha*rho_m + beta*rho_v`, implying `d rho_m/d ln a = -(3+alpha)rho_m - beta rho_v` and `d rho_v/d ln a = alpha rho_m + beta rho_v`. The analytic source solution agrees with direct ODE integration to about `5.9e-12` normalized maximum error over the tested controls; the alpha=beta=0 limit returns `rho_m~a^-3` and constant vacuum at machine precision. Eigen-exponents match the interaction matrix to machine precision. This freezes the source convention but does not replace a full Boltzmann regression.

## 2026-08-24 — Experiment 014: GDM zero-limit source regression
Pinned `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829` was audited. For `w=cs2=cv2=0`, the background reduces to `rho_gdm~a^-3`; `Pi_nad=0`; the GDM continuity/Euler equations reduce to pressureless CDM when shear is zero; dynamic shear with `cv2=0` preserves zero shear; and leading adiabatic GDM IC match CDM. A crucial numerical caveat was found: when GDM is enabled the upstream code deliberately drops finite-start matter-radiation corrections of order `omega*tau` in several IC expressions and requires an early start (`start_small_k_at_tau_c_over_tau_h <= 1e-6`). Therefore the correct full-solver gate is convergence with earlier start, not bitwise equality at one finite start.

## 2026-08-24 — clean-room Boltzmann transition
Added `ci/compare_class_outputs.py` and `.github/workflows/gdm-zero-limit.yml`. The workflow clones the pinned upstream on a clean Ubuntu runner, builds it, runs matched CDM and zero-GDM calculations, compares matched numerical products, and uploads the complete regression artifact. The first run is intentionally calibration-only: no arbitrary physics tolerance is imposed before the actual clean-room numerical floor is measured. A later commit must freeze the tolerance from the observed convergence behavior.
