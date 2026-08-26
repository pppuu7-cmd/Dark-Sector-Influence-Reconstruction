# G7 linear training-family physical power-input feasibility — 2026-08-26

## Scope

Source-level audit only. This document does not fit a G7 relation, does not select a G8 withheld family, and does not change Exp068A. It asks whether existing DSIR **training families** can, in principle, provide the three independent physical spectra required by the validated ACT×unWISE linear/no-CLEFT projector:

\[
P_{WW}(k,z),\qquad P_{Wm}(k,z),\qquad P_{mm}(k,z),
\]

without reconstructing Weyl from matter through a GR Poisson relation.

Current top-level state remains G7/G8/G9 OPEN.

---

## 1. Designer f(R) / C5 — source-level feasible

Existing C5 calculations pin

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

The pinned H-EFTCAMB tree preserves the standard CAMB matter-power variable contract. Its `docs/source/transfer_variables.rst` defines

- `delta_nonu` as the CDM+baryon density variable;
- `Weyl` as

\[
W\equiv k^2(\phi+\psi)/2;
\]

- cross spectra can be requested directly with `var1,var2`, including `('Weyl','delta_nonu')`;
- the transfer-table `1/k^2` rescaling applies to `get_matter_transfer_data`, not to the physical power-spectrum variable itself.

Therefore a linear designer-f(R) ACT input can be requested directly from the modified solver as

\[
P_{mm}=P(\delta_{nonu},\delta_{nonu}),
\]

\[
P_{Wm}=P(Weyl,\delta_{nonu}),
\]

\[
P_{WW}=P(Weyl,Weyl),
\]

with `hubble_units=False`, `k_hunit=False`, and `nonlinear=False`.

This is **not** a Poisson reconstruction. The modified Einstein sector inside EFTCAMB determines its own Weyl transfer, and CAMB forms the requested auto/cross power from the solver transfer variables.

### Required prospective validation before G7 use

A separately preregistered bridge should still verify:

1. exact H-EFTCAMB commit and designer-f(R) stability;
2. physical `k[Mpc^-1]` and `P[Mpc^3]` conventions;
3. finite/nonzero signed `P_Wm` over the ACT projection support;
4. GR-limit agreement with the already validated pinned CAMB convention at `B0=0`;
5. a deliberately wrong transfer-table missing-`k^2` negative control;
6. no nonlinear/Halofit/CLEFT corrections in the v0.1 bridge.

Hence C5 is **source-level feasible but not yet observationally projected**.

---

## 2. GDM / C3 — physically feasible in principle, one accessor barrier remains

Existing C3 metric work pins

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

The hard GDM metric runs use

- `omega_cdm = 0`;
- `omega_gdm = 0.1200`;
- `w_gdm = 0` at every frozen time bin;
- single scalar adiabatic initial condition `ic=ad`;
- synchronous gauge;
- `output=mPk,mTk`.

### 2.1 What the solver's `mPk` actually uses

The pinned nonlinear module maps total matter power to `ppt->index_tp_delta_m`.

In `perturbations.c`, that source is explicitly described and implemented as the gauge-invariant/comoving matter density source, not the ordinary `d_tot` transfer column. Before the gauge correction,

\[
\delta_m^{(gauge)}=\frac{\delta\rho_m}{\rho_m}.
\]

For the frozen C3 species content with `omega_cdm=0` and `w_gdm=0`, the matter numerator contains baryons and GDM,

\[
\delta\rho_m=\rho_b\,\delta_b+\rho_{gdm}\,\delta_{gdm},
\]

and the matter velocity is built from

\[
\theta_m=\frac{(\rho+p)\theta_m}{\rho+p}
\]

with the GDM contribution carrying the explicit `(1+w_gdm)` factor in the pinned source. The final source adds the standard comoving-density correction; for the frozen `w_gdm=0` case this is

\[
D_m=\delta_m^{(gauge)}+3aH\frac{\theta_m}{k^2}.
\]

The exact GDM_CLASS source contains a special generalized `(1+P_m/\rho_m)` factor for nonzero GDM equation of state; it reduces to unity for the C3 `w_gdm=0` manifold.

### 2.2 Why ordinary `mTk` is insufficient

CLASS-format `mTk` from this pinned fork exports species density transfers, `d_tot`, `phi`, `psi`, etc., but **does not export the internal `index_tp_delta_m` source used to construct `mPk`**.

Therefore DSIR must not substitute

\[
D_m\stackrel{\rm invalid}{\leftarrow}d_{tot}
\]

merely because both look like matter-like transfer variables. Doing so could change gauge/species semantics and, crucially, the signed Weyl–matter cross power.

### 2.3 Clean prospective route

Because C3 uses a single adiabatic primordial mode, a signed physical power triplet can be formed from the same-mode transfer products once the internal `D_m` transfer is exposed:

\[
q_W(k,z)=k^2\frac{\phi+\psi}{2D_m},
\]

\[
P_{mm}=P_m,
\qquad
P_{Wm}=q_W P_m,
\qquad
P_{WW}=q_W^2 P_m.
\]

This is a transfer-product identity for one primordial mode. It is not a Poisson equation and does not infer metric dynamics from matter.

The remaining barrier is purely an **accessor/provenance barrier**: the pinned fork does not expose `D_m` in ordinary `mTk`.

A future preregistered GDM bridge may add a read-only diagnostic accessor for the already computed `index_tp_delta_m` source, provided that it does not alter evolution equations, source calculation, precision settings, or cosmology.

### Required hard controls

Before GDM enters a G7 observational training set, require at least:

1. accessor patch/source hash and proof that only output exposure changed;
2. the exposed `D_m` source is finite and nonzero on the frozen support;
3. reconstructing `P_mm` from `D_m` transfer normalization agrees with the solver's own `mPk` to a preregistered tolerance;
4. signed `P_Wm` is stable under a frozen precision/step check;
5. `P_{Wm}^2/(P_{WW}P_{mm})` obeys the expected single-IC coherence within the numerical floor of this solver path;
6. `d_tot` substitution is included as a negative/inequivalence control rather than silently accepted;
7. no Poisson relation between Weyl and matter is used.

Thus C3 is **physically feasible in principle but not yet bridge-certified**.

---

## 3. Consequence for the first linear/no-CLEFT G7 search

The cleanest current training path is not to invent new families. It is to finish observational and power-input bridges for already characterized families:

- C5 designer f(R): direct modified-CAMB `P_WW/P_Wm/P_mm` bridge;
- C3 GDM: read-only `D_m` accessor + transfer-product bridge;
- additional already-existing training families may be added only if their metric/matter power conventions are independently validated.

A fresh G8 withheld family must still not be chosen before the G7 relation and acceptance statistic are frozen.

The order remains:

1. finish Exp068A real-kernel physical forward gate;
2. freeze/measure the selected-26D linear/no-CLEFT nuisance tangent rank under Exp067A whitening;
3. validate training-family physical power inputs (C5 direct; C3 accessor route);
4. state the linear validity mask/domain explicitly;
5. only then fit one covariance-whitened nuisance-quotiented relation and run its frozen null/permutation control;
6. freeze that relation before selecting the fresh G8 withheld family.

No result in this document closes G7, G8, or G9.
