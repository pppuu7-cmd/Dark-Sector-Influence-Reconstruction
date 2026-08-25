# DSIR scientific findings register

**Live document.** Update on every iteration that adds, strengthens, limits, supersedes, or falsifies a scientific interpretation.  
**Preserved previous full register:** `docs/SCIENTIFIC_FINDINGS_REGISTER_PRE_EXP045A_2026-08-25.md`.  
**Recovery:** `docs/RECOVERY_MANUAL.md`, `docs/RECOVERY_LATEST.md`.  
**Influence atlas:** `docs/BUYANOVGPT_TABLE.md`.

DSIR is a reconstruction/meta-inference framework, not a fundamental theory. Nothing below is a discovery or a new law unless future gates establish that status.

## Status vocabulary

- **HARD ESTABLISHED** — reproduced by a frozen hard workflow or exact validated identity, restricted to the stated domain.
- **SUPPORTED / PARTIAL** — backed by validated calculations but missing a major observation/family/robustness layer.
- **PRELIMINARY** — motivated or numerically indicated before confirmatory hard validation.
- **LIMIT / NEGATIVE RESULT** — demonstrated limitation, failed approximation, degeneracy, no-go, or validation failure in a stated domain.
- **SUPERSEDED / RETRACTED** — later evidence materially invalidated an earlier interpretation; never delete the chronology.

---

## F1 — observational degeneracy/nullity is channel-dependent

**Status: HARD ESTABLISHED for current frozen examples; broader principle SUPPORTED.**

The relevant object is `(physical direction, response/observation operator)`. A direction can be almost collinear with another, or exactly null, in one channel and separated in another:

\[
K_i t_A\simeq K_i t_B,\quad K_j t_A\not\simeq K_j t_B,
\]

or

\[
K_i t_A=0,\quad K_j t_A\neq0.
\]

Hard examples include GDM cs2/cv2 density-vs-slip, GDM/f(R) scale-vs-time/full structure, WDM low-k-vs-high-k, IDE AP-vs-structure, and the exact AP nulls of frozen GDM and designer f(R).

**Interpretation:** model identity is a multi-channel influence trajectory, not one scalar response.

---

## F2 — density-shape compression can erase GDM pressure/viscosity microphysics

**Status: HARD ESTABLISHED for frozen C3 low-k/ShapeFit-proxy blocks.**

GDM cs2/cv2:

- low-k matter-power acute angle `0.322616 deg`;
- DESI `m+n` marginal-whitened proxy `0.189582 deg`;
- finite-bin temporal response `1.334013 deg`;
- metric-slip oriented angle `137.943212 deg` and equalized two-block acute `56.963212 deg`.

**Interpretation:** density/time retains net growth suppression while losing much of the pressure-vs-viscosity mechanism information; slip retains it.

---

## F3 — scale-only shape is insufficient for GDM versus designer f(R)

**Status: HARD ESTABLISHED at theory-response level; observational distinguishability PARTIAL.**

GDM/f(R):

- leading scale-only `0.078-0.102 deg`;
- temporal response `16.05-17.28 deg`;
- full `(k,z)` structure `25.18-25.49 deg`.

Experiment 045A further sharpens this: removing irreducible scale-time interaction collapses the GDM/f(R) angle to about `14.8-14.9 deg`.

**Interpretation:** the separator is not merely “scale + time”; the coupling of scale and time itself carries information.

---

## F4 — compressed ShapeFit `m+n` is not a universal shape operator

**Status: LIMIT / NEGATIVE RESULT, HARD.**

The finite-node ShapeFit proxy leaves roughly `36%` relative representation residual for GDM cs2, GDM cv2 and designer f(R). Therefore proxy angles are not DESI distinguishability claims. A survey/window-aware shape operator or explicit compression-model error is required.

---

## F5 — AP geometry is exactly insensitive to expansion normalization anchor

**Status: HARD ESTABLISHED analytic + numerical identity (Exp035).**

\[
F_{AP}(z)=E(z)\int_0^z\frac{dz'}{E(z')},
\]

so multiplicative normalization cancels, and

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}.
\]

