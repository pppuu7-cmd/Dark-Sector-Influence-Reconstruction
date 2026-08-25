# DSIR RECOVERY LATEST — live per-iteration overlay

**Date:** 2026-08-25  
**Stable manual:** `docs/RECOVERY_MANUAL.md`  
**Scientific findings:** `docs/SCIENTIFIC_FINDINGS_REGISTER.md`  
**Current status:** `docs/STATUS.md`  
**Gates:** `docs/GATES.md`  
**Influence atlas:** `docs/BUYANOVGPT_TABLE.md`  
**Latest observational log:** `docs/RESEARCH_LOG_OBSERVATIONAL_2026-08-25.md`

This is the mandatory per-iteration recovery layer. Update it after every substantive research iteration. If a later result contradicts an earlier interpretation, preserve chronology and mark the old conclusion `SUPERSEDED/RETRACTED` rather than deleting it.

Hard boundary: **DSIR is independent of RTK. Never modify, import, overwrite, merge, or use the RTK repository as an unstated prior.**

---

## 1. Claim boundary and live gates

DSIR is a reconstruction/meta-inference framework, not a fundamental theory. No new law or discovery is claimed.

- **G1 PASS v0.1.1** — conservation/gauge contract.
- **G2 PASS v0.1.1** — same-solver total-matter `r_Delta` response basis.
- **G3A PASS v0.1** — six background family embeddings.
- **G3B PASS v0.1 block-aware** — six-family beyond-background atlas comparison-ready.
- **G4 PASS** — synthetic rank recovery.
- **G5 PARTIAL** — real-covariance shape/AP pieces and theory-level temporal operator exist; family-complete observational growth/window/shape whitening and rank stress tests do not.
- **G6A/G6B PASS** — DESI DR2 AP and corrected DESI DR1 ShapeFit observational layers.
- **G7 OPEN** — no residual-law claim yet.
- **G8 OPEN** — no discovery before a withheld prediction.

Latest controlled chronology:

- Exp034 run `32777716140` — ShapeFit `m+n` marginal whitening proxy PASS.
- Exp035 run `32778635058` — exact calibration-free AP operator PASS.
- Exp036 run `32782545098` — C1/C2 production AP geometry PASS.
- Exp037 run `32783243120` — GDM C3 AP-zero audit PASS.
- Exp038 final regression run `32786915513` — designer-f(R) C5 AP-zero + transfer handoff PASS.
- Exp040 run `32785987735` — finite-bin theory growth operator PASS.
- Exp041 run `32791510072` — C5 high-precision density/velocity scalar-RSD representability PASS; scalar compression is not exact.
- Exp042 run `32793688546` — GDM synchronous/Newtonian absolute comoving-density bridge FAIL; exploratory velocity science rejected.
- Exp043 run `32794067542` — tighter-precision GDM gauge bridge convergence FAIL; absolute mismatch does not improve.
- Exp045A run `32883280742` — simple additive `(G,T,tau)` core FAIL on common C1/C2/C3/C5 low-k block; scale-time interaction is required for faithful C5 representation.

---

## 2. Frozen response basis

