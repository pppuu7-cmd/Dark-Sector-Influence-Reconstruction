# BuyanovGPT table — DSIR influence atlas

**Date:** 2026-08-26  
**Status:** live research atlas / hypothesis organizer  
**Important:** this is not a fundamental theory, not a no-hair theorem, and not evidence that the dark sector has any preselected number of parameters.

The nickname **BuyanovGPT table** refers to the DSIR classification of dark-sector models by observable influence channels and response geometry rather than by microscopic model names alone.

## 1. Hard structural lesson

Model identity belongs to a **multi-channel influence trajectory**. The same microscopic direction may be exactly null, nearly degenerate, or strongly separated depending on the operator.

Current hard minimum hitting set for the frozen evidence graph remains:

`{metric slip, small-scale transfer, time/sign evolution}`.

This is not a theorem about fundamental parameter count.

## 2. Current response labels

Provisional bookkeeping labels:

- `G` — global growth / structure-amplitude information;
- `T` — scale / transfer dependence;
- `tau` — time evolution;
- `I` — irreducible scale-time nonseparability after additive projection;
- `S` — metric slip / anisotropic-stress / gravitational-potential information;
- `M` — small-scale/free-streaming/domain-localized information;
- `N` — interaction / exchange information;
- `B` — background / geometry information.

These are response types, **not guaranteed independent parameters**.

For the common low-k structure block,

\[
R(z,k)=\mu+T(k)+\tau(z)+I(z,k),
\]

with

\[
\chi_I=\frac{\|I\|^2}{\|R\|^2}.
\]

## 3. The simple Core=(G,T,tau) hypothesis is falsified

Exp045A hard result:

`FAIL_COMPACT_G_T_TAU_CORE_LOW_K_V0_1`.

Key local interaction-power fractions:

| Direction | `chi_I` |
|---|---:|
| C1 smooth-w | `0.0010805` |
| C2 IDE negative-alpha | `1.57e-11` |
| C2 IDE beta | `5.49e-11` |
| C3 GDM cs2 | `0.045305` |
| C3 GDM cv2 | `0.043634` |
| C5 designer f(R) | **`0.299856`** |

Thus `T(k)` and `tau(z)` cannot generally be treated as independent additive summaries. **How scale dependence evolves with time carries information.**

Do not replace the failed three-core hypothesis by an untested four-parameter claim. `I` is a required representation component for some tested responses, not yet a fundamental hair.

## 4. Pairwise localization of separation

Exp046 defines

\[
\eta_I(A,B)=\frac{\|d_I\|^2}{\|d\|^2}
\]

for the fraction of normalized pairwise response-shape separation power carried by irreducible `k x z` interaction.

Key hard descriptive values:

- GDM cs2/f(R): `0.611982`;
- GDM cv2/f(R): `0.613829`;
- IDE-alpha/f(R): `0.571946`;
- GDM cs2/cv2: `0.731139`, **but total angle only `0.323 deg`**.

Therefore `eta_I` must always be interpreted together with total distance/angle. A large fraction of a tiny distinction is still a tiny distinction.

Metric slip remains the established GDM pressure/viscosity separator.

## 5. Grid robustness — Exp047B

The descriptive hierarchy

\[
\boxed{\mathrm{IDE\ near\!-\!null}<\mathrm{smooth\!-\!w}<\mathrm{GDM}<f(R)}
\]

survives **12/12** deterministic single-node deletions (5 leave-one-k and 7 leave-one-z). Both IDE directions remain below the existing `chi_I=1e-6` morphology floor in every reduced grid.

GDM/f(R) pairwise interaction localization remains material under every deletion:

- cs2/f(R): `eta_I=0.5504..0.6539`;
- cv2/f(R): `eta_I=0.5520..0.6554`.

Hard caveat: smooth-w's absolute `chi_I` is sensitive to `k=0.001 h/Mpc`; removing that node lowers it by a factor about `27.6`. The **tier** is robust, the precise scalar value is not yet a family invariant.

## 6. Finite-amplitude manifolds — Exp047A

Exp047A reuses exact immutable solver products and asks whether the local hierarchy persists away from the tangent limit.

Hard provenance:

- run `32900174734`;
- artifact `9582737965`;
- SHA256 `95d6ce81bc208443ca2377c6f1c4b9523393e2620a2876a2fb53c36a8beabb37`.

All algebraic controls pass.

Sampled finite-amplitude `chi_I` envelopes:

| Class | sampled range |
|---|---:|
| IDE | `1.4351e-11 .. 5.4945e-11` |
| smooth-w | `0.00108051 .. 0.00108806` |
| GDM | `0.0130105 .. 0.0454103` |
| designer f(R) | `0.173327 .. 0.313326` |

The envelopes remain non-overlapping over all sampled physical amplitudes:

\[
\boxed{\mathrm{IDE}<\mathrm{smooth\!-\!w}<\mathrm{GDM}<f(R)}.
\]

Minimum descriptive gaps:

- smooth over IDE: factor `1.97e7`;
- GDM over smooth: factor `11.96`;
- f(R) over GDM: factor `3.82`.

This strengthens the response-class hierarchy, but no post-hoc scientific stability threshold was imposed and it is **not a universal law**.

## 7. New axis: trajectory geometry

`chi_I` is not constant along a family. One microscopic parameter may trace a curved path in response space.

Maximum sampled turning relative to each family's smallest reliable amplitude:

| Direction | full response turn | interaction turn |
|---|---:|---:|
| smooth-w | `0.155 deg` | `0.227 deg` |
| IDE alpha physical ray | `0.251 deg` | interaction below morphology floor |
| IDE beta central | `0.0041 deg` | interaction below morphology floor |
| GDM cs2 | `0.0279 deg` | `0.0324 deg` |
| GDM cv2 | **`7.18 deg`** | **`12.19 deg`** |
| designer f(R) | **`12.14 deg`** | **`13.00 deg`** |

