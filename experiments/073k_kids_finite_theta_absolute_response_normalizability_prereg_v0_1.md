# Exp073K — KiDS finite-theta absolute-response normalizability mechanism audit — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp073K ASYMPTOTIC FIT OR NEW HIGH-ELL OUTPUT

## 1. Parent result

Bind the Exp073J KiDS-BNT component exactly as

`FAIL_EXP073J_KIDS_COMPONENT_REPRODUCTION_OR_NUMERICAL_COMPLETENESS`

from run `33045812989`, artifact `9635628042`, digest `sha256:907ac6130afb2292eac6e8cdd03493bb0f3b4507d5042e1ac15c282bbb901d3b`.

Preserve the BOSS non-classifying component `54/240`. Preserve the frozen Exp073J 5% criterion and physical rectangle. Exp073K is a mechanism/measure-existence audit and cannot by itself open covariance.

## 2. Question

Determine whether the P-independent positive support measure

`A_b(ell)=|R_b(ell)|`

for the **released finite-theta KiDS estimator** has a cutoff-independent finite normalization, or whether the discrete theta sampling produces an asymptotically non-integrable absolute response.

This is distinct from asking whether the signed bandpower estimator itself is well defined. Oscillatory cancellation may make the signed transform useful while its absolute domination measure is not normalizable.

## 3. Frozen asymptotic hypothesis

The pinned released estimator is a finite weighted sum of Bessel functions evaluated at 326 non-zero theta nodes, with an external Hankel factor proportional to `ell`.

For fixed theta,

`J_n(ell theta) = O(ell^-1/2)` oscillatory,

so unless exact cancellation removes the leading discrete sum for all phases, the absolute response is expected to scale in envelope as

`|R_b(ell)| = O(ell^1/2)`.

Then

`N_b(L)=integral_0^L |R_b(ell)| d ell = O(L^(3/2))`,

and the dyadic-shell fraction

`[N_b(2L)-N_b(L)]/N_b(2L)`

approaches

`q_sqrt = 1-2^(-3/2) = 0.6464466094067263`.

This numerical target is frozen before new Exp073K output.

## 4. Exact operator

Use exactly the already-bound `xi2bandpow.c` semantics, default `pfrac=0.5`, 326 logarithmic theta nodes, `0.5--300 arcmin` apodized production range, 8 bands `100<=ell<=1500`, and separate GGL and shear E-mode response formulas already frozen for Exp073J.

No BNT, source n(z), lens n(z), cosmology, k mapping or physical support mask is needed for the primary normalizability question; Exp073K isolates the angular estimator only.

## 5. Frozen numerical ladder

Evaluate direct positive angular normalization on dyadic cutoffs

`L = [7500, 15000, 30000, 60000, 120000]`.

Use a primary integration spacing `Delta ell=1` for `ell>=20` and the already-frozen logarithmic low-ell segment. For the final two shells, an equivalent chunked evaluation is allowed but no coarser than `Delta ell=1` for the primary classification.

A secondary `Delta ell=0.5` check is required for the shell `30000..60000` for at least bands 0, 3 and 7 in both GGL and shear. Its shell integral must agree with the primary to relative tolerance `5e-3`; otherwise classify numerical incompleteness rather than asymptotic behavior.

## 6. Frozen diagnostics

For each of 8 bands and each response type (`Wm/GGL`, `WW/shear`), record:

1. `N_b(L)` for every cutoff;
2. dyadic shell fractions for every adjacent pair;
3. local power-law exponents
   `p_j = log[N(2L)/N(L)]/log(2)`;
4. relative deviation of the last two shell fractions from `q_sqrt`;
5. signed integral over the same intervals as a non-classifying contrast only.

## 7. Frozen classifications

Classify

`NONNORMALIZABLE_DISCRETE_ABSOLUTE_RESPONSE_EXP073K`

iff all provenance/numerical controls pass and **for at least 7/8 bands in each response type**:

- the last local exponent is in `[1.35,1.65]`;
- the final dyadic shell fraction is in `[0.55,0.75]`;
- `N_b(L)` is strictly increasing across the full ladder;
- there is no evidence of saturation, defined prospectively as final shell fraction `<0.10`.

This broad frozen box tests the predicted `L^(3/2)` mechanism without fitting the acceptance region after seeing the data.

Classify

`FINITE_ABSOLUTE_RESPONSE_NOT_EXCLUDED_EXP073K`

iff all numerical controls pass and **at least 7/8 bands in each response type** instead have final shell fraction `<0.10` and final local exponent `<0.25`.

If neither pattern is met with trustworthy numerics, classify

`INDETERMINATE_ABSOLUTE_RESPONSE_ASYMPTOTICS_EXP073K`.

If exact source/operator reproduction or the frozen numerical controls fail, classify

`FAIL_EXP073K_REPRODUCTION_OR_NUMERICAL_COMPLETENESS`.

## 8. Consequence boundary

A `NONNORMALIZABLE...` result means the already-frozen P-independent positive absolute-response support fraction is not a well-defined cutoff-independent measure for the released finite-theta KiDS estimator. It does **not** mean the signed KiDS bandpower measurement is invalid, nor does it directly falsify any dark-sector model.

Such a result authorizes only a new prospectively frozen search for an observational operator whose positive physical-support measure is finite by construction, or a separately justified support definition that is not selected using covariance/held-out/model performance. It does not authorize post-hoc ell truncation or fiducial-power weighting inside Exp073J.

A `FINITE...` result authorizes returning to Exp073J with a prospectively frozen cutoff/convergence rule implied by the demonstrated saturation, but cannot alter the existing 5% support threshold.

No covariance, nuisance SVD/rank, relation/null output or G8 result may be read.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
