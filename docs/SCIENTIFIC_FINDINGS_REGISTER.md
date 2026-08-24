# DSIR scientific findings register

**Live document.** Update this file on every research iteration that adds, strengthens, limits, supersedes, or falsifies a scientific interpretation. Technical recovery remains in `RECOVERY_MANUAL.md` and `RECOVERY_LATEST.md`; this register preserves the evolving scientific meaning of the calculations.

DSIR is a reconstruction/meta-inference framework, not a fundamental theory. Nothing below is a discovery or a new law of nature unless future gates explicitly establish that status.

## Status vocabulary

- **HARD ESTABLISHED** — reproduced by a frozen hard workflow or exact validated identity; claim is restricted to the stated response basis/model set.
- **SUPPORTED / PARTIAL** — backed by validated calculations, but an important observation operator, covariance block, family, or robustness layer is still missing.
- **PRELIMINARY** — numerically extracted or analytically motivated before the corresponding frozen hard run is complete.
- **LIMIT / NEGATIVE RESULT** — a demonstrated limitation, degeneracy, failed approximation, or no-go within a stated domain.
- **SUPERSEDED / RETRACTED** — later evidence invalidated or materially changed the earlier interpretation. Do not delete the old entry; preserve chronology and link the replacement.

## F1 — observational degeneracy is channel-dependent

**Status: HARD ESTABLISHED for the current frozen examples; broader principle SUPPORTED, not universal.**

Different microscopic directions can become almost collinear—or exactly null—after one observation operator while remaining well separated after another. The degeneracy/null space therefore belongs to the pair `(physical direction, observation operator)`, not to the microscopic models alone.

Schematic statement:

\[
K_i\,t_A \simeq K_i\,t_B,\qquad K_j\,t_A \not\simeq K_j\,t_B,
\]

with the stronger channel-null possibility

\[
K_i\,t_A=0,\qquad K_j\,t_A\neq0.
\]

Current hard examples:

1. GDM `cs2` versus `cv2`: low-k matter-power angle `0.322616 deg`; DESI `m+n` proxy after marginal covariance weighting `0.189582 deg`, while metric slip gives `137.943212 deg` oriented and an equalized two-block angle `56.963212 deg`.
2. GDM versus designer f(R): leading scale-mode angles only `0.07813/0.10169 deg`; finite-bin temporal-growth angles are `16.052/17.284 deg` acute; full frozen `(k,z)` structure gives about `25.18/25.49 deg` acute with opposite orientation near `155 deg`.
3. WDM: essentially blind in the frozen low-k block but strongly visible in the separate small-scale transfer block (`r_T(0.1)=-3.46e-6`, `r_T(10)=-0.10375` for the 3 keV control).
4. IDE negative-alpha versus beta: AP acute angle `9.0379006 deg`, finite-bin temporal-growth angle `29.3978236 deg`, full frozen structure angle `58.9337977 deg`.
5. GDM `cs2/cv2` with frozen `w_gdm=0`: Experiment 037 gives exactly zero saved-solver background/AP response while the same directions are nonzero in perturbation channels.
6. Designer f(R) `B0`: Experiment 038 gives exactly zero saved-solver background/AP response over `B0=0..1e-3` on the source-proven `EFTwDE=0` LCDM background branch, while the frozen structure response is nonzero.
7. Smooth-w versus IDE negative-alpha: AP separates them strongly (`72.803493 deg` acute), whereas the finite-bin temporal-growth operator collapses them to `10.310585 deg` acute.

**Interpretation:** model identity is not expected to be carried by one response shape alone; complementary influence channels are required. Some physical directions can lie in the exact null space of an entire channel, and the location of pairwise degeneracies can migrate when the observation/response operator changes.

**Revisit if:** a future family-complete observational projection makes these separators disappear, or if solver/systematic audits overturn any hard pairwise/null result.

## F2 — density-shape compression can erase microphysical distinctions

**Status: HARD ESTABLISHED for GDM `cs2/cv2` in the current low-k and ShapeFit-proxy blocks.**