Examples:

GDM viscosity:

\[
\chi_I(cv^2)=0.04377\rightarrow0.01301
\]

across `1e-8 -> 1e-4`.

Designer f(R):

\[
0.29986,\ 0.31333,\ 0.28617,\ 0.17333
\]

for `B0={1e-6,1e-5,1e-4,1e-3}`.

**Interpretation:** response-space complexity can arise from curvature of a one-dimensional physical manifold. Significant global SVD modes must not automatically be counted as additional microscopic degrees of freedom.

Keep distinct:

\[
N_{micro},\quad N_{manifold},\quad N_{repr},\quad N_{disc}.
\]

## 8. Current family map

| Family | Validated influence facts | Current atlas interpretation |
|---|---|---|
| C0 LambdaCDM/GR | common response origin | origin / zero point |
| C1 smooth non-phantom DE | nonzero background/AP; low-k response largely additive; weak `I`; finite trajectory nearly straight | background-active, weak scale-time coupling |
| C2 IDE | alpha/beta channel migration; low-k `I` near numerical-null across finite amplitudes | exchange-active candidate `N`; current structure highly separable in scale/time |
| C3 GDM (`w=0`) | exact background/AP null; density pressure/viscosity degeneracy; slip separates; moderate `I` | perturbation-only; `S` crucial; pressure ray nearly straight, viscosity bends at large amplitude |
| C4 thermal WDM | low-k nearly blind, high-k transfer strong | domain-localized/free-streaming candidate `M`; `I` unknown until high-k time atlas exists |
| C5 designer f(R) | exact background/AP null; scale-only near GDM; time/full structure separate; RSD scalar compression defect; strong `I`; curved finite trajectory | strongest current scale-time coupling example; modified-gravity response manifold visibly curved |

## 9. New promising comparison: localization geometry

Preliminary analysis after Exp047A suggests that for the smallest reliable GDM and f(R) responses, the **interaction-power localization over k** is almost identical while its localization over redshift is strongly different.

This may explain the older combination:

`scale-only near-degeneracy + temporal/full-structure separation`.

This is not yet registered as a hard finding. The next experiment must explicitly define localization profiles and controls before promoting it.

## 10. No-hair / universal-model boundary

The only defensible current hypothesis is:

> many microscopic dark-sector models may project onto a smaller structured observable influence space whose geometry includes null patterns, channel migration, nonseparability and trajectory curvature.

DSIR does **not** claim a dark-sector no-hair theorem or a universal model. Any dimensionality claim must survive C4 domain completion, observational projection, solver/gauge stress tests, prior/sampling changes, channel removal and withheld-family prediction.

## 11. Current continuation

1. Formalize interaction localization profiles over `k` and `z`; test whether GDM/f(R) are scale-localization lookalikes but time-localization opposites.
2. Connect trajectory bending to movement of characteristic transition scales through the finite observational window.
3. Extend C4 WDM to a high-k **time-dependent** atlas and compute its scale-time interaction without zero imputation.
4. Preserve slip/lensing and high-k transfer as independent channels.
5. Continue observation/window/covariance projection before detectability claims.
6. Estimate `N_repr` and `N_disc` only after common observation-space operators exist.
7. Universal model only after `docs/UNIVERSAL_MODEL_READINESS.md` criteria and a credible withheld-family test.

<!-- F23_ATLAS_UPDATE_2026-08-26 -->
## Atlas update through F23 — 2026-08-26

This section supersedes older provisional localization wording where it conflicts.

| Family/direction | Geometry/AP | low-k structure | irreducible k-z interaction | physical transition-scale status | independent localization prediction |
|---|---|---|---|---|---|
| C1 smooth-w | active | active | weak but grid-sensitive | no source scale assigned in current atlas | not tested |
| C2 IDE alpha/beta | active; alpha/beta AP-near-degenerate | active and separating | near-null on current local rays | no transition-scale claim | not tested |
| C3 GDM cs2 | exact AP/background null | active; density nearly collinear with cv2 | moderate | pressure Hubble-gradient scale source-derived; remains outside current low-k window for sampled cs2 | not applicable to current sampled crossing |
| C3 GDM cv2 | exact AP/background null | active; slip separates microphysics | moderate | dynamic-shear quasi-steady `k_v,QS=sqrt(9/8) Hconf/sqrt(cv2)` | 🟢 withheld PASS F21 |
| C4 thermal WDM | background geometry not represented by static transfer control | low-k nearly blind; high-k transfer strongly active | **unknown in time-dependent high-k block** | half-mode/free-streaming block separate | **running Exp050A; missing is not zero** |
| C5 designer f(R) B0 | exact AP/background null on frozen designer branch | active and scale-dependent | strong | exact EFTCAMB B-derived inverse-Compton scale | 🟢 withheld PASS F23 |

Current mechanism-level statement: when the source-derived transition lies inside the finite low-k window, moving it to smaller k predicts non-increasing interaction-energy scale localization on the tested C3-cv2 and C5-B0 withheld rays. This is two-family replicated evidence, **not a universal dark-sector law**.

Current missing blocks that prevent family-complete rank/law claims:
1. C4 genuine high-k `(k,z)` response (Exp050A running);
2. observation/window/covariance projection for the interaction/localization descriptors;
3. additional withheld families/directions rather than interpolation only within C3/C5;
4. validated GDM velocity/RSD channel remains blocked by gauge bridge;
5. no common block may be filled by zero for a missing family.

