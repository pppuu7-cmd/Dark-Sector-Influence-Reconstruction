# Experiment 055A — retrospective endpoint-normalized half-transition candidate v0.1

Date: 2026-08-26
Status: **RETROSPECTIVE CANDIDATE SEARCH AFTER Exp054C FAILURE — NOT A G7/G8 GATE**

## Motivation

Exp054C prospectively falsified the Exp054A raw full-response `R^2` centroid slope on withheld C7 IDM-DR. The failure mechanism is concrete: C7 is nearly scale-only on the frozen low-k domain and increasing suppression amplitude pushes the `R^2` centroid to the upper endpoint `k=0.1 h/Mpc`.

This experiment asks whether an amplitude-normalized **transition-location** operator can be defined identically on the immutable C3 GDM, C5 designer-f(R), and now-unblinded C7 IDM-DR responses.

Because the operator was motivated after seeing C7, **C7 is calibration/diagnostic data here, not withheld evidence**. Even a perfect result cannot close G7 or G8.

## Immutable input provenance

Use only already generated artifacts:

- C3 GDM Exp049B run `32904158849`, artifact `9584180621`, SHA256 `892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a`;
- C5 designer-f(R) Exp049C run `32907619613`, artifact `9585579947`, SHA256 `bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942`;
- C7 IDM-DR Exp054C first science-evaluable run `32920776596`, artifact `9589768992`, SHA256 `fa61a7ae5d53550fd9bf057a4354f8f343e74c18f93a4ce23d5ed964f6dc4c2a`.

No new theory response is generated in Exp055A.

All three families use the frozen low-k nodes

\[
k=\{0.001,0.003,0.01,0.03,0.1\}\;h/{\rm Mpc}
\]

and seven redshifts

\[
z=\{0.295,0.51,0.706,0.934,1.317,1.491,2.33\}.
\]

## Common operator

For every model amplitude and every redshift define the endpoint-affine response coordinate

\[
\boxed{
u(z,k)=\frac{R(z,k)-R(z,k_{min})}{R(z,k_{max})-R(z,k_{min})}}
\]

provided the denominator is finite and non-zero.

This removes an arbitrary additive response offset and an arbitrary non-zero multiplicative response amplitude/sign. It does **not** assume the full profile is monotone.

Require a unique crossing of

\[
u(z,k_{50})=1/2
\]

inside the frozen k interval. Locate that crossing by piecewise linear interpolation of `u` in `ln k`; no additional k nodes are introduced.

Compress the seven row crossings only after all seven are valid:

\[
\boxed{k_{50}^{geo}=\exp\left[\frac1{7}\sum_z\ln k_{50}(z)\right]}.
\]

For adjacent points of one family define

\[
\boxed{C_{50,i}=\frac{\Delta\ln k_{50}^{geo}}{\Delta\ln k_*}}.
\]

The source-native `k_*` values are the same immutable values used in Exp054A/054C:

- C3: dynamic-shear quasi-steady source proxy from F21;
- C5: exact pinned designer-f(R) Compton-source statistic from F23;
- C7: IDM-DR drag/Hubble equality source scale from Exp054B.

## Retrospective candidate criterion

This is descriptive candidate qualification, not a preregistered discovery gate.

Report `RETROSPECTIVE_COMMON_HALF_TRANSITION_CANDIDATE_POSITIVE_V0_1` only if:

1. every endpoint contrast is finite and non-zero;
2. every one of the `3 families x 5 amplitudes x 7 redshifts = 105` rows has exactly one `u=1/2` crossing;
3. every adjacent `C_50` is finite and strictly positive;
4. the sign remains positive after each of the seven leave-one-redshift-out recomputations.

No common magnitude band is fitted. The hypothesis being screened is only the order-preserving inequality

\[
\boxed{C_{50}>0}.
\]

## Interpretation boundary

A positive result means only that `k_50` is a promising common **candidate response coordinate** on the three already-seen scale-transition mechanisms. It can justify a later preregistration against a genuinely fresh mechanism/family.

It does not:

- rescue Exp054C or change F27;
- make C7 withheld again;
- establish G7 or G8;
- establish observational detectability;
- define a universal dark-sector parameter;
- determine intrinsic field count/rank;
- reconstruct an action or fundamental dynamics.
