# Experiment 057A — C8 failure-mechanism audit

Date: 2026-08-26

## Purpose

Diagnose *why* the preregistered Exp056B/F29 endpoint-normalized half-transition law failed on C8 IDM-photon scattering, without modifying, rescuing, or reinterpreting the frozen Exp056B gate.

## Frozen inputs

Use the exact Exp056B C8 model grid, cosmology, redshifts and low-k nodes:

- `u_idm_g = {1.9784961959913951e-13, 2.7180740724473660e-13, 4.2866377403625277e-13, 7.7340788471244140e-13, 1.1546648138593298e-12}`;
- `z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`;
- `k={0.001,0.003,0.01,0.03,0.1} h/Mpc`;
- source scales `k_source={0.08484582985947185,0.07347864406347489,0.05999506164903260,0.04647197492427811,0.03927598733289058} h/Mpc`.

## Audit quantities

For each model and redshift, reconstruct `r_Delta=ln(P_model/P_ref)` on the frozen nodes and report:

1. endpoint contrast `D=r(k_max)-r(k_min)`;
2. endpoint-normalized profile `u=(r-r_min)/D` and whether it is monotone over the five nodes;
3. the already-frozen unique `u=0.5` crossing `k50` for traceability only;
4. adjacent-model cosine similarity of the full 35-component response vectors;
5. singular values of the five model response vectors after row-normalizing each model vector to unit L2 norm;
6. the fraction of variance captured by the leading singular mode;
7. sign reversals in adjacent-coupling finite differences at each `(z,k)` cell.

## Interpretation rule

This is a **diagnostic audit, not a discovery gate**. No alternative transition coordinate, threshold, normalization, redshift subset, k subset, coupling replacement, or fitted rescue law may be selected from these outputs and then counted as prospective evidence.

The scientific question is only whether Exp056B failed in an approximately one-dimensional response family or whether the C8 response changes shape/orientation materially across the frozen coupling sequence.

- If leading normalized-profile variance is near unity and adjacent cosines remain near 1, the failure is most naturally attributed to the endpoint-half-transition coordinate rather than a strongly multi-directional family.
- If substantial higher-mode variance and/or orientation changes appear, the failure indicates genuine response-shape evolution across C8 couplings.

Any future candidate law must be defined separately and preregistered before exposure to a new withheld family/mechanism.

Top-level gates remain `G7 OPEN`, `G8 OPEN`, `G9 OPEN` regardless of this audit.