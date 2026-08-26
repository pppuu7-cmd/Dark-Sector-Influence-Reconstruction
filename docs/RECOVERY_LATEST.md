# DSIR RECOVERY LATEST — live overlay

**Date:** 2026-08-26  
**Base main entering this overlay:** `502af6dc9789665d373868536ff5282af8d446bf`  
**Stable historical manual:** `docs/RECOVERY_MANUAL.md`  
**Current detailed overlay:** `docs/RECOVERY_POST_EXP067E_2026-08-26.md`  
**Current next protocol:** `experiments/068a_act_unwise_physical_forward_reproduction_v0_1.md`

DSIR is independent of RTK. Preserve negative results and preregistration chronology. Missing response is never zero. No universal-model, law, intrinsic-rank, no-hair or discovery claim is currently allowed.

## Current top-level state

- G1 PASS v0.1.1 — conservation/gauge contract.
- G2 PASS v0.1.1 — response basis/cross-solver bridge.
- G3A PASS — background atlas.
- G3B PASS block-aware — beyond-background atlas; WDM remains high-k masked rather than zero-padded.
- G4 PASS — synthetic rank recovery.
- G5 PARTIAL — family-complete observation-space robustness remains incomplete.
- G6A/G6B PASS — DESI AP + corrected ShapeFit layers.
- **G7 OPEN.** No nontrivial observational residual relation has yet survived the full frozen requirements.
- **G8 OPEN.** Withheld-family evidence exists, but no frozen G7 law has yet survived a fresh G8 test.
- **G9 OPEN.**

## Immutable late-stage scientific chronology

1. **F27 / Exp054C — HARD PROSPECTIVE FAIL.** The raw full-response `R^2` scale-centroid source-response slope calibrated on C3+C5 failed on withheld C7 IDM–DR; all four adjacent slopes had the wrong sign.
2. **F28 / Exp055A — RETROSPECTIVE candidate only.** Endpoint-normalized `u=1/2` crossing gave positive source-response slopes on C3/C5/C7.
3. **F29 / Exp056B — HARD PROSPECTIVE FAIL.** Fresh C8 IDM–photon broke that endpoint-half-transition sign relation; no retuning is allowed.
4. **F30 / Exp061A — HARD PROSPECTIVE PASS.** A preregistered two-coordinate localization+shape/orientation path survived genuinely withheld C9 IDM–baryon, including leave-one-redshift rebuilds. This supports a multicoordinate representation but is not a G7 law.
5. **F31 / Exp064A — HARD NEGATIVE.** The eligible DESI ShapeFit `(AP,G,m+n)` common-plane relation was statistically nontriviality-null (`p_lambda≈0.265`, `p_LOO≈0.361`); do not retune or rescue it.

## ACT DR6 × unWISE bridge status

- Exp065A: permanent FAIL for the naive unselected 236×236 covariance.
- Exp065B: PASS for the exact official selected 26×26 covariance in order `[Blue gg6, Blue kg7, Green gg6, Green kg7]`.
- Exp066A: PASS solver-neutral raw no-CLEFT projector algebra with independent `P_WW,P_Wm,P_mm`.
- Exp066B: permanent FAIL of the cheap constant-mode white-noise shortcut.
- Exp066C: PASS exact survey-only shot-noise template from `C x = w2 1`.
- Exp067A: PASS exact selected covariance whitening, no repair.

Frozen Exp067A whitener binding:

- covariance SHA256 `df7e285c40009e0ba20cc5d920342e1066ceff69d277fdf3233ac63463ffddb9`;
- Cholesky `L` SHA256 `6a30b1792d8b3f29ae66102dadb285f394f6aa4c30cba29dc3c3234a1897f109`;
- whitener `W` SHA256 `b32e59a98b6910427ac5026bc3f882ea8b0934b65de9abe44c599e1c7ec66822`.

## CAMB ↔ CLASS physical convention status

Correct Weyl power variable:

\[
W=k^2(\phi+\psi)/2.
\]

Exp067B remains a permanent hard FAIL because its preregistered raw-CAMB rank-one coherence threshold `5e-8` was below the pinned CAMB numerical floor, even though all three CAMB↔CLASS power comparisons passed at about 0.9%.

Exp067C localized the `~1.6e-7` coherence defect to native CAMB powers. Exp067D causally reproduced it from float32-first multiplication of stored transfer values; promoting the same values to float64 before multiplication removes the rank-one defect to reported machine precision.

Exp067E then prospectively tested the corrected physical convention on fresh LambdaCDM references R1/R2 and returned

`PASS_CAMB_CLASS_OUT_OF_SAMPLE_POWER_CONVENTION_V0_1`.

Do not reclassify Exp067B; Exp067D explains it and Exp067E supplies a separate prospective certification.

## Exact current next barrier — Exp068A

Before any nuisance quotient or G7 fit, run the preregistered physical ACT×unWISE forward reproduction:

- pinned CAMB R0 linear `P_WW,P_Wm,P_mm`;
- released Blue/Green xmatch, xcorr and PCA redshift kernels;
- exact pinned upstream no-CLEFT raw projector versus `src/dsir/act_unwise_projection.py`;
- full `ell=0..6143` input support;
- `0<=z<=3`, projector `kmax=10 Mpc^-1`, common Gauss-Legendre order 96;
- inherited component tolerance `5e-13*max(1,max|reference|)`;
- no CLEFT, no ACT fit, no dark-sector family, no law search.

Allowed immutable outcomes:

`PASS_ACT_UNWISE_PHYSICAL_FORWARD_REPRODUCTION_V0_1`

or

`FAIL_ACT_UNWISE_PHYSICAL_FORWARD_REPRODUCTION_V0_1`.

If FAIL, diagnose separately and keep the nuisance quotient blocked. If PASS, only then preregister the selected 26D nuisance tangent quotient.

## Future quotient design — not yet executed

Candidate structure after Exp068A PASS:

\[
J_\eta=\partial d/\partial\eta,\qquad A=WJ_\eta,
\]

\[
A=U_\eta\Sigma_\eta V_\eta^T,
\]

\[
Q=I-U_{\eta,r}U_{\eta,r}^T.
\]

The candidate nuisance inventory currently contains at most 18 named Blue+Green directions, but the effective nuisance rank **must not be assumed to be 18**. Freeze the SVD rank rule before fitting any G7 relation.

## Recovery order

1. `docs/RECOVERY_MANUAL.md` — detailed history/derivations through F26.
2. `docs/RECOVERY_POST_EXP067E_2026-08-26.md` — F27–F31 and Exp065–067E chronology plus formulas.
3. newest `docs/RESEARCH_CHECKPOINT_*` file.
4. current numbered experiment protocol/result.

Known archival gap: standalone `experiments/042...` and `043...` files are absent from the current tree, but their negative GDM velocity/RSD validation conclusion is preserved in the manual. Do not invent missing details.
