# DSIR RECOVERY MANUAL — chat-independent research backup

**Project:** Dark-Sector Influence Reconstruction (DSIR)  
**Repository:** `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`  
**Manual snapshot:** 2026-08-25 after Exp046  
**Live overlay:** `docs/RECOVERY_LATEST.md`  
**Influence atlas:** `docs/BUYANOVGPT_TABLE.md`  
**Scientific interpretation register:** `docs/SCIENTIFIC_FINDINGS_REGISTER.md`  
**Preserved previous full manual:** `docs/RECOVERY_MANUAL_PRE_EXP044_2026-08-25.md`

The preserved pre-Exp044 manual contains older detailed derivations and infrastructure chronology. This file is the current stable methodology/recovery manual and must be updated whenever mathematics, hard provenance, interpretation, gate state or the exact continuation sequence changes.

After any chat/session loss read, in order:

1. `docs/RECOVERY_MANUAL.md`;
2. `docs/RECOVERY_LATEST.md`;
3. `docs/SCIENTIFIC_FINDINGS_REGISTER.md`;
4. `docs/BUYANOVGPT_TABLE.md`;
5. `docs/GATES.md` and `docs/STATUS.md`;
6. latest dated research log;
7. newest numbered experiment protocol and frozen result JSON;
8. `docs/RECOVERY_MANUAL_PRE_EXP044_2026-08-25.md` when older derivation detail is needed.

---

## 0. Hard project boundary and claim discipline

DSIR is independent of RTK. **Never edit, import, overwrite, merge or silently use RTK as a prior.**

DSIR is a reconstruction/meta-inference framework, not a fundamental theory. Preserve these rules:

- missing response is never zero;
- a validated zero is evidence, not missing data;
- raw SVD rank is not microscopic dimension;
- an observational degeneracy is not a physical identity;
- theory-space angles are not survey distinguishability;
- a compressed-data correlation is not causality;
- a known identity is not a discovery;
- a theory-level temporal response is not automatically tracer RSD;
- negative results, failed approximations, numerical limitations and infrastructure history are retained;
- no residual-law claim before G7;
- no discovery claim before G8 withheld prediction.

Primary strategy: **compare physically different models, locate exact nulls, approximate degeneracies, channel reversals, scale/time/sign structures, domain localization and cross-family regularities.** Minimal latent dimension is parallel work; never force it to 3, 4 or another chosen value. A universal model is postponed until `docs/UNIVERSAL_MODEL_READINESS.md` is satisfied.

---

## 1. Scientific question and inverse architecture

Central question:

> What is the minimal observable influence structure required to reproduce empirically allowed dark-sector effects, and which relations survive model labels, gauge conventions, observational compression, covariance whitening and theory-family priors?

Direction of inference:

`data -> observable response operators -> response geometry/manifolds -> cross-channel relations -> candidate effective dynamics -> candidate fundamental theory`.

Keep three layers distinct:

- **data/measurement:** likelihoods, covariances, windows, nuisance and selection effects;
- **response/influence:** expansion/AP, density/growth/velocity, metric potentials/slip/lensing, small-scale transfer, tensor channels;
- **theory:** LambdaCDM, smooth DE, IDE, GDM, WDM, modified gravity, EFT/PPF, etc.

Law search belongs mainly to the response layer after quotienting known identities and measurement/compression degeneracies.

---

## 2. Common residual source bookkeeping

Use

\[
\boxed{X_{\mu\nu}=M_0^2G_{\mu\nu}-T^{known}_{\mu\nu}}.
\]

For homogeneous FLRW,

\[
\rho_X=3M_0^2(H^2+K/a^2)-\rho_{known},
\]

\[
p_X=-M_0^2(2\dot H+3H^2+K/a^2)-p_{known}.
\]

`X_{mu nu}` is bookkeeping, not a unique observable; it depends on the split defining `T_known` and normalization/frame choices. At perturbation level map solver output into gauge/frame-safe response quantities before model comparison.

---

## 3. Frozen conservation/gauge and matter-response contract — G1/G2

Production total matter:

\[
\delta_m=\frac{\sum_i\rho_i\delta_i}{\rho_m},
\]

