# DSIR RECOVERY MANUAL — chat-independent research backup

**Project:** Dark-Sector Influence Reconstruction (DSIR)  
**Repository:** `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`  
**Manual snapshot:** 2026-08-25 after Exp047B  
**Live overlay:** `docs/RECOVERY_LATEST.md`  
**Scientific register:** `docs/SCIENTIFIC_FINDINGS_REGISTER.md`  
**Influence atlas:** `docs/BUYANOVGPT_TABLE.md`  
**Preserved older detailed manual:** `docs/RECOVERY_MANUAL_PRE_EXP044_2026-08-25.md`

Use this file to recover the active methodology and state after chat/session loss. For older derivation/infrastructure detail, read the preserved pre-Exp044 manual rather than inventing missing history.

Recovery read order:

1. `docs/RECOVERY_MANUAL.md`;
2. `docs/RECOVERY_LATEST.md`;
3. `docs/SCIENTIFIC_FINDINGS_REGISTER.md`;
4. `docs/STATUS.md` and `docs/GATES.md`;
5. `docs/BUYANOVGPT_TABLE.md`;
6. newest experiment protocol/result JSON and dated research log;
7. preserved older manual/register snapshots when historical detail is needed.

---

## 0. Non-negotiable project/claim rules

DSIR is independent of RTK. **Never mix repositories or silently use RTK as a prior.**

DSIR is a reconstruction/meta-inference framework, not a fundamental theory. Preserve these boundaries:

- missing response is never zero;
- a validated zero is evidence;
- raw SVD/catalog dimension is not microscopic dimension;
- theory-space angles are not survey distinguishability;
- a compressed-data correlation is not causality;
- a known identity is not discovery;
- negative results and infrastructure failures are preserved;
- no residual-law claim before G7;
- no discovery before G8 withheld prediction.

Primary scientific program: compare qualitatively different models, identify exact nulls, degeneracies, channel reversals, sign/orientation changes, scale/time structure, domain localization and cross-family regularities. Minimal latent dimension is parallel work, not an assumption. Universal-model construction remains postponed until `docs/UNIVERSAL_MODEL_READINESS.md` criteria are met.

---

## 1. Inverse architecture and residual bookkeeping

Central question:

> What is the minimal observable influence structure required to reproduce allowed dark-sector effects, and which relations survive model labels, gauge conventions, observational compression, covariance whitening and family priors?

Inference direction:

`data -> observation/response operators -> response geometry -> cross-channel relations -> candidate effective dynamics -> candidate theory`.

Common bookkeeping object:

\[
\boxed{X_{\mu\nu}=M_0^2G_{\mu\nu}-T^{known}_{\mu\nu}}.
\]

For FLRW,

\[
\rho_X=3M_0^2(H^2+K/a^2)-\rho_{known},
\]

\[
p_X=-M_0^2(2\dot H+3H^2+K/a^2)-p_{known}.
\]

`X_munu` is bookkeeping, not a unique observable. Map solver output into validated response quantities before comparing theories.

---

## 2. Frozen matter/gauge and response basis — G1/G2 PASS

Total matter:

\[
\delta_m=\frac{\sum_i\rho_i\delta_i}{\rho_m},
\qquad
\theta_m=\frac{\sum_i(\rho_i+p_i)\theta_i}{\rho_m+p_m},
\]

\[
\boxed{\Delta_m=\delta_m+3(1+w_m){\cal H}\frac{\theta_m}{k^2}}.
\]

Frozen structure nodes:

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`,

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

Anchored expansion response:

\[
\boxed{r_E(z;z_*)=\ln\left[\frac{H(z)/H(z_*)}{H_{ref}(z)/H_{ref}(z_*)}\right]},\qquad z_*=0.51.
\]

Production structure response:

\[
\boxed{r_\Delta(k,z)=\ln\frac{P^S_{\Delta,model}(k,z)}{P^S_{\Delta,ref}(k,z)}}.
\]

Cross-solver comparisons require explicit bridges. RSD tracer velocity is not automatically the same semantic object as gauge-safe total-matter density.

---

## 3. Frozen family atlas and pinned upstream

- **C0:** LambdaCDM/GR origin.
- **C1:** smooth non-phantom DE; `epsilon_w=1+w -> 0+`; production step `1e-4`.
- **C2:** IDE `Q=H(alpha rho_idm+beta rho_iv)`; positive alpha excluded by positivity history; use `u=-alpha>=0` and beta line.
- **C3:** GDM `cs2/cv2`, frozen `w_gdm=0`.
- **C4:** thermal WDM, separate high-k transfer block. Never insert as low-k zero.
- **C5:** designer f(R), H-EFTCAMB `DesignerEFTmodel=1`, `EFTwDE=0`, production `B0={1e-6,1e-5,1e-4,1e-3}`, controls `0,1e-7`.

Pinned source revisions:

- C1/C3: `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`;
- C2: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- C5: `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

