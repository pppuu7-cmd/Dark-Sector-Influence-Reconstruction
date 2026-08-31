# DSIR recovery — Exp073BH hosted D2 timeout/external-cancellation class evidenced

**Date:** 2026-08-31  
**Scope:** DSIR only. RTK/RQIR excluded.  
**Scientific authority readiness:** **52.0%**  
**Draft/data readiness:** **53.714285714285715%** (display **53.7%**)

## Authority result

Exp073BH hosted run **33370998182** completed successfully at `2026-08-31T08:02:28Z` from head `f6c6cfd83828fef12ee2685fa6aa527b449d0e9a`.

Hosted diagnostic artifact:

- artifact id: **9750041348**
- name: `exp073bh-ba-execution-rootcause-f6c6cfd83828fef12ee2685fa6aa527b449d0e9a`
- digest: `sha256:d3abc316f9dbdc33fbcef4c17de3861ebde912bca88f99a645a957f66da14b77`
- frozen diagnostic status: **`BH_D2_TIMEOUT_OR_EXTERNAL_CANCELLATION_EVIDENCED`**
- scientific classification: **none**
- readiness increment: **`+0 Verified / +0 Draft-data`**

## Direct hosted evidence

The Exp073BA workflow frozen at the clean rerun contains `timeout-minutes: 360` for each compact replica job.

For BA run **33345968620**:

- compact B job `99350035503`: started `2026-08-31T00:54:52Z`, completed `2026-08-31T06:55:09Z`, duration **21617 s**; job conclusion `cancelled`; full-scale compact compute step conclusion `cancelled`.
- compact A job `99350035615`: started `2026-08-31T00:54:53Z`, completed `2026-08-31T06:55:10Z`, duration **21617 s**; job conclusion `cancelled`; full-scale compact compute step conclusion `cancelled`.
- configured job deadline: **360 min = 21600 s**.
- both hosted job durations are therefore 17 s beyond the nominal configured deadline, inside the prospectively diagnostic bookkeeping window used only for infrastructure metadata.
- compact comparator, finalizers and final comparator had no complete A/B inputs and remained skipped.

The diagnostic attempted to retrieve archived hosted job-log text but the log fetch failed; therefore `explicit_timeout_phrase_seen_in_any_hosted_log=false`. This does **not** license a stronger causal statement than the frozen D2 class. The durable conclusion is exactly: **both independent BA compact jobs reached the configured 360-minute execution boundary and were cancelled there; this is direct hosted metadata evidence for the frozen timeout/external-cancellation class.** Do not rewrite this as proven OOM, dependency failure, runner loss, or manual cancellation.

## Scientific firewall

Exp073BH is infrastructure/root-cause evidence only. It does not evaluate Wm_S1 exact repeatability and cannot classify the BA science result. No incomplete BA arrays are admitted as scientific evidence.

Immutable rules preserved:

- Exp073AQ remains permanent hosted exact-repeatability scientific FAIL.
- DES `NSIDE=4096`, ell `0..12287`, 39 bands, Wm `TE <- TE`, canonical `<f8 [39,12288]` remain frozen.
- any future Track-A comparator remains exact `numpy.array_equal` / canonical byte-SHA equality with no tolerance, ULP, rounding, averaging, majority vote, preferred-replica or closeness rescue.
- Exp073BD remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`; branch B cannot be preferred/salvaged.
- synthetic/infrastructure/provenance QA gets no scientific authority credit.
- no covariance/whitening/nuisance/quotient/relation/null/G8 information was read by BH.

## G7 order unchanged

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`

No G8 jump is authorized.

## Exact next gate

Before any new classifying heavy Wm_S1 run, freeze a **new Track-A execution successor** informed by BH_D2. It must inherit the entire BA scientific contract unchanged while changing only execution engineering needed to finish inside the hosted limit (for example checkpointable/blockwise work only after mathematical-equivalence validation, or another admissible execution environment). The successor must still produce two complete immutable compact replicas before exact comparison, then complete frozen finalizers and final exact comparison before any scientific PASS can exist.

No heavy successor is launched by this checkpoint itself.

## Exact chronology

- `2026-08-31T00:54:52Z` / `00:54:53Z`: BA compact B/A jobs start.
- `2026-08-31T06:55:09Z` / `06:55:10Z`: BA compact B/A jobs terminate cancelled after 21617 s each.
- `2026-08-31T07:06:51Z`: Exp073BH preregistration frozen in commit `48e39a3063b3c525feefd99d2821f7fcf77a8941`.
- implementation commit: `ea006ca40afce2388bc374b9593785d77a6748f0`.
- workflow freeze/tightening commit: `b44a87318a84a79a1d04c8a8e36295413c2be03e`.
- trigger/head commit: `f6c6cfd83828fef12ee2685fa6aa527b449d0e9a`.
- `2026-08-31T08:02:03Z`: hosted BH run `33370998182` created.
- `2026-08-31T08:02:23.681332+00:00`: diagnostic JSON generated.
- `2026-08-31T08:02:24Z`: immutable artifact `9750041348` created.
- `2026-08-31T08:02:28Z`: BH run terminal success.

`Verified: 52.0% | Draft/data: 53.7%`
