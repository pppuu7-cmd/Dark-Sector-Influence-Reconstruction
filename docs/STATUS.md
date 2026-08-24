# DSIR status snapshot — 2026-08-24

DSIR remains a reconstruction/meta-inference framework, not a fundamental theory.

| Item | Status | Evidence |
|---|---|---|
| Project separation from RTK | PASS | dedicated repository |
| Recovery/manual backup | PASS and live | `docs/RECOVERY_MANUAL.md` + `docs/RECOVERY_LATEST.md` contain formulas, derivations, gates, provenance, failure modes, and restart sequence |
| Response basis v0.1 | PASS G2 | frozen machine-readable schema + implementation + Experiment 017 |
| Synthetic latent-rank recovery | PASS | injected rank 3 recovered with corrected global noise edge |
| Rank coordinate/covariance robustness | PASS on tested suite; G5 PARTIAL | Experiment 011: 30/30 after whitening; naive raw ranks 20–35 |
| Theory-catalog prior sensitivity | FAILURE MODE IDENTIFIED + synthetic control PASS | Experiment 012: multiplicity prior hides rare third mode (rank 2); equal-family prior with matched null recovers rank 3 |
| DESI DR2 BAO/AP response | PASS G6A | calibration-free AP and relative expansion |
| DESI DR1 corrected ShapeFit response | PASS G6B | geometry-growth-shape covariance from 2026 erratum |
| Conditional innovation quotient | PASS as G7 preparation | no significant aggregate innovation (`chi2~5.53/5`, `p~0.355`) |
| Interacting-vacuum source regression | PASS source-level; full solver OPEN | Exp. 013/016: source convention, zero-coupling background and synchronous perturbation limit |
| GDM zero-limit source regression | PASS source-level | Exp. 014: `rho~a^-3`, CDM perturbation RHS and leading IC recovered for zero closure |
| GDM full-solver zero limit | OPEN but numerically converging | high precision gives max `|Delta P/P|~8.28e-4` for `k>=1e-3` and `~2.82e-5` for `k>=0.1`; precision plateau still required |
| GDM ultra-large-scale sector | SEPARATE DIAGNOSTIC | `k<1e-3 h/Mpc` remains strongly finite-start/IC sensitive and is not mixed into first common six-family rank block |
| class_iv upstream build | CAVEAT IDENTIFIED | pinned `ac627d54...` has one premature brace before `case IDM_IV`; PR #2 uses assertion-checked compile-only repair with diff/provenance |
| Linear perturbation controls | PARTIAL G3B | LambdaCDM, smooth wCDM, thermal WDM, designer-f(R), source-level IDE/GDM; full IDE/GDM numerical gates remain |
| New residual law | OPEN G7 | none claimed |
| Withheld prediction | OPEN G8 | required before discovery |
