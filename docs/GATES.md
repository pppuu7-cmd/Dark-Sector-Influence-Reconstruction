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

