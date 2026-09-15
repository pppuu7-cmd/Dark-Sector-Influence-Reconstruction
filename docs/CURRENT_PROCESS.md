# DSIR current-process ledger

Updated: 2026-09-15. Scope: **DSIR only**. GitHub repository/Actions state, frozen DSIR4 preregistrations/contracts, terminal authorities and independent audit qualifications are authoritative. Chat is not authority.

## Numerical/reproducibility baseline
The numerical/reproducibility chain is terminal through V0.25. V0.25 classification remains `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. Historical independent `INVALID_PROVENANCE` remains scoped to the original producer binding; the separate V0.25 provenance-correction authority reconciled it without rewriting history.

Consolidated V0.26 R1 is the current prospective specification. Preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0`; machine contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`; R1 promotion merge `438ab2e6732512cf50c163719ade01575257b209`. Frozen denominator: 107 rows (DES 53 / BOSS 54), retained-ID SHA256 `44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7`, row-order SHA256 `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`; scientific `<1e-3`, technical `<1e-5`, requested-node `<=1e-12`, alpha tolerance `3e-10`, beta exact-target tolerance `1e-12`.

## Sentinel implementation/package chain
PR171 implementation is promoted and independently `QUALIFIED`; frozen executor blob `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`, decision blob `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`.

PR173 froze and promoted the acyclic package DAG `W -> A(W) -> L(A,W) -> static audit -> Q(W,A,L)`. Candidate blobs W `19907175f0f3417ddee2aba6916d961c6be02e26`, A `4ba40e59e6a9d48636d95d07efab575e56ae0966`, L `9c217e41764d979bea12644fae372354241bc976`. PR173 package/static and external-funnel authorities remain terminal and scoped to launch governance only.

## Q candidate state
Exact Q candidate blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd` passed response-blind static run `35016371281` and independent funnel run `35016565037`; terminal Q funnel authority `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_Q_FUNNEL_QUALIFICATION_V0_1.json` blob `43696ebc566c23871c0bcd94feca40bb9c03d82c`, verdict `QUALIFIED`. Authority merge PR175 `a86209ed04a93d70f55efdd5f8035c0f09868c2a` preceded exact inactive Q promotion PR176 `b7d65db1dacb355ddf2419a22cec38cc4b091c39`. The Q object remains at its inactive candidate path; the final Q authority path is absent.

## W/A pretrigger qualification and PR178 staging
After inactive Q promotion, exact staging candidate head `15e7dbfb9c05744c026d5b03e5466267d802a2c7` passed pretrigger static run `35017254145` and independent pretrigger funnel run `35017440323`. Terminal W/A pretrigger authority `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_WA_PRETRIGGER_FUNNEL_QUALIFICATION_V0_1.json` blob `7c365449795d523d4ada39804c55c90e8c527a85`, verdict `QUALIFIED`, entered main via PR177 merge `9a14b804c0743023c1225a53d55865612b3d0a97` before PR178 staging.

PR178 merge `d605a941b412bb9625bf2fc6fedb0c7d9f8e8293` has parents exactly `9a14b804c0743023c1225a53d55865612b3d0a97` and audited candidate head `15e7dbfb9c05744c026d5b03e5466267d802a2c7`. Relative to first parent it adds exactly four audited files. Current active-path workflow W is exact blob `19907175f0f3417ddee2aba6916d961c6be02e26`; current authority-path A is exact blob `4ba40e59e6a9d48636d95d07efab575e56ae0966`; pretrigger static auditor/workflow blobs remain `2dbc76f15ee3510111db2bbe7da3cefb496d027b` / `f039472f7a94cda2ccf088f2e0e36b90ef08dc5d`.

The active workflow is fail-closed by trigger topology: push to `main` only, exact final-L path only, no `workflow_dispatch`; A binds W, requires separate package Q, deliberately does not bind L. Final L is absent and final Q is absent. Exact promotion head `d605a941b412bb9625bf2fc6fedb0c7d9f8e8293` has zero push Actions runs, therefore no sentinel workflow executed during PR178 promotion.

## Post-promotion evidence awaiting durable independent confirmation
Hosted response-blind post-promotion audit run `35017910362`, run #1 / attempt #1, job `104545919688`, completed success on audit head `4d0076f155e36326263c1b420f9944e57c4690b9`. Artifact `10417107515`, ZIP SHA256 `ce839f31ad5dfb164611df4cd49ee9b774c64cef7289e861944bb7e1c04e1c52`; inner `wa_post_promotion_audit.json` 1179 bytes, SHA256 `034c546a75dfccc94dfb31596bea4d1967a33bccff219bffe1641e58f4a32ed2`. Receipt says `CONFIRMED_SCOPED` for fail-closed staging, with no CLASS solve, no scientific-response read, no covariance read, no sentinel run and no full-107 authorization. This receipt is supporting static/provenance evidence, not a scientific result, and requires independent funnel review before final-Q promotion.

## Current gate position
`V0.25 TERMINAL -> V0.26 R1 PREREGISTERED/QUALIFIED -> PR171 IMPLEMENTATION QUALIFIED/PROMOTED -> PR173 ACYCLIC PACKAGE QUALIFIED/PROMOTED -> Q CANDIDATE QUALIFIED+INACTIVELY PROMOTED -> PR178 EXACT W/A STAGED FAIL-CLOSED -> POST-PROMOTION STATIC RECEIPT TERMINAL SUCCESS -> INDEPENDENT CONFIRMATION PENDING -> FINAL Q ABSENT -> FINAL L ABSENT -> SENTINEL SCIENCE NOT EXECUTED -> FULL 107 ROW CLOSED`.

## Exact next admissible action
Independently audit PR178 post-promotion state and persist exactly one scoped verdict. If confirmed, only then may exact Q candidate blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd` be copied byte-for-byte to `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json` **without creating L**. That final-Q promotion must itself be re-audited before final-L creation. Sentinel science is not authorized now. Full 107-row replay remains closed even after any future sentinel PASS until a separate independent sentinel-result funnel audit and distinct explicit full-replay launch authority.

## Interpretation boundary
No substantive sentinel response exists. Do not infer interpolation success, resolution/tolerance stability, cross-host scientific reproducibility, execution-order independence, covariance or nuisance validity, statistical/model validity, or physical dark-sector inference from static CI/provenance. Covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 and downstream science remain closed. Effect `+0/+0`; readiness `68%`; scientific frontier `67%`.

Latest Researcher handoff remains `docs/dsir4/handoffs/DSIR_FUNNEL_HANDOFF_V0_25_TERMINAL.md`; later state is carried by terminal authorities and auditor handoffs. `docs/ACTIVE_FRONTIER_2026-09-06.md` is historical and cannot override the later DSIR4 authority chain. PR #168 remains governance-only and does not authorize F2-F7.
