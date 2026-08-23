# DSIR method v0.1 (working specification)

## Scientific objective
Reconstruct the minimum observable influence structure of the cosmic dark sector without fixing its ontology in advance. Dark matter, dark energy, interactions, and modified gravity are candidate interpretations at the theory layer, not labels imposed on the response layer.

## Layers
1. **Data** — likelihood products, compressed measurements, covariances, systematics and calibration variables.
2. **Response** — observable/gauge-robust expansion, AP geometry, growth, lensing/Weyl response, gravitational slip, GW propagation, coupling and nonlinear signatures.
3. **Theory** — model families and effective descriptions such as residual stress tensors, GDM, PPF/EFT, interacting sectors and microphysical actions.

## Two ranks
`R_obs` measures the dimension that the observational response operator can actually distinguish after covariance whitening. `R_model` measures the dimension occupied by viable theory manifolds after projection into the identifiable space. Low `R_obs` is a data degeneracy; low `R_model` inside a larger identifiable space is the interesting case for common-law discovery.

## Quotients before law discovery
Candidate relations are searched only after removing/conditioning on:
- exact definitions and algebraic identities;
- Bianchi/conservation relations already assumed by the framework;
- shared calibrations such as an overall ruler when a calibration-free quotient exists;
- gauge/frame artifacts;
- measurement-induced covariance directions.

For a Gaussian response residual `r` with covariance `C`, the conditional innovation of target channel `t` after conditioning on channels `N` is

`r_t_perp = r_t - C_tN C_NN^{-1} r_N`

with conditional variance

`V_t_perp = C_tt - C_tN C_NN^{-1} C_Nt`.

This is a statistical innovation, not automatically a causal residual.

## Claim hierarchy
- control identity: expected and already known;
- observational identifiability pattern: property of measurement/covariance geometry;
- empirical residual relation: survives identity/covariance quotient;
- predictive law candidate: survives independent/withheld data without refitting;
- physical model candidate: admits consistent dynamics/action and additional predictions.

No discovery claim is permitted before G8.
