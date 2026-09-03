# Exp073CR 64-shard scheduler v0.0 — SUPERSEDED / NEVER EXECUTED

Status: NON-AUTHORITATIVE RESEARCH HISTORY ONLY. Scientific/resource credit: +0/+0.

`exp073cr_64shard_scheduler_v0_0.py` was inspected before any execution and found to bind a nonexistent C helper symbol `exp073cr_stream_band_ll3_range`. The actual research helper v0.1 exports `exp073cr_stream_compress_band_ll3_range_v0_1`.

The defect was caught prospectively. v0.0 was never used in GitHub Actions or on the self-hosted runner and has no numerical/checkpoint authority.

Superseding research implementation: `exp073cr_64shard_scheduler_v0_1.py`, which uses an explicit `HELPER_SYMBOL`, probes the ABI before worker launch, and records the symbol in every shard receipt.
