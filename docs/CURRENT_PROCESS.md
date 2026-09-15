# DSIR current-process ledger

Updated: 2026-09-15. Scope: **DSIR only**. GitHub repository/Actions state, frozen DSIR4 preregistrations/contracts, terminal authorities and independent audit qualifications are authoritative. Chat is not authority.

## Numerical/reproducibility baseline
The numerical/reproducibility chain is terminal through V0.25. V0.25 classification remains `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. Historical independent `INVALID_PROVENANCE` remains scoped to the original producer binding; the separate V0.25 provenance-correction authority reconciled it without rewriting history.

Consolidated V0.26 R1 is the current prospective specification. Preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0`; machine contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`; R1 promotion merge `438ab2e6732512cf50c163719ade01575257b209`. Frozen denominator: 107 rows (DES 53 / BOSS 54), retained-ID SHA256 `44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7`, row-order SHA256 `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`; scientific `<1e-3`, technical `<1e-5`, requested-node `<=1e-12`, alpha tolerance `3e-10`, beta exact-target tolerance `1e-12`.

## Sentinel implementation/package chain
PR171 implementation is promoted and independently `QUALIFIED`; executor blob `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`, decision blob `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`. PR173 froze/promoted the acyclic package DAG `W -> A(W) -> L(A,W) -> static audit -> Q(W,A,L)` with exact candidate blobs W `19907175f0f3417ddee2aba6916d961c6be02e26`, A `4ba40e59e6a9d48636d95d07efab575e56ae0966`, L `9c217e41764d979bea12644fae372354241bc976`.

## Q candidate state
Exact Q candidate blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd` passed response-blind static run `35016371281` and independent funnel run `35016565037`. Terminal Q funnel authority `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_Q_FUNNEL_QUALIFICATION_V0_1.json` blob `43696ebc566c23871c0bcd94feca40bb9c03d82c`, verdict `QUALIFIED`, reached main before exact inactive-Q promotion merge `b7d65db1dacb355ddf2419a22cec38cc4b091c39`. Q remains stored at the inert candidate path; final Q path is absent.

## PR178 W/A staging
Exact W/A staging candidate head `15e7dbfb9c05744c026d5b03e5466267d802a2c7` passed pretrigger static run `35017254145` and independent funnel run `35017440323`. Terminal pretrigger authority `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_WA_PRETRIGGER_FUNNEL_QUALIFICATION_V0_1.json` blob `7c365449795d523d4ada39804c55c90e8c527a85`, verdict `QUALIFIED`, reached main via `9a14b804c0743023c1225a53d55865612b3d0a97` before PR178.

PR178 merge `d605a941b412bb9625bf2fc6fedb0c7d9f8e8293` has parents exactly authority-bearing main `9a14b804c0743023c1225a53d55865612b3d0a97` and audited candidate `15e7dbfb9c05744c026d5b03e5466267d802a2c7`. Relative to first parent it adds exactly four audited files, no deletions. Active-path W is exact blob `19907175f0f3417ddee2aba6916d961c6be02e26`; authority-path A exact blob `4ba40e59e6a9d48636d95d07efab575e56ae0966`; pretrigger auditor/workflow exact blobs `2dbc76f15ee3510111db2bbe7da3cefb496d027b` / `f039472f7a94cda2ccf088f2e0e36b90ef08dc5d`.

W is fail-closed to `push` on `main` for exact final-L path and has no `workflow_dispatch`. A binds W, requires separate final Q, deliberately does not bind L, and keeps full-107 false. Final L and final Q are absent. Exact PR178 promotion head has zero push Actions runs; no sentinel workflow executed during staging.

## Terminal post-promotion review
Hosted response-blind post-promotion run `35017910362`, run #1 / attempt #1 / push, job `104545919688`, completed success. Artifact `10417107515`, ZIP SHA256 `ce839f31ad5dfb164611df4cd49ee9b774c64cef7289e861944bb7e1c04e1c52`; inner receipt 1179 bytes, SHA256 `034c546a75dfccc94dfb31596bea4d1967a33bccff219bffe1641e58f4a32ed2`. It records L absent, final Q absent, exact-promotion push-run count zero, no CLASS solve, scientific-response read, covariance read, sentinel execution or full-107 authorization.

Independent audit `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_WA_PR178_POST_PROMOTION_FUNNEL_AUDIT_V0_1.md` blob `883393d170c32cc3b27022999a77c45bcb8defad` produced verdict **`CONFIRMED_SCOPED`**.

Terminal confirmation `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_WA_PR178_POST_PROMOTION_CONFIRMATION_V0_1.json` blob `500fbea5dbad463debf712bd466a3aaf8d9a7653` has classification `SENTINEL_WA_MAIN_STAGING_CONFIRMED_FAIL_CLOSED_FINAL_Q_PROMOTION_ADMISSIBLE`. Scope is only exact fail-closed W/A staging; this is not a sentinel scientific-response PASS.

## Current gate position
`V0.25 TERMINAL -> V0.26 R1 PREREGISTERED/QUALIFIED -> PR171 IMPLEMENTATION QUALIFIED/PROMOTED -> PR173 ACYCLIC PACKAGE QUALIFIED/PROMOTED -> Q CANDIDATE QUALIFIED+INACTIVELY PROMOTED -> PR178 EXACT W/A STAGED -> POST-PROMOTION CONFIRMED_SCOPED -> FINAL Q ABSENT -> FINAL L ABSENT -> SENTINEL SCIENCE NOT EXECUTED -> FULL 107 ROW CLOSED`.

## Exact next admissible action
Copy only exact Q candidate blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd` byte-for-byte to `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json` **without creating L**. Then perform a separate response-blind final-Q post-promotion audit. Final L creation and sentinel science are not authorized until that later audit is terminal. Full 107-row replay remains closed even after any future sentinel PASS until independent sentinel-result funnel audit plus distinct explicit full-replay launch authority.

## Interpretation boundary
No substantive sentinel response exists. Do not infer interpolation/grid/resolution/tolerance success, cross-host scientific reproducibility, execution-order independence, covariance/nuisance validity, statistical/model validity or physical dark-sector inference from static CI/provenance. Covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 and downstream science remain closed. Effect `+0/+0`; readiness `68%`; scientific frontier `67%`.

Latest Researcher handoff remains `docs/dsir4/handoffs/DSIR_FUNNEL_HANDOFF_V0_25_TERMINAL.md`; later state is carried by terminal authorities and auditor handoffs. `docs/ACTIVE_FRONTIER_2026-09-06.md` is historical. PR #168 remains governance-only and does not authorize F2-F7.