Numerical bridge errors are `~1e-14`. Production AP must use full history from `z=0`; never extrapolate the seven-node structure grid below `z=0.295`.

---

## F6 — IDE interaction directions are AP-degenerate but structure-separated

**Status: HARD ESTABLISHED for frozen local C2 directions.**

IDE negative-alpha/beta:

- AP acute `9.0379006 deg`;
- temporal response `29.3978236 deg`;
- full structure `58.9337977 deg`.

Time restores part, but not all, of the mechanism information lost by AP.

---

## F7 — current hard discriminator graph needs complementary channel types

**Status: HARD ESTABLISHED for the current frozen evidence graph only.**

Unique minimum hitting set from Exp033:

\[
\{\text{metric slip},\;\text{small-scale transfer},\;\text{time/sign evolution}\}.
\]

This is not a universal survey design and **not proof of three fundamental dark-sector parameters**. Recompute as families/operators expand.

---

## F8 — model identity as a block-sparse multi-channel influence trajectory

**Status: SUPPORTED HYPOTHESIS, not a law.**

Repeated results support

\[
\theta_{micro}\rightarrow X_{\mu\nu}\rightarrow\{K_1X,K_2X,\ldots\},
\]

with exact null blocks possible. Exp037/038 give two qualitatively different background/AP-null but perturbation-active examples; Exp040 shows degeneracy migration; Exp041 shows geometry-null yet density/velocity-compression-active C5.

---

## F9 — frozen GDM cs2/cv2 are exactly background/AP-null but perturbation-active

**Status: HARD ESTABLISHED for sampled C3 `w_gdm=0` manifold (Exp037).**

For audited cs2/cv2 variants, all saved background columns and AP responses equal reference at stored solver precision:

\[
K_{AP}t_{cs2}=K_{AP}t_{cv2}=0.
\]

Run `32783243120`, artifact `9540510596`, SHA256 `ba1fa93e348f9685d84a675311c79f9c746574463086710b4a46911d125f4edf`.

Boundary: not arbitrary GDM with nonzero/time-dependent `w_gdm`.

---

## F10 — frozen designer-f(R) B0 is exactly background/AP-null but perturbation-active

**Status: HARD ESTABLISHED for sampled high-precision C5 manifold (Exp038).**

For `B0={0,1e-7,1e-6,1e-5,1e-4,1e-3}` on the designer `EFTwDE=0` branch, saved background/AP quantities are exactly reference at stored solver precision:

\[
K_{AP}t_{B0}=0.
\]

Final regression run `32786915513`, artifact `9541895055`, SHA256 `74d975790d00a04762d45bf183481f69d6fc54b84d186c63e89b88bbb9d20b16`.

Boundary: this is specific to the frozen designer construction, not arbitrary f(R)/MG.

---

## F11 — degeneracies migrate between AP, temporal response and full structure

**Status: HARD ESTABLISHED for frozen pairwise examples (Exp040); broader principle SUPPORTED.**

Examples:

- smooth-w/IDE-alpha: AP `72.80 deg`, temporal `10.31 deg`, structure `52.19 deg`;
- IDE-alpha/GDM: structure `~24.8-24.9 deg`, temporal `~60.9 deg`;
- GDM cs2/cv2: structure `0.3226 deg`, temporal `1.3340 deg`;
- GDM/f(R): scale-only `~0.1 deg`, temporal `16-17 deg`, full `25 deg`.

**Interpretation:** no single globally best scalar channel; an operator can separate one pair and collapse another.

---

## F12 — printed CAMB growth summaries are inadequate for small-B0 tangent calibration

**Status: LIMIT / NEGATIVE RESULT for frozen C5 logs.**

H-EFTCAMB text logs print `sigma8` and `sigma8^2_vd/sigma8` to only about four decimals. Small-B0 differences are quantized away and finite-difference tangents become artificial. Use machine-readable high-precision transfer/cross-power products instead.

---

## F13 — frozen designer-f(R) density/velocity response is not exactly scalar-growth representable

**Status: HARD ESTABLISHED (Exp041).**

Define

\[
{\cal D}_{RSD}=1-\frac{S_{\delta\Theta}^2}{S_{\delta\delta}S_{\Theta\Theta}}
=\frac{\mathrm{Var}_w[g]}{\langle g^2\rangle_w},\qquad g=\Theta/\delta.
\]