Structure grid:

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`,

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

Anchored background response:

\[
r_E(z;z_*)=\ln\left[\frac{H(z)/H(z_*)}{H_{ref}(z)/H_{ref}(z_*)}\right],\qquad z_*=0.51.
\]

Gauge-safe total-matter comoving response:

\[
\delta_m=\frac{\sum_i\rho_i\delta_i}{\rho_m},\qquad
\theta_m=\frac{\sum_i(\rho_i+p_i)\theta_i}{\rho_m+p_m},
\]

\[
\Delta_m=\delta_m+3(1+w_m){\cal H}\frac{\theta_m}{k^2},
\]

\[
\boxed{r_\Delta(k,z)=\ln\frac{P_{\Delta,model}^{S}(k,z)}{P_{\Delta,ref}^{S}(k,z)}}.
\]

Never infer microscopic dimension from a raw catalog SVD. Missing response is never zero unless a theory/solver contract validates the zero.

---

## 3. Frozen family atlas

- **C0** LambdaCDM/GR origin.
- **C1** smooth non-phantom DE: one-sided `epsilon_w=1+w -> 0+`, production step `1e-4`.
- **C2** IDE `Q=H(alpha rho_idm+beta rho_iv)`: positive alpha excluded by frozen positivity history; physical coordinate is negative-alpha ray `u=-alpha>=0` plus two-sided beta line.
- **C3** GDM: pinned GDM_CLASS, `cs2/cv2` closure directions with frozen `w_gdm=0`.
- **C4** thermal WDM: separate small-scale transfer block. Do not zero-impute it into the low-k common-grid atlas.
- **C5** designer f(R): pinned H-EFTCAMB, production `B0={1e-6,1e-5,1e-4,1e-3}`.

---

## 4. Experiments 034–038 observational bridge

### Exp034 — shape proxy

Corrected ShapeFit order is `[DV/rd, DH/DM, f_sigma_s8, m+n]`. Marginal `m+n` weighting preserves the GDM cs2/cv2 degeneracy (`0.189582 deg`). The finite-node ShapeFit representation leaves about `36%` residual for GDM/f(R), so its ~`23 deg` proxy separation is **not** a DESI distinguishability claim.

### Exp035 — AP operator

For flat FLRW,

\[
F_{AP}(z)=E(z)\int_0^z\frac{dz'}{E(z')},
\]

and any multiplicative normalization of `E` cancels exactly. Therefore anchored `r_E` keeps all AP information and

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}.
\]

AP needs full history from `z=0`; never extrapolate the seven-node structure atlas below `z=0.295`.

### Exp036 — C1/C2 AP geometry

Corrected DESI marginal-whitened acute angles:

- smooth-w / IDE negative-alpha: `72.803493 deg`;
- smooth-w / IDE beta: `64.151094 deg`;
- IDE negative-alpha / beta: `9.0379006 deg` acute (`170.962099 deg` oriented).

The same IDE alpha/beta directions are `58.9338 deg` apart in full structure.

### Exp037 — C3 GDM AP exact null

Pinned C3 artifact run `32759738560`, artifact `9532247349`, upstream `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

For audited `cs2={1e-8,1e-7,1e-6}` and `cv2={1e-8,1e-7,1e-6,1e-5,1e-4}` with `w_gdm=0`, every saved background column equals the reference exactly and

\[
K_{AP}t_{cs2}=K_{AP}t_{cv2}=0.
\]

Hard run `32783243120`, result artifact `9540510596`, SHA256 `ba1fa93e348f9685d84a675311c79f9c746574463086710b4a46911d125f4edf`.

### Exp038 — C5 designer-f(R) AP exact null

Pinned upstream `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`. Frozen hard config artifact run `32759477319`, artifact `9532245261`, hard lineage `dsir_mgs1_hp_*`.

The pinned source maps `EFTwDE=0` to exact `w_DE=-1`. Experiment 038 reruns `B0={0,1e-7,1e-6,1e-5,1e-4,1e-3}` and finds every saved background/AP quantity exactly equal to the `B0=0` reference at stored solver precision. Thus

\[
\boxed{K_{AP}t_{B0}=0}
\]

for the frozen C5 B0 direction while its perturbation/structure response is nonzero.

First scientific hard run `32785800977`, artifact `9541598468`. Final transfer-preserving regression run `32786915513`, artifact `9541895055`, SHA256 `74d975790d00a04762d45bf183481f69d6fc54b84d186c63e89b88bbb9d20b16`.

**Scientific consequence:** exact background/AP channel-null structure is hard-reproduced in two qualitatively different families: GDM closure physics and designer modified gravity. This supports block-sparse influence trajectories but is not a universal law.

---

## 5. Experiment 040 — finite-bin temporal structure operator

Define for adjacent frozen early->late nodes

\[
\boxed{
\Delta\bar f_P(k)=\frac{r_\Delta(k,z_{late})-r_\Delta(k,z_{early})}{2[\ln a_{late}-\ln a_{early}]}
}.
\]

This is a theory-space temporal derivative of power response, **not tracer RSD and not ShapeFit `f_sigma_s8`**.

Hard controls pass at machine precision. Run `32785987735`, artifact `9541462864`, SHA256 `0457823510fead4ff56e8e29843e39de47805f8fbfda86f4d9d33585be556ac9`.

Key hard comparisons:

- IDE alpha/beta: AP `9.0379 deg` -> temporal growth `29.3978 deg` -> full structure `58.9338 deg`.
- smooth-w / IDE alpha: AP `72.8035 deg`, full structure `52.1943 deg`, temporal growth only `10.3106 deg`.
- IDE alpha / GDM cs2/cv2: full structure ~`24.8-24.9 deg` -> temporal growth ~`60.9 deg`.
- GDM cs2/cv2: full structure `0.3226 deg` -> temporal growth only `1.3340 deg`; metric slip remains necessary.
- GDM cs2/cv2 / f(R): leading scale-only `0.078-0.102 deg` -> temporal growth `16.05-17.28 deg` -> full structure `25.18-25.49 deg`.

**Hard interpretation:** pairwise degeneracies migrate between response operators. Joint multi-channel geometry is the correct object.

---

## 6. Experiments 039/041 — ShapeFit growth/RSD representability

The corrected ShapeFit growth coordinate is `f_sigma_s8`, with

\[
s=r_d/r_d^{ref},\qquad R=s\,8h^{-1}{\rm Mpc}.
\]

For scale-dependent density/velocity fields define

\[
{\cal D}_{RSD}=1-\frac{S_{\delta\Theta}^2}{S_{\delta\delta}S_{\Theta\Theta}}.
\]

Experiment 041 established the identity

\[
{\cal D}_{RSD}=\frac{\mathrm{Var}_w[g]}{\langle g^2\rangle_w},\qquad g=\Theta/\delta,
\]

and `CV_w(g)=sqrt(D/(1-D))`.

C5 hard run `32791510072`, artifact `9543375564`, SHA256 `1e4d86f7f13185d69a07b71afa9bfd6fefa6003119064652d6388491738212bc`.

At `kmax=0.24 h/Mpc`, representative defects are:

- GR floor ~`1.42e-10`;
- `B0=1e-6`: `5.18e-6`;
- `B0=1e-5`: `1.92e-4`;
- `B0=1e-4`: `8.81e-4`;
- `B0=1e-3`: `8.78e-4`.

Thus scalar growth compression is not exact for the frozen designer-f(R) direction. Also preserve F12: old printed CAMB growth summaries are too coarse for small-B0 tangent calibration.

---

## 7. Experiments 042/043 — GDM gauge/velocity negative chronology

The pinned GDM_CLASS synchronous transfer output is not a safe RSD velocity representation because the dark-matter velocity is gauge-fixed/ill-conditioned. The branch exposes an N-body transfer route, but pinned upstream stops because the derivative of `H_T_Nb_prime` is not propagated.

Experiment 042 therefore compared matched synchronous and Newtonian runs and required an independently reconstructed comoving matter field to agree before any velocity science was admitted.

Run `32793688546`:

- raw transfer k-grid mismatch `2.16e-11` (later recognized as a bad comparison because adaptive transfer grids can differ by gauge);
- max absolute `ln|Delta_S/Delta_N| = 2.58664e-6`, above frozen `1e-6`;
- max model/reference response difference `6.78698e-7`, within `1e-6`.

Status: `FAIL_GDM_SYNC_NEWTONIAN_DELTA_BRIDGE_V0_2`. Exploratory velocity angles and `D_RSD` from this run are **not scientific claims**.

Experiment 043 corrected the k-grid method by interpolating each gauge independently to frozen DSIR nodes and tightened only perturbation integration precision:

- p8 absolute bridge `2.51958e-6`, response bridge `6.78698e-7`;
- p10 absolute bridge `3.00625e-6`, response bridge `8.02174e-7`;
- p10/p8 absolute residual ratio `1.19316`.

Run `32794067542`, artifact `9544255453`, SHA256 `c62613798a6a6f8e9e573bb158315ca03a5c9f998805ebfc6bdda25de4d4100a`.

**Negative conclusion:** tighter perturbation precision does not explain the absolute synchronous/Newtonian mismatch. Do not loosen the gate and do not use the exploratory GDM velocity/RSD branch as validated physics yet.

---

## 8. Experiments 044/045A — BuyanovGPT table and `(G,T,tau)` core test

The chat nickname **BuyanovGPT table** now refers to `docs/BUYANOVGPT_TABLE.md`, an influence atlas, not a separate theory.

Preserve these distinctions:

