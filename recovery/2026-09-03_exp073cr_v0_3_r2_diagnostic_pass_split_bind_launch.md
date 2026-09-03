# DSIR immutable recovery — Exp073CR v0.3 r2 diagnostic PASS and split-bind launch

Date: 2026-09-03
Scope: DSIR only. Credit: +0/+0.

Diagnostic run/job `33770780033` / `100700156146` completed SUCCESS with raw token `PASS_EXP073CR_V0_3_R2_HOME_BIND_DIAGNOSTIC`. The exact DSIR-HOME-PC environment measured `nproc=8`, `_NPROCESSORS_ONLN=8`, 4 physical cores x 2 threads, `/usr/bin/python3` Python 3.14.4. Bound commits were driver `365fd7a8527b2dafe4785f95fa104276788c11d1`, repaired workflow `9eafc1c431f508d7a34800328b6718f146b346b5`, binding `0e0d13a6f7736eb56689d57c3557410007ec48d2`. `py_compile` passed, source-order static audit passed, and read-only seed identity remained exactly `cb408d4edb2a73413db8d3181e9cb1680dc19276`.

Therefore the previous r1 combined bind failure is not attributable to insufficient online CPU count, missing system Python, bad bound lineage, Python syntax, static-audit failure, or seed-head drift. Because all individual controls pass on the exact runner, the smallest prospective repair is control-plane isolation only: split the combined bind shell into distinct fail-closed Actions steps, without changing numerical arithmetic, shard geometry/order, worker count, nested threading, CPU threshold or swap rule.

Split-bind workflow commit: `3f78577a12d5c6943f713c1451948ce00b8acc26`. Dedicated hosted audit run/job `33770942410` / `100700703465` completed SUCCESS with raw token `PASS_EXP073CR_V0_3_R2_SPLIT_BIND_CONTROL_AUDIT`, while also revalidating base token `PASS_EXP073CR_V0_3_SOURCE_ORDER_STATIC_AUDIT`, exactly 8 ProcessPool workers, CPU_MIN=.90, durability-before-refill, bound driver/namespace and unchanged exact seed head.

Immediately before activation live Actions audit showed `0 in_progress` and `0 queued`. Repaired activation commit `1e4345286d8816ff3d850d3a39b8aff0645948df` triggered exactly one Exp073CR v0.3 resource run `33771012683`. At note creation hosted authorize job `100700943092` is QUEUED. When the self-hosted job is instantiated, it exclusively owns DSIR-HOME-PC. No competing home workload is allowed.

Exact next action: consume run `33771012683` as it advances. If the split bind succeeds, restore the unchanged exact v0.3 seed and proceed with the frozen 64-shard resource gate. At terminal, inspect durable shard receipts, exact reconstructed complete-band equality, durability ordering, swap and CPU>=0.90 before any authority classification.
