# DSIR RECOVERY MANUAL — chat-independent research backup

**Project:** Dark-Sector Influence Reconstruction (DSIR)  
**Repository:** `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`  
**Manual snapshot:** 2026-08-25 after Exp045A  
**Live overlay:** `docs/RECOVERY_LATEST.md`  
**Influence atlas:** `docs/BUYANOVGPT_TABLE.md`  
**Scientific interpretation register:** `docs/SCIENTIFIC_FINDINGS_REGISTER.md`  
**Preserved previous full manual:** `docs/RECOVERY_MANUAL_PRE_EXP044_2026-08-25.md`

This is the stable recovery/methodology manual. The previous detailed manual has been preserved byte-for-byte at the path above before this update, so historical derivations and older experiment details are not lost.

After any chat/session loss read, in order:

1. `docs/RECOVERY_MANUAL.md`;
2. `docs/RECOVERY_LATEST.md`;
3. `docs/SCIENTIFIC_FINDINGS_REGISTER.md`;
4. `docs/BUYANOVGPT_TABLE.md`;
5. `docs/GATES.md` and `docs/STATUS.md`;
6. the latest dated research log;
7. the most recent numbered experiment protocol and frozen result JSON;
8. if older derivation detail is needed, `docs/RECOVERY_MANUAL_PRE_EXP044_2026-08-25.md`.

---

## 0. Hard project boundary and claim discipline

DSIR is independent of RTK. **Never edit, import, overwrite, merge, or silently use the RTK project as a prior.**

DSIR is a reconstruction/meta-inference framework, not a fundamental theory. No discovery or new law is claimed. Preserve these rules:

- missing response is never zero;
- a validated zero is evidence, not missing data;
- raw SVD rank is not microscopic dimension;
- an observational degeneracy is not a physical identity;
- theory-space angles are not survey distinguishability;
- a compressed-data correlation is not causality;
- a known identity is not a discovery;
- a theory-level temporal response is not automatically tracer RSD;
- failed approximations, numerical limits and infrastructure chronology are retained;
- no residual-law claim before G7;
- no discovery claim before G8 withheld prediction.

The main research strategy remains: **compare physically different models, find exact nulls, approximate degeneracies, channel reversals, scale/time/sign patterns and cross-family regularities; look for genuinely new physics only after the relevant solver/gauge/observation contracts pass.** Estimating a minimal latent dimension is parallel work, not the primary target and never a reason to force the answer to 3, 4, or any chosen number.

A universal model is deliberately postponed until `docs/UNIVERSAL_MODEL_READINESS.md` criteria are met.

---

## 1. Scientific question and inverse architecture

Central question:

> What is the minimal **observable influence structure** required to reproduce empirically allowed dark-sector effects, and which relations survive model labels, gauge conventions, observational compression, covariance whitening and theory-family priors?

The intended direction is

`data -> observable response operators -> response geometry/manifolds -> cross-channel relations -> candidate effective dynamics -> candidate fundamental theory`,

not

`assumed model name -> fit parameters -> declare ontology`.

Three layers remain distinct:

- **data/measurement:** likelihoods, covariances, windows, nuisance and selection effects;
- **response/influence:** expansion/AP, density/growth/velocity, metric potentials/slip/lensing, small-scale transfer, tensor channels;
- **theory:** LambdaCDM, smooth DE, IDE, GDM, WDM, modified gravity, EFT/PPF, etc.

Law search belongs primarily to the response layer after quotienting known identities and measurement/compression degeneracies.

---

## 2. Common residual source bookkeeping

Use

\[
\boxed{X_{\mu\nu}=M_0^2G_{\mu\nu}-T^{known}_{\mu\nu}}.
\]

This can represent missing stress-energy, modified-gravity terms or mixtures, but depends on the bookkeeping split and is not itself a unique observable.

For homogeneous FLRW,

\[
\rho_X=3M_0^2(H^2+K/a^2)-\rho_{known},
\]

\[
p_X=-M_0^2(2\dot H+3H^2+K/a^2)-p_{known}.
\]

At perturbation level DSIR maps theory output into gauge/frame-safe response quantities before comparing models.

---

## 3. Frozen conservation/gauge and matter-response contract — G1/G2

For production total matter,

\[
\delta_m=\frac{\sum_i\rho_i\delta_i}{\rho_m},
\]

\[
\theta_m=\frac{\sum_i(\rho_i+p_i)\theta_i}{\rho_m+p_m},
\]

\[
\boxed{\Delta_m=\delta_m+3(1+w_m){\cal H}\frac{\theta_m}{k^2}}.
\]

Frozen response grid:

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

`S` means matched solver lineage/setup when possible. Cross-solver comparison requires an explicit bridge.

