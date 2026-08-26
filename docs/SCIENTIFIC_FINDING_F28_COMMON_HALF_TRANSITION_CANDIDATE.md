# F28 — endpoint-normalized half-transition is a viable common candidate coordinate

Date: 2026-08-26  
Experiment: Exp055A  
Status: **SUPPORTED / RETROSPECTIVE CANDIDATE; NOT A G7/G8 VALIDATION**

## Context

F27 prospectively falsified the Exp054A raw full-response `R^2` centroid slope on C7 IDM-DR. The failure was not hidden or recalibrated away: the C7 response became increasingly dominated by the upper frozen k endpoint while its source-native transition moved downward.

That failure suggested separating response **shape/transition location** from additive and multiplicative response amplitude. Because this idea was formulated after C7 was seen, Exp055A treats C7 as ordinary retrospective calibration/diagnostic data.

## Common operator

At each redshift,

\[
u(z,k)=\frac{R(z,k)-R(z,k_{min})}{R(z,k_{max})-R(z,k_{min})}.
\]

The response transition `k50(z)` is the unique piecewise-log-k crossing of `u=1/2`; the seven-redshift scalar is

\[
k_{50}^{geo}=\exp\left[\frac{1}{7}\sum_z\ln k_{50}(z)\right].
\]

For adjacent source-scale points,

\[
C_{50}=\frac{\Delta\ln k_{50}^{geo}}{\Delta\ln k_*}.
\]

The retrospective candidate is only the sign relation `C50>0`. No common magnitude band is claimed.

## Immutable-input run

Exp055A generated no new theory response. It consumed only:

- C3 GDM Exp049B run `32904158849`, artifact `9584180621`;
- C5 designer-f(R) Exp049C run `32907619613`, artifact `9585579947`;
- C7 IDM-DR Exp054C run `32920776596`, artifact `9589768992`.

Analysis run:

- run `32921449255`;
- PR checkout SHA `4194c3c6efa18d8fb6a0ef581e3993ba5670cb35`;
- analysis branch head `3f31235b9fefb3ddf173f4f5da31916dbb08f7c8`;
- artifact `9589960526`;
- artifact SHA256 `bb737e4cb290923b08faab6ac77d16ef95e1357115791d779e92a8ae454743d2`.

## Result

All **105/105** family/amplitude/redshift rows have finite non-zero endpoint contrast and exactly one `u=1/2` crossing.

C3 GDM:

- `k50_geo = {0.05128353,0.05119135,0.05099082,0.05053544,0.05003177} h/Mpc`;
- `C50 = {0.0125083,0.0193601,0.0351225,0.0595389}`.

C5 designer-f(R):

- `k50_geo = {0.05082760,0.05061787,0.05023963,0.04959446,0.04904751} h/Mpc`;
- `C50 = {0.0287471,0.0369973,0.0506064,0.0659218}`.

C7 IDM-DR:

- `k50_geo = {0.06872866,0.06496381,0.06115403,0.05818873,0.05695898} h/Mpc`;
- `C50 = {0.391654,0.298100,0.194603,0.126966}`.

Every adjacent slope is positive.

## Redshift-node robustness

The sign survives all seven leave-one-redshift-out recomputations in every family:

- C3 leave-one-z `C50` range: `0.0115118 .. 0.0642912`;
- C5: `0.0220791 .. 0.0752787`;
- C7: `0.126958 .. 0.391682`.

Thus all 21 family-by-deletion tests preserve the candidate sign.

## Important morphology refinement

All 35 C7 response rows are non-monotone across the full five-node k grid, whereas C3/C5 rows are monotone. Nevertheless, every C7 row has exactly one half-transition crossing.

Therefore a future operator contract should require a **unique half-transition crossing**, not global monotonicity. This avoids rejecting physically useful profiles that contain a low-k shoulder/enhancement before the main high-k transition.

## Scientific interpretation

1. The F27 failure was specific to the raw squared-response centroid; it does not imply that no common source-linked transition coordinate exists.
2. Endpoint-affine normalization is a promising way to remove arbitrary offset and response amplitude before locating the transition.
3. The sign relation `C50>0` is much more portable across the three already-seen mechanisms than a common slope magnitude. C7 slopes are much larger than C3/C5 slopes, so no universal numerical coefficient is supported.
4. This is a **candidate qualification result only**. Since C7 motivated the operator, C7 cannot serve as withheld confirmation.
5. G7 remains OPEN. G8 remains OPEN.
6. The next decisive experiment must freeze this operator and sign criterion before any response from a genuinely fresh scale-transition mechanism/family is inspected.
7. No action reconstruction, intrinsic field count, universal-model parameter, observational detectability or discovery claim follows.