At `kmax=0.24 h/Mpc`:

- GR floor `~1.42e-10`;
- B0 `1e-6`: `5.18e-6`;
- `1e-5`: `1.92e-4`;
- `1e-4`: `8.81e-4`;
- `1e-3`: `8.78e-4`.

Run `32791510072`, artifact `9543375564`, SHA256 `1e4d86f7f13185d69a07b71afa9bfd6fefa6003119064652d6388491738212bc`.

**Interpretation:** one scalar `f_sigma_s8`-like amplitude is not an exact representation for this scale-dependent C5 response.

---

## F14 — current pinned GDM Newtonian velocity/RSD route is not validated by the synchronous/Newtonian density bridge

**Status: LIMIT / NEGATIVE RESULT, HARD for Exp042/043 validation tests.**

Chronology:

1. synchronous GDM velocity is gauge-ill-conditioned for RSD;
2. pinned built-in N-body transfer route stops upstream because `H_T_Nb_prime` derivative is not propagated;
3. Exp042 matched synchronous/Newtonian runs and, after a parser-only 16-vs-15-column fix, found max absolute comoving-density bridge residual `2.58664e-6` > frozen `1e-6`, while model/reference response difference was `6.78698e-7` < `1e-6`;
4. Exp043 independently interpolated each gauge to frozen nodes and tightened perturbation precision only.

Exp043:

- p8 absolute bridge `2.51958e-6`, response bridge `6.78698e-7`;
- p10 absolute bridge `3.00625e-6`, response bridge `8.02174e-7`;
- p10/p8 absolute residual ratio `1.19316`.

Run `32794067542`, artifact `9544255453`, SHA256 `c62613798a6a6f8e9e573bb158315ca03a5c9f998805ebfc6bdda25de4d4100a`.

**Hard negative conclusion:** tighter perturbation precision does not explain the absolute mismatch. Do not loosen the gate. Exp042 GDM velocity angles and `D_RSD` remain exploratory and must not be used as validated physics.

---

## F15 — simple additive `(G,T,tau)` core is insufficient; scale-time nonseparability carries material response information

**Status: LIMIT / NEGATIVE RESULT, HARD on common C1/C2/C3/C5 frozen low-k theory block (Exp045A).**

The chat proposed a candidate core organized by global growth/amplitude `G`, scale-only `T`, and time-only `tau`. Exp045A made this testable via

\[
\boxed{R(z,k)=\mu+T(k)+\tau(z)+I(z,k)},
\]

with orthogonal irreducible scale-time interaction `I`.

Pre-frozen compact adequacy required >=95% core power capture for every direction and <=5 deg pairwise-angle distortion.

Final controlled run `32883280742`, artifact `9576600500`, SHA256 `59839a2717646e50501a949cf5b310cb6c0e55f85dd6839fce2832c704ec28dd`.

Operator controls pass:

- reconstruction error `0`;
- zero-mean residual `4.22e-21`;
- normalized core/I inner product `2.57e-15`.

Scientific status:

`FAIL_COMPACT_G_T_TAU_CORE_LOW_K_V0_1`.

Interaction structure:

- C1 smooth-w: interaction power `0.108%`;
- C2 IDE alpha/beta: interaction power essentially negligible (`~1e-11`);
- C3 GDM cs2/cv2: interaction power `4.53% / 4.36%`;
- C5 designer f(R): interaction power **29.99%**, so additive core captures only **70.01%**.

Dropping `I` changes GDM/f(R) acute angles from `25.18/25.49 deg` to `14.77/14.93 deg`; maximum pairwise distortion is IDE-alpha/f(R), **14.31 deg**.

**Hard interpretation:** the simple additive three-type core is falsified on this block. For frozen C5, and to a lesser extent C3, **how scale dependence evolves with time is itself information that cannot be reconstructed by separate scale-only and time-only summaries.**

**New hypothesis, not yet a law:** `I(k,z)` may be a useful mechanism-sensitive response signature. Do not yet call it a universal parameter/hair or infer `N_repr=4`.

