# DSIR recovery V107 — JM active; parallel 16385 response-blind preflight

Date: 2026-09-11. Scope: **DSIR only**. RTK/RQIR excluded.

## Preserved scientific state
Recovered canonical Exp073JL remains independently verified `COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, activating only Exp073JM. Frozen science is unchanged: `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, exact physical support/masks/107-row accounting and lookup ceiling `1e-12`. Covariance restriction remains unauthorized; Wm_S3 remains unopened.

## Primary scientific-support computation
Exactly one recovered Exp073JM 4097->8193 support-convergence run is active:
- run/job `34548136827 / 103105092111`;
- head `ab9e29234781c94b80280aa0d7b16245a3e31804`;
- canonical requested grids 4097 -> 8193;
- pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`;
- capacities 9216 / parser 262144;
- eight sequential role-major solver lifetimes, max one live;
- inherited response-blind request plan, 4040 transfer calls;
- unchanged strict fourth-refinement classifier.

Latest verified status: all identity, build, CAMB and external-input gates PASS; `Execute frozen recovered Exp073JM 4097 to 8193` remains IN_PROGRESS. No partial response value has been consumed for adaptation.

## Parallel independent work
To avoid idle GitHub capacity without changing JM execution, workflow run `34548892789`, head `f3c724aa6009e7817d8d5bf383a68d629b98fe9c`, runs response-blind/non-scientific 16385 successor preflight lanes. These lanes do not read the JM result and cannot activate the successor branch.

### Static contract lane
Job `103107390283` completed success. Artifact `10180040376`; ZIP SHA256 `0705d8e522f975d7e4218b8f53deb2e2aa95bc390ad9c401ee764aaf458bc7f9`; `static.json` SHA256 `69b941116e8264698fd42ba6be81c4a623c9eaf8304fe6020f990b2ad8befa64`. Independently verified 18/18 `LAYERB_16385_RESOURCE_PREFLIGHT_STATIC_PASS_PLUS_0_PLUS_0`. No CLASS, no JM result, no scientific response. Durable authority commit `9fe5723526e176fee53a1d0df09dfcb457158cf7`.

### Build-envelope lane
Job `103107389831` completed success. Artifact `10180060523`; ZIP SHA256 `9b47f7cac4f5a86dc64d8907dc6febca908b77aea5eef63d1a5e72cf22a3d4d7`; `build.json` SHA256 `33f7dcfabcd99ff744051692f92cf420061c46c1fe42d0efda5e4250c8f9208b`. Independently verified `LAYERB_16385_CLASS_BUILD_ENVELOPE_PASS_PLUS_0_PLUS_0`: pinned CLASS-IV builds with exact one-replacement capacities 18432 / parser 524288. No JM result or scientific response read. Durable authority commit `1cdaab023f6953ef58dcb793151f183498292d57`.

### Canonical 16385 resource lane
Job `103107390094` is active. Identity, install and exact pinned CLASS-IV build stages PASS. `Execute branch-blind canonical 16385 resource pilot` is IN_PROGRESS. It uses exact dormant canonical 16385 bytes, four sequential roles and max one live, but does not execute the full 107-row next support rung and cannot create a next-rung convergence classification.

## Parallelization boundary
Do not parallelize the eight CLASS lifetimes inside JM: `max_live=1` and same-process raw operands are part of the frozen protocol. Parallelization is allowed only across independent response-blind/static/resource tasks that do not share scientific state and do not consume partial JM responses.

## Terminal transitions
1. Independently verify JM terminal artifact. Only its frozen terminal classification selects a post-JM branch.
2. Independently verify the 16385 resource-pilot artifact when terminal; this remains process/resource `+0/+0` regardless of JM outcome.
3. If JM CONVERGED, stop the support ladder and activate only the prospectively frozen fresh Layer-B scientific closure.
4. If JM NOT_CONVERGED, the already-frozen next support rung may proceed only after all dormant static/resource authorities are independently verified; exact canonical 8193->16385, no density/tolerance/estimator rescue.
5. Infrastructure failure activates neither scientific branch and permits only minimal process repair.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%** until the JM terminal support result is independently verified. Parallel preflight authorities are process/reproducibility `+0/+0` and do not change readiness.
