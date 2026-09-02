# Exp073CF versioned continuation v0.1 hosted QA — PASS

Date: 2026-09-02
Classification: SYNTHETIC_NONCLASSIFYING_INFRASTRUCTURE_QA
Readiness delta: +0/+0

## Coordination

Immediately before this write, repository-wide GitHub Actions checks showed queued=0 and in_progress=0. No self-hosted run was launched.

## Frozen inputs

- preregistration commit: `36853b723b172a6038c6d3023805f08f37ffac72`;
- continuation wrapper commit: `ce818db7ae53376ba6e5f7934c24f4c5acb3c75c`;
- synthetic test commit: `748cf7778aa9ddd441a9cb7c051a2a9491fa4262`;
- hosted workflow/head commit: `69ffe9962c17e63c79d0fbcf80439ed73ccb4815`;
- checkpoint sync v0.2 helper commit: `bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1`.

Historical checkpoint payload authority remains unchanged:

- source commit `f9cb1eec582276776ddac3b1207686b1e01d3b6a`;
- historical checkpoint sync commit inside payload contract `96886916b41dce7f0a40807622928c841ef5fc58`;
- A root `5c7ccddb54afe1ad286d08abc6f7372aa5a11103` = 32/39;
- B root `ce9189a1ccaabc62708f753897b9cab5f51cb9f4` = 28/39.

## Hosted immutable evidence

Run `33585095288`, job `100107489860`, `ubuntu-latest`, terminal completed/success.

Artifact `9829783026`, name `exp073cf-continuation-v0-1-hosted-qa`, digest `sha256:b8324bc9305b02ad08326117d8f2f7cb6e2c78ec5fb473b03c3f23ff3d8f2f36`.

All workflow steps passed, including the synthetic compatibility test, source-hash binding, and immutable artifact upload.

## What the QA proves

1. The versioned wrapper fail-closes if frozen historical driver constants drift.
2. The wrapper forces `GITHUB_SHA` used by the historical payload contract to the historical attempt2 authority head rather than the fresh workflow head.
3. The historical `checkpoint_sync_commit=96886916...` remains inside the payload contract; no historical checkpoint fingerprint rewrite is performed.
4. The wrapper contains no v0.1 transport invocation and routes continuation push through `ci/dsir_checkpoint_git_sync_v0_2.sh` only.
5. Synthetic A-form and B-form checkpoint contracts restore exactly under unchanged historical provenance.
6. A synthetic completed row can be added while preserving pre-existing row bytes and the historical contract fingerprint.
7. Changed historical `source_commit` fails closed.
8. Changed historical checkpoint-sync contract field fails closed.
9. Previously hosted-tested v0.2 transport remains the separately bound durability path, including compare-and-push lease and exact post-push verification.

This is synthetic/infrastructure/provenance evidence only. It does NOT classify real-survey Wm_S2 repeatability and gives no readiness increment.

## Scientific authority preserved

Exp073CF attempt2 remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CF_ATTEMPT2`, +0/+0. Durable authority remains A 32/39 and B 28/39. Exp073BJ/BV/BW/BZ authority, Exp073AQ historical FAIL, Exp073BD no-downstream, frozen Article-3 order and thresholds are unchanged.

Article-3 readiness remains Verified 52.0% | Draft/data 53.7%.

## Exact next permitted gate

Perform the second static continuation binding/integration audit. It must verify a future successor workflow can:

1. exact-pinned restore A=`5c7ccddb54afe1ad286d08abc6f7372aa5a11103` and B=`ce9189a1ccaabc62708f753897b9cab5f51cb9f4` with v0.2;
2. invoke only `ci/exp073cf_continuation_wm_s2_v0_1.py` for resumed heavy computation;
3. keep all scientific arithmetic/thread/chunk/output/comparator/finalizer semantics frozen;
4. bind wrapper/prereg/v0.2 transport provenance separately from historical payload fingerprint;
5. preserve <=60 s heartbeat semantics;
6. fail closed on any restore-head, historical-contract, helper, threshold, or lineage mismatch.

No self-hosted successor is authorized until that second static audit passes and a separate prospective successor binding explicitly authorizes the run.
