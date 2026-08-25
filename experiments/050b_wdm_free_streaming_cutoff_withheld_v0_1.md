# Experiment 050B — withheld thermal-WDM free-streaming cutoff validation v0.1

## Purpose

Exp050A established a solver-native C4 high-k time atlas and found that the thermal-WDM response is strongly scale-dominated with extremely small irreducible scale-time interaction on the frozen linear domain. Therefore this withheld test does **not** reuse the GDM/f(R) interaction-localization coordinate `k_I^geo`.

Instead we test a mechanism-native scale directly in the WDM suppression curve.

## Frozen before withheld outputs

New thermal-relic masses:

\[
m=\{2.5,3.5,4.0,4.5\}\ {\rm keV}.
\]

Reference and thermal mapping match Exp050A:

- official CLASS pinned to `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`;
- `omega_b=0.0224`, total dark-matter density `omega=0.1200`, `h=0.67`;
- one FD ncdm species for WDM;
- mass+density enforced by CLASS;
- thermal temperature from the `94.1 eV` instantaneous-decoupling density relation;
- `N_ur` adjusted so total early effective radiation remains `N_eff=3.046`;
- upstream `pk_ref.pre` retained;
- seven standard DSIR redshifts;
- high-k solver coverage to `25 h/Mpc`.

Response:

\[
r_{\rm WDM}(k,z)=\ln\frac{P_{\rm WDM}(k,z)}{P_{\rm CDM}(k,z)}.
\]

Define the first downward cutoff crossing

\[
r_{\rm WDM}(k_{0.1},z)=-0.1.
\]

The crossing is recovered by interpolation in `ln k` between the native CLASS samples bracketing `-0.1`.

## Pre-frozen scientific prediction

At **each** frozen redshift,

\[
\boxed{k_{0.1}(m_{i+1},z)-k_{0.1}(m_i,z)>10^{-4}\ h/{\rm Mpc}}
\]

for consecutive masses in the frozen grid.

Physical rationale: at fixed matched dark-matter density, the heavier thermal relic has a smaller thermal velocity/free-streaming length, so the suppression cutoff should move to higher wavenumber.

The `1e-4 h/Mpc` minimum positive step is a numerical-sign guard, not a fit to any withheld output.

## Explicitly not frozen

No prediction or threshold is frozen for:

- exact `k_0.1` values;
- a power-law mass exponent;
- redshift drift of `k_0.1`;
- `chi_I` or interaction morphology;
- agreement with the legacy Viel transfer fit;
- Ly-alpha likelihood or nonlinear observables.

## Interpretation boundary

A PASS would be an independent interpolation validation of the C4 free-streaming scale ordering, not a withheld-family G8 test. It would not prove that the GDM/f(R) interaction-centroid window-crossing relation is universal; WDM is being tested in its own mechanism-native scale coordinate precisely because its high-k `I(k,z)` is nearly null in Exp050A.

A FAIL must be retained as a scientific/implementation limit and must not be repaired by changing the mass grid or target response after seeing the outputs.