- `N_repr` = dimension needed to reconstruct/approximate responses;
- `N_disc` = independent channels needed to distinguish mechanisms;
- they need not be equal;
- the black-hole/no-hair analogy is only a falsifiable organizer, not a theorem;
- the current minimum discriminator set `{slip, small-scale transfer, time/sign}` does **not** prove three fundamental parameters.

The conversational candidate `Core=(G,T,tau)` was made operational using

\[
R(z,k)=\mu+T(k)+\tau(z)+I(z,k),
\]

where `I` is the irreducible scale-time interaction.

Pre-frozen compact adequacy required >=95% core power capture for every direction and <=5 deg distortion of every pairwise acute angle. Final controlled run `32883280742`, artifact `9576600500`, SHA256 `59839a2717646e50501a949cf5b310cb6c0e55f85dd6839fce2832c704ec28dd`.

Operator controls pass:

- reconstruction error `0`;
- zero-mean residual `4.22e-21`;
- normalized core/interaction inner product `2.57e-15`.

Scientific status:

`FAIL_COMPACT_G_T_TAU_CORE_LOW_K_V0_1`.

Key interaction fractions:

- C1 smooth-w: `||I||/||R||=0.03287`, interaction power `0.108%`;
- C2 IDE alpha/beta: interaction essentially negligible (`~1e-11` power);
- C3 GDM cs2/cv2: `||I||/||R||~0.21`, interaction power `~4.4-4.5%`;
- C5 designer f(R): `||I||/||R||=0.54759`, interaction power **29.99%**, core captures only **70.01%**.

Dropping `I` changes GDM/f(R) acute angles from about `25 deg` to about `15 deg`; the largest pairwise distortion is IDE negative-alpha/f(R), `14.31 deg`.

**Hard conclusion on this block:** simple additive `(G,T,tau)` is not sufficient. **Scale-time nonseparability `I(k,z)` is a hard-required representation component for C5 and non-negligible for C3 on the frozen low-k theory block.** Do not yet call `I` a universal parameter or new fundamental degree of freedom.

C4 WDM is outside this common-grid test; its informative high-k transfer must be extended with time information before any C1-C5 complete core claim.

---

## 9. Current scientific findings to remember

Read `docs/SCIENTIFIC_FINDINGS_REGISTER.md` for authoritative status.

Newest/high-priority entries:

- **F10 HARD:** frozen designer-f(R) B0 is exactly background/AP-null but perturbation-active.
- **F11 HARD:** degeneracies migrate between AP, temporal growth, and full structure.
- **F12 LIMIT:** printed CAMB growth summaries are too coarse for small-B0 tangent calibration.
- **F13 HARD:** frozen designer-f(R) density/velocity response is not exactly scalar-growth representable.
- **F14 LIMIT/NEGATIVE (to consolidate):** GDM synchronous/Newtonian absolute comoving-density bridge remains above threshold and does not converge under p10 precision; reject exploratory velocity science.
- **F15 HARD/NEGATIVE:** the simple additive `(G,T,tau)` core fails on the common C1/C2/C3/C5 low-k block; C5 has a large scale-time interaction component.

---

## 10. Exact continuation from this checkpoint

1. Consolidate Exp042/043 negative chronology into main and close stale exploratory PRs only after preservation; never erase failures.
2. Treat `I(k,z)` scale-time nonseparability as a **candidate response signature** and test whether its shape/direction is stable across parameter steps, solver precision and families.
3. Quantify whether `I` itself separates GDM from f(R), IDE and smooth-w better than additive summaries; freeze comparison criteria before target interpretation.
4. Extend C4 WDM with physically relevant high-k **and time** support before testing whether WDM has an analogous `I(k,z)` signature.
5. Continue survey/window-aware shape and RSD forward modelling; no observation-space distinguishability claim from theory angles alone.
6. Preserve slip/lensing because GDM cs2/cv2 proves density/time compression can miss mechanism information.
7. Estimate minimal latent response dimension only after common-domain/observation operators exist; do not force the answer to 3, 4, or any chosen number.
8. Continue searching for cross-family regularities, exact nulls, degeneracy migrations, orientation/sign changes, domain-localized effects and failed compressions. These are the primary DSIR research target.
9. Build a universal model only when `docs/UNIVERSAL_MODEL_READINESS.md` criteria are satisfied and a withheld-family test is credible.
10. Resume G7 only after observationally whitened manifold/rank stability. **Never claim discovery before G8.**
