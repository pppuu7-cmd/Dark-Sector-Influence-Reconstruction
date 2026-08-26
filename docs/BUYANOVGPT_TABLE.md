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

<!-- DSIR_EXP050A_DOC_SYNC_2026_08_26 -->
## 12. Exp050A update — C4 high-k time geometry

The previous C4 entry `I unknown until high-k time atlas exists` is superseded by Exp050A.

| C4 quantity | Hard result on frozen high-k linear atlas |
|---|---|
| masses | `2,3,5 keV` |
| k-domain | `0.1,0.3,1,3,10,20 h/Mpc` |
| z-domain | standard seven DSIR nodes |
| high-k suppression | strong; e.g. at z=0.295, k=20: `r=-1.193,-0.445,-0.119` |
| redshift drift | tiny: max `6.83e-5,2.26e-5,5.07e-6` |
| irreducible interaction `chi_I` | `2.58e-10,2.21e-10,2.29e-10` |
| atlas interpretation | **domain-localized free-streaming / scale-dominated; nearly time-separable on this frozen linear domain** |

This gives the current response-class contrast:

`IDE`: near-separable low-k exchange response;
`smooth-w`: weak low-k interaction;
`GDM`: moderate low-k interaction, viscosity curvature/window flow;
`WDM`: strong high-k scale signature with almost no `k x z` interaction;
`designer-f(R)`: strong low-k scale-time interaction and curved window flow.

Do not compare these `chi_I` numbers as if they came from one common k-domain; the atlas remains block-aware/masked.

### Updated continuation

1. Recompute block-aware discriminant coverage including the C4 time block.
2. Design a withheld/intermediate WDM free-streaming test before proposing any generalized transition-window law involving C4.
3. Preserve metric slip for GDM pressure/viscosity and high-k transfer for WDM as distinct channel requirements.
4. Continue observation-space mapping before any `N_repr`/`N_disc` hard claim.

<!-- DSIR_EXP050B_DOC_SYNC_2026_08_26 -->
## 13. Exp050B/F25 update — C4 free-streaming scale flow

C4 now has a validated mechanism-native finite-amplitude coordinate:

`k_0.1(z)` defined by `ln(P_WDM/P_CDM)=-0.1`.

Withheld masses `2.5,3.5,4.0,4.5 keV` passed the preregistered prediction that `k_0.1` increases with mass at every one of the seven DSIR redshifts.

At z=0.295:

| m [keV] | k_0.1 [h/Mpc] |
|---:|---:|
| 2.5 | 8.38666 |
| 3.5 | 12.19283 |
| 4.0 | 14.23013 |
| 4.5 | 16.47374 |

This sharpens the C4 atlas label from merely `M/high-k active` to:

**strong scale-dominated free-streaming response + nearly time-separable shape + monotonic cutoff-scale manifold.**

Descriptive, not hard: all old+new masses at z=0.295 fit roughly `k_0.1 ~ m^1.1434` to <0.8% relative residual. A new preregistered test is required before treating that exponent as stable.

### Cross-family lesson

The current useful common abstraction is not “one universal k_I”. It is **characteristic response-scale motion with mechanism-dependent coordinates**:

- GDM viscosity / f(R): nonseparable interaction localization;
- WDM: nearly separable transfer cutoff.

Whether these can be mapped to a common residual-law coordinate is an open G7 problem.

<!-- DSIR_F26_C6_SYNC_2026_08_26 -->
## 14. C6 DCDM withheld-family extension — F26

C6 introduces a mechanism qualitatively different from C1-C5: cold dark matter decays into dark radiation with lifetime control `Gamma/H0`.

| C6 channel | Current status |
|---|---|
| background | active; dedicated AP angle not yet hard-audited |
| low-k structure | active |
| temporal localization | **active + preregistered withheld-family PASS** |
| `I(k,z)` | active, `chi_I~0.066..0.082` descriptive range |
| metric slip | unknown |
| high-k transfer | unknown |
| density-velocity compression | unknown |

Pre-frozen temporal centroid moves `0.63046 -> 0.65624` as `Gamma/H0` grows `0.25 -> 2`, passing every `Delta z_R>1e-3` step.

New descriptive C6 fingerprint: redshift-moving scale-sign pivot around `k~0.0026..0.0067 h/Mpc`, approximately insensitive to decay-rate amplitude along the sampled ray.

### Updated cross-mechanism picture

The current common abstraction is increasingly **motion/localization of response features**, not a universal fixed coordinate:

- GDM viscosity: spatial transition + interaction localization;
- designer f(R): Compton transition + interaction localization;
- WDM: free-streaming cutoff with nearly time-separable response;
- DCDM: lifetime/epoch control + temporal response localization, plus a descriptive scale-sign pivot.

This is now supported by a truly withheld family, but remains an organizing principle rather than a frozen G7 law.