**Boundary:** C4 WDM is not in this common low-k matrix; family-complete testing requires a high-k time-dependent atlas and no zero imputation.

---

## F16 — pairwise model separation can be localized in irreducible scale-time interaction

**Status: HARD ESTABLISHED descriptive response geometry for the frozen C1/C2/C3/C5 low-k block (Exp046); broader mechanism principle SUPPORTED.**

Experiment 046 defines

\[
\chi_I=\frac{\|I\|^2}{\|R\|^2}
\]

for individual directions and, after response normalization and acute-orientation alignment,

\[
\boxed{\eta_I(A,B)=\frac{\|d_I\|^2}{\|d\|^2}},
\qquad
\|d\|^2=\|d_C\|^2+\|d_I\|^2.
\]

Thus `eta_I` is an exact orthogonal decomposition of **pairwise normalized shape-separation power** into additive-core and scale-time-interaction pieces.

Hard provenance:

- run `32884761188`;
- artifact `9577142860`;
- artifact SHA256 `6e2c7026efe17a81bee10c9a9904c78f5299dce1bf594535be5ded600a3d2834`;
- source head `d292cb90245c3e472dcbffd076947181fd6ed7cf`.

Controls pass:

- max unit-norm error `5.42e-20`;
- max core/interaction orthogonality residual `1.01e-14`;
- max pairwise Pythagorean residual `3.25e-19`;
- max acute-angle/chord residual `4.76e-15`.

Key `eta_I` values:

- GDM cs2/cv2: **`0.731139`**;
- GDM cv2/f(R): **`0.613829`**;
- GDM cs2/f(R): **`0.611982`**;
- IDE-alpha/f(R): **`0.571946`**;
- IDE-beta/f(R): `0.305340`;
- smooth-w/f(R): `0.280354`;
- IDE-alpha/GDM cs2/cv2: `0.243027 / 0.236822`;
- IDE alpha/beta: `1.49e-11`.

Valid interaction-shape acute angles:

- GDM cs2/cv2: `0.742556 deg`;
- GDM cs2/f(R): `10.985703 deg`;
- GDM cv2/f(R): `11.710540 deg`;
- smooth-w versus GDM/f(R): approximately `69.6-70.0 deg`.

**Hard interpretation:** for GDM/f(R), roughly **61% of their normalized low-k structure-shape separation power resides specifically in scale-time nonseparability**, so the previously observed temporal/full-structure separation is substantially a joint `k x z` effect rather than a sum of independent scale-only and time-only summaries.

**Hard negative refinement:** a large `eta_I` is not the same as large distinguishability. GDM cs2/cv2 have `eta_I=0.731` but a total acute angle only `0.323 deg`; interaction carries most of a tiny difference and their interaction shapes are themselves almost collinear (`0.743 deg`). Metric slip therefore remains the demonstrated microphysical separator.

**Supported mechanism pattern:** the pair `(interaction strength chi_I, interaction morphology)` may classify response mechanisms more usefully than a single interaction amplitude, but this must survive tangent-step, solver-precision, domain, observational-kernel and withheld-family tests.

**Boundary:** `eta_I` is not S/N, likelihood significance, Bayes evidence or survey distinguishability. C4 remains excluded by domain contract. No intrinsic-rank, universal fourth parameter, no-hair theorem, G7 law or discovery claim follows.

---

## F17 — scale-time interaction hierarchy survives every single-node deletion

**Status: HARD ESTABLISHED descriptive grid robustness on the frozen C1/C2/C3/C5 low-k theory-response atlas (Exp047B); broader mechanism interpretation SUPPORTED only.**

Experiment 047B recomputes the decomposition and pairwise interaction localization on exactly twelve deterministic reduced grids: five leave-one-k-out and seven leave-one-z-out variants. No scientific drift threshold was applied post hoc.

Hard provenance:

- run `32894616114`;
- source head `9a05c451401ac2cede3a56ef4ca2a1923eecb9c3`;
- artifact `9580724793`;
- artifact SHA256 `948038245e4eeea9ca569a48e138f5bdddaede19f0ff98ea941fc91a00272bb7`.

Controls pass:

