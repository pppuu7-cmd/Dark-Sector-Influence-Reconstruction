# Recovery — remaining WW autonomous heavy queue frozen through S3S3

Date: 2026-09-06. Scope: DSIR only.

## Purpose

Preserve the prospectively frozen autonomous sequence of every remaining heavy WW angular job from the current Exp073FM frontier through final `WW_S3_S3`, without requiring a new chat instruction between successful steps. This note records infrastructure and preregistration only; it does **not** promote any future target to scientific authority before its own heavy exact A/B gate and provenance admission pass.

## Current live frontier

- Exp073FM / `WW_S1_S1` run `34050657030`, home job `101533574294`, head `f0caca0c3e812710e5958ee13348a150d045a7d8`.
- At the latest reconciliation the home job remains `IN_PROGRESS` inside the frozen A/B science step.
- Do not inspect partial numerical output and do not launch a competing self-hosted heavy job.
- Canonical post-terminal admission remains Exp073FR prereg blob `aa08636426dd48142c3a3da7c032f1075a1be1f9`.
- Automatic FM terminal support-consumer verifies terminal evidence first; only after PASS does it generate/run the canonical FR admission. FR PASS dispatches Exp073FS.

## Frozen autonomous queue

The allowed heavy sequence is:

`Exp073FM WW_S1_S1`
`-> terminal support-consumer`
`-> Exp073FR S1S1 provenance admission`
`-> Exp073FS WW_S1_S2`
`-> Exp073FT S1S2 admission`
`-> Exp073FU WW_S1_S3`
`-> Exp073FV S1S3 admission`
`-> Exp073FW WW_S2_S2`
`-> Exp073FX S2S2 admission`
`-> Exp073FY WW_S2_S3`
`-> Exp073FZ S2S3 admission`
`-> Exp073GA WW_S3_S3`
`-> Exp073GB final S3S3 admission`
`-> STOP HEAVY AUTOQUEUE`.

Each successor heavy workflow may start only after the predecessor's independent scientific authority admission token is present. Exact science FAIL, provenance FAIL, malformed evidence, resource/infrastructure block, or missing admission evidence stops the chain fail-closed. No successor is launched on workflow success alone.

## Existing S1 successors

### Exp073FS / WW_S1_S2

- science prereg blob `80c6af017b47d51db3f588221749fb152577b0e5`;
- admission Exp073FT prereg blob `072bdeae68e86312142e980fe2015f979e7b117f`;
- heavy workflow blob `157850a2ae01b7c58c0bfac20df6360525f3a198`;
- ordered `[1,2]`, two independently reconstructed sources and two distinct spin-2 fields;
- exact A/B candidate then independent FT admission;
- on FT PASS dispatches Exp073FU.

### Exp073FU / WW_S1_S3

- science prereg blob `9a65174bb6e4f2ce4def3a83bad2f992ddd38d6a`;
- admission Exp073FV prereg blob `6f6e995bdeeea02b64e192f91fd2f5078d5eeedd`;
- repaired science driver v0.1 blob `0b05e8dbf5cf87c6b35e6729bc3c4e5443a1421d`;
- heavy workflow blob `254a5826c34f34771dd36fe80b20b5a0a194fdb1`;
- repaired static audit v0.2 run `34054859313` SUCCESS; support only, no science;
- ordered `[1,3]`, distinct fields;
- on FV PASS dispatches Exp073FW.

Historical immutable support outcome: FU static audit v0.1 run `34054723711 / 101544419091` failed only because a decorative literal `Exp073FS` was incorrectly required by the audit transform. It is infrastructure/support `+0/+0`, not scientific FAIL; no self-hosted science ran. Minimal prospective repair retained the frozen scientific semantics.

## Newly frozen remaining heavy targets

### Exp073FW / WW_S2_S2 -> Exp073FX admission

Science prereg:
- path `experiments/073fw_ww_s2_s2_filebacked_full_resolution_ab_science_v0_1_prereg.md`;
- creation commit `7ecdbac03f4fed4a6275f33a8ae178ef76a8a456`;
- blob `10ffd2b4d3c709fa79fd64222cc132cccd13440f`;
- target `[2,2]`, `S2->S2`;
- one authoritative S2 reconstruction per replica;
- exactly one spin-2 field object reused on both coupling sides;
- candidate token `PASS_EXP073FW_WW_S2_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

Admission prereg:
- Exp073FX creation commit `8af75065672ae74dccb80c4c8e8da59fc8c42ce0`;
- blob `9f4722ebbcdb3e36e753b35d1b5765c8974f48a3`;
- token `PASS_EXP073FX_WW_S2_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

Frozen implementation:
- driver v0.1 `e396b69639b1db73044d60c0afc37f2f74e643ed`;
- exact file-backed adapter v0.2 `f63ffe431a034ea4e842970210365a156fb35089`;
- verify/prune `1dfc57bddd1db6c8aeaadd0bc1e73b130e611bcb`;
- comparator `5b6ab180bf13d1fe8ac4557310a19d4a4e9668f6`;
- home envelope `7e6399a3d829c9a4068908c583957fbe7e2a9c50`;
- admission verifier `eb907944eac68b9fd13c405399cf238a8cb5bc96`;
- workflow `.github/workflows/exp073fw-ww-s2-s2-home-science-v0-1.yml`, blob `db53deb69ad59c8c0f74c26394da8b32a478bc88`.

On FX PASS it dispatches Exp073FY.

### Exp073FY / WW_S2_S3 -> Exp073FZ admission

