# Exp073BU — Article 3 Wm_S3 fresh-independent-PCL A/B exact repeatability v0.1

**Frozen:** 2026-09-04 before any Exp073BU Wm_S3 A/B numerical output exists and after the Exp073CR v0.3 resource gate closed PASS `+0/+0`.

**Scope:** DSIR only. RTK/RQIR excluded.

## Purpose and authority status

Exp073BU is the new prospectively versioned scientific angular-authority successor for the missing `Wm_S3` finite DES Y1 window. It does not revive or modify Exp073AA, Exp073X2 or Exp073AF. Historical Exp073AF `BLOCK_PRODUCTION`, Exp073X2 P=`INFRASTRUCTURE_INCOMPLETE`, Q=`SCIENTIFIC_REPEATABILITY_FAIL`, and all Exp073CM/CQ resource results remain immutable history.

Exp073CR v0.3 authorizes only the exact-arithmetic/checkpoint/resource architecture. **No Exp073CR/CQ/CM numerical Wm_S3 array, band value, hash, checkpoint payload or partial result may be used as a scientific input, reference target, acceptance target or rescue for Exp073BU.** A and B must each construct a fresh Wm_S3 pseudo-C_ell coupling workspace from the frozen upstream mask authorities.

The gate is frozen before output inspection. No acceptance criterion below may be changed after either A or B starts.

## Frozen upstream operator authority

This successor inherits the exact angular science contract from:

- `docs/ARTICLE3_DES_ANGULAR_14_TASK_MANIFEST_2026-08-30.md`;
- Exp073AA preregistration commit `14b79794ab5dc1b8cc8a0fa769ab50cac99f45d9`;
- Exp073X2 exact-repeatability preregistration commit `efe8a4e17638dfd9568fa710e24f56cd10526c6a` only for the prospective independent-replica comparison semantics;
- authority-gap audit commit `1f80751ca1cde9614b7ce8b167d8b4201af117fd`;
- Exp073CR resource-PASS immutable authority only for execution/checkpoint architecture, never numerical authority.

### Source-mask authority — S3

Bind exact hosted Exp073R1:

