# Exp070A — C3/GDM read-only gauge-invariant D_m physical-power bridge v0.1

**Date:** 2026-08-26  
**Status:** prospective contract frozen before the first Exp070A accessor patch execution or numerical output.

## 1. Purpose

Certify that the existing C3 GDM training family can provide a solver-native matter/Weyl physical-power triplet for the future solver-neutral ACT×unWISE linear/no-CLEFT projector without replacing the native gauge-invariant matter source by ordinary transfer-table `d_tot`, without a GR Poisson closure, and without modifying any GDM/background/perturbation/source equation.

The source-only prerequisite is `docs/C3_GDM_READONLY_DM_SOURCE_ACCESSOR_AUDIT_2026-08-26.md`.

This experiment is a provider bridge only. It does not project ACT observables, select the common physical support mask, whiten a retained covariance, measure nuisance rank, fit G7, or choose a G8 withheld family.

## 2. Immutable upstream solver and patch boundary

Pinned solver:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

The only allowed source-tree modifications are wrapper-only changes to:

- `python/cclassy.pxd`;
- `python/classy.pyx`.

The patch may expose existing read-only members/functions required to query the already computed `ppt->index_tp_delta_m` source through `perturb_sources_at_tau(...)`.

Hard forbidden modifications include all files under the physical C source/evolution path, in particular:

- `source/perturbations.c`;
- `source/nonlinear.c`;
- `source/primordial.c`;
- background/thermodynamics source;
- GDM equations;
- source construction;
- native `mPk` construction;
- precision defaults.

No new ordinary `mTk` column may be added.

## 3. Frozen C3 cosmology and precision

Reuse the validated C3 configuration and `p8` precision preset from Exp025.

Cosmology/model:

- `h = 0.67`;
- `T_cmb = 2.7255`;
- `omega_b = 0.0224`;
- `omega_cdm = 0`;
- `omega_gdm = 0.1200`;
- `Omega_Lambda = 0.684`;
- `N_ur = 3.046`;
- `N_ncdm = 0`;
- `Omega_k = 0`;
- `YHe = 0.2404`;
- `recombination = RECFAST`;
- `reio_parametrization = reio_none`;
- `type_gdm = time_only_bins`;
- `smooth_bins_gdm = yes`;
- `time_transition_width_gdm = 8`;
- `time_values_gdm = 1e-5,1e-4,1e-3,1e-2,1e-1`;
- all six `w_values_gdm = 0`;
- all six `cv2_values_gdm = 0`;
- `dynamic_shear_gdm = yes`;
- scalar mode only, `ic=ad`, synchronous gauge;
- analytic primordial spectrum with `A_s=2.10e-9`, `n_s=0.965`, `alpha_s=0`, `k_pivot=0.05 Mpc^-1`;
- no nonlinear correction.

Frozen p8 precision:

- `k_step_sub = 0.0010`;
- `k_step_super = 0.000003`;
- `k_step_super_reduction = 0.1`;
- `start_small_k_at_tau_c_over_tau_h = 1e-6`;
- `start_large_k_at_tau_h_over_tau_k = 0.05`;
- `tight_coupling_trigger_tau_c_over_tau_h = 0.005`;
- `tight_coupling_trigger_tau_c_over_tau_k = 0.008`;
- `start_sources_at_tau_c_over_tau_h = 0.006`;
- `tol_perturb_integration = 3e-10`;
- `perturb_sampling_stepsize = 0.00035`;
- radiation streaming approximation 2 with triggers `240` and `100` as in Exp025;
- ultra-relativistic fluid approximation 2 with trigger `50`.

## 4. Frozen validation models and grid

Use three pre-existing C3 points, selected before any Exp070A output:

- `cs2 = 0` exact GDM zero-sound-speed control;
- `cs2 = 1e-6` representative local-manifold point;
- `cs2 = 1e-5` stronger nonzero point with previously established large response above numerical floor.

For each model all six `cs2_values_gdm` entries equal that constant.

Frozen redshifts:

\[
z=\{0.295,0.51,0.706,0.934,1.317,1.491,2.33\}.
\]

Frozen DSIR comparison nodes are the existing

\[
k_h=\{0.001,0.003,0.01,0.03,0.1\}\ h/{\rm Mpc},
\]

converted to physical CLASS wavenumber by

\[
k=h\,k_h.
\]

Set `P_k_max_h/Mpc = 0.25` as in Exp025. The accessor may additionally return the native scalar source k grid; interpolation to the five frozen physical k nodes must be deterministic and performed in log-k with signed source amplitudes, never after squaring away a sign.

## 5. Read-only accessor semantics

Add a dedicated Python diagnostic method equivalent to

`get_delta_m_source(z)`

that:

1. requires `has_source_delta_m`;
2. converts `z` to conformal time using existing background routines;
3. queries scalar mode + adiabatic IC + `index_tp_delta_m` through the already public `perturb_sources_at_tau(...)`;
4. returns physical `k [1/Mpc]` and signed gauge-invariant `D_m(k,z)`;
5. performs no write to solver state and invokes no perturbation evolution routine.

The authoritative identity is the pinned native source chain

\[
\text{native }mPk\longleftarrow ppt\to index\_tp\_delta\_m
\longleftarrow D_m.
\]

For the frozen `w_gdm=0` matter sector,

\[
D_m=\delta_m^{\rm current\ gauge}+3aH\frac{\theta_m}{k^2}.
\]

## 6. Physical-power construction

The pinned nonlinear module constructs native matter power from the same `index_tp_delta_m` source and the scalar primordial spectrum. Exp070A must reproduce that source normalization directly from pinned source semantics, not fit a normalization factor to the native `mPk` output.

