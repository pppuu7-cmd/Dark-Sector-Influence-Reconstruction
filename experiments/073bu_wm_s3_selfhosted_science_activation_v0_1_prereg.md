# Exp073BU — Wm_S3 self-hosted science activation v0.1

**Frozen prospectively:** 2026-09-04 after Exp073CX v0.4 `A1_EXP073BU_ACTIVATION_READINESS_PASS`, before any self-hosted Exp073BU Wm_S3 A/B numerical science output exists.

Scope: DSIR only. RTK/RQIR excluded.

## Purpose

This document freezes only the final execution/activation shell needed to run the already-preregistered Exp073BU science contract. It does **not** change the science operator, masks, binning, equality rule, thresholds, or classification vocabulary in `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`.

The original Exp073BU preregistration remains the science authority:

- prereg commit: `e1a0332c128c87049fb8699018a3a3e71c9c5321`;
- prereg blob: `816542c7eb7a8ba4e72d6e01228aa62d05c7c805`;
- required PASS raw token: `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`.

## Frozen admitted implementation chain

The self-hosted activation may use only the following exact repository blobs:

- unified production A/B driver `ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py`: `5c8d5d3463e455389a1ca3df2639bf06a3b7b603`;
- fresh S3 mask/PCL authority helper `ci/exp073bu_fresh_wm_s3_pcl_v0_1.py`: `73ef04c479547dc8e2e89c9f511f1a55fae3ed64`;
- production exact adapter `ci/exp073cv_wm_s3_production_exact_adapter_v0_1.py`: `dafe86086a470c852106f0d4ecccbda1d389e397`;
- exact component lineage `ci/exp073cv_component_blobs_v0_1.json`: `0d6d6e882d1a4cf1ff79fbe8227a4f2b460c7e40`;
- admitted full-stock mmap downstream `ci/exp073by_mmap_full_mcm_downstream_v0_1.c`: `acafb095deafae7602101d8305e239341010ba79`;
- final science launcher `ci/exp073bu_wm_s3_science_launcher_v0_1.py`: `1a54ad89d32dd217443bc3062a6215bf10e8b17d`.

The launcher is intentionally separate from the frozen production driver. It invokes replica A and replica B as separate fresh processes and does not use the driver's internal `AB` comparator. This is required because the original production driver was admitted by Exp073CX for exact SHA/`numpy.array_equal` execution semantics but its internal mismatch label is a technical `FAIL_EXP073BU...` token, whereas the science preregistration freezes the terminal scientific class `SCIENTIFIC_REPEATABILITY_FAIL`. The launcher therefore preserves the already-frozen numerical implementation while enforcing the original preregistration's exact terminal vocabulary prospectively, before any Exp073BU science output exists.

No numerical mismatch has been observed or inspected in making this execution-shell repair.

## Frozen upstream hosted authority

The activation is allowed only if immutable recovery `recovery/2026-09-04_exp073cx_v0_4_a1_activation_readiness_pass.md` remains an ancestor and contains `A1_EXP073BU_ACTIVATION_READINESS_PASS`. Its current blob is `43b658028f74b7a0b52fca8261beeb58026d8ffc`.

CW H1, CV I1 and CZ Z1 immutable authorities consumed by CX remain inherited without reinterpretation. Historical CX v0.1/v0.2/v0.3 and CZ v0.1 negative results remain immutable.

## Execution order

1. A hosted-only static activation audit must PASS against all exact blobs above and the manual science workflow before any home numerical job is allowed.
2. After that PASS, the science workflow must be explicitly activated by `workflow_dispatch` on `main`; no push or schedule trigger is allowed for science.
3. A hosted preflight in that manually activated run must re-bind the source head, exact implementation blobs, original prereg and this activation prereg, and must verify no competing queued/in-progress DSIR Actions workload except the current run.
4. Exactly one self-hosted `[self-hosted, Linux, X64]` job may own `DSIR-HOME-PC`.
5. Before numerical work, that home job must acquire an exclusive local DSIR lock, perform a fresh Actions noncompetition check, verify at least 8 available CPUs, verify the process ledger, and reject known competing DSIR/heavy cosmology processes.
6. The home job must independently stage and hash-verify the frozen R1 S3 source payload and first-party DES lens mask, bind PyMaster/NaMaster 2.7, compile the admitted exact downstream, then execute A followed by B sequentially.
7. Replica state must remain isolated under the original namespaces `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`. Durable local checkpoint payloads may survive infrastructure interruption only under exact source-head + contract-fingerprint identity; mismatched restore is fail-closed.
8. Only after both complete receipts exist may the launcher compare the entire canonical `<f8 [39,12288]` arrays by both exact SHA256 equality and `numpy.array_equal`.

## Frozen terminal classes

The launcher/workflow must preserve the original preregistration vocabulary exactly:

- `PASS` only with full valid provenance, exact whole-array SHA256 equality and `numpy.array_equal`; emit raw token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`.
- `SCIENTIFIC_REPEATABILITY_FAIL` only when two complete provenance-valid A/B arrays differ exactly.
- `INFRASTRUCTURE_INCOMPLETE` when two valid comparable arrays do not exist because of execution/dependency/runner/artifact/checkpoint infrastructure failure.
- `BLOCKED` when source/prereg/implementation/provenance/exclusivity/checkpoint identity is invalid or ambiguous before valid science comparison.

No tolerance, ULP, rounding, smoothing, averaging, rerun-to-prefer, effective-scale or fiducial-P rescue is allowed.

## Activation boundary

Creating, auditing, or displaying the workflow does not activate science and creates `+0/+0` authority. The explicit manual `Run workflow` action is the activation event, but numerical execution remains blocked unless the preceding hosted static audit and the run-local hosted/live preflights are all valid.

Until a terminal valid `PASS` is consumed against the original Exp073BU preregistration, Wm_S3 scientific angular authority remains absent and Article-3 readiness is not increased by this activation shell.
