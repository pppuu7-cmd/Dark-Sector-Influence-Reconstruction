# Exp070C — C3/GDM native-grid physical power provider v0.1

Date frozen: 2026-08-27

## Purpose

Exp070A remains permanently `FAIL_C3_GDM_READONLY_DM_PHYSICAL_POWER_BRIDGE_V0_1`. Exp070B subsequently localized its ~4.75% target-grid failure to DSIR-side signed-amplitude interpolation: the same physical `D_m` source reconstructs native `pk_lin` to O(1e-14) at common native nodes. Exp070C is a new prospective provider certification. It does not reclassify Exp070A.

The scientific question is whether C3/GDM can provide solver-native physical inputs `P_mm`, signed `P_Wm`, and `P_WW` on a common native low-k grid without interpolating `D_m` amplitudes.

## Frozen provenance

- DSIR base: `00e6b1125bfa5ac7f5e7bf5e48a11af37ba46006`.
- Pinned solver: `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.
- Exp070B preregistration: `e386c0b742067d309a0116b4629b5f85ce3b55fd`.
- Exp070B result: `INTERPOLATION_DOMINATED`.
- Same cosmology, p8 precision preset, scalar adiabatic ICs and read-only accessor as Exp070A/B.

## Frozen cases and support

Redshifts:

`z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`.

GDM cases:

- `cs2 = 0`,
- `cs2 = 1e-6`,
- `cs2 = 1e-5`.

At each redshift use only nodes that are already present in both:

1. the read-only native `index_tp_delta_m` source grid, and
2. the standard transfer grid,

with `0.001 <= k/(h Mpc^-1) <= 0.1` and finite positive native `pk_lin(k,z)`.

Node equality after the transfer API's `h` unit conversion may use only a `64*eps(float64)` relative representation guard. This is not a scientific tolerance. No amplitude interpolation is permitted anywhere in Exp070C.

## Frozen provider construction

At each retained native node define the analytic primordial curvature spectrum

`P_R(k) = A_s * (k/k_pivot)^(n_s-1)`

with the inherited `A_s=2.10e-9`, `n_s=0.965`, `k_pivot=0.05 Mpc^-1`.

Define

`P_mm = (2*pi^2/k^3) * P_R(k) * D_m^2`.

From the standard transfer quantities at the exactly matched native node define the already audited DSIR Weyl convention

`W = 0.5 * k^2 * (phi + psi)`.

Then

`q_W = W / D_m`,

`P_Wm = q_W * P_mm`,

`P_WW = q_W^2 * P_mm`.

`P_Wm` remains signed. No absolute value may be applied to the cross-power.

## Frozen certification tests

### C1 — native matter-power closure

Compare provider `P_mm` to solver-native `pk_lin(k,z)` at every retained node.

PASS iff the maximum relative error over all cells/cases is `<= 1e-10`.

This tolerance is inherited from Exp070A's frozen native-output equivalence scale; it is not fitted to Exp070B's observed O(1e-14) residual.

### C2 — native-grid alignment

Every retained source node must have exactly one transfer-grid match under the machine-representation guard. Each case/redshift must retain at least one node. Record node counts and maximum representation-level k mismatch.

PASS iff these conditions hold. No nearest-neighbour or interpolation fallback is allowed.

### C3 — signed Weyl finiteness and nonzero source

All `D_m`, `phi`, `psi`, `W`, `q_W`, `P_mm`, `P_Wm`, and `P_WW` cells must be finite; every retained `D_m` must be nonzero; `P_mm>0`, `P_WW>0`, and `P_Wm!=0` at every retained node.

PASS iff all conditions hold.

### C4 — same-mode coherence

For every retained cell compute

`rho2 = P_Wm^2 / (P_WW * P_mm)`.

PASS iff `P_WW*P_mm>0` everywhere and

`max |rho2-1| <= 2e-10`.

The tolerance is inherited from Exp070A V5.

### C5 — missing-k^2 negative control

Construct deliberately wrong

`W_wrong = 0.5 * (phi + psi)`

and `q_wrong=W_wrong/D_m`, followed by the corresponding signed cross-power. The wrong construction must not be promoted regardless of residual behavior.

For the two nonzero GDM cases, require at least one retained node with

`|q_wrong/q_W - 1| > 1e-3`.

This uses the inherited Exp070A negative-control separation scale `1e-3` and verifies that the explicit `k^2` factor is operationally nontrivial.

### C6 — repeatability and no state mutation

Repeated `D_m` reads must be bitwise identical. Solver-native `pk_lin` evaluated on the fixed five Exp070A control k values before and after all read-only provider construction must agree to relative `<=1e-12`.

The tolerance is inherited from Exp070A V8.

### C7 — provider output contract

For every case/redshift output explicit native arrays for:

- `k (1/Mpc)`,
- `k (h/Mpc)`,
- `D_m`, `phi`, `psi`, `W`,
- `P_mm`, signed `P_Wm`, `P_WW`,
- native `pk_lin`,
- all closure/coherence diagnostics.

The output must state that it is a **native-grid physical input provider only** and contains no ACT/unWISE projection, support-validity mask, covariance whitening, nuisance projection, G7 relation fit, or observational likelihood evaluation.

PASS iff the schema is complete and the gate state is exactly `G7=OPEN, G8=OPEN, G9=OPEN`.

## Overall classification

`PASS_C3_GDM_NATIVE_GRID_PHYSICAL_POWER_PROVIDER_V0_1`

iff C1–C7 all pass. Otherwise

`FAIL_C3_GDM_NATIVE_GRID_PHYSICAL_POWER_PROVIDER_V0_1`.

Exp070A remains permanent FAIL under either outcome.

## G7 boundary

Even an Exp070C PASS cannot authorize the common physical support-validity mask by itself. C5 remains independently unresolved after Exp069B until its mechanism audit and any separately preregistered corrective bridge are completed.

Mandatory ordering remains:

validated C3 + C5 physical providers -> preregistered common support-validity mask -> covariance restriction/whitening -> nuisance tangent SVD/rank -> G7 quotient/relation/null control -> fresh G8 withheld family -> G9.

G7/G8/G9 remain OPEN.
