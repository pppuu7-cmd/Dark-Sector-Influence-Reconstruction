# Exp067C — CAMB native-grid coherence localization v0.1

Date: 2026-08-26
Status: PREREGISTERED BEFORE FIRST NATIVE-GRID DIAGNOSTIC

## Motivation

Exp067B is permanently recorded as `FAIL_CAMB_CLASS_PHYSICAL_POWER_CONVENTION_BRIDGE_V0_1`. Its three CAMB↔CLASS physical power comparisons passed the frozen 3% log bound, cross-spectrum signs matched, the CLASS internal Weyl construction passed to machine precision, and the missing-k^2 negative control passed strongly. The sole failing condition was the CAMB rank-one adiabatic coherence control

\[
\rho^2(k,z)=\frac{P_{Wm}(k,z)^2}{P_{WW}(k,z)P_{mm}(k,z)},
\qquad
\max|\rho^2-1|=9.253183930191256\times10^{-8}
\]

against the already frozen threshold `5e-8`.

Exp067C is a diagnosis only. It cannot rescue, replace, reinterpret as PASS, or retune Exp067B.

## Frozen solver and cosmology

Use the exact CAMB pin and LambdaCDM setup from Exp067B:

- CAMB `cmbant/CAMB@fa3f097343fbbe427cc04b4f5f0041c22c6ec764`;
- `H0=67`, `ombh2=0.0224`, `omch2=0.1200`, `omk=0`, `mnu=0`, `nnu=3.046`;
- `TCMB=2.7255`, `YHe=0.24`, `tau=0`;
- `As=2.10e-9`, `ns=0.965`, pivot `0.05 Mpc^-1`;
- linear power only;
- physical power units (`hubble_units=False`) and physical `k [Mpc^-1]` (`k_hunit=False`).

No CLASS calculation is required in Exp067C because the question is solely where the CAMB-side coherence defect appears.

## Frozen spectra

Use exactly the Exp067B CAMB variables:

- `P_mm = P(delta_nonu,delta_nonu)`;
- `P_Wm = P(Weyl,delta_nonu)`;
- `P_WW = P(Weyl,Weyl)`.

Operational CAMB `Weyl` remains the corrected power-spectrum convention `k^2(phi+psi)/2`.

## Frozen redshift and target support

Use the same requested redshifts and target points as Exp067B:

`z = [0.0, 0.5, 1.0, 2.0]`

`k_target = [0.005, 0.02, 0.05, 0.10, 0.20] Mpc^-1`.

For native-grid statistics retain every raw CAMB matter-power k node satisfying

\[
0.005\le k\le0.20\;{\rm Mpc}^{-1}.
\]

No native k node may be deleted after seeing its coherence residual.

## Three frozen representations

For each of the three spectra construct:

1. **raw native power arrays** from `get_linear_matter_power_spectrum`, with no k interpolation;
2. **PkInterpolator evaluated back on the same native k,z knots**;
3. **PkInterpolator evaluated on the original Exp067B target k,z cells**.

All three representations must use the same CAMB result object and the same variable pairs.

## Frozen diagnostics

For each representation compute

\[
E=\max |P_{Wm}^2/(P_{WW}P_{mm})-1|.
\]

Also record:

- native k count within the frozen support;
- the `(z,k)` location and signed residual at the maximum for each representation;
- maximum relative reconstruction difference between raw native spectra and PkInterpolator values evaluated at their native knots, separately for `mm`, `Wm`, `WW`;
- the exact target-cell coherence array used to reproduce Exp067B.

The only numerical boundary is inherited unchanged from Exp067B:

`COHERENCE_TOL = 5e-8`.

## Frozen classification

Let `E_native`, `E_knots`, and `E_target` denote the three maxima.

- `INTERIOR_INTERPOLATION_LOCALIZED_V0_1` iff `E_native <= 5e-8`, `E_knots <= 5e-8`, and `E_target > 5e-8`.
- `NATIVE_CAMB_COHERENCE_DEFECT_V0_1` iff `E_native > 5e-8`.
- `KNOT_RECONSTRUCTION_DEFECT_V0_1` iff `E_native <= 5e-8` but `E_knots > 5e-8`.
- `EXP067B_TARGET_FAIL_NOT_REPRODUCED_V0_1` iff `E_target <= 5e-8`.

If more than one condition could appear to apply, priority is: target-not-reproduced first, then native defect, then knot defect, then interior interpolation localization.

No classification is a PASS of Exp067B.

## Anti-retuning

After the first Exp067C output, do not change CAMB commit, cosmology, requested redshifts, target k values, native support interval, variable definitions, power units, k units, interpolation API, coherence definition, inherited `5e-8` threshold, or classification rules inside v0.1.

## Gate consequence

Exp067C is a convention/numerics localization experiment only. Regardless of classification: **G7 OPEN, G8 OPEN, G9 OPEN**. No fresh withheld family may be selected from this diagnostic alone.
