# DSIR recovery — WW_S1_S2 admitted; Exp073FU wrapper repair run 5

Date: 2026-09-07. Scope: DSIR only; RTK/RQIR excluded.

## Preserved scientific authority

Exp073FS run `34067352681` attempt 2 completed successfully. Home job `101592579318` produced artifact `10005532345` with GitHub/independent ZIP SHA256 `f878a49241dde97eb0ef1d24561719cf896a77d111c3a3b91725d4989b894d23`. Terminal candidate token was `PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; A/B canonical `<f8 [39,12288] EE<-EE` SHA256 was exactly `77f3e314d76f85cb95ed8edade672575bfa0e40c3b10a831f380a6c6d5f977fd`, with exact array equality, all finite, ordered `S1->S2`, distinct fields, complete pre-prune chains, frozen source `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, and `19,327,352,832`-byte file-backed MCM proof.

Hosted Exp073FT admission job `101632852284` independently reverified the candidate and emitted `PASS_EXP073FT_WW_S1_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `ww_s1_s2_authority_created=true`. Therefore `WW_S1_S2` is admitted authority. The admission dispatched Exp073FU.

## Exp073FU historical pre-science failures

Run `34087011068`, home job `101632910644`, failed before creation of a science root. First causal defect: the outer FU transform wrapper scanned the inherited FS wrapper source for forbidden rescue strings, thereby matching the inherited scanner's own literal token list. Classification: implementation/infrastructure failure `+0/+0`; no scientific gate scored and no checkpoint created.

Repair commit `07de7028dd2cb8baf1927ddcdbceef812bda45f3` removed only that redundant intermediate false-positive scan while preserving the inherited final-payload scanner. Workflow binding commit `511d008b7b5ce74ade38e6d3cdc7faa537d95dc8` updated the frozen wrapper blob.

Repaired run `34089005639`, home job `101638631901`, then failed before science with a generated-shell syntax error at transformed line 72. This exposed the fragility of transform-of-transform orchestration; still `+0/+0`, no science/checkpoints.

The smallest robust orchestration repair changed FU to transform the same frozen FA base directly, exactly as FS does, but prospectively maps `S0->S1` and `S2->S3` and retains the hardened per-replica verify/prune/terminal comparison path. Direct-base repair commit `fa01c7d7a2d20cd222c1d208ac4e359ad1313710`, wrapper blob `7dcde986e4621a3bdf75562170444e1608114504`. Run `34089259696`, home job `101639297762`, passed syntax generation but failed immediately because the FU workflow had never exported FA-base-required storage audit identities `EM_GENERATOR_BLOB` and `EM_COMPARE_BLOB`. Again implementation/configuration `+0/+0`, before science.

Final prospective configuration repair commit `614c5bca01280792b5ea0affe93729fbea174d40` binds exact frozen storage helper blobs `bd1795f2a2c2cf80341f212996eb8278e0be53d9` and `f0de92f3f121592b6d139eb7d948426946d901d1` inside the FU wrapper; wrapper blob `4e6d24fc26760c7e7d31545837239148269d81d5`. No scientific formula, domain, source pair, tolerance, arithmetic or checkpoint semantics changed.

## Authoritative live process

Exp073FU run `34089383137`, head `11b62ebd73fe8bed03f31c559593756149c7fbc0`, predecessor Exp073FS/FT authority run `34067352681`. Hosted launch job `101639612389` succeeded. Home job `101639652148` is queued at this recovery write and is the only permitted self-hosted FU job. Runner owner becomes authoritative when GitHub assigns the job; no competing heavy run is permitted.

Expected science gate: `WW_S1_S3`, ordered `[1,3]`, distinct field objects, canonical `<f8 [39,12288] EE<-EE`, exact A/B equality, finite, same frozen source/contract, file-backed `19,327,352,832`-byte proof, durable complete-stage checkpoints. Checkpoint namespace root: `~/.cache/dsir/exp073fu-ww-s1-s3-filebacked-ab-v0-1` with `checkpoints/A` and `checkpoints/B`. Partial numerical output must not be inspected while running.

On terminal success, consume raw artifact/log and independently verify digest, complete chains, ordered reconstruction counts, distinct field identities, frozen provenance, mmap proof, finiteness and exact A/B equality. Candidate PASS alone does not create authority; only prospectively frozen Exp073FV may create `WW_S1_S3` authority. On infrastructure/resource failure, diagnose first causal defect and resume from verified complete checkpoints without weakening science. On exact numerical mismatch, record scientific FAIL.

Frozen queue after valid FV authority: `FW -> FX -> FY -> FZ -> GA -> GB -> STOP`.
