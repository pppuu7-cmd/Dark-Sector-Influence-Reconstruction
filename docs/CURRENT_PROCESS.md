# DSIR current-process ledger

Updated: 2026-09-16. Scope: **DSIR only**. GitHub repository/Actions state, frozen DSIR4 preregistrations/contracts, terminal authorities and independent audit qualifications are authoritative. Chat is not authority.

## Numerical/reproducibility baseline

The numerical/reproducibility chain remains terminal through V0.25. V0.25 classification is `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`; historical `INVALID_PROVENANCE` remains scoped to the original producer binding and was reconciled by the separate provenance-correction authority without rewriting history.

Consolidated V0.26 R1 remains the current prospective specification: preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0`, machine contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`, 107 rows (DES 53 / BOSS 54), alpha canonical-32769 tolerance `3e-10`, beta exact-target-union tolerance `1e-12`, scientific strict `<1e-3`, technical strict `<1e-5`, requested-node binding `<=1e-12`. Full-replay accounting remains 738 CLASS constructions. None of this scientific content changed in the launch-governance work below.

## Frozen sentinel implementation

PR171 implementation remains independently `QUALIFIED` and promoted. Frozen active workflow content W blob `19907175f0f3417ddee2aba6916d961c6be02e26`; executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`; decision finalizer `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`; implementation contract `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`.

PR173 originally froze the acyclic package DAG `W -> A(W) -> L(A,W) -> static audit -> Q(W,A,L)` with original candidate A blob `4ba40e59e6a9d48636d95d07efab575e56ae0966`, L blob `9c217e41764d979bea12644fae372354241bc976`, and Q blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd`.

## W/A staging and old final-Q state

PR178 exactly staged active-path W and old authority-path A without L. Merge: `d605a941b412bb9625bf2fc6fedb0c7d9f8e8293`. Hosted and independent pretrigger/post-promotion audits established that staging was fail-closed and caused zero sentinel runs.

PR179 then promoted exact old Q blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd` to final Q path, merge `bcd1cfaaee2961fe4997d5789971547e3ea42955`, **without L**. PR179 head had zero push Actions runs.

Current final runtime paths before correction replacement are therefore:

- W present, blob `19907175f0f3417ddee2aba6916d961c6be02e26`;
- final A present, old blob `4ba40e59e6a9d48636d95d07efab575e56ae0966`;
- final Q present, old blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd`;
- final L **absent**.

No sentinel scientific run has occurred.

## Historical runtime-chain blocker remains authoritative for old A/Q

PR179 post-promotion review discovered that frozen W consumes six Q bindings at the **top level**, while old Q stores the same correct values only inside nested sections. A complete consumer-chain review then found that executor `require_launch_authority()` consumes A field `promotion_authority_git_blob_sha1`, while old A contains the same correct PR169 blob only as `r1_promotion_authority_git_blob_sha1`.

The broader historical blocker authority remains `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_RUNTIME_CHAIN_SCHEMA_BLOCKER_V0_2.json`, blob `09190c92c1311b66e953d19ef3811d63a0bf871a`, verdict `BLOCKED`, classification `SENTINEL_RUNTIME_CHAIN_SCHEMA_INCOMPATIBILITY_REQUIRES_GOVERNANCE_ONLY_A_L_Q_CORRECTION`. It is not rewritten by the correction result.

## Prospectively frozen corrected A-L-Q package

Research branch `research/v026-r1-sentinel-runtime-chain-correction-v02`, exact audited head `d3b32cd341ce16b5494024dfa9785a2480173dc1`, freezes a governance-only correction with no W/executor/decision/R1 change:

- corrected A candidate `1c9945dd00b137f3e202efa14bf4112fffebf8af`: old A plus exactly one alias `promotion_authority_git_blob_sha1`;
- corrected L candidate `fa7014435f0a5688def2124898ddd01d0c0183aa`: old L with only its exact A binding updated;
- corrected Q candidate `f7b97f47d9e771e3d3ea78875da5a45962160cd0`: six W-required top-level bindings plus exact corrected A/L bindings.

Exact source diff relative to correction base `78f96f2c60db385f88a391b7fd046dd312176019`: six governance/audit files only; no scientific/executable runtime file changed. Correction contract blob: `01af3648bd3dc640acf35c7b0b7c116334b61cfe`.

