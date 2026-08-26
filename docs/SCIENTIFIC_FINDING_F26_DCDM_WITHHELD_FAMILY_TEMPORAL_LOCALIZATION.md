# F26 — withheld-family DCDM response shifts to earlier epochs as decay rate increases

**Status: HARD ESTABLISHED for the preregistered Exp053A C6 test; broader characteristic-scale/epoch principle STRONGLY SUPPORTED but not yet a frozen universal law.**

Experiment 053A is the first DSIR withheld-family/mechanism test rather than an interpolation within C1-C5. The new mechanism is decaying cold dark matter (DCDM) into dark radiation, implemented in the same pinned official CLASS lineage used independently for C4:

`lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`.

DCDM was not used to construct the earlier characteristic-scale findings F21, F23 or F25.

## Source-native physical control

Pinned CLASS implements

\[
\frac{d\rho_{\rm dcdm}}{d\ln a}
=-3\rho_{\rm dcdm}-\frac{\Gamma_{\rm dcdm}}{H}\rho_{\rm dcdm},
\]

\[
\frac{d\rho_{\rm dr}}{d\ln a}
=-4\rho_{\rm dr}+\frac{\Gamma_{\rm dcdm}}{H}\rho_{\rm dcdm},
\]

and explicit decay/source terms in the perturbation hierarchy. Therefore the natural control is a lifetime/epoch variable rather than a primary spatial cutoff.

The frozen dimensionless decay rates were

\[
\gamma\equiv\Gamma_{\rm dcdm}/H_0
=\{0.25,0.5,1,2\}.
\]

The DCDM runs use `omega_ini_dcdm=0.1200`, while the matched stable-CDM reference uses `omega_cdm=0.1200`.

## Preregistered observable

On the standard DSIR low-k and redshift grids,

\[
r(k,z;\gamma)=\ln\frac{P_{\rm DCDM}(k,z;\gamma)}{P_{\rm CDM}(k,z)}.
\]

Define

\[
q_z(z;\gamma)=
\frac{\sum_k r^2(k,z;\gamma)}{\sum_{z,k}r^2(k,z;\gamma)},
\]

and

\[
1+z_R(\gamma)=
\exp\left[\sum_zq_z(z;\gamma)\ln(1+z)\right].
\]

Before the first C6 solver outputs were inspected, the frozen prediction was

\[
\boxed{
z_R(\gamma_{i+1})-z_R(\gamma_i)>10^{-3}
}
\]

for every consecutive rate step. A minimum response norm `||r||_2>1e-4` was also frozen.

## Infrastructure history

The first workflow run `32915553193` successfully built CLASS and generated all DCDM and reference `P(k,z)` outputs, but an overly specific background filename assertion failed before the scientific step. The preregistered science test was **skipped**. That run is infrastructure-only and is not a failed or passed scientific result.

Only the background filename glob was corrected. The gamma grid, response definition, centroid, k/z grids and threshold were unchanged.

## Hard result

The first science-executing run and the clean-current-main confirmation both passed.

Clean confirmation provenance:

- run `32915877993` — PASS;
- artifact `9588160014`;
- SHA256 `541e3449801f0e853fa573784fd72685ad407c1a3f041b18884e715017aa5e10`;
- clean head `7653bae9059ddeae065b0ae87d27350b9476b794`.

The temporal centroids are

\[
z_R=
(0.6304573,\;0.6343830,\;0.6419613,\;0.6562403)
\]

for `Gamma/H0=(0.25,0.5,1,2)`.

The consecutive shifts are

\[
\boxed{
(0.00392568,\;0.00757834,\;0.01427902)
}
\]

and every step exceeds the preregistered `10^-3` threshold. Response norms increase from `0.1254` to `0.9095`, well above the frozen numerical floor.

**Hard conclusion:** in a dark-sector family that was not used to build the previous DSIR characteristic-scale picture, increasing the physical decay rate moves the localization of the observable matter-power response to earlier cosmic epochs in the preregistered direction.

## New descriptive morphology

The following were not part of the gate and remain descriptive.

### Moderate scale-time nonseparability

Using the same additive decomposition

\[
R=\mu+T(k)+\tau(z)+I(k,z),
\]

DCDM has

\[
\chi_I\simeq
0.0820,\;0.0797,\;0.0751,\;0.0665.
\]

This places the sampled C6 response above current smooth-w but below the small-amplitude designer-f(R) interaction fraction, and in the broad range of moderate nonseparability seen in GDM. Direct cross-family ordering must still respect solver/domain masks.

### Nearly one-ray finite family with measurable curvature

The extreme full-response angle between `Gamma/H0=0.25` and `2` is only about

\[
2.17^\circ,
\]

so the sampled DCDM family is close to an amplitude-scaled response ray, but not exactly one-dimensional in linear response coordinates.

### Scale-sign pivot

For all four sampled rates, the response is positive at `k=0.001 h/Mpc` and negative at sufficiently larger frozen k. The first interpolated zero crossing is mainly redshift-dependent and only weakly lifetime-dependent. For example:

- at `z=0.295`: approximately `0.00268 -> 0.00257 h/Mpc` from gamma `0.25 -> 2`;
- at `z=2.33`: approximately `0.00669 h/Mpc` for both extremes.

Thus C6 introduces a potentially useful new fingerprint: a redshift-moving scale-sign pivot that is approximately invariant along the sampled lifetime direction. This requires a dedicated preregistered follow-up before hardening.

## Scientific significance

F21/F23 showed withheld characteristic-scale motion inside GDM viscosity and designer-f(R). F25 showed a withheld free-streaming cutoff shift inside WDM. F26 now extends the broader organizing idea to a **new mechanism with a temporal lifetime scale**.

The strongest defensible statement is therefore:

> distinct dark-sector mechanisms can encode their microscopic transition scale or epoch as systematic motion of a response-localization coordinate, even when the appropriate observable coordinate differs by mechanism.

This is now supported by a true withheld-family test.

However, **G8 is not automatically closed**. G7 still lacks one preregistered, model-independent quantitative relation whose same mathematical form can be applied across these families. F26 supplies the withheld-family evidence needed to make construction of such a relation scientifically worthwhile; it does not retroactively define the relation.

## Boundary

- no observational detectability claim;
- no claim that DCDM is favored by data;
- no claim that `z_R` is universally the correct temporal coordinate;
- no universal no-hair or intrinsic-rank claim;
- no G7/G8 closure without a common frozen relation;
- the scale-sign pivot and `chi_I` behavior are descriptive until separately preregistered.
