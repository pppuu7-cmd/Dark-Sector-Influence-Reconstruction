# DSIR immutable recovery — Exp073CR v0.3 home bind failure and r1 prospective repair

Date: 2026-09-03
Scope: DSIR only. Scientific/resource credit: +0/+0.

Run `33770178685`, head `3404eccc347d5f44f1cdc1514078d411fce1682b`: hosted authorize job `100698111100` SUCCESS; home job `100698177477` FAILURE before seed restore or numerical compute.

Decoded raw log establishes the first causal failure in step `Bind v0.3 runtime`: shell exited at `test "$(nproc)" = "8"` before any Python compile/static audit output. Later steps were skipped. No shard was computed and the exact hosted seed `cb408d4edb2a73413db8d3181e9cb1680dc19276` remains untouched. The later `CR_ROOT: unbound variable` in the always-run artifact-preparation path is secondary fallout, not the first cause.

Classification: **INFRASTRUCTURE/CONTROL-PLANE FAILURE +0/+0**, not resource/performance FAIL and not Wm_S3 scientific FAIL.

Causal diagnosis: frozen DSIR heavy architecture requires exactly 8 outer compute workers and nested threads=1. It does not require the host to expose exactly 8 logical CPUs. Therefore `nproc==8` was an over-constrained machine-property check unrelated to frozen scientific arithmetic or the CPU acceptance threshold.

Prospective r1 control repair at home-workflow commit `9eafc1c431f508d7a34800328b6718f146b346b5` changes only the machine availability guard to `nproc>=8`; the actual ProcessPool remains exactly 8 workers, nested threads remain 1, shard geometry/order and exact reconstruction are unchanged, CPU threshold remains `>=0.90`, and swap increase remains forbidden. The artifact-preparation fallback was also made fail-safe when `CR_ROOT` was never created, without changing numerical execution.

A dedicated hosted repair audit workflow was added at commit `6fc6db1d0e074d02ce6e58e7ed58977e76a18b75` and triggered by commit `3c3086489195bdc610ec026772a148fec5b15625`. Audit run `33770476672`, job `100699131834` is QUEUED at note creation. It must PASS token `PASS_EXP073CR_V0_3_R1_NPROC_CONTROL_AUDIT` before the activation file may be updated to launch exactly one repaired home continuation.

Until that hosted audit passes, DSIR-HOME-PC is FREE but Exp073CR home relaunch is BLOCKED by the prospective audit interlock. No blind rerun is allowed.