**RSD caveat:** gauge-safe total-matter density does not automatically identify the tracer velocity entering galaxy RSD.

---

## 4. Frozen six-family atlas

- **C0:** LambdaCDM/GR response origin.
- **C1:** smooth non-phantom DE, one-sided `epsilon_w=1+w -> 0+`, production step `1e-4`.
- **C2:** interacting vacuum `Q=H(alpha rho_idm + beta rho_iv)`; positive alpha excluded by frozen positivity history; physical coordinate `u=-alpha>=0` plus beta line.
- **C3:** GDM closure directions `cs2/cv2` with `w_gdm=0`.
- **C4:** thermal WDM, intentionally separate informative high-k transfer block.
- **C5:** designer f(R), H-EFTCAMB `DesignerEFTmodel=1`, `EFTwDE=0`, production `B0={1e-6,1e-5,1e-4,1e-3}` with controls `0,1e-7`.

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

hence

\[
\boxed{F_{AP}(z)=\frac{D_M}{D_H}=E(z)\int_0^z\frac{dz'}{E(z')}}.
\]

A multiplicative normalization of `E` cancels. Corrected ShapeFit geometry uses `D_H/D_M`, so

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}.
\]

AP requires full background history from `z=0`; never extrapolate the seven-node structure atlas below `z=0.295`.

Key hard results:

- Exp035 AP operator run `32778635058`, direct bridge error `1.00e-14`.
- Exp036 C1/C2 AP angles: smooth-w/IDE-alpha `72.803493 deg`; smooth-w/IDE-beta `64.151094 deg`; IDE alpha/beta `9.0379006 deg` acute vs `58.9338 deg` in full structure.
- Exp037: frozen GDM cs2/cv2 are exactly background/AP-null while perturbation-active:
  \[
  K_{AP}t_{cs2}=K_{AP}t_{cv2}=0.
  \]
- Exp038: frozen designer-f(R) B0 is exactly background/AP-null while perturbation-active:
  \[
  K_{AP}t_{B0}=0.
  \]

Final C5 transfer-preserving regression: run `32786915513`, artifact `9541895055`, SHA256 `74d975790d00a04762d45bf183481f69d6fc54b84d186c63e89b88bbb9d20b16`.

**Hard cross-family lesson:** `K_geometry t=0` does not imply `t≈0`. New physics can be exactly invisible in background/AP while present in perturbations.

---

## 6. ShapeFit shape and RSD contracts

Corrected DR1 ShapeFit order:

`[D_V/r_d, D_H/D_M, f_sigma_s8, m+n]`.

Finite-node shape proxy:

