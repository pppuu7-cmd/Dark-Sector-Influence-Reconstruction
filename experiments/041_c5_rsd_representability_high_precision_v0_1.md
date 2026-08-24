# Experiment 041 — C5 high-precision RSD representability v0.1

**Date:** 2026-08-25  
**Status:** confirmatory protocol frozen after an explicitly exploratory low-precision extraction; independent high-precision run pending  
**Scope:** C5 designer-f(R) only; CAMB-native total-matter-density / Newtonian-CDM-velocity compression validity

## Question

Experiment 039 established that a scalar ShapeFit-style growth amplitude is only legitimate when the density and velocity fields are effectively related by one scale-independent amplitude over the smoothing window. Experiment 040 showed that temporal information is scientifically valuable but is not itself an RSD observable.

Experiment 041 asks a narrower and falsifiable question for the frozen C5 designer-f(R) manifold:

> Is the linear density-velocity relation sufficiently scale independent that the C5 response can be represented by a single scalar `f sigma_s8`, or does the C5 direction acquire a nonzero RSD representability defect?

This is a compression-validity test, not a DESI likelihood and not a parameter constraint.

## Frozen source convention

Pinned upstream:

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

The pinned CAMB source defines the matter-power/sigma density variable as

`transfer_power_var = Transfer_tot`,

and its native growth-sigma calculation uses

`Transfer_Newt_vel_cdm`

for the velocity leg. Therefore this experiment uses:

- density `delta = Transfer_tot`;
- velocity-like variable `Theta = Transfer_Newt_vel_cdm = -v_N,c k/Hcal`.

This matches CAMB's own `sigma8^2_vd/sigma8` convention rather than introducing an arbitrary new velocity definition. The baryon-velocity result is recorded only as a diagnostic.

## ShapeFit smoothing radius for C5

Experiment 038 hard-established that the frozen C5 `B0` direction lies on the same source-proven LCDM background branch and has exactly zero saved background/AP response across the production grid. The standard cosmological/recombination inputs are unchanged along this direction. Hence for this C5-only test

`r_d(B0)/r_d(B0=0) = 1`

within the frozen construction and the ShapeFit smoothing radius reduces to

\[
R=s\,8h^{-1}{\rm Mpc}=8h^{-1}{\rm Mpc}.
\]

This statement is restricted to the frozen C5 B0 manifold; other families must compute their own `s=r_d/r_d_ref`.

## Density-velocity moments

Using the saved same-run linear matter power `P_dd(k)` and the transfer ratio

\[
g(k,z)=\frac{\Theta(k,z)}{\delta(k,z)},
\]

construct

\[
\Delta^2_{dd}(k)=\frac{k^3P_{dd}(k)}{2\pi^2},
\]

and, because the frozen runs use a single adiabatic primordial mode,

\[
P_{d\Theta}=gP_{dd},\qquad P_{\Theta\Theta}=g^2P_{dd}.
\]

For a top-hat window `W_TH(kR)`, define

\[
S_{dd}=\int d\ln k\,\Delta^2_{dd}W_{TH}^2,
\]

\[
S_{d\Theta}=\int d\ln k\,\Delta^2_{dd}gW_{TH}^2,
\]

\[
S_{\Theta\Theta}=\int d\ln k\,\Delta^2_{dd}g^2W_{TH}^2.
\]

The representability defect is

\[
\boxed{
{\cal D}_{RSD}=1-\frac{S_{d\Theta}^2}{S_{dd}S_{\Theta\Theta}}
}.
\]

By Cauchy-Schwarz `0<=D_RSD<=1` in the exact positive-weight limit. `D_RSD=0` means that one scalar density-velocity amplitude represents the entire weighted k-range. A positive value measures the weighted non-collinearity caused by scale-dependent `g(k)`.

## Why a new high-precision run is required

The first exploratory extraction used the ordinary CAMB transfer text format `E15.6`. It suggested:

- GR / designer `B0=0`: `D_RSD` near the numerical floor (`~1e-10`);
- production C5: nonzero defects ranging from roughly `1e-6` to `1e-3` depending on `B0`, redshift and k-cut.

Those numbers were **inspected before this confirmatory protocol** and therefore are not themselves a hard result. In addition, the six-digit transfer mantissa is inadequate for a clean small-response threshold.

The confirmatory workflow changes only the text-output format in the pinned `Transfer_SaveToFiles` routine from

`E15.6 -> E24.16`.

No evolution equation, parameter, stability rule, sampling grid or physics routine is changed. The workflow records the exact I/O-only diff and rebuilds the pinned solver.

## Frozen models and redshifts

Use the exact hard-production config lineage `dsir_mgs1_hp_*` from immutable artifact:

- source run `32759477319`;
- artifact `9532245261`;
- digest `sha256:9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`.

Runs:

- GR;
- designer `B0=0`;
- exploratory transition control `B0=1e-7`;
- production `B0={1e-6,1e-5,1e-4,1e-3}`.

Redshifts are the frozen seven structure nodes

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`.

## k-range robustness

Compute the defect independently for upper cuts

`k_max={0.10,0.15,0.20,0.24} h/Mpc`.

The lower integration limit is the first common positive point between the transfer and matter-power tables. Matter power is log-interpolated onto the transfer k-grid; no extrapolation is allowed.

## Confirmatory hard thresholds

These thresholds are frozen **after** the explicitly exploratory `E15.6` extraction but **before** the independent `E24.16` target output. This chronology is intentional and must be preserved.

1. GR control:
   `max_z,kcut D_RSD <= 1e-8`.
2. Designer `B0=0` control:
   `max_z,kcut D_RSD <= 1e-8`.
3. Every production point `B0={1e-6,1e-5,1e-4,1e-3}` must show
   `max_z D_RSD(k_max=0.24) >= 1e-7`.
4. The same four production points must remain detectably non-collinear under the aggressive low-k cut:
   `max_z D_RSD(k_max=0.10) >= 1e-8`.
5. All moments and defects must be finite, and numerical Cauchy-Schwarz violations below zero may not exceed `1e-12` in magnitude.
6. The exact source variable contracts and the I/O-only precision patch must be verified by the workflow.

The `B0=1e-7` point is a transition diagnostic and has no required nonzero threshold.

No monotonicity requirement in `B0` is imposed; representability is a shape property and need not be monotonic with a microscopic parameter.

## Claim if PASS

A PASS establishes only that, for the frozen C5 designer-f(R) production manifold and the CAMB-native total-matter/CDM-velocity convention,

\[
\exists B_0>0:\quad {\cal D}_{RSD}>0
\]

well above the validated GR/B0=0 numerical floor, including after a conservative `k<=0.1 h/Mpc` cut.

Scientific interpretation:

**the C5 modified-gravity direction cannot in general be represented exactly by one scale-independent density-velocity growth amplitude over the smoothing window.**

That would make scalar `f sigma_s8` a lossy compression for this family and justify retaining scale-dependent anisotropic/RSD information in DSIR.

## Claim boundary

Experiment 041 is not:

- a DESI detection or parameter constraint;
- proof that current data can distinguish C5 from GR;
- a statement about arbitrary f(R) theories;
- a family-complete RSD operator;
- an intrinsic-rank result;
- a residual law or discovery.

C1/C2/C3/C4 still require their own density/velocity conventions and representability audits before the full observational growth block can be assembled.
