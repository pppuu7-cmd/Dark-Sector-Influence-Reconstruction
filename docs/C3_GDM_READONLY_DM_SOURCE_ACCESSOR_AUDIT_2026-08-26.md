# C3/GDM read-only gauge-invariant `D_m` accessor audit — 2026-08-26

## Purpose

This note fixes the minimal implementation boundary needed to feed the C3 GDM training family into the future solver-neutral ACT×unWISE linear/no-CLEFT projector without replacing the native GDM matter source by ordinary transfer-table `d_tot` and without modifying the GDM perturbation equations.

Pinned source audited:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

No C3 physics was rerun while producing this audit.

## 1. Native `mPk` source identity

The pinned nonlinear module selects the perturbation source used for native total matter power as

```c
if ((pnl->has_pk_m == _TRUE_) && (index_pk == pnl->index_pk_m)) {
  index_tp = ppt->index_tp_delta_m;
}
```

Thus the authoritative transfer amplitude underlying native `P_m(k,z)` is `ppt->index_tp_delta_m`.

This is **not** the ordinary transfer-output column `d_tot` and must not be silently replaced by it.

## 2. Meaning of `index_tp_delta_m`

The pinned perturbation header exposes

```c
short has_source_delta_m;
int index_tp_delta_m;
```

and the source assembly stores

```c
_set_source_(ppt->index_tp_delta_m) = ppw->delta_m;
```

with the code commenting this quantity as the total matter overdensity in a gauge-invariant definition.

Before storage, the current-gauge matter density and velocity are combined into the gauge-invariant matter variable. In the GDM branch the pinned code performs

```c
ppw->delta_m += 3. * (1. + P_m/rho_m)
               * a * H * ppw->theta_m / k2;
```

where `P_m/rho_m` contains the pressure contribution of all matter species including GDM. For the frozen C3 training family, `w_gdm=0`, no massive neutrinos are used, and the matter sector is pressureless, so this reduces to

\[
D_m(k,z)=\delta_m^{\rm current\ gauge}(k,z)
+3\,aH\,\frac{\theta_m(k,z)}{k^2}.
\]

This is the exact source whose primordial-mode amplitude is squared to build native C3 `mPk`.

## 3. Existing read-only source interpolation API

The pinned perturbation module already exposes the public function

```c
int perturb_sources_at_tau(
  struct perturbs *ppt,
  int index_md,
  int index_ic,
  int index_tp,
  double tau,
  double *psource
);
```

It does not evolve perturbations. It only reads/interpolates the already precomputed source tables:

- early-time path: `ppt->sources[...]`;
- late-time path: spline interpolation of `ppt->late_sources[...]` and `ppt->ddlate_sources[...]`.

The same source interpolation tables are used by output quantities such as transfer functions and power spectra.

Therefore an accessor for `index_tp_delta_m` can be **strictly read-only**.

## 4. Existing Python-wrapper architecture

The current pinned `classy.pyx::get_transfer()` already calls C output-layer functions directly:

1. `perturb_output_titles(...)`;
2. `perturb_output_data(...)`;
3. convert the returned C array to NumPy/dictionary objects.

The wrapper declarations live in `python/cclassy.pxd`, which explicitly states that only C struct fields used by the Python wrapper are declared there.

Hence adding read-only declarations needed for a diagnostic source getter is consistent with the wrapper's existing architecture.

## 5. Frozen minimal patch boundary for the future C3 bridge

A prospective C3 bridge should use a small patch applied on top of the exact pinned commit. The patch is allowed to touch only:

- `python/cclassy.pxd`;
- `python/classy.pyx`.

It must **not** modify:

- `source/perturbations.c`;
- `source/nonlinear.c`;
- `source/primordial.c`;
- background/thermodynamics equations;
- GDM equations of motion;
- source construction;
- `mPk` construction;
- precision defaults, except explicit runtime parameters frozen by the experiment.

### `cclassy.pxd` additions

Expose by name only the already-existing read-only members/functions needed by Cython, including:

