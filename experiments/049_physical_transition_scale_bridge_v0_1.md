# Experiment 049A — source-native physical transition-scale bridge v0.1

**Date:** 2026-08-26  
**Status:** contract frozen; hard controls are provenance/algebra only  
**Parent results:** Exp048A/048B  
**Scope:** C3 GDM and C5 designer-f(R) on the frozen low-k DSIR window.

## Question

Exp048B found that finite-amplitude GDM viscosity and designer-f(R) both move the interaction-energy localization centroid toward lower wavenumber while `chi_I` falls, whereas GDM pressure remains almost stationary over its sampled ray.

This experiment asks whether that response-space migration coincides with a characteristic physical transition scale derived directly from the pinned solver equations.

This is deliberately **not** a fit of a phenomenological scale to `k_I`. The model amplitudes are known control parameters; characteristic scales are derived from source equations first and then compared with the already measured localization.

## Frozen response window

\[
z=\{0.295,0.51,0.706,0.934,1.317,1.491,2.33\},
\]

\[
k=\{0.001,0.003,0.01,0.03,0.1\}\;h/{\rm Mpc}.
\]

The localization data are the immutable Exp048B summary already admitted on the stacked branch.

## C3: GDM pressure scale

Pinned solver:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

The frozen configuration has

\[
w=c_a^2=0,\qquad \Omega_k=0,
\]

and constant `cs2` or `cv2` bins as appropriate.

For the pressure direction the Euler equation contains the pressure-gradient term proportional to

\[
k^2 c_s^2\delta.
\]

A source-native Hubble/gradient crossing proxy is therefore

\[
\boxed{k_s(z)=\frac{\mathcal H(z)}{\sqrt{c_s^2}}},
\qquad \mathcal H=aH.
\]

This is a diagnostic crossing scale, not an exact Jeans wavenumber.

`\mathcal H(z)` is read from the exact retained CLASS background of the same frozen artifact. No hand-reconstructed Friedmann closure is used.

## C3: dynamic viscosity scale

The frozen viscosity direction uses `dynamic_shear_gdm=yes`. The pinned source evolves shear as

\[
\sigma'=-3\mathcal H\sigma+\frac{8}{3}\frac{c_v^2}{1+w}(\theta+\mathrm{metric\ shear}),
\]

while the Euler equation contains

\[
\theta'\supset-\mathcal H\theta-k^2\sigma
\]

for the frozen `w=ca2=0`, flat case.

For a labelled quasi-steady diagnostic only, neglect `sigma'` and the metric-shear source in the closure estimate. Then

\[
\sigma\simeq\frac{8}{9}\frac{c_v^2}{\mathcal H}\theta,
\]

so equality of viscous and Hubble damping gives

\[
\boxed{k_{v,\mathrm{QS}}(z)=\sqrt{\frac{9}{8}}\frac{\mathcal H(z)}{\sqrt{c_v^2}}}.
\]

This is **not** asserted to be the exact viscosity eigenmode scale. Its purpose is to test whether the onset of the observed localization migration occurs when the source-derived viscous scale enters the finite DSIR k-window.

## C5: exact designer-f(R) B relation

Pinned solver:

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

The pinned designer source stores

\[
\Omega_{\rm EFT}=f_R
\]

and its `B` implementation is algebraically

\[
\boxed{B=\frac{f_R'}{1+f_R}\frac{H}{H'}
      =\frac{f_{RR}R'}{1+f_R}\frac{H}{H'}},
\]

where prime denotes `d/d ln a`.

The source also uses

\[
E=H^2/H_0^2,\qquad \bar R\equiv R/H_0^2=3(4E+E'),
\]

therefore

\[
\bar R'=3(4E'+E'').
\]

It follows exactly from the code convention that

\[
\frac{1+f_R}{3f_{RR}H_0^2}
=\frac{\bar R'}{3B(H'/H)}.
\]

Define the inverse Compton-length diagnostic

\[
\boxed{
\frac{k_C}{h}
=a\frac{100}{c}
\sqrt{\frac{\bar R'}{3B(H'/H)}}
}
\]

in `h/Mpc`.

For reference, the exact linear scalaron mass including the curvature term is also reported:

\[
\frac{m^2}{H_0^2}
=\frac{\bar R'}{3B(H'/H)}-\frac{\bar R}{3},
\]

\[
\boxed{\frac{k_m}{h}=a\frac{100}{c}\sqrt{m^2/H_0^2}}
\]

when the expression is positive.

In the high-curvature LCDM limit the first scale approaches the familiar orientation

\[
k_C\sim aH\sqrt{2/B},
\]

but the workflow uses the exact source quantities rather than this approximation.

## Diagnostic-only H-EFTCAMB instrumentation

The normal H-EFTCAMB background writer does not emit `B(a)` or the required designer internals. The workflow therefore applies a narrowly scoped diagnostic patch to the pinned source that only writes

`x, a, B, R/H0^2, f_R, E, E', E''`

during the final already-existing designer background integration.

The patch does **not** alter:

- the designer ODE right-hand side;
- initial-condition/root solving;
- stability conditions;
- solver precision;
- perturbation equations;
- frozen cosmological parameters.

The exact patch is uploaded with the run artifact.

## Immutable inputs

C3 retained artifact:

- run `32759738560`;
- digest `sha256:126c839ce948b5b25ec46b687af70e230c31d87071e6526727d1551a3c0f136d`.

C5 frozen configuration artifact:

- run `32759477319`;
- digest `sha256:9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`.

Production C5 amplitudes:

\[
B_0=10^{-6},10^{-5},10^{-4},10^{-3}.
\]

## Hard controls frozen before the first Exp049 CI result

Only the following may produce a hard FAIL:

1. same-background GDM `H(z)` agreement for the cs2/cv2 controls: maximum relative difference `<=1e-12` on frozen redshifts;
2. terminal diagnostic `B(a=1)` reproduces requested `B0` to relative error `<=1e-6`;
3. exact upstream SHAs and source-equation markers are present;
4. all production designer runs are stable and diagnostic tables are produced.

## Scientific interpretation rule

No threshold is frozen for

- `|k_I-k_*|/k_*`;
- entry/exit of a characteristic scale through the DSIR window;
- correlation with `chi_I`;
- monotonicity of localization motion.

Those patterns were already partly visible before this experiment was formalized. They are therefore descriptive/supporting evidence only unless confirmed by a genuinely independent future test.

A particularly useful falsification outcome would be that the exact designer-f(R) scale moves in a direction inconsistent with the measured localization flow, or that its transition is nowhere near the frozen window while localization changes strongly. Such a result must be retained, not tuned away.

## Gate boundary

Exp049A can strengthen or weaken the hypothesis that response nonseparability is controlled by a physical transition traversing the observed `(k,z)` window. It cannot by itself establish a universal dark-sector law, close G7, close G8, determine a field count, or justify construction of the universal model.
