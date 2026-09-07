# DSIR-4 C2 interacting-dark-sector residual mapping v0.1

Frozen: 2026-09-07 under `DSIR4_COMMON_RESIDUAL_CONVENTION_V0_1` and `DSIR4_MODEL_MAPPING_ARTIFACT_CONTRACT_V0_1`.

Status: **MAPPING_READY / PREDICTION_NOT_YET_FROZEN**. This artifact closes the six-component source mapping for the pinned C2 implementation. It does not create a DSIR scientific PASS.

Frozen hypothesis: `C2_IDE_LOCAL_TANGENT_CONE`.

Pinned implementation: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

## 1. Common residual partition

The DSIR residual convention is

\[
X_{\mu\nu}=M_0^2G_{\mu\nu}-T^{\rm known}_{\mu\nu}.
\]

For C2 the interacting dark pair is entirely in the residual sector,

\[
X^{\rm C2}_{\mu\nu}=T^{\rm idm}_{\mu\nu}+T^{\rm iv}_{\mu\nu},
\]

while baryons, photons and the frozen standard-neutrino sector remain in `T_known`.

The source implementation defines

\[
Q=H\left(\alpha\rho_{\rm idm}+\beta\rho_{\rm iv}\right).
\]

The pinned background source is consistent with the conformal-time sign convention

\[
\rho'_{\rm idm}=-3aH\rho_{\rm idm}-aQ,\qquad
\rho'_{\rm iv}=aQ,
\]

so the internal transfer cancels in the total dark residual conservation law.

Source anchors at the pinned commit:

- `source/background.c`: `Q_idm_iv = alpha_idm_iv*H*rho_idm_iv + beta_idm_iv*H*rho_iv`;
- the same source-level `Q_prime_idm_iv` expression contains the factors corresponding to `rho'_idm=-3aH rho_idm-aQ` and `rho'_iv=aQ`;
- `test_idm_iv_lcdm.ini`: `f_idm_iv=1`, `f_iv=1`, `gauge=synchronous`.

## 2. Background residual components

The pinned `background.c` implementation adds interacting dark matter as pressureless matter and interacting vacuum with negative pressure:

\[
\rho_X=\rho_{\rm idm}+\rho_{\rm iv},
\]

\[
p_X=-\rho_{\rm iv}.
\]

This follows directly from the source bookkeeping:

- `rho_tot += rho_idm_iv`, `p_tot += 0`;
- `rho_tot += rho_iv`, `p_tot -= rho_iv`.

Therefore the background entries are **DERIVED** and source-bound.

## 3. Scalar perturbation gauge/basis

The pinned IDM-IV perturbation implementation is explicitly synchronous-gauge bound. In `source/perturbations.c`:

- the Newtonian branch stops with `IDM IV implementation not supporting newtonian gauge (yet)`;
- in synchronous gauge only `delta_idm_iv` is an evolved IDM-IV perturbation degree of freedom;
- `theta_idm_iv` is not allocated as a synchronous-gauge dynamical variable and is set to zero in the source bookkeeping;
- the synchronous density equation is

\[
\delta'_{\rm idm}=-\mathrm{metric\_continuity}
+\delta_{\rm idm}\,aQ/\rho_{\rm idm}.
\]

This mapping therefore records the six residual components in the **pinned IDM-comoving synchronous gauge/basis**. These intermediate quantities must not be compared directly against raw variables from another solver/gauge.

## 4. Six-component residual decomposition

### 4.1 Scalar density perturbation

The total perturbed stress-energy assembly adds

\[
\delta\rho_X^{(\rm sync)}=\rho_{\rm idm}\,\delta_{\rm idm}.
\]

At the pinned commit there is no independent `delta_iv` perturbation variable and `rho_iv` is never added to the perturbative `delta_rho` accumulator. Thus

\[
\delta\rho_{\rm iv}^{(\rm sync)}=0
\]

is a **STRUCTURAL_ZERO of this pinned interacting-vacuum realization/gauge**, not a statement about arbitrary IDE models.

### 4.2 Scalar momentum / velocity potential

For the frozen common residual convention, `q_X` is the scalar momentum potential associated with the scalar part of `T^0_i`, with the exact velocity convention bound here to the CLASS `rho_plus_p_theta` bookkeeping.

In the pinned synchronous IDM-IV implementation:

- `theta_idm_iv=0` by the implemented comoving synchronous gauge choice;
- the interacting-vacuum component has `rho_iv+p_iv=0` and no independent velocity degree of freedom;
- the IDM-IV contribution to `rho_plus_p_theta` is added only outside synchronous gauge, while the Newtonian IDM-IV branch is unsupported.

Therefore

\[
q_X^{(\rm sync)}=0
\]

is a **GAUGE-BOUND STRUCTURAL_ZERO** for this mapping. It must not be reinterpreted as absence of an observable structure response.

### 4.3 Scalar isotropic pressure perturbation

Pressureless IDM contributes no pressure perturbation. The pinned interacting vacuum has no independent density perturbation in the implemented synchronous realization, and the IDM-IV stress-energy block never adds a contribution to the global `delta_p` accumulator. Hence

\[
\delta p_X^{(\rm sync)}=0.
\]

This is a **STRUCTURAL_ZERO for the pinned C2 realization**.

### 4.4 Scalar anisotropic stress

The IDM-IV stress-energy block never adds a contribution to the global `rho_plus_p_shear` accumulator. Pressureless IDM and the vacuum component carry no intrinsic scalar shear degree of freedom in this implementation. Hence

\[
\pi_X^{(\rm sync)}=0.
\]

This is a **STRUCTURAL_ZERO for the pinned C2 realization**.

### 4.5 Final six-component table

| Required DSIR component | C2 pinned mapping | Status |
|---|---|---|
| `rho_X` | `rho_idm + rho_iv` | DERIVED |
| `p_X` | `-rho_iv` | DERIVED |
| `delta_rho_X` | `rho_idm * delta_idm` in pinned synchronous gauge | DERIVED |
| `q_X` | `0` in pinned IDM-comoving synchronous gauge | GAUGE_BOUND_STRUCTURAL_ZERO |
| `delta_p_X` | `0` | STRUCTURAL_ZERO |
| `pi_X` | `0` | STRUCTURAL_ZERO |

No required component remains `NOT_YET_MAPPED` in this C2 mapping artifact.

## 5. Observable-response bridge

The structural zeros above do **not** imply a zero C2 observational response. The interaction modifies the time evolution of `rho_idm`, `rho_iv`, `delta_idm` and the metric, producing nontrivial growth/geometry responses.

The repository's frozen production perturbation basis is the same-solver comoving total-matter response

\[
\Delta_m=\delta_m+3(1+w_m)\mathcal H\theta_m/k^2,
\]

and

\[
r_\Delta(k,z)=\ln\left[P^S_{\Delta,\,\rm model}(k,z)/P^S_{\Delta,\,\rm ref}(k,z)\right],
\]

with model/reference evaluated in the same solver lineage and matched numerical settings. The pinned source also applies a gauge correction when exporting `delta_idm_iv` transfer data, reinforcing that raw synchronous `delta_idm_iv` is not itself the cross-model DSIR comparison coordinate.

The future C2 prediction artifact must therefore bind the exact same-solver extraction path used to construct the authoritative common response; no raw-gauge proxy may be substituted.

## 6. Certified domain and branch mask

The common DSIR-4 v0.1 model-comparison domain is

- `0.295 <= z <= 2.33`;
- `0 < k <= 0.06664762008318016 Mpc^-1`.

The C2 physical branch additionally requires throughout the required history

\[
\rho_{\rm idm}>0,\qquad \rho_{\rm iv}\ge 0.
\]

The frozen C2 local geometry is a tangent cone: positive-`alpha` perturbations that violate full-history `rho_iv>=0` are `OUTSIDE_DOMAIN`; the admitted local alpha direction is left-sided, while the beta tangent is two-sided where the branch mask remains satisfied. No invalid positive-alpha point may be extrapolated through or counted as an observational FAIL.

This artifact does not enlarge the legacy C2 parameter domain and does not select a new parameter point after seeing any observational gate.

## 7. Source-audit closure and remaining provenance

The source audit is now sufficient to set

- `mapping_ready = true` for `C2_IDE_LOCAL_TANGENT_CONE`;
- six-component decomposition complete;
- exact gauge/implementation lineage pinned.

Still required before `G_DOMAIN_MAPPING` can be scientifically evaluated:

- a frozen versioned C2 prediction payload over the mandatory DSIR grid/domain;
- exact alpha/beta finite tangent definitions inherited from the frozen legacy hypothesis;
- matched numerical settings and solver invocation;
- deterministic prediction payload hash;
- mapping artifact SHA-256 bound into the prediction artifact;
- branch-mask validation over the complete required history for every emitted prediction point.

Therefore current status remains

- `mapping_ready = true`;
- `prediction_ready = false`;
- `numerically_evaluated = false` for the dedicated DSIR-4 C2 prediction artifact;
- `G_DOMAIN_MAPPING = NOT_YET_TESTABLE`.

This is progress in mapping authority, not evidence for or against IDE.

## 8. Non-generalization warning

The structural perturbation zeros in this artifact belong to the **specific pinned geodesic/comoving interacting-vacuum implementation represented by `kaeonikc/class_iv@ac627d54...` and the frozen C2 hypothesis**. They must not be generalized to all interacting-dark-energy theories, alternate momentum-transfer frames, clustered vacuum prescriptions, or other IDE parameterizations. Such realizations are distinct hypotheses and require separate mapping artifacts.