- reconstruction error `0`;
- max core/I orthogonality `8.3946e-14`;
- max pairwise Pythagorean residual `2.3505e-17`;
- frozen ceiling `1e-12`.

### Direction-level robustness

The descriptive ordering

\[
\boxed{\text{IDE near-null}<\text{smooth-w}<\text{GDM}<f(R)}
\]

is preserved in **12/12** single-node deletions. Both IDE directions remain below the existing `chi_I=1e-6` morphology floor in **12/12** reduced grids.

Leave-one-node ranges:

- IDE alpha `1.99e-13 .. 7.36e-11`;
- IDE beta `3.66e-13 .. 7.45e-11`;
- smooth-w `3.91e-5 .. 1.34e-3`;
- GDM cs2 `0.0279 .. 0.0525`;
- GDM cv2 `0.0265 .. 0.0505`;
- designer f(R) `0.2233 .. 0.3497`.

### Pairwise robustness

GDM cs2/f(R):

\[
\eta_I=0.5504..0.6539,
\]

GDM cv2/f(R):

\[
\eta_I=0.5520..0.6554.
\]

Thus every single-node deletion keeps more than half of the normalized GDM/f(R) response-shape separation power in irreducible scale-time interaction. This is descriptive hard robustness, not a preregistered `eta_I>0.5` gate.

### Hard limitation

Smooth-w's absolute interaction magnitude is not grid-insensitive. Removing `k=0.001 h/Mpc` changes

\[
\chi_I=1.0805\times10^{-3}\rightarrow3.9123\times10^{-5},
\]

a factor `0.0362` of the full-grid value. Therefore its **tier** is robust, but its precise `chi_I` is not yet a stable family invariant.

GDM cs2/cv2 keep `eta_I=0.6525..0.7377`, but their total response distance remains tiny; interaction still does not replace metric slip.

**Supported interpretation:** on the current low-k response domain, GDM closure physics and designer modified gravity exhibit persistent scale-time coupling qualitatively stronger than the local IDE directions, and GDM/f(R) separation remains substantially encoded in joint `k x z` evolution rather than a single special node.

**Boundary:** this is internal grid robustness, not independent-data confirmation, survey distinguishability, intrinsic rank, a universal mechanism law, a fourth parameter, no-hair theorem, G7 law or discovery. C4 remains excluded by domain contract.

Detailed standalone record: `docs/SCIENTIFIC_FINDING_F17_INTERACTION_GRID_ROBUSTNESS.md`.

---

## Research discipline after F17

1. Keep `N_repr` distinct from `N_disc`.
2. Never interpret `eta_I` without the total pair distance/angle; report both.
3. Treat current `chi_I` primarily as a mechanism-tier descriptor; smooth-w demonstrates that precise magnitudes can be node/domain sensitive.
4. Next test parameter-amplitude/finite-step stability of `chi_I` and interaction morphology using independent manifold points where available.
5. Add C4 only after a high-k `(k,z)` time-dependent response atlas exists; never insert low-k zero.
6. Preserve slip/lensing because interaction morphology does not resolve GDM pressure/viscosity.
7. Continue observation-space window/covariance projection before detectability claims.
8. Continue cross-family null-space, channel-migration, orientation/sign, localization and failed-compression searches.
9. No G7 law and no G8 discovery claim yet.

<!-- DSIR_EXP049B_DOC_SYNC_2026_08_26 -->
## F18 — finite-amplitude interaction hierarchy persists while response manifolds curve

**Status: HARD ESTABLISHED descriptive finite-manifold result on sampled C1/C2/C3/C5 low-k rays (Exp047A); broader classification only SUPPORTED.**

Across every retained finite amplitude in Exp047A the sampled interaction-power classes remain non-overlapping in the order

\[
\boxed{\mathrm{IDE}<\mathrm{smooth\mbox{-}w}<\mathrm{GDM}<f(R)}.
\]

At the same time GDM-viscosity and designer-\(f(R)\) response/interaction directions rotate with amplitude. Therefore `chi_I` is **not** a constant model label and tangent dimension must remain distinct from finite-manifold linear span and curvature.

