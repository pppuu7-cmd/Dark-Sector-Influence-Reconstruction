# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities: `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, **`S2_S2`**.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-07_EXP073FX_S2S2_ADMITTED_AND_EXP073FY_DIRECT_FA_ACTIVE_V17.md`, creation commit `f8bdb43cb377c39b3c9c81c3da8b1c73f2ba0314`.

## Newly closed — Exp073FX WW_S2_S2 admission

- final Exp073FW run `34146468135`, head `d7fdb410819dcec14276e0423c25c0d2f1b29b3b` SUCCESS;
- home job `101819517843` SUCCESS;
- artifact `10027835016`, digest `sha256:ef36ddafc5f30d33206fbf952deea5c0f58f5465370a9c8bd96c2b2d61b1ecef`;
- unchanged frozen Exp073FX verifier blob `eb907944eac68b9fd13c405399cf238a8cb5bc96`;
- hosted admission job `101819621240` SUCCESS with `PASS_EXP073FX_WW_S2_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `ww_s2_s2_authority_created=true`.

All earlier FW implementation failures remain historical `+0/+0`.

## FY pre-science failures and repairs

- `34146528784`: invalid shell lexical requirement; `+0/+0`;
- `34146669028`: guard self-match; `+0/+0`;
- `34146860145`: nested transform self-overwrite; `+0/+0`.

Minimal repair commits: `143723e842104ae62ab426f146dbeceec04207b7`, `0b7812be611ec72f7dbeb30336e9727e1aa0dfc5`, and direct frozen-FA repair `ed517b6652dc8172c64e5324b842e047c575b2cb`. No frozen FY science changed.

## Authoritative current process — Exp073FY WW_S2_S3

- workflow/run: **`34147009217`**;
- branch/head: `main` / **`f04346a8e6909cb4342e536a0e7328f5ca5e54c9`**;
- hosted audit: **job `101821110137` SUCCESS**, raw `PASS_EXP073FY_HOSTED_LAUNCH_AUDIT_V0_4`, support `+0/+0`;
- home-science: **job `101821144414` IN_PROGRESS** inside frozen A/B gate at latest reconciliation;
- runner owner: **`DSIR-HOME-PC-2`**, machine `win-ws338`;
- checkpoint root: `~/.cache/dsir/exp073fy-ww-s2-s3-filebacked-ab-v0-1`;
- frozen target: ordered `S2->S3`, indices `[2,3]`, distinct fields, canonical `<f8 [39,12288] EE<-EE`, exact `19,327,352,832`-byte file-backed MCM proof, exact A/B equality, no tolerance/rescue;
- expected candidate token: `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- exact next action on SUCCESS: terminal-consume raw logs/artifact, independently verify hashes/provenance/checkpoint chains/finiteness/exact equality, then require frozen Exp073FZ admission token `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` before creating authority;
- exact next action on FAIL/BLOCKED: preserve all complete checkpoints, diagnose first causal defect, smallest prospective repair; a genuine frozen numerical mismatch is scientific FAIL and is never repaired post hoc.

No competing heavy run is permitted. Partial numerical output must not be inspected. FY currently retains its temporary one-shot path trigger and must return to dispatch-only only after a safe terminal transition.

## Independent C2 frontier

Exp073GW/GX/GY remain hosted support-only `+0/+0`. Exact next C2 action is real runtime generation/admission of the frozen 28-packet set, **BLOCKED while FY owns home**; no additional metadata-only scaffolding is justified.

## Global frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.