The GDM pressure and viscosity directions are nearly identical in low-k matter-power response, and real DESI DR1 `m+n` marginal weighting does not resolve the degeneracy. Metric slip does.

Experiment 040 adds a temporal test: their finite-bin growth angle rises from `0.322616 deg` to `1.334013 deg`, but this remains a strong degeneracy. Time evolution helps weakly and does not replace metric slip.

**Interpretation:** the density field can retain the net suppression of growth while losing information about whether that suppression arose from effective pressure or viscosity; metric-potential relations retain substantially more of that distinction.

**Boundary:** this is not a statement about every survey or every nonlinear scale.

## F3 — scale shape alone is insufficient for separating GDM-like suppression from designer f(R)

**Status: HARD ESTABLISHED at theory-response level; observational distinguishability still PARTIAL.**

GDM and designer f(R) have almost identical leading scale modes in the frozen low-k response atlas (`0.078-0.102 deg`). Experiment 040 isolates their temporal response and finds `16.052 deg` (GDM cs2/fR) and `17.284 deg` (GDM cv2/fR) acute finite-bin growth angles. Full frozen `(k,z)` structure is more separating still, around `25.18-25.49 deg` acute.

**Interpretation:** a useful classifier must retain `(k,z,sign/orientation)` information rather than compressing a response to a scale-only template. Temporal information is a genuine separator, but growth-only compression still loses information relative to the full structure history.

**Observation-space caution:** Experiment 034 finds about `23 deg` whitened `m+n` proxy separation, but the finite-node ShapeFit representation leaves roughly `36%` relative residual for GDM and f(R). Therefore this is not a DESI distinguishability claim.

## F4 — compressed ShapeFit `m+n` is not an adequate universal operator for strongly scale-dependent new physics

**Status: LIMIT / NEGATIVE RESULT, HARD.**

The frozen finite-node ShapeFit-basis proxy has small/acceptable residuals for smooth-w and IDE directions, but roughly `36%` relative L2 residual for GDM `cs2`, GDM `cv2`, and designer f(R) over the full frozen `0.001-0.1 h/Mpc` range.

**Consequence:** absence of an anomaly in a small set of compressed shape parameters cannot automatically be interpreted as absence of an anomalous full shape. A survey/window-aware response or explicit compression-model error is required before full observational claims.

## F5 — AP geometry is exactly insensitive to the arbitrary normalization of the anchored expansion response

**Status: HARD ESTABLISHED analytic + numerical identity (Experiment 035).**

For flat FLRW,

\[
F_{AP}(z)=E(z)\int_0^z\frac{dz'}{E(z')}.
\]

If `E_model=A E_ref exp(r_E)`, the constant factor `A` cancels exactly. Therefore anchoring the DSIR expansion response at `z*=0.51` removes no AP information. The ShapeFit geometry response is

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}.
\]

Hard numerical bridge errors are at the `1e-14` level.

**Production requirement discovered:** AP depends on the full history from `z=0`; the seven-node structure atlas beginning at `z=0.295` must never be extrapolated to zero for production AP work.

## F6 — IDE interaction directions are nearly degenerate in AP geometry while being separated in structure

**Status: HARD ESTABLISHED for the C2 local directions; refined by Experiment 040.**

Experiment 036 gives corrected DESI DR1 `DH/DM` marginal geometry:

- IDE negative-alpha versus beta: `170.9620994 deg` oriented, `9.0379006 deg` acute;
- smooth-w versus IDE negative-alpha: `72.8034931 deg` acute;
- smooth-w versus IDE beta: `64.1510936 deg` acute.

Experiment 040 then gives IDE alpha/beta finite-bin temporal-growth separation `29.3978236 deg` acute, while the frozen full structure angle is `58.9337977 deg`.

Thus temporal structure restores part of the mechanism information lost in AP but not all of the complete `(k,z)` structure information.

Hard Exp036 provenance: run `32782545098`, artifact ID `9540273287`, SHA256 `553faa2ef7ddbc44e25ddd6faca237d0be7fc265b9c23cfafb2a32570534d126`.

