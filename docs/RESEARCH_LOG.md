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
