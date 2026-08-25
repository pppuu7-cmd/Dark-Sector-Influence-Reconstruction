# F24 — thermal-WDM high-k response is strongly scale-dominated and nearly time-separable

**Status: HARD ESTABLISHED descriptive response geometry for the frozen C4 thermal-WDM atlas (Exp050A); broader mechanism interpretation SUPPORTED only.**

Experiment 050A removes the previous C4 time-domain gap by computing a solver-native high-k matter-power response atlas with pinned official CLASS rather than extending the legacy static Viel transfer fit to P(k,z).

Frozen grid:

- thermal WDM masses `m={2,3,5} keV`;
- `k={0.1,0.3,1,3,10,20} h/Mpc`;
- `z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`;
- matched CDM reference;
- one FD ncdm species with mass+density enforced and early-radiation bookkeeping matched through `N_ur`.

Hard provenance:

- workflow run `32908751625` — PASS;
- artifact `9585845292`;
- artifact SHA256 `5d02bdce07da95c2bb9eab01acb2641f110b6b16e4ecf29ac2e8b1619d053139`;
- branch head `fa5f2e57bff008e860b4ab1ecd30116714c3b7ce`;
- status `PASS_WDM_HIGHK_TIME_ATLAS_OPERATOR_CONTROLS_V0_1`.

The response is

\[
r_{\rm WDM}(k,z)=\ln\frac{P_{\rm WDM}(k,z)}{P_{\rm CDM}(k,z)}.
\]

At the lowest frozen redshift `z=0.295`, selected values are:

| mass | `r(10 h/Mpc)` | `r(20 h/Mpc)` |
|---:|---:|---:|
| 2 keV | -0.2722369 | -1.1934447 |
| 3 keV | -0.0946742 | -0.4451668 |
| 5 keV | -0.0244695 | -0.1191708 |

Thus the expected mass ordering is present descriptively: lighter thermal relics produce stronger high-k suppression.

The maximum absolute redshift drift across the seven frozen redshifts is small compared with the high-k response amplitude:

- 2 keV: `6.8304e-5`;
- 3 keV: `2.2572e-5`;
- 5 keV: `5.0650e-6`.

Applying the same orthogonal scale-time decomposition used in Exp045-048,

\[
R(z,k)=\mu+T(k)+\tau(z)+I(z,k),\qquad
\chi_I=\frac{\|I\|^2}{\|R\|^2},
\]

gives

- 2 keV: `chi_I = 2.58257e-10`;
- 3 keV: `chi_I = 2.20807e-10`;
- 5 keV: `chi_I = 2.29161e-10`.

**Hard descriptive conclusion:** over this frozen high-k/redshift domain, thermal-WDM suppression is extremely close to a scale-dominated, time-separable response. The response can be large while its irreducible `k x z` interaction fraction is tiny. This is qualitatively different from the current low-k C3 GDM and especially C5 designer-f(R) examples, where scale-time interaction is material.

The solver atlas also does not exactly equal the legacy static Viel fit. Relative to the matched-cosmology legacy log-transfer proxy at `z=0.295`, the solver response is less negative by:

- at `k=20 h/Mpc`: `0.08413`, `0.04245`, `0.02046` for 2, 3, 5 keV;
- at `k=10 h/Mpc`: `0.01388`, `0.01079`, `0.00527` respectively.

This is not a failure of either calculation: the old Viel expression remains a useful static fitting proxy, while Exp050A is the production solver-native `P(k,z)` response atlas for DSIR comparisons.

## Boundary

- No Ly-alpha likelihood, nonlinear correction or observational detectability claim is made.
- `chi_I~1e-10` is specific to this frozen high-k linear solver domain; it is not a theorem that WDM is universally time-separable.
- Do not zero-pad C4 onto the low-k C1/C2/C3/C5 matrix.
- No intrinsic-rank, field-count, no-hair, G7 law, G8 discovery or universal-model claim follows.
