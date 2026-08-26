# DSIR recovery checkpoint — Exp055A / F28

Date: 2026-08-26

## Restore point

Base main after F27: `ca9a8a6852a8a349f4d4d598927ec78f99cf10bd`.

Exp055A branch: `research/exp055a-endpoint-half-transition-retrospective-v0-1`.

Analysis run `32921449255`; artifact `9589960526`; SHA256 `bb737e4cb290923b08faab6ac77d16ef95e1357115791d779e92a8ae454743d2`.

Exp055A consumes immutable C3/C5/C7 response artifacts only and generates no new theory response.

## Why Exp055A exists

Exp054C/F27 prospectively falsified the raw full-response `R^2` centroid candidate because C7 IDM-DR is almost scale-only and increasing suppression amplitude drives the centroid toward the hard `k=0.1 h/Mpc` boundary.

The replacement candidate must therefore locate **shape transition** after removing additive offset and multiplicative response amplitude/sign.

## Candidate operator

At each redshift,

\[
u(z,k)=\frac{R(z,k)-R(z,k_{min})}{R(z,k_{max})-R(z,k_{min})}.
\]

Require finite nonzero endpoint contrast and exactly one `u=1/2` crossing. Interpolate crossing linearly in `ln k`.

Then

\[
k_{50}^{geo}=\exp\left[\frac1{N_z}\sum_z\ln k_{50}(z)\right],
\qquad
C_{50}=\frac{\Delta\ln k_{50}^{geo}}{\Delta\ln k_*}.
\]

Retrospective candidate relation:

\[
\boxed{C_{50}>0}.
\]

No common magnitude band is supported or allowed from this experiment.

## Exact result

- unique crossings: `105/105`;
- all 12 adjacent slopes across C3/C5/C7 positive;
- all 21 family x leave-one-z sign checks positive;
- C3 C50 `0.012508..0.059539`;
- C5 C50 `0.028747..0.065922`;
- C7 C50 `0.126966..0.391654`;
- all 35 C7 rows are nonmonotone, yet each has one unique half-transition crossing.

Therefore the candidate is qualified for a **future preregistration**, not validated as a law.

## Gate state

- Exp054C/F27 remains permanent HARD FAIL.
- G7 remains OPEN.
- G8 remains OPEN.
- G9 remains OPEN.
- C7 is no longer eligible as withheld evidence for this candidate.

## Exact continuation

1. Select a genuinely fresh scale-transition mechanism C8 using source equations only; do not inspect its response first.
2. Prefer a mechanism implemented independently enough to test transfer of the operator, not a trivial reparameterization of C7.
3. Freeze C8 background, source-native `k_*`, coupling grid, response k/z grid, endpoint-half-transition operator, unique-crossing validity condition, and `C50>0` sign criterion **before first C8 P(k,z)**.
4. Generate matched reference and C8 responses only after the preregistration commit exists.
5. A prospective FAIL must be preserved without changing the operator or sign rule.
6. A prospective PASS would provide the first withheld support for the F28 common relation, but claim scope must still be assessed before any G7/G8 wording is upgraded.
7. Continue independent block-aware observation-space/discriminant work; one scalar transition coordinate does not replace multi-channel DSIR geometry.

Promising C8 source families in pinned official CLASS include IDM-baryon scattering (`cross_idm_b`, `n_index_idm_b`) and IDM-photon scattering (`u_idm_g`/`cross_idm_g`, `n_index_idm_g`). They must be audited at source level before one is chosen.