For the single adiabatic primordial mode, use the pinned analytic curvature spectrum

\[
\mathcal P_{\cal R}(k)=A_s\left(\frac{k}{k_{pivot}}\right)^{n_s-1}
\]

and the CLASS normalization documented/implemented in the pinned nonlinear module to reconstruct

\[
P_{mm}^{recon}(k,z)=\frac{2\pi^2}{k^3}\,\mathcal P_{\cal R}(k)\,D_m(k,z)^2.
\]

This formula must be verified against the pinned `source/nonlinear.c` source text before accepting V3; a source-contract mismatch is a hard FAIL rather than grounds to alter the formula after seeing outputs.

From the same solver state, use exported signed metric transfers `phi` and `psi` to form

\[
W(k,z)=\frac{k^2}{2}[\phi(k,z)+\psi(k,z)].
\]

Define

\[
q_W=W/D_m,
\]

then the production bridge triplet is

\[
P_{mm}=P_m^{native},\qquad
P_{Wm}=q_WP_m^{native},\qquad
P_{WW}=q_W^2P_m^{native}.
\]

This is a same-primordial-mode transfer identity. No Poisson relation is allowed. The sign of `P_Wm` must be retained.

## 7. Hard validation tests

### V1 — exact patch scope

Diff the patched tree against the pinned upstream SHA. Require that every changed path is one of exactly

- `python/cclassy.pxd`;
- `python/classy.pyx`.

Also inspect the patch text and require no assignment to physical perturbation/source arrays by the new accessor. Any source/evolution file modification is hard FAIL.

### V2 — native-output invariance

Build pristine pinned upstream and the patched tree separately. Run identical frozen models and p8 settings.

For each `cs2` and each frozen `(z,k_h)` cell compare native linear `mPk`. Require

\[
\max\frac{|P_m^{patch}-P_m^{pristine}|}{\max(|P_m^{pristine}|,10^{-300})}\le10^{-10}.
\]

No jitter, rescaling or post-hoc alignment is permitted.

### V3 — native-mPk reconstruction from exposed D_m

For every model and frozen cell compare `P_mm^recon` above with native patched-solver linear `mPk` at the same physical k and z. Require

\[
\max r_{recon}\le5\times10^{-4}.
\]

The normalization is fixed from source semantics and primordial parameters; no fitted multiplicative constant is allowed.

### V4 — signed Weyl construction

Require finite nonzero `D_m`, finite `phi`, `psi`, `W`, and finite `q_W` on every frozen cell. Require finite positive `P_mm` and `P_WW`, finite nonzero signed `P_Wm`.

Record the sign pattern of `P_Wm`; do not replace it by an absolute value.

### V5 — same-mode coherence identity

Require positive denominator and

\[
\left|\frac{P_{Wm}^2}{P_{WW}P_{mm}}-1\right|\le2\times10^{-10}
\]

at every valid frozen cell. Because the three blocks are explicitly constructed from one `q_W` and one native `P_m`, this is primarily an implementation/serialization guard and must be near machine precision.

### V6 — wrong-d_tot negative control

From the ordinary standard transfer output at the same model/redshift, obtain `d_tot` and construct the deliberately wrong reconstruction by substituting `d_tot` for `D_m` in the same primordial normalization.

Require both:

1. the correct accessor reconstruction passes V3;
2. for at least one frozen cell in each nonzero model (`cs2=1e-6` and `1e-5`), the wrong-`d_tot` relative error against native `mPk` exceeds

\[
10^{-3}.
\]

Also record the full wrong-control error field. Failure of `d_tot` to separate at this preregistered threshold is a V6 FAIL; do not lower the threshold after output.

### V7 — deterministic accessor repeatability

Within one patched solver state, query every redshift twice. Require bitwise equality of returned physical k arrays and `D_m` arrays between repeated read-only calls.

### V8 — no state mutation after accessor calls

For each model, evaluate native `mPk` before any accessor query and again after all accessor queries. Require relative change at every frozen cell

\[
\le10^{-12}.
\]

This directly guards the read-only claim.

## 8. PASS/FAIL

PASS iff V1-V8 all pass:

`PASS_C3_GDM_READONLY_DM_PHYSICAL_POWER_BRIDGE_V0_1`.

Otherwise:

`FAIL_C3_GDM_READONLY_DM_PHYSICAL_POWER_BRIDGE_V0_1`.

A scientific FAIL must be preserved. Infrastructure/build failures before evaluable numerical output may be corrected only without altering this frozen contract.

## 9. Anti-retuning

After the first Exp070A numerical output, do not change:

- pinned GDM_CLASS commit;
- wrapper-only patch scope;
- C3 cosmology;
- p8 precision;
- selected `cs2` points;
- redshift/k grid;
- primordial normalization formula;
- Weyl definition;
- V2/V3/V5/V6/V8 thresholds;
- PASS/FAIL logic.

If a source audit proves the frozen primordial normalization formula itself does not match pinned source semantics **before the first Exp070A numerical output**, amend the preregistration in a new commit documenting the source proof. After numerical output, any such change requires a separately numbered corrective experiment.

## 10. Gate semantics

A PASS certifies C3 only as a physical input provider. It does not certify a common ACT physical-validity support, does not close G7 and does not authorize G8 selection.

Only after C5 and C3 physical bridges pass may the common survey-kernel/bandwindow support-leakage mask be preregistered and evaluated, followed by covariance restriction/re-whitening and nuisance SVD.

Entering state: **G7 OPEN, G8 OPEN, G9 OPEN**.