C5 immutable hard config artifact: run `32759477319`, artifact `9532245261`, SHA256 `9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`, lineage `dsir_mgs1_hp_*`.

---

## 4. AP and exact null-space results

Flat-FLRW AP:

\[
D_H=\frac{c}{H_0E(z)},\qquad D_M=\frac{c}{H_0}\int_0^z\frac{dz'}{E(z')},
\]

\[
\boxed{F_{AP}=\frac{D_M}{D_H}=E(z)\int_0^z\frac{dz'}{E(z')}}.
\]

Multiplicative normalization of `E` cancels exactly. Corrected ShapeFit coordinate obeys

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}.
\]

Never extrapolate the seven-node structure grid to `z=0` for production AP; use full solver backgrounds.

Hard nulls:

\[
K_{AP}t_{cs2}=K_{AP}t_{cv2}=0
\]

for frozen GDM closure directions (Exp037), and

\[
K_{AP}t_{B0}=0
\]

for frozen designer f(R) (Exp038), while both are perturbation-active.

C5 final transfer-preserving Exp038 regression: run `32786915513`, artifact `9541895055`, SHA256 `74d975790d00a04762d45bf183481f69d6fc54b84d186c63e89b88bbb9d20b16`.

**Hard lesson:** no background/AP anomaly does not imply proximity to the physical origin in the full response space.

---

## 5. Temporal response, degeneracy migration and compression limits

Finite-bin theory temporal response:

\[
\boxed{\Delta\bar f_P(k)=\frac{r_\Delta(k,z_{late})-r_\Delta(k,z_{early})}{2[\ln a_{late}-\ln a_{early}]}}.
\]

Key Exp040 comparisons:

- IDE alpha/beta: AP `9.04 deg` -> temporal `29.40 deg` -> structure `58.93 deg`;
- smooth-w/IDE-alpha: AP `72.80`, temporal `10.31`, structure `52.19 deg`;
- GDM cs2/cv2: structure `0.3226`, temporal `1.334 deg`, slip still required;
- GDM/f(R): scale-only `0.078-0.102`, temporal `16-17`, full `(k,z)` `25.18-25.49 deg`.

**Hard lesson:** degeneracies migrate between operators; one channel can separate one pair and collapse another.

Corrected ShapeFit order:

`[D_V/r_d, D_H/D_M, f_sigma_s8, m+n]`.

Finite-node `m+n` representation leaves ~36% residual for GDM/f(R), so proxy angles are not survey distinguishability.

---

## 6. Density/velocity representability and GDM velocity negative gate

ShapeFit growth uses

\[
s=r_d/r_d^{ref},\qquad R=s\,8h^{-1}{\rm Mpc}.
\]

Density/velocity representability defect:

\[
\boxed{{\cal D}_{RSD}=1-\frac{S_{\delta\Theta}^2}{S_{\delta\delta}S_{\Theta\Theta}}}
=\frac{\mathrm{Var}_w[g]}{\langle g^2\rangle_w},\qquad g=\Theta/\delta.
\]

C5 Exp041 hard run `32791510072`, artifact `9543375564`, SHA256 `1e4d86f7f13185d69a07b71afa9bfd6fefa6003119064652d6388491738212bc` shows nonzero production `D_RSD`, so scalar growth compression is not exact for frozen designer f(R).

Old printed CAMB growth summaries are rejected for small-B0 tangents because of four-decimal quantization.

GDM Exp042/043 negative chronology:

- synchronous velocity is gauge-ill-conditioned for RSD;
- pinned N-body transfer route is incomplete upstream;
- Exp042 absolute synchronous/Newtonian comoving-density bridge fails `1e-6`;
- Exp043 tighter perturbation precision worsens the absolute residual (`2.5196e-6 -> 3.0063e-6`, ratio `1.19316`).

