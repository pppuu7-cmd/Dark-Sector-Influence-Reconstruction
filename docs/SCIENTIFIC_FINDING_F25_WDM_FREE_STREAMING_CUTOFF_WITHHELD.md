# F25 — thermal-WDM free-streaming cutoff scale passes withheld mass ordering

**Status: HARD ESTABLISHED for the frozen Exp050B interpolation test; broader scaling law SUPPORTED only.**

Experiment 050B was frozen before generating the intermediate-mass CLASS outputs. Because Exp050A/F24 found the C4 high-k response to be nearly time-separable, the test deliberately did not reuse the GDM/f(R) interaction centroid `k_I^geo`. Instead it defined a mechanism-native cutoff scale from the solver response

\[
r_{\rm WDM}(k,z)=\ln\frac{P_{\rm WDM}(k,z)}{P_{\rm CDM}(k,z)},
\qquad
r_{\rm WDM}(k_{0.1},z)=-0.1.
\]

The first downward crossing is interpolated in `ln k` between the native pinned-CLASS samples.

## Frozen before withheld outputs

New masses:

\[
m=\{2.5,3.5,4.0,4.5\}\ {\rm keV}.
\]

The scientific gate was frozen as

\[
\boxed{
 k_{0.1}(m_{i+1},z)-k_{0.1}(m_i,z)>10^{-4}\ h/{\rm Mpc}
}
\]

for every consecutive mass pair at **each of the seven standard DSIR redshifts**.

No exact crossing values, mass exponent, redshift drift, `chi_I`, or legacy-fit agreement were frozen.

## Hard result

The clean-current-main confirmation run passed:

- run `32911928403`;
- artifact `9586893981`;
- artifact SHA256 `7c01e71c4223115976dc6887a1bcac06cac99e7fc50d039fae47307dd105ff0e`;
- branch scientific head `38a80d71af47bbda08bc27ff6fd9368439f91a4d`;
- merged science PR #35, merge SHA `7630cf23554bdd9e0bc7c738bb3b0b33d1b67388`.

A first independent run `32911710049` also completed successfully under the same frozen contract.

At `z=0.295`,

| mass [keV] | `k_0.1 [h/Mpc]` |
|---:|---:|
| 2.5 | `8.3866564` |
| 3.5 | `12.1928293` |
| 4.0 | `14.2301306` |
| 4.5 | `16.4737430` |

The consecutive steps are

`3.80617`, `2.03730`, `2.24361 h/Mpc`.

Across all seven redshifts the smallest measured positive mass step is

\[
\boxed{2.03728277\ h/{\rm Mpc}},
\]

more than four orders of magnitude above the frozen `1e-4 h/Mpc` numerical-sign guard. Every mass step at every redshift is positive.

The scale is also nearly time-stationary over the frozen linear domain. From `z=0.295` to `z=2.33`, the total crossing drifts are only

- 2.5 keV: `1.5739e-4 h/Mpc`;
- 3.5 keV: `2.8284e-4 h/Mpc`;
- 4.0 keV: `2.6432e-4 h/Mpc`;
- 4.5 keV: `3.9676e-4 h/Mpc`.

These redshift-drift values are descriptive, not part of the preregistered gate.

## Descriptive mass scaling — not a hard law

Combining the already-known Exp050A masses `2,3,5 keV` with the withheld Exp050B masses at `z=0.295`, a simple post-result log-log fit gives approximately

\[
k_{0.1}\propto m^{1.1434},
\]

with maximum relative residual below about `0.8%` across the seven sampled masses.

This exponent was **not preregistered** and must not be called a hard universal free-streaming law. It is only a compact descriptive target for a future independent-mass or alternate-threshold test.

## Interpretation

F25 establishes that C4 has a stable, physically meaningful scale coordinate: increasing the thermal-relic mass moves the solver-defined suppression cutoff to higher wavenumber, exactly as expected from a shorter free-streaming length at fixed matched dark-matter density.

Together with F24, this implies a useful mechanism-specific contrast:

- WDM: large, nearly time-separable high-k suppression whose main finite-amplitude motion is a cutoff-scale displacement;
- GDM viscosity / designer f(R): material low-k scale-time interaction whose finite-window motion is captured by interaction localization.

This supports the broader DSIR idea that different microscopic mechanisms can be compared by **movement of characteristic response scales**, while the appropriate observable coordinate need not be the same in every family.

## Boundary

- This is a withheld **interpolation within C4**, not a withheld-family G8 test.
- It is not a Ly-alpha likelihood or nonlinear-WDM statement.
- It does not prove the post-result `m^1.1434` fit.
- It does not prove that the GDM/f(R) `k_I` window-crossing relation is universal.
- It does not close G7 or G8 and does not establish an intrinsic parameter count.
