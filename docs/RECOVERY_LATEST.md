# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_EXP073FY_ACTIVE_EXP073GZ_PREREG_V20.md` (creation commit `8fe8db6af6a144dbf1c68901b87a1b91ec6ffb76`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, and `S2_S2`.

`WW_S2_S2` authority remains Exp073FW final run `34146468135`, artifact `10027835016`, digest `sha256:ef36ddafc5f30d33206fbf952deea5c0f58f5465370a9c8bd96c2b2d61b1ecef`, admitted by Exp073FX job `101819621240` with `PASS_EXP073FX_WW_S2_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1` and `ww_s2_s2_authority_created=true`. Historical FW failures remain historical `+0/+0`.

## Authoritative current heavy process — Exp073FY WW_S2_S3

Run **`34147009217`**, head `f04346a8e6909cb4342e536a0e7328f5ca5e54c9`:
- hosted audit job `101821110137`: SUCCESS, raw `PASS_EXP073FY_HOSTED_LAUNCH_AUDIT_V0_4`, support `+0/+0`;
- home job **`101821144414`**: IN_PROGRESS inside the frozen A/B gate at latest reconciliation;
- owner `DSIR-HOME-PC-2` / `win-ws338`;
- checkpoint root `~/.cache/dsir/exp073fy-ww-s2-s3-filebacked-ab-v0-1`;
- frozen target ordered `S2->S3`, `[2,3]`, distinct fields, DES NSIDE=4096, ell 0..12287, 39 bands, canonical `<f8 [39,12288] EE<-EE`, exact file-backed MCM proof, finiteness and exact A/B equality;
- candidate token `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- only FZ token `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may create WW_S2_S3 authority.

No competing heavy run is permitted and partial numerical output must not be inspected. On terminal success, independently verify artifact digest, complete A/B durable chains, provenance, ordered distinct-field semantics, exact file-backed proof, finiteness and exact equality before scientific admission. On failure preserve complete checkpoints and diagnose the first causal defect.

FY still retains its temporary one-shot path trigger; do not edit FY while run `34147009217` is active.

## Prospectively hardened final heavy successor — Exp073GA WW_S3_S3

The dispatch-only GA successor uses the proven direct frozen-FA base. Direct-base repair remains commit `4a232aa8369ba8e4f6c5a247ecaf2b75696ced8c`. Additional terminal-resume hardening commit `e9aa36283d0f3b78a91b8a855326c0faec9a613c` updates only the GA home launcher; current home blob is `f28bf114e6da502e2a3a0a97f0828c27849814c9`. Workflow binding commit `d149630f30f3e904c78c7ca43f32917f9e2aaf85` requires that blob plus explicit terminal-pruned restore and post-comparator re-attestation tokens. Expected GA hosted token remains `PASS_EXP073GA_HOSTED_LAUNCH_AUDIT_V0_2`.

Frozen GA science remains unchanged: ordered `[3,3]`, same-field `S3->S3`, `compute_coupling_matrix(f3,f3,b)`, exact A/B equality and exact file-backed proof. Only Exp073GB may create WW_S3_S3 authority. GA remains workflow-dispatch only and FY's hosted FZ admission dispatches GA only after successful frozen S2S3 admission.

## Independent C2 frontier

Exp073GW/GX/GY remain hosted support-only `+0/+0`; no real C2 record-set/model authority exists.

Commit `a8499c404aa2b862cc08634fe4ed20d2753c9f25` prospectively froze `C2_IDE_RUNTIME_ADMISSION_RECEIPT_CONTRACT_V0_1.md`, blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`. It binds a future exact 28-packet / 1792-byte raw record set to producer/build/config/model-point/coordinate/provenance identities and keeps decoding, mapping, prediction readiness and scientific authority false.

Exp073GZ static audit is prospectively preregistered by commit `d5791df0c81169c9a3797ac1867b921028097579`, exact token `PASS_EXP073GZ_C2_RUNTIME_ADMISSION_RECEIPT_CONTRACT_STATIC_AUDIT_V0_1`. A workflow-install write was rejected by the connector/platform safety layer before any repository write; therefore GZ is **PREREGISTERED / BLOCKED_BY_AUDIT_EXECUTION_PATH**, not PASS/FAIL. Do not bypass or weaken it. Real C2 runtime production remains BLOCKED while FY owns home and additionally requires GZ PASS.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
