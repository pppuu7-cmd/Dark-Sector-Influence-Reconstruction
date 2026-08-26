# Experiment 053A — withheld-family DCDM temporal localization v0.1

## Purpose

Test the current DSIR characteristic-scale/epoch hypothesis on a **new dark-sector mechanism that was not used to construct F21/F23/F25**: decaying cold dark matter (DCDM) into dark radiation, using the same pinned official CLASS lineage as C4.

Unlike GDM viscosity, designer-f(R), and WDM, DCDM has a natural **lifetime / epoch** control rather than a primary spatial cutoff. This makes it a deliberately difficult withheld-family test.

## Pinned source audit before solver outputs

Pinned solver:

`lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`.

The pinned CLASS input contract states that `Gamma_dcdm` is the DCDM decay constant in the same units as `H0` (`km/s/Mpc`) and permits an initial rescaled abundance through `omega_ini_dcdm`.

The pinned background source implements

\[
\frac{d\rho_{\rm dcdm}}{d\ln a}
=-3\rho_{\rm dcdm}-\frac{\Gamma_{\rm dcdm}}{H}\rho_{\rm dcdm},
\]

\[
\frac{d\rho_{\rm dr}}{d\ln a}
=-4\rho_{\rm dr}+\frac{\Gamma_{\rm dcdm}}{H}\rho_{\rm dcdm}.
\]

The perturbation module also contains explicit decay terms in DCDM density and sourced dark-radiation multipoles. Thus this is not a background-only proxy.

## Frozen cosmology and withheld family points

Reference:

- `h=0.67`;
- `omega_b=0.0224`;
- stable `omega_cdm=0.1200`;
- `N_ur=3.046`, `N_ncdm=0`;
- flat closure, with `Omega_Lambda` inferred by CLASS;
- no reionization;
- analytic primordial spectrum with `A_s=2.10e-9`, `n_s=0.965`;
- standard DSIR seven redshifts;
- production low-k comparison nodes `k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

Withheld C6 points use

- `omega_cdm=0`;
- `omega_ini_dcdm=0.1200`;
- dark radiation generated self-consistently by decay;
- dimensionless lifetime controls

\[
\gamma\equiv\Gamma_{\rm dcdm}/H_0=\{0.25,0.5,1,2\},
\]

corresponding at `H0=67 km/s/Mpc` to

`Gamma_dcdm={16.75,33.5,67,134} km/s/Mpc`.

This grid is frozen before the first C6 solver output is inspected.

## Observable response and preregistered coordinate

For each C6 point,

\[
r(k,z;\gamma)=\ln\frac{P_{\rm DCDM}(k,z;\gamma)}{P_{\rm CDM}(k,z)}.
\]

Define temporal response-power weights

\[
q_z(z;\gamma)=
\frac{\sum_k r^2(k,z;\gamma)}
{\sum_{z,k} r^2(k,z;\gamma)}
\]

and the geometric redshift centroid

\[
1+z_R(\gamma)
=\exp\left[\sum_z q_z(z;\gamma)\ln(1+z)\right].
\]

## Pre-frozen scientific prediction

Increasing the decay rate moves the observable response to earlier epochs. Therefore, before any C6 output,

\[
\boxed{
z_R(\gamma_{i+1})-z_R(\gamma_i)>10^{-3}
}
\]

is frozen for each consecutive pair in `gamma={0.25,0.5,1,2}`.

The `1e-3` value is a numerical/sign guard. The exact `z_R` values and step sizes are not predicted.

A minimum total response norm `||r||_2>1e-4` is also required so the normalized centroid cannot pass on numerical noise.

## Explicitly not preregistered

The following are descriptive only after the run:

- the irreducible scale-time fraction `chi_I`;
- any scale centroid `k_R`;
- exact background survival/decay fractions;
- an analytic mapping between `z_R` and `Gamma/H(z)`;
- the sign or value of any fitted exponent;
- observational detectability.

## Gate interpretation

This is a genuinely withheld **family/mechanism** relative to C1-C5 and to the construction of F21/F23/F25. A PASS would therefore be much stronger than another within-family interpolation test: it would show that a new mechanism with a temporal source scale exhibits the predicted motion of a response-localization coordinate.

However, top-level G8 must still remain open unless a sufficiently precise G7 relation has first been frozen. The present test is therefore a withheld-family validation of the **characteristic epoch/scale hypothesis**, not permission to retroactively declare a universal law.

A FAIL is scientifically meaningful and must be retained. The gamma grid, centroid definition, threshold, k-grid and z-grid must not be changed after seeing the outputs to rescue the hypothesis.
