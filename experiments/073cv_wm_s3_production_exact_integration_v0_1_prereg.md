# Exp073CV v0.1 — Wm_S3 production exact-integration gate

Status: **PROSPECTIVELY FROZEN / support-readiness only / +0/+0**

This gate is created after Exp073CU returned `U2_PRODUCTION_ASSEMBLY_GAP_IDENTIFIED`. It closes only the production-interface gap between already validated exact components. It MUST NOT create Wm_S3 scientific authority and MUST NOT activate Exp073BU.

## Frozen purpose

Demonstrate, on hosted synthetic cases only, that a production-capable adapter can connect the already validated full-stock NaMaster-2.7 arithmetic and file-backed memory path without changing any scientific arithmetic:

`stock workspace -> stock write_to() FITS -> workspace release -> row-stream canonical <f8 MCM -> verified read-only OS mmap -> exact full-stock ncls=2 downstream -> full <f8 [2,nb,2,nl] -> Wm TE <- TE -> canonical <f8 [nb,nl] receipt`.

The hosted gate is an executable regression/static audit. It is not DES Wm_S3 numerical production.

## Frozen inherited authority

The implementation must preserve the exact validated operation order and semantics from Exp073BX/BY/CA/CC, the fresh-PCL/provenance rules admitted for Exp073BU, and the six Exp073CD durable boundaries. NaMaster provenance remains the repository-frozen 2.7 authority. No historical Wm_S3 numerical payload may be imported.

For the eventual DES production route the inherited dimensions remain `nl=12288`, `nb=39`, `ncls=2`, full unbinned MCM `24576 x 24576`, canonical selected output `<f8 [39,12288]`, Wm `TE <- TE`. This hosted gate uses small prospectively fixed synthetic dimensions only to prove interface and exact arithmetic equivalence.

## Required production interface

The adapter must expose explicit paths/identities for input workspace or workspace-MCM FITS, canonical mmap backing, full-window output, selected-TE output, checkpoint namespace and receipt. The receipt must bind at least source-head/contract identity, component blob identities, input identity, dimensions, mmap proof, full-window SHA256 and selected-TE SHA256.

The implementation must:

1. persist a stock workspace via stock `write_to()`; DES-scale `get_coupling_matrix()` materialization is forbidden;
2. canonicalize the persisted unbinned MCM one complete row at a time, never requiring a second full-MCM heap copy;
3. verify fail-closed that the numerical MCM base chain reaches `mmap.mmap` and that the exact backing path appears in `/proc/self/maps`;
4. preserve the exact Exp073BX/BY full `ncls=2` source-order binning, GSL LU/inversion and BLAS multiplication order before selecting TE;
5. materialize the full canonical tensor before selecting `full[0,:,0,:]` as Wm TE;
6. hash exact canonical bytes; use `numpy.array_equal` plus canonical SHA256 equality for executable regression acceptance;
7. preserve the Exp073CD boundaries `fresh_masks_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_te_complete -> replica_receipt_complete` and A/B namespace isolation in the production-facing contract.

## Fail-closed prohibitions

No tolerance, rounding, smoothing or averaging rescue. No effective ell/z/k. No fiducial-P shortcut. No selected/general-coupling arithmetic substitute. No historical Wm_S3 PCL/window/band numerical import. No cross-replica numerical restore. No silent fallback from mmap to resident full-MCM materialization. No weakening of any Exp073BU scientific criterion.

## Frozen hosted cases

Use the same three deterministic small synthetic mask/bin cases already exercised by the validated exact-chain QA where practicable, with fixed seeds and source-order binning. The candidate production adapter output must be compared against the stock/full validated reference route for the complete full tensor and selected TE tensor. Acceptance is exact only.

## Frozen classification

- `I1_PRODUCTION_INTERFACE_EXACT_INTEGRATION_PASS`: all static/fail-closed interface checks pass; every frozen synthetic case has full-tensor canonical SHA equality, full `numpy.array_equal == true`, selected-TE canonical SHA equality and selected `numpy.array_equal == true`; mmap backing proof passes; forbidden materialization/import patterns are absent.
- `I2_ARITHMETIC_EQUIVALENCE_FAIL`: valid candidate and reference executions complete but any exact full/selected equality condition fails. This is a negative support result `+0/+0`; no tolerance rescue.
- `I3_PRODUCTION_INTERFACE_INCOMPLETE`: a required production interface, receipt binding, checkpoint boundary, mmap proof or fail-closed guard is absent/incomplete. `+0/+0`.
- `I4_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL`: execution cannot validly reach comparison because of infrastructure, dependency, source-head/blob/provenance binding, build or transport failure. Diagnose the first causal failure prospectively. `+0/+0`.

`I1` authorizes only the next hosted executable/integrated-driver audit and subsequent explicit activation review. It does **not** activate Exp073BU or create Wm_S3 scientific authority.
