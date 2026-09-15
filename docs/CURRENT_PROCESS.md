# DSIR current-process ledger

Updated: 2026-09-16. Scope: **DSIR only**. Repository/Actions state, frozen DSIR4 contracts and terminal authorities are authoritative. Chat is not authority.

## Scientific baseline remains unchanged

V0.25 remains terminal numerical classification `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains the prospectively frozen successor specification: preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0`, contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`, 107 rows (DES 53/BOSS 54), alpha tolerance `3e-10`, beta exact-target tolerance `1e-12`, scientific strict `<1e-3`, technical strict `<1e-5`, exact-node binding `<=1e-12`. Full-replay accounting remains 738 CLASS constructions.

No full-107 authority exists. Covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537, statistical/model inference and physical inference remain closed.

## Frozen sentinel implementation

Frozen implementation identities remain:

- active W `.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml`, blob `19907175f0f3417ddee2aba6916d961c6be02e26`;
- executor `ci/layerb_beta_v026_r1_sentinel_v0_1.py`, blob `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`;
- decision `ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py`, blob `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`;
- implementation contract blob `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`.

The historical old-A/Q runtime-schema blockers remain historical facts. They were corrected through the independently audited governance-only A-L-Q correction chain.

## Corrected runtime package was promoted and independently checked

Corrected governance identities:

- A `1c9945dd00b137f3e202efa14bf4112fffebf8af`;
- L `fa7014435f0a5688def2124898ddd01d0c0183aa`;
- Q `f7b97f47d9e771e3d3ea78875da5a45962160cd0`.

PR #184 merge `41ef654d7552b670c20d3202249d7687bae5f870` replaced final A/Q only; L remained absent. Hosted post-replacement run `35032839418` and independent funnel run `35032991806` both passed response-blind checks, reproduced the minimal A/Q deltas, confirmed W->Q and executor->A compatibility, recorded zero sentinel-science runs at the replacement head, and read no scientific response/covariance.

A separate exact-one-run L-gate authority was then promoted by PR #185 merge `2ca2d4c35f9dcfe2be00e573598e6189f987508d`. Authority path:

`docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_EXACT_L_GATE_AUTHORITY_V0_1.json`

blob `1c1819ee6aa7a48597770d9bc9116185d061a49c`.

It authorized exactly one new-file final-L creation / one first-attempt sentinel run, explicitly forbade rerun, and kept full-107 false.

## Exact L trigger and consumed first attempt

PR #186 merge `9a333294f3acb80201c5f6ed5b74918c1c767232` added exactly one runtime path relative to first parent `2ca2d4c35f9dcfe2be00e573598e6189f987508d`:

`docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json`

with exact L blob `fa7014435f0a5688def2124898ddd01d0c0183aa`. No A/Q/W/executor/decision/R1 file changed in the trigger operation.

This created exactly one sentinel workflow run at the trigger head:

- run `35033268924`;
- run #1 / attempt #1;
- event `push`;
- exact head `9a333294f3acb80201c5f6ed5b74918c1c767232`;
- terminal conclusion `failure`.

The first attempt is **consumed**. Do not rerun it.

## First-attempt failure occurred before science

Hosted jobs:

- authorize job `104596462857`: `failure`;
- materialize-plan: `skipped`;
- lane matrix: `skipped`;
- decision job `104596495504`: `failure` because current-run authorization did not succeed;
- decision finalizer: `skipped`;
- run artifacts: zero.

Therefore no source-plan materialization, no lane execution, no CLASS scientific solve and no sentinel decision artifact occurred. There is **no sentinel scientific classification** from attempt #1.

Authorize traceback is exact embedded Python line 48:

`assert added.count(launch)==1`

All A/Q/L/package assertions preceding that line were reached before the traceback and are independently reproducible as passing. The repository tree is also correct: the staging commit and merge both show exact L as added, and the net first-parent-to-merge diff contains exactly one added L.

## Exact platform-contract root cause

Frozen W reconstructs added files from `github.event.commits[*].added`. GitHub Actions documentation states that the push payload exposed to Actions does **not include** the commit-level `added`, `removed`, and `modified` attributes. Source checked 2026-09-16:

`https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#push`

The frozen code uses `c.get('added', [])`; under the documented Actions payload this deterministically falls back to `[]`, giving effective `added.count(launch)=0`. Thus the exact frozen event guard is unsatisfiable even though the repository diff correctly contains one added L.

This is a pre-science workflow/event-validation defect, not an interpolation, solver, tolerance, reproducibility or physical-science result.

## Fail-closed interim authority on main

PR #187 merge `f85d679fd4e8a16b83e7b44fd74911149e868746` persisted:

- `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_PRELIMINARY_FAILURE_AUDIT_V0_1.md`, blob `387e13ac2f1c88d0405c7b3f7a41886cd1e276af`;
- `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAIL_CLOSED_INTERIM_V0_1.json`, blob `8f898f3579ac55db4bfd3b7cc6a12cad04a4a613`.

The interim authority explicitly forbids rerun of `35033268924`, a same-nonce second attempt, final-L modification/removal/recreation, full 107-row replay and downstream science. It does not claim a sentinel scientific result.

## Current evidence gate

Hosted forensic audit branch: `audit/v026-r1-sentinel-first-attempt-forensic`.

Exact current forensic head `c5502bc124f502cb4ef1c19300fcdf87f260089b`; forensic run `35033678449` is pending GitHub-hosted runner execution. It is designed to persist run/jobs/artifacts snapshots plus authorize log, map traceback line 48 back to the exact frozen W source, reproduce all preceding package predicates and record the documented Actions push-payload root cause.

After an immutable forensic receipt, a separate independent first-attempt failure funnel audit is required before a terminal result authority is written.

## Current funnel position

`V0.25 TERMINAL -> V0.26 R1 QUALIFIED -> PR171 IMPLEMENTATION -> CORRECTED A/Q PROMOTED -> POST-REPLACEMENT AUDITS PASS -> EXACT L-GATE AUTHORITY -> EXACT L TRIGGER -> SENTINEL RUN #1/ATTEMPT #1 CONSUMED -> AUTHORIZE EVENT-GUARD FAILURE BEFORE SCIENCE -> RERUN FORBIDDEN -> FORENSIC/FUNNEL TERMINALIZATION PENDING -> FULL 107 ROW CLOSED`.

## Exact next admissible action

Complete forensic run `35033678449`, independently audit its immutable evidence, and persist a terminal first-attempt result authority.

Do **not** rerun run `35033268924`. Do not modify/remove/recreate final L. Do not silently patch W and call it the same attempt. Any future scientific sentinel requires a separately prospectively frozen successor launch-governance package/workflow with a new trigger identity and independent static/funnel qualification.

A future successor guard should validate the aggregate `before...after` repository diff (or equivalent first-parent tree diff), rather than absent commit-level file lists in the Actions push payload.

Effect remains `+0/+0`; readiness `68%`; scientific frontier `67%`.
