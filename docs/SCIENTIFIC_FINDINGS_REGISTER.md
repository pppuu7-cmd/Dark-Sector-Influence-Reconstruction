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

Different microscopic directions can become almost collinear after one observation operator while remaining well separated after another. The degeneracy therefore belongs to the pair `(physical direction, observation operator)`, not to the microscopic models alone.

Schematic statement:

\[
K_i\,t_A \simeq K_i\,t_B,\qquad K_j\,t_A \not\simeq K_j\,t_B.
\]

Current hard examples:

1. GDM `cs2` versus `cv2`: low-k matter-power angle `0.322616 deg`; DESI `m+n` proxy after marginal covariance weighting `0.189582 deg`, while metric slip gives `137.943212 deg` oriented and an equalized two-block angle `56.963212 deg`.
2. GDM versus designer f(R): leading scale-mode angles only `0.07813/0.10169 deg`, but time modes differ by about `25.18/25.49 deg` and full physical rays have opposite orientation around `154.82/154.51 deg`.
3. WDM: essentially blind in the frozen low-k block but strongly visible in the separate small-scale transfer block (`r_T(0.1)=-3.46e-6`, `r_T(10)=-0.10375` for the 3 keV control).

**Interpretation:** model identity is not expected to be carried by one response shape alone; complementary influence channels are required.

**Revisit if:** a future family-complete observational projection makes these separators disappear, or if solver/systematic audits overturn any hard pairwise result.

## F2 — density-shape compression can erase microphysical distinctions

**Status: HARD ESTABLISHED for GDM `cs2/cv2` in the current low-k and ShapeFit-proxy blocks.**

The GDM pressure and viscosity directions are nearly identical in low-k matter-power response, and real DESI DR1 `m+n` marginal weighting does not resolve the degeneracy. Metric slip does.

**Interpretation:** the density field can retain the net suppression of growth while losing information about whether that suppression arose from effective pressure or viscosity; metric-potential relations retain substantially more of that distinction.

**Boundary:** this is not a statement about every survey or every nonlinear scale.

## F3 — scale shape alone is insufficient for separating GDM-like suppression from designer f(R)

**Status: HARD ESTABLISHED at theory-response level; observational distinguishability still PARTIAL.**

GDM and designer f(R) have almost identical leading scale modes in the frozen low-k response atlas, yet their time/sign evolution separates them strongly.

**Interpretation:** a useful classifier must retain at least `(k,z,sign/orientation)` information rather than compressing a response to a scale-only template.

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

## F6 — IDE interaction directions appear nearly degenerate in AP geometry while being separated in structure

**Status: PRELIMINARY pending Experiment 036 hard CI.**

Using the exact frozen C1/C2 full-background artifacts and the validated AP operator, the current extraction gives for IDE negative-alpha versus beta an approximately antiparallel AP response with DESI `DH/DM` marginally whitened acute angle near `9.04 deg`, while their frozen structure-block angle is about `58.93 deg`.

Other preliminary AP angles are smooth-w versus IDE negative-alpha near `72.80 deg` acute, and smooth-w versus IDE beta near `64.15 deg`.

**Interpretation if hard-confirmed:** background geometry alone cannot identify the IDE interaction mechanism; growth/structure provides complementary information. This would be another independent example of F1.

**Do not promote until:** Experiment 036 hard run passes with the pre-frozen convergence thresholds and exact pinned input histories.

## F7 — current hard discriminator graph requires complementary channel types

**Status: HARD ESTABLISHED for the current frozen evidence graph only.**

Experiment 033 gives the unique minimum hitting set

\[
\{\text{metric slip},\;\text{small-scale transfer},\;\text{time/sign evolution}\}.
\]

**Interpretation:** the current family set cannot be robustly discriminated by repeatedly measuring one class of observable more precisely; qualitatively different influence channels are required.

**Boundary:** this is not a universal optimal survey design and must be recomputed as observational kernels/families are added.

## F8 — emerging DSIR meta-hypothesis: model identity is a multi-channel influence trajectory

**Status: SUPPORTED HYPOTHESIS, not a law.**

The repeated pattern across GDM, f(R), WDM, and preliminarily IDE suggests that the useful model identifier is not a single response function but the trajectory of the residual source through several observation operators:

\[
\theta_{micro}\rightarrow X_{\mu\nu}\rightarrow\{K_1X,K_2X,\ldots\}.
\]

A stronger future formulation would require showing that the joint observational map consistently restores distinctions that individual blocks lose, under family-prior, covariance, solver-precision, and channel-removal stress tests.

**Falsification tests:**

- family-complete AP+growth+shape whitening fails to restore known structure distinctions;
- discriminant graph becomes unstable under modest solver/covariance perturbations;
- new families produce unresolved degeneracies across all proposed independent channels;
- local manifold/rank behavior is dominated by arbitrary family sampling or compression choices.

## Iteration protocol for this register

At every substantive iteration:

1. Re-evaluate all entries directly touched by the new result.
2. Change status rather than silently rewriting history.
3. Preserve negative results and failed approximations.
4. Add exact experiment/run/artifact provenance once hard-frozen.
5. Distinguish theory-space separation from survey-level distinguishability.
6. Never infer intrinsic rank, a residual law, or discovery from descriptive singular spectra or selected pairwise angles.
7. Mirror any material change into `RECOVERY_LATEST.md`, `STATUS.md`, the dated research log, and gate files when a gate changes.