Hard Exp040 provenance: run `32785987735`, artifact ID `9541462864`, SHA256 `0457823510fead4ff56e8e29843e39de47805f8fbfda86f4d9d33585be556ac9`.

**Boundary:** these are local tangent/cone and theory-response statements, not parameter significance or a full likelihood.

## F7 — current hard discriminator graph requires complementary channel types

**Status: HARD ESTABLISHED for the current frozen evidence graph only.**

Experiment 033 gives the unique minimum hitting set

\[
\{\text{metric slip},\;\text{small-scale transfer},\;\text{time/sign evolution}\}.
\]

Experiment 040 strengthens the rationale: temporal evolution can be highly informative for some pairs but leaves the GDM cs2/cv2 microphysical degeneracy almost intact, so qualitatively independent metric information remains necessary.

**Boundary:** this is not a universal optimal survey design and must be recomputed as observational kernels/families are added.

## F8 — emerging DSIR meta-hypothesis: model identity is a multi-channel influence trajectory

**Status: SUPPORTED HYPOTHESIS, not a law.**

The repeated hard pattern across GDM, f(R), WDM, and IDE suggests that the useful model identifier is not a single response function but the trajectory of the residual source through several observation operators:

\[
\theta_{micro}\rightarrow X_{\mu\nu}\rightarrow\{K_1X,K_2X,\ldots\}.
\]

Experiments 037 and 038 sharpen this: the trajectory can be **block-sparse**, with an exactly zero coordinate in background/AP and a substantial response in perturbation channels in two qualitatively different families. Experiment 040 further shows that pairwise degeneracies can migrate between projections of the same physical directions.

Thus absence of a geometry response does not imply proximity to the common physical origin in the full response space, and a pair that is well separated in one channel can be nearly degenerate in another.

A stronger future formulation requires showing that the joint observational map consistently restores distinctions that individual blocks lose, under family-prior, covariance, solver-precision, and channel-removal stress tests.

**Falsification tests:**

- family-complete AP+growth+shape whitening fails to restore known structure distinctions;
- discriminant graph becomes unstable under modest solver/covariance perturbations;
- new families produce unresolved degeneracies across all proposed independent channels;
- local manifold/rank behavior is dominated by arbitrary family sampling or compression choices.

## F9 — frozen GDM pressure/viscosity directions are exactly background/AP-null but perturbation-active

**Status: HARD ESTABLISHED for the sampled C3 `w_gdm=0` manifold (Experiment 037).**

Experiment 037 reuses the exact immutable GDM_CLASS artifact that generated the frozen C3 manifold. It audits `cs2={1e-8,1e-7,1e-6}` and `cv2={1e-8,1e-7,1e-6,1e-5,1e-4}`, verifying `w_gdm=0` and the other closure direction zero.

For every audited variant the saved background table is exactly equal to the reference, `max_relative_H=0`, and the validated AP operator returns `Delta ln(D_H/D_M)=0` at all five DESI target redshifts.

Pre-frozen hard tolerances were `1e-12`; hard provenance: run `32783243120`, artifact ID `9540510596`, SHA256 `ba1fa93e348f9685d84a675311c79f9c746574463086710b4a46911d125f4edf`.

**Interpretation:** within this frozen GDM manifold, `cs2/cv2` are pure perturbation-channel directions with respect to background/AP.

**Boundary:** this does not apply to arbitrary GDM histories with nonzero/time-dependent `w_gdm`.

## F10 — frozen designer-f(R) B0 is exactly background/AP-null but perturbation-active

**Status: HARD ESTABLISHED for the sampled high-precision C5 manifold (Experiment 038).**

The pinned H-EFTCAMB source maps `EFTwDE=0` to an exact `w_DE=-1` parametrization. Experiment 038 reruns the immutable hard C5 configurations

`B0={0,1e-7,1e-6,1e-5,1e-4,1e-3}`

and compares their full saved background tables on the same designer branch.

For every audited `B0`:

