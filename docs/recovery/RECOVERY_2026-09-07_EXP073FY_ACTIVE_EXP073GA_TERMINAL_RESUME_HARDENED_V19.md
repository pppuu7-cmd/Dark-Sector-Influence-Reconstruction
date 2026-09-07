# DSIR recovery — Exp073FY active / Exp073GA terminal-resume hardening V19

Date: 2026-09-07. Scope: DSIR only. Repository state is authoritative.

## Current heavy authority

Exp073FY `WW_S2_S3` run `34147009217`, head `f04346a8e6909cb4342e536a0e7328f5ca5e54c9`, remains IN_PROGRESS on home job `101821144414` (`DSIR-HOME-PC-2` / `win-ws338`). Hosted launch audit job `101821110137` is SUCCESS. No competing home-heavy run was launched, and no FY partial numerical result was inspected.

Frozen FY science is unchanged: ordered distinct fields `S2->S3`, `[2,3]`, DES NSIDE=4096, ell `0..12287`, 39 bands, canonical `<f8 [39,12288] EE<-EE`, exact file-backed proof, finiteness and exact A/B equality. Only Exp073FZ may create `WW_S2_S3` authority.

## Independent prospective GA audit while FY owns home

The already-installed final heavy successor Exp073GA `WW_S3_S3` had been repaired to the direct frozen-FA launcher before any GA run. A further infrastructure-only audit identified one recovery-class risk inherited from the pre-hardened terminal path: after a future GA run has already produced and pruned a complete replica checkpoint, a retry must not feed that intentionally pruned checkpoint back through the full expensive driver. This is the same class of recovery defect previously encountered and repaired for Exp073FW; it is not a scientific result.

Prospective repair commit `e9aa36283d0f3b78a91b8a855326c0faec9a613c` updates only `ci/exp073ga_home_filebacked_fullres_v0_1.sh`; new blob `f28bf114e6da502e2a3a0a97f0828c27849814c9`.

The hardened GA tail now:
- selects a terminal-pruned restore path only when `post_receipt_prune.json` exists for the replica;
- otherwise runs the frozen replica driver and GA pruner normally;
- never sends a terminal-pruned checkpoint back through the full-stage driver;
- runs the frozen GA terminal comparator before re-attesting historical pre-prune proof tokens on a restore path;
- re-attests `PASS_EXP073GA_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1` and the corresponding B token only after comparator revalidation of prune receipts, stage-manifest hashes, terminal receipts, selected-EE payloads, exact A/B equality and finiteness;
- retains fail-closed rejection of legacy `--replica AB` restore and all tolerance/rounding/smoothing/averaging rescue paths.

Workflow binding commit `d149630f30f3e904c78c7ca43f32917f9e2aaf85` updates `.github/workflows/exp073ga-ww-s3-s3-home-science-v0-1.yml` to require the new home blob and statically require both terminal-pruned restore tokens and both re-attested pre-prune proof tokens. Workflow blob after binding: `e7505c0264b0f66aa2682a326486567784a54135`.

Frozen GA science remains unchanged: ordered `[3,3]`, same-field `S3->S3`, `compute_coupling_matrix(f3,f3,b)`, exact A/B equality, exact file-backed proof; only Exp073GB may create `WW_S3_S3` authority. This repair is `SUPPORT +0/+0` and does not alter any scientific readiness/gate result.

GA remains workflow-dispatch only and was not launched while FY is active. FY/FZ retains sole authority to dispatch GA after successful independent `WW_S2_S3` admission.

## Current next actions

1. Keep FY run `34147009217` as the sole home-heavy owner; do not rerun or duplicate it while active.
2. On FY terminal state, inspect artifact/log/provenance and classify according to the frozen FY/FZ contract before any successor action.
3. If FY/FZ admits `WW_S2_S3`, allow the preregistered dispatch path to GA; the hardened GA launcher is now recovery-safe for terminal-pruned retries.
4. If FY fails for infrastructure/software reasons, preserve complete checkpoints and repair/resume from the first causal defect without changing frozen science.
5. Independent C2 real 28-packet runtime generation remains BLOCKED while FY owns home.