\[
\theta_m=\frac{\sum_i(\rho_i+p_i)\theta_i}{\rho_m+p_m},
\]

\[
\boxed{\Delta_m=\delta_m+3(1+w_m){\cal H}\frac{\theta_m}{k^2}}.
\]

Frozen structure grid:

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`,

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

Anchored background response:

\[
\boxed{r_E(z;z_*)=\ln\left[\frac{H(z)/H(z_*)}{H_{ref}(z)/H_{ref}(z_*)}\right]},\qquad z_*=0.51.
\]

Production structure response:

\[
\boxed{r_\Delta(k,z)=\ln\frac{P^S_{\Delta,model}(k,z)}{P^S_{\Delta,ref}(k,z)}}.
\]

`S` denotes matched solver lineage/setup whenever possible. Cross-solver comparison requires an explicit bridge.

**RSD caveat:** gauge-safe total-matter density does not automatically identify the tracer velocity entering galaxy RSD.

---

## 4. Frozen six-family atlas and provenance

- **C0:** LambdaCDM/GR origin.
- **C1:** smooth non-phantom DE, one-sided `epsilon_w=1+w -> 0+`, production step `1e-4`.
- **C2:** interacting vacuum `Q=H(alpha rho_idm + beta rho_iv)`; positive alpha excluded by frozen positivity history; physical coordinate `u=-alpha>=0` plus beta line.
- **C3:** GDM `cs2/cv2` closure directions, `w_gdm=0`.
- **C4:** thermal WDM, separate informative high-k transfer block.
- **C5:** designer f(R), H-EFTCAMB `DesignerEFTmodel=1`, `EFTwDE=0`, production `B0={1e-6,1e-5,1e-4,1e-3}`, controls `0,1e-7`.

Pinned upstream:

- C1/C3: `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`;
- C2: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- C5: `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

C5 hard config artifact: run `32759477319`, artifact `9532245261`, SHA256 `9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`, lineage `dsir_mgs1_hp_*`.

---

## 5. AP operator and exact geometry-null results

For flat FLRW,

\[
D_H=\frac{c}{H_0E(z)},\qquad D_M=\frac{c}{H_0}\int_0^z\frac{dz'}{E(z')},
\]

therefore

\[
\boxed{F_{AP}(z)=\frac{D_M}{D_H}=E(z)\int_0^z\frac{dz'}{E(z')}}.
\]

A multiplicative normalization of `E` cancels exactly. Corrected ShapeFit geometry uses `D_H/D_M`:

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}.
\]

AP requires full background history from `z=0`; never extrapolate the seven-node structure atlas below `z=0.295`.

Hard examples:

- Exp035 AP bridge error `~1e-14`.
- Exp036 IDE alpha/beta AP acute `9.0379 deg` versus full structure `58.9338 deg`.
- Exp037 frozen GDM closure directions:
  \[
  K_{AP}t_{cs2}=K_{AP}t_{cv2}=0.
  \]
- Exp038 frozen designer-f(R) B0:
  \[
  K_{AP}t_{B0}=0.
  \]

Final C5 transfer-preserving regression: run `32786915513`, artifact `9541895055`, SHA256 `74d975790d00a04762d45bf183481f69d6fc54b84d186c63e89b88bbb9d20b16`.

**Hard cross-family lesson:** `K_geometry t=0` does not imply `t≈0`; physics can be exactly invisible in background/AP and still perturbation-active.

---

## 6. ShapeFit shape and density/velocity contracts

Corrected DR1 ShapeFit order:

`[D_V/r_d, D_H/D_M, f_sigma_s8, m+n]`.

Finite-node shape proxy:

