# DSIR status snapshot — 2026-08-24

DSIR remains a reconstruction/meta-inference framework, not a fundamental theory.

| Item | Status | Evidence |
|---|---|---|
| Project separation from RTK | PASS | dedicated repository |
| Recovery/manual backup | PASS and live | `docs/RECOVERY_MANUAL.md` contains formulas, derivations, gates, provenance, failure modes, and restart sequence |
| Synthetic latent-rank recovery | PASS | injected rank 3 recovered with corrected global noise edge |
| Rank coordinate/covariance robustness | PASS on tested suite; G5 PARTIAL | Experiment 011: 30/30 after whitening; naive raw ranks 20–35 |
| Theory-catalog prior sensitivity | FAILURE MODE IDENTIFIED + synthetic control PASS | Experiment 012: multiplicity prior hides rare third mode (rank 2); equal-family prior with matched null recovers rank 3 |
| DESI DR2 BAO/AP response | PASS G6A | calibration-free AP and relative expansion |
| DESI DR1 corrected ShapeFit response | PASS G6B | geometry-growth-shape covariance from 2026 erratum |
| Conditional innovation quotient | PASS as G7 preparation | no significant aggregate innovation (`chi2~5.53/5`, `p~0.355`) |
| Interacting-vacuum source regression | PASS source-level; full solver OPEN | Experiment 013 freezes `Q/H=alpha rho_m+beta rho_v`, alpha=beta=0 limit, analytic-vs-ODE and eigenmode consistency |
| GDM zero-limit source regression | PASS source-level; full solver OPEN | Experiment 014: rho~a^-3, CDM perturbation RHS and leading IC recovered for zero closure; finite-start O(omega*tau) caveat identified |
| Clean-room GDM Boltzmann workflow | CALIBRATION RUN PREPARED | `.github/workflows/gdm-zero-limit.yml`; first run measures numerical floor before a tolerance is frozen |
| Linear perturbation controls | PARTIAL G3B | LambdaCDM, smooth wCDM, thermal WDM, designer-f(R), plus source-level IDE/GDM controls; full IDE/GDM spectra pending |
| New residual law | OPEN G7 | none claimed |
| Withheld prediction | OPEN G8 | required before discovery |
