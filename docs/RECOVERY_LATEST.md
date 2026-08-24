# DSIR RECOVERY LATEST — live per-iteration overlay

**Date:** 2026-08-25  
**Stable manual:** `docs/RECOVERY_MANUAL.md`  
**Scientific findings:** `docs/SCIENTIFIC_FINDINGS_REGISTER.md`  
**Current status:** `docs/STATUS.md`  
**Gates:** `docs/GATES.md`  
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

Latest hard chronology:

- Exp034 run `32777716140` — ShapeFit `m+n` marginal whitening proxy PASS.
- Exp035 run `32778635058` — exact calibration-free AP operator PASS.
- Exp036 run `32782545098` — C1/C2 production AP geometry PASS.
- Exp037 run `32783243120` — GDM C3 AP-zero audit PASS.
- Exp038 run `32785800977` — designer-f(R) C5 AP-zero audit PASS.
- Exp040 run `32785987735` — finite-bin theory growth operator PASS.

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
- **C4** thermal WDM: separate small-scale transfer block.
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

The pinned source maps `EFTwDE=0` to exact `w_DE=-1`. Experiment 038 reruns

`B0={0,1e-7,1e-6,1e-5,1e-4,1e-3}`

and finds for every point:

- redshift-grid mismatch `0`;
- maximum relative `H` response `0`;
- maximum relative `D_M` response `0`;
- maximum `|Delta ln(D_H/D_M)| = 0`;
- all saved numerical background columns exactly equal to `B0=0` at stored solver precision.

Thus

\[
\boxed{K_{AP}t_{B0}=0}
\]

for the frozen C5 B0 direction, while its previously validated perturbation/structure response is nonzero.

Hard run `32785800977`, result artifact `9541598468`, SHA256 `24b7fa5951c06d4cea72e6c0bf6baad2d2174f2d86794ec0818cf57c309b81c8`.

**Scientific consequence:** exact background/AP channel-null structure is now hard-reproduced in two qualitatively different families: GDM closure physics and designer modified gravity. This supports block-sparse influence trajectories but is not a universal law because both are frozen constructions with fixed background contracts.

---

## 5. Experiment 040 — finite-bin temporal structure operator

Define for adjacent frozen early->late nodes

\[
\boxed{
\Delta\bar f_P(k)=\frac{r_\Delta(k,z_{late})-r_\Delta(k,z_{early})}{2[\ln a_{late}-\ln a_{early}]}
}.
\]

This is a theory-space temporal derivative of power response, **not tracer RSD and not ShapeFit `f_sigma_s8`**.

Hard controls were frozen before looking at pair angles and pass:

- endpoint reconstruction `1.1102230246251565e-16`;
- constant-mode residual `0`;
- linearity residual `9.769962616701378e-15`.

Run `32785987735`, artifact `9541462864`, SHA256 `0457823510fead4ff56e8e29843e39de47805f8fbfda86f4d9d33585be556ac9`.

Key hard comparisons:

- IDE alpha/beta: AP `9.0379 deg` -> temporal growth `29.3978 deg` -> full structure `58.9338 deg`.
- smooth-w / IDE alpha: AP `72.8035 deg`, full structure `52.1943 deg`, temporal growth only `10.3106 deg`.
- IDE alpha / GDM cs2/cv2: full structure ~`24.8-24.9 deg` -> temporal growth ~`60.9 deg`.
- GDM cs2/cv2: full structure `0.3226 deg` -> temporal growth only `1.3340 deg`; metric slip remains necessary.
- GDM cs2/cv2 / f(R): leading scale-only `0.078-0.102 deg` -> temporal growth `16.05-17.28 deg` -> full structure `25.18-25.49 deg`.

**Hard interpretation:** pairwise degeneracies migrate between response operators. Adding a new channel does not monotonically make every pair more distinguishable; it can separate one pair and collapse another. Joint multi-channel geometry is therefore the correct object.

---

## 6. Experiment 039 — ShapeFit growth/RSD contract

The corrected ShapeFit growth coordinate is **`f_sigma_s8`**, not naive fixed-radius textbook `f sigma8`.

Use

\[
s=r_d/r_d^{ref},\qquad R=s\,8h^{-1}{\rm Mpc}.
\]

Before compressing scale-dependent growth into one scalar, test density/velocity representability. Planned diagnostic:

\[
{\cal D}_{RSD}=1-\frac{S_{\delta\Theta}^2}{S_{\delta\delta}S_{\Theta\Theta}}.
\]

If this is non-negligible, a single scalar `f_sigma_s8` is not an adequate representation and a survey/window-aware anisotropic RSD operator is required.

Pinned CAMB exposes machine-readable transfer variables including `delta_tot`, `v_newtonian_cdm`, and `v_newtonian_baryon`, allowing a proper high-precision density/velocity bridge.

### Hard negative/limit result

Do **not** derive the small-B0 C5 growth tangent from old printed H-EFTCAMB logs. They print `sigma8` and `sigma8^2_vd/sigma8` only to roughly four decimals; at `B0=1e-7` rounding quantizes away most of the signal and produces artificial sparse/unstable derivatives. This output representation is rejected for tangent calibration.

---

## 7. Current scientific findings to remember

Read `docs/SCIENTIFIC_FINDINGS_REGISTER.md` for the authoritative statuses. Newest entries include:

- **F10 HARD:** frozen designer-f(R) B0 is exactly background/AP-null but perturbation-active.
- **F11 HARD for frozen examples:** degeneracies migrate between AP, temporal growth, and full structure.
- **F12 LIMIT:** printed CAMB growth summaries are too coarse for small-B0 tangent calibration.

Earlier hard findings F1–F9 remain active unless explicitly marked superseded.

---

## 8. Exact continuation from this checkpoint

1. Extend Experiment 039 to a numerical high-precision density/velocity representability test. Never use the rounded CAMB summary logs for small-B0 derivatives.
2. Preserve C5 H-EFTCAMB `transfer_filename` products from the same pinned hard configurations; use the transfer variables to build density and velocity moments.
3. Define and validate a total-matter/tracer velocity convention before mixing CDM and baryon Newtonian-gauge velocities. Do not silently equate solver-specific velocity variables.
4. For C3 GDM and C2 IDE, launch matched pinned-solver transfer-output runs with the same total-matter/gauge contract.
5. Apply the ShapeFit smoothing-radius convention `R=s*8 h^-1 Mpc`, calculate the density/velocity moments and `D_RSD`, and only then decide whether scalar `f_sigma_s8` is admissible family by family.
6. Replace/calibrate the finite-node `m+n` proxy with a survey/window-aware shape operator or propagate compression-model error.
7. Form the full corrected ShapeFit block `Z=C^{-1/2} Delta O` only after geometry+growth+shape operators are validated on common observable coordinates.
8. Freeze null/rank thresholds before inspecting the resulting whitened spectrum; stress-test family prior `pi`, within-family sampling, covariance, solver precision, and channel removal.
9. Continue observational slip/lensing and WDM small-scale transfer layers in parallel because Exp033 identifies them as independent discriminators.
10. Resume G7 residual-law search only after observationally whitened manifold/rank stability. **Never claim discovery before G8.**
