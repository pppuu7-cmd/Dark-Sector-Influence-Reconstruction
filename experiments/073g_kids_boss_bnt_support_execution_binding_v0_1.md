# Exp073G — KiDS/BOSS/BNT support-envelope execution binding v0.1

**Date frozen:** 2026-08-27  
**Status:** BOUND BEFORE ANY Exp073G INVALID-SUPPORT FRACTION IS EVALUATED

## Purpose

This second pre-output binding resolves the harmonic-space KiDS filter and the
configuration-space BOSS Fourier--Bessel tail that were not fully specified by
the first Exp073G operator binding.  It does not compute an invalid-support
fraction, a retained mask, or a final Exp073G classification.

The machine-readable record is
`data/derived/g7/exp073g_kids_boss_bnt_support_execution_binding_v0_1.json`.

## Additional immutable likelihood sources

The KiDS harmonic bandpower implementation is bound to

- `KiDS-WL/kcap@sanchez2017@1a0fcfe1dea694a176c30ec019d6f0ca101e8ae8`;
- tree `35cc43a1b8f01502b626d9d4b2914c100c16e6f9`;
- `cosebis/BandPower_interface.cc` SHA256
  `42fd8788bec206af6c4f5e99798e0cc68a70c2fb31d3d65499b314d00c0f2e98`;
- `cosebis/modules/BandPower_W.cc` SHA256
  `b7e2c74c928507308e1436b4e7052a242213aa3ea7193ade663ff9c37e51a863`;
- `cosebis/modules/BandPower_g.cc` SHA256
  `1ad01fe613875c66a3ee7b901f81641066b836540a76632f15e9c4e643bd8b72`.

The public BOSS wedges theory module is bound to

- `KiDS-WL/kcap_boss_module@0e894a7e58b257f50f9348f35309b3171688f004`;
- tree `875f0ef7c8cabe50247b04302b91f5c433ccd141`;
- the five exact source-file hashes recorded in the machine-readable binding.

The scientific source files at this pin are unchanged from
`e9d0739811b5c317715b0b0da18c05f15ce7aaca` (2020-07-06); the two later commits
change only the README and add the license.  This connects the frozen code to
the module documented for the KiDS-1000 3x2pt analysis without silently
substituting a later modelling implementation.

The BOSS-only high-redshift distribution is additionally bound as
`data/boss/nofz/BOSS_n_of_z2_res_0.01.txt`, SHA256
`00237c6f5a8df94b7c8de6e1a94d2d6fdf1bf934687183f9dbafb529d8c99c9b`.
It has positive tabulated support only over `0.50<=z<=0.74`; therefore its
redshift support is wholly inside the already-frozen Exp073G rectangle.

## KiDS harmonic response

Use the public KCAP Fourier-space bandpower response rather than treating the
nominal bands as top hats.  The source fixes

- `LLOW=0.1`, `LHIGH=1e4`;
- a logarithmic internal response table with `NLBINS=1000`;
- top-hat target bands with the eight logarithmic edges already bound over
  `100<=ell<=1500`;
- `theta_min=0.5 arcmin`, `theta_max=300 arcmin`, `Delta_x=0.5`;
- Bessel order 2 for galaxy--galaxy lensing;
- the equal `0.5*(order-0 + order-4)` E-mode combination for cosmic shear.

For each target band and Bessel order, reconstruct the public continuous
response

`W_n(ell) = integral dtheta theta A(theta) J_n(ell theta) g_n(theta)`,

where `A` is the exact log-cosine-squared apodisation and `g_n` is the analytic
top-hat response in the pinned source.  The positive support operator uses
`abs(ell W_2/N)` for GGL and
`0.5*(abs(ell W_0/N)+abs(ell W_4/N))` for shear, with
`N=log(ell_high/ell_low)`.  Thus signed lobes cannot cancel between physical
input multipoles; the signed future `P_Wm` itself is not replaced by an
absolute power spectrum.

The evaluation grid is frozen to 4097 log-spaced multipoles over the exact
KCAP interval `[0.1,1e4]`.  Each response integral uses 4096-point
Gauss--Legendre quadrature in `log(theta)` over
`[0.5 exp(-0.25),300 exp(0.25)] arcmin`.  A 2048-point construction is computed
independently as a convergence control; the normalized L1 response difference
must be at most `2e-5` for every band/order.  The exact KCAP lower and upper
multipole limits are support boundaries, not silently zeroed numerical tails.

