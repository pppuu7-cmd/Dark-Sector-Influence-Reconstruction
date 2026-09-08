# DSIR recovery authority V27 — Exp073GA post-compute pruner recovery

Date: 2026-09-08

This file supersedes the GA-active operational portion of V26. Frozen scientific authority from earlier recovery records remains unchanged.

## Current admitted authority

1. `WW_S2_S2 = SCIENTIFIC_AUTHORITY_ADMITTED`.
2. `WW_S2_S3 = SCIENTIFIC_AUTHORITY_ADMITTED` via Exp073HF authority run `34189183845`.
3. `WW_S3_S3 = NOT_YET_ADMITTED` and is the only permitted active heavy target.

## Latest GA incident

Run `34189540992` at head `10e6fb67af7d6485fca3d1ecf2362e4622883417`:

- hosted audit `101944582891`: SUCCESS;
- self-hosted `home-science` `101944608861`: FAILURE after expensive Replica-A compute;
- final provenance admission `101964415971`: SKIPPED;
- partial/evidence artifact `10043979600`;
- digest `sha256:b859e658e1046c4d9905d589003a1d26aaf3e2601c51d9db361b48176226906a`.

Failure text: `fail-closed missing GA pruner token 'WW_S1_S1'`.

The frozen FM pruner does not contain literal `WW_S1_S1`; therefore the requirement was a false lexical implementation guard. Classification is strictly `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`, scientific FAIL = 0.

## Safe repair identity

- `ci/exp073ga_verify_and_prune_replica_v0_1.py` repair commit: `f52fa856eb029c64f744926eecf55f506fcf1da5`.
- repaired blob: `fc3e4d8444630e4b5a2dde0a052e1069b7887c01`.
- workflow binding/regression commit: `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`.

The repair removes only the nonexistent uppercase token guard. Frozen drivers, contract fingerprint, source pair/order `[3,3]`, same-field semantics, thresholds, hypothesis IDs, exact comparator and provenance-admission requirements are unchanged.

## Recovery run authority

Current recovery run: `34197207582`, head `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`.

- hosted audit `101967492875`: SUCCESS;
- self-hosted `home-science` `101967543808`: IN_PROGRESS at last inspection.

Exactly one heavy chain is permitted. Do not dispatch another GA or other heavy target while this run is active. The same durable checkpoint namespace is retained; reuse valid checkpoints where verifier rules permit, and never relabel invalid or incomplete evidence as terminal scientific evidence.

## Fail-closed continuation rule

If run `34197207582` reaches a valid terminal GA candidate, only then execute/accept the frozen `Exp073GB` provenance admission. `WW_S3_S3` becomes scientific authority only after explicit markers:

- `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`
- `classification=SCIENTIFIC_AUTHORITY_ADMITTED`
- `ww_s3_s3_authority_created=true`

Until then:

`WW_S3_S3 = NOT_YET_ADMITTED`

and downstream 14-window join is not authorized.

Never map infrastructure/provenance failures, `INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, or `OUTSIDE_DOMAIN` onto scientific FAIL.