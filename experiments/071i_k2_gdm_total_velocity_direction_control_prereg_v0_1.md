# Exp071I — K2/GDM total-velocity transfer direction control v0.1

**Frozen before first Exp071I spectra:** 2026-08-28

**Pre-execution I/O amendment:** after the initial preregistration, but still before any Exp071I spectrum was generated or any Exp071I statistic inspected, direct parser audit established that `mTk` activates density/metric transfers while `vTk` independently activates velocity transfers in both pinned CLASS branches. Therefore both solver families must be rerun with the I/O-only extension `mPk,mTk,vTk`. This amendment changes no science parameter, primary observable, grid, threshold or classification rule.

## Question

Does the K2 fixed-total-`omega_m` known-sector direction that overlaps the GDM sound-speed-like direction in static matter/Weyl/slip space remain overlapping when compared in a same-definition CLASS total-velocity-transfer channel?

This is a theory-transfer specificity control. It is **not** tracer RSD, `f sigma_8`, a likelihood, covariance whitening, or observational distinguishability.

## Immutable numerical/parameter parents

- K2 parameter grid and reference are inherited unchanged from Exp071C preregistration commit `4180661fe3187c710c363cdbafac12de2dc70d41` and immutable run `33020201997`.
- Official CLASS is pinned to `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`.
- GDM numerical/parameter parents are the immutable GDM Weyl/slip run `32774198185`, artifact family `gdm-weyl-slip-*`, generated with `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829` and its frozen p8 precision file.
- Primary GDM axes are `cs2=1e-7` and `cv2=1e-7` relative to the GDM zero reference.
- Redshift grid is frozen to `[0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`.
- k grid is frozen to `[0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`.

The immutable parents are not treated as velocity-data sources because their historical output requests did not include `vTk`. They bind the cosmology, parameter steps, precision, solver SHAs and numerical matter-power results against which the fresh I/O-extended runs must be checked.

## Cross-solver source/output contract frozen before execution

Direct audit of the two pinned `source/perturbations.c` files shows that both CLASS branches:

1. expose the transfer title `t_tot` when velocity transfers are enabled;
2. write `tk[index_tp_theta_tot]` directly into CLASS-format transfer output;
3. define the total-velocity source with the same CLASS expression based on `rho_plus_p_theta/rho_plus_p_tot` plus the same `theta_shift` gauge/N-body correction.

Direct audit of both pinned input parsers additionally establishes that:

- `mTk`/`dTk` activate density transfers;
- `vTk` independently activates velocity transfers.

The GDM fork changes the physical stress-energy content by adding GDM contributions, but not the output meaning of the `t_tot` channel. `t_b` is also common to both branches and is retained only as a non-classifying sensitivity channel.

The workflow must verify these source/parser contracts against the two exact pinned source trees before scoring.

## Fresh I/O-only reproductions

### K2

Exp071C generated K2 with `output = mPk`. Exp071I uses exactly the same cosmology, gauge, primordial spectrum, z grid, k limits and K2 baryon/CDM grid, changing only the requested output to:

`output = mPk,mTk,vTk`

K2 reference:

- `omega_b = 0.0224`
- `omega_cdm = 0.1200`

K2 bars:

- bar1 `(0.0228, 0.1196)`
- bar2 `(0.0232, 0.1192)`
- bar3 `(0.0236, 0.1188)`
- bar4 `(0.0240, 0.1184)`
- bar5 `(0.0244, 0.1180)`

with fixed `omega_b + omega_cdm = 0.1424`.

### GDM

The GDM zero reference and the two primary one-sided models are regenerated with the exact immutable GDM solver SHA, baseline cosmology and frozen p8 precision used by run `32774198185`:

- `gdm0`: `cs2=0`, `cv2=0`;
- `cs1em7`: all frozen GDM sound-speed bins set to `1e-7`, `cv2=0`;
- `cv1em7`: all frozen GDM viscosity bins set to `1e-7`, `cs2=0`.

The only output extension is:

`output = mPk,mTk,vTk`

No GDM physical parameter or precision parameter may be altered.

## Numerical reproduction integrity gate

Before any velocity classification is allowed, fresh I/O-extended matter-power spectra must reproduce their immutable parents.

For every available parent/fresh matched redshift file and every common stored k node, require:

`max_abs_relative_P_difference <= 1e-10`.

This applies independently to:

- K2 `ref`, `bar1..bar5` against immutable Exp071C outputs;
- GDM `gdm0`, `cs1em7`, `cv1em7` against immutable run-32774198185 matter-power outputs.

The comparison must use numerical arrays rather than filenames alone and must fail closed if the expected parent files cannot be uniquely bound.

If either family violates this integrity gate, Exp071I is **INVALID_FOR_SCIENCE** and no velocity classification is allowed. The `1e-10` tolerance is an integrity/reproduction criterion, not a science separator.

## Velocity response

For each model/reference pair and each frozen `(z,k)` node, define

`r_ttot = ln(abs(t_tot_model / t_tot_ref))`.

Before taking the logarithm require at every sampled node:

- finite model and reference values;
- `abs(t_tot_ref) > 1e-30`;
- `t_tot_model * t_tot_ref > 0` (sign preservation).

K2 local directions are `r_ttot / Delta_omega_b`, with

`Delta_omega_b = [0.0004, 0.0008, 0.0012, 0.0016, 0.0020]`

for `bar1..bar5` relative to the K2 reference. The compensating `Delta_omega_cdm = -Delta_omega_b` is inherited unchanged.

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

Any missing transfer column, missing redshift, insufficient k support, non-finite value, sign violation, reference denominator failure, source/parser-contract mismatch, parent-artifact ambiguity, solver-SHA mismatch, precision mismatch or matter-power reproduction failure invalidates the science classification.

## Gate boundary

Regardless of Exp071I outcome:

- G7 remains OPEN;
- G8 remains OPEN;
- G9 remains OPEN;
- no covariance/whitening is authorized;
- no nuisance quotient is authorized;
- no tracer-RSD or observational claim is authorized.
