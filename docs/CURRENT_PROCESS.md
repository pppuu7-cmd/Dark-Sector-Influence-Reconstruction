# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities: `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-07_EXP073FY_ACTIVE_EXP073GZ_PREREG_V20.md`, creation commit `8fe8db6af6a144dbf1c68901b87a1b91ec6ffb76`.

## Authoritative current process — Exp073FY WW_S2_S3

- workflow/run: **`34147009217`**;
- branch/head: `main` / **`f04346a8e6909cb4342e536a0e7328f5ca5e54c9`**;
- hosted audit: job **`101821110137` SUCCESS**, raw `PASS_EXP073FY_HOSTED_LAUNCH_AUDIT_V0_4`, support `+0/+0`;
- home-science: job **`101821144414 IN_PROGRESS`** inside frozen A/B gate at latest reconciliation;
- runner owner: **`DSIR-HOME-PC-2`**, machine `win-ws338`;
- checkpoint root: `~/.cache/dsir/exp073fy-ww-s2-s3-filebacked-ab-v0-1`;
- expected candidate token: `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- authority token: `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`;
- SUCCESS action: consume terminal raw logs/artifact, independently verify digest/provenance/complete A+B chains/ordered distinct S2->S3 semantics/exact mmap proof/finiteness/exact equality, then require FZ admission before authority;
- FAIL/BLOCKED action: preserve all complete checkpoints and diagnose the first causal defect; never repair a genuine frozen numerical mismatch.

No competing heavy run is permitted. Partial numerical output must not be inspected.

## Prepared successor — Exp073GA WW_S3_S3

GA is dispatch-only and has **not** been launched while FY owns home. It now uses the proven direct frozen-FA architecture plus prospective terminal-pruned retry hardening.

- direct-base repair commit: `4a232aa8369ba8e4f6c5a247ecaf2b75696ced8c`;
- terminal-resume hardening commit: `e9aa36283d0f3b78a91b8a855326c0faec9a613c`;
- GA home blob: `f28bf114e6da502e2a3a0a97f0828c27849814c9`;
- workflow binding commit: `d149630f30f3e904c78c7ca43f32917f9e2aaf85`;
- expected hosted token: `PASS_EXP073GA_HOSTED_LAUNCH_AUDIT_V0_2`;
- frozen target: ordered `[3,3]`, same-field `S3->S3`, canonical `<f8 [39,12288] EE<-EE`, exact file-backed proof and exact A/B equality;
- only Exp073GB may create WW_S3_S3 authority.

The FY workflow may dispatch GA only after successful FZ S2S3 admission. These GA repairs are implementation/support `+0/+0` and changed no science arithmetic, domain, thresholds or acceptance criteria.

## Independent C2 frontier

Commit `a8499c404aa2b862cc08634fe4ed20d2753c9f25` froze the runtime admission receipt contract, blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`.

Exp073GZ was prospectively preregistered at commit `d5791df0c81169c9a3797ac1867b921028097579` with exact token `PASS_EXP073GZ_C2_RUNTIME_ADMISSION_RECEIPT_CONTRACT_STATIC_AUDIT_V0_1` and classification on PASS `SUPPORT_PLUS_0_PLUS_0` only. Current state: **PREREGISTERED / BLOCKED_BY_AUDIT_EXECUTION_PATH** because the connector/platform rejected creation of a new hosted workflow before any repository write. Do not bypass or weaken the frozen audit.

Real frozen 28-packet runtime generation/admission remains BLOCKED while FY owns home and additionally requires Exp073GZ static-audit PASS. No scientific/model authority exists for C2.

## Global frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
