# DSIR status snapshot — 2026-08-24

DSIR remains a reconstruction/meta-inference framework, not a fundamental theory.

| Item | Status | Evidence |
|---|---|---|
| Project separation from RTK | PASS | dedicated repository |
| Recovery/manual backup | PASS and live | `docs/RECOVERY_MANUAL.md` + `docs/RECOVERY_LATEST.md` contain formulas, derivations, gates, provenance, failure modes, and restart sequence |
| Conservation/gauge contract | PARTIAL G1 | `docs/CONSERVATION_GAUGE_V0_1.md`; total-transfer bookkeeping frozen; raw `mPk` gauge audit exposes a blocking artifact |
| Response basis v0.1 | REOPENED G2 | Experiment 017 background/identity rules remain valid, but perturbation block must be upgraded to v0.1.1 because cross-gauge raw `mPk` is unsafe |
| Synthetic latent-rank recovery | PASS | injected rank 3 recovered with corrected global noise edge |
| Rank coordinate/covariance robustness | PASS on tested suite; G5 PARTIAL | Experiment 011: 30/30 after whitening; naive raw ranks 20–35 |
| Theory-catalog prior sensitivity | FAILURE MODE IDENTIFIED + synthetic control PASS | Experiment 012: multiplicity prior hides rare third mode (rank 2); equal-family prior with matched null recovers rank 3 |
| DESI DR2 BAO/AP response | PASS G6A | calibration-free AP and relative expansion |
| DESI DR1 corrected ShapeFit response | PASS G6B | geometry-growth-shape covariance from 2026 erratum |
| Conditional innovation quotient | PASS as G7 preparation | no significant aggregate innovation (`chi2~5.53/5`, `p~0.355`) |
| Interacting-vacuum source regression | PASS S0 | Exp. 013/016: source convention, zero-coupling background and synchronous perturbation limit |
| Interacting-vacuum full-solver zero limit | PASS IDE-S1 | hard linear-core tolerance `2e-8` and semantic-background tolerance `2e-12` both pass on frozen z grid; pinned source repair/toolchain caveats fully recorded |
| GDM zero-limit source regression | PASS S0 | Exp. 014: `rho~a^-3`, CDM perturbation RHS and leading IC recovered for zero closure |
| GDM full-solver zero limit | PASS GDM-S1 | p6/p7/p8 core maxima `~4.70e-6, 2.96e-6, 1.47e-6`; hard pre-frozen tolerance `5e-6` passes with actual max `1.471e-6` |
| GDM ultra-large-scale sector | SEPARATE DIAGNOSTIC | `k<1e-3 h/Mpc` remains strongly finite-start/IC sensitive and is not mixed into the first common rank block |
| Raw matter-power gauge audit | FAIL as common coordinate | identical cosmology in Newtonian vs synchronous gauge differs by up to `9.843e-5` inside `1e-3<=k<=1e-1`, much larger than solver zero-limit floors |
| Common six-family perturbation matrix | BLOCKED by G1/G2 | solver embeddings are ready; common perturbation coordinate is not yet gauge safe |
| Transfer-level invariant audit | IN PROGRESS | testing whether a comoving/gauge-invariant matter-density response can replace raw `mPk` in v0.1.1 |
| New residual law | OPEN G7 | none claimed; search remains blocked until G1/G2 repair |
| Withheld prediction | OPEN G8 | required before discovery |