Run `32794067542`, artifact `9544255453`, SHA256 `c62613798a6a6f8e9e573bb158315ca03a5c9f998805ebfc6bdda25de4d4100a`.

Do not loosen the gate and do not use exploratory GDM velocity/RSD outputs as validated physics.

---

## 7. BuyanovGPT taxonomy and dimension discipline

`docs/BUYANOVGPT_TABLE.md` is a response atlas/hypothesis organizer, not a theory. Provisional labels include:

- `G` global amplitude/growth;
- `T` scale dependence;
- `tau` time evolution;
- `S` metric slip/aniso-stress;
- `M` small-scale/free-streaming localization;
- `N` interaction/exchange;
- `B` background/geometry.

Keep distinct:

- `N_repr`: coordinates/functions needed to reconstruct responses;
- `N_disc`: independent channels needed to discriminate mechanisms.

No dark-sector no-hair theorem exists. The analogy is only a falsifiable organizing question.

---

## 8. Exp045A — additive `(G,T,tau)` core falsified

For each response matrix define

\[
\mu=\langle R\rangle_{z,k},
\]

\[
T(k)=\langle R\rangle_z-\mu,
\qquad
\tau(z)=\langle R\rangle_k-\mu,
\]

\[
\boxed{R(z,k)=\mu+T(k)+\tau(z)+I(z,k)}.
\]

`I` is irreducible scale-time interaction and is orthogonal to the additive core under the frozen-grid inner product.

Define

\[
\boxed{\chi_I=\frac{\|I\|^2}{\|R\|^2}}.
\]

Hard run `32883280742`, artifact `9576600500`, SHA256 `59839a2717646e50501a949cf5b310cb6c0e55f85dd6839fce2832c704ec28dd`.

Full-grid `chi_I`:

- C1 smooth-w `0.0010805`;
- C2 IDE alpha `1.57e-11`;
- C2 IDE beta `5.49e-11`;
- C3 GDM cs2 `0.0453054`;
- C3 GDM cv2 `0.0436337`;
- C5 f(R) `0.299856`.

C5 additive core captures only `70.01%`; compact `(G,T,tau)` hypothesis fails. Dropping `I` reduces GDM/f(R) angles from `25.18/25.49` to `14.77/14.93 deg`.

Do not infer `I` is a fourth fundamental parameter or that `N_repr=4`.

---

## 9. Exp046 — pairwise interaction localization

For normalized responses

\[
u_A=R_A/\|R_A\|,\qquad u_B=R_B/\|R_B\|,
\]

choose the acute orientation `s=sign(<u_A,u_B>)` and

\[
d=u_A-su_B=d_C+d_I.
\]

Orthogonality gives

\[
\boxed{\|d\|^2=\|d_C\|^2+\|d_I\|^2},
\]

so

\[
\boxed{\eta_I=\frac{\|d_I\|^2}{\|d\|^2}}.
\]

Hard run `32884761188`, artifact `9577142860`, SHA256 `6e2c7026efe17a81bee10c9a9904c78f5299dce1bf594535be5ded600a3d2834`.

Key full-grid `eta_I`:

- GDM cs2/cv2 `0.7311`, but total angle only `0.323 deg`;
- GDM cs2/f(R) `0.6120`;
- GDM cv2/f(R) `0.6138`;
- IDE-alpha/f(R) `0.5719`;
- IDE alpha/beta `~1.5e-11`.

GDM cs2/cv2 interaction shapes remain nearly collinear (`0.743 deg`), so interaction does not replace slip.

PR #25 merged to `main` as `bb4261224efd09b2063f29faca22d6f2efbda1f7` after current-head regressions passed.

---

## 10. Exp047B — leave-one-node robustness of scale-time interaction

Purpose: test whether Exp046 results are driven by one particular frozen `k` or `z` node.

Generate exactly 12 reduced grids: leave out each of five k nodes and each of seven z nodes once, recomputing the decomposition from scratch. No scientific drift threshold was set; only algebraic controls could fail.

First run failed only at JSON serialization of `numpy.longdouble`; serialization-only fix left formulas/grids/thresholds unchanged.

Successful provenance:

- run `32894616114`;
- source head `9a05c451401ac2cede3a56ef4ca2a1923eecb9c3`;
- artifact `9580724793`;
- SHA256 `948038245e4eeea9ca569a48e138f5bdddaede19f0ff98ea941fc91a00272bb7`.

