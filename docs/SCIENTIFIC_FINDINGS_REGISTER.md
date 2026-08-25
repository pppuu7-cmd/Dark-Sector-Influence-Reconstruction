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

## Research discipline after F16

1. Keep `N_repr` distinct from `N_disc`.
2. Never interpret `eta_I` without the total pair distance/angle; report both.
3. Test `chi_I` and interaction morphology across parameter step, solver precision and grid/domain changes before calling them stable mechanism coordinates.
4. Add C4 only after a high-k `(k,z)` response atlas exists.
5. Preserve slip/lensing because interaction morphology does not resolve GDM pressure/viscosity.
6. Continue observation-space window/covariance projection before detectability claims.
7. Continue cross-family null-space, channel-migration, orientation/sign, localization and failed-compression searches.
8. No G7 law and no G8 discovery claim yet.
