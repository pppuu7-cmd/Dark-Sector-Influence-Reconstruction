# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities are `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, and **`S2_S3`**. `WW_S3_S3` remains **NOT_YET_ADMITTED** while the frozen final heavy gate is active.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-08_WW_S2_S3_ADMITTED_GA_ACTIVE_V26.md` (creation commit `f2ba0ea22a1008f41b10b1014d84fa3abd9905bd`).

## Consumed S2->S3 authority chain

Preserved expensive evidence is Exp073FY run `34160898921`, home job `101862390771`, artifact `10040351900`, digest `sha256:ebd1800b9f2b179305d8c1a83208c146915c492f0c3ae614f6ded6ab3be35ad6`, frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`.

HD/HE implementation/provenance failures remain historical `+0/+0`. HE run `34189083696`, job `101943248885`, established exact FY A/B candidate equality and finiteness. HF run `34189183845`, job `101943539978`, emitted `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s2_s3_authority_created=true`. Therefore `WW_S2_S3 = SCIENTIFIC_AUTHORITY_ADMITTED`.

## Authoritative current process — Exp073GA WW_S3_S3

- workflow/run: **`34189540992`**;
- workflow path: `.github/workflows/exp073ga-ww-s3-s3-home-science-v0-1.yml`;
- branch/head: `main` / **`10e6fb67af7d6485fca3d1ecf2362e4622883417`**;
- workflow/run start: **`2026-09-08T05:09:09Z`**;
- hosted launch-audit job: **`101944582891` SUCCESS**;
- self-hosted home-science job: **`101944608861 IN_PROGRESS`**;
- current active step: `Run frozen WW_S3_S3 A/B gate with durable checkpoints`;
- runner ownership: **single self-hosted owner; do not launch competing home-heavy work**;
- checkpoint root/namespace: **`$HOME/.cache/dsir/exp073ga-ww-s3-s3-filebacked-ab-v0-1`** with replica checkpoint subtrees `A` and `B`;
- evidence artifact name: `exp073ga-ww-s3-s3-filebacked-ab-v0-1`;
- frozen source head: `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint: `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- exact candidate token: `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- final authority token: `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` plus `classification=SCIENTIFIC_AUTHORITY_ADMITTED` and `ww_s3_s3_authority_created=true`;
- last durable checkpoint: live partial checkpoint internals are intentionally not inspected while the frozen computation is running; terminal artifact/checkpoint evidence must be consumed fail-closed after completion;
- SUCCESS action: consume raw home log and artifact, verify digest/provenance/checkpoint identity/full A+B chains, exact same-field `S3->S3/[3,3]`, exact file-backed proof, finiteness and byte/array equality; only then permit the frozen hosted GB verifier to create `WW_S3_S3` authority;
- FAIL action: diagnose the first causal failure. Infrastructure/implementation/provenance failure remains `+0/+0`; a valid frozen numerical inequality/non-finiteness is scientific FAIL and must not be repaired post hoc.

Live global reconciliation at this ledger update: exactly **1 in-progress workflow** (`34189540992`) and **0 known competing heavy workflows**. Do not duplicate GA.

## Prepared final admission

The GA workflow already contains the frozen hosted `Exp073GB` provenance-admission stage. Current final GB verifier blob: `cc815737e658a850452d9b0f9488e703f8de84ea`. It may run only if `home-science` succeeds; workflow success alone is insufficient unless the raw verifier output contains the exact GB authority token and authority flag.

## Independent C2 frontier

Exp073GZ hosted static audit remains PASS `SUPPORT_PLUS_0_PLUS_0`. Real frozen 28-packet / 1792-byte runtime generation/admission remains blocked by GA home-heavy ownership. Do not start it while GA owns the self-hosted runner.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
