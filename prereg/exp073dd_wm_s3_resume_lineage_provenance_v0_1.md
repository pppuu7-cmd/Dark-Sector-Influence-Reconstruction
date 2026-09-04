# Exp073DD v0.1 — Wm_S3 resume-lineage provenance audit

Status: prospectively frozen support/readiness gate; scientific score `+0/+0` only.

## Authority and scope

This gate is independent of the currently running frozen Exp073BU science process at source head `a2f14dfd5a9e54a30fb467f6d0e717bd4f00bd35`. It MUST NOT alter, restart, cancel, inspect partial numerical output from, or write into that process or its durable checkpoint namespaces.

The observed implementation defect is provenance-only: in `ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py`, a verified restore after `fresh_workspace_mcm_complete` skips fresh reconstruction (correct) but records invocation-local reconstruction counts `{lens:0,source:0}` in the eventual replica receipt. The activation contract requires the cumulative lineage fact that each replica's masks were originally reconstructed exactly once. A correct resume can therefore be misclassified as infrastructure incomplete.

## Frozen repair semantics

A future `v0_2` driver may change provenance bookkeeping only. It MUST NOT alter DES/Wm_S3 science arithmetic, band edges, `NSIDE=4096`, `ell=0..12287`, 39 bands, Wm `TE<-TE`, canonical `<f8 [39,12288]`, exact SHA256/`numpy.array_equal` comparator, NaMaster 2.7 path, checkpoint order, A/B isolation, or any frozen scientific acceptance criterion.

The repair MUST separate:

1. `invocation_new_reconstruction_counts`: work newly performed in the current invocation;
2. `cumulative_reconstruction_counts`: immutable lineage restored from a verified checkpoint.

Fresh construction requires both values to be exactly `{lens:1,source:1}`. A verified resume after the mask/workspace checkpoint requires invocation-new counts exactly `{lens:0,source:0}` while cumulative counts remain exactly `{lens:1,source:1}`. Missing, malformed, non-integer, or any cumulative count other than exactly `{lens:1,source:1}` MUST fail closed. Existing source-head, contract-fingerprint, replica, checkpoint-namespace, historical-import, and cross-replica checks remain fail closed.

## Prospective machine gate

Hosted/static regression only; no DES-scale science numerics and no self-hosted runner.

PASS token: `D1_RESUME_LINEAGE_PROVENANCE_PASS` iff all are true:
- fresh bookkeeping is exactly invocation `{1,1}` and cumulative `{1,1}`;
- verified workspace-resume bookkeeping is exactly invocation `{0,0}` and cumulative `{1,1}`;
- missing/malformed/wrong cumulative lineage fails closed;
- checkpoint identity/source/contract/replica semantics remain fail closed;
- a source/static audit confirms frozen arithmetic constants, band edges, TE selection, exact comparator, 8-worker policy, and checkpoint order are unchanged from v0.1.

Otherwise token: `D2_RESUME_LINEAGE_PROVENANCE_FAIL`.

A D1 result is support/readiness `+0/+0` only and cannot create Wm_S3 scientific authority. The live Exp073BU terminal artifact remains the sole current scientific gate.