Standalone record: `docs/SCIENTIFIC_FINDING_F18_FINITE_INTERACTION_MANIFOLD.md`.

---

## F19 — interaction-energy localization has complementary scale and time geometry

**Status: HARD ESTABLISHED descriptive operator result for frozen C1/C3/C5 low-k directions (Exp048A).**

For

\[
q_k(k)=\frac{\sum_z I^2}{\|I\|^2},\qquad q_z(z)=\frac{\sum_k I^2}{\|I\|^2},
\]

GDM and designer-\(f(R)\) are almost identical in scale localization (`q_k` angle `0.040-0.051 deg`) but separated in time localization (`20.15-21.52 deg`). Smooth-w and \(f(R)\) show the complementary pattern: `q_z` angle `1.93 deg`, `q_k` angle `79.37 deg`.

GDM cs2/cv2 remain almost degenerate in localization (`q_k=0.0113 deg`, `q_z=1.382 deg`), so metric slip remains the validated microphysical separator.

Standalone record: `docs/SCIENTIFIC_FINDING_F19_INTERACTION_LOCALIZATION_GEOMETRY.md`.

---

## F20 — finite-amplitude GDM viscosity and designer-f(R) localization migrates toward lower k, but temporal flow is not universal

**Status: HARD ESTABLISHED descriptive finite-manifold result (Exp048B); physical window-crossing explanation was initially SUPPORTED only.**

GDM viscosity moves from `k_I_geo≈0.05099` to `0.04063 h/Mpc` as `cv2` grows `1e-8 -> 1e-4`; designer-f(R) moves `0.05109 -> 0.03994 h/Mpc` over `B0=1e-6 -> 1e-3`. Their time centroids differ qualitatively: GDM is nearly monotone upward, whereas f(R) is non-monotone.

Thus a common scale-migration pattern does not imply a universal time trajectory. Exp049B below supplies the first withheld test of the GDM scale-migration interpretation.

Standalone record: `docs/SCIENTIFIC_FINDING_F20_FINITE_LOCALIZATION_FLOW.md`.

---

## F21 — GDM interaction localization follows the pre-frozen window-crossing direction on withheld intermediate amplitudes

**Status: HARD ESTABLISHED for the Exp049B C3 withheld interpolation test; broader physical-window principle SUPPORTED/PARTIAL.**

Before generating any intermediate outputs, Exp049B froze the dynamic-shear quasi-steady proxy

\[
\boxed{k_{v,\mathrm{QS}}=\sqrt{9/8}\,\mathcal H/\sqrt{c_v^2}}
\]

and a single directional prediction on the new grid `cv2={1.5e-5,2e-5,3e-5,5e-5,7e-5}`: once this proxy has entered `k<=0.1 h/Mpc`, the interaction-energy centroid must be non-increasing with increasing `cv2`, allowing only `1e-6 h/Mpc` positive numerical drift.

Run `32904158849` passed. Artifact `9584180621`, SHA256 `892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a`.

Source-derived proxy at fixed `z=1.317`:

`0.084846, 0.073479, 0.059995, 0.046472, 0.039276 h/Mpc`.

Withheld measured localization:

`0.050174, 0.049835, 0.049046, 0.047046, 0.044604 h/Mpc`.

All four measured steps are negative:

`-3.397e-4, -7.890e-4, -2.000e-3, -2.441e-3 h/Mpc`.

Operator controls are clean: reconstruction `0`, core/interaction orthogonality `2.43e-19`, zero-mean residual `7.07e-21`, profile-normalization residual `2.17e-19` against the frozen `1e-12` ceiling.

**Hard interpretation:** the previously observed GDM viscosity scale-localization migration survives a genuinely withheld intermediate-amplitude test in the direction predicted by source-derived window penetration.

**Boundary:** this does not prove `k_v_QS` is the exact viscosity eigenmode scale, does not yet validate the same principle for designer-f(R), does not establish a universal dark-sector law, and does not close G7 or G8.

Standalone record: `docs/SCIENTIFIC_FINDING_F21_GDM_WINDOW_CROSSING_VALIDATION.md`.

---

## Research discipline after F21

