# F27 — prospective C7 falsifies the common full-response centroid slope v0.1

Date: 2026-08-26  
Experiment: Exp054C  
Status: **LIMIT / NEGATIVE RESULT, HARD PROSPECTIVE**

## Question

Exp054A used only immutable C3 GDM and C5 designer-f(R) response products to calibrate one common full-response scale operator,

\[
q_k^R(k)=\frac{\sum_zR(z,k)^2}{\sum_{z,k}R(z,k)^2},\qquad
k_R^{geo}=\exp\left(\sum_kq_k^R\ln k\right),
\]

and the adjacent source-response slope

\[
\mathcal C_i=\frac{\Delta\ln k_R^{geo}}{\Delta\ln k_*}.
\]

All C3/C5 calibration slopes were positive, so before any C7 response existed Exp054A froze the prospective acceptance interval

\[
0.0022992620786061375\le \mathcal C_i\le0.09951219222831723.
\]

Exp054B then selected five IDM-DR couplings from the pinned CLASS source equations only. The complete Exp054C science contract was committed at `1df523f02a549dccc9b7bb11cb608922546b56c1` before the first C7 matter-power response was generated.

## First science-evaluable prospective run

- run: `32920776596`;
- source branch head: `304383093968107a114494d312efacd78890e49a`;
- pinned CLASS: `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`;
- artifact: `9589768992`;
- artifact SHA256: `fa61a7ae5d53550fd9bf057a4354f8f343e74c18f93a4ce23d5ed964f6dc4c2a`.

The earlier infrastructure attempts did not supply a science result. The first failed before C7 response generation because pinned precision triggers collided; the final run changes only the unused IDM-DR streaming-trigger numerical value from the colliding default while retaining the pre-frozen physical and scientific contract.

All six configurations generated all seven requested `P(k,z)` tables and passed the explicit output-count/header/domain checks before evaluation.

## Hard result

Frozen source scales:

`k_* = {0.08484583, 0.07347864, 0.05999506, 0.04647197, 0.03927599} h/Mpc`.

Measured full-response centroids:

`k_R^geo = {0.06627534, 0.08089267, 0.09263361, 0.09796438, 0.09915098} h/Mpc`.

Thus all four prospective slopes have the opposite sign to the C3/C5 calibration:

`C = {-1.38559414, -0.66851005, -0.21906458, -0.07156512}`.

Every pair fails the frozen positive interval. Therefore

`FAIL_IDM_DR_COMMON_SOURCE_RESPONSE_SLOPE_V0_1`.

This is a genuine prospective falsification. The v0.1 band must not be widened, the sign must not be flipped, and the C7 grid/operator must not be altered to convert this outcome into a pass.

## Why the operator failed

The failure is structurally informative. As the IDM-DR coupling grows, the fraction of response power assigned by `q_k^R` to the upper endpoint `k=0.1 h/Mpc` rises

`0.6923 -> 0.8417 -> 0.9432 -> 0.9850 -> 0.9939`.

The centroid therefore approaches the hard upper boundary even though the source-native transition scale moves to lower k.

A post-gate orthogonal additive decomposition

\[
R=\mu+T(k)+\tau(z)+I(k,z)
\]

finds

`chi_I=||I||^2/||R||^2 = 1.48e-8 -> 3.65e-10`.

Hence C7 on this frozen domain is almost perfectly scale-only/time-separable. The amplitude of the high-k suppression, rather than movement of a nonseparable interaction patch, dominates the raw `R^2` localization operator.

## New descriptive clue — not part of the failed gate

Define an endpoint-affine response coordinate at each redshift,

\[
u(z,k)=\frac{R(z,k)-R(z,k_{min})}{R(z,k_{max})-R(z,k_{min})},
\]

and locate the unique `u=1/2` crossing by linear interpolation in `ln k`. Its redshift-geometric mean gives a descriptive half-transition scale `k_50`.

For the same C7 outputs,

`k_50 = {0.06872866, 0.06496381, 0.06115403, 0.05818873, 0.05695898} h/Mpc`,

with positive adjacent log-slopes relative to `k_*`:

`{0.39165, 0.29810, 0.19460, 0.12697}`.

This does **not** rescue Exp054C. It only identifies a plausible reason for the failure and motivates a separately registered candidate operator.

## Scientific interpretation

1. **Hard negative:** there is no support for a common C3/C5/C7 law based on the raw full-response `R^2` centroid with the Exp054A quantitative band.
2. **Broader hypothesis survives:** the failure is of a specific common operator, not of the broader mechanism-native characteristic-scale/epoch idea supported by F21/F23/F25/F26.
3. **Mechanism morphology matters:** an operator suited to nonseparable interaction localization can be dominated by endpoint amplitude for an almost scale-only response.
4. **G7 remains OPEN.** The failed relation cannot close it.
5. **G8 remains OPEN.** A new relation must be formulated without using its future withheld test mechanism.
6. No fundamental action, universal dark-sector model, intrinsic field count, survey detectability, or discovery claim follows.

## Next research action

Analyze the endpoint-normalized half-transition operator on the immutable C3/C5/C7 products as a **retrospective candidate only**. If it admits a clean common definition and stability checks, freeze it before testing on fresh withheld points/mechanism. Do not use C7 again as the withheld family for a relation whose form was chosen after seeing C7.
