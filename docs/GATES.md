# DSIR research gates

| Gate | Requirement | Status |
|---|---|---|
| G0 | LambdaCDM embedding reproduces reference observables | PARTIAL — background/growth controls pass; clean-room Boltzmann references exist inside GDM/IDE work, but a solver-independent reference gate is not yet frozen |
| G1 | Bianchi/conservation and gauge-invariant bookkeeping verified | PARTIAL — conservation/gauge contract frozen in `docs/CONSERVATION_GAUGE_V0_1.md`; internal IDE transfer cancellation passes; raw cross-gauge `mPk` audit FAILS the required safety condition (`~9.84e-5` gauge shift in linear core), so a common gauge-invariant perturbation extractor is now mandatory |
| G2 | Response basis and conventions frozen for v0.1 | REOPENED — background/identity conventions from Experiment 017 remain valid, but raw solver `r_P=ln(P_m/P_ref)` is not a safe cross-family coordinate when families require different gauges; v0.1.1 must replace/qualify the perturbation block |
| G3A | Six control classes embedded at background/AP level | PASS/PARTIAL — representatives and exact intersections documented |
| G3B | Control classes embedded beyond background | PARTIAL — LambdaCDM, smooth wCDM, thermal WDM, designer-f(R) linear controls; **GDM-S1 PASS** and **IDE-S1 PASS** as solver-specific zero-limit embeddings; common six-family perturbation matrix remains blocked by G1/G2 gauge-safe coordinate construction |
| G4 | Synthetic low-rank recovery test passes | PASS — corrected global noise-edge criterion recovers injected rank 3 |
| G5 | Rank robust to noise null, feature scaling, covariance coordinates, and model sampling | PARTIAL — Exp. 011: rank 3 in 30/30 after covariance whitening; Exp. 012: theory-catalog multiplicity prior can hide a real mode, so R_model must be reported as R_model(pi); broader non-Gaussian/family stress tests remain |
| G6A | First real-data response reconstruction | PASS — DESI DR2 AP calibration quotient and relative expansion reconstruction |
| G6B | First real multi-channel response reconstruction | PASS — corrected DESI DR1 ShapeFit vectors jointly provide geometry, growth, and shape with covariance; Experiment 009 |
| G7 | First nontrivial residual cross-channel relation found after quotienting known identities and observational degeneracy directions | OPEN — conditional innovation aggregate remains statistically consistent with null; law search is blocked until G1/G2 perturbation coordinate is repaired |
| G8 | Relation survives at least H2 withheld prediction; strong claim targets H3/H4 | OPEN |
| G9 | Candidate underlying dynamics/action reconstructed or ruled out | OPEN |

## G1 bookkeeping contract

The hard covariant identities are

`nabla_mu T_i^{mu nu}=Q_i^nu`, `sum_i Q_i^nu=0`, hence `nabla_mu T_tot^{mu nu}=0`.

Exact Bianchi/conservation-derived relations are projected before rank estimation, not rediscovered. First-order solver perturbations transform at tensor level as `delta T -> delta T - L_xi Tbar`; raw gauge-specific density, velocity and metric variables are not common response coordinates without an explicit invariant mapping.

The first direct gauge audit uses identical LambdaCDM cosmology in the same pinned GDM_CLASS code, changing only `gauge=newtonian` versus `gauge=synchronous`. Raw `mPk` differs by up to `9.8434e-5` on `1e-3 <= k <= 1e-1 h/Mpc`. This is about twenty times larger than the frozen GDM zero-limit solver tolerance (`5e-6`), so raw cross-gauge `mPk` is rejected for the common matrix.

## G2 basis status after gauge audit

Experiment 017 still validates:

- anchored relative expansion `r_E(z;z*) = ln[(H(z)/H(z*))/(H_ref(z)/H_ref(z*))]`, `z*=0.51`;
- AP log identity and non-double-counting of derived coordinates;
- covariance-metric amplitude quotient;
- fixed-primordial normalization rule.

However, the original perturbation coordinate

`r_P(k,z)=ln[P_m(k,z)/P_m_ref(k,z)]`

must not be populated from raw solver `mPk` across families using different gauges. A transfer-level audit is now testing a common comoving/gauge-invariant matter-density construction for v0.1.1.

## Current G3B numerical sub-gates

- **IDE-S0 PASS (source level):** pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c` convention frozen as `Q/H = alpha rho_m + beta rho_v`; analytic background agrees with direct ODE integration and `alpha=beta=0` gives CDM + constant vacuum (Exp. 013). In synchronous gauge the explicit IDM_IV density equation also reduces exactly to CDM at zero coupling (Exp. 016).
- **GDM-S0 PASS (source level):** pinned `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829` gives `rho_gdm~a^-3` and CDM continuity/Euler/leading adiabatic IC for the zero closure (Exp. 014).
- **GDM-S1 PASS (full solver):** fixed start `1e-6`; precision tail p1->p8 was calibrated without tuning the start parameter. High-precision core maxima p6/p7/p8 are approximately `4.70e-6`, `2.96e-6`, `1.47e-6`. A hard tolerance `max |Delta P/P| <= 5e-6` on `1e-3 <= k <= 1e-1 h/Mpc` was frozen *before* the final p8 regression; the hard run passed with actual global core maximum `1.471014806e-6`. Ultra-large `k<1e-3` remains a separate IC-sensitive diagnostic sector.
- **IDE-S1 PASS (full solver):** pinned `class_iv` requires a provenance-tracked compile-only repair for one premature brace plus legacy compiler/linker semantics; no cosmological equation is changed. Two calibration runs gave core residuals of order `1e-8` or below. Hard tolerances were frozen before the final run: `max |Delta P/P| <= 2e-8` on `1e-3 <= k <= 1e-1 h/Mpc` and semantic-background peak-normalized mismatch `<=2e-12`. Both hard gates passed on the frozen redshift grid `{0,0.295,0.51,0.706,0.934,1,1.317,1.491,2.33}`.

Solver-specific zero-limit PASS does **not** authorize mixing their raw perturbation outputs across gauges. G1/G2 must be repaired first.

No discovery claim is permitted before G8.
