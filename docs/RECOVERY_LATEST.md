# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_EXP073FY_NAMESPACE_REPAIR_RESUME_V22.md` (creation commit `94607e9b068552bc565bb4d3b58e32e973584b22`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, and `S2_S2`.

`WW_S2_S2` authority remains Exp073FW final run `34146468135`, artifact `10027835016`, digest `sha256:ef36ddafc5f30d33206fbf952deea5c0f58f5465370a9c8bd96c2b2d61b1ecef`, admitted by Exp073FX job `101819621240` with `PASS_EXP073FX_WW_S2_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1` and `ww_s2_s2_authority_created=true`. Historical FW failures remain historical `+0/+0`.

## Consumed Exp073FY failures and repair

Original Exp073FY run `34147009217` is terminal implementation/infrastructure FAIL `+0/+0`, not scientific FAIL. Expensive Replica A completed through `replica_receipt_complete` with correct ordered `S2->S3`, `[2,3]` science payload and exact file-backed evidence, but its manifests carried invalid checkpoint namespace `checkpoints/exp073fy-ww-s3-s3-a-v0-1`. FZ admission was skipped.

Recovery run `34157571794` correctly failed closed at `fresh_sources_complete`, exposing the namespace cascade. The cause was the FY wrapper's generic symbol shift mutating an already-correct `S2-S3` checkpoint namespace to `S3-S3`.

Prospective driver repair commit `f899b93f966e617ad1ff46b5abba6f928d4ad389`, blob `65161f78f7c993df571be3ea871de03c54f6847a`, protects the exact S2-S3 checkpoint namespace strings before generic source-symbol substitution and statically forbids `exp073fy-ww-s3-s3-`. Frozen arithmetic/domain/order/tolerance rules are unchanged.

First namespace-repair workflow run `34160466102` had hosted audit SUCCESS but home job `101861088550` failed before heavy computation because the self-hosted machine has no `gh` executable (`gh: command not found`). Classification remains infrastructure FAIL `+0/+0`. Recovery workflow V0.3 commit `b5c8a059a014bee5d318d6067f7a2fac37c5b173` replaces that self-hosted service call with authenticated `curl`; hosted-only steps may continue using GitHub CLI.

Invalid historical S3-S3-labelled FY checkpoint directories are not rewritten or relabelled. The V0.3 recovery verifies their known defect and hashes, records retirement evidence, and moves them outside the active checkpoint path before constructing a new valid authority chain.

## Authoritative current heavy process — Exp073FY namespace-repair V0.3

Run **`34160898921`**, head `b5c8a059a014bee5d318d6067f7a2fac37c5b173`, workflow `.github/workflows/exp073fy-ww-s2-s3-namespace-repair-resume-v0-3.yml`:
- hosted audit job `101862362835`: SUCCESS;
- home job **`101862390771`**: IN_PROGRESS at latest reconciliation;
- invalid S3-S3-labelled FY checkpoint retirement step: SUCCESS;
- repaired frozen `WW_S2_S3` A/B gate: IN_PROGRESS;
- single self-hosted DSIR runner owns the job;
- no competing heavy run is permitted;
- partial numerical output must not be inspected.

Frozen FY science remains ordered `S2->S3`, `[2,3]`, distinct fields, DES NSIDE=4096, ell `0..12287`, 39 bands, canonical `<f8 [39,12288] EE<-EE`, exact file-backed MCM proof, finiteness and exact A/B equality. `WW_S2_S3` remains **NOT ADMITTED**. Only FZ token `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may create authority.

## Prospectively hardened final heavy successor — Exp073GA WW_S3_S3

GA remains dispatch-only and forbidden until successful FZ admission. Direct-base repair commit `4a232aa8369ba8e4f6c5a247ecaf2b75696ced8c`; additional terminal-resume hardening commit `e9aa36283d0f3b78a91b8a855326c0faec9a613c`; current home blob `f28bf114e6da502e2a3a0a97f0828c27849814c9`; workflow binding `d149630f30f3e904c78c7ca43f32917f9e2aaf85`. Frozen GA target is `[3,3]`, same-field `S3->S3`, exact A/B equality and exact file-backed proof. Only Exp073GB may create authority.

## Independent C2 frontier

Exp073GW/GX/GY remain hosted support-only `+0/+0`; no real C2 record-set/model authority exists. Runtime admission contract commit `a8499c404aa2b862cc08634fe4ed20d2753c9f25`, blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`, remains frozen. Exp073GZ static audit preregistration commit `d5791df0c81169c9a3797ac1867b921028097579`, expected token `PASS_EXP073GZ_C2_RUNTIME_ADMISSION_RECEIPT_CONTRACT_STATIC_AUDIT_V0_1`, remains **PREREGISTERED / BLOCKED_BY_AUDIT_EXECUTION_PATH**. Real C2 runtime remains blocked while FY owns home and additionally requires GZ PASS.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.