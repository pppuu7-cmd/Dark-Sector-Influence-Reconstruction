# Exp069A — C5 designer-f(R) physical `P_WW/P_Wm/P_mm` bridge v0.1

**Date:** 2026-08-26  
**Status:** prospective scientific contract frozen before the first Exp069A numerical output.

## 1. Purpose

Certify that the already-established C5 designer-`f(R)` training family can feed the solver-neutral ACT×unWISE linear/no-CLEFT projector with three **independent physical power spectra**

\[
P_{WW}(k,z),\qquad P_{Wm}(k,z),\qquad P_{mm}(k,z),
\]

without reconstructing Weyl from matter through a GR Poisson equation and without using text transfer-table columns as if they were physical power variables.

This is a power-input bridge only. It does not project ACT observables, does not choose a physical support mask, does not construct a nuisance quotient, and does not fit G7.

Exp068A remains a permanent FAIL. Exp068B is a separate forward-interface gate and may run independently of this bridge.

## 2. Immutable solver provenance

Pinned solver:

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

The pinned source contract used by this experiment is:

- `delta_nonu`: CDM+baryon density variable;
- `Weyl = k^2(phi+psi)/2`;
- power spectra may be requested directly for arbitrary transfer-variable pairs;
- `get_matter_transfer_data` returns transfer variables divided by `k^2`, but **matter power-spectrum functions do not apply that transfer-table rescaling**.

Any solver SHA mismatch is a hard Exp069A FAIL.

## 3. Frozen C5 cosmology and designer model

Use the existing DSIR C5 common baseline, not a newly tuned cosmology:

- `H0 = 67 km/s/Mpc`;
- `ombh2 = 0.0224`;
- `omch2 = 0.1200`;
- `omnuh2 = 0`;
- `massless_neutrinos = 3.046`;
- no massive neutrino eigenstates;
- `helium_fraction = 0.2404`;
- `As = 2.10e-9`;
- `ns = 0.965`;
- reionization disabled for this transfer-only bridge;
- `do_nonlinear = 0`;
- no HALOFIT/HMcode/CLEFT contribution.

Designer branch:

- `EFTflag = 3`;
- `DesignerEFTmodel = 1`;
- `EFTwDE = 0`;
- stability settings exactly as in the existing hard C5 manifold workflows;
- `EFTCAMB_turn_on_time = 0.01`;
- `EFTCAMB_stability_time = 1e-10`;
- `EFTCAMB_stability_threshold = 0`.

Frozen `B0` controls:

- GR reference: `EFTflag=0`;
- exact designer GR-limit control: `B0=0`;
- production bridge points: `B0={1e-6, 1e-5, 1e-4, 1e-3}`.

No `B0` point may be removed after the first Exp069A output merely because its power bridge is inconvenient.

## 4. Frozen physical evaluation grid

All `k` arguments below are physical `Mpc^-1`, not `h/Mpc`:

\[
z=\{0,0.295,0.51,0.934,1.491,2.33,3.0\},
\]

\[
k=\{0.003,0.01,0.03,0.10,0.20\}\ {\rm Mpc}^{-1}.
\]

The internal solver transfer range must extend beyond the largest requested physical `k`; freeze `kmax_internal = 0.30 Mpc^-1`.

This grid is for bridge certification, not a declaration that linear theory is physically valid across every ACT kernel at all these points. Physical validity is a later separately preregistered gate.

## 5. Frozen direct-power construction

For each GR/designer run, read the exact `.ini` into the pinned Python/CAMB wrapper and calculate transfer/power results from that same solver state.

Request, with `nonlinear=False`, `hubble_units=False`, `k_hunit=False`:

\[
P_{mm}=P(\texttt{delta_nonu},\texttt{delta_nonu}),
\]

\[
P_{Wm}=P(\texttt{Weyl},\texttt{delta_nonu}),
\]

\[
P_{WW}=P(\texttt{Weyl},\texttt{Weyl}).
\]

No Poisson relation, no matter-to-Weyl closure, no forced rank-one replacement and no transfer-table `1/k^2` assumption may be used to create these three primary outputs.

## 6. Hard tests

### A1 — provenance and source contract

Require exact solver SHA and pinned source/documentation evidence for:

1. `delta_nonu` variable;
2. `Weyl = k^2(phi+psi)/2`;
3. arbitrary cross-power request support;
4. transfer-table-only `1/k^2` rescaling statement.

### A2 — stable solver execution

GR, exact `B0=0`, and every production `B0` run must complete without `ERROR STOP` and the designer runs must report the pinned EFTCAMB stability success condition.

### A3 — physical-unit direct powers

For every frozen `(B0,z,k)` cell require:

