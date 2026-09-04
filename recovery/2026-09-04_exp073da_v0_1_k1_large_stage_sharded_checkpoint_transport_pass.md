# DSIR immutable recovery — Exp073DA v0.1 K1 large-stage sharded-checkpoint transport PASS

Date: 2026-09-04. Scope: DSIR only; RTK/RQIR excluded.

Authoritative hosted process: run/job/head `33881849442 / 101052130027 / 7e6e570aff26fba974f8eb10fbecf04eb3495ca4`; artifact `9940168039`; independently downloaded ZIP SHA256 `a2df2e2ec20308a6d0f5c04e540ad817098ae13002a066dbcac253778e6741d7`; raw receipt SHA256 `4710776bacbbd2b4bf764688da85c445255495d8e89396512a9d08d61ae6d5f3`; self-test SHA256 `2a48b1b307cd52c8da2e060802e60ed6f2aa97cbff8c91874421d1f877c5a707`.

Frozen classification: `K1_LARGE_STAGE_SHARDED_CHECKPOINT_TRANSPORT_PASS`, accounting `+0/+0`. `science_gate_scored=false`, `wm_s3_authority_created=false`, `exp073bu_activated=false`, and no DES-scale numerical science was executed.

Cause and result: the proven whole-tree `ci/dsir_checkpoint_git_sync_v0_2.sh` cannot safely carry Exp073BU's large stages. The frozen stock MCM payload alone is 4,831,838,208 bytes before FITS overhead; each dense NSIDE=4096 `<f8` map is 1,610,612,736 bytes. The existing transport copies the whole checkpoint into a Git tree, conflicting with GitHub's enforced 100 MB object/file and 2 GB push limits. This is an infrastructure/readiness finding, not a scientific failure.

Prospective repair layer: prereg commit/blob `c10580116420a4c01d73dc6307b0a9b100c3ac69 / f1244ebf0f0b70cc624aa12cd62710438cb2fbf4`; exact-byte sharding adapter commit/blob `5883481af17401d048e26d1a3b7816193e825653 / 72870dc0946f94b421ef104feea2daf34047434f`; auditor commit/blob `aa9763088dc492130e1d805048f1c3258bd6a528 / b4469c41307f9347fbfe1cec788e9b8a7a5bf8ba`; workflow commit `bcbe8c232fc290d1499a47388b2531b4d7f9bb74`; activation/head `7e6e570aff26fba974f8eb10fbecf04eb3495ca4`.

The frozen adapter caps Git-safe chunks at 64 MiB and prospective new-payload batches at 1 GiB, records exact chunk order/offset/length/SHA256 plus whole-file SHA256/source-head/contract/stage/replica/namespace identity, and restores only after exact reassembly verification. Hosted deterministic tests proved byte-exact roundtrip and fail-closed rejection of corruption, missing/reordered chunks and head-race model mutations.

Important boundary: K1 validates the sharded payload/manifest layer, not yet the actual incremental remote Git push/restore orchestration. A stage may not be declared remotely durable merely because local shards exist. The only permitted successor is a prospective remote-Git batch orchestration binding audit that implements exact lease/post-push verification and stage-final manifest semantics. Exp073BU home science remains forbidden until that layer is closed and re-bound to the six A/B stage boundaries.

During the activation push GitHub also emitted run `33881843095` against the manual Exp073BU science workflow with conclusion failure and zero jobs. No self-hosted job, input-confirmed dispatch, DES computation or scientific comparator ran; therefore this is workflow-validation/infrastructure noise `+0/+0`, not Exp073BU activation or a Wm_S3 scientific result. It remains to be diagnosed independently before scientific dispatch.
