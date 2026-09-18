# DSIR-2 Table 1 — terminal comparison matrix v0.1

**Date:** 2026-08-28  
**Status:** final-table source under current Article-2 scientific closure  
**Frozen separator where applicable:** `45 deg`  
**Metric:** theory/provider-space Euclidean metric for the Exp071 angle chain unless stated otherwise.

## Table 1. Response specificity across representation and nuisance geometry

| Control / experiment | Response representation | Physical comparison object | GDM `cs2` angle | GDM `cv2` angle | Terminal interpretation |
|---|---|---|---:|---:|---|
| Exp071E | equalized `(r_W, Delta_slip)` | K2 positive oriented displacement | `18.9257°` | `58.9127°` | K2 overlaps `cs2`; static metric augmentation is not generically specific |
| Exp071F — matter only | `r_P` | K2 positive oriented displacement | `19.2231°` | `19.0371°` | matter-direction overlap with both tested GDM axes |
| Exp071F — 3 channel | equalized `(r_P,r_W,Delta_slip)` | K2 positive oriented displacement | `19.0749°` | `50.1667°` | adding matter to Weyl+slip still leaves `cs2`-like overlap |
| Exp071H | finite-bin temporal transform of matter response | K2 positive **ray** | `138.1006°` | `137.0973°` | preregistered oriented-ray PASS; not a sign-invariant line claim |
| Exp071H — descriptive line diagnostic | same temporal response | line spanned by measured K2+ response | `41.8994°` | `42.9027°` | retrospective geometry only; below 45°, no retroactive reclassification |
| Exp071I | raw CLASS `Delta ln|t_tot|` | K2 positive **ray** | `165.9455°` | `164.7113°` | strong oriented-ray separation; `t_tot` is not tracer RSD |
| Exp071J | per-redshift constant-in-`k` projected `t_tot` shape | K2 positive **ray** | `166.4387°` | `164.9271°` | robust oriented separation; ~83% raw norm retained |
| Exp071K | same projected velocity shape under all leave-one-`k/z` deletions | K2 positive **ray** | global min across primary tests `157.8212°` | global min included in same 24-test set | all 24 primary support-deletion tests remain >45° |
| Exp071J — nuisance-line geometry | projected `t_tot` shape | line spanned by K2+ | `13.5613°` | `15.0729°` | large positive-ray angles correspond to small sign-invariant line angles |
| Exp071L | projected `t_tot` shape | fresh K2− branch / physical two-sided K2 line | `13.5503°` | `15.0709°` | **FALSIFICATION:** K2 nuisance line overlaps both GDM directions |
| Exp071M | transfer-only `Delta ln|t_tot|` | K1 primordial-tilt two-sided nuisance | undefined | undefined | `INVALID_FOR_SCIENCE`: K1 response exactly zero; representation does not resolve nuisance |
| Exp071N | `Delta ln P_R + 2 Delta ln|t_tot|`, projected shape | K1+ oriented branch | `36.0622°` | `37.8458°` | K1 becomes resolvable but positive branch already lies below 45° |
| Exp071N | same velocity-power shape | K1− oriented branch | `143.9378°` | `142.1542°` | opposite orientation of same nuisance line |
| Exp071N — physical line | same velocity-power shape | two-sided K1 nuisance line | `36.0622°` | `37.8458°` | **FALSIFICATION:** independently resolved K1 nuisance line overlaps both GDM directions |

## Integrity and geometry notes

### K2 velocity line — Exp071L

- `angle(K2−,K2+) = 179.9078021°`.
- nonlinear antisymmetry error = `0.00299225`.
- fresh K2− versus line prediction from Exp071J differs by only `0.0110453°` (`cs2`) and `0.0020188°` (`cv2`).
- fresh parent `P` and `t_tot` reproduce with max relative difference `0.0` against `1e-10`.

### K1 transfer kernel — Exp071M

- `n_s(ref)=0.965`, `n_s(+)=0.970`, `n_s(-)=0.960`.
- both K1 transfer-only responses are exactly zero on frozen support.
- no normalization and no angle are scientifically allowed.

### K1 velocity-power recovery — Exp071N

- `angle(K1−,K1+) = 179.9999991°`.
- antisymmetry error = `0.0`.
- retained projected norm fraction: K1 `0.625535`; GDM `cs2` `0.827183`; GDM `cv2` `0.837239`.
- fresh parent `P` and `t_tot` reproduce with max relative difference `0.0` against `1e-10`.
- original non-classifying diagnostic branch/line mismatch was corrected; frozen primary four-angle classification is unchanged.

## Caption draft

**Table 1.** Response-space comparisons become progressively stricter as the physical comparison object is upgraded from a selected oriented displacement to a two-sided nuisance line and as representation resolvability is enforced. Static matter/metric combinations retain a K2 sound-speed-like ambiguity. A selected positive K2 ray appears strongly separated after temporal and velocity transformations and remains so under amplitude and support controls, but the physical two-sided K2 velocity line overlaps both tested GDM directions. Primordial tilt K1 is exactly unresolved in transfer-only `t_tot`, making angular comparison undefined; restoring the primordial-spectrum contribution resolves K1 in a common velocity-power response, where its two-sided nuisance line again overlaps both GDM directions. Angles are theory/provider-space quantities and are not survey distinguishability statements.

## Paper-safe takeaway

The table must be read vertically as a **falsification hierarchy**, not as a ranking of the “best” channel. The decisive variables are representation resolvability and the physically allowed nuisance geometry, not the magnitude of one selected oriented angle.