Controls pass:

- reconstruction `0`;
- max core/I orthogonality `8.3946e-14`;
- max Pythagorean residual `2.3505e-17`;
- ceiling `1e-12`.

### Hard descriptive hierarchy robustness

The ordering

\[
\boxed{\text{IDE near-null}<\text{smooth-w}<\text{GDM}<f(R)}
\]

is preserved in **12/12** single-node deletions. Both IDE directions stay below the existing `chi_I=1e-6` morphology floor in **12/12** grids.

Leave-one-node `chi_I` ranges:

- IDE alpha `1.99e-13 .. 7.36e-11`;
- IDE beta `3.66e-13 .. 7.45e-11`;
- smooth-w `3.91e-5 .. 1.34e-3`;
- GDM cs2 `0.0279 .. 0.0525`;
- GDM cv2 `0.0265 .. 0.0505`;
- f(R) `0.2233 .. 0.3497`.

### Hard descriptive GDM/f(R) pair robustness

- cs2/f(R): `eta_I=0.5504 .. 0.6539`;
- cv2/f(R): `eta_I=0.5520 .. 0.6554`.

Thus more than half of normalized GDM/f(R) shape-separation power remains in irreducible interaction for every leave-one-node grid. This is descriptive because `eta_I>0.5` was not preregistered as a scientific gate.

### Hard limitation: smooth-w magnitude

Removing `k=0.001 h/Mpc` changes

\[
\chi_I:1.0805\times10^{-3}\rightarrow3.9123\times10^{-5},
\]

about `27.6x` lower. The smooth-w **tier** is robust; the precise `chi_I` magnitude is not yet a grid-insensitive family invariant.

**Current safest interpretation:** `chi_I` is presently a response descriptor whose coarse mechanism hierarchy is robust on this grid, while absolute magnitudes have family-dependent domain sensitivity. GDM/f(R) joint `k x z` separation is substantially more robust than smooth-w magnitude.

Detailed result: `experiments/047b_interaction_leave_one_node_stability_v0_1.md` and `data/derived/comparison_readiness/experiment_047b_interaction_leave_one_node_stability_v0_1.json`.

---

## 11. Current strongest cross-family patterns

1. **Block-sparse influence:** GDM and designer f(R) can be exactly geometry/AP-null but perturbation-active.
2. **Degeneracy migration:** pair similarity belongs to `(direction, operator)`, not the model pair alone.
3. **Domain localization:** WDM is low-k blind/high-k active.
4. **Metric information can be indispensable:** GDM pressure/viscosity remain density/time/interaction-degenerate but slip-separated.
5. **Scale-time nonseparability:** current coarse hierarchy `IDE << smooth-w < GDM < f(R)` survives every single-node deletion.
6. **Persistent GDM/f(R) joint evolution:** `eta_I` remains `0.55-0.655` under all leave-one-node tests.
7. **Magnitude is not automatically invariant:** smooth-w low-k sensitivity is a hard caution against overinterpreting `chi_I` as a universal scalar hair.
8. **Representation is not discrimination:** keep `N_repr` and `N_disc` separate.

Current discriminant-graph minimum hitting set remains `{metric slip, small-scale transfer, time/sign evolution}` for the current evidence graph only.

---

## 12. Gate state

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

## 13. Exact continuation sequence

1. **Exp047A amplitude/finite-step stability:** inspect immutable C1/C2/C3/C5 manifold artifacts and reconstruct finite-amplitude response matrices where complete `(k,z)` output exists. Test the nonseparability hierarchy away from one local tangent.
2. For smooth-w, diagnose the `k=0.001` sensitivity using neighboring low-k support and solver-precision/domain checks before assigning physical meaning.
3. If amplitude stability supports the hierarchy, preregister an independent future classification test using thresholds not fitted to Exp045A/046/047B outcomes.
4. Extend C4 WDM to a high-k time-dependent `(k,z)` atlas and evaluate its nonseparability without cross-domain zero imputation.
5. Preserve metric slip/lensing and high-k transfer as independent channels.
6. Continue survey/window-aware shape and RSD operators before detectability claims.
7. Estimate stable `N_repr`/`N_disc` only after common observation coordinates plus prior/sampling/precision/covariance/channel-removal stress tests.
8. Continue searching for exact nulls, channel reversals, orientation/sign changes, localization and robust cross-family relations.
9. Universal model only after readiness criteria and a withheld-family prediction plan.
10. G7 stays open; **no discovery before G8**.

