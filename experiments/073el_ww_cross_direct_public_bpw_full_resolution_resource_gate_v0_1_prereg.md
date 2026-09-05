# Exp073EL — WW cross direct-public-BPW full-resolution resource gate v0.1 preregistration

Prepared prospectively on 2026-09-05 after terminal Exp073EK `DIRECT_PUBLIC_BPW_ADAPTER_EXACT +0/+0` and while Exp073DT attempt 5 remained queued. This is support/resource preregistration only. It does not activate computation, score a WW science gate, or create WW authority.

## Purpose
Qualify whether the only currently exact cross-workspace adapter candidate established by Exp073EK — serialized PyMaster 2.7 workspace reload followed directly by public `NmtWorkspace.get_bandpower_windows()` — is operationally viable at the frozen DSIR full resolution without changing scientific arithmetic.

## Frozen geometry and semantics
- ordered distinct source fields `(S0,S1)` reconstructed independently from authoritative R1 source pixel-record streams;
- DES `NSIDE=4096`;
- ell `0..12287`;
- existing 39 frozen bands unchanged;
- two distinct spin-2 `NmtField` objects;
- ordered cross workspace `S0 -> S1`, never auto substitution;
- serialize workspace FITS, independently reload it, then invoke only public PyMaster 2.7 `NmtWorkspace.get_bandpower_windows()`;
- full result shape exactly `[4,39,4,12288]`;
- selected result exactly `wins[0,:,0,:] = EE<-EE`, contiguous canonical `<f8 [39,12288]`;
- no manual P/Q reconstruction, inverse, `decouple_cell` composition, alternate tensor layout, tolerance, allclose, rounding, smoothing, averaging, effective ell/z/k, or fiducial-P shortcut.

## Provenance / fail-closed requirements
Activation must prospectively bind source authority, R1 artifact digest, PyMaster 2.7 identity, source head, contract fingerprint, implementation blobs, checkpoint namespace and expected token. Both S0 and S1 map payloads and the serialized cross-workspace FITS must be SHA256-bound. Any restore must verify exact namespace/source-head/contract/payload SHA/shape/dtype before use.

## Durable resource/checkpoint architecture
If executed on `DSIR-HOME-PC`, use exactly one heavy DSIR process under one continuous nonblocking flock. Reuse the repository durable checkpoint standard. Complete-stage boundaries must include at minimum:

`fresh_s0_s1_masks_complete -> fresh_cross_workspace_mcm_complete -> mcm_fits_verified -> direct_public_full_window_complete -> selected_ee_complete -> terminal_resource_receipt_complete`.

Each complete stage receives an atomic manifest. Interrupted/incomplete stages are never treated as complete. A verified expensive complete stage must not be recomputed unnecessarily.

Where independent complete work units actually exist, use exactly 8 outer workers with nested BLAS/OpenMP/MKL/OpenBLAS/NumExpr/BLIS threads pinned to 1. Do not manufacture parallelism by changing PyMaster arithmetic or decomposing a public call in a way that changes its operation ordering.

## Resource classification
This gate is support-only `+0/+0` under all outcomes.

`PASS_EXP073EL_DIRECT_PUBLIC_BPW_FULLRES_RESOURCE_V0_1` requires all frozen provenance/checkpoint checks plus successful completion of the exact direct-public-BPW path at full resolution, exact full/selected shapes and finite canonical payloads, with resource telemetry captured and no fallback arithmetic.

`RESOURCE_FAIL_EXP073EL_DIRECT_PUBLIC_BPW_FULLRES_V0_1` applies when the frozen exact operation is scientifically well-defined but cannot complete within the prospectively specified resource envelope. This is a resource/performance FAIL `+0/+0`, never a WW arithmetic FAIL.

Dependency/runtime/runner loss, malformed artifact, checkpoint corruption, source/contract mismatch or provenance incompleteness is infrastructure/BLOCKED `+0/+0` and requires causal repair/resume, not weakening this contract.

## Activation constraints
Do not activate while any competing self-hosted DSIR heavy run is queued or in progress. In particular, Exp073DT attempt 5 owns `DSIR-HOME-PC` until terminal consumption. Exp073EL PASS is required before Exp073DV may use the Exp073EK direct-public-BPW adapter at full resolution. Exp073DV additionally remains blocked on valid `WW_S0_S0` authority and Exp073EB provenance closure.

Status: `PREREGISTERED_NOT_ACTIVATED`; `science_gate_scored=false`; `ww_authority_created=false`.