Science prereg:
- creation commit `7a53d8bc372331d323b8d656c6a48aeb15ecfbf1`;
- blob `8aacb4e7f6615fe7e30a88ae02eb02ee5f4dba24`;
- target ordered `[2,3]`, `S2->S3`; reversed order forbidden;
- exactly one S2 and one S3 reconstruction per replica;
- exactly two distinct spin-2 field objects, coupling `f2,f3`;
- candidate token `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

Admission prereg:
- Exp073FZ creation commit `5439e089461faacfd8a97036f1ec717092d12203`;
- blob `3bbfae2fb5816b6933aeafdb74b8f6b4bce25c2f`;
- token `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

Frozen implementation:
- driver v0.1 `53c3a12fe01ce2cccf404c5938d622363d4c7928`; the source-index transform protects left/right source tokens before converting `[1,2] -> [2,3]` to prevent accidental order collapse;
- v0.2 `78ecb51a0d249c6dc25b2b8925d1075efbb5aefc`;
- verify/prune `62026ccea2fb983340caaf3c98256b1efc371d04`;
- comparator `4e28dbbbc08d38c292cfb437477c9d7e55624064`;
- home envelope `c6a88414eac03994e14f052bba28f921936bc628`;
- admission verifier `c3f967c8fc9efed017bb6d5794d53433afefd4ac`;
- workflow `.github/workflows/exp073fy-ww-s2-s3-home-science-v0-1.yml`, blob `6830de6b9773f1f9e13ebf771166cb9f58f61c22`.

On FZ PASS it dispatches the final heavy target Exp073GA.

### Exp073GA / WW_S3_S3 -> Exp073GB final admission

Science prereg:
- creation commit `a83194464baada8103de64d913449b41b69d8a1e`;
- blob `d2365e70d65b51ccca6ddf13cb788ebf60fca0ec`;
- target `[3,3]`, `S3->S3`;
- one authoritative S3 reconstruction per replica;
- exactly one spin-2 field object reused on both coupling sides;
- candidate token `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

Final admission prereg:
- Exp073GB creation commit `edb3101e6b1fc60edfa1866cec55f7d0eb7d8498`;
- blob `8751e843f9a6f91a4b2b22c0ff81f930e0dbbfc8`;
- token `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

Frozen implementation:
- driver v0.1 `b839681a5a86640513c1600a6a130d75345cb127`;
- v0.2 `facc3e2bd6c36ae160d35009b5df4494809d1322`;
- verify/prune `24ee2408b4b66a17001fb734e9e46d008179c310`;
- comparator `263c69075f8a9c5ad3644224485f20fbb3961406`;
- home envelope `775348eb79f6f15d5c11a15fb6866bb1fa5f6774`;
- final admission verifier `ee065b7d844090ae16386cc6944db23846d663ec`;
- workflow `.github/workflows/exp073ga-ww-s3-s3-home-science-v0-1.yml`, blob `ed19c5fbfa2198fce22f1495d76c1c5046b17f49`.

The GA workflow contains no `NEXT_WORKFLOW` and no workflow-dispatch successor. After valid GB admission the heavy queue terminates. It explicitly records `DOWNSTREAM_14_WINDOW_JOIN_NOT_STARTED=true`. Angular closure does not itself authorize downstream join/radial/covariance/relation gates.

## Frozen source authorities for remaining targets

S2:
- selected `8,238,547`;
- bytes `32,954,188`;
- record SHA `259295a1f5a23ad9e5c6b46842bcf612b0eb13dc701ab6d54eb15f0d7bb0105f`;
- unique pixels `4,401,919`;
- occupancy SHA `9e2bfb92289ca4a3abb11efabf7ac8d59bb7c68eb63a7104c2b247267733b24d`.

S3:
- selected `4,196,641`;
- bytes `16,786,564`;
- record SHA `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`;
- unique pixels `2,943,132`;
- occupancy SHA `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`.

Common: NSIDE=4096; ell `0..12287`; 39 bands; selected `EE<-EE`, canonical `<f8 [39,12288]`; public file-backed NaMaster route; MCM backing exactly `19,327,352,832` bytes; source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; no tolerance/allclose/isclose/rounding/smoothing/averaging rescue.

## Exp073GC end-to-end static queue audit

- prereg path `experiments/073gc_remaining_ww_autoqueue_static_audit_v0_1_prereg.md`;
- creation commit `65b1b52f77d6b2aa949b1d2ee5f913bd0c050662`;
- prereg blob `9c890d179141f2c210b5d1dc76f426c8464d6b31`;
- workflow creation commit `090dbcee2e15546368b4ea66650723a5c0fba0a5`;
- activation commit `7b1a46bf2714ba22a0e6712a8cf62ff39658410d`;
- run/job `34056613061 / 101549570367` completed SUCCESS;
- exact token `PASS_EXP073GC_REMAINING_WW_AUTOQUEUE_STATIC_AUDIT_V0_1`;
- `classification=SUPPORT_PLUS_0_PLUS_0`;
- `self_hosted_science_started=false`;
- `queue_terminal=WW_S3_S3`.

Exp073GC independently checked exact blobs, Python/Bash syntax, same-object S2S2/S3S3 semantics, ordered distinct-field S2S3 semantics, exact 19,327,352,832-byte MCM constant, absence of tolerance-rescue, predecessor admission-token requirements, exactly one self-hosted job per heavy workflow, successor order `FU -> FW -> FY -> GA`, absence of any successor dispatch after GA, and preservation of downstream gates as not started.

## Operational rule

If `DSIR-HOME-PC` remains online and its runner continues listening, no new chat instruction is required between successful heavy tasks in this frozen queue. GitHub-hosted verification/admission steps should take the handoff automatically. Any failed mandatory gate must stop the queue. Never bypass a stopped gate merely to reduce idle time.
