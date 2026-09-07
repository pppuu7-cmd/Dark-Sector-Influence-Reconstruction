# DSIR recovery V18 — Exp073FY active; Exp073GA direct-FA successor repaired prospectively

Date: 2026-09-07. Scope: **DSIR only**. RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority remains `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`. No new scientific authority is created by this recovery note.

## Authoritative current heavy process — unchanged

Exp073FY run `34147009217`, head `f04346a8e6909cb4342e536a0e7328f5ca5e54c9` remains the sole authoritative heavy process. Hosted launch audit job `101821110137` is SUCCESS with `PASS_EXP073FY_HOSTED_LAUNCH_AUDIT_V0_4`; home job `101821144414` remains IN_PROGRESS inside the frozen WW_S2_S3 A/B gate. Owner: `DSIR-HOME-PC-2` / `win-ws338`; checkpoint root `~/.cache/dsir/exp073fy-ww-s2-s3-filebacked-ab-v0-1`. No competing home run was launched and no partial numerical output was inspected.

Frozen FY science remains ordered `S2->S3`, indices `[2,3]`, distinct spin-2 fields, `compute_coupling_matrix(f2,f3,b)`, DES NSIDE=4096, ell 0..12287, 39 bands, canonical `<f8 [39,12288] EE<-EE`, exact file-backed MCM proof, finiteness and exact A/B equality. Only Exp073FZ admission token `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may create WW_S2_S3 authority.

The FY workflow already contains fail-closed hosted FZ admission and deterministic dispatch of the prospectively installed final heavy successor `exp073ga-ww-s3-s3-home-science-v0-1.yml` after FZ PASS.

## New independent pre-launch finding — Exp073GA launcher architecture

While FY was running, the installed future Exp073GA WW_S3_S3 successor was audited without executing it. Its previous home launcher blob `775348eb79f6f15d5c11a15fb6866bb1fa5f6774` transformed the older `exp073fm_home_filebacked_fullres_v0_1.sh` nested-generator route. That is the same architectural class that previously caused pre-science nested self-overwrite failures in FW/FY. This was an implementation-risk finding only; GA had not run and no GA scientific/checkpoint result existed.

A minimal prospective repair changed only the launcher architecture:

- commit `4a232aa8369ba8e4f6c5a247ecaf2b75696ced8c`;
- new GA home blob `90e8fc8ba66dce9c47cccb5ce79fbc0cebed2259`;
- GA now directly transforms the already-proven frozen FA launcher blob `309c464bbfbe4896bd560165985ee7f643d9ee22`, matching the repaired FW/FY architecture;
- S3->S3 driver/pruner/comparator identities remain unchanged;
- frozen source order `[3,3]`, `compute_coupling_matrix(f3,f3,b)`, domain, arithmetic, exact equality, file-backed proof and no-rescue acceptance remain unchanged;
- terminal path remains per-replica verify/prune followed by exact receipt comparison; legacy `--replica AB` restore path is fail-closed absent;
- generated transformed shell is syntax-checked with `bash -n` before execution.

Workflow binding commit `71f552c802d720583b85b14790671fe02122c7da` updates only the GA home blob binding and strengthens the hosted static audit to require the frozen FA base, exact base blob, and `bash -n` path. GA is dispatch-only, so this maintenance did **not** launch a heavy job. Expected hosted audit token is now `PASS_EXP073GA_HOSTED_LAUNCH_AUDIT_V0_2`.

This repair is `SUPPORT/IMPLEMENTATION +0/+0`; it does not create or alter scientific authority.

## Exact next actions

1. Continue to watch only Exp073FY `34147009217`; do not duplicate it.
2. On terminal FY success, independently consume logs/artifact and require frozen FZ admission before accepting WW_S2_S3 authority.
3. If FZ admits, the installed GA successor may be dispatched by the FY workflow; its hosted launch audit must raw-emit `PASS_EXP073GA_HOSTED_LAUNCH_AUDIT_V0_2` before home science.
4. On FY infrastructure failure, preserve all complete durable checkpoints and repair only the first causal defect prospectively.
5. C2 real 28-packet runtime generation remains blocked while FY owns home; no further metadata-only scaffolding is justified.
