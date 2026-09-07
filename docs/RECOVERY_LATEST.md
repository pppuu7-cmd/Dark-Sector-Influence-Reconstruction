# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_EXP073FY_ACTIVE_GB_PREFLIGHT_REPAIRED_V24.md` (creation commit `424e2f404267ec364cbc614899936a564a0bf2de`). Earlier recovery notes remain immutable history.

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

## Prospectively hardened final heavy successor — Exp073GA / Exp073GB

GA remains dispatch-only and forbidden until successful FZ admission. Frozen GA numerical target is `[3,3]`, same-field `S3->S3`, exact A/B equality and exact file-backed proof. Direct-base repair commit `4a232aa8369ba8e4f6c5a247ecaf2b75696ced8c`; terminal-resume hardening commit `e9aa36283d0f3b78a91b8a855326c0faec9a613c`; GA home blob remains `f28bf114e6da502e2a3a0a97f0828c27849814c9`.

Parallel hosted-only preflight found two deterministic defects in the original GB transform before any GA heavy execution: missing lowercase base token (`Exp073HA` run `34168565710`) and a redundant authority-key replacement after the shorter `ww_s2_s2 -> ww_s3_s3` substitution (`Exp073HB` run `34168722516`). Both are implementation/provenance `+0/+0`, never scientific FAIL.

Final prospective GB repair commit `7846c63765fcc8b1fc748fd7ecb25f88c1333a81`; current GB verifier blob `cc815737e658a850452d9b0f9488e703f8de84ea`. GA rebinding commit `23b2253d02739c064bc539f28f8020de5069168c`; current GA workflow blob `7c408b877a5c0ddc96346cff74efffc1a1985687` binds that exact verifier.

Exp073HC hosted static audit run **`34168906285`**, job **`101885299058`**, completed SUCCESS with exact tokens `PASS_EXP073HC_REPAIRED_GB_TRANSFORM_INVARIANTS`, `PASS_EXP073HC_REPAIRED_GA_GB_BINDING_INVARIANTS`, and `PASS_EXP073HC_WW_S3_S3_GB_REDUNDANT_AUTHORITY_TRANSFORM_REPAIR_STATIC_AUDIT_V0_1`. It verifies both pre-prune proofs, GA exact A/B PASS, live exclusivity, S3->S3/[3,3], same-field semantics, 19327352832-byte file-backed MCM, exact adapter route, complete stage-manifest SHA binding, byte equality, finiteness, and no tolerance/rounding/smoothing/averaging rescue. Classification remains `SUPPORT_PLUS_0_PLUS_0`; `ww_s3_s3_authority_created=false`.

Only a future real Exp073GB execution over a valid successful GA artifact may create `WW_S3_S3` authority.

## Independent C2 frontier — Exp073GZ PASS

Runtime admission contract commit `a8499c404aa2b862cc08634fe4ed20d2753c9f25`, exact blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`, remains frozen.

Exp073GZ preregistration was commit `d5791df0c81169c9a3797ac1867b921028097579`. Repository commit `a4961a87432f53bc55a13c7f542a8775634b90bd` added the dedicated hosted audit without changing the frozen contract. Actions run **`34168323933`**, hosted job **`101883674574`**, completed SUCCESS; raw job log contains exact token `PASS_EXP073GZ_C2_RUNTIME_ADMISSION_RECEIPT_CONTRACT_STATIC_AUDIT_V0_1` after verifying the exact contract blob and frozen fail-closed provenance/receipt requirements.

Exp073GZ classification is strictly **`SUPPORT_PLUS_0_PLUS_0`**. It creates no scientific/model authority, performs no decoding/mapping, and launches no CLASS/scientific prediction.

The next C2 transition is real frozen 28-packet / 1792-byte runtime production and admission under the audited receipt contract, but it remains **BLOCKED_BY_HEAVY_RUN_EXCLUSIVITY** while FY owns the home runner. No competing home job may be launched.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.