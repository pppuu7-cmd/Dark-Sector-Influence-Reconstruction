# Experiment 041 — C5 high-precision RSD representability v0.1

**Date:** 2026-08-25  
**Status:** **HARD PASS — `PASS_C5_RSD_REPRESENTABILITY_HIGH_PRECISION_V0_1`**  
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

An exact useful rewriting follows by defining the normalized positive weight

\[
p(k)=\frac{\Delta^2_{dd}W_{TH}^2}{S_{dd}}.
\]

Then

\[
\boxed{
{\cal D}_{RSD}
=\frac{\operatorname{Var}_{p}[g]}{\langle g^2\rangle_p}
}
\]

and the weighted coefficient of variation is

\[
\boxed{
\frac{\sigma_{g,p}}{|\langle g\rangle_p|}
=\sqrt{\frac{{\cal D}_{RSD}}{1-{\cal D}_{RSD}}}
}.
\]

Thus the defect is literally a normalized weighted variance of the scale-dependent effective growth ratio, not an arbitrary diagnostic distance.

## Why a new high-precision run was required

The first exploratory extraction used the ordinary CAMB transfer text format `E15.6`. It suggested:

- GR / designer `B0=0`: `D_RSD` near the numerical floor (`~1e-10`);
- production C5: nonzero defects ranging from roughly `1e-6` to `1e-3` depending on `B0`, redshift and k-cut.

Those numbers were inspected before the confirmatory protocol and therefore were never treated as a hard result. In addition, the six-digit transfer mantissa was inadequate for a clean small-response threshold.

The confirmatory workflow changed only the text-output format in the pinned `Transfer_SaveToFiles` routine from

`E15.6 -> E24.16`.

No evolution equation, parameter, stability rule, sampling grid or physics routine was changed. The workflow verified the exact one-line I/O-only diff and rebuilt the pinned solver.

## Frozen models and redshifts

Exact hard-production config lineage `dsir_mgs1_hp_*` from immutable artifact:

- source run `32759477319`;
- artifact `9532245261`;
- digest `sha256:9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`.

Runs:

- GR;
- designer `B0=0`;
- transition control `B0=1e-7`;
- production `B0={1e-6,1e-5,1e-4,1e-3}`.

Redshifts are the frozen seven structure nodes

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`.

## k-range robustness

The defect was computed independently for upper cuts

`k_max={0.10,0.15,0.20,0.24} h/Mpc`.

The lower integration limit is the first common positive point between the transfer and matter-power tables. Matter power is log-interpolated onto the transfer k-grid; no extrapolation is used.

## Confirmatory thresholds frozen before the high-precision target output

1. GR control: `max_z,kcut D_RSD <=1e-8`.
2. Designer `B0=0` control: `max_z,kcut D_RSD <=1e-8`.
3. Every production point `B0={1e-6,1e-5,1e-4,1e-3}`: `max_z D_RSD(k_max=0.24) >=1e-7`.
4. The same production points under the aggressive low-k cut: `max_z D_RSD(k_max=0.10) >=1e-8`.
5. All moments/defects finite; negative numerical Cauchy-Schwarz violations no larger than `1e-12`.
6. Exact source variable contracts and the I/O-only precision patch required.

`B0=1e-7` was a transition diagnostic and had no required nonzero threshold. No monotonicity requirement in `B0` was imposed.

## Hard result

Hard run:

- run ID `32791510072`;
- artifact ID `9543375564`;
- artifact name `c5-rsd-representability-high-precision-v0-1-c57c929e4c712e4bbe3e773e813fa6d782d4d3dc`;
- artifact digest `sha256:1e4d86f7f13185d69a07b71afa9bfd6fefa6003119064652d6388491738212bc`;
- result status `PASS_C5_RSD_REPRESENTABILITY_HIGH_PRECISION_V0_1`;
- `failures=[]`.

Maximum defects over redshift at `k_max=0.24 h/Mpc`:

| model | max `D_RSD` |
|---|---:|
| GR | `1.4189527331e-10` |
| designer `B0=0` | `1.4197298892e-10` |
| `B0=1e-7` control | `1.2562646543e-6` |
| `B0=1e-6` | `5.1775048112e-6` |
| `B0=1e-5` | `1.9224972376e-4` |
| `B0=1e-4` | `8.8058345719e-4` |
| `B0=1e-3` | `8.7803829400e-4` |

Maximum defects over redshift at `k_max=0.10 h/Mpc`:

| model | max `D_RSD` |
|---|---:|
| GR | `2.3362134449e-10` |
| designer `B0=0` | `2.3331336862e-10` |
| `B0=1e-7` control | `3.8910821454e-8` |
| `B0=1e-6` | `1.7383740314e-7` |
| `B0=1e-5` | `1.2403086244e-5` |
| `B0=1e-4` | `3.0063090369e-4` |
| `B0=1e-3` | `5.9388167251e-4` |

Every pre-frozen production threshold passes. The production defects stand roughly four to six orders of magnitude above the GR / `B0=0` numerical floor.

At the `k_max=0.24` redshift where each model's defect is largest, the exact weighted coefficient of variation of `g(k)` is approximately:

- `B0=1e-6`: `0.2275%`;
- `B0=1e-5`: `1.3867%`;
- `B0=1e-4`: `2.9688%`;
- `B0=1e-3`: `2.9645%`;
- GR / `B0=0`: about `0.00119%` numerical floor.

The `B0=1e-4` and `1e-3` defects plateau rather than remaining monotonic. This is permitted by the frozen protocol and is scientifically sensible because representability measures response shape, not simply microscopic amplitude.

## Scientific interpretation

**HARD ESTABLISHED for the frozen C5 manifold:** the designer-f(R) production direction cannot in general be represented exactly by one scale-independent density-velocity growth amplitude over the ShapeFit smoothing window. The loss remains detectable even after restricting to `k<=0.1 h/Mpc`.

Equivalently, modified gravity generates a genuinely scale-dependent

\[
g(k,z)=\Theta(k,z)/\delta(k,z)
\]

inside the relevant weighted range. Therefore a scalar `f sigma_s8`-like coordinate is a lossy compression for this C5 family; DSIR must retain scale-dependent anisotropic/RSD information or carry an explicit compression-error model.

This finding complements Experiment 038 in a particularly sharp way:

\[
K_{AP}t_{B0}=0
\]

exactly on the frozen designer background branch, while the density-velocity relation is nontrivially scale dependent. **The same microscopic direction is therefore geometry-null but growth-compression-active.**

## Claim boundary

Experiment 041 is not:

- a DESI detection or parameter constraint;
- proof that current data can distinguish C5 from GR;
- a statement about arbitrary f(R) theories;
- a family-complete RSD operator;
- an intrinsic-rank result;
- a residual law or discovery.

C1/C2/C3/C4 still require their own density/velocity conventions and representability audits before the full observational growth block can be assembled.
