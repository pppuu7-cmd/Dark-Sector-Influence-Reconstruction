# DSIR recovery — Article 3 IZ observed / JA running — V63

Date: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved scientific authority
All prior admitted DSIR scientific authority remains unchanged. Repaired Exp073IR run/job `34432102035 / 102729564736`, artifact `10134905199`, remains exactly `NUMERICALLY_UNRESOLVED_EXP073IR`: zero invalid rows, `f_B=0`, retained 107, exact production-vs-dense maximum `0.9998247463807295 > 1e-3`, covariance restriction unauthorized. Exp073IV remains historical support-invalid; IW/IY/IX support reproducibility authorities remain preserved. No tolerance rescue.

## Newly closed — Exp073IZ
Exp073IZ native-grid mechanism run/job `34452935477 / 102792610244`, head `2367abfb48538cac0750c024eebf77d47b4e057d`, completed infrastructure-success and was raw-log/artifact validated as `NATIVE_GRID_MECHANISM_OBSERVED_PLUS_0_PLUS_0`, token `PASS_EXP073IZ_NATIVE_GRID_MECHANISM_OBSERVED_V0_1`.

Artifact `10142351750`; GitHub digest and independently downloaded ZIP SHA256 both equal `2d479e359b82ce735d5b630610836598a1cc510d7a605f99e5bf40b5bc914748`.

Observed response magnitudes over kpd `{10,20,40,80}`:
- alpha-left probe `(z,k)=(0.7000000000000001, 0.002502504647141259 Mpc^-1)`: `15.004842009744834, 0.0026296528687907994, 6.017543332745845, 8.879123658118715`; adjacent relative differences `0.9998247463807295, 0.9995630022546774, 0.3222818417171559`.
- beta-symmetric probe `(z,k)=(0.9351, 0.01860440444314368 Mpc^-1)`: `12.060403107625461, 0.003871989520121133, 6.347953676595353, 0.6721100135109737`; adjacent relative differences `0.9996789502402558, 0.9993900413082097, 0.8941217835301767`.

Exact post-consumption algebraic decomposition of the validated artifact shows the mechanism is dominated by cancellation between a comparatively stable endpoint-value derivative and a large model-dependent interpolation-fraction/grid-motion term. For alpha, endpoint-value signed terms at kpd 20/40/80 are about `-114.3338758, -114.3203919, -114.3141069`, while grid-fraction terms are `+114.3365055, +108.3028486, +105.4349832`. For beta, endpoint-value signed terms are about `-617.9812704, -613.9518233, -613.7185496`, while grid-fraction terms are `+617.9773984, +607.6038696, +613.0464396`. This decomposition is support interpretation only and creates no new science authority.

The pattern is not monotone convergence with simple grid refinement. Therefore no replacement of the original Exp073IR 10-vs-20 gate is authorized from IZ alone.

Durable IZ authority: `docs/dsir4/authority/EXP073IZ_ARTICLE3_LAYERB_NATIVE_GRID_MECHANISM_OBSERVED_V0_1.json`, creation commit `dc835be2b4a250a47a21dc3b3eef2df625ed19e8`.

## Prospectively frozen next diagnostic — Exp073JA
Preregistration: `docs/dsir4/prereg/EXP073JA_ARTICLE3_LAYERB_HIGH_DENSITY_CANCELLATION_DIAGNOSTIC_V0_1.md`, commit `6cc634bf956a414c653b364cda38604c6aa147bc`.
Implementation: `ci/exp073ja_article3_layerb_high_density_cancellation_v0_1.py`, commit `3f285cd0461c9ee7f8c8ae9d8e4d91e4a680b273`.
Workflow/launch head: `.github/workflows/exp073ja-article3-layerb-high-density-cancellation-v0-1.yml`, commit/head `b510d33339530f7d0643e158ff0bf3200f869ee1`.

Exp073JA is support-only and uses the same two frozen probes and exact `h=1e-4` response/interpolation arithmetic at prospectively frozen kpd `{80,160,320,640}`. It additionally records exact signed endpoint-value and grid-fraction cancellation terms. These high-density values are diagnostic only and cannot retrospectively redefine Exp073IR or authorize covariance/model science.

## Current authoritative process — Exp073JA
- workflow: `exp073ja-article3-layerb-high-density-cancellation-v0-1`;
- run ID: `34457952958`;
- job ID: `102808675330`;
- branch/head: `main / b510d33339530f7d0643e158ff0bf3200f869ee1`;
- checkpoint namespace / durable checkpoint: N/A, complete GitHub-hosted support diagnostic;
- start/registration: `2026-09-10T08:57:13Z`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership none;
- last observed state: IN_PROGRESS; prospective contract/lineage SUCCESS, frozen stack installation active;
- expected valid classification: `HIGH_DENSITY_CANCELLATION_OBSERVED_PLUS_0_PLUS_0`; infrastructure invalid: `INVALID_INFRA_PLUS_0_PLUS_0`;
- scientific effect: always `+0/+0`; covariance/model authority forbidden.

## Exact next action
On terminal Exp073JA, inspect steps and first causal failure if any; download/read artifact and verify ZIP digest/provenance. If valid, inspect both probe sequences through kpd 640 and exact cancellation decomposition. Only if the sequence supplies a defensible numerical mechanism may the next experiment prospectively define a numerical-resolution architecture; otherwise continue mechanism isolation. Never weaken the original `REL_TOL=1e-3` criterion or rewrite historical Exp073IR.

## Frozen boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
