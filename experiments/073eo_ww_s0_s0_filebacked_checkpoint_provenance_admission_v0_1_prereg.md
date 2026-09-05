# Exp073EO — WW_S0_S0 file-backed checkpoint provenance admission v0.1 preregistration

Prepared prospectively while authoritative Exp073EN full-resolution file-backed A/B science is still running. Exp073EO is an admission/provenance gate only. It MUST NOT inspect or tune against partial Exp073EN numerical output and MUST NOT alter any frozen DSIR science criterion.

## Upstream authority required
Exp073EO may run only after a terminal Exp073EN candidate artifact exists. The candidate must bind the frozen Exp073EN science identity:
- source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- NaMaster v2.7 source commit `24365fa59a38c15732f4f37e8b29265b75c442d5`;
- file-backed storage patch SHA256 `9a80a756960afa8b4ddf61b5fbba7fba6ad5ed9ac919e093bb1365a636c789f0`;
- hosted Exp073EM support PASS artifact `9977333691`, digest `sha256:0ece75e489b6f413d96e85a099e42db96b5d5acdc03c3ee6901273357762cda1`;
- DES NSIDE=4096, ell `0..12287`, 39 bands, spin-2 auto `S0 -> S0`, selected `EE<-EE`, canonical `<f8 [39,12288]`;
- exact A/B equality only; no tolerance/allclose/rounding/smoothing/averaging rescue.

## Immutable checkpoint chain to audit
For replicas A and B independently, Exp073EO must validate the complete ordered six-stage chain from the durable driver without skipping any stage:
1. `fresh_s0_mask_complete`;
2. `fresh_workspace_mcm_complete`;
3. `mcm_fits_verified`;
4. `full_window_complete`;
5. `selected_ee_complete`;
6. `replica_receipt_complete`.

Each manifest must satisfy fail-closed identity checks for:
- schema and exact stage name;
- `complete=true`;
- correct replica identity;
- exact checkpoint namespace `checkpoints/exp073dq-ww-s0-s0-a-v0-1` or `checkpoints/exp073dq-ww-s0-s0-b-v0-1`;
- exact frozen source head and contract fingerprint;
- `historical_ww_numerical_import=false`;
- `other_replica_output_read=false`;
- every retained payload hash/shape/dtype/semantics required by the stage.

If an Exp073EN post-receipt pruning rule removed a huge workspace FITS or canonical MCM intermediate, EO must require a prior verified `replica_receipt_complete` plus the retained immutable SHA/provenance record proving that pruning occurred only after complete-stage admission. Missing pre-receipt evidence, hash mismatch, namespace mismatch or unverifiable pruning is FAIL-CLOSED/BLOCKED `+0/+0`, not scientific FAIL.

## Storage/resource provenance required
EO must also verify from terminal Exp073EN evidence that every newly computed full-resolution workspace used the exact file-backed MCM backend and that the proof records:
- regular-file mapping, not anonymous/swap-only replacement;
- mapped backing size exactly `19327352832` bytes;
- expected unbinned matrix rows `49152`;
- local stock-vs-patched Exp073EM exact qualifier PASS before full-resolution arithmetic;
- no surviving `dsir-nmt-mcm-*` backing file after each replica process exit;
- exact 8-CPU execution contract and nested BLAS/OpenMP/MKL/OpenBLAS/NumExpr threading constraints as frozen upstream;
- no competing self-hosted DSIR heavy ownership during the science run.

## Scientific candidate verification
EO must independently consume the uploaded compact Exp073EN artifact rather than trusting workflow SUCCESS. It must verify artifact digest/provenance and require the terminal candidate token `PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1` together with all prospectively frozen exact checks. A/B selected payloads must have identical canonical SHA256 and `numpy.array_equal=true`, be finite canonical `<f8 [39,12288]`, and preserve `EE<-EE` semantics.

EO must not regenerate or replace a missing scientific payload, must not import historical WW numerical output, and must not infer PASS from close numerical agreement.

## Classification
- `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_1`: all compact-artifact, storage, identity, six-stage checkpoint and exact A/B requirements pass. Only this token may set `WW_S0_S0` scientific authority valid.
- `BLOCKED_EXP073EO_* +0/+0`: terminal artifact absent/incomplete, checkpoint evidence missing, unverifiable pruning, source/contract/storage provenance mismatch, or other infrastructure/provenance defect. No WW authority.
- `FAIL_EXP073EO_SCIENTIFIC_REPEATABILITY_*`: only if Exp073EN reached the fully qualified scientific arithmetic comparison under all upstream provenance/storage conditions and the exact A/B scientific repeatability gate itself failed. EO must not manufacture a scientific FAIL from infrastructure or provenance defects.

Exp073EO is not allowed to weaken or supersede Exp073EN arithmetic. It is an independent admission audit whose sole scientific write authority is admission of the already frozen `WW_S0_S0` candidate when every requirement above passes.

Status at preregistration: `PREREGISTERED_NOT_ACTIVATED`; `ww_s0_s0_authority_created=false`.
