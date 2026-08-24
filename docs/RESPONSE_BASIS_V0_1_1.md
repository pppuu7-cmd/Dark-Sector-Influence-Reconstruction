# DSIR response basis v0.1.1

**Status:** frozen candidate pending the direct cross-solver response-quotient bridge.  
**Parent:** `dsir-response-v0.1`.

## Why v0.1.1 exists

The v0.1 perturbation block used a generic `P_m` label. Subsequent Newtonian/synchronous audits showed that this is too ambiguous: species-level density contrasts are gauge dependent, default-precision solver outputs can carry gauge/precision contamination, and an old `class_iv` transfer header is misaligned in synchronous interacting-vacuum output.

The correction is not to discard matter power. It is to define exactly which matter perturbation generates it.

## Common perturbation variable

For the documented total matter component set,

\[
\delta_m=\frac{\sum_i\rho_i\delta_i}{\rho_m},
\qquad
\theta_m=\frac{\sum_i(\rho_i+p_i)\theta_i}{\rho_m+p_m},
\qquad
w_m=\frac{p_m}{\rho_m}.
\]

The comoving matter density contrast is

\[
\boxed{\Delta_m=\delta_m+3(1+w_m){\cal H}\frac{\theta_m}{k^2}},
\qquad {\cal H}=aH.
\]

For stable pressureless matter, `w_m=0` and

\[
\Delta_m=\delta_m+3{\cal H}\theta_m/k^2.
\]

Both pinned CLASS-family implementations used by DSIR implement this concept internally for the total-matter source. GDM_CLASS includes the explicit `(1+P_m/rho_m)` correction when GDM carries pressure. See Experiment 018.

Define

\[
P_\Delta(k,z)=P[\Delta_m](k,z)
\]

and the production response coordinate

\[
\boxed{
 r_\Delta(k,z)=\ln\frac{P_\Delta^{\rm model,S}(k,z)}
 {P_\Delta^{\rm ref,S}(k,z)}
}
\]

where `S` is the **same solver lineage and numerical configuration** for model and reference.

This same-solver quotient is mandatory whenever possible. It suppresses solver-version, sampling and normalization differences before responses from different theory families are compared.

## Background coordinate retained from v0.1

\[
r_E(z;z_*)=
\ln\left[
\frac{H(z)/H(z_*)}{H_{\rm ref}(z)/H_{\rm ref}(z_*)}
\right],
\qquad z_*=0.51.
\]

Frozen redshift nodes:

`{0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33}`.

Frozen linear k nodes:

`{0.001, 0.003, 0.01, 0.03, 0.1} h/Mpc`.

## Numerical evidence leading to this definition

A matched CDM Newtonian/synchronous audit in pinned GDM_CLASS found:

- default-precision raw matter-power mismatch within the linear core: about `9.84e-5`;
- p8 raw matter-power mismatch: about `5.1e-6`;
- p8 explicitly reconstructed comoving `Delta_m` mismatch: `2.5514e-6`;
- hard comoving gauge threshold frozen before rerun: `5e-6`; hard rerun PASS.

Thus numerical precision matters, but an explicit comoving construction gives the cleanest common physical coordinate.

## Solver requirements

Before a solver/family can enter a production DSIR rank matrix:

1. Pin the exact source commit.
2. State the gauge used internally.
3. State exactly which components enter `rho_m,p_m,delta_m,theta_m`.
4. Audit the source code or explicitly reconstruct `Delta_m`.
5. Compute the model/reference ratio inside the same solver.
6. Pass the solver's own zero/control-limit regression.
7. If two different solvers overlap on a physical deformation, run a cross-solver **response quotient** bridge; do not demand bitwise equality of absolute spectra from different code vintages.

## Known `class_iv` transfer caveat

In the pinned synchronous interacting-vacuum output, `theta_idm_iv` is not an active source, but the title generator still inserts a velocity-block label named `d_idm_iv`. This creates a one-column title/data shift for subsequent velocity transfers. The internal total-matter `mPk` path is not affected.

Therefore species-level `vTk` columns from this fork are **not** common DSIR coordinates unless their order is recovered from source indices or the title bug is separately repaired and regression-tested.

## Rank/law-discovery rules unchanged

Before SVD/rank/law discovery:

- project exact identities and calibration modes;
- remove measurement-induced nuisance directions;
- whiten with the correct covariance;
- propagate family priors into `R_model(pi)` null calibration;
- never count a derived coordinate and its parents as independent dimensions.

## Acceptance gate for final v0.1.1

The current file is a frozen candidate. Final PASS requires a direct **cross-solver response-quotient bridge** on at least one nontrivial overlapping deformation. The preferred control is smooth `wCDM` relative to LambdaCDM, computed independently in both pinned solver lineages with matched physics and then compared at the response level.
