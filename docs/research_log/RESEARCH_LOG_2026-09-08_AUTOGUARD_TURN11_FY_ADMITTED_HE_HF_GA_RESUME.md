# DSIR Auto-Guard — FY admission, HE/HF repair chain, GA successor resume

Date: 2026-09-08
Scope: DSIR4 frozen heavy-chain / provenance recovery only.

## 1. Preserved Exp073FY evidence; no heavy recomputation

The expensive `WW_S2_S3 / Exp073FY` source run remains run `34160898921`, self-hosted job `101862390771`. The home job completed and verified both expensive replicas before the post-compute infrastructure guard stopped the workflow on a checkpoint-namespace identity mismatch. Required original log markers include:

- `PASS_EXP073FY_LIVE_EXCLUSIVITY`
- `PASS_EXP073FY_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`
- `PASS_EXP073FY_REPLICA_B_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`

Preserved artifact: `10040351900`, name `exp073fy-ww-s2-s3-filebacked-ab-v0-1`, digest `sha256:ebd1800b9f2b179305d8c1a83208c146915c492f0c3ae614f6ded6ab3be35ad6`. Frozen source head: `de83e20a68f79ccf25b89b0d33eb4206e294c757`. Contract fingerprint: `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`.

The expensive FY numerical work was not rerun in this recovery chain.

## 2. Exp073HD dependency and source-semantics failures

HD run `34188871787`, job `101942632770`, failed before scientific comparison because the hosted comparator environment lacked NumPy. Classification: `INFRASTRUCTURE/DEPENDENCY_FAILURE +0/+0`, not scientific FAIL. Exact runtime dependency repair was commit `8fe0c6cc5bcfcabfd212ce73e2caf8016fd281f2`, pinning `numpy==2.3.3` without changing comparator science.

HD recovery run `34188961637`, job `101942898124`, then passed the dependency layer but stopped fail-closed on `RuntimeError: fail-closed source semantics A`. Artifact audit showed the preserved FY replicas contain the prospectively frozen S2->S3 identities `ordered_source_indices=[2,3]` and `reconstruction_counts={'s2':1,'s3':1}`; the transformed HD comparator still required the stale FS counts `{'s1':1,'s2':1}`. Classification: `IMPLEMENTATION/PROVENANCE_FAILURE +0/+0`, not scientific FAIL.

## 3. Exp073HE prospective comparator repair

A separate prospective comparator was added rather than rewriting frozen HD evidence:

- `ci/exp073he_compare_terminal_receipts_v0_1.py`, blob `7698487dd137ec4c2b4f3f2faa158aeb6846ef78`
- prereg blob `7b47a9f6acd588c0dddd176784077332b66846ac`
- workflow commit `cc95d0c0b9af9c912b97cdded5cc7abf6edbfd59`

HE changes only the exact implementation identities needed for FY (`exp073fs-ww-s1-s2 -> exp073fy-ww-s2-s3` and `{'s1':1,'s2':1} -> {'s2':1,'s3':1}`), while preserving exact `numpy.array_equal`, finiteness, stage/source/hash checks and the no-tolerance-rescue policy.

