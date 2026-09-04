# DSIR immutable recovery — Exp073CZ v0.2 scoped unified-driver integration PASS

Date: 2026-09-04. Scope: DSIR only.

Authoritative hosted process: run/job/head `33871304159 / 101017678531 / b7cc90467006718a115b4dba40962cc8275f1c69`; artifact `9935990587`; artifact ZIP SHA256 `f9fdc68c951362c8f0b04cd0c48b3f88f9f9e77b7ddb37b3b4e74c8f095c93b6`; raw receipt SHA256 `03938c3b2f2759a60be1f4d5bfdd6eb23018e9507e0a6688ba20364e02eaa5b1`.

Frozen raw classification: `Z1_UNIFIED_PRODUCTION_AB_DRIVER_INTEGRATION_PASS`, accounting `+0/+0`. No DES-scale Wm_S3 numerics were executed; `science_gate_scored=false`, `wm_s3_authority_created=false`, `exp073bu_activated=false`.

All frozen implementation checks were true: exact 39-band edges; six durable checkpoint boundaries in order; isolated A/B namespaces; one lens/source reconstruction site; exactly two `NmtField` constructors; same-field PCL/workspace handoff; stock `write_to`; forbidden production `get_coupling_matrix` materialization; exact adapter composition; `TE<-TE` semantics; exact SHA comparator plus `numpy.array_equal`; no tolerance rescue; 8-worker contract with nested threads pinned to 1; fail-closed checkpoint identity; source-head/fingerprint binding; no historical Wm_S3 numerical import; no cross-replica numerical read; and corrected `run_replica`-scoped resume ordering.

Historical Exp073CZ v0.1 remains immutable `Z2_IMPLEMENTATION_CONTRACT_FAIL` because its whole-file static verifier mis-scoped the resume-order check. v0.2 does not rewrite that result and does not change production arithmetic or the audited production-driver blob.

This PASS closes the missing unified production A/B driver support layer only. The permitted successor is a fresh prospectively frozen Exp073CX activation-readiness audit that binds the exact production-driver blob and this Z1 support authority before any live/home Exp073BU activation.