- finite `P_mm`, `P_Wm`, `P_WW`;
- `P_mm > 0`;
- `P_WW > 0`;
- `P_Wm != 0`;
- no nonlinear correction requested;
- physical `k[Mpc^-1]` and `P[Mpc^3]` interface flags exactly as frozen above.

### A4 — unit-conversion roundtrip

For the GR reference and exact `B0=0` designer run, independently request `P_mm` in CAMB's `(k/h, (Mpc/h)^3)` convention on the corresponding `k/h` grid and convert back using

\[
k = h\,k_h,
\qquad
P_{\rm Mpc^3}=P_{(Mpc/h)^3}/h^3.
\]

Require relative agreement with the direct physical-unit `P_mm` values within

\[
\epsilon_{unit}=2\times10^{-8}.
\]

This is a unit/interface control, not a model comparison.

### A5 — exact designer GR-limit agreement

Compare the exact designer `B0=0` run against the `EFTflag=0` GR reference at every frozen cell for all three blocks.

For each block define

\[
r_X=\frac{|P_X^{B0=0}-P_X^{GR}|}{\max(|P_X^{GR}|,10^{-300})},
\quad X\in\{mm,Wm,WW\}.
\]

Require

\[
\max r_X \le 5\times10^{-6}
\]

for each of the three blocks separately.

This tolerance is frozen before the first Exp069A output and is comparable to, but does not weaken, the previously certified C5 exact-zero density-response scale.

### A6 — signed coherence consistency

All runs use a single adiabatic primordial scalar mode and no massive-neutrino isocurvature source. Therefore the direct same-mode powers should satisfy the transfer-product coherence identity up to numerical interpolation error:

\[
\rho^2(k,z)=\frac{P_{Wm}^2}{P_{WW}P_{mm}}.
\]

Require finite positive denominator and

\[
|\rho^2-1|\le 2\times10^{-5}
\]

at every frozen cell for GR, `B0=0`, and all production `B0` points.

The sign of `P_Wm` is recorded and must not be replaced by `|P_Wm|`.

### A7 — deliberately wrong missing-`k^2` negative control

Construct a **diagnostic only** wrong Weyl-power convention

\[
P_{WW}^{wrong}=P_{WW}/k^4,
\qquad
P_{Wm}^{wrong}=P_{Wm}/k^2,
\]

which mimics treating the transfer-table `Weyl/k^2` column as if it were the physical Weyl variable.

For the GR reference require that this wrong convention is clearly inequivalent to the direct physical convention: across the frozen `k` grid at every tested `z`, the ratio must show the expected explicit nonconstant `k^{-4}` / `k^{-2}` scaling and the maximum relative discrepancy from the correct block must exceed `1e2` in at least one frozen cell for both `WW` and `Wm`.

The negative control is never eligible as a production bridge.

### A8 — production nondegeneracy diagnostic

For each production `B0`, record the maximum absolute log-response relative to the exact designer `B0=0` control in each block,

\[
R_X=\ln\left|P_X(B0)/P_X(0)\right|.
\]

Do **not** impose a fitted common slope or magnitude law in Exp069A. The only hard requirement is that each production run is not bitwise identical to the exact-zero control in all three blocks simultaneously.

This prevents a disconnected/no-op designer run from passing the bridge without turning Exp069A into a mechanism-selection experiment.

## 7. Hard outcome

PASS iff A1-A8 all pass:

`PASS_C5_DESIGNER_FR_PHYSICAL_POWER_BRIDGE_V0_1`.

Otherwise:

`FAIL_C5_DESIGNER_FR_PHYSICAL_POWER_BRIDGE_V0_1`.

Scientific FAIL must be preserved as an artifact and must not be converted to an infrastructure exception. Infrastructure problems occurring before the numerical science output may be repaired only if this frozen contract is unchanged.

## 8. Anti-retuning

After the first Exp069A output do not alter:

- solver commit;
- C5 cosmology;
- designer/stability settings;
- `B0` grid;
- physical `(z,k)` grid;
- power-variable pairs;
- physical-unit flags;
- GR-limit tolerance;
- coherence tolerance;
- negative-control definition;
- PASS/FAIL logic.

## 9. Gate semantics and next step

A PASS certifies **C5 only** as a physical input provider for the validated linear/no-CLEFT ACT projector. It does not certify C3, does not certify linear physical validity of all ACT bins and does not close G7/G8/G9.

After C5 bridge certification, the next independent training-input prerequisite is the C3/GDM read-only gauge-invariant `D_m` accessor bridge with native-`mPk` reconstruction control. Only after the training-family power bridges are certified may the common survey-kernel validity/leakage mask be frozen and evaluated.

Top-level state entering Exp069A: **G7 OPEN, G8 OPEN, G9 OPEN**.