Hosted response-blind full-chain static audit run `35025081430`, job `104570053404`, run #1 / attempt #1, terminal success. Artifact `10419525675`; ZIP SHA256 `82929104a6129f5f8f8bd465ef574b4ce55c172411415c19458de9bb8fe5fa0f`; inner receipt SHA256 `b326cfc032a2e758d9565b4672d34f5f18ec61d8475ee5d23601e037bf3dab39`.

## Independent correction funnel result is now terminal and confirmed scoped

The formerly pending independent response-blind funnel audit is now terminal:

- run `35025283328`, run #1 / attempt #1, event `push`, terminal `success`;
- exact audit head `5c34da32133f086d53c5af939e3e6e80147786d3`;
- sole job `104570712438`, terminal `success`;
- artifact `10419217250`;
- Actions ZIP digest and independent redownload SHA256 both `51fa034ee9b3ff4bafe2f030db1b619adabd5f8e69b3b88cbd626ed126e53592`;
- inner `runtime_chain_correction_funnel_audit.json`: 1607 bytes, SHA256 `7edd0cdaa06a43c7c42518993891c63c071c3feda2c187ff9b60f767b1a1b9d6`;
- `science_runs.json`: 36 bytes, SHA256 `a2790a384d7d281e7395679000c35d27768d89dbd7052f725b8f4688beb59915`, exact count zero.

Producer receipt verdict is `QUALIFIED`, classification `SENTINEL_GOVERNANCE_ONLY_A_L_Q_RUNTIME_CHAIN_CORRECTION_QUALIFIED_FOR_AUTHORITY_FIRST_PROMOTION`, effect `+0/+0`.

Independent auditor review `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_RUNTIME_CHAIN_CORRECTION_FUNNEL_AUDIT_REVIEW_V0_1.md` gives verdict `CONFIRMED_SCOPED`. Terminal confirmation authority is `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_RUNTIME_CHAIN_CORRECTION_FUNNEL_CONFIRMATION_V0_1.json`.

The confirmed scope is narrow: exact corrected A/L/Q are qualified for **authority-first no-L promotion sequencing only**. No CLASS solver ran; no scientific response or covariance was read; no sentinel-science run exists at the correction head. The review does not establish sentinel numerical validity.

## Current funnel position

`V0.25 TERMINAL -> V0.26 R1 PREREGISTERED/QUALIFIED -> PR171 IMPLEMENTATION PROMOTED -> PR173 ORIGINAL PACKAGE -> PR178 OLD W/A STAGED -> PR179 OLD FINAL Q PRESENT -> HISTORICAL RUNTIME CHAIN BLOCKED -> V0.2 GOVERNANCE-ONLY A-L-Q CORRECTION STATIC PASS -> INDEPENDENT CORRECTION FUNNEL QUALIFIED -> AUDITOR CONFIRMED_SCOPED -> CORRECTED A/Q NOT YET PROMOTED -> FINAL L ABSENT -> SENTINEL SCIENCE NOT EXECUTED -> FULL 107 ROW CLOSED`.

## Exact next admissible action

The correction-funnel confirmation authority is now on main. The next admissible gate is **exact replacement of old final A and old final Q with corrected A `1c9945dd00b137f3e202efa14bf4112fffebf8af` and corrected Q `f7b97f47d9e771e3d3ea78875da5a45962160cd0`, without creating final L**.

After that replacement, a separate response-blind fail-closed post-replacement audit is mandatory. Only a later terminal authority may authorize creation of exact corrected L `fa7014435f0a5688def2124898ddd01d0c0183aa` as the unique new-file one-run sentinel trigger.

Do not create L early. Do not launch or rerun sentinel science from this authority. Full 107-row replay remains closed even after any future sentinel PASS until independent sentinel-result funnel audit plus a distinct explicit full-replay launch authority.

## Interpretation boundary

No substantive sentinel response exists. Do not infer interpolation/grid/resolution/tolerance success, cross-host scientific reproducibility, covariance/nuisance validity, statistical/model validity or physical dark-sector inference from governance/static audits. Covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 and downstream science remain closed. Effect `+0/+0`; readiness `68%`; scientific frontier `67%`.
