# Experiment 056A — C8 IDM–photon source-only selector v0.1

Date: 2026-08-26
Status: **SOURCE-ONLY / NO C8 RESPONSE ALLOWED**

## Purpose

Select a genuinely fresh C8 scale-transition mechanism and its coupling grid **without generating or inspecting any C8 matter-power response**. The resulting C8 points may later be used in a separately preregistered prospective test of the F28 endpoint-normalized half-transition candidate.

C8 is interacting dark matter–photon scattering (`idm_g`) in pinned official CLASS. It is distinct from C7 IDM–dark-radiation: in the perturbation equations it contributes to the visible photon opacity/shear and to the IDM Euler equation.

Pinned solver:

`lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`

## Frozen background and microphysics

- `h = 0.67`;
- `T_cmb = 2.7255 K`;
- `omega_b = 0.0224`;
- `omega_idm = 0.1200`, `omega_cdm = 0`;
- `m_idm = 1e9 eV`;
- `Omega_k = 0`;
- `N_ur = 3.046`;
- no `idr` component;
- Lambda inferred by CLASS;
- IDM–photon temperature index `n_index_idm_g = 0`.

The source-selection stage may write CLASS background and thermodynamics tables only. It must not request `mPk`, transfer functions, CMB spectra, source functions, or any perturbation response product.

## Source-native interaction rate

Pinned CLASS computes

\[
\dot\mu_{idm\gamma}(z)
= \frac{3}{8\pi G}(1+z)^{2+n_\gamma}\,\Omega_{idm}H_0^2\,u_{idm\gamma}\,\mathcal K,
\]

where `n_gamma = n_index_idm_g` and `K` is the fixed CLASS unit-conversion factor appearing in `source/thermodynamics.c`.

Pinned `source/perturbations.c` defines

\[
S_{idm\gamma}(z)=\frac43\frac{\rho_\gamma(z)}{\rho_{idm}(z)}
\]

and the IDM Euler drag is

\[
\boxed{\Gamma_{idm\leftarrow\gamma}(z)=S_{idm\gamma}(z)\,\dot\mu_{idm\gamma}(z)}.
\]

For `n_index_idm_g=0`, this rate is linear in `u_idm_g` and scales approximately as `(1+z)^3` before late-time corrections to the background become relevant.

## Frozen source epoch and scale

Define the mechanism-native transition epoch by

\[
\boxed{\Gamma_{idm\leftarrow\gamma}(z_*)=\mathcal H(z_*)},
\qquad
\mathcal H(z)=aH(z)=\frac{H(z)}{1+z},
\]

and the source scale

\[
\boxed{k_*=\mathcal H(z_*)/h}.
\]

To compare against the already established C3/C5/C7 source-scale range without looking at C8 responses, freeze the five target source scales to

\[
k_*^{target}=[
0.08484582985947185,
0.07347864406347489,
0.05999506164903260,
0.04647197492427811,
0.03927598733289058
]\;h/{\rm Mpc}.
\]

These are source targets only; they do not encode any C8 response information.

## Source-only inversion algorithm

1. Run pinned CLASS once with a harmless non-zero trial `u_idm_g = 1e-8`, with background and thermodynamics outputs only.
2. From the CLASS background table, solve `H(z)/(1+z)/h = k_*^target` by interpolation in `ln(1+z)`.
3. At each resulting `z_*`, interpolate the trial thermodynamic `dmu_idm_g`, and background `rho_g`, `rho_idm`.
4. Form
   \[
   \Gamma_{trial}=\frac43\frac{\rho_g}{\rho_{idm}}d\mu_{trial}.
   \]
5. Since the pinned source equation is exactly linear in `u_idm_g`, set
   \[
   \boxed{u_i=u_{trial}\frac{\mathcal H(z_{*,i})}{\Gamma_{trial}(z_{*,i})}}.
   \]
6. Report reconstructed source-target residuals; do not optimize against any response observable.

## Hard contamination rule

Exp056A fails as a source-only selector if any `*pk.dat`, transfer, Cl, perturbation-source, or other C8 response product is produced. No C8 response may be used to reorder, prune, expand, or tune the coupling grid.

## Interpretation boundary

A successful Exp056A only establishes a response-blind C8 parameter grid and source-scale provenance. It does not test F28, does not close G7/G8, and does not imply detectability or a universal dark-sector law.