\[
\ln(P'/P_{ref})=A+\frac{m}{0.6}\tanh[0.6\ln(k/0.03)]+n\ln(k/0.03).
\]

It leaves about `36%` representation residual for GDM/f(R), so proxy angles are not DESI distinguishability.

Correct growth convention:

\[
s=\frac{r_d}{r_d^{ref}},\qquad \sigma_{s8}=\sigma(R=s\,8h^{-1}{\rm Mpc}).
\]

For density/velocity moments:

\[
\boxed{{\cal D}_{RSD}=1-\frac{S_{\delta\Theta}^2}{S_{\delta\delta}S_{\Theta\Theta}}}.
\]

Exp041 establishes

\[
\boxed{{\cal D}_{RSD}=\frac{\mathrm{Var}_w[g]}{\langle g^2\rangle_w}},\qquad g=\Theta/\delta,
\]

and

\[
CV_w(g)=\sqrt{\frac{{\cal D}_{RSD}}{1-{\cal D}_{RSD}}}.
\]

C5 hard run `32791510072`, artifact `9543375564`, SHA256 `1e4d86f7f13185d69a07b71afa9bfd6fefa6003119064652d6388491738212bc`.

At `kmax=0.24 h/Mpc`, GR floor is `~1.42e-10`; production B0 gives `D_RSD=5.18e-6,1.92e-4,8.81e-4,8.78e-4` for `1e-6,1e-5,1e-4,1e-3`. Hence scalar growth compression is not exact for frozen designer f(R).

Old printed H-EFTCAMB `sigma8` summaries have only about four decimals and are rejected for small-B0 tangent work.

---

## 7. Temporal response and degeneracy migration — Exp040

For adjacent frozen early->late nodes,

\[
\boxed{\Delta\bar f_P(k)=\frac{r_\Delta(k,z_{late})-r_\Delta(k,z_{early})}{2[\ln a_{late}-\ln a_{early}]}}.
\]

This is theory-space temporal response, not tracer RSD.

Hard comparisons:

- IDE alpha/beta: AP `9.04 deg` -> temporal `29.40 deg` -> structure `58.93 deg`.
- smooth-w/IDE-alpha: AP `72.80 deg`, temporal `10.31 deg`, structure `52.19 deg`.
- IDE-alpha/GDM: structure `~25 deg` -> temporal `~61 deg`.
- GDM cs2/cv2: structure `0.3226 deg` -> temporal `1.3340 deg`; slip remains necessary.
- GDM/f(R): scale-only `0.078-0.102 deg` -> temporal `16-17 deg` -> full `(k,z)` `25.18-25.49 deg`.

**Hard interpretation:** degeneracies migrate between response operators. Adding one channel can separate one pair and collapse another.

---

## 8. GDM velocity/gauge negative chronology — Exp042/043

Preserve the sequence:

1. synchronous GDM velocity is gauge-ill-conditioned for RSD;
2. pinned N-body transfer route stops upstream because the derivative of `H_T_Nb_prime` is not propagated;
3. Exp042 parser initially mishandled a 16-vs-15-column gauge layout; parser-only fix did not alter thresholds;
4. actual synchronous/Newtonian comoving-density bridge failed: `2.58664e-6 > 1e-6`, while response bridge was `6.78698e-7`;
5. Exp043 independently interpolated each gauge to frozen nodes and tightened numerical precision only.

Exp043 p8 absolute bridge `2.51958e-6`; p10 `3.00625e-6`; ratio `1.19316`. Response bridge remains below `1e-6` but absolute bridge fails.

Run `32794067542`, artifact `9544255453`, SHA256 `c62613798a6a6f8e9e573bb158315ca03a5c9f998805ebfc6bdda25de4d4100a`.

**Negative result:** tighter precision does not cure the mismatch. Do not loosen the gate or use Exp042 velocity/RSD values as validated science.

---

## 9. BuyanovGPT atlas, no-hair analogy and dimensions

`docs/BUYANOVGPT_TABLE.md` is a response influence atlas, not a theory.

Provisional response labels include `G` global amplitude, `T` scale, `tau` time, `S` metric slip/aniso-stress, `M` small-scale/free-streaming localization, `N` interaction/exchange and `B` background/geometry. They are **not proven independent fundamental parameters**.

Keep separate:

- `N_repr`: coordinates needed to reconstruct/approximate responses;
- `N_disc`: channels needed to discriminate mechanisms.

GDM cs2/cv2 proves these concepts can differ: density/time responses are almost collinear but slip separates the mechanisms.

The dark-sector no-hair analogy is only a falsifiable organizing question. There is no theorem.

---

## 10. Exp045A — simple additive `Core=(G,T,tau)` falsified

Orthogonal decomposition:

\[
\mu=\langle R\rangle_{z,k},
\]

\[
T(k)=\langle R\rangle_z-\mu,
\]

\[
\tau(z)=\langle R\rangle_k-\mu,
\]

\[
\boxed{R(z,k)=\mu+T(k)+\tau(z)+I(z,k)}.
\]

`I(z,k)` is the irreducible scale-time interaction. Under the uniform frozen-grid inner product, the additive core and interaction are orthogonal.

Pre-frozen compact adequacy required `>=95%` core power capture for every direction and `<=5 deg` distortion of every pairwise acute angle.

Run `32883280742`, artifact `9576600500`, SHA256 `59839a2717646e50501a949cf5b310cb6c0e55f85dd6839fce2832c704ec28dd`.

Controls pass. Scientific result:

`FAIL_COMPACT_G_T_TAU_CORE_LOW_K_V0_1`.

Direction interaction power

\[
\boxed{\chi_I=\frac{\|I\|^2}{\|R\|^2}}:
\]

- C1 smooth-w `0.0010805`;
- C2 IDE alpha `1.57e-11`;
- C2 IDE beta `5.49e-11`;
- C3 GDM cs2 `0.0453054`;
- C3 GDM cv2 `0.0436337`;
- C5 designer f(R) **`0.299856`**.

Dropping `I` changes GDM/f(R) acute angles from `25.18/25.49 deg` to `14.77/14.93 deg`; maximum pairwise distortion is IDE-alpha/f(R), `14.31 deg`.

**Hard negative conclusion:** scale and time are not generally separable response coordinates. C5 requires a large joint `k x z` component, C3 a moderate one, while the local IDE directions are essentially additive on this grid.

---

## 11. Exp046 — exact pairwise localization of separation in scale-time interaction

Normalize each response:

\[
u_A=R_A/\|R_A\|,\qquad u_B=R_B/\|R_B\|.
\]

Choose orientation

\[
s=\mathrm{sign}\langle u_A,u_B\rangle
\]

and pair difference

\[
d=u_A-su_B.
\]

Apply the same linear orthogonal decomposition to obtain

\[
d=d_C+d_I,
\]

so

\[
\boxed{\|d\|^2=\|d_C\|^2+\|d_I\|^2}.
\]

Define the pairwise interaction-localization fraction

\[
\boxed{\eta_I(A,B)=\frac{\|d_I\|^2}{\|d\|^2}},\qquad \eta_C=1-\eta_I.
\]

This identity is exact for the frozen-grid inner product. `eta_I` measures the fraction of **normalized pairwise response-shape separation power** in scale-time interaction. It is not significance or detectability.

Hard run `32884761188`, artifact `9577142860`, SHA256 `6e2c7026efe17a81bee10c9a9904c78f5299dce1bf594535be5ded600a3d2834`, source head `d292cb90245c3e472dcbffd076947181fd6ed7cf`.

Controls:

- unit norm residual `5.42e-20`;
- core/interaction orthogonality `1.01e-14`;
- Pythagorean residual `3.25e-19`;
- angle/chord residual `4.76e-15`.

Key `eta_I`:

- GDM cs2/cv2 **`0.731139`**;
- GDM cv2/f(R) **`0.613829`**;
- GDM cs2/f(R) **`0.611982`**;
- IDE-alpha/f(R) **`0.571946`**;
- IDE-beta/f(R) `0.305340`;
- smooth-w/f(R) `0.280354`;
- IDE-alpha/GDM cs2/cv2 `0.243027/0.236822`;
- IDE alpha/beta `1.49e-11`.

Valid interaction-shape acute angles:

- GDM cs2/cv2 `0.742556 deg`;
- GDM cs2/f(R) `10.985703 deg`;
- GDM cv2/f(R) `11.710540 deg`;
- smooth-w versus GDM/f(R) approximately `69.6-70.0 deg`.

### Interpretation rules

1. **Always report `eta_I` with total pair angle/distance.** GDM cs2/cv2 have `eta_I=0.731` but total angle only `0.323 deg`; interaction carries most of a tiny distinction and does not solve the microphysical degeneracy.
2. GDM/f(R) combine a material full angle (`~25 deg`) with `eta_I~0.612`; therefore a substantial fraction of their separation genuinely lives in how scale dependence evolves with time.
3. Interaction morphology itself leaves GDM cs2/cv2 nearly collinear (`0.743 deg`), so metric slip remains necessary.
4. The ordering `IDE near-null -> smooth-w weak -> GDM moderate -> f(R) strong` in `chi_I` is a promising mechanism-level regularity candidate, **not yet a law**.

Repo summary: `data/derived/comparison_readiness/experiment_046_scale_time_interaction_morphology_v0_1.json`.

---

## 12. Current strongest cross-family patterns

### A. Block-sparse influence

\[
K_{AP}t_{GDM}=0,\quad K_{pert}t_{GDM}\neq0,
\]

\[
K_{AP}t_{f(R)}=0,\quad K_{pert}t_{f(R)}\neq0.
\]

### B. Degeneracy migration

Pair similarity belongs to `(model directions + response operator)`, not to the pair alone.

### C. Domain localization

WDM: low-k nearly blind, high-k visible.

### D. Mechanism information outside density growth

GDM pressure/viscosity require metric slip for robust separation.

### E. Scale-time nonseparability

`chi_I` differs by many orders across mechanisms on the current grid, and Exp046 shows interaction can carry most of the materially relevant GDM/f(R) separation.

### F. Representation is not discrimination

A direction may need a component for accurate representation without that component being an effective mechanism discriminator, and vice versa. Keep `N_repr` and `N_disc` separate.

Current discriminant graph minimum hitting set remains `{metric slip, small-scale transfer, time/sign evolution}` for the frozen evidence graph only.

---

## 13. Gate state

- G1 PASS v0.1.1.
- G2 PASS v0.1.1.
- G3A PASS.
- G3B PASS block-aware.
- G4 PASS synthetic rank.
- G5 PARTIAL.
- G6A/G6B PASS.
- G7 OPEN.
- G8 OPEN.

No universal-model, intrinsic-rank, law or discovery claim.

---

## 14. Exact continuation sequence

1. **Exp047A amplitude/step stability:** reconstruct `chi_I` and interaction morphology from available finite family-manifold amplitudes; test whether the hierarchy `IDE -> smooth-w -> GDM -> f(R)` survives beyond one local tangent.
2. **Exp047B leave-one-node-out stability:** delete each k node and each z node in turn, recompute `chi_I` and key `eta_I`, and quantify maximum/rms drift under pre-frozen metrics.
3. Only if those tests are stable, define an independent confirmatory mechanism-classification gate. Do not choose a threshold after seeing results.
4. Extend C4 WDM to a high-k time-dependent `(k,z)` atlas and evaluate its `chi_I`/interaction morphology without low-k zero imputation.
5. Preserve metric slip/lensing and high-k transfer as independent channels.
6. Continue survey/window-aware shape and RSD forward modelling; theory-space geometry is not survey detectability.
7. Estimate stable `N_repr`/`N_disc` only after common observation coordinates and prior/sampling/precision/covariance/channel-removal stress tests.
8. Continue searching for exact nulls, degeneracy migration, orientation/sign changes, localization and robust cross-family relations.
9. Universal model only after readiness criteria and a credible withheld-family prediction plan.
10. Resume G7 only after observationally whitened stability; **no discovery before G8**.

---

## 15. Short recovery summary

**Mission:** reconstruct dark-sector influence without assuming DM/DE/MG ontology.  
**Current state:** six-family block-aware atlas; exact AP nulls for frozen GDM and designer f(R); hard degeneracy migration; C5 density/velocity compression defect; unresolved GDM velocity bridge; additive `(G,T,tau)` core falsified; scale-time interaction morphology quantified.  
**Newest hard insight:** for GDM/f(R), about **61%** of normalized low-k structure-shape separation power lies in irreducible `k x z` interaction. GDM cs2/cv2 show why this is not automatically detectability: `eta_I=0.731` but total separation is tiny.  
**Priority hypothesis:** `chi_I` hierarchy `IDE near-null -> smooth-w weak -> GDM moderate -> f(R) strong`; stress-test before elevation.  
**Boundary:** C4 requires high-k time support; `I` is not a universal parameter/hair.  
**No law/discovery:** G5 partial, G7/G8 open.  
**Never mix DSIR with RTK.**