---

## 14. Short recovery summary

**Mission:** infer observable dark-sector influence without assuming DM/DE/MG ontology.  
**Current state:** six-family block-aware atlas; exact AP nulls for frozen GDM/f(R); hard degeneracy migration; C5 density/velocity compression defect; GDM velocity bridge negative; additive `(G,T,tau)` core falsified; scale-time interaction and pairwise localization quantified and grid-stress-tested.  
**Newest robust pattern:** `IDE near-null < smooth-w < GDM < f(R)` in `chi_I` survives 12/12 leave-one-node grids; GDM/f(R) keeps `eta_I=0.55-0.655`.  
**Newest caution:** smooth-w absolute `chi_I` is strongly low-k sensitive and should not yet be called a precise invariant.  
**Priority next:** amplitude/finite-step stability, then C4 high-k time support and observation-space validation.  
**No law/discovery:** G5 partial, G7/G8 open.  
**Never mix DSIR with RTK.**

<!-- DSIR_EXP049B_DOC_SYNC_2026_08_26 -->
## Recovery addition — Exp049B physical-window validation (2026-08-26)

### Why this experiment exists

Exp048B showed, retrospectively, that GDM viscosity localization moves toward lower k at large amplitude. Exp049A source audit identified a physical diagnostic scale from the exact pinned dynamic-shear equations. Exp049B converts that retrospective pattern into a withheld prediction.

For frozen `w=ca2=0`, flat C3 with `dynamic_shear_gdm=yes`:

\[
\theta'\supset-\mathcal H\theta-k^2\sigma,
\qquad
\sigma'=-3\mathcal H\sigma+\frac{8}{3}c_v^2(\theta+\mathrm{metric\ shear}).
\]

Under a **diagnostic quasi-steady approximation only** (`sigma'≈0`, metric-shear omitted only in this estimate),

\[
\sigma\simeq\frac{8}{9}\frac{c_v^2}{\mathcal H}\theta,
\]

and equality of viscous and Hubble damping gives

\[
\boxed{k_{v,QS}=\sqrt{9/8}\,\mathcal H/\sqrt{c_v^2}}.
\]

Use the same-run CLASS background to obtain `Hconf=aH`; never reconstruct it from a hand-closed Friedmann approximation.

### Frozen independent test

Reference redshift: `z=1.317`; window edge `kmax=0.1 h/Mpc`; crossing amplitude about `1.08e-5`.

Withheld grid: `cv2={1.5e-5,2e-5,3e-5,5e-5,7e-5}`.

Frozen prediction before solver output:

`k_I_geo(cv2[i+1]) <= k_I_geo(cv2[i]) + 1e-6 h/Mpc`.

No time-centroid or magnitude prediction was frozen.

### Result and provenance

Run `32904158849`; artifact `9584180621`; SHA256 `892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a`.

Measured `k_I_geo`:

`0.0501743 -> 0.0498346 -> 0.0490456 -> 0.0470456 -> 0.0446043 h/Mpc`.

All steps negative; operator controls pass by many orders of magnitude. Status: **HARD ESTABLISHED for this withheld C3 interpolation test**.

### Recovery boundary

Do not upgrade this to a universal scale law. `k_v_QS` is not yet an exact eigenmode scale. The required next cross-mechanism check is Exp049A using exact pinned designer-f(R) `B(a)` diagnostics. G7 and G8 remain open.

<!-- EXP049A_F22_SYNC_2026-08-26 -->
## Recovery addendum — physical transition-scale bridge (Exp049A/F22)

When reconstructing the research, do not infer a characteristic scale from fitted localization. Re-derive it from the pinned source equations.