\[
\ln(P'/P_{ref})=A+\frac{m}{0.6}\tanh[0.6\ln(k/0.03)]+n\ln(k/0.03).
\]

It leaves about 36% representation residual for GDM/f(R); therefore its ~23 deg separation is not a DESI distinguishability claim.

Correct ShapeFit growth convention:

\[
s=\frac{r_d}{r_d^{ref}},\qquad \sigma_{s8}=\sigma(R=s\,8h^{-1}{\rm Mpc}).
\]

For density/velocity moments define

\[
\boxed{{\cal D}_{RSD}=1-\frac{S_{\delta\Theta}^2}{S_{\delta\delta}S_{\Theta\Theta}}}.
\]

Experiment 041 establishes

\[
\boxed{{\cal D}_{RSD}=\frac{\mathrm{Var}_w[g]}{\langle g^2\rangle_w}},\qquad g=\Theta/\delta,
\]

and

\[
CV_w(g)=\sqrt{\frac{{\cal D}_{RSD}}{1-{\cal D}_{RSD}}}.
\]

C5 run `32791510072`, artifact `9543375564`, SHA256 `1e4d86f7f13185d69a07b71afa9bfd6fefa6003119064652d6388491738212bc`.

At `kmax=0.24 h/Mpc`:

- GR floor `~1.42e-10`;
- B0 `1e-6`: `5.18e-6`;
- `1e-5`: `1.92e-4`;
- `1e-4`: `8.81e-4`;
- `1e-3`: `8.78e-4`.

Therefore scalar growth compression is not exact for frozen designer f(R).

**Output-quality limit:** old printed H-EFTCAMB `sigma8` summaries have only ~4 decimals and must not be used for small-B0 tangents.

---

## 7. Temporal response and degeneracy migration — Exp040

For adjacent frozen early->late nodes,

\[
\boxed{\Delta\bar f_P(k)=\frac{r_\Delta(k,z_{late})-r_\Delta(k,z_{early})}{2[\ln a_{late}-\ln a_{early}]}}.
\]

This is theory-space temporal response, not tracer RSD.

Run `32785987735`, artifact `9541462864`.

Hard comparisons:

- IDE alpha/beta: AP `9.04 deg` -> temporal `29.40 deg` -> structure `58.93 deg`.
- smooth-w/IDE-alpha: AP `72.80 deg`, structure `52.19 deg`, temporal only `10.31 deg` (**channel reversal**).
- IDE-alpha/GDM: structure ~`24.8-24.9 deg` -> temporal ~`60.9 deg`.
- GDM cs2/cv2: structure `0.3226 deg` -> temporal `1.3340 deg`; slip still required.
- GDM/f(R): scale-only `0.078-0.102 deg` -> temporal `16-17 deg` -> full `(k,z)` `25.18-25.49 deg`.

**Hard interpretation:** degeneracies migrate between response operators. Adding one channel can separate one pair and collapse another; the joint multi-channel object matters.

---

## 8. GDM velocity/gauge negative chronology — Exp042/043

Do not lose this sequence.

1. Synchronous GDM velocity is gauge-ill-conditioned for RSD.
2. Pinned GDM_CLASS exposes an N-body transfer option but upstream stops because the derivative of `H_T_Nb_prime` is not propagated.
3. Exp042 generated matched synchronous/Newtonian runs. The first parser assumed the same transfer-column layout, but synchronous had an auxiliary CDM column and Newtonian did not. This parser-only bug was fixed without changing scientific thresholds.
4. The actual bridge then failed:
   - max absolute `ln|Delta_S/Delta_N| = 2.58664e-6` > `1e-6`;
   - model/reference response difference `6.78698e-7` < `1e-6`.
5. Exp043 removed the bad raw-k-grid comparison by interpolating each gauge independently to the frozen nodes and tightened only numerical precision.

Exp043 p8:

- absolute bridge `2.51958e-6`;
- response bridge `6.78698e-7`.

p10:

- absolute bridge `3.00625e-6`;
- response bridge `8.02174e-7`;
- p10/p8 residual ratio `1.19316`.

Run `32794067542`, artifact `9544255453`, SHA256 `c62613798a6a6f8e9e573bb158315ca03a5c9f998805ebfc6bdda25de4d4100a`.

**Negative result:** tighter perturbation precision does not explain the absolute gauge mismatch. Do not loosen the threshold. All Exp042 GDM velocity angles and `D_RSD` values remain exploratory/non-admissible science.

---

## 9. BuyanovGPT table and no-hair analogy

`docs/BUYANOVGPT_TABLE.md` is the live influence atlas. The nickname is an organizer, not a theory.

The chat introduced provisional labels:

- `G`: global growth/amplitude;
- `T`: scale dependence;
- `tau`: time dependence;
- `S`: metric slip/aniso-stress information;
- `M`: small-scale/free-streaming/domain-localized information;
- `N`: interaction/exchange information;
- `B`: background/geometry information.

Do **not** treat these labels as proven independent parameters.

Two dimensions must be kept separate:

- `N_repr`: minimum coordinates needed to reproduce/approximate responses;
- `N_disc`: minimum independent channels needed to discriminate physical mechanisms.

GDM cs2/cv2 already proves they can differ: density/time responses are nearly collinear while metric slip separates the mechanisms.

The black-hole/no-hair analogy is only the falsifiable question whether many microscopic models project onto a smaller stable observable influence space. **There is no dark-sector no-hair theorem.**

---

## 10. Experiment 045A — falsification of simple `Core=(G,T,tau)`

The conversational claim that all common responses might be captured by three additive types was made testable via the orthogonal decomposition

\[
\boxed{R(z,k)=\mu+T(k)+\tau(z)+I(z,k)},
\]

where

\[
\mu=\langle R\rangle_{z,k},
\]

\[
T(k)=\langle R\rangle_z-\mu,
\]

\[
\tau(z)=\langle R\rangle_k-\mu,
\]

and `I(z,k)` is irreducible scale-time interaction.

Pre-frozen compact adequacy required:

1. `||R_core||^2/||R||^2 >= 0.95` for every direction;
2. every pairwise acute angle distortion <= `5 deg`.

Final controlled run `32883280742`, artifact `9576600500`, SHA256 `59839a2717646e50501a949cf5b310cb6c0e55f85dd6839fce2832c704ec28dd`, head `b3e2aacb1330a68b7b3ae07e8802a0ac5dc03c63`.

Operator controls pass with reconstruction error `0`, zero-mean residual `4.22e-21`, core-interaction normalized inner product `2.57e-15`.

Status:

`FAIL_COMPACT_G_T_TAU_CORE_LOW_K_V0_1`.

Key results:

| Direction | `||I||/||R||` | interaction power | core power capture |
|---|---:|---:|---:|
| C1 smooth-w | 0.03287 | 0.001081 | 0.998919 |
| C2 IDE alpha | 3.97e-6 | 1.57e-11 | ~1 |
| C2 IDE beta | 7.41e-6 | 5.49e-11 | ~1 |
| C3 GDM cs2 | 0.21285 | 0.04531 | 0.954695 |
| C3 GDM cv2 | 0.20889 | 0.04363 | 0.956366 |
| C5 designer f(R) | **0.54759** | **0.29986** | **0.700144** |

Dropping `I` distorts:

- IDE-alpha/f(R) by **14.31 deg**;
- GDM-cs2/f(R) by **10.41 deg**;
- GDM-cv2/f(R) by **10.56 deg**.

**Hard negative conclusion:** simple additive `(G,T,tau)` is not sufficient even on the common C1/C2/C3/C5 low-k theory block.

**New research direction:** `I(k,z)` — scale-time nonseparability — is a hard-required representation component for C5 on this block and non-negligible for C3. It is a **candidate response signature**, not yet a universal fundamental parameter.

This sharpens the earlier GDM/f(R) result: their difference is not merely “scale plus time”; part of the distinction lives in how scale dependence evolves with time.

C4 WDM is excluded from Exp045A because its informative response lives at high k. Never insert it as low-k zero. Family-complete testing requires high-k time support.

---

## 11. Current strongest cross-family patterns

### A. Block-sparse influence

Hard examples:

\[
K_{AP}t_{GDM}=0,\qquad K_{pert}t_{GDM}\neq0,
\]

\[
K_{AP}t_{f(R)}=0,\qquad K_{pert}t_{f(R)}\neq0.
\]

### B. Degeneracy migration

Pair similarity is a property of `(model directions + response operator)`, not an intrinsic scalar attribute of a pair.

### C. Domain localization

WDM: low-k nearly blind, high-k visible.

### D. Mechanism information can live outside density growth

GDM cs2/cv2 remain nearly collinear in density/time but metric slip separates them strongly.

### E. Scale-time nonseparability

Exp045A shows C5 carries ~30% of structure-response power in an irreducible `k x z` interaction, with C3 ~4.4-4.5%. This is now a priority cross-family signature to test.

Current minimum hitting set of the frozen discriminant graph remains

`{metric slip, small-scale transfer, time/sign evolution}`,

but this is **not** proof of three parameters and may be refined by the new `I(k,z)` analysis.

---

## 12. Gate state

- G1 PASS v0.1.1.
- G2 PASS v0.1.1.
- G3A PASS v0.1.
- G3B PASS block-aware.
- G4 PASS synthetic rank.
- G5 PARTIAL.
- G6A/G6B PASS.
- G7 OPEN.
- G8 OPEN.

No universal-model, law, intrinsic-rank or discovery claim.

---

## 13. Exact continuation sequence

1. Consolidate Exp042/043 negative gauge chronology into the findings register/status/log and preserve their open-PR history; do not merge stale exploratory claims as if validated.
2. Promote Exp045A to the findings register as a hard negative representation result.
3. Test **`I(k,z)` morphology and stability** across parameter step size/precision and across C1/C2/C3/C5. Freeze metrics before looking at new target comparisons.
4. Ask whether the interaction component itself improves mechanism discrimination, especially GDM vs f(R), and whether its sign/orientation is characteristic.
5. Extend C4 WDM to a high-k `(k,z)` response atlas so its scale-time nonseparability can be tested without domain mismatch.
6. Continue metric slip/lensing and small-scale transfer because existing hard results show they carry independent discriminator information.
7. Continue survey/window-aware shape and RSD operators; theory-space angles alone do not establish observability.
8. Only after common observation-space coordinates exist, estimate stable latent dimension under family priors, sampling, precision, covariance and channel removal.
9. Continue primary DSIR work: compare models, search for exact nulls, degeneracy migrations, sign changes, domain-localized effects, nonseparable response structures and any cross-family relation that survives controls.
10. Universal model only after readiness criteria and a credible withheld-family prediction plan.
11. G7 residual-law search only after observational-whitened stability; **no discovery before G8**.

---

## 14. Short recovery summary

**Mission:** reconstruct dark-sector influence without assuming DM/DE/MG ontology.  
**Current state:** six-family block-aware atlas; exact AP nulls for frozen GDM and designer f(R); hard channel-degeneracy migration; C5 density/velocity scalar-compression defect; unresolved GDM gauge-velocity bridge; simple additive `(G,T,tau)` core falsified.  
**Newest hard insight:** **scale and time are not generally separable response coordinates. The joint `k x z` interaction carries ~30% of the frozen C5 structure-response power and materially preserves GDM/f(R) separation.**  
**Important boundary:** C4 WDM still requires high-k time support; `I(k,z)` is not yet a universal hair/parameter.  
**No law/discovery:** G5 partial, G7/G8 open.  
**Never mix DSIR with RTK.**