- run `33270843577`;
- job `99148916507`;
- head `ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- artifact `9720335366`;
- artifact digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- summary logical SHA256 `100458e046088b24cba671db1852112676e487331d5c1f5c5cb55f8a9e011df4`.

For source bin S3 require exactly:

- selected rows `4,196,641`;
- little-endian uint32 pixel-record bytes `16,786,564`;
- pixel-record SHA256 `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`;
- unique occupied pixels `2,943,132`;
- bitpacked occupancy SHA256 `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`.

Each replica independently reconstructs the dense float64 unweighted object-count HEALPix map by adding `1.0` at every selected pixel record and independently verifies all five quantities before NaMaster is invoked.

### Lens-mask authority

Bind the public file `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`:

- bytes `104595840`;
- SHA256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.

Each replica independently reads RING field 0 as float64, maps UNSEEN to zero, retains original mask weights only where `mask>0.5`, and sets every other pixel to zero.

## Frozen software, geometry and binning

- Cosmotheka semantic lineage pinned by the 14-task manifest; no alternative mask semantics.
- NaMaster/PyMaster `2.7` lineage only.
- HEALPix `NSIDE=4096`, `NPIX=201326592`, RING ordering, coordinates C.
- true-ell axis exactly `0..12287`.
- band edges exactly `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`.
- exactly 39 bands.
- spin-0 lens field x spin-2 S3 source field.
- full NaMaster bandpower-window shape must be `[2,39,2,12288]` before component selection.
- selected physical component is exactly `wins[0,:,0,:]`, i.e. output `TE` from physical input `TE` (`TE <- TE`).
- selected logical authority is finite canonical little-endian C-order `<f8 [39,12288]`.
- every band's absolute-response normalization must be finite and strictly positive, as inherited from Exp073AA.
- no effective ell, effective z, effective k, band-center replacement, smoothing, averaging, rounding or tolerance rescue.
- no fiducial-P shortcut.

## Fresh-independent A/B execution contract

Replicas A and B are two **fresh** executions of the same frozen operator. They may reuse validated Exp073CR source code patterns for exact 8-core scheduling/checkpoint durability, but must not import any numerical Wm_S3 output from Exp073CR/CQ/CM or from the other replica.

Before either replica starts, bind this preregistration commit and a static-audited implementation/contract fingerprint.

Each replica must independently:

1. acquire and hash-verify the immutable R1 source authority;
2. acquire and hash-verify the public lens mask;
3. reconstruct both dense masks from upstream authorities;
4. construct its own NaMaster fields/workspace under the frozen contract;
5. compute the complete 39-band selected TE window with exactly 8 outer compute workers when the Exp073CR sharded architecture is applicable, with nested BLAS/OpenMP/MKL/OpenBLAS threads pinned to 1;
6. persist only complete deterministic task/shard or band units, with durability-before-refill, canonical payload SHA256, provenance/contract fingerprint and fail-closed restore;
7. assemble its complete canonical `<f8 [39,12288]` array in exact source order;
8. independently write a final immutable receipt containing canonical array SHA256 and all frozen provenance.

A and B must use distinct durable checkpoint namespaces and must not read one another's checkpoints, arrays, hashes, workspace files or receipts before both final receipts are durably complete.

Default namespaces:

- `checkpoints/exp073bu-wm-s3-a-v0-1`;
- `checkpoints/exp073bu-wm-s3-b-v0-1`.

Only one self-hosted DSIR job may own `DSIR-HOME-PC`. Therefore A and B must not be launched as competing home jobs. A permitted implementation is one explicitly activated self-hosted workflow that executes the two frozen replicas sequentially as independent fresh stages, releasing all replica-local workspace/mask state between stages, while each stage internally uses the validated 8-core architecture. A later implementation may use two non-overlapping home jobs only if a prospective control plane guarantees that B cannot queue/run until A is terminal and this preregistration is not changed.

## Prospective A/B comparison

A lightweight comparator may run only after both final replica receipts exist. It must independently re-hash both stored canonical arrays and require all of the following before a scientific comparison is valid:

- both final receipts declare complete=true;
- both bind the same frozen Exp073BU preregistration/implementation fingerprint;
- exact S3 R1 source identity and hashes match this contract;
- exact lens-mask identity/hash and threshold semantics match this contract;
- PyMaster lineage is 2.7 in both;
- NSIDE/RING/C, ell axis, band edges, full workspace shape and `TE <- TE` semantics match exactly;
- each canonical array has exact dtype/endianness/order/shape `<f8 [39,12288]` and only finite values;
- no forbidden shortcut/firewall flag is present;
- both arrays are re-hashed from canonical bytes by the comparator.

If and only if those provenance conditions are all valid, compare A and B by **both**:

1. exact canonical SHA256 equality; and
2. `numpy.array_equal(A, B)` over the full `[39,12288]` logical arrays.

No tolerance, ULP allowance, rounding, smoothing, averaging, bandwise rescue or selection of a preferred replica is allowed.

## Frozen classification vocabulary

The final comparator must emit exactly one class:

### `PASS`

Allowed only when all provenance checks pass and both full canonical SHA256 equality and `numpy.array_equal` are true. The authority array is the common exact A/B array; neither replica may be preferred based on numerical content.

Required raw token:

`PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`

### `SCIENTIFIC_REPEATABILITY_FAIL`

If both A and B are complete under identical valid frozen provenance/contract and the exact canonical arrays differ by SHA or `numpy.array_equal`, classify as a scientific exact-repeatability FAIL. Preserve both artifacts. Do not repair, average, smooth, choose a replica, or rerun to seek a favorable pair under this frozen gate.

### `INFRASTRUCTURE_INCOMPLETE`

Use when an exact scientific A/B comparison cannot validly occur because a replica/job is cancelled, times out, loses the runner, lacks a dependency, fails artifact/checkpoint transport, has malformed/missing final data, the comparator itself cannot execute, or another software/infrastructure defect occurs before two valid comparable arrays exist. Preserve every verified durable checkpoint and repair only prospectively under a new version.

### `BLOCKED`

Use fail-closed before numerical authority when preregistration/implementation lineage, upstream mask authority, contract fingerprint, source head, checkpoint ownership, live-run exclusivity or another mandatory provenance condition is invalid or ambiguous. No scientific conclusion follows.

`numerically_unresolved` is reserved for an inherited exact downstream threshold ambiguity; this A/B equality gate has no approximate threshold and therefore cannot use `numerically_unresolved` to convert a mismatch into PASS.

## Resource and checkpoint invariants

The Exp073CR v0.3 resource result is frozen only as execution architecture evidence:

- exactly 8 outer workers where applicable;
- nested numerical-library threads = 1;
- independent complete source-order units dynamically scheduled;
- durable checkpoint after every complete unit;
- durability-before-refill;
- exact canonical reassembly and hash verification;
- fail-closed restore;
- resource telemetry.

The Exp073CR frozen resource threshold is **not** a new Wm_S3 scientific acceptance threshold. Resource telemetry must still be recorded to diagnose infrastructure/resource failure, and swap growth must not be silently ignored, but A/B scientific PASS is controlled solely by the frozen provenance and exact equality contract above.

## Anti-leakage firewall

Before Exp073BU terminal classification, neither replica nor comparator may read or score:

- radial kernels or physical-k support;
- Layer-A `operator_f_invalid`;
- Layer-B invalid rows;
- retained coordinates/dimension;
- fiducial P weighting;
- covariance/whitening;
- nuisance SVD/rank;
- relation/null statistics;
- G8/new-physics conclusions;
- any Exp073CR/CQ/CM numerical window as a target.

Frozen global boundaries remain unchanged: `0.295<=z<=2.33`, `0<k<=0.06664762008318016 Mpc^-1`, Layer-A operator_f_invalid `<=0.05`, Layer-B invalid-row fraction `<=0.05`, retained dimension `>=15`. These boundaries are not evaluated inside Exp073BU.

## Readiness accounting

Until the terminal A/B comparator is consumed against this preregistration, Wm_S3 scientific angular authority remains absent and Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.

A `SCIENTIFIC_REPEATABILITY_FAIL`, `INFRASTRUCTURE_INCOMPLETE` or `BLOCKED` result does not create Wm_S3 authority. A `PASS` establishes only the missing exact Wm_S3 angular-window authority; any readiness change must be separately accounted by the already-frozen Article-3 authority ledger rather than invented by this workflow.

## Required pre-execution gates

Before any self-hosted Exp073BU numerical execution:

1. static-audit this preregistration and implementation on hosted GitHub Actions;
2. freeze implementation/contract fingerprint and exact source head;
3. verify checkpoint namespace isolation and fail-closed restore;
4. verify no numerical import/reference to Exp073CR/CQ/CM Wm_S3 outputs;
5. explicitly activate the frozen implementation after audit PASS;
6. re-check live Actions and require no competing queued/in-progress DSIR home workload;
7. update `docs/CURRENT_PROCESS.md` with exact workflow/run/job/head/namespaces and successor actions.

No numerical Exp073BU result has authority before all seven gates are satisfied.