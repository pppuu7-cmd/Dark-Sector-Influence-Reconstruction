# DSIR research log — 2026-09-08 — Exp073HB pinned-upstream build block

Scope: DSIR only. This entry preserves the frozen DSIR4 scientific ordering and classification boundaries.

## Reconciliation

`WW_S3_S3` is now `SCIENTIFIC_AUTHORITY_ADMITTED` from hosted recovery/admission run `34218457380`, job `102035691774 SUCCESS`, consuming GA artifact `10051382493` (`sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`) and emitting the frozen GA/GB PASS/admission markers. Historical GA terminal-comparator failure remains implementation/provenance `+0/+0`, not scientific FAIL.

After that admission, the next permitted gate is Exp073HB under prereg blob `fc5f08889f84e628cb789070abd9179a74ef7e04`.

## Exp073HB implementation and run

Deterministic exact-endpoint producer patcher was added in commit `09908cdea139deee26f79ec2b6b56a093250dfe9`; its pinned-Git-blob guard was tightened in `c2602fb42a289292cdc37394058a6fbcbc5c9042`; hosted build/static workflow was added in `38e25e208ea730399f293b6c1930c34de6cc7aee`; hosted solver dependency installation was added in `1df037bdb071f9b5c1cfa3e11f8978c88754b552`.

Hosted-only Exp073HB run `34223854538`, job `102053091684`, completed `failure`. The following portions succeeded before the failure:

- frozen prereg identity check;
- pinned upstream commit and pinned `perturbations.c` / `evolver_ndf15.c` Git-blob checks;
- deterministic patch application and `git diff --check`;
- static exact-endpoint semantic audit (`PASS_EXP073HB_STATIC_SEMANTICS_V0_1`);
- installation of the hosted GSL build dependency.

The deterministic patch receipt reported:

- patch SHA256 `01c0e0b1cadfaba58e312d054cb4ce3a50d210f3aeed7ea8ef73d58cab3969c5`;
- patched `source/perturbations.c` SHA256 `da7c427e383f1e9b83d7ff75ef82784c2fe89d91f9681e21e7805b7f354e7e79`;
- patched `tools/evolver_ndf15.c` SHA256 `b3967efaf7a45a3ec6c0144e892caab54f91c595bc726dc1704cfb812f9c0df6`.

## Exact failure classification

The failure occurs in `make -j2 class` while compiling **unchanged pinned upstream** `source/background.c`, not either file modified by the HB diagnostic patch. GCC reports at upstream lines around 611--695 errors including `case label not within a switch statement`, `break statement not within loop or switch`, and subsequent top-level `switch` / `return` parse failures.

This is therefore a pinned-upstream baseline/full-build blocker exposed by the HB build contract. It is classified exactly as:

`BLOCKED/IMPLEMENTATION_PLUS_0_PLUS_0`

Scientific FAIL contribution: `0`.

It MUST NOT be converted into scientific FAIL, `INVALID_FOR_SCIENCE`, or evidence against hypothesis `C2_IDE_LOCAL_TANGENT_CONE`.

## Why no automatic source repair was applied

The frozen HB prereg requires the pinned solver commit `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c` and a successful build of the patched pinned solver. Editing `background.c`, changing the upstream commit, weakening the audit to compile only selected translation units, or redefining the build-success requirement would alter the frozen provenance/build contract and potentially the solver scientific path. Those actions are therefore not safe infrastructure repairs under the current authority and were not performed.

No cosmological CLASS execution occurred. No 28-packet / 1792-byte payload was created. No home/self-hosted heavy run was started or duplicated.

## Current scientific/process status

- `WW_S2_S3 = SCIENTIFIC_AUTHORITY_ADMITTED`;
- `WW_S3_S3 = SCIENTIFIC_AUTHORITY_ADMITTED`;
- `Exp073HB = BLOCKED/IMPLEMENTATION_PLUS_0_PLUS_0`;
- `cosmological_run_started=false`;
- `record_payload_created=false`;
- `runtime_record_count=0`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false` for C2;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`;
- new scientific FAILs: `0`.

The next DSIR4 action remains resolution of the HB pinned-upstream build blocker under an explicit prospective authority that preserves scientific semantics; real C2 runtime remains NOT YET AUTHORIZED until raw-log validated HB PASS.
