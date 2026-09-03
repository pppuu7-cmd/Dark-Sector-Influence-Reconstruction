# DSIR immutable recovery — Exp073CR v0.3 r1 bind failure and r2 diagnostic

Date: 2026-09-03
Scope: DSIR only. Scientific/resource credit: +0/+0.

## r1 repaired continuation terminal state

Run `33770577708`, head `8eded6a41271e77750a0206ba2766fbbb7819dc3`: hosted authorize job `100699474546` SUCCESS; self-hosted job `100699512748` FAILURE in `Bind v0.3 runtime`. Seed restore, helper compile, 64-shard compute and frozen final resource classification were skipped. No shard was computed and durable seed `cb408d4edb2a73413db8d3181e9cb1680dc19276` remains the exact checkpoint authority.

The decoded combined-step log shows the repaired shell source beginning with `test "$(nproc)" -ge "8"`, followed by git-lineage capture, py_compile and static audit commands, then a generic exit code 1 without exposing the exact failing subcommand or its value/output. Therefore this attempt is classified **INFRASTRUCTURE/CONTROL-PLANE INCOMPLETE +0/+0** and no narrower cause is inferred. In particular, the repository must not assume whether `nproc` is below, equal to, or above 8 until measured explicitly.

## r2 diagnostic

Because the combined bind shell masked the first causal subcommand, a narrow diagnostic-only workflow was added at commit `a607cb2a548dfdb569445524b03639ddfa7b298b` and triggered at commit `87ebc2bd850aba7beea6d6f84970ed9241a3e908`.

Diagnostic run/job: `33770780033` / `100700156146`. It performs no numerical Wm_S3 computation and writes no checkpoint. It separates the candidate causes into distinct Actions steps: host CPU availability (`nproc`/lscpu), system Python availability, bound git lineage, Python source compilation, bound source-order static audit, and read-only exact seed-head verification. It is explicitly non-authoritative research/infrastructure diagnostic `+0/+0`.

At note creation job `100700156146` is IN_PROGRESS on `DSIR-HOME-PC`. The runner is therefore reserved exclusively for this diagnostic until terminal. No heavy or competing home workload may be launched.

Exact next action: consume the diagnostic raw log when terminal. If host capacity is `<8` logical CPUs, the current frozen 8-worker CPU-utilization gate is externally BLOCKED on this runner and must not be oversubscribed or threshold-weakened. If host capacity is `>=8`, use the first failed distinct diagnostic step to make only the smallest prospective control repair, hosted-audit it, then resume from the unchanged exact seed.