1. Treat F21 as independent support for a C3 window-crossing mechanism, not a universal law.
2. Keep `k_v_QS` explicitly labelled quasi-steady until an eigenmode/closure derivation is validated.
3. Use Exp049A exact designer-B diagnostics as the next cross-mechanism test; a mismatch must be retained as a negative result.
4. Do not infer a common temporal trajectory from the scale result.
5. G7 and G8 remain open; universal-model construction remains premature.

<!-- EXP049A_F22_SYNC_2026-08-26 -->
## F22 — source-native transition scales track interaction-localization migration

**Status: source-scale extraction HARD ESTABLISHED for frozen C3/C5; cross-family window-crossing interpretation SUPPORTED / PARTIAL.**

Exp049A derives characteristic scales from pinned solver equations rather than fitting them to localization. For frozen GDM,
\[k_s=\mathcal H/\sqrt{c_s^2},\qquad k_{v,QS}=\sqrt{9/8}\,\mathcal H/\sqrt{c_v^2},\]
where the viscosity expression is explicitly a quasi-steady proxy, not an exact eigenmode scale. For pinned designer f(R), EFTCAMB's exact B definition and diagnostic `B(a),f_R,R/H0^2,E,E',E''` give the inverse Compton scale through
\[\frac{1+f_R}{3f_{RR}H_0^2}=\frac{(R/H_0^2)'}{3B(H'/H)}.\]

Hard provenance: run `32904376001`, artifact `9584346604`, SHA256 `6a2c7f4e072fe7ee5d3a125bd798e975ab7031f5e7e92f3c71b47dbe71856f22`; max terminal B0 relative error `8.75255e-9` versus frozen `1e-6` control.

Observed ordering: GDM pressure stays outside the low-k window and `k_I^geo` stays near `0.051`; dynamic shear enters around `cv2~1e-5` and localization migrates downward. Designer f(R) similarly has `k_C` outside the window for `B0=1e-6,1e-5`, entering on the frozen z range by `1e-4`, with `k_I^geo` moving from `0.0510862` to `0.0399397` by `B0=1e-3`.

The GDM ordering now has an independent withheld confirmation (Exp049B/F21). The f(R) ordering remains retrospective until Exp049C. No universal law, G7 closure, field count, or detectability claim follows. Standalone record: `docs/SCIENTIFIC_FINDING_F22_PHYSICAL_TRANSITION_SCALE_BRIDGE.md`.

<!-- F23_FR_WINDOW_CROSSING_SYNC_2026-08-26 -->
## F23 — withheld designer-f(R) validation extends the finite-window prediction to a second mechanism

**Status: HARD ESTABLISHED for the frozen Exp049C test; two-family predictive support HARD for the tested GDM/f(R) rays; broader universality SUPPORTED / PARTIAL only.**

Exp049C froze five previously uncomputed designer-f(R) amplitudes before solver output,

\[
B_0=\{1.5,2,3,5,7\}\times10^{-4},
\]

and predicted only

\[
k_I^{geo}(B_{0,i+1})-k_I^{geo}(B_{0,i})\le10^{-6}\;h/{\rm Mpc}.
\]

Run `32907619613`, artifact `9585579947`, SHA256 `bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942` passed source eligibility, operator controls and the scientific prediction.

Withheld `k_I^geo` values are

`0.0480162, 0.0472514, 0.0459188, 0.0437628, 0.0420339 h/Mpc`,

with consecutive steps

`-7.6481e-4, -1.33256e-3, -2.15603e-3, -1.72888e-3 h/Mpc`.

Minimum exact frozen-z inverse-Compton scales decrease simultaneously from `0.0573747` to `0.0265600 h/Mpc`. Maximum terminal B0 relative error is `7.50777e-11`; all operator residuals are below `5.7e-20` versus the frozen `1e-12` algebraic ceiling.

Combined with GDM Exp049B/F21, the same directional finite-window statement has now survived two independently frozen interpolation tests in physically distinct mechanisms. This is **not** a universal function, a dark-sector theorem, a field count, a no-hair result, G7 closure, G8 discovery, or survey detectability.

Standalone record: `docs/SCIENTIFIC_FINDING_F23_FR_WINDOW_CROSSING_VALIDATION.md`.

