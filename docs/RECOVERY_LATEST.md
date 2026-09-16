# DSIR recovery — latest authoritative continuation state

Updated: 2026-09-16. Scope: **DSIR only**. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

## Terminal scientific/numerical baseline

V0.25 remains terminal: `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. Its historical producer provenance defect was separately corrected without rewriting the historical authority/result. Numerical/reproducibility chain remains terminal through V0.25; statistical/model and physical dark-sector layers remain unopened.

V0.26 R1 is prospectively frozen under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`. Frozen denominator/criteria remain: 107 rows = DES 53 + BOSS 54; alpha route `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions. These values must not be changed by the current governance work.

## Sentinel implementation and consumed first attempt

Frozen identities: W `19907175f0f3417ddee2aba6916d961c6be02e26`; executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`; decision `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`; implementation contract `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`; corrected A `1c9945dd00b137f3e202efa14bf4112fffebf8af`; corrected L `fa7014435f0a5688def2124898ddd01d0c0183aa`; corrected Q `f7b97f47d9e771e3d3ea78875da5a45962160cd0`.

PR #186 merge `9a333294f3acb80201c5f6ed5b74918c1c767232` created the exact final L as the one authorized trigger. Actions science run `35033268924`, workflow `359060727`, run #1 / attempt #1, is terminal failure **before science**. Authorize job `104596462857` failed at frozen W event guard `assert added.count(launch)==1`; materialize-plan and lane were skipped; science artifact count is zero; no CLASS scientific response, covariance or sentinel classification exists. The repository tree diff itself has the correct one-file L addition; the failure is the workflow's use of commit-file-list fields not supplied by the Actions push payload it receives.

Historical fail-closed interim authority blob `8f898f3579ac55db4bfd3b7cc6a12cad04a4a613` is preserved. **Never rerun run `35033268924`. Never create a same-nonce second attempt. Never modify/remove/recreate final L.** No full-107 or downstream science follows from this failure.

## Immutable forensic evidence

Forensic branch head `c5502bc124f502cb4ef1c19300fcdf87f260089b`; auditor blob `63b6a0db41ff5e0e3c36be605596fb1c5aee0f1d`; workflow blob `4d09b78d3a586d3c4f7e42573a7bdac4454d3a48`. Exact run `35033678449`, run #3 / attempt #1, job `104597783801`, terminal success. Exactly one artifact id `10422924571`; ZIP SHA256 `226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b`; producer receipt SHA256 `207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e`; producer classification `SENTINEL_FIRST_ATTEMPT_AUTHORIZATION_EVENT_GUARD_BLOCKED_BEFORE_SCIENCE`. This evidence is immutable and response-blind; it is not a science PASS.

## PR #190 hardening chain

Original PR190 candidate was independently reviewed and terminally qualified by authority `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_PR190_QUALIFICATION_V0_1.json`, blob `74b10d5d326ec6984edec986fe1bbc368a73b4f6`, verdict `QUALIFIED`. Required prospective corrections were: bind the exact forensic artifact/run/digests; live-enumerate exact science workflow/head and reject duplicate/rerun history; recursively reject artifact/tree extras; require exact manifest relative names/cardinality; ensure future hosted workflow has full graph/exact historical SHAs; fresh response-blind static re-audit before any failure-funnel execution.

Those corrections were frozen at open/draft PR #190 exact head `5731b605afdc35bd85d3a2014a9e135719a07697`, base `52662ca7a21b3a32377f9b3afe6cfe9d290d6cca`. Independent compare shows exactly two non-runtime changed files. Target auditor blob: `f7eff337e511baa25d51e5b0c333a97534e1bbc3`. Target contract blob: `3369e5cdd2086ca22dca6bfa575054286fd1dcd7`. No hosted failure-funnel workflow exists on that target and no execution is authorized there.

## Independent hardened-PR190 static re-audit — terminal

Frozen re-auditor blob `4bf1b3867a953b61e62225735883628869218ded`; re-audit workflow blob `5db1a2580c22ca2c65d9b0f0d87aa42940f402bd`; exact re-audit head `ece06ed801c65aa336a06ee8b421e9812b8e1e58`.

Hosted run `35036894735`, workflow id `359177543`, event push, run #1 / attempt #1, is now **completed/success**. Exact-head Actions enumeration returns exactly one run. Only job `104607902297` is success. Exactly one artifact exists: id `10425156161`, `dsir-v026-r1-first-attempt-failure-funnel-pr190-reaudit-v0-1`. Actions ZIP digest is `sha256:760f3093f1482461412c433358843c86b477b9d42eae88c7a7be48c04323b9d1`; independent download SHA256 matches exactly.

