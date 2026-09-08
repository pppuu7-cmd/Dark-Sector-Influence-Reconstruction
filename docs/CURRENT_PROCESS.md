# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities remain `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`. `WW_S2_S3` is NOT ADMITTED.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-08_EXP073FY_TERMINAL_COMPARATOR_REPAIR_HD_QUEUED_V25.md`.

## Consumed Exp073FY run

Exp073FY namespace-repair V0.3 run `34160898921`, head `b5c8a059a014bee5d318d6067f7a2fac37c5b173`, is terminal FAILURE. Hosted audit `101862362835` SUCCESS. Home job `101862390771` completed both expensive replicas and both full-chain pre-prune verification markers before the terminal comparator failed with `RuntimeError: fail-closed receipt identity A:checkpoint_namespace`.

Frozen evidence artifact: `10040351900`, digest `sha256:ebd1800b9f2b179305d8c1a83208c146915c492f0c3ae614f6ded6ab3be35ad6`. Both valid checkpoint namespaces are `checkpoints/exp073fy-ww-s2-s3-{a,b}-v0-1`; both canonical selected EE SHA256 values are `3a787a12152ec023b6747145ec96345bc805ab0c96b5a26d0b528a9d68672de2`; A and B canonical payload bytes are identical. Classification remains implementation/provenance FAIL `+0/+0`, not scientific FAIL, until the prospectively repaired comparator is run over the frozen evidence.

Comparator repair commit `950bf2334ce192b18bf96df7498c68a3e4a7a52e`, blob `5ccce6c459a5ce541fcccc6b576e78c531fea01f`, changes only the missing hyphenated namespace transform and adds stale/correct namespace regression checks.

## Authoritative current process — Exp073HD hosted terminal recovery/admission

- workflow/run: **`34188871787`**;
- workflow path: `.github/workflows/exp073hd-ww-s2-s3-terminal-comparator-repair-admission-v0-1.yml`;
- branch/head: `main` / **`2f99b9f9d8d078675731c30a080afaba66e04be9`**;
- current state at latest reconciliation: **QUEUED**;
- runner ownership: **hosted-only; no home-heavy owner**;
- preregistration commit: `293d56e9c7e0cca24875b42586a47076163ef4f0`;
- prereg blob: `531253189d9e250cc4617564c44256d2e4ba27c0`;
- source run/job/artifact: `34160898921` / `101862390771` / `10040351900`;
- exact artifact digest: `sha256:ebd1800b9f2b179305d8c1a83208c146915c492f0c3ae614f6ded6ab3be35ad6`;
- repaired comparator blob: `5ccce6c459a5ce541fcccc6b576e78c531fea01f`;
- frozen FZ verifier blob: `c3f967c8fc9efed017bb6d5794d53433afefd4ac`;
- expected candidate token: `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- authority token: `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` plus `ww_s2_s3_authority_created=true`;
- SUCCESS action: consume raw HD job log; only if both exact tokens and authority flag are present may `WW_S2_S3` be admitted and Exp073GA become the next heavy owner;
- FAIL action: diagnose first causal defect. Artifact/provenance/tooling mismatch is infrastructure/provenance `+0/+0`; exact A/B inequality or non-finiteness under otherwise valid frozen evidence is scientific FAIL.

Do not launch Exp073GA or real C2 runtime until Exp073HD is terminal-consumed. No competing home-heavy run exists at this ledger update.

## Prepared successor

Exp073GA/GB remains the frozen `WW_S3_S3` successor, dispatch-only until valid S2-S3 admission. Current final GB verifier blob `cc815737e658a850452d9b0f9488e703f8de84ea`; GA workflow blob `7c408b877a5c0ddc96346cff74efffc1a1985687`; Exp073HC hosted preflight remains PASS support-only.

## Independent C2 frontier

Exp073GZ hosted static audit remains PASS `SUPPORT_PLUS_0_PLUS_0`. Real frozen 28-packet / 1792-byte runtime generation/admission remains blocked until the current S2-S3 admission transition is consumed and no heavy successor owns the home runner.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
