# DSIR method v0.1 (working specification)

## Scientific objective
Reconstruct the minimum observable influence structure of the cosmic dark sector without fixing its ontology in advance. DM, DE, interactions, and modified gravity are theory-layer interpretations, not response-layer labels.

## Layers
1. **Data** — likelihood products, covariances, systematics and calibrations.
2. **Response** — expansion/AP, growth, lensing/Weyl, slip, GW propagation, couplings and nonlinear signatures.
3. **Theory** — model families and effective descriptions such as residual stress tensors, GDM, PPF/EFT, interacting sectors and microphysical actions.

## Two ranks
`R_obs` is the dimension the observational response operator can distinguish after covariance whitening. `R_model` is the dimension occupied by viable theory manifolds after projection into identifiable space. Low `R_obs` is data blindness; low `R_model` inside a larger identifiable space is the interesting unification case.

## Mandatory whitening and theory-prior sensitivity
Noise-edge rank claims are made only in covariance-whitened coordinates. Arbitrary units or correlated feature transformations must not change the result if their covariance is transformed consistently.

A finite theory catalog also defines an implicit prior through sample multiplicity. Therefore DSIR treats model rank as `R_model(pi)`, a sensitivity profile over defensible theory-family priors/stratifications, not as one catalog-frequency scalar. Any weighting is propagated into the null simulations used for rank calibration.

## Quotients before law discovery
Candidate relations are searched only after removing/conditioning on exact definitions, Bianchi/conservation identities, shared calibrations, gauge/frame artifacts, and measurement-induced covariance directions.
For a Gaussian residual r: `r_t_perp = r_t - C_tN C_NN^{-1} r_N`, with conditional variance `C_tt-C_tN C_NN^{-1} C_Nt`. This is statistical innovation, not automatically causal.

## Claim hierarchy
control identity -> observational identifiability pattern -> empirical residual relation -> predictive law candidate -> physical model candidate. No discovery claim before G8.
