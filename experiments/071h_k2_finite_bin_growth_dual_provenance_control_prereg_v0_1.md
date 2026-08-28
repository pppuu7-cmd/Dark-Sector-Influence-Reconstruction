# Exp071H — K2 finite-bin growth dual-provenance control preregistration v0.1

**Frozen after Exp071G v0.1 failed its parent-integrity assertion and before any K2-vs-GDM finite-bin-growth angle was computed.**

Date: 2026-08-28

## Motivation

Exp071G v0.1 was retired without a science classification because it incorrectly required equality between two distinct C3 local-tangent constructions:

- the single-step `1e-7` GDM parent used by Exp071E/F;
- the Exp040 averaged local tangent over the `<=1e-6` branch.

Exp071H preserves both constructions explicitly instead of conflating them.

## Scientific question

Does the finite-bin temporal derivative of the common matter response separate the K2 known-sector control from the two local GDM axes when the **same single-step `1e-7` parent convention used by Exp071E/F** is used for the primary test?

A second, non-classifying sensitivity calculation repeats the comparison against the frozen Exp040 averaged C3 tangents.

This remains a theory-space temporal-response test, not tracer RSD or observational `f sigma8`.

## Immutable parents

Primary parents:

- Exp071C run `33020201997`, artifact `9626235928` — K2 matter spectra.
- GDM metric run `32774198185`, artifact `9537340616` — `gdm0`, `cs2_1e-7`, `cv2_1e-7` matter spectra.
- Exp071F terminal summary — raw-matter primary K2 angles.

Sensitivity parent:

- `data/derived/comparison_readiness/local_response_tangents_v0_1.json`
  - `C3_GDM_cs2`: averaged `r/cs2` local tangent over `cs2<=1e-6`;
  - `C3_GDM_cv2`: averaged `r/cv2` local tangent over `cv2<=1e-6`.
- Exp040 terminal finite-bin-growth result.

## Frozen grid and temporal operator

Use exactly:

`z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`

`k = [0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`

`r_P = ln(P_model/P_ref)`

and the unchanged Exp040 operator

`g_P(i,k) = [r_P(z[i],k)-r_P(z[i+1],k)]/[2 ln(a[i]/a[i+1])]`.

## Primary tangents

K2 primary = bar1 only:

`t_g,K2 = g_P(bar1)/delta_f_b`.

Primary GDM axes:

- `t_g,cs(1e-7) = g_P(cs2_1e-7)/1e-7`
- `t_g,cv(1e-7) = g_P(cv2_1e-7)/1e-7`.

## Primary classification

Compute oriented angles:

- `theta_K2_cs_primary`
- `theta_K2_cv_primary`.

Use the same **45 degree** separation threshold inherited from Exp071E/F.

- both `>=45 deg` -> `K2_FINITE_BIN_GROWTH_SEPARATED_FROM_BOTH_GDM_1E7_AXES_EXP071H`
- otherwise -> `K2_FINITE_BIN_GROWTH_OVERLAPS_AT_LEAST_ONE_GDM_1E7_AXIS_EXP071H`.

No post-result retuning.

## Frozen Exp040 sensitivity construction — non-classifying

Take the stored 35-component raw matter tangents `C3_GDM_cs2` and `C3_GDM_cv2` from `local_response_tangents_v0_1.json`, reshape to 7×5, and apply the exact same finite-bin operator.

Required parent-integrity check:

`acute angle(growth(C3_GDM_cs2), growth(C3_GDM_cv2)) = 1.3340128035605052 deg`

within `1e-8 deg`.

Report K2 bar1 angles to these two averaged-growth axes, but **do not allow them to change the primary classification**.

The difference between primary and averaged-parent K2 angles is reported as a provenance-sensitivity diagnostic.

## Other integrity checks

1. The primary single-step GDM `cs2/cv2` growth acute angle is reported and must be finite/nonzero; Exp071G v0.1 observed `1.2926742378142244 deg` before stopping, but this value is diagnostic rather than a threshold.
2. Raw K2 bar1 vs single-step GDM matter angles must reproduce Exp071F:
   - cs2 `19.223081503733017 deg`
   - cv2 `19.037102938963482 deg`
   within `1e-8 deg`.
3. Exp040 endpoint, constant-mode and linearity operator controls remain frozen at `1e-12`, `1e-14`, `1e-12`.
4. All spectra/atlas vectors must be finite, complete and nonzero.

## K2 robustness — non-classifying

For bar2..bar5 report growth angle to bar1 and to both single-step GDM axes; report centered SVD and maximum drift. These cannot overturn the bar1 result.

## Interpretation

A primary PASS means temporal evolution separates K2 from both **single-step** GDM axes on this support. Sensitivity angles state whether that conclusion is stable to the older averaged-local C3 construction.

A primary FAIL means the residual K2/local-GDM ambiguity survives the finite-bin temporal derivative under the same parent convention as Exp071E/F. That would justify moving to a genuinely velocity/tracer or other independent block only after a common variable convention is proven.

No outcome closes G7, G8 or G9.
