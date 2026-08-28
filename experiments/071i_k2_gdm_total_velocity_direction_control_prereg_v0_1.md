# Exp071I — K2/GDM total-velocity transfer direction control v0.1

**Frozen before first Exp071I spectra:** 2026-08-28

## Question

Does the K2 fixed-total-`omega_m` known-sector direction that overlaps the GDM sound-speed-like direction in static matter/Weyl/slip space remain overlapping when compared in a same-definition CLASS total-velocity-transfer channel?

This is a theory-transfer specificity control. It is **not** tracer RSD, `f sigma_8`, a likelihood, covariance whitening, or observational distinguishability.

## Immutable parents

- K2 parameter grid and reference are inherited unchanged from Exp071C preregistration commit `4180661fe3187c710c363cdbafac12de2dc70d41`.
- Official CLASS is pinned to `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`.
- GDM parents are the immutable GDM Weyl/slip run `32774198185`, artifact family `gdm-weyl-slip-*`, generated with `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.
- Primary GDM axes are `cs2=1e-7` and `cv2=1e-7` relative to the GDM zero reference.
- Redshift grid is frozen to `[0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`.
- k grid is frozen to `[0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`.

## Cross-solver source contract frozen before execution

Direct audit of the two pinned `source/perturbations.c` files shows that both CLASS branches:

1. expose the transfer title `t_tot`;
2. write `tk[index_tp_theta_tot]` directly into CLASS-format transfer output;
3. define the total-velocity source as the same expression based on `rho_plus_p_theta/rho_plus_p_tot` plus the same `theta_shift` gauge/N-body correction.

The GDM fork changes the physical stress-energy content by adding GDM contributions, but not the output meaning of the `t_tot` channel. `t_b` is also common to both branches and is retained only as a non-classifying sensitivity channel.

The workflow must verify these source-contract strings/regexes against the two exact pinned source trees before scoring.

## K2 I/O-only extension

Exp071C generated K2 with `output = mPk`. Exp071I uses the same cosmology, gauge, primordial spectrum, z grid, k limits and K2 baryon/CDM grid, changing only:

`output = mPk,mTk`

The fresh Exp071I matter-power outputs must reproduce the immutable Exp071C `ref` and `bar1..bar5` numerical spectra on their stored grids with:

`max_abs_relative_P_difference <= 1e-10`.

If this integrity condition fails, Exp071I is **INVALID_FOR_SCIENCE** and no velocity classification is allowed. The threshold is an integrity threshold, not a science separator.

## Velocity response

For each model/reference pair and each frozen `(z,k)` node, define

`r_ttot = ln(abs(t_tot_model / t_tot_ref))`.

Before taking the logarithm require at every sampled node:

- finite model and reference values;
- `abs(t_tot_ref) > 1e-30`;
- `t_tot_model * t_tot_ref > 0` (sign preservation).

K2 local directions are `r_ttot / Delta_omega_b`, with

`Delta_omega_b = [0.0004, 0.0008, 0.0012, 0.0016, 0.0020]`

for `bar1..bar5` relative to the Exp071C reference. The compensating `Delta_omega_cdm = -Delta_omega_b` is inherited unchanged.

GDM directions are `r_ttot / 1e-7` for the `cs2` and `cv2` parents.

Flattening order is ascending redshift, then ascending frozen k.

## Frozen primary statistic

Primary K2 point: **bar1 only**.

Compute oriented Euclidean angles:

- `theta(K2_bar1_ttot, GDM_cs2_1e-7_ttot)`
- `theta(K2_bar1_ttot, GDM_cv2_1e-7_ttot)`

The directional separator is inherited unchanged from Exp071E/F/H:

`45 degrees`.

Primary PASS iff **both** oriented angles are at least 45 degrees.

Frozen classifications:

- `K2_TOTAL_VELOCITY_SEPARATED_FROM_BOTH_GDM_AXES_EXP071I`
- `K2_TOTAL_VELOCITY_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071I`

The outcome may strengthen or falsify velocity-channel specificity. Neither outcome is a dark-sector detection claim.

## Non-classifying robustness and sensitivity

These diagnostics cannot alter the primary classification:

1. K2 bar2..bar5 `t_tot` direction angle relative to bar1;
2. centered SVD of the five K2 `t_tot` directions;
3. GDM `cs2` vs `cv2` `t_tot` angle;
4. same calculations using the common `t_b` transfer instead of `t_tot`;
5. static Exp071F matter angles and Exp071H finite-bin temporal angles copied only as context, never used to tune Exp071I.

## Fail-closed rules

Any missing transfer column, missing redshift, insufficient k support, non-finite value, sign violation, reference denominator failure, source-contract mismatch, parent-artifact mismatch or K2 matter-power reproduction failure invalidates the science classification.

## Gate boundary

Regardless of Exp071I outcome:

- G7 remains OPEN;
- G8 remains OPEN;
- G9 remains OPEN;
- no covariance/whitening is authorized;
- no nuisance quotient is authorized;
- no tracer-RSD or observational claim is authorized.
