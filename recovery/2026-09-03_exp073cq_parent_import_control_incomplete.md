# Exp073CQ terminal — parent-import control/infrastructure incomplete

Date: 2026-09-03
Classification: `INFRASTRUCTURE_CONTROL_INCOMPLETE_DURING_PARENT_IMPORT`
Scientific credit: +0/+0
Resource credit: +0/+0

## Immutable execution identity

- experiment: Exp073CQ v0.1
- GitHub Actions run: `33742582807`
- launch/head: `ef4f02f0ff3e23d845b6dcd1f45317a0d3811b12`
- authorize job: `100607659399` — SUCCESS
- self-hosted job: `100607697336` — FAILURE
- self-hosted runner: `DSIR-HOME-PC`, runner id `21`
- self-hosted started: `2026-09-03T11:17:15Z`
- self-hosted completed: `2026-09-03T11:27:19Z`

## Last observed step state

Completed successfully before failure:

1. Set up job
2. actions/checkout
3. exact runtime lineage binding
4. proven NaMaster 2.7 environment
5. restore/initialize successor checkpoint first

The job terminated while GitHub still reported step 6, `Exact import of immutable Exp073CP band0-28 authority`, as the active/in-progress step.

Never started:

- `Compile or restore frozen complete-band helper checkpoint`;
- `Missing29-38 bounded eight-worker compute with per-band durability and diagnostics`;
- `Frozen final classification`;
- artifact upload.

Therefore no Exp073CQ numerical Wm_S3 band 29..38 was admitted and no CPU/swap/exact final comparator was executed.

## Durable-state audit

At terminal inspection:

- `refs/heads/checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-1` does NOT exist;
- GitHub Actions artifact list for run `33742582807` is empty (`total_count=0`);
- decoded job-log retrieval for job `100607697336` returns `BlobNotFound`;
- no durable successor diagnostic is available.

Consequently the exact lower-level exception inside the parent-import shell step is unresolved and MUST NOT be invented. Timing alone is insufficient to label the failure TLS, fetch, validation, import, or push.

## Diagnostic-contract consequence

Two live control audits discovered before/at terminal state:

- `recovery/2026-09-03_exp073cq_diagnostic_coverage_static_audit_gap.md`;
- `recovery/2026-09-03_exp073cq_precompute_diagnostic_durability_addendum.md`.

The frozen workflow performs parent restore and imported-parent checkpoint push directly in shell under `set -euo pipefail`, outside the Python diagnostic wrapper. Non-compute Python diagnostics are also local-only unless later staged. Therefore this failure occurred in a control region where the preregistered canonical diagnostic guarantee was incompletely implemented.

The historical hosted audit PASS remains immutable but is no longer evidence of complete failure-path diagnostic coverage.

## Preserved parent authority

Exp073CP durable parent remains unchanged and authoritative for the completed resource checkpoint state:

- namespace `checkpoints/exp073cp-wm-s3-full39-resource-v0-1`;
- head `025629d9bb7b113bd0548ff6a32c6ee5812ae245`;
- contract fingerprint `32d15a39f1bcdcee0f9b9f88ebc8fd8f82eb850bb71eca4b51d95eb40f111efc`;
- exact complete bands `0..28`;
- bands `29..38` absent.

Bands `0..28` MUST NOT be numerically recomputed in the next resource successor.

## Why Exp073CQ must not be rerun unchanged

A blind rerun of the same frozen CQ implementation would preserve the now-known diagnostic-coverage defect and would not address the independently established complete-band tail-granularity risk. It would spend home-runner time without improving the protocol.

This terminal CQ state is therefore permanent `+0/+0` infrastructure/control history. Any repair must be a NEW prospectively versioned/bound successor.

## Next research direction

Before another heavy home dispatch, the new successor should close two independent gates:

1. **control/transport gate:** structural diagnostic coverage for every restore/import/materialization/checkpoint-sync failure and durable always-upload diagnostic staging; exact parent checkpoint acquisition must be robust and fail closed;
2. **numerical resource architecture gate:** hosted bitwise proof of exact-safe `ll3` output sharding against frozen Exp073CP band payloads, followed by a balanced multi-shard eight-worker resource design only if equivalence PASSes.

Non-authoritative preflight currently favors about 64 balanced complete `ll3` shards over missing bands 29..38, with modeled scheduling utilization ~0.977 versus ~0.54 for ten indivisible complete bands. Those numbers are planning evidence only and are not an Exp073CQ result.

Wm_S3 scientific authority remains absent. Full Wm_S3 A/B scientific production remains forbidden.
