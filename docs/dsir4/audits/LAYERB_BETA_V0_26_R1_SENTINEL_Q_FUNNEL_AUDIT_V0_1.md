# DSIR V0.26 R1 sentinel package-Q funnel audit

Status: **INDEPENDENT FUNNEL AUDIT — QUALIFIED**  
Date: 2026-09-15  
Effect: `+0/+0`.

## Result reviewed

Reviewed the inactive package-qualification candidate Q on branch `research/v026-r1-sentinel-package-q-v02`, exact head `0b22c49010e86d09f7c881381613c99fb40c70aa`, against exact reviewed main `f9de6daceb887bf86b47b02f71cae70b70f173a0`.

Candidate Q path:
`docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_CANDIDATE_V0_1.json`, git blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd`.

The reviewed branch is exactly three commits ahead of the reviewed main and changes exactly three files, all additions and no deletions:

- Q candidate JSON;
- response-blind Q static auditor;
- hosted Q static-audit workflow.

No historical science result, terminal numerical authority, active workflow, final launch authority, final launch descriptor, or final Q path is modified or created by the candidate branch.

## Authorization check

Current main authority permits construction of an inactive Q only after the exact PR173 W/A/L package was statically audited, externally funnel-audited, exactly promoted, and post-promotion confirmed. That chain is present on the reviewed main.

The Q candidate remains inert because it is stored under `docs/dsir4/authority_candidates/`. Its embedded future content may authorize exactly one preregistered sentinel run only after the exact Q is independently qualified and copied byte-for-byte to its final authority path in the frozen activation order. This audit itself does not authorize a sentinel science execution.

Full 107-row execution remains false.

## Exact Q and package bindings

The Q candidate binds:

- W candidate git blob `19907175f0f3417ddee2aba6916d961c6be02e26`;
- A candidate git blob `4ba40e59e6a9d48636d95d07efab575e56ae0966`;
- L candidate git blob `9c217e41764d979bea12644fae372354241bc976`;
- sentinel executor git blob `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`;
- sentinel decision finalizer git blob `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`;
- implementation contract git blob `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`;
- R1 contract git blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`;
- R1 promotion authority git blob `cdbcea2622564d40aa9d1edc045a5808f8cdd1c4`;
- PR171 implementation qualification git blob `5d042377fa48d896865db0ada11508015c74e350`;
- PR173 funnel authority git blob `ed3cec954d2077e6b5a6daab5da53e8fe72cc2e0`;
- PR173 post-promotion confirmation git blob `499fec9c1738f410bb1d4c714da96f60ac1de7ab`;
- inactive package contract git blob `26806597e651fb22956de59f102c0ad24d11c576`.

The acyclic edge structure remains W -> A(W) -> L(A,W) -> static audit -> external funnel -> Q. A binds W but not L; L binds exact A and W. No mutual A/L exact-blob cycle is introduced.

## Immutable upstream audit receipts

PR173 package static audit:

- run `34959657394`, job `104349972403`;
- artifact `10393170033`;
- ZIP SHA256 `e95c4675db77a2ecd864d21e39dfdccffe289ed61a84ece95182f22c46e16184`;
- inner `launch_package_static_audit.json`, 1348 bytes, SHA256 `133df1d2753c9228198a15be792fdcbbf99da243efeccdb785d610aad7dc5ee5`.

PR173 external funnel audit:

- run `34960031527`, job `104351158807`;
- artifact `10392992058`;
- ZIP SHA256 `73ea7849b60dd65b20e2f93144c7afbb0f7dc7bd09ae8e0e9cfe0e3d63801c59`;
- inner `funnel_audit.json`, 1728 bytes, SHA256 `f525feaf938e99a9282ea97619842ded9883ac54219e60c9bbdd3f34f934a1aa`;
- verdict `QUALIFIED`.

Both receipts independently bind the exact W/A/L object and contain no CLASS solve or scientific-response read.

## Q static audit

Q static auditor:
`ci/layerb_beta_v026_r1_sentinel_q_static_audit_v0_1.py`, git blob `5d1070460041c3a3a4ebd18df3164145eaeb5aec`.

