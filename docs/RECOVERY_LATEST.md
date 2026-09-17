# DSIR recovery — latest authoritative continuation state

Updated: 2026-09-17. Scope: **DSIR only**. GitHub repository/Actions state, frozen authorities and terminal artifacts are authoritative; chat is not authority.

## Frozen science boundary

V0.25 remains terminal `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains frozen: 107 DES53+BOSS54 rows; alpha `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions. Full107 and all downstream science remain closed.

Never rerun consumed identities: V0.2 `35181812498`; V0.6 `35251121404`; V0.7 static qualification `35253515074`; V0.8 repair-primitive qualification `35264388526`; completed one-shot captures.

## V0.6 terminal state

Canonical V0.6 workflow registry ID `360576929` was prospectively bound and one-shot run `35251121404` executed run #1 / attempt #1. Frozen terminal decision is `INVALID_DIAGNOSTIC_PROVENANCE`; decision artifact `10510805424`, outer SHA256 `fe664cd5ef1c5adf959d40f7c179550074b380ccd0c3805dc361661bf97bc574`, inner decision SHA256 `e57bcb39736bf80dac16900cb124ec66429e00bc1e20c31df0b05ea5f2a86325`. Aggregate observed `HTTP 415 Unsupported Media Type` retrieving lane artifact ZIPs. This transport defect remains open and must be prospectively qualified in a new identity.

V0.6 is immutable and must not be rerun.

## Source-root-cause correction — definitive

The old V0.6 audit's claim that canonical V0.1 lacked final LF is superseded. Dedicated provenance capture run `35253892736`, workflow ID `360739640`, artifact `10511577132` (outer SHA256 `55268b6f8302b269583e6546d61a8504c82bc644ed04d8ddb87765fd6122cf24`, inner result SHA256 `2d6d5d5cd5fc0cefc5f9ab53b64379a4a1e722638188d5734f3e6c051ccca9c7`) established:

- working tree = `git show` = exact Git blob;
- `git hash-object` = `24fa61685ab45e42e3ab0d453f5cb223c247ced6`;
- no checkout line-ending transform;
- actual V0.1 = 15248 bytes, SHA256 `f84d6fa7cf9e5b8014176fd480062b27aaf97947d4a5211c7fbb5c69f93634ba`;
- final LF present; 897 lines; at least one line not 16 lowercase hex chars.

Exact comparison with pre-v0.2 origin run `34954905127` / artifact `10390997654` proves a one-byte publication corruption:

- deleted ASCII `e` at zero-based byte offset `13182`;
- line 776, column 8 (1-based);
- correct origin token `3f9c8a9eeea3c9c8`;
- malformed committed token `3f9c8a9eea3c9c8`.

Applying that single deletion to the pre-existing origin serialization reproduces exactly committed V0.1 Git blob `24fa6168...` and SHA256 `f84d6fa7...`. The intact origin serialization is 15249 bytes, SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`, Git blob `ded43b233a71a631809111514c9dd35d0419af2d`, 897 valid lowercase hex16 words, and payload SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`.

Correct classification: `CANONICAL_V0_1_SINGLE_HEX_DELETION_CONFIRMED_AND_PRIOR_FINAL_LF_INTERPRETATION_SUPERSEDED`.

V0.6 source guard was therefore correct to reject the malformed published V0.1 object. This is not host disagreement.

## V0.7 closure

First V0.7 implementation was designed under the now-superseded final-LF hypothesis. One-shot static qualification `35253515074`, run #1 / attempt #1, terminated `INVALID_STATIC_QUALIFICATION` with `FileNotFoundError: canonical raw SHA256 mismatch`. Artifact `10512311250`: outer SHA256 `736b412c171afe1e04b30b5735fcd7a728c032f4f142e08b535a8bb964e91c9a`, inner SHA256 `260bf466611d9b5f7666246bcfb27601a94a6e99b1409a384c057241b548a072`. No CLASS/science/covariance was touched.

V0.7 is historical and closed. Do not rerun or mutate that identity.

## Corrected canonical V0.2 repair specification

A frozen V0.2 repair specification retains corrupt V0.1 as immutable evidence and defines corrected bytes as exactly V0.1 plus one inserted `e` at byte offset 13182. Successors must verify before payload use:

- corrected byte length `15249`;
- corrected SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`;
- corrected Git blob SHA1 `ded43b233a71a631809111514c9dd35d0419af2d`;
- 897 lowercase hex16 lines;
- payload length 7176;
- payload SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`;
- negative-control SHA256 `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800`.

Do not overwrite historical V0.1.

## Prospective population evidence

