# Exp071D — K2 known-sector metric/slip specificity control v0.1

**Frozen before execution:** 2026-08-28.

## Motivation

Exp071C established that the matter-only F30 morphology is not uniquely dark-sector-specific: the K2 family, which redistributes baryon and CDM density at fixed `omega_m=0.1424`, passes the full F30 gate and every leave-one-redshift gate. Separately, the frozen GDM Weyl/slip hard regression showed that local `cs2` and `cv2` rays are nearly aligned in the Weyl-amplitude response but are strongly separated in gravitational-slip response.

Exp071D asks the next prospective question: **does the known-sector K2 family that mimics F30 in matter space also activate the metric-slip channel with a comparable slip-to-Weyl response ratio?**

This is a mechanism-control diagnostic, not an observational detection and not a G7/G8/G9 gate.

## Immutable parent bindings

1. Exp071C immutable artifact from run `33020201997` must have:
   - status `COMPLETE_KNOWN_SECTOR_F30_SPECIFICITY_CONTROL_V0_1`;
   - `primary_specificity_classification = F30_DARK_SPECIFICITY_WEAKENED_BY_KNOWN_SECTOR_CONTROL`;
   - K2 `pass_full_and_all_leave_one_z = true`.
2. GDM metric control immutable artifact from run `32774198185` must have hard-gate status `PASS_GDM_SLIP_BREAKS_LOW_K_DEGENERACY`.

## Fresh known-sector solver

Use official `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`.

Reference:
- `h=0.67`, `omega_b=0.0224`, `omega_cdm=0.1200`, `N_ur=3.046`;
- `A_s=2.10e-9`, `n_s=0.965`, no reionization;
- scalar adiabatic synchronous calculation;
- outputs `mPk,mTk`.

K2 points, all at fixed `omega_b + omega_cdm = 0.1424`:

- `(0.0228,0.1196)`;
- `(0.0232,0.1192)`;
- `(0.0236,0.1188)`;
- `(0.0240,0.1184)`;
- `(0.0244,0.1180)`.

Frozen redshifts:
`[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`.

Frozen k grid for the metric response:
`[0.001,0.003,0.01,0.03,0.1] h/Mpc`.

## Metric definitions

From CLASS transfer columns `phi` and `psi`, for each K2 model relative to the reference:

- `W = phi + psi` (the factor 1/2 is irrelevant to a same-solver log response);
- `r_W = ln |W_model/W_ref|`;
- `slip = (phi-psi)/(phi+psi)`;
- `Delta_slip = slip_model - slip_ref`.

Potentials are interpolated linearly in `ln k` without taking logs of signed amplitudes, exactly as in the prior GDM metric-control implementation.

For every model define the channel ratio

`q_slip/W = ||Delta_slip||_2 / ||r_W||_2`

over the same flattened `(z,k)` grid.

The ratio is dimensionless and does not depend on how the K2 family parameter is scaled.

For the immutable GDM artifact, calculate the same finite-response ratio at the frozen `1e-7` `cs2` and `cv2` points using the stored response arrays.

## Prospective classification rule

No numerical threshold is fitted.

- `K2_SLIP_TO_WEYL_RATIO_BELOW_BOTH_GDM_AXES_EXP071D` if the maximum K2 `q_slip/W` is strictly smaller than both GDM `1e-7` ratios.
- `K2_SLIP_TO_WEYL_RATIO_OVERLAPS_GDM_AXES_EXP071D` otherwise.

This ordering classification is descriptive mechanism evidence only. Even the first outcome does not prove dark-sector specificity: it shows only that the particular K2 matter-space mimic activates less relative slip than both frozen GDM local axes under this metric.

## Additional diagnostics frozen before output

Record:
- all five K2 `q_slip/W` ratios;
- GDM `cs2` and `cv2` ratios;
- K2 channel norms;
- angles among one-sided K2 tangents in `r_W` and `Delta_slip` space;
- K2 family SVD in each channel;
- Weyl-sign preservation and denominator safety.

No result may be discarded for an inconvenient sign or angle.

## Anti-retuning

Forbidden after output:
- changing the K2 grid, z grid or k grid;
- replacing `phi+psi` or the slip definition;
- inventing a tolerance to reverse the strict-ordering classification;
- training/retraining F30 on K2;
- using observational covariance, nuisance fitting or G7/G8 quantities.

## Gate state

G7/G8/G9 remain OPEN irrespective of Exp071D outcome.
