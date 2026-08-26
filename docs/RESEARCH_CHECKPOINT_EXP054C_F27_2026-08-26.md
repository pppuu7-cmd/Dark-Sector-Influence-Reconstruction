# DSIR recovery checkpoint — Exp054C / F27

Date: 2026-08-26

This checkpoint is additive. It does not delete or rewrite earlier recovery chronology.

## Restore point

Repository: `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`

Pre-Exp054C main: `74e052d1050ace6ad9e0257f87a143bb0f3f3900`.

Exp054C branch: `research/exp054c-idm-dr-common-slope-v0-1`.

Scientific preregistration committed **before first C7 response**:

`1df523f02a549dccc9b7bb11cb608922546b56c1`

First science-evaluable C7 run:

- Actions run `32920776596`;
- source head `304383093968107a114494d312efacd78890e49a`;
- PR checkout merge SHA `5a1f34d2e6813e450331ab2b7c194bbb000f0996`;
- artifact `9589768992`;
- SHA256 `fa61a7ae5d53550fd9bf057a4354f8f343e74c18f93a4ce23d5ed964f6dc4c2a`;
- pinned CLASS `e85808324f51fc694d12e3ed7439552a3c3f9540`.

The initial failed infrastructure run generated no C7 response. The science-evaluable run generated all requested C7 spectra before the frozen evaluator returned failure.

## Frozen Exp054C relation

The source-native C7 scale is set by

\[
\Gamma_{idm\leftarrow idr}(z_*)=\mathcal H(z_*),
\qquad k_*=\mathcal H(z_*)/h,
\]

with pinned CLASS

\[
\Gamma_{idm\leftarrow idr}(z)=\frac43\omega_{idr}a_{idm-dr}(1+z)
\left(\frac{1+z}{10^7}\right)^4.
\]

Frozen source targets:

`k_*={0.0848458299,0.0734786441,0.0599950616,0.0464719749,0.0392759873} h/Mpc`.

Frozen response operator:

\[
R(z,k)=\ln[P_{C7}(k,z)/P_{ref}(k,z)],
\]

\[
q_k^R=\frac{\sum_zR^2}{\sum_{z,k}R^2},
\qquad
k_R^{geo}=\exp\sum_kq_k^R\ln k,
\]

\[
\mathcal C_i=\frac{\Delta\ln k_R^{geo}}{\Delta\ln k_*}.
\]

Frozen C3+C5 acceptance band from Exp054A:

`0.0022992620786061375 <= C_i <= 0.09951219222831723`.

No post-output widening or sign change is allowed.

## Hard outcome

Measured C7 centroids:

`k_R^geo={0.0662753445,0.0808926726,0.0926336064,0.0979643755,0.0991509796} h/Mpc`.

Adjacent slopes:

`C={-1.3855941363,-0.6685100505,-0.2190645818,-0.07156512047}`.

All four fail by sign and lie outside the frozen band.

**Permanent result:** `FAIL_IDM_DR_COMMON_SOURCE_RESPONSE_SLOPE_V0_1`.

## What is falsified

Falsified: the Exp054A v0.1 claim that the same raw full-response `R^2` centroid has a positive, C3/C5-calibrated logarithmic source-response slope on withheld C7 IDM-DR.

Not falsified:

- the DSIR residual/source formalism;
- the broader characteristic-scale/epoch organizing idea;
- F21 GDM, F23 designer-f(R), F25 WDM, F26 DCDM mechanism-specific/withheld results;
- block-aware multi-channel response geometry.

G7 remains OPEN. G8 remains OPEN. G9 remains OPEN.

## Post-gate mechanism diagnosis

The C7 response becomes dominated by the upper frozen node:

`q_R(k=0.1)={0.6923,0.8417,0.9432,0.9850,0.9939}`.

Orthogonal additive decomposition

\[
R=\mu+T(k)+\tau(z)+I(k,z)
\]

gives

`chi_I={1.475e-8,7.555e-9,2.745e-9,7.882e-10,3.653e-10}`.

So C7 is nearly scale-only on this domain. Raw `R^2` centroid is therefore an amplitude/endpoint-dominated statistic here rather than a clean moving transition coordinate.

A descriptive endpoint-normalized half-transition operator,

\[
u(z,k)=\frac{R(z,k)-R(z,k_{min})}{R(z,k_{max})-R(z,k_{min})},
\]

with unique `u=1/2` crossing gives

`k50={0.0687286641,0.0649638121,0.0611540268,0.0581887269,0.0569589830} h/Mpc`,

and positive C7 adjacent log-slopes `{0.39165,0.29810,0.19460,0.12697}`.

This is **post-gate descriptive evidence only**. It cannot rescue Exp054C and C7 can no longer be used as the unseen withheld mechanism for a relation chosen from this observation.

## Exact continuation after restore

1. Preserve Exp054C/F27 as a permanent negative result.
2. Retrospectively evaluate one common endpoint-normalized half-transition `k50` definition on immutable C3 GDM, C5 designer-f(R), and C7 IDM-DR products; report uniqueness/domain failures explicitly.
3. If that retrospective operator is coherent, preregister a fresh relation **before** new response outputs.
4. Use new within-family C7 points only for C7 operator stability, not as G8 withheld-family evidence.
5. Reserve a genuinely fresh scale-transition mechanism/family for the next G8 attempt.
6. Continue masked observation-space and discriminant-coverage work independently; do not let a source-response scalar replace multi-channel information.
7. Keep `N_micro`, `N_manifold`, `N_repr`, and `N_disc` distinct.
8. No universal-model, no-hair, intrinsic-rank, fundamental-action, detectability or discovery claim.

Primary records:

- `experiments/054c_idm_dr_common_source_response_slope_v0_1.md` — immutable preregistration;
- `data/derived/comparison_readiness/experiment_054c_idm_dr_common_source_response_slope_v0_1_summary.json` — compact result;
- `docs/SCIENTIFIC_FINDING_F27_COMMON_RESPONSE_CENTROID_WITHHELD_FAILURE.md` — scientific interpretation.