Artifact contents are exactly two files:
- `pr190_failure_funnel_reaudit.json`: 1633 bytes, SHA256 `a3426a0dd1a6e5392450c38df3bab1b7c9fd6534f47a6c56dc5a3131ca129ce0`;
- `pr190_failure_funnel_reaudit.sha256`: 105 bytes, SHA256 `84f29443de7f45c278c25640052144965509009b0d1538d72709d3c2a6b76d5d`.

The manifest exactly binds `safe/pr190_failure_funnel_reaudit.json` to the receipt SHA above. Producer re-audit verdict is `QUALIFIED`; exact classification is `PR190_HARDENED_FAILURE_FUNNEL_CANDIDATE_STATICALLY_QUALIFIED_FOR_SEPARATE_HOSTED_WORKFLOW_AUTHORING_ONLY`. It records duplicate/rerun exact-head fail-closed, recursive ZIP-extra rejection, recursive extracted-tree-extra rejection, basename-collision manifest rejection, and all science/execution authorizations false.

Independent Funnel Auditor review of that terminal static result found no new invalidating static counterexample. Verdict: **`CONFIRMED_SCOPED`**.

Durable audit: `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_PR190_REAUDIT_FUNNEL_AUDIT_V0_1.md`, commit `7e23139342dcf60e93b1ad7b399a9da9ede1d26e`.

Terminal confirmation authority: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_PR190_REAUDIT_CONFIRMATION_V0_1.json`, commit `92f6779edc504ef1e9553a79e0abe4da696cd420`, blob `d2fe264e2866b9f490a7523a32f341fb7cc08d0b`.

Auditor handoff: `docs/dsir4/handoffs/DSIR_FUNNEL_AUDITOR_HANDOFF_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_PR190_REAUDIT_V0_1.md`, commit `e17de91639b471558f8ad2de11ca4f856a0c9f68`, blob `6e681714410b596aa212a19df7e9bb73139b698b`.

`docs/CURRENT_PROCESS.md` reconciliation commit: `cd1b0a11888d126bfef771a57b01779e5a249676`.

## Current funnel position and interpretation ceiling

`V0.25 TERMINAL -> V0.26 R1 QUALIFIED -> CORRECTED A/Q PROMOTED -> EXACT L-GATE AUTHORITY -> EXACT L TRIGGER -> RUN #1/ATTEMPT #1 CONSUMED -> PRE-SCIENCE EVENT-GUARD FAILURE -> HISTORICAL INTERIM BLOCKED -> FORENSIC RUN #3 TERMINAL SUCCESS -> PR190 ORIGINAL CANDIDATE QUALIFIED WITH CORRECTIONS -> PR190 HARDENED HEAD 5731b605 -> INDEPENDENT STATIC RE-AUDIT RUN 35036894735 TERMINAL SUCCESS -> STATIC RE-AUDIT CONFIRMED_SCOPED -> HOSTED FAILURE-FUNNEL WORKFLOW NOT YET AUTHORED/AUDITED -> FULL 107 ROW CLOSED`.

Interpretation ceiling is governance/provenance/static implementation only. No CLASS solve or scientific response was reviewed. Green static CI is not numerical science, statistical/model validity, nuisance removal or physical dark-sector evidence. Effect remains `+0/+0`; readiness remains `68%`; scientific frontier remains `67%`.

## Exact authorized next stage

`PROSPECTIVELY_AUTHOR_SEPARATE_FROZEN_HOSTED_FAILURE_FUNNEL_WORKFLOW_CANDIDATE_AND_AUDIT_BEFORE_EXECUTION` only.

Next admissible sequence:
1. Preserve exact hardened PR190 and terminal re-audit identities/hashes above.
2. Author a **separate non-executed** hosted failure-funnel workflow candidate that exact-hash-binds hardened PR190 auditor/contract, immutable forensic producer/artifact identities, and required live exact-head science-run enumeration.
3. Prospectively freeze that workflow/code before execution.
4. Conduct a separate independent response-blind static audit with fail-closed negative controls.
5. Only a later terminal authority may decide whether one hosted failure-funnel execution is admissible.

Until then: **do not execute the failure funnel; never rerun run `35033268924`; never create a same-nonce second attempt; never modify/remove/recreate final L; do not run successor sentinel science; do not run full 107 rows; keep covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537 and all downstream statistical/model/physical science closed.**