Historical V0.22 run `34875798025` had 32/32 eligible = `10 NATIVE_AVX512_ACTIVE + 22 NATIVE_AVX512_INACTIVE`. V0.2 later retained exactly 10 ACTIVE lanes while others died after fingerprinting at native GRID896 materialization. This is response-blind evidence that an exact corrected content-addressed producer could restore the censored INACTIVE class. It is not a science result or authorization.

## V0.8 repair-primitive qualification — terminal infrastructure failure

A scoped authority and independent static Critic authorized exactly one response-blind repair-primitive qualification, run #1 / attempt #1, with no CLASS, scientific response, covariance, diagnostic promotion, or diagnostic execution.

Marker-only launch commit `74a2a3de41da0d18be1642f955850525f2e7f786` triggered workflow ID `360747162`, run `35264388526`, job `105347779372`. The exact-identity verification step passed; the response-blind qualification computation ran and produced its result; immutable artifact upload passed; only the final classifier-reflection step failed.

Frozen artifact `10516021621`, name `layerb-beta-v026-r1-grid896-v08-repair-primitive-qualification-v0-1`, outer digest `sha256:7e64635f2d03d91c63e73b2d76d1f721b0105535a5c6af4d4792f59320d1d001`, contains `result.json` SHA256 `6a3c62aeeee4191c163bbbd17f26e3f50c5d385fcedb48f0e3473b77afff7093` with:

- classification `INVALID_V0_8_REPAIR_PRIMITIVE_QUALIFICATION`;
- error `HTTPError: HTTP Error 401: Server failed to authenticate the request...`;
- `class_solver_invoked=false`;
- `scientific_response_read=false`;
- `covariance_read=false`;
- effect `+0/+0`;
- interpretation ceiling `INFRASTRUCTURE_PROVENANCE_ONLY`.

Because the qualification code performs all corrected-canonical local identity checks before the first network artifact request, reaching the HTTP 401 establishes that those local checks reached the network phase without exception. It does **not** complete qualification of the repair pair.

The historical source artifact remains present and independently retrievable: artifact `10508904186` downloaded with outer SHA256 exactly `b8897d2b5ff336be7f472bca740f1bc4b82e301b7b6ca0381127627a71050ffd` and contains sole member `R01.json`. Therefore this V0.8 result is classified narrowly as `INFRASTRUCTURE_FAILURE_V0_8_QUALIFICATION_HTTP_AUTH`, not as canonical-repair falsification, numerical reproducibility failure, or science failure.

Terminal decision authority: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_GRID896_V0_8_REPAIR_PRIMITIVE_QUALIFICATION_TERMINAL_V0_1.json`.

V0.8 qualification identity is consumed and must not be rerun.

## Current authorization state

- V0.6: terminal `INVALID_DIAGNOSTIC_PROVENANCE`, rerun false.
- V0.7 static qualification: terminal `INVALID_STATIC_QUALIFICATION`, rerun false.
- canonical V0.1 single-hex deletion: independently confirmed; old final-LF interpretation superseded.
- corrected canonical V0.2 repair specification: frozen.
- V0.8 repair-primitive qualification: terminal `INFRASTRUCTURE_FAILURE_V0_8_QUALIFICATION_HTTP_AUTH`, rerun false.
- same V0.8 diagnostic promotion/execution: **closed**.
- one new prospective transport-qualification successor may be authored, but its execution requires a separate prospective scoped authority/audit.
- successor sentinel science: **closed**.
- full107/downstream: **closed**.

## Exact next stage

`AUTHOR_ONE_NEW_RESPONSE_BLIND_TRANSPORT_QUALIFICATION_IDENTITY_WITH_EXPLICIT_HTTP_AUTH_REDIRECT_DEFECT_HYPOTHESIS;_SEPARATE_METADATA_REQUEST_FROM_ARCHIVE_REDIRECT_DOWNLOAD;_DO_NOT_FORWARD_REPOSITORY_AUTHORIZATION_TO_REDIRECTED_STORAGE_HOST;_FREEZE_EXACT_ARTIFACT_ID_DIGEST_MEMBER_AND_NO_SCIENCE_CRITERIA;_INDEPENDENTLY_AUDIT_BEFORE_ONE_SHOT_EXECUTION;_NO_V0_8_DIAGNOSTIC_PROMOTION_OR_EXECUTION_YET`.

The successor repair criterion is falsifiable and narrow: it must retrieve historical artifact `10508904186`, verify outer ZIP SHA256 `b8897d2b5ff336be7f472bca740f1bc4b82e301b7b6ca0381127627a71050ffd`, require sole member `R01.json`, and confirm the receipt did not invoke CLASS or read scientific response. Any authentication, redirect, digest, member, or provenance mismatch is terminal FAIL for that successor.

Scientific effect remains `+0/+0`; science remains `NOT_EVALUATED`.