### C3 GDM
For frozen `w_gdm=0`, pressure enters the Euler equation through a `c_s^2 k^2` gradient, giving the labelled Hubble-gradient crossing
\[k_s=\mathcal H/\sqrt{c_s^2}.\]
Pinned dynamic shear satisfies a damping/source equation of the form
\[\sigma'=-3\mathcal H\sigma + (8/3)c_v^2(\theta+\text{metric shear}),\]
while Euler contains `-k^2 sigma`. Neglecting `sigma'` and metric shear only for the diagnostic quasi-steady estimate gives `sigma~(8/9)c_v^2 theta/Hconf`, hence
\[k_{v,QS}=\sqrt{9/8}\,\mathcal H/\sqrt{c_v^2}.\]
Never relabel this as an exact Jeans/eigenmode scale.

### C5 designer f(R)
Pinned EFTCAMB defines
\[B=\frac{f_R'}{1+f_R}\frac{H}{H'}=\frac{f_{RR}R'}{1+f_R}\frac{H}{H'},\]
prime `d/d ln a`. Exp049A adds diagnostic-only output of `x,a,B,R/H0^2,f_R,E,E',E''` without changing the solved equations. With `Rbar=R/H0^2`,
\[\frac{1+f_R}{3f_{RR}H_0^2}=\frac{Rbar'}{3B(H'/H)},\quad Rbar'=3(4E'+E''),\quad H'/H=E'/(2E).\]
The comoving inverse-Compton wavenumber is `a*(100/c)*sqrt((1+f_R)/(3 f_RR H0^2))` in `h/Mpc`; scalaron mass additionally subtracts `Rbar/3` inside the mass-squared expression.

Recovery provenance: run `32904376001`, artifact `9584346604`, artifact digest `6a2c7f4e072fe7ee5d3a125bd798e975ab7031f5e7e92f3c71b47dbe71856f22`; pinned GDM_CLASS `4c87916a...`, pinned H-EFTCAMB `16d9c4e9...`.

Scientific discipline: the Exp049A f(R) alignment is retrospective. Only GDM has a withheld validation so far (Exp049B/F21). Exp049C must be frozen before new intermediate B0 outputs. Do not advance G7 or G8 from F22 alone.

<!-- DSIR_EXP050A_DOC_SYNC_2026_08_26 -->
## Recovery update — Exp049A through Exp050A (2026-08-26)

### Window-crossing result chain

Exp048B first observed that finite-amplitude GDM-viscosity and designer-f(R) interaction localization moves toward smaller `k_I^geo`. Exp049A then derived characteristic scales from pinned source equations rather than fitting the response:

- GDM pressure: `k_s=Hconf/sqrt(cs2)`;
- GDM dynamic-shear labelled quasi-steady proxy: `k_v,QS=sqrt(9/8) Hconf/sqrt(cv2)`;
- designer-f(R): exact inverse-Compton scale from the pinned EFTCAMB `B(a)` definition through `f_RR`.

Exp049B froze new GDM amplitudes before output and predicted non-increasing `k_I^geo`; run `32904158849` passed. Exp049C then froze new designer-f(R) `B0={1.5,2,3,5,7}e-4` before output and the same directional prediction; run `32907619613` passed. Therefore two physically distinct represented mechanisms now have genuine withheld interpolation support for the finite-window directional principle. This is still not G7 or G8.

### C4 high-k time completion — Exp050A

Use pinned official CLASS solver output, not the old static Viel fit, for production `P_WDM(k,z)/P_CDM(k,z)` comparisons.

Frozen domain:

- masses `m={2,3,5} keV`;
- `k={0.1,0.3,1,3,10,20} h/Mpc`;
- `z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`.

Response:

`r_WDM(k,z)=ln[P_WDM(k,z)/P_CDM(k,z)]`.

Hard run `32908751625`, artifact `9585845292`, SHA256 `5d02bdce07da95c2bb9eab01acb2641f110b6b16e4ecf29ac2e8b1619d053139`.

At `z=0.295`, `r(k=20)` is `-1.1934447, -0.4451668, -0.1191708` for `2,3,5 keV`. Maximum redshift drift is only `6.83e-5, 2.26e-5, 5.07e-6`.

Applying `R=mu+T(k)+tau(z)+I(k,z)` gives `chi_I={2.5826e-10,2.2081e-10,2.2916e-10}`. Hence current linear high-k thermal-WDM is strongly scale-dominated and nearly time-separable. Do not generalize this beyond the frozen domain.

Legacy Viel comparison is descriptive only; the solver atlas is the DSIR production time-dependent C4 block.

### Recovery discipline

- Never zero-pad C4 into low-k matrices.
- Keep C4 high-k and C1/C2/C3/C5 low-k as masked blocks until an operator genuinely maps them to common observation coordinates.
- Keep `N_micro`, `N_manifold`, `N_repr`, `N_disc` distinct.
- G7/G8 remain open; universal-model construction stays blocked.
