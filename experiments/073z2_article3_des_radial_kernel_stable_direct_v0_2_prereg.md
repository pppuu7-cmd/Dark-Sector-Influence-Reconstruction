# Exp073Z2 — Article 3 DES radial-kernel stable-direct repair v0.2

**Frozen:** 2026-08-30, after Exp073Z v0.1 numerical failure and before any DES physical-k/support fraction is evaluated.

## Why a repair is required

Exp073Z v0.1 run `33277788565`, job `99167465260` stopped before producing any radial authority because the source-efficiency guard observed `min(g)=-1.4307726212042506e-10` while the v0.1 canonicalization guard allowed only `>=-1e-12`.

The failure occurred in the algebraically correct but numerically cancellation-prone representation

`g(z)=T0(z)-chi(z) T1(z)`

when each tail was formed as `total cumulative - prefix cumulative`. Near the high-z end both tail terms are tiny differences of nearly equal accumulated totals. No physical support fraction, retained coordinate, covariance, nuisance, relation/null statistic or G8 output was computed. This is therefore a numerical implementation failure, not a science FAIL.

Exp073Z2 is a prospective repair. It does **not** relax any physical or convergence threshold and does not inspect any Layer-A outcome.

## Immutable inheritance from Exp073Z v0.1

Keep exactly:

- DES source FITS SHA256 `b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b`, HDU 1, `BIN1..BIN4`;
- DES lens FITS SHA256 `114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca`, HDU 7, `BIN1..BIN5`;
- common `Z_MID` SHA256 `b93b65adb24b98fd76a41486a1352978459af2836f533d0adadd0ca390dca89b`;
- all Exp073Y per-BIN logical-array hashes;
- released-node trapezoidal normalization before interpolation;
- zero direct `n(z)` interpolation outside the released midpoint domain;
- CAMB `fa3f097343fbbe427cc04b4f5f0041c22c6ec764` with `H0=67`, `ombh2=0.0224`, `omch2=0.1200`, `mnu=0`, `nnu=3.046`, `TCMB=2.7255`, `YHe=0.24`, `tau=0`, `w=-1`, `wa=0`;
- coarse grid maximum spacing `0.005`, fine grid maximum spacing `0.0025`, both spanning `0..4` and containing all released nodes plus exact `z=0.295,2.33` boundaries;
- 20 Wm kernels ordered lens-major/source-major;
- 10 WW kernels ordered `(0,0),(0,1),...,(3,3)`;
- full-kernel coarse/fine relative normalization tolerance `<=5e-4`;
- strict Article-3 readiness `52%`;
- G7/G8/G9 OPEN and covariance BLOCKED.

## Stable source-efficiency representation

For normalized source distribution `n_i(z_s)`, compute directly

`g_i(z) = integral_z^infinity dz_s n_i(z_s) [chi(z_s)-chi(z)]/chi(z_s)`.

The numerical quadrature is frozen as follows.

1. If `z` is below the first released `Z_MID`, integrate on the complete released midpoint grid. No artificial point is inserted below the released domain because direct `n(z)` is frozen to zero there.
2. If `z` lies inside the released midpoint domain, insert `z` as the first quadrature node, with `n(z)` obtained by linear interpolation of the released normalized samples, followed by every released midpoint strictly above `z`.
3. At the inserted lower endpoint the geometric factor is exactly zero.
4. At every later source point compute the geometric factor as `(chi_s-chi)/chi_s`, not as `1-chi/chi_s`; this avoids subtractive loss near the lower endpoint.
5. The integrand must be finite and non-negative at every quadrature node. No negative `g` clipping is permitted in v0.2.
6. If `z>=Z_MID[-1]`, set the finite released-grid representation to exactly zero.

This is the same lensing-efficiency integral as v0.1, evaluated in a positivity-preserving form rather than by subtracting two nearly equal tail moments.

## Independent algebraic equivalence control

On every released raw `Z_MID` node, independently build positive reverse cumulative trapezoid tails

`T0_rev(z_i)=sum_{j>=i} trapezoid[n]`,

`T1_rev(z_i)=sum_{j>=i} trapezoid[n/chi]`,

where segments are accumulated from high z toward low z, never as `total-prefix`.

Compare

`g_tail_rev=T0_rev-chi*T1_rev`

against the direct nonnegative quadrature on the same raw nodes. Before the repaired run, freeze the implementation-equivalence tolerance to

`max_abs(g_direct-g_tail_rev) / max_abs(g_direct) <= 5e-12`

for every source bin. This tolerance is a numerical identity check only and cannot retain/reject any observation coordinate.

## Radial kernels

Unchanged from v0.1:

`B_Wm[a,i](z)=abs(n_lens,a(z) g_i(z)/chi(z))`, with the continuous bookkeeping value zero at `z=0`;

`B_WW[i,j](z)=abs((c/H(z)) g_i(z) g_j(z))`, `c=299792.458 km/s`.

Require all 20 Wm and 10 WW arrays to be finite and non-negative, with finite strictly positive total normalizations.

## Convergence and authority

For every radial kernel require the unchanged coarse/fine relative normalization difference `<=5e-4`. Canonically hash little-endian float64 logical arrays for the fine z grid, `chi`, `H`, normalized source/lens n(z), source efficiencies, 20 Wm kernels and 10 WW kernels. NPZ metadata is transport-only.

## Firewall

Exp073Z2 must not compute or read:

- physical k;
- any NaMaster angular window;
- `f_invalid`;
- retained/rejected observation rows;
- covariance or inverse covariance;
- whitening/Cholesky;
- nuisance SVD/rank;
- quotient/relation/null statistics;
- G8 outputs.

## Required PASS token

`PASS_EXP073Z2_DES_RADIAL_KERNEL_STABLE_DIRECT_V0_2`

PASS closes only the DES radial prerequisite. Strict scientific readiness remains **52%** until the complete DES angular authority and immutable full pre-support finite-operator manifest exist.
