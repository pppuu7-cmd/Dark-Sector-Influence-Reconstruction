# DSIR checkpoint — Exp071E terminal joint metric-direction control; Exp073R1 v0.5 still live

Date: 2026-08-28
Branch authority: `main`

## Scope and ordering guard

This checkpoint records an independent theory-space validation result while the priority G7 physical-support prerequisite remains live. It does **not** change any frozen acceptance criterion and it does **not** authorize skipping the required G7 ordering:

1. validated physical forward/power-input bridges;
2. preregistered physical support-validity mask;
3. covariance restriction/whitening;
4. nuisance tangent rank/SVD;
5. quotient/relation/null control;
6. only then a fresh G8 withheld family.

## Exp071E terminal result

Authoritative workflow run: `33191061359`

Workflow: `Exp071E K2 vs GDM joint metric direction v0.1`

Head SHA: `d6ca028337cef0994e16a6c8f09f93eacf41e6d8`

Run conclusion: `success`

Frozen prospective semantics asserted by CI:

- `threshold_deg = 45.0`
- `frozen_z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`
- `frozen_k_h_mpc = [0.001, 0.003, 0.01, 0.03, 0.1]`
- 5 K2 models
- parent artifacts downloaded immutably from Exp071D run `33176559280` and GDM run `32774198185`

Observed terminal classification:

`K2_JOINT_DIRECTION_OVERLAPS_CS2_ONLY_EXP071E`

Numerics:

- minimum K2-to-`cs2` angle = `18.840917160801848 deg`
- minimum K2-to-`cv2` angle = `58.89487692347028 deg`
- GDM joint `cs2`-`cv2` angle = `56.96321243480535 deg`

Artifact:

- id `9693749249`
- name `exp071e-k2-gdm-joint-direction-d6ca028337cef0994e16a6c8f09f93eacf41e6d8`
- digest `sha256:4d00b2e767bd57f6eb57a23fbf600766c9752bff951515faed008373a3bdaeca`

## Scientific interpretation

Exp071E is a **scientific partial-overlap / negative-specificity result**, not an infrastructure failure. Under the preregistered 45-degree criterion, the joint K2 metric-direction family is not cleanly separated from both local GDM nuisance axes: it substantially overlaps the `cs2` direction (18.84 deg), while remaining separated from the `cv2` direction (58.89 deg).

Therefore no claim of generic K2-vs-GDM joint-direction uniqueness is permitted. The defensible statement is narrower: within this frozen joint metric-direction construction K2 retains separation from the `cv2` axis but not from `cs2`. This is consistent with preserving prior negative/two-sided K2 specificity findings rather than retroactively selecting only favorable oriented directions.

This result is theory-space validation only. It does not substitute for observational support validity, covariance restriction/whitening, nuisance tangent quotienting, or withheld-family validation.

## Priority G7 prerequisite status

Canonical Exp073R1 v0.5 workflow run `33175886694` remains `in_progress` as checked on 2026-08-28. Its `source-index` stage had already completed successfully and the authoritative sequential `metacal-map` whole-stream reconstruction remained active. No duplicate heavy run was launched in this iteration.

Until a genuine canonical Exp073R1 PASS exists, the physical support-validity mask and all later G7 stages remain closed.

## Classification summary

- Exp071E: **terminal scientific partial-overlap result** (`cs2` overlap; `cv2` separation).
- Exp073R1 v0.5: **reproduction/infrastructure INCOMPLETE**, not scientific FAIL.
- G7 downstream: **closed by ordering guard**.
