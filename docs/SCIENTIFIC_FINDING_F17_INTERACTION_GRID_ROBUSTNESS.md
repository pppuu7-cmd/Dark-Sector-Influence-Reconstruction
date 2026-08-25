# F17 — scale-time interaction hierarchy survives every single-node deletion

**Status:** HARD ESTABLISHED descriptive robustness on the frozen C1/C2/C3/C5 low-k theory-response atlas (Experiment 047B); broader mechanism interpretation SUPPORTED only.

## Statement

Experiment 047B recomputes the orthogonal response decomposition

\[
R=\mu+T+\tau+I
\]

on twelve deterministic reduced grids: each of the five frozen k nodes and each of the seven frozen z nodes is removed once.

The direction statistic is

\[
\chi_I=\frac{\|I\|^2}{\|R\|^2},
\]

and pairwise localization is

\[
\eta_I=\frac{\|d_I\|^2}{\|d\|^2}.
\]

No scientific stability threshold was applied post hoc; only algebraic controls could fail.

## Hard provenance

- run `32894616114`;
- source head `9a05c451401ac2cede3a56ef4ca2a1923eecb9c3`;
- artifact `9580724793`;
- artifact SHA256 `948038245e4eeea9ca569a48e138f5bdddaede19f0ff98ea941fc91a00272bb7`;
- result summary `data/derived/comparison_readiness/experiment_047b_interaction_leave_one_node_stability_v0_1.json`.

The first workflow attempt failed only at JSON serialization of `numpy.longdouble`; the successful rerun changed serialization only, not formulas, grids or thresholds.

## Controls

- max reconstruction error `0`;
- max core/I orthogonality residual `8.3946e-14`;
- max pairwise Pythagorean residual `2.3505e-17`;
- frozen ceiling `1e-12`.

Controls pass.

## Hard descriptive result 1 — tier ordering

The ordering

\[
\boxed{\text{IDE near-null}<\text{smooth-w}<\text{GDM}<f(R)}
\]

is preserved in **12/12** leave-one-node grids. Both IDE directions remain below the pre-existing `chi_I=1e-6` morphology floor in **12/12** grids.

Ranges:

- IDE alpha: `1.99e-13 .. 7.36e-11`;
- IDE beta: `3.66e-13 .. 7.45e-11`;
- smooth-w: `3.91e-5 .. 1.34e-3`;
- GDM cs2: `0.0279 .. 0.0525`;
- GDM cv2: `0.0265 .. 0.0505`;
- designer f(R): `0.2233 .. 0.3497`.

This supports a robust **coarse ordering** of scale-time nonseparability on the current low-k atlas.

## Hard descriptive result 2 — GDM/f(R) interaction localization

For GDM cs2/f(R),

\[
\eta_I=0.5504..0.6539,
\]

and for GDM cv2/f(R),

\[
\eta_I=0.5520..0.6554.
\]

Thus every leave-one-node grid retains **more than half** of the normalized GDM/f(R) response-shape separation power in irreducible scale-time interaction.

Because `eta_I>0.5` was not a preregistered scientific threshold, this is a descriptive hard result, not a formal new gate.

## Hard limitation — smooth-w absolute magnitude is grid-sensitive

Dropping `k=0.001 h/Mpc` changes smooth-w

\[
\chi_I=1.0805\times10^{-3}\rightarrow3.9123\times10^{-5},
\]

a factor `0.0362` of the full-grid value (about `27.6x` lower).

Therefore the smooth-w **tier** is robust, but its precise `chi_I` value is not yet a grid-insensitive family invariant.

## GDM pressure/viscosity caveat remains

GDM cs2/cv2 `eta_I` remains `0.6525..0.7377`, but their total response separation is tiny. A large fraction of a tiny distance is not detectability or mechanism identification. Metric slip remains the validated separator.

## Interpretation

The strongest supported physical hypothesis after Exp047B is narrower than “chi_I is a universal parameter”:

> on the current low-k response domain, mechanisms dominated by GDM closure physics and designer modified gravity exhibit persistent scale-time coupling that is qualitatively stronger than the local IDE directions, and the GDM/f(R) distinction remains substantially encoded in the joint evolution of scale dependence with time.

This may reflect different dynamical structure of perturbation propagation, but that causal interpretation is not established yet.

## Falsification / next tests

- finite parameter-amplitude/step stability;
- solver-precision stability;
- domain extension, especially C4 high-k time dependence;
- survey/window projection;
- withheld-family test.

## Boundary

Not independent-data confirmation, survey distinguishability, intrinsic rank, a universal fourth parameter, no-hair theorem, residual law or discovery. C4 is absent by domain contract, not zero.