- `perturbs.index_tp_delta_m`;
- `perturbs.has_source_delta_m`;
- `perturbs.index_ic_ad`;
- existing scalar mode index/k-grid members as necessary;
- declaration of the already-public `perturb_sources_at_tau(...)` C function.

No C struct layout or C header is changed.

### `classy.pyx` diagnostic method

Add a dedicated method with semantics equivalent to

```text
get_delta_m_source(z)
```

that:

1. requires the perturbation/nonlinear modules to have been computed with `has_source_delta_m` true;
2. converts input redshift to conformal time using the existing background API;
3. calls `perturb_sources_at_tau` for:
   - scalar mode,
   - adiabatic IC,
   - `index_tp_delta_m`;
4. returns the native physical CLASS `k [1/Mpc]` array and signed `D_m(k,z)` source amplitude;
5. performs no assignment into any solver state and invokes no evolution routine.

A new standard `mTk` column should **not** be added: that would modify the ordinary transfer-output contract globally and is unnecessary.

## 6. Required prospective validation before accepting the patch as C3 bridge infrastructure

The future preregistered experiment must prove that the wrapper-only patch is observationally/read-only by hard controls.

### V1 — patch scope

The diff against the exact pinned upstream commit may modify only the two Python-wrapper files listed above. Any C/Fortran/source-equation modification is a hard FAIL for the read-only bridge claim.

### V2 — native output invariance

Run the same frozen C3 configuration once with pristine pinned upstream and once with the wrapper-only patch. Require byte/numerical equality, under a frozen tolerance, for all native quantities used by prior C3 gates, especially native `mPk` over the frozen cells.

The accessor is not allowed to alter native `mPk`.

### V3 — same-source reconstruction

For the single adiabatic C3 configuration, let the accessor return signed `D_m(k,z)`. Combine it only with the pinned primordial scalar spectrum to reconstruct the native matter power using the same single-IC normalization convention. Require agreement with native `mPk` under a preregistered tolerance.

This is the decisive proof that the accessor exposes the same source as native matter power.

### V4 — signed Weyl transfer

Use the already-exported pinned metric sources `phi` and `psi` from the same solver state to form

\[
W(k,z)=\frac{k^2}{2}[\phi(k,z)+\psi(k,z)].
\]

Then define the signed same-mode transfer ratio

\[
q_W(k,z)=\frac{W(k,z)}{D_m(k,z)}.
\]

No Poisson equation is used.

For single adiabatic IC, construct

\[
P_{mm}=P_m^{native},\qquad
P_{Wm}=q_W P_m^{native},\qquad
P_{WW}=q_W^2P_m^{native}.
\]

The sign of `P_Wm` must be retained.

### V5 — coherence identity

As a same-single-primordial-mode consistency control,

\[
\frac{P_{Wm}^2}{P_{WW}P_{mm}}=1
\]

must hold to numerical precision on valid nonzero cells. This is a transfer-product identity, **not** a GR Poisson closure.

### V6 — wrong-transfer negative control

Demonstrate that substituting ordinary `d_tot` (or another visibly different standard transfer column) for `D_m` does not satisfy the native-`mPk` reconstruction criterion over the chosen nontrivial GDM cells. This guards against accidental use of the wrong matter source.

## 7. Scientific status

This audit does **not** certify the C3 physical-power bridge. It only proves that a minimally invasive, wrapper-only prospective bridge is technically available and defines the validation controls needed to certify it.

Current G7 ordering remains:

1. Exp068B physical ACT forward bridge;
2. C5 physical power bridge (Exp069A);
3. prospective C3/GDM wrapper-only `D_m` bridge;
4. only then freeze/evaluate common survey-kernel physical validity mask;
5. restrict covariance and re-whiten retained subspace;
6. nuisance tangent Jacobian/SVD;
7. quotient/relation/null control;
8. fresh G8 withheld family.

**G7 OPEN, G8 OPEN, G9 OPEN.**