HE run `34189083696`, job `101943248885`, produced the exact candidate token `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Both selected payloads had SHA-256 `73dc92e39b043172fc1f917998187321e737b627af8a75b28e06aeaee43ea555`, `numpy_array_equal=true`, and `all_finite=true`.

HE then stopped before authority because the frozen FZ wrapper was pinned to historical FV blob `03cf7109...` while the repository FV path had drifted, and the wrapper transform order also contained an implementation hazard around overlapping `ww_s1_s3` tokens. This is `IMPLEMENTATION/PROVENANCE_FAILURE +0/+0`; the already-established exact candidate equality is not converted into a scientific FAIL.

## 4. Exp073HF materialized provenance admission

A separate prospectively frozen materialized FY verifier was added:

- `ci/exp073hf_verify_fy_candidate_materialized_v0_1.py`, blob `ad1a43b216b67125ed473b74d95e362a4666aa04`
- prereg blob `d48dd061661eb95b711cd3f42116a664a704d4bb`
- workflow commit `1f17ee193472f890bf91dc5b699cde93a7545db8`

It preserves the historical provenance checks while materializing their intended final S2->S3 identities: original pre-prune A/B markers, live exclusivity, exact candidate PASS, exact terminal receipt fields, source ordering/counts, distinct-field construction, file-backed MCM (`19327352832` bytes), full stage-manifest SHA chain, exact selected-payload hashes, byte-for-byte A/B equality, finiteness, frozen source head and contract fingerprint.

HF run `34189183845`, job `101943539978`, completed `SUCCESS` and emitted:

- `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`
- `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`
- `classification=SCIENTIFIC_AUTHORITY_ADMITTED`
- `ww_s2_s3_authority_created=true`
- `PASS_EXP073HF_WW_S2_S3_MATERIALIZED_PROVENANCE_ADMISSION_V0_1`

Therefore `WW_S2_S3 = SCIENTIFIC_AUTHORITY_ADMITTED`.

## 5. Exp073GA successor orchestration repair

After S2->S3 admission, the next frozen heavy target is `WW_S3_S3 / Exp073GA`. Before launch, global Actions state was checked: no in-progress and no queued workflows. The existing GA hosted predecessor gate was technically blocked because it required a successful run named FY, although the expensive FY run correctly ended in a post-compute infrastructure failure and its authority was subsequently created by the successful hosted-only HF admission.

The GA predecessor handoff was therefore changed only at orchestration level to consume HF run `34189183845` and require the same downstream authority markers `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` and `ww_s2_s3_authority_created=true`. Frozen GA/GB numerical drivers, scientific contracts, thresholds, source ordering and hypothesis identities were not changed.

Initial orchestration repair commit `a2638d900033092819d3bd984df06a83e8f18474` contained a one-character typo in the hosted-only `PRUNER_BLOB` pin. GA run `34189505842`, hosted job `101944481137`, therefore stopped in `Freeze final S3S3 code and require admitted S2S3 predecessor`; `home-science` job `101944506715` and final admission job `101944507082` were skipped. No heavy computation started. Classification: `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`, not scientific FAIL.

The pin was immediately restored to the frozen pruner blob `24ee2408b4b66a17001fb734e9e46d008179c310` in commit `10e6fb67af7d6485fca3d1ecf2362e4622883417`.

The resulting single recovery run is `34189540992`, head SHA `10e6fb67af7d6485fca3d1ecf2362e4622883417`:

- hosted launch audit job `101944582891` = `SUCCESS`
- self-hosted `home-science` job `101944608861` = `IN_PROGRESS`
- active step: `Run frozen WW_S3_S3 A/B gate with durable checkpoints`

A global post-launch check found exactly one `in_progress` workflow, run `34189540992`, and zero queued workflows. No duplicate heavy-run was started.

## Scientific status after this turn

- `WW_S2_S2 = SCIENTIFIC_AUTHORITY_ADMITTED`
- `WW_S2_S3 = SCIENTIFIC_AUTHORITY_ADMITTED`
- `WW_S3_S3 = NOT_YET_ADMITTED` while run `34189540992` is active
- new scientific FAIL contribution this turn: `0`
- HD dependency failure, HD source-semantics mismatch, HE/FZ wrapper provenance drift, and the first GA hosted pin typo are infrastructure/implementation/provenance failures `+0/+0`, not scientific FAIL

Next allowed primary transition: do not start another heavy workflow. Wait for terminal evidence from `34189540992`; if the GA candidate completes successfully, perform only its frozen GB provenance admission. Any future infrastructure failure must remain separate from scientific FAIL, and `INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, and `OUTSIDE_DOMAIN` remain non-FAIL classifications unless their own frozen scientific gates explicitly say otherwise.
