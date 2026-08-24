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
Pinned `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829` was audited. For `w=cs2=cv2=0`, the background reduces to `rho_gdm~a^-3`; `Pi_nad=0`; the GDM continuity/Euler equations reduce to pressureless CDM when shear is zero; dynamic shear with `cv2=0` preserves zero shear; and leading adiabatic GDM IC match CDM. A crucial numerical caveat was found: when GDM is enabled the upstream code deliberately drops finite-start matter-radiation corrections of order `omega*tau` in several IC expressions and requires an early start (`start_small_k_at_tau_c_over_tau_h <= 1e-6`).

## 2026-08-24 — GDM start sweep: negative result
A clean-room sweep of `start_small_k_at_tau_c_over_tau_h={1e-6,3e-7,1e-7,3e-8}` falsified the simple hypothesis that pushing this single parameter earlier monotonically improves the zero-GDM/CDM match. Values below `1e-6` worsened the full solver. The parameter participates in the coupled perturbation/tight-coupling start logic and is not an independent accuracy knob. `1e-6` is retained as the working start; this negative result prevents tolerance tuning by start-time manipulation.

## 2026-08-24 — GDM high-precision clean-room calibration
At fixed start `1e-6`, a high-precision calculation using the pinned solver's precision conventions substantially reduced the working-scale zero-limit residual. Scale-aware interpolation gives approximately `max |Delta P/P|=8.28e-4` for `k>=1e-3 h/Mpc`, `5.55e-4` for `k>=1e-2`, `1.44e-4` for `k>=0.03`, and `2.82e-5` for `k>=0.1` in the tested z output. Background quantities agree at numerical/interpolation level. The very large fractional residual at `k~1e-5` is retained as a separate ultra-large-scale IC-sensitive diagnostic and is not used to inflate or hide the linear-core metric. A multi-level precision sweep was launched to establish a plateau before any tolerance is frozen. Initial p2/p3/p4 jobs received GitHub runner shutdown signals (`exit 143`); this is classified as infrastructure failure, not scientific failure, and jobs are being rerun unchanged.

## 2026-08-24 — Experiment 016 / interacting-vacuum perturbation audit
The pinned `class_iv` explicit IDM_IV implementation supports the relevant perturbation path only in synchronous gauge. There, at `alpha=beta=0`, the interacting pressureless density equation reduces to the CDM equation and the upstream adiabatic IC use the same `delta=3/4 delta_gamma`. Upstream's own `test_idm_iv_lcdm.ini` confirms the intended separate-component zero-coupling configuration (`alpha=beta=0`, `f_idm_iv=f_iv=1`) with `fluid_equation_of_state=IDM_IV` commented out.

## 2026-08-24 — class_iv pinned-source build caveat
The exact pinned `class_iv@ac627d54...` source does not compile unmodified on the clean runner: in `background_w_fld()` a premature closing brace after `case EDE` leaves the following `case IDM_IV` outside the switch. This is a source syntax defect, not a cosmological result. PR #2 applies an assertion-checked compile-only repair that removes exactly that one brace, records the resulting `git diff` and repair-script SHA256, and changes no equation/coefficient. IDE-S1 remains OPEN until the repaired pinned source builds and the matched zero-coupling spectra/background comparison passes a justified numerical gate.

## 2026-08-24 — Experiment 017 / G2 response basis v0.1 frozen
Frozen `config/response_basis_v0_1.json`, `docs/RESPONSE_BASIS_V0_1.md`, and `src/dsir/response_basis.py`. The first six-family core uses anchored relative expansion `r_E=ln[(H/H*)/(H_ref/H_ref*)]` with `z*=0.51` and fixed-primordial matter-power `r_P=ln(P/P_ref)` on the linear k grid `{0.001,0.003,0.01,0.03,0.1} h/Mpc`. Derived identities are not double-counted; covariance whitening, component matching, and theory-prior propagation remain mandatory. Experiment 017 verifies common-H calibration cancellation, the AP log identity, preservation of fixed-As power amplitude, and covariance-metric orthogonality of the amplitude quotient. G2 is PASS.
