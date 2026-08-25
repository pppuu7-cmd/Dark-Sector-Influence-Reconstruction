# F18 — finite-amplitude response trajectories preserve class ordering but are not straight

**Status:** HARD ESTABLISHED descriptive finite-amplitude geometry on the sampled C1/C2/C3/C5 frozen low-k manifolds (Exp047A); broader mechanism interpretation SUPPORTED only.

## Definition

For every finite response matrix

\[
R(z,k)=\mu+T(k)+\tau(z)+I(z,k),
\]

use

\[
\chi_I=\frac{\|I\|^2}{\|R\|^2}.
\]

For a one-parameter physical branch with smallest reliable amplitude `a0`, define response-space and interaction-space turning angles

\[
\theta_R(a)=\angle(R(a),R(a_0)),
\]

\[
\theta_I(a)=\angle(I(a),I(a_0)),
\]

with `theta_I` reported only when both interaction vectors exceed the existing morphology floor `chi_I>=1e-6`.

These are turning angles, not Frenet curvature scalars.

## Provenance

- workflow run `32900174734`;
- artifact `9582737965`;
- artifact SHA256 `95d6ce81bc208443ca2377c6f1c4b9523393e2620a2876a2fb53c36a8beabb37`;
- source head `efdd85847d4244285716824f960329fa24cbf852`;
- exact immutable parent artifacts are the already admitted C1/C2/C3/C5 solver products listed in Exp047A.

Operator controls pass:

- reconstruction error `0`;
- max normalized core/interaction orthogonality `7.3270e-15`;
- max scaled zero-mean residual `9.4258e-21`;
- required ceiling `1e-12`.

## Finite-amplitude class envelopes

Across all sampled physical finite amplitudes used for the class envelopes:

| class | sampled `chi_I` range |
|---|---:|
| IDE | `1.4351e-11 .. 5.4945e-11` |
| smooth-w | `0.00108051 .. 0.00108806` |
| GDM | `0.0130105 .. 0.0454103` |
| designer f(R) | `0.173327 .. 0.313326` |

Therefore the current sampled envelopes are non-overlapping:

\[
\boxed{\mathrm{IDE}<\mathrm{smooth\!-\!w}<\mathrm{GDM}<f(R)}.
\]

Descriptive gap factors are:

- `smooth_min / IDE_max = 1.9665e7`;
- `GDM_min / smooth_max = 11.9575`;
- `fR_min / GDM_max = 3.81691`.

This substantially strengthens the local-tangent hierarchy seen in Exp045A/046 and the grid robustness of Exp047B. It is still a sampled-domain result, not a universal law.

## The hierarchy does not mean `chi_I` is a family constant

### Smooth-w

`epsilon_w=1e-4 -> 1e-2`:

- `chi_I = 0.00108051 -> 0.00108806`;
- max full-response turning `0.1550 deg`;
- max interaction turning `0.2274 deg`.

The response is nearly straight over this sampled ray.

### IDE

Physical negative-alpha ray:

- `chi_I = 1.57e-11 -> 1.44e-11` from `|alpha|=1e-4 -> 1e-2`;
- max response turning `0.2511 deg`.

The central odd beta response is even straighter:

- `chi_I = 5.4945e-11 -> 5.4924e-11`;
- max response turning only `0.00414 deg` over `|beta|=1e-4 -> 1e-2`.

IDE remains essentially scale-time separable on this frozen low-k domain.

### GDM pressure `cs2`

`cs2=1e-8 -> 1e-6`:

- `chi_I = 0.0452455 -> 0.0454103`;
- response turning `0.0279 deg`;
- interaction turning `0.0324 deg`.

This is an almost straight response ray over the sampled range.

### GDM viscosity `cv2`

`cv2=1e-8 -> 1e-4`:

\[
0.0437706,\ 0.0437365,\ 0.0433932,\ 0.0397495,\ 0.0130105.
\]

At the largest sampled amplitude:

- response turning `7.1765 deg`;
- interaction turning `12.1916 deg`.

Thus pressure and viscosity, although almost collinear locally in density response, have very different **finite-amplitude trajectory curvature**.

### Designer f(R)

Production `B0={1e-6,1e-5,1e-4,1e-3}`:

\[
\chi_I=0.299856,\ 0.313326,\ 0.286168,\ 0.173327.
\]

At `B0=1e-3` relative to the `1e-6` response direction:

- full-response turning `12.1367 deg`;
- interaction turning `12.9969 deg`.

Therefore a strictly one-parameter microscopic family can trace a visibly curved trajectory in the 35-dimensional frozen response space.

## Hard conceptual consequence

A global multi-mode decomposition of finite points along a one-parameter family can report several significant response modes simply because a **one-dimensional manifold is curved**.

Hence DSIR must keep distinct:

\[
N_{micro},\qquad N_{manifold},\qquad N_{repr},\qquad N_{disc}.
\]

For the sampled C5 family, `N_micro=1` by construction even though the finite response trajectory turns by about `12 deg` and a global SVD can require multiple modes to approximate the curve.

**This directly rules out interpreting every significant response-space singular vector as an additional fundamental dark-sector degree of freedom.**

## Supported physical interpretation

The magnitude of nonseparability appears to depend both on mechanism and on where the mechanism's characteristic transition lies relative to the finite `(k,z)` window. Shape/nonseparability descriptors should therefore be treated as **window-localized trajectory properties**, not monotonic measures of microscopic coupling strength.

This is consistent with the earlier C5 RSD result where the scalar-growth representability defect rises and then plateaus rather than remaining monotonic in `B0`.

## Boundaries

- No scientific drift threshold was frozen after the finite products had already been inspected; the numerical pattern is hard descriptive, not a preregistered mechanism-classification PASS.
- C4 WDM is absent from this low-k finite-amplitude comparison and must not be imputed as zero.
- No survey detectability, universal no-hair theorem, intrinsic rank, G7 residual law or G8 discovery follows.
