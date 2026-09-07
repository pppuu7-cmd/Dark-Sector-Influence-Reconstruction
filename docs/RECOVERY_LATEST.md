# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_EXP073FY_PRUNER_REPAIR_RESUME_V21.md` (creation commit `2c645a5c1e4e4416ab8d26b5496c6bbd2f55d252`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, and `S2_S2`.

`WW_S2_S2` authority remains Exp073FW final run `34146468135`, artifact `10027835016`, digest `sha256:ef36ddafc5f30d33206fbf952deea5c0f58f5465370a9c8bd96c2b2d61b1ecef`, admitted by Exp073FX job `101819621240` with `PASS_EXP073FX_WW_S2_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1` and `ww_s2_s2_authority_created=true`. Historical FW failures remain historical `+0/+0`.

## Newly consumed Exp073FY failure

Exp073FY run `34147009217`, head `f04346a8e6909cb4342e536a0e7328f5ca5e54c9`, is terminal FAILURE. Hosted job `101821110137` succeeded; home job `101821144414` failed; FZ admission was skipped. Classification: **implementation/infrastructure FAIL +0/+0**, not scientific FAIL.

First causal failure: after expensive Replica A had completed through `replica_receipt_complete`, the FY post-receipt pruner required lexical token `WW_S1_S2`, which is absent from its pinned frozen FS base. Artifact `10031272604` has GitHub digest and independently recomputed ZIP SHA256 `624a44f05b2762a58d1191b58df41c194b86bcc7ceb5622517c0a55f64405a6c`. It preserves A selected EE `<f8 [39,12288]`, 3,833,856 bytes, SHA256 `3a787a12152ec023b6747145ec96345bc805ab0c96b5a26d0b528a9d68672de2`, ordered `[2,3]`, `S2->S3`, distinct fields, and exact `19,327,352,832`-byte file-backed MCM receipt. No B result exists in that artifact.

Independent provenance audit also found that A manifests carry checkpoint namespace `checkpoints/exp073fy-ww-s3-s3-a-v0-1` despite correct S2->S3 science payload. The cause is a cascade in the FY wrapper: intended hyphenated namespace transformation is subsequently altered again by word-boundary `s2 -> s3` variable transformation. This is a provenance/checkpoint-identity defect. It is not scientific authority and must not be relabelled or rescued by weakening namespace checks.

Minimal lexical-pruner repair is commit `c28396aa4cba6206f737cfd683b9f27f9cbe5273`, blob `8c0e7ae30a80c6d74e6a1fbc079c1d2bc4eef773`; only the impossible uppercase-token requirement was removed. Workflow binding commit `3217ea05f5ab8a45bc237f34a8fa894e8c49df38` prospectively pins that blob; frozen arithmetic/domain/order/tolerance rules were unchanged.

## Authoritative current heavy process — Exp073FY recovery run

Run **`34157571794`**, head `3217ea05f5ab8a45bc237f34a8fa894e8c49df38`:
- hosted audit job `101852463413`: SUCCESS;
- home job **`101852500796`**: IN_PROGRESS inside frozen FY checkpoint-first path at latest reconciliation;
- single self-hosted DSIR runner owns the job;
- checkpoint root `~/.cache/dsir/exp073fy-ww-s2-s3-filebacked-ab-v0-1`;
- no competing heavy run is permitted;
- partial numerical output must not be inspected.

Because the namespace-cascade defect was discovered independently while this run is active, do not edit its workflow mid-run. On terminal state consume logs/artifact first. If the namespace inconsistency is the first causal failure, prospectively repair the wrapper transformation by protecting checkpoint namespace tokens before source-variable substitutions, add a static regression requiring exact `exp073fy-ww-s2-s3-{a,b}-v0-1` and forbidding `ww-s3-s3`, then resume only from checkpoints that pass the repaired fail-closed identity. Do not rewrite invalid checkpoint manifests in place.

Frozen FY science remains ordered `S2->S3`, `[2,3]`, distinct fields, DES NSIDE=4096, ell 0..12287, 39 bands, canonical `<f8 [39,12288] EE<-EE`, exact file-backed MCM proof, finiteness and exact A/B equality. `WW_S2_S3` remains **NOT ADMITTED**. Only FZ token `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may create authority.

## Prospectively hardened final heavy successor — Exp073GA WW_S3_S3

GA remains dispatch-only and forbidden until successful FZ admission. Direct-base repair commit `4a232aa8369ba8e4f6c5a247ecaf2b75696ced8c`; additional terminal-resume hardening commit `e9aa36283d0f3b78a91b8a855326c0faec9a613c`; current home blob `f28bf114e6da502e2a3a0a97f0828c27849814c9`; workflow binding `d149630f30f3e904c78c7ca43f32917f9e2aaf85`. Frozen GA target is `[3,3]`, same-field `S3->S3`, exact A/B equality and exact file-backed proof. Only Exp073GB may create authority.

## Independent C2 frontier

Exp073GW/GX/GY remain hosted support-only `+0/+0`; no real C2 record-set/model authority exists. Runtime admission contract commit `a8499c404aa2b862cc08634fe4ed20d2753c9f25`, blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`, remains frozen. Exp073GZ static audit preregistration commit `d5791df0c81169c9a3797ac1867b921028097579`, expected token `PASS_EXP073GZ_C2_RUNTIME_ADMISSION_RECEIPT_CONTRACT_STATIC_AUDIT_V0_1`, remains **PREREGISTERED / BLOCKED_BY_AUDIT_EXECUTION_PATH**. Real C2 runtime remains blocked while FY owns home and additionally requires GZ PASS.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
