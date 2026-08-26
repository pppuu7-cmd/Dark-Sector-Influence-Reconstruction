# C5 designer-f(R) exact-zero analytic GR boundary

Date: 2026-08-27  
Status: **SOURCE-DERIVED MECHANISM THEOREM — NOT A PROVIDER CERTIFICATION, NOT A RECLASSIFICATION OF EXP069B**

Pinned upstream: `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

## Question

Does `EFTB0=0` physically define an f(R) state distinct from GR, or does the pinned designer system itself contain an exact GR solution that the numerical root-finding branch only approximates?

This note answers that question algebraically from the upstream equations. It does not use the Exp069E numerical output.

## 1. LCDM background functions are exact in the upstream parametrization

For `EFTwDE=0`, the pinned designer f(R) code allocates `wDE_LCDM_parametrization_1D`.

The pinned neutral parametrization defines exactly

- `w(a) = -1`;
- `dw/da = d2w/da2 = d3w/da3 = d4w/da4 = 0`;
- the special designer integral `I(a)=a^2`.

Source:

`fortran/eftcamb/04f_parametrizations_1D/04p000_neutral_parametrizations_1D.f90`

https://github.com/EFTCAMB/EFTCAMB/blob/16d9c4e9f85751e30efd0a53b177941713078904/fortran/eftcamb/04f_parametrizations_1D/04p000_neutral_parametrizations_1D.f90

## 2. Exact particular solution on LCDM

The designer source sets

`g = -( ln I(a) - 2 ln a ) / 3`.

Since `I(a)=a^2`,

`g=0`, `g'=0`, `g''=0`, `g'''=0`.

The source constructs

`CoeffA_Part = (-6 C)/[-3 a w' + 9w^2 +(18-3B)w +9-3B+C]`.

For `w=-1` and `w'=0`, the denominator reduces exactly to `C`, so

`CoeffA_Part = -6`.

It then defines

`yStar = CoeffA_Part * Omega_vac * exp(-2 x_initial) * I(a_initial)`.

Because `I(a)=a^2=exp(2x)`, this is

`yStar = -6 Omega_vac`.

Thus the initialized state is

`y1 = A yPlus - 6 Omega_vac`,

`y2 = PPlus A yPlus`.

For the exact homogeneous amplitude

`A=0`,

we obtain

`y1 = -6 Omega_vac`,

`y2 = 0`.

Source:

`fortran/eftcamb/07f_designer_models/007p3_Designer_fR.f90`

https://github.com/EFTCAMB/EFTCAMB/blob/16d9c4e9f85751e30efd0a53b177941713078904/fortran/eftcamb/07f_designer_models/007p3_Designer_fR.f90

## 3. The A=0 state remains an exact solution of the designer ODE

On the LCDM background, `g'=g''=g'''=0`, so the dark-energy contribution to `E(a)` is constant.

Substituting `y1=-6 Omega_vac` and `y2=0` into the designer equation gives

`dy1/dx = y2 = 0`.

The source term in `dy2/dx` cancels the term proportional to `y1` because `6 E_de + y1 = 0`. Therefore

`dy2/dx = 0`.

Hence `(-6 Omega_vac,0)` is not merely an initial approximation: it is the exact LCDM/GR solution of the designer background ODE.

## 4. Exact EFT functions of this state

The pinned `output` routine computes

`f_sub_R = ydot(1) / [3 (4 E' + E'')]`.

For the exact A=0 solution, `ydot(1)=0`, therefore

`f_sub_R = 0`.

The code stores

`EFTOmega = f_sub_R`,

so the effective Planck-mass modification is exactly zero.

It also computes

`EFTLambda = 0.5 H0^2 ( y1 - f_sub_R R ) a^2`.

At A=0 this becomes the ordinary cosmological-constant term. The Return-to-GR definition explicitly tests the combination

`abs(EFTLambda/a^2 + params_cache%grhov)`,

which is the corresponding GR-offset coordinate.

Finally, `EFTCAMBDesignerFRSecondOrderEFTFunctions` sets every `Gamma1..Gamma6` entry used by the RGR vector to literal `0._dl` for designer f(R).

Therefore the pinned theory contains an exact GR boundary at A=0.

## 5. Relation to B0

The model parameter exposed to users is `B0`, not A. Upstream determines A by solving

`B0(A) = B0_wanted`.

For `B0_wanted=0`, however, there is **no exact-zero dispatch** to `A=0` or to the ordinary `EFTflag=0` GR branch. The same generic bracketing and Brent root-finding path is used.

The pinned source calls

`zbrent(..., 1.d-50, self%B0, success)`

and only afterwards computes `BTemp1=DesFR_BfuncA(realAp)` for a debug compatibility check. The apparent compatibility rejection is disabled by the literal `.and..false.` condition.

Thus a numerically determined `realAp != 0` can survive even when the requested theoretical parameter is exactly `B0=0`.

This is a concrete mechanism by which a theoretically exact GR boundary can acquire a small numerical EFT residue.

## 6. What is proven and what is not

### Proven from pinned source and algebra

1. For the LCDM designer background, `A=0` is an exact solution.
2. That solution has `EFTOmega=0` and the GR cosmological-constant EFT contribution.
3. Designer f(R) second-order Gamma functions are exactly zero in the pinned implementation.
4. `EFTB0=0` is still routed through generic numerical inversion `B0(A)=0`; there is no special exact-GR dispatch.

### Not proven by this note

1. The actual numerical root returned for `EFTB0=0` is nonzero.
2. Any such root residue quantitatively causes the ~5.3e-6 matter/Weyl power mismatch.
3. A piecewise `B0=0 -> GR` software dispatch is by itself a valid C5 physical provider.
4. Positive-B0 solutions are unaffected by numerical branch floors.

Those are numerical/provider questions. Exp069E is the source-native numerical test of item 1/2 at the EFT-function level.

## 7. Consequence for a future corrective provider

If Exp069E finds nonzero source-native RGR-subset entries at literal `B0=0`, the next provider design may legitimately use this theorem as causal justification for an **analytic exact-zero boundary condition**. But certification must not become tautological.

A future prospective provider would still need, before acceptance:

- exact GR closure at `B0=0` under the pre-existing hard criterion;
- independent positive-B0 controls approaching the boundary continuously over a frozen sequence;
- a nontrivial production `B0` signal;
- solver-state/readback/provenance controls;
- signed `P_Wm`, `P_WW`, `P_mm` consistency;
- no threshold retuning after output.

Exp069B remains a permanent FAIL. A corrected provider, if eventually validated, must receive a new experiment number and cannot rewrite that history.

## Gate state

- C3 physical provider: eligible from Exp070C.
- C5 physical provider: **NOT YET ELIGIBLE**.
- common support-validity mask: not authorized.
- G7: OPEN.
- G8: OPEN.
- G9: OPEN.
