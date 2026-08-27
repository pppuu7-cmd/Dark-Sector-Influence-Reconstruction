# Exp073J — KiDS-BNT component support evaluator pre-output binding v0.1

**Date frozen:** 2026-08-27  
**Status:** BOUND BEFORE ANY KiDS-BNT SUPPORT FRACTION IS EVALUATED

## Purpose

This binding completes the numerical implementation choices required to evaluate the KiDS `Wm` and `WW` component of the already-preregistered Exp073J common-support audit. It does not change the inherited physical rectangle, the `5%` positive-invalid threshold, or the final minimum retained dimension `15`.

The BOSS finite-matrix component remains the immutable non-classifying parent component from run `33042052616`; this step evaluates only the still-missing KiDS-BNT component.

## Immutable sources and geometry

Use exactly:

- `KiDS-WL/Cat_to_Obs_K1000_P1@36676da44471979dacb779155d7e6e7212ae1f4f` and the source/lens `n(z)` plus `xi2bandpow.c` hashes already frozen in `exp073g_kids_boss_bnt_operator_binding_v0_1.json`;
- the already-validated DSIR continuous-bin BNT implementation in `src/dsir/bnt.py`, reproducing the pinned `pltaylor16/x-cut@fcab1439c896ff4bff0fa21300366eef8107578c` convention;
- `cmbant/CAMB@fa3f097343fbbe427cc04b4f5f0041c22c6ec764` with the frozen Exp068B R0 geometry: `H0=67`, `ombh2=0.0224`, `omch2=0.1200`, massless neutrinos, `nnu=3.046`, `TCMB=2.7255 K`, `YHe=0.24`, `w=-1`.

No covariance object is part of this binding.

## Exact bandpower response

Reproduce the released `xi2bandpow.c` production path, not an effective-ell or top-hat approximation.

For the 326 released logarithmic theta nodes and the exact cos^2 apodisation, construct the E-mode xi-to-bandpower matrix exactly from the pinned C formulas. Compose that matrix with the continuum Hankel relations to obtain a direct positive-support angular response to the underlying angular spectrum:

- GGL: `R_b(ell) = ell/(2*pi) * sum_theta T_ne[b,theta] J_2(ell theta)`;
- shear: `R_b(ell) = ell/(2*pi) * [sum_theta T_plus[b,theta] J_0(ell theta) + sum_theta T_minus[b,theta] J_4(ell theta)]`.

The support envelope is `abs(R_b)`. Taking this absolute value is only a domination operation for support accounting; the future physical `P_Wm` remains signed.

No `xi2bandpow_pmweights_*` file is present in the pinned release, so use the released default `pfrac=0.5` for shear E mode.

## Solver-neutral line-of-sight support

Let each normalized source distribution define

`g_i(z) = integral_z^infinity dz_s n_i(z_s) (chi_s-chi)/chi_s`.

Apply the already-frozen BNT matrix to obtain localized efficiencies `g_r(z)` for zero-based rows `[2,3,4]`.

For support geometry only, use the model-independent projection coefficients implied by the Weyl variable `W=k^2(Phi+Psi)/2`:

- signed-Weyl/matter GGL envelope coefficient: `B_Wm(z) = abs[n_lens(z) g_r(z) / chi(z)]`;
- Weyl/Weyl shear envelope coefficient: `B_WW(z) = abs[(c/H(z)) g_r(z) g_s(z)]`.

These are operator factors only; no GR Poisson closure, fiducial `P(k)`, nonlinear boost, or matter-to-Weyl conversion is used.

Use the full Limber mapping `k=(ell+0.5)/chi(z)` in physical `Mpc^-1`.

## Numerical integration and convergence controls

The scientific support boundary remains exactly

- `0.295 <= z <= 2.33`;
- `0.000704833374744468 <= k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05`.

Freeze the numerical evaluator before observing support output as follows.

### Angular integration

Construct two deterministic ell grids:

- coarse: logarithmic `0.01..20` segment with 256 nodes followed by linear spacing `Delta ell=2` through `30000`;
- fine: logarithmic `0.005..20` segment with 512 nodes followed by `Delta ell=1` through `30000`, then `Delta ell=2` through `60000`.

For every released band and both response types require:

1. positive angular normalization is finite and non-zero;
2. the coarse normalization and the fine normalization restricted to `ell<=30000` agree to relative tolerance `5e-3`;
3. the fine positive tail above `ell=30000` is below `2e-3` of the full fine normalization.

Failure of these numerical trust controls is a reproduction/numerical-completeness failure, not a scientific 5% support FAIL.

### Redshift integration

Evaluate line-of-sight support on deterministic refined grids with maximum spacing `0.005` (coarse) and `0.0025` (fine), covering the complete non-zero public source/lens distributions. Source `n(z)` uses the prospectively frozen lower-edge plus half-bin convention. Interpolation and tail moments are piecewise linear, consistent with trapezoidal normalization.

Require every fine support fraction to reproduce the corresponding coarse fraction to absolute tolerance `1e-3`. The retained/non-retained label at the frozen 5% threshold must be identical between coarse and fine evaluations; otherwise the component result is numerically unresolved and cannot be used for full Exp073J classification.

## Candidate inventory

Without inspecting support output, enumerate exactly:

- `24` signed-`Wm` coordinates = 3 localized BNT rows x 8 released bands;
- `48` `WW` coordinates = 6 unordered localized-row pairs x 8 released bands;
- `72` KiDS-BNT component coordinates total.

A coordinate is retained iff its fine positive-invalid fraction is `<=0.05` and its coarse/fine label agrees.

## Hard controls K1-K10

K1 exact KiDS source/operator hashes and CAMB pin reproduce.  
K2 BNT rows `[2,3,4]` satisfy both frozen nulling moments to `1e-10` and deterministic repeatability to `1e-12`.  
K3 released bandpower matrix semantics and default `pfrac=0.5` reproduce.  
K4 all positive angular and redshift envelope normalizations are finite and strictly positive.  
K5 full physical `k=(ell+0.5)/chi` mapping and inherited rectangle are used with no effective coordinate.  
K6 angular-grid normalization/tail controls pass.  
K7 coarse/fine redshift support fractions converge and classification labels agree.  
K8 signed `P_Wm` semantics are preserved; absolute values occur only in support domination weights.  
K9 no fiducial power, covariance, nuisance SVD/rank, relation/null output or G8 information is read.  
K10 all `72` per-coordinate invalid fractions and retained flags are written machine-readably.

This component result is deliberately non-classifying for Exp073J by itself. After K1-K10 pass, a separate exact parent-composition step may bind the immutable BOSS per-row artifact and apply the already-frozen Exp073J J1-J8 classification without changing any threshold.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
