# DSIR immutable recovery — Exp073CC v0.1 V1 verified OS mmap exact chain

Date: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.
Accounting: support/resource +0/+0; no Wm_S3 scientific authority created.

## Prospective authority
Exp073CC v0.1 preregistration commit: `02ae088e01aeeb4b9476c2e9b195ea5161ff07f8`.
Helper commit/blob: `a5ba4af5b1a0c0c264ed43d492e5d87a81c888b8` / `88d17ad76cabc1651df6b6035d897e9f42853ca5`.
Workflow commit: `9c48482d070a908ade70daf2ab821f061e6bf9ce`.
Activation/head: `2bbb68a2e08be1ac7ed7567361d5d41b5bfdc81c`.
Frozen outcomes included `V1_VERIFIED_OS_MMAP_AND_EXACT_CHAIN` through `V5_INFRASTRUCTURE_INCOMPLETE`.

## Validated terminal
Run/job: `33831289247 / 100894641290`.
Workflow conclusion: success, but this is not itself the scientific/support classification.
Artifact: `9921785254`, name `exp073cc-fits-mmap-verification-2bbb68a2e08be1ac7ed7567361d5d41b5bfdc81c`.
Actions digest and independently downloaded ZIP SHA256: `81378d4da4886615bac73f573e36ca8bb25ed1ac0c86e98f96439ae2dc30b901`.

Raw receipt status: `V1_VERIFIED_OS_MMAP_AND_EXACT_CHAIN`.
All three frozen cases satisfy stock/emulator full-tensor SHA equality, `numpy.array_equal=true`, and `max_abs_difference=0.0`. Each case records base chain `numpy.ndarray -> numpy.ndarray -> mmap.mmap`, `os_mmap_backed=true`, `/proc/self/maps` path observed, and maximum canonical row buffer 768 bytes. NaMaster lineage is 2.7 and GSL lineage is 2.7. No tolerance rescue was used.

## Classification
Authoritative Exp073CC support/resource result: **V1 PASS +0/+0**.
This closes the Exp073CB verification defect: the exact stock-write-to/read-only-mmap/downstream chain is both bitwise exact on the frozen synthetic cases and explicitly OS-mmap backed.
It does **not** score Wm_S3 science and does not activate Exp073BU.

## Permitted successor
V1 permits prospective DES-scale Exp073BU resource sizing and checkpoint architecture design. The successor must preserve full stock `ncls=2` arithmetic, fresh replica-local PCL construction, durable checkpoint semantics, exact canonical reassembly, and fail-closed provenance. No old Wm_S3 numerical payload may be reused as a scientific input.
