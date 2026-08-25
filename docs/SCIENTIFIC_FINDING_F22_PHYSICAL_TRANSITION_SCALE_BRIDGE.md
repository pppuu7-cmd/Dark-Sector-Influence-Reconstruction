# F22 — source-native transition scales track interaction-localization migration

**Status:** source-scale extraction **HARD ESTABLISHED** for the frozen C3/C5 implementations; cross-family window-crossing interpretation **SUPPORTED / PARTIAL**.

## Result

Experiment 049A derives characteristic physical scales from the pinned solver equations rather than fitting them to the previously measured localization.

For frozen GDM with `w_gdm=0`, the pressure-gradient crossing is

\[
k_s=\frac{\mathcal H}{\sqrt{c_s^2}},
\]

and the pinned dynamic-shear equation gives the labelled quasi-steady viscosity proxy

\[
k_{v,QS}=\sqrt{\frac98}\frac{\mathcal H}{\sqrt{c_v^2}}.
\]

The latter is not claimed to be an exact Jeans/eigenmode wavenumber.

For pinned designer f(R), EFTCAMB defines

\[
B=\frac{f_R'}{1+f_R}\frac{H}{H'}
  =\frac{f_{RR}R'}{1+f_R}\frac{H}{H'},
\]

with prime `d/d ln a`. Diagnostic-only instrumentation of the unmodified background solution writes `B(a), f_R(a), R/H0^2, E, E', E''`, from which

\[
\frac{1+f_R}{3f_{RR}H_0^2}
=\frac{(R/H_0^2)'}{3B(H'/H)}
\]

and therefore the inverse Compton scale is computed directly.

## Hard provenance and controls

- GitHub Actions run: `32904376001`
- source head: `bdccf72fd1e63edc91f2927278623cd5b27e0e95`
- artifact: `9584346604`
- artifact SHA256: `6a2c7f4e072fe7ee5d3a125bd798e975ab7031f5e7e92f3c71b47dbe71856f22`
- pinned GDM_CLASS: `4c87916aab5ca124a68f1dd16f31846fc13d1829`
- pinned H-EFTCAMB: `16d9c4e9f85751e30efd0a53b177941713078904`
- GDM background response check: exactly `0` at retained precision for the audited cs2/cv2 controls
- maximum terminal designer-B0 relative error: `8.75255e-9`, below the frozen `1e-6` hard control.

## GDM pattern

Pressure ray `cs2={1e-8,1e-7,1e-6}` keeps its source scale above the entire low-k window; measured interaction localization remains essentially fixed near `k_I^geo=0.051 h/Mpc`.

Dynamic-shear ray:

| cv2 | k_v,QS(z_I) [h/Mpc] | transition in frozen window? | k_I^geo [h/Mpc] |
|---:|---:|:---:|---:|
| 1e-8 | 3.25407 | no | 0.0509858 |
| 1e-7 | 1.02904 | no | 0.0509818 |
| 1e-6 | 0.325464 | no | 0.0509412 |
| 1e-5 | 0.103107 | yes on part of frozen z range | 0.0504785 |
| 1e-4 | 0.0331561 | yes | 0.0406271 |

This retrospective Exp049A pattern was subsequently given an independent withheld test in Exp049B/F21; five unseen intermediate cv2 points passed the pre-frozen non-increasing `k_I^geo` prediction.

## Designer-f(R) pattern

| B0 | k_C(z_I) [h/Mpc] | min k_C over frozen z [h/Mpc] | transition in frozen window? | k_I^geo [h/Mpc] |
|---:|---:|---:|:---:|---:|
| 1e-6 | 1.52752 | 0.702689 | no | 0.0510862 |
| 1e-5 | 0.415201 | 0.222210 | no | 0.0508385 |
| 1e-4 | 0.142365 | 0.0702692 | yes | 0.0488757 |
| 1e-3 | 0.0550213 | 0.0222220 | yes | 0.0399397 |

Thus a physically distinct mechanism shows the same descriptive ordering: the interaction-energy scale centroid is nearly stationary while the source-derived transition lies outside the frozen `k<=0.1 h/Mpc` window, then migrates to smaller k after the transition enters it.

## Interpretation boundary

The exact scale calculations and provenance are hard. The **cross-family causal/general principle is not yet hard**, because the f(R) comparison was formulated after Exp048B localization had already been inspected. It must survive a withheld f(R) interpolation test (Exp049C), broader families/domains, and eventually observation-space projection.

Do **not** promote this to a universal dark-sector law, a no-hair theorem, an intrinsic field count, G7 closure, or a survey-detectability statement.