## Lensing geometry and BNT support kernels

Use the previously pinned CAMB R0 geometry and the exact source distributions
from the first binding.  The normalized source histograms are linearly
interpolated between the frozen half-bin integration coordinates and are zero
outside the tabulated coordinate interval.  This interpolation rule is fixed
before support output.

For original source bin `a`, define the geometry-only source kernel

`q_a(z) = -chi(z) integral_z^infinity dz_s n_a(z_s)
          [chi(z_s)-chi(z)]/chi(z_s)`.

Apply the already-frozen continuous-bin BNT matrix to `q_a`, retaining only
rows `[2,3,4]`.  On a midpoint redshift quadrature, the non-negative block
envelopes are

- GGL/Wm: `n_lens(z) * abs(q_A(z))/chi(z)^2`;
- shear/WW: `(dchi/dz) * abs(q_A(z) q_B(z))/chi(z)^2`.

The GGL lens distribution is the bound BOSS+2dFLenS bin 2.  The six unordered
localized shear pairs are `(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)`.
The Limber mapping is exactly `k=(ell+0.5)/chi` in physical `Mpc^-1`.

Use 12000 uniform midpoint redshift cells over `0<=z<=6`; recompute with 24000
cells.  Every coordinate fraction must agree between the two grids to absolute
`2e-5`.  The source tables are zero by their bound interpolation outside this
range, so no non-zero source tail is omitted.

## BOSS configuration-space support envelope

The public likelihood uses the same positive `32x180` radial window for each
of three wedges and slices zero-based rows `[4,32)` and columns `[20,160)`.
Retain those exact 84 coordinates.

The pinned source constructs multipoles `ell={0,2,4}` with

- transform lower limit `k_h=exp(-6.2) h/Mpc`;
- `cutoff_0=exp[-(k_h/0.7)^2]`;
- `cutoff_2=exp[-(k_h/0.58)^4]`;
- `cutoff_4=exp[-(k_h/0.6)^2]`.

The support envelope integrates the absolute contribution before summing over
radial bands, wedge angle, or multipole:

`E_i(k_h) = k_h^2 sum_r abs(window_ir)
             sum_L cutoff_L(k_h)
             <abs[L_L(mu_true) j_L(k_h s_true)]>_wedge`.

The AP map is evaluated at the released high-z effective redshift `z=0.61`
using R0 and the source fiducial `(Omega_m,h)=(0.31,0.7)`.  This effective
redshift enters only the released scale operator.  The separate positive BOSS
`n(z)` supplies the redshift support envelope.

Use 128 Gauss--Legendre nodes in each observed-mu wedge and 32769 log-spaced
`k_h` nodes over `[exp(-6.2),6] h/Mpc`.  Recompute with 64 mu nodes and 16385
`k_h` nodes; every coordinate fraction must agree to absolute `2e-5`.
For efficient exact AP angular averaging, tabulate the three wedge/multipole
absolute Bessel averages on 65537 uniformly spaced nodes in
`x=k_h*r` from zero through the largest transformed argument required by the
bound radial/k range, then linearly interpolate.  Repeat with 32769 x nodes;
the same coordinate-fraction tolerance applies.
At the upper limit the slowest exact cutoff is below `2e-32`, which is the
predeclared tail-closure control.  Convert only by `k_phys=h*k_h` and require
the roundtrip tolerance from Exp073G G7.

## Classification discipline

All 156 frozen candidate coordinates are evaluated.  A coordinate is retained
only when every required block has invalid positive weight at most `0.05`.
The final Exp073G classification and the 15-coordinate/channel-coverage gate
remain exactly as preregistered.

No covariance value, measured residual, nuisance rank/SVD, G7 relation, G8
response, or held-out output may be read.  Failure of a predeclared numerical
closure control is `FAIL_EXP073G_REPRODUCTION_OR_PROVENANCE`, not permission to
change a grid, cutoff, source selection, support rectangle, or threshold after
inspection.

G7 OPEN. G8 OPEN. G9 OPEN.
