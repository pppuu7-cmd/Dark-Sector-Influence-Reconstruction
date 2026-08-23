# DSIR research gates

| Gate | Requirement | Status |
|---|---|---|
| G0 | LambdaCDM embedding reproduces reference observables | PARTIAL — background/growth controls pass; full clean-room Boltzmann reference pending |
| G1 | Bianchi/conservation and gauge-invariant bookkeeping verified | OPEN |
| G2 | Response basis and conventions frozen for v0.1 | IN PROGRESS |
| G3A | Six control classes embedded at background/AP level | PASS/PARTIAL — representatives and exact intersections documented |
| G3B | Control classes embedded beyond background | PARTIAL — LambdaCDM, smooth wCDM, thermal WDM, designer-f(R) linear controls; interacting-vacuum source convention/background regression PASS (Exp. 013); GDM background/equation/leading-IC zero-limit regression PASS (Exp. 014); full Boltzmann spectra regressions remain required |
| G4 | Synthetic low-rank recovery test passes | PASS — corrected global noise-edge criterion recovers injected rank 3 |
| G5 | Rank robust to noise null, feature scaling, covariance coordinates, and model sampling | PARTIAL — Exp. 011: rank 3 in 30/30 after covariance whitening; Exp. 012: theory-catalog multiplicity prior can hide a real mode, so R_model must be reported as R_model(pi); broader non-Gaussian/family stress tests remain |
| G6A | First real-data response reconstruction | PASS — DESI DR2 AP calibration quotient and relative expansion reconstruction |
| G6B | First real multi-channel response reconstruction | PASS — corrected DESI DR1 ShapeFit vectors jointly provide geometry, growth, and shape with covariance; Experiment 009 |
| G7 | First nontrivial residual cross-channel relation found after quotienting known identities and observational degeneracy directions | OPEN — conditional innovation aggregate remains statistically consistent with null |
| G8 | Relation survives at least H2 withheld prediction; strong claim targets H3/H4 | OPEN |
| G9 | Candidate underlying dynamics/action reconstructed or ruled out | OPEN |

## Current G3B numerical sub-gates

- **IDE-S0 PASS (source level):** pinned `kaeonikc/class_iv@ac627d54...` convention frozen as `Q/H = alpha rho_m + beta rho_v`; analytic background agrees with direct ODE integration and alpha=beta=0 gives CDM + constant vacuum (Experiment 013).
- **GDM-S0 PASS (source level):** pinned `s-ilic/gdm_class_public@4c87916...` gives rho_gdm proportional to a^-3 and CDM continuity/Euler/leading adiabatic IC when `w=cs2=cv2=0` and shear is zero (Experiment 014).
- **GDM-S1 OPEN (full solver):** compare zero-GDM and CDM spectra on a clean runner while varying the integration start. The upstream GDM branch deliberately drops finite-start O(omega*tau) IC corrections, so convergence — not bitwise equality at one start — is the correct criterion.
- **IDE-S1 OPEN (full solver):** run matched alpha=beta=0 CLASS_IV versus LambdaCDM and establish numerical tolerance for background, P(k), growth and CMB/lensing responses.

No discovery claim is permitted before G8.
