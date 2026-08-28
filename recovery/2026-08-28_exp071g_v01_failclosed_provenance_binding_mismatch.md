# Exp071G v0.1 — fail-closed provenance-binding mismatch

**Date:** 2026-08-28

## Terminal status

Run `33178800144`, job `98874344318` terminated before any Exp071G K2-vs-GDM science classification.

Status for scientific use:

`INVALID_FOR_SCIENCE__PREREG_INTERNAL_PARENT_BINDING_MISMATCH`

No Article-2 readiness credit is assigned to the failed science test itself.

## Exact failure

The preregistration required the recomputed GDM `cs2` vs `cv2` finite-bin-growth acute angle to equal the frozen Exp040 value

`1.3340128035605052 deg`

within `1e-8 deg`.

The Exp071G implementation, using the immutable GDM Weyl/slip parent run `32774198185` at the explicitly frozen `1e-7` local points, obtained

`1.2926742378142244 deg`.

The fail-closed assertion triggered before K2 primary angles or classification were emitted.

## Provenance diagnosis

The mismatch is expected once the two parent constructions are inspected:

- Exp040 consumes `data/derived/comparison_readiness/local_response_tangents_v0_1.json`.
- Its C3 records are not single-step `1e-7` tangents. They are frozen as:
  - `C3_GDM_cs2`: `positive cs2 local tangent mean of r/cs2 over cs2<=1e-6`
  - `C3_GDM_cv2`: `positive cv2 local tangent mean of r/cv2 over cv2<=1e-6`
  - provenance run `32759738560`
  - stored `source_step = 1e-8` is the minimum source step, while the construction explicitly averages the local branch.
- Exp071E/F instead bind the newer GDM Weyl/slip hard-regression parent run `32774198185` and use the single `1e-7` `cs2_1e-7` and `cv2_1e-7` responses.

Therefore Exp071G v0.1 preregistration accidentally imposed two different local-tangent conventions as if they were identical.

## Why the tolerance is not relaxed

The `1e-8 deg` integrity threshold is not changed after observing the mismatch. Doing so would hide a real provenance distinction and weaken the fail-closed design.

Instead v0.1 is retired without a science classification. A replacement protocol must freeze **before computing K2 growth angles** and must explicitly distinguish:

1. primary `1e-7` GDM tangents, preserving continuity with Exp071E/F;
2. frozen Exp040 averaged-local C3 tangents as a non-classifying sensitivity construction.

The replacement must reproduce each parent on its own terms rather than forcing equality between them.

## Gate state

- G7 OPEN
- G8 OPEN
- G9 OPEN

No observational or discovery claim is affected.