Q static workflow:
`.github/workflows/layerb-beta-v026-r1-sentinel-q-static-audit-v0-1.yml`, git blob `59ee8c2847404dcaa7cf08aea6f92889519d872f`.

Hosted run `35016371281`, run #1 / attempt #1 / event `push`, exact head `0b22c49010e86d09f7c881381613c99fb40c70aa`, job `104540706572`, terminal success.

Artifact `10416085334`, name `layerb-beta-v026-r1-sentinel-q-static-audit-v0-1`, ZIP SHA256 `f6902133327a78fcb387c114f6ef31f5f8cd37024827bab9655b6708410be14b`.

Inner `q_static_audit.json`: 1739 bytes, SHA256 `0f654ce0e5609189eb675da623a8c4adfa6042479bcfebe7e8f5e9ce7a869a2e`.

Receipt token:
`PASS_LAYERB_BETA_V0_26_R1_SENTINEL_Q_STATIC_AUDIT_PLUS_0_PLUS_0`.

The receipt confirms the exact Q/W/A/L bindings, candidate storage inertness, all four active/final paths absent, future exact-copy Q semantics, full-replay authorization false, full-107 false, `class_solver_invoked=false`, `scientific_response_read=false`, and `covariance_read=false`.

## Independent funnel implementation

Independent audit branch: `audit/v026-r1-sentinel-package-q-v02`.

Funnel auditor:
`ci/dsir_v026_r1_sentinel_q_funnel_audit_v0_1.py`, git blob `7f210b2dd3c6f98b94f2786ab8afe6d906670aa7`.

Funnel workflow:
`.github/workflows/dsir-v026-r1-sentinel-q-funnel-audit-v0-1.yml`, git blob `9722b77118a3e56235011dc8b67dd5f0371342d0`.

The independent auditor does not import or execute the candidate Q auditor. It reads the exact candidate head as a git object, independently checks the base/head relationship and three-added-file diff, exact Q/W/A/L/code/upstream blobs, four negative active/final paths, the future W runtime Q contract, exact Q static run uniqueness, and independently downloaded Q/PR173 artifacts.

Hosted independent funnel run `35016565037`, run #1 / attempt #1 / event `push`, exact execution head `288457c1b08f82faef1accecc7734ba1b21dff09`, job `104541396827`, terminal success.

Artifact `10415269967`, name `dsir-v026-r1-sentinel-q-funnel-audit-v0-1`, ZIP SHA256 `d943607cf423708912b46962d9ba26c9e37ddc8eb1d63b6bd7ac1cb7c7b66520`.

Inner `q_funnel_audit.json`: 1549 bytes, SHA256 `96b824df3b9a9fc40f298b95e5f858aa6c72e4d740beb1fa66961c429208a1f3`.

Receipt token:
`QUALIFIED_DSIR_V0_26_R1_SENTINEL_Q_FUNNEL_AUDIT_PLUS_0_PLUS_0`.

Verdict: `QUALIFIED`. Classification: `SENTINEL_PACKAGE_Q_QUALIFIED_FOR_INACTIVE_PROMOTION_TO_MAIN`.

## Reproducibility and negative controls

The Q static audit and external funnel audit independently reproduce exact byte-level artifact identities. Neither audit launches or imports the future active sentinel workflow, invokes CLASS, reads a scientific response, or reads covariance.

At the reviewed Q head all four future active/final paths are absent:

- `.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml`;
- `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json`;
- `docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json`;
- `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json`.

The candidate branch cannot itself trigger sentinel science.

## Verdict and promotion boundary

**QUALIFIED** for inactive promotion only.

The exact next promotion sequence is:

1. persist the Q-funnel qualification authority on main;
2. only then promote the exact inactive Q candidate object, preserving Q blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd` and its reviewed static files without mutation;
3. only after exact Q is qualified and present on main may a separate gate stage exact W and A without L;
4. W/A staging must undergo its own response-blind pretrigger static audit before final Q activation/final-L trigger work.

This review does **not** authorize staging W/A in the same promotion, does not authorize final L creation, does not authorize sentinel science execution, and does not authorize the full 107-row replay.

Covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, statistical/model inference, and physical dark-sector inference remain closed. Readiness and scientific frontier are unchanged.
