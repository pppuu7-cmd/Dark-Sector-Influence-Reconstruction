# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_EXP073FX_S2S2_ADMITTED_AND_EXP073FY_DIRECT_FA_ACTIVE_V17.md` (creation commit `f8bdb43cb377c39b3c9c81c3da8b1c73f2ba0314`). Earlier recovery notes remain immutable history.

## Preserved and newly admitted authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority now includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, and **`S2_S2`**.

`WW_S2_S2` authority was created only by Exp073FW final run `34146468135`, head `d7fdb410819dcec14276e0423c25c0d2f1b29b3b`, after unchanged frozen Exp073FX verifier admitted artifact `10027835016` (`sha256:ef36ddafc5f30d33206fbf952deea5c0f58f5465370a9c8bd96c2b2d61b1ecef`). Admission job `101819621240` raw-emitted `PASS_EXP073FX_WW_S2_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `ww_s2_s2_authority_created=true`.

Frozen S2S2 evidence remains ordered `[2,2]`, same-field `S2->S2`, canonical `<f8 [39,12288] EE<-EE`, finite and exact A/B equality, exact `19,327,352,832`-byte file-backed MCM proof; A/B canonical SHA256 `3daa7894648cc44d3ee822fe5f9b02aa0ccb756b11abfa0852a08b57d4ba75c9`.

Historical FW implementation/infrastructure failures remain historical `+0/+0` and are not rewritten by the final admission.

## Authoritative current heavy process — Exp073FY WW_S2_S3

GitHub-native successor Exp073FY is prospectively frozen by prereg blob `8aacb4e7f6615fe7e30a88ae02eb02ee5f4dba24`. Scientific target is ordered `S2->S3`, indices `[2,3]`, distinct spin-2 fields, `compute_coupling_matrix(f2,f3,b)`, DES NSIDE=4096, ell 0..12287, 39 bands, canonical `<f8 [39,12288] EE<-EE`, exact A/B equality and exact file-backed MCM proof. Only separate frozen Exp073FZ may create `WW_S2_S3` authority.

Three predecessor FY attempts were pre-science implementation `+0/+0`: run `34146528784` invalid shell lexical requirement; run `34146669028` self-matching generated-shell guard; run `34146860145` nested transform self-overwrite. No expensive science/checkpoint authority was created by those failures.

Minimal repairs preserved science: `143723e842104ae62ab426f146dbeceec04207b7`, `0b7812be611ec72f7dbeb30336e9727e1aa0dfc5`, and direct frozen-FA repair **`ed517b6652dc8172c64e5324b842e047c575b2cb`**. Current home blob `63132e199c0af956f27218393240d5f85c681f88`; workflow binding/head **`f04346a8e6909cb4342e536a0e7328f5ca5e54c9`**.

Authoritative run **`34147009217`**:
- hosted audit job **`101821110137`**: SUCCESS, raw `PASS_EXP073FY_HOSTED_LAUNCH_AUDIT_V0_4`, `SUPPORT_PLUS_0_PLUS_0`;
- home-science job **`101821144414`**: IN_PROGRESS inside frozen WW_S2_S3 A/B gate at latest reconciliation;
- owner: `DSIR-HOME-PC-2` / `win-ws338`;
- durable namespace/root: `~/.cache/dsir/exp073fy-ww-s2-s3-filebacked-ab-v0-1`;
- expected candidate token: `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- only FZ token `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may create S2S3 authority.

No competing heavy run is permitted and partial numerical output must not be inspected. On terminal result, independently verify artifact digest, complete A/B checkpoint/provenance chains, ordered distinct-field semantics, exact file-backed proof, finiteness and exact A/B equality before scientific classification/admission. On infrastructure failure preserve completed checkpoints and repair only the first causal defect.

FY retains a temporary path-scoped one-shot push trigger; do not edit it while run `34147009217` is active. Restore dispatch-only semantics at a safe terminal transition. FW's historical recovery trigger also awaits safe cleanup without launching a competing run.

## Independent C2 support frontier

Exp073GW/GX/GY remain hosted support-only `+0/+0`; no real C2 record set/model authority exists. Exact C2 z/k contract and no-rescue policy remain frozen. The next meaningful C2 step is real runtime generation/admission of the complete frozen 28-packet set, **BLOCKED while Exp073FY owns home**. Do not substitute more metadata-only scaffolding.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.