- redshift grid mismatch `0`;
- `max_relative_H=0`;
- `max_relative_DM_nonzero_rows=0`;
- `max_abs Delta ln(D_H/D_M)=0`;
- every saved numerical background column is exactly equal to `B0=0` at saved solver precision.

These exact zeros are stronger than the pre-frozen `1e-8` tolerances. Hard provenance: run `32785800977`, artifact ID `9541598468`, SHA256 `24b7fa5951c06d4cea72e6c0bf6baad2d2174f2d86794ec0818cf57c309b81c8`.

**Interpretation:** the frozen C5 `B0` direction is a second hard example of an exact background/AP null with a nonzero perturbation response, now in modified gravity rather than a dark-fluid closure family.

**Boundary:** this does not imply arbitrary f(R) or modified-gravity models have LCDM backgrounds; it follows from this specific designer `EFTwDE=0` construction.

## F11 — degeneracies migrate between AP, temporal growth, and full structure

**Status: HARD ESTABLISHED for the frozen pairwise examples in Experiment 040; broader principle SUPPORTED.**

Experiment 040 applies a finite-bin temporal operator

\[
\Delta\bar f_P=\frac{r_\Delta(late)-r_\Delta(early)}{2\Delta\ln a}
\]

to the already frozen low-k structure atlas. Operator controls pass at machine precision and no pairwise angle was used as a hard threshold.

The same temporal projection has opposite effects on different pairs:

- smooth-w vs IDE negative-alpha: full structure `52.1943 deg` -> temporal growth `10.3106 deg`, while AP is `72.8035 deg`;
- IDE negative-alpha vs GDM cs2/cv2: full structure about `24.8-24.9 deg` -> temporal growth about `60.9 deg`;
- IDE negative-alpha vs beta: AP `9.0379 deg` -> temporal growth `29.3978 deg` -> full structure `58.9338 deg`;
- GDM cs2/cv2: structure `0.3226 deg` -> temporal growth only `1.3340 deg`, still strongly degenerate;
- GDM cs2/cv2 vs designer f(R): scale-only `0.078-0.102 deg` -> temporal growth `16.05-17.28 deg` -> full structure `25.18-25.49 deg`.

**Interpretation:** adding a channel does not monotonically make every model pair more distinct. An operator can expose one mechanism contrast while erasing another. This motivates joint multi-channel geometry rather than selecting a single globally 'best' scalar observable.

**Boundary:** Experiment 040 is theory-response temporal structure, not tracer RSD or ShapeFit `f_sigma_s8`; observational distinguishability still requires the validated density-velocity/window/covariance operator.

## F12 — printed CAMB growth summaries are inadequate for small-B0 tangent calibration

**Status: LIMIT / NEGATIVE RESULT for the current frozen C5 logs.**

The frozen C5 H-EFTCAMB logs print `sigma8` and `sigma8^2_vd/sigma8` only to roughly four decimal places. At `B0=1e-7` this rounding makes most redshift values identical to the reference even when larger-B0 runs show a smooth nonzero perturbation trend. Finite-difference tangents inferred from these printed values are therefore dominated by quantization/rounding artifacts.

**Consequence:** DSIR will not use those text logs for the small-B0 growth tangent or for an RSD representability claim. Experiment 039 must use high-precision machine-readable density/velocity transfer or cross-power outputs. Pinned CAMB exposes `delta_tot`, `v_newtonian_cdm`, and `v_newtonian_baryon` transfer variables, so a proper numerical bridge is feasible.

This is a methodological failure of an output representation, not a failure of the underlying C5 solver/model.

## Iteration protocol for this register

At every substantive iteration:

1. Re-evaluate all entries directly touched by the new result.
2. Change status rather than silently rewriting history.
3. Preserve negative results and failed approximations.
4. Add exact experiment/run/artifact provenance once hard-frozen.
5. Distinguish theory-space separation from survey-level distinguishability.
6. Never infer intrinsic rank, a residual law, or discovery from descriptive singular spectra or selected pairwise angles.
7. Mirror any material change into `RECOVERY_LATEST.md`, `STATUS.md`, the dated research log, and gate files when a gate changes.
