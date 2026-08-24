# DSIR research gates

| Gate | Requirement | Status |
|---|---|---|
| G0 | LambdaCDM embedding reproduces reference observables | PARTIAL — background/growth controls pass; clean-room Boltzmann references now exist inside GDM/IDE calibration work, but a solver-independent reference gate is not yet frozen |
| G1 | Bianchi/conservation and gauge-invariant bookkeeping verified | OPEN |
| G2 | Response basis and conventions frozen for v0.1 | PASS — `config/response_basis_v0_1.json`, `docs/RESPONSE_BASIS_V0_1.md`, `src/dsir/response_basis.py`; Experiment 017 verifies calibration invariance, AP identity and covariance-metric amplitude quotient |
| G3A | Six control classes embedded at background/AP level | PASS/PARTIAL — representatives and exact intersections documented |
| G3B | Control classes embedded beyond background | PARTIAL — LambdaCDM, smooth wCDM, thermal WDM, designer-f(R) linear controls; IDE and GDM source-level zero limits pass; full-solver GDM precision convergence and IDE calibration remain open |
| G4 | Synthetic low-rank recovery test passes | PASS — corrected global noise-edge criterion recovers injected rank 3 |
| G5 | Rank robust to noise null, feature scaling, covariance coordinates, and model sampling | PARTIAL — Exp. 011: rank 3 in 30/30 after covariance whitening; Exp. 012: theory-catalog multiplicity prior can hide a real mode, so R_model must be reported as R_model(pi); broader non-Gaussian/family stress tests remain |
| G6A | First real-data response reconstruction | PASS — DESI DR2 AP calibration quotient and relative expansion reconstruction |
| G6B | First real multi-channel response reconstruction | PASS — corrected DESI DR1 ShapeFit vectors jointly provide geometry, growth, and shape with covariance; Experiment 009 |
| G7 | First nontrivial residual cross-channel relation found after quotienting known identities and observational degeneracy directions | OPEN — conditional innovation aggregate remains statistically consistent with null |
| G8 | Relation survives at least H2 withheld prediction; strong claim targets H3/H4 | OPEN |
| G9 | Candidate underlying dynamics/action reconstructed or ruled out | OPEN |

## G2 frozen basis v0.1

Core common coordinates are dimensionless log responses. The first six-family matrix uses anchored relative expansion

`r_E(z;z*) = ln[(H(z)/H(z*))/(H_ref(z)/H_ref(z*))]`, with `z*=0.51`,

and fixed-primordial matter-power response

`r_P(k,z) = ln[P_m(k,z)/P_m_ref(k,z)]`.

The linear core is `k/(h Mpc^-1)={0.001,0.003,0.01,0.03,0.1}`. Exact/derived coordinates (for example `r_FAP=r_DM+r_H`) are never counted simultaneously with their parents. Covariance whitening and matched component definitions remain mandatory.

## Current G3B numerical sub-gates

- **IDE-S0 PASS (source level):** pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c` convention frozen as `Q/H = alpha rho_m + beta rho_v`; analytic background agrees with direct ODE integration and `alpha=beta=0` gives CDM + constant vacuum (Exp. 013). In synchronous gauge the explicit IDM_IV density equation also reduces exactly to CDM at zero coupling (Exp. 016).
- **GDM-S0 PASS (source level):** pinned `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829` gives `rho_gdm~a^-3` and CDM continuity/Euler/leading adiabatic IC for the zero closure (Exp. 014).
- **GDM-S1 OPEN (full solver, converging):** high-precision clean-room calibration at fixed start `1e-6` reduces the zero-GDM/CDM matter-power mismatch to about `8.28e-4` maximum for `k>=1e-3 h/Mpc` and `2.82e-5` for `k>=0.1 h/Mpc` at the tested z output. Ultra-large `k<1e-3` remains a separately tracked finite-start/IC-sensitive diagnostic sector. A multi-level precision plateau is required before freezing tolerance. Earlier-start-only sweep is not monotone and is not used to tune a tolerance.
- **IDE-S1 OPEN (full solver):** the pinned upstream `class_iv` commit does not compile unmodified because `background_w_fld()` contains a premature closing brace before `case IDM_IV`. A provenance-tracked assertion-checked compile-only repair is being calibrated on PR #2; no physics equations are changed. Full matched spectra/background comparison is required after build succeeds.

No discovery claim is permitted before G8.
