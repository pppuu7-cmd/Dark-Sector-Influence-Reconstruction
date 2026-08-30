# DSIR Article 3 recovery checkpoint — Exp073X cancelled, Exp073X2 split repeatability launched

Date: 2026-08-30.
Strict Article-3 scientific repository readiness: **52%** (unchanged).
G7/G8/G9: **OPEN / OPEN / OPEN**.

## Authority-state correction

The earlier live pointer described Exp073X as running. That state is superseded.

Exp073X hosted run `33277263287`, job `99166064222`, head `62c66faec2123a05a2a8bc83b34a758737b33539` did not produce a final reusable authority artifact. It is recorded as:

`INCOMPLETE_INFRASTRUCTURE_RESOURCE_CANCELLED_NO_AUTHORITY_REUSE`

This is neither scientific PASS nor scientific FAIL. No incomplete Wm_S0 numerical output may be bound into production authority.

The infrastructure flaw in X was persistence topology: the implementation computed two exact `NSIDE=4096` NaMaster workspaces sequentially and persisted JSON/NPZ only after both completed. Therefore cancellation during the second part could discard a valid first computation. This observation changes execution topology only and does not alter the frozen angular operator.

## Exp073X2 prospective repair

The following chain was committed prospectively in this order:

1. preregistration commit `efe8a4e17638dfd9568fa710e24f56cd10526c6a`;
2. single-workspace replica implementation commit `df2eecd73ed0d8de080348ba155a2f1a3e84d7e1`;
3. strict replica aggregator implementation commit `8ec6f94ea9ddf3cc0a4c98e5af696d28d995b2b3`;
4. hosted workflow commit `a14047090d46e024965d1bd76b60830ef21616e9`;
5. workflow-freeze commit `5bd0ba084b00d963c670db6d04b1db6ea53e8f36`;
6. execution-only trigger/head commit `2403d9680e1d08a3853084034eb2878faa52b4e0`.

Hosted run created: `33300997298`.
Workflow: `.github/workflows/exp073x2-article3-des-n4096-wm0-maskonly-repeatability-v0-1.yml`.
State at checkpoint creation: **QUEUED/RUNNING AUTHORITY PENDING**; no PASS is asserted here.

## Frozen X2 scientific/angular contract

Unchanged from X:

- genuine DES Y1 mask route;
- `NSIDE=4096`, RING;
- NaMaster/PyMaster 2.7 lineage;
- Exp073R1 source-bin-0 count-map authority, exact hosted artifact digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- public DES Y1 redMaGiC lens mask exact SHA-256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`;
- frozen lens threshold `m <= 0.5 -> 0`;
- exact 39 frozen bandpowers with ell axis 0..12287;
- spin-0 × spin-2, selected `TE <- TE` response;
- no effective-ell/z/k shortcut and no fiducial-P weighting.

Only the execution topology changes: independent hosted replica A and B each compute and immediately persist exactly one workspace. A third lightweight aggregator may PASS only if frozen metadata match exactly, canonical `<f8` SHA-256 values match, and stored TE arrays satisfy `numpy.array_equal`.

## Anti-leakage state

X2 must not read or score:

- direct measured signal catalog for workspace construction;
- physical-support classification;
- retained-coordinate selection;
- fiducial-P weights;
- covariance/whitening;
- nuisance geometry/SVD/rank;
- quotient/relation/null information;
- G8 information.

Therefore X2 PASS, if obtained, is **non-classifying angular authority** and contributes **0 percentage points** to scientific readiness by itself.

## Exact chronology

- Exp073Z2 stable-direct radial authority had already PASSed non-classifying checks; readiness 52%.
- Exp073X was launched as exact Wm_S0 angular repeatability pilot.
- Exp073X ended without reusable final authority and is frozen as infrastructure INCOMPLETE, not science.
- A post-result reuse rule already forbids production reuse when X does not PASS; therefore no X array is inherited.
- Exp073X2 was preregistered before its implementation.
- Replica and aggregator code were committed after preregistration.
- Hosted workflow was committed after code.
- Freeze bound all last-modifying commit identities before trigger.
- Trigger commit modified only the X2 trigger file.
- GitHub Actions created run `33300997298` at head `2403d9680e1d08a3853084034eb2878faa52b4e0`.
- At this checkpoint, hosted authority remains pending and readiness remains 52%.

## Authorized continuation

While run `33300997298` is active, do not launch a duplicate X2. Independent work may audit authority/recovery and prepare, but must not trigger, the successor production expansion.

If and only if the hosted X2 aggregator PASS artifact exists and binds both independent replicas, use its exact Wm_S0 authority as the replacement pilot authority and then prospectively bind/freeze the remaining 13 angular tasks. If X2 is cancelled or fails infrastructure, preserve that outcome and repair infrastructure without changing the angular contract post hoc.

Only after the ordered 14-window exact angular authority is complete may it be joined with Exp073Z2 radial authority, Exp073AB row-to-operator mapping and Exp073W BOSS authority into the immutable full pre-support finite-operator candidate manifest. Real Layer A is forbidden before that manifest freeze.

DSIR remains independent of RTK and RQIR.
