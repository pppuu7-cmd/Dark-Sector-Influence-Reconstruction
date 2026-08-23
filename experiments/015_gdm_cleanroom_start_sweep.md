# Experiment 015 — GDM zero-limit clean-room finite-start sweep

**Date:** 2026-08-24  
**Upstream:** `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`  
**GitHub Actions run:** `32670664137`  
**Artifact:** `9501282931`, digest `sha256:5321f8aaf12cf2895979e194390f1784fc1a6e3cdb6ae42ec0fdbab1af901f65`

## Question

Experiment 014 established at source level that the zero-closure GDM equations reduce to CDM, while the GDM-enabled initial-condition branch omits some finite-start `O(omega*tau)` matter-radiation corrections. Does decreasing `start_small_k_at_tau_c_over_tau_h` monotonically improve the full Boltzmann agreement between ordinary CDM and zero-GDM?

## Test

Matched ordinary-CDM and zero-GDM runs were executed at

`start_small_k_at_tau_c_over_tau_h = {1e-6, 3e-7, 1e-7, 3e-8}`.

The background, matter power at `z=0,1`, unlensed/lensed CMB spectra, and lensing channels were compared. `P(k)` was evaluated with explicit lower-k cuts so ultra-large-scale numerical behavior could not dominate a single global metric.

## Result

The hypothesis of monotonic improvement with smaller start parameter is **rejected**.

At `1e-6`, representative discrepancies are:

- `max |P_GDM/P_CDM-1|` for `k>=1e-3 h/Mpc`: `3.01e-3` at z=0, `2.95e-3` at z=1;
- for `k>=1e-2 h/Mpc`: about `2.41e-3`;
- for `k>=0.1 h/Mpc`: about `2.86e-4`;
- unlensed TT max-absolute-over-peak metric: `1.73e-3`;
- lensing-potential `phiphi`: `4.82e-4`;
- E-phi cross-channel: `6.63e-3`.

The background itself is essentially the same: `H` is identical to numerical precision and the mapped growth-D background output differs at only about `1.67e-7` in the peak-relative metric.

Decreasing the start parameter below `1e-6` **worsens** the perturbation/spectrum agreement. For example, the z=0 `P(k)` discrepancy above `0.1 h/Mpc` grows from `2.86e-4` at `1e-6` to `2.12e-3`, `1.12e-2`, and `2.33e-2` at `3e-7`, `1e-7`, and `3e-8`, respectively. TT likewise worsens from `1.73e-3` to `8.91e-3`, `2.34e-2`, and `9.36e-2`.

## Interpretation

`start_small_k_at_tau_c_over_tau_h` participates in CLASS's coupled choice of initial integration time/tight-coupling regime. Although decreasing it is associated with an earlier-start condition, pushing it much lower does not constitute an isolated asymptotic convergence operation for this old GDM_CLASS branch. Other numerical timescales/integration tolerances become relevant and the calculation becomes less stable.

Therefore the source-level finite-start identity

`Delta delta_gamma / delta_gamma,leading ~ omega*tau/5`

must **not** be promoted into a prediction that all full-solver discrepancies decrease monotonically with this one precision parameter.

## Gate decision

- GDM-S0 (source zero-closure): remains **PASS**.
- GDM-S1 (full Boltzmann zero-limit): remains **OPEN**.
- `1e-6` is the best of the tested start values and becomes the current working start for the next calibration.
- No tolerance is frozen from Experiment 015.
- Next: keep start=`1e-6` and vary independent CLASS precision controls (`tol_perturb_integration`, perturbation sampling, hierarchy/spectral sampling) to determine the numerical floor.

This is a methodological/negative result, not a dark-sector physical effect.
