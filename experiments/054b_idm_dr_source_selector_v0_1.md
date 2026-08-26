# Experiment 054B — C7 IDM–DR source-only selector v0.1

Date: 2026-08-26
Status: SOURCE-ONLY PARAMETER SELECTION; NO C7 RESPONSE OUTPUTS
Gate relevance: preparation for prospective Exp054C only

## Purpose

Select a C7 interacting-DM / dark-radiation (ETHOS) coupling grid from the pinned CLASS source equations **without generating any C7 matter-power spectrum**.

The future Exp054C response gate is already inherited from Exp054A:

\[
0.0022992620786061375 \le
\mathcal C_{C7} \le
0.09951219222831723,
\qquad
\mathcal C=\frac{\Delta\ln k_R^{geo}}{\Delta\ln k_*}.
\]

This band cannot be changed after source selection.

## Pinned mechanism

Upstream:

`lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`

Use ETHOS IDM–DR with

- `omega_idm = 0.1200`, `omega_cdm = 0`;
- `omega_b = 0.0224`, `h = 0.67`, `T_cmb = 2.7255 K`;
- `N_ur = 3.046`;
- `N_idr = 0.2`;
- `nindex_idm_dr = 4`;
- default fermionic `stat_f_idr=7/8` convention;
- future matched reference will have identical IDM+IDR background but `a_idm_dr=0`.

Pinned CLASS defines

\[
\dot\mu_{idm-dr}
=a_{idm-dr}\,\omega_{idm}
\left(\frac{1+z}{10^7}\right)^n,
\]

and the IDM drag rate carries

\[
S^{-1}=\frac{4}{3}\frac{\rho_{idr}}{\rho_{idm}}
=\frac{4}{3}\frac{\omega_{idr}}{\omega_{idm}}(1+z).
\]

Therefore

\[
\Gamma_{idm\leftarrow idr}(z)
=\frac43\,\omega_{idr}\,a_{idm-dr}(1+z)
\left(\frac{1+z}{10^7}\right)^n.
\]

The mechanism-native decoupling epoch is frozen by

\[
\Gamma_{idm\leftarrow idr}(z_*)=\mathcal H(z_*),
\]

and

\[
\boxed{k_*=\mathcal H(z_*)/h}.
\]

No response observable enters this definition.

## Source targets

To avoid choosing a favorable source window after seeing C7 response, use the already calibrated C3 source-scale nodes verbatim:

\[
k_*^{target}=\{
0.08484582985947185,
0.07347864406347489,
0.05999506164903260,
0.04647197492427811,
0.03927598733289058
\}\ h/{\rm Mpc}.
\]

Exp054B deterministically inverts the source equations to obtain the five `a_idm_dr` values. Those values, in the returned order, become the frozen prospective Exp054C coupling grid.

## Background used by the source selector

For this source-only inversion use the same flat radiation+matter+Lambda background implied by the frozen parameters. `N_idr` is converted exactly according to the pinned CLASS input convention,

\[
\omega_{idr}=N_{idr}\frac78\left(\frac4{11}\right)^{4/3}\omega_\gamma.
\]

The photon density is frozen as `omega_gamma=2.4728e-5` at `T_cmb=2.7255 K`, consistent with the standard CLASS blackbody normalization at the precision needed here.

## Frozen controls

- recovered source target relative error `<=1e-10` for every node;
- all selected `a_idm_dr` finite, positive and strictly increasing as `k_*` decreases;
- all decoupling redshifts positive;
- no C7 `mPk`, transfer or perturbation output is allowed in this workflow.

## Boundary

Exp054B is parameter selection, not scientific validation. It cannot close G7/G8 and cannot be counted as a C7 PASS. The first C7 response may only be generated after this selected grid and the inherited Exp054A band are committed to a separate prospective experiment.
