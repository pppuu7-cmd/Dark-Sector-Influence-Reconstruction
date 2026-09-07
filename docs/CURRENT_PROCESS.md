# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities: `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-08_EXP073FY_ACTIVE_GB_PREFLIGHT_REPAIRED_V24.md`, creation commit `424e2f404267ec364cbc614899936a564a0bf2de`.

`WW_S2_S2` authority remains Exp073FW final run `34146468135`, artifact `10027835016`, digest `sha256:ef36ddafc5f30d33206fbf952deea5c0f58f5465370a9c8bd96c2b2d61b1ecef`, admitted by Exp073FX job `101819621240` with `PASS_EXP073FX_WW_S2_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1` and `ww_s2_s2_authority_created=true`.

## Authoritative current process — Exp073FY namespace-repair V0.3 / WW_S2_S3

- workflow/run: **`34160898921`**;
- workflow path: `.github/workflows/exp073fy-ww-s2-s3-namespace-repair-resume-v0-3.yml`;
- branch/head: `main` / **`b5c8a059a014bee5d318d6067f7a2fac37c5b173`**;
- hosted audit: job **`101862362835 SUCCESS`**;
- home-science: job **`101862390771 IN_PROGRESS`** inside repaired frozen A/B gate at latest live reconciliation;
- runner owner: **single DSIR self-hosted home runner (`DSIR-HOME-PC-2`)**;
- invalid historical FY checkpoint retirement step: **SUCCESS**; invalid S3-S3-labelled manifests are preserved as retired evidence and are not relabelled into authority;
- active repaired gate step: **IN_PROGRESS**;
- valid checkpoint namespace required prospectively: `checkpoints/exp073fy-ww-s2-s3-{a,b}-v0-1` under the FY durable checkpoint root;
- invalid namespace `exp073fy-ww-s3-s3-` is fail-closed forbidden by repaired driver blob `65161f78f7c993df571be3ea871de03c54f6847a`;
- expected candidate token: `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- authority token: `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`;
- current state: `IN_PROGRESS / WW_S2_S3 NOT ADMITTED`;
- last verified process milestone: invalid historical checkpoint retirement completed; repaired frozen A/B calculation active;
- SUCCESS action: consume terminal raw logs and artifact, independently verify artifact digest, provenance and contract fingerprint, complete A+B checkpoint chains, exact S2-S3 namespace identity, ordered distinct `S2->S3` semantics, exact 19,327,352,832-byte file-backed MCM proof, canonical finite `<f8 [39,12288] EE<-EE`, SHA equality and `numpy.array_equal`; only then allow Exp073FZ admission;
- FAIL/BLOCKED action: preserve all newly complete valid checkpoint stages, diagnose the first causal infrastructure/software defect, repair only that cause prospectively, and never weaken or reinterpret a genuine frozen numerical mismatch.

Live Actions reconciliation at this ledger update found run `34160898921` still active with home job `101862390771` in progress at the repaired frozen A/B gate. Do not inspect partial numerical output and do not launch a competing home-heavy task while that job remains active.

## Consumed FY failure history relevant to resume

Original Exp073FY run `34147009217` and checkpoint-first recovery `34157571794` remain implementation/infrastructure `+0/+0`, not scientific FAIL. Their useful numerical/checkpoint evidence is historical only where provenance remains valid; invalid S3-S3-labelled checkpoint identity is never imported into scientific authority.

First namespace-repair workflow run `34160466102` also remains infrastructure FAIL `+0/+0`: hosted audit succeeded, but home job `101861088550` failed before heavy computation because `gh` was unavailable. Workflow V0.3 commit `b5c8a059a014bee5d318d6067f7a2fac37c5b173` replaced that self-hosted service call with authenticated `curl`; frozen science was unchanged.

## Prepared successor — Exp073GA / Exp073GB WW_S3_S3

GA is dispatch-only and forbidden until successful FZ S2-S3 admission. It uses the direct frozen-FA architecture plus prospective terminal-resume hardening.

- direct-base repair commit: `4a232aa8369ba8e4f6c5a247ecaf2b75696ced8c`;
- terminal-resume hardening commit: `e9aa36283d0f3b78a91b8a855326c0faec9a613c`;
- GA home blob: `f28bf114e6da502e2a3a0a97f0828c27849814c9`;
- final GB repair commit: `7846c63765fcc8b1fc748fd7ecb25f88c1333a81`;
- current GB verifier blob: `cc815737e658a850452d9b0f9488e703f8de84ea`;
- GA rebinding commit: `23b2253d02739c064bc539f28f8020de5069168c`;
- current GA workflow blob: `7c408b877a5c0ddc96346cff74efffc1a1985687`;
- expected hosted token: `PASS_EXP073GA_HOSTED_LAUNCH_AUDIT_V0_2`;
- frozen target: ordered `[3,3]`, same-field `S3->S3`, canonical `<f8 [39,12288] EE<-EE`, exact file-backed proof and exact A/B equality;
- only Exp073GB may create `WW_S3_S3` authority.

Parallel hosted preflight consumed two deterministic implementation/provenance failures before any GA heavy execution: Exp073HA run `34168565710` (missing lowercase transform token) and Exp073HB run `34168722516` (redundant post-substitution authority-key transform). Both remain support-only `+0/+0`, never scientific FAIL.

Exp073HC run **`34168906285`**, job **`101885299058 SUCCESS`**, raw-log validated the final repaired GB transform and GA binding with exact tokens `PASS_EXP073HC_REPAIRED_GB_TRANSFORM_INVARIANTS`, `PASS_EXP073HC_REPAIRED_GA_GB_BINDING_INVARIANTS`, and `PASS_EXP073HC_WW_S3_S3_GB_REDUNDANT_AUTHORITY_TRANSFORM_REPAIR_STATIC_AUDIT_V0_1`. Classification is `SUPPORT_PLUS_0_PLUS_0`; `ww_s3_s3_authority_created=false`.

The FY workflow may dispatch GA only after successful FZ S2-S3 admission. GA/GB preparation is implementation/support `+0/+0`; it changes no science arithmetic, domain, thresholds or acceptance criteria.

## Independent C2 frontier — Exp073GZ consumed PASS

Frozen runtime admission receipt contract: commit `a8499c404aa2b862cc08634fe4ed20d2753c9f25`, blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`.

Exp073GZ preregistration: commit `d5791df0c81169c9a3797ac1867b921028097579`. Hosted workflow commit: `a4961a87432f53bc55a13c7f542a8775634b90bd`.

- run: **`34168323933`**;
- hosted job: **`101883674574 SUCCESS`**;
- raw-log token: `PASS_EXP073GZ_C2_RUNTIME_ADMISSION_RECEIPT_CONTRACT_STATIC_AUDIT_V0_1`;
- classification: **`SUPPORT_PLUS_0_PLUS_0`**;
- audited object: exact contract blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`;
- no runtime bytes decoded or mapped;
- `prediction_ready=false`;
- no scientific/model authority created.

The exact next C2 task is real frozen 28-packet / 1792-byte runtime generation and receipt admission under this audited contract. It remains **BLOCKED_BY_HEAVY_RUN_EXCLUSIVITY** because FY owns the single home runner. Do not dispatch C2 runtime while FY or a successor GA heavy task is active.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.