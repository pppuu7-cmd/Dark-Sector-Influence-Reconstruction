# DSIR research gates

| Gate | Requirement | Status |
|---|---|---|
| G0 | LambdaCDM embedding reproduces reference observables | PARTIAL — multiple solver-specific LambdaCDM/control limits pass; a broader solver-independent reference suite remains desirable |
| G1 | Bianchi/conservation and gauge-invariant bookkeeping verified | **PASS for v0.1.1 scope** — covariant conservation contract frozen; comoving total-matter source audited; Newtonian/synchronous hard gauge regression passes at `5e-6`; cross-solver response bridge passes at `1e-9` |
| G2 | Response basis and conventions frozen | **PASS v0.1.1** — production perturbation coordinate is same-solver comoving total-matter response `r_Delta`; Experiments 018/020 |
| G3A | Six control classes embedded at background/AP level | **PASS v0.1 scope** — representatives, exact intersections and background equivalence maps documented |
| G3B | Six control classes embedded beyond background and comparison-ready | **PASS v0.1 block-aware scope** — C0 reference; C1 smooth-w local ray; C2 IDE positivity-masked tangent cone; C3 GDM `cs2/cv2` local rays; C4 WDM small-scale transfer block; C5 full H-EFTCAMB designer-f(R) production manifold. Experiment 030 hard readiness PASS |
| G4 | Synthetic low-rank recovery test passes | PASS — corrected global noise-edge criterion recovers injected rank 3 |
| G5 | Rank robust to noise null, feature scaling, covariance coordinates, missing channels, and model sampling | PARTIAL — whitening robustness passes; catalog-prior failure mode controlled via `R_model(pi)`; validity masks/common-subspace and family-balanced sampling implemented; data-whitened cross-family rank stress tests remain |
| G6A | First real-data response reconstruction | PASS — DESI DR2 AP calibration quotient and relative expansion reconstruction |
| G6B | First real multi-channel response reconstruction | PASS — corrected DESI DR1 ShapeFit geometry/growth/shape covariance; Experiment 009 |
| G7 | First nontrivial residual cross-channel relation after quotienting known identities/measurement degeneracies | **OPEN, raw-theory comparison now unblocked** — Experiment 031 completed first model comparison; next prerequisite is observational kernel/covariance whitening before any law claim |
| G8 | Relation survives withheld prediction | OPEN |
| G9 | Candidate underlying dynamics/action reconstructed or ruled out | OPEN |

## G1 conservation and gauge contract

For internal interactions,

`nabla_mu T_i^{mu nu}=Q_i^nu`, `sum_i Q_i^nu=0`, hence `nabla_mu T_tot^{mu nu}=0`.

Exact Bianchi/conservation identities are quotient directions, not candidate discoveries. At first order, gauge changes act at tensor level as `delta T -> delta T - L_xi Tbar`; raw gauge-specific `delta`, `theta` and metric variables are not common DSIR coordinates without an invariant mapping.

Production matter variable:

`Delta_m = delta_m + 3 (1+w_m) Hconf theta_m/k^2`, with `w_m=p_m/rho_m` and `Hconf=aH`.

Pinned GDM_CLASS and class_iv source audits confirm the same total-matter concept. GDM_CLASS retains the `(1+p_m/rho_m)` factor when GDM has pressure.

### Gauge hard regression

Identical CDM cosmology was run in Newtonian and synchronous gauges in pinned GDM_CLASS. At p8 precision explicit comoving `Delta_m` reconstruction gave a maximum mismatch `2.5514e-6`. A threshold `5e-6` was frozen before the final hard rerun and passed.

## G2 response basis v0.1.1

Background:

`r_E(z;z*) = ln[(H(z)/H(z*))/(H_ref(z)/H_ref(z*))]`, `z*=0.51`.

Perturbation:

`r_Delta(k,z) = ln[P_Delta_model^S(k,z)/P_Delta_ref^S(k,z)]`,

where model/reference use the same solver lineage `S` and matched numerical settings whenever possible.

Frozen low-k nodes:

- `z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`;
- `k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

Cross-solver smooth-w bridge hard threshold `1e-9` passed; calibration mismatch at matched p8 was `2.3747404043e-10`.

## G3B numerical sub-gates and manifold patches

- **C0 LambdaCDM:** reference origin, with multiple solver-specific zero limits.
- **C1 smooth non-phantom DE:** one-sided `epsilon_w=1+w -> 0+` local ray at p8. Smallest-step `epsilon_w=1e-4`; finite-difference change at `1e-3` is `0.12%` L2 and `0.014 deg`.
- **C2 IDE:** pinned `kaeonikc/class_iv@ac627d54...`; zero limit and hard regression pass. Physical local geometry is a **tangent cone**: `alpha>0` violates full-history `rho_iv>=0`; use left-sided alpha ray and two-sided beta tangent. Structure angle alpha/beta = `58.9338 deg`; background-H angle = `10.8306 deg`.
- **C3 GDM:** pinned `s-ilic/gdm_class_public@4c87916...`; zero limit and hard regression pass. Local `cs2` and `cv2` rays are nearly collinear in low-k `P_Delta`: angle `0.322616 deg`, two-axis `sigma2/sigma1=2.572e-3`.
- **C4 WDM:** low-k is intentionally treated as an identifiability blind block. For 3 keV, `r_T(0.1)=-3.46e-6`, while `r_T(10)=-0.10375`; small-scale transfer is a separate valid block.
- **C5 designer f(R):** official H-EFTCAMB `EFTCAMB/EFTCAMB@16d9c4e9...`. MG-S0 exact-GR hard gate PASS. MG-S1 common-baseline multi-z hard gate PASS; production points `B0={1e-6,1e-5,1e-4,1e-3}`, while `1e-7` remains transition control near the solver GR threshold.

Undefined theory/channel cells remain masked, never zero-imputed. Tangent/Jacobian rank and global linear-span rank are reported separately because a curved one-parameter manifold can generate several linear SVD modes.

## Comparison-readiness hard gate — Experiment 030

Run `32772758188` returned `PASS_READY_FOR_BLOCK_AWARE_MODEL_COMPARISON`, `failures=[]`.

Frozen positive controls reproduced:

- GDM `cs2/cv2` low-k angle `0.322616 deg <= 1 deg`;
- IDE alpha/beta structure angle `58.9338 deg >= 30 deg`;
- WDM 3 keV low-k/high-k blindness-break conditions pass.

The normalized six-direction raw-theory singular ratios were `(1,0.52046,0.26140,0.20087,0.08299,5.92e-4)`. **No intrinsic-rank threshold was frozen; this must not be called `R_model=5`.**

## First comparison and hard conditional discriminants — Experiments 031/032

Experiment 031 hard rerun `32774501126` PASS:

- GDM cs2 vs cv2 full low-k angle `0.3226 deg`;
- GDM cs2 vs f(R) leading scale-mode angle `0.07813 deg`, time-mode unoriented angle `25.18 deg`, full oriented ray angle `154.82 deg`;
- GDM cv2 vs f(R) leading scale-mode angle `0.10169 deg`, time-mode angle `25.49 deg`, full oriented angle `154.51 deg`.

Thus scale-only GDM/f(R) similarity is broken by time evolution / physical response sign.

Experiment 032 slip hard rerun `32774501069` PASS:

- GDM cs2/cv2 Weyl-amplitude angle `0.3007 deg` at `1e-7`;
- metric-slip angle `137.9432 deg`;
- equalized Weyl+slip angle `56.9632 deg`.

Thus the GDM `cs2/cv2` matter-power degeneracy has a reproducible metric-slip separator in the frozen theory setup.

## Hard scientific rule

No discovery claim is permitted before G8 withheld prediction. A raw theory-space separator is not observational distinguishability until survey response kernels and covariance whitening are applied.

<!-- DSIR_EXP049B_DOC_SYNC_2026_08_26 -->
## Gate update — 2026-08-26 Exp049B

### Physical-window mechanism bridge

**State: SUPPORTED/PARTIAL; not a new top-level PASS gate.**

Exp049B is a genuine pre-frozen interpolation prediction inside C3. After the source-derived dynamic-viscosity proxy enters `k<=0.1 h/Mpc`, all five newly computed intermediate amplitudes satisfy the frozen directional prediction that `k_I_geo` is non-increasing with `cv2`.

This upgrades the C3 **window-crossing mechanism explanation** from retrospective support to independent within-family support.

It does **not** close G7 because:
- the proxy is quasi-steady rather than a validated exact eigenmode scale;
- only C3 has the withheld validation so far;
- designer-f(R) exact `B(a)` bridge is still being tested;
- no common functional law across families has been frozen and validated.

It does **not** close G8 because the withheld points belong to a known C3 ray, not a withheld model family/mechanism.

Therefore top-level state remains: **G7 OPEN, G8 OPEN**.

<!-- EXP049A_F22_SYNC_2026-08-26 -->
## Exp049A/F22 gate note — physical transition-scale hypothesis

- **Source/algebra gate:** 🟢 PASS for frozen C3/C5 implementations (Exp049A run `32904376001`).
- **GDM independent prediction gate:** 🟢 PASS via Exp049B/F21.
- **designer-f(R) independent prediction gate:** 🟡 OPEN; Exp049C required.
- **Cross-family universalization:** 🔴 NOT ELIGIBLE. One withheld family is insufficient; C4 and observation-space/domain robustness remain missing.
- **G7:** OPEN.
- **G8:** OPEN.

<!-- DSIR_EXP050A_DOC_SYNC_2026_08_26 -->
## Gate update — 2026-08-26 Exp049C / Exp050A

### Two-mechanism withheld window-crossing support

**State: HARD for the two frozen withheld tests; broader G7 interpretation remains SUPPORTED/PARTIAL.**

Exp049B/F21 (GDM dynamic shear) and Exp049C/F23 (designer-f(R)) independently froze the same directional statement before their new intermediate outputs: after the relevant source-derived transition lies inside the finite response window, moving that transition toward smaller k with increasing microscopic parameter is accompanied by non-increasing `k_I^geo`. Both tests passed with every measured step negative.

This is stronger than retrospective correlation, but G7 remains OPEN because no model-independent functional relation has been frozen across a sufficiently broad set of mechanisms/operators and quotient identities.

G8 remains OPEN because these are withheld interpolation points within mechanisms already represented in the atlas, not a truly withheld model family/mechanism used for discovery validation.

### C4 time-domain completion

Exp050A hard run `32908751625` fills the previous C4 high-k time-dependent response gap with pinned CLASS for thermal WDM masses 2, 3 and 5 keV on six high-k nodes and seven redshifts. Operator/provenance controls pass.

This strengthens **G3B block-aware comparison readiness**: C4 is no longer represented only by a static transfer proxy. However, C4 remains a distinct high-k block; it is not valid to zero-pad it into the low-k C1/C2/C3/C5 matrix.

The new C4 response is nearly time-separable (`chi_I ~ 2e-10`) on the frozen linear domain, which is a scientific feature, not a new gate closure.

Top-level state remains: **G7 OPEN, G8 OPEN, G9 OPEN**.

<!-- DSIR_EXP050B_DOC_SYNC_2026_08_26 -->
## Gate update — 2026-08-26 Exp050B / F25

### C4 withheld interpolation

**State: HARD PASS within the frozen thermal-WDM family.**

Exp050B froze new masses `2.5,3.5,4.0,4.5 keV` and the directional cutoff-scale criterion before generating their CLASS outputs. The solver-defined first `ln(P_WDM/P_CDM)=-0.1` crossing increases with mass at all seven frozen redshifts; clean run `32911928403` passed.

This strengthens the C4 mechanism atlas and shows that the free-streaming response has a stable scale coordinate. It does **not** close G8 because the held-out points are interpolation inside an already represented family.

### G7 boundary after F21/F23/F25

There are now preregistered directional successes in three response directions/mechanisms:

- C3 GDM viscosity: interaction-localization scale moves with the source-derived viscous transition;
- C5 designer-f(R): interaction-localization scale moves with the exact inverse-Compton transition;
- C4 thermal WDM: solver cutoff `k_0.1` moves monotonically with relic mass.

However the observable coordinates and microscopic control variables are not yet unified by one frozen model-independent equation. Therefore **G7 remains OPEN**. A common qualitative phrase such as “characteristic scales move through the response window” is not yet a residual law.

### Exp051A mask

The block-aware observability atlas v0.2 is now the required input for future rank/coverage claims. Unknown, solver-limited and near-null cells cannot be filled with zeros. Any future `N_repr` or `N_disc` gate must state which fully observed submatrix or masked bound it uses.

Top-level state: **G7 OPEN, G8 OPEN, G9 OPEN**.
