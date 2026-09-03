# Exp073BU support — NaMaster 2.7 stock bandpower-window source/operation-order audit v0.1

Status: **PREREGISTERED NON-SCIENTIFIC SOURCE AUDIT**
Accounting: `+0/+0` for every outcome. No Wm_S3 scientific authority can be created.

## Motivation frozen before output

The preceding frozen synthetic support QA returned `Q2_NUMERIC_ONLY_SELECTED_TE_EQUIVALENCE`: the selected low-memory algebra differs bitwise from stock `NmtWorkspace.get_bandpower_windows()` despite a very small numerical difference. Exp073BU therefore cannot use that selected route as a substitute for its preregistered full-stock-window semantics.

This audit asks where the exact stock operation order is implemented in NaMaster/PyMaster 2.7 and what source-level route must be preserved by any future memory-stable exact-stock implementation.

## Frozen upstream authority

- upstream repository: `LSSTDESC/NaMaster`;
- tag: `v2.7`;
- tag commit: `24365fa59a38c15732f4f37e8b29265b75c442d5`;
- package lineage required at runtime: `pymaster` exactly `2.7` or `2.7.x`.

## Audit actions

Hosted-only job must:

1. install NaMaster/PyMaster 2.7;
2. verify runtime package version;
3. record `inspect.getsource(NmtWorkspace.get_bandpower_windows)` and `inspect.getsource(NmtWorkspace.compute_coupling_matrix)`;
4. clone/fetch the exact upstream tag commit and verify HEAD exactly;
5. search pinned Python/SWIG/C source for all symbols/definitions called by `get_bandpower_windows`, plus binned coupling-matrix inversion/solve routines;
6. record SHA256 for every cited upstream source file and source snippets with function/symbol names;
7. emit only source/operation-order evidence; no DES/R1/current Wm arrays are read.

## Frozen classifications

- **S1_STOCK_OPERATION_ROUTE_IDENTIFIED**: exact v2.7 commit/runtime verified and the stock window wrapper plus downstream source symbols controlling construction/inversion/reshape are identified with pinned file hashes/snippets sufficient to design a prospective emulator QA.
- **S2_PARTIAL_SOURCE_ROUTE**: exact v2.7 commit/runtime verified but one or more downstream compiled/SWIG operation-order steps remain opaque or cannot be tied to pinned source. No emulator authorization.
- **S3_SOURCE_LINEAGE_MISMATCH**: runtime/package/upstream commit does not match frozen v2.7 authority. Diagnose infrastructure/provenance; no semantic conclusion.
- **S4_INFRASTRUCTURE_INCOMPLETE**: installation/fetch/tool failure before a valid source audit. Diagnose first causal failure.

All outcomes remain `+0/+0`. Even S1 does not authorize Exp073BU scientific execution; it only permits a subsequent prospectively frozen exact-stock emulator/equivalence implementation audit.

## Firewall

No DSIR physical data, Exp073R1 artifact, DES mask, historical Wm numerical arrays, current Exp073BU PCL, covariance, nuisance geometry or result-dependent numerical criterion is read or changed.
