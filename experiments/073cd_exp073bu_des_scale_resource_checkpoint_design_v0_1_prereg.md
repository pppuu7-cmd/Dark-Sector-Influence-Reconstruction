# Exp073CD v0.1 — prospective DES-scale resource/checkpoint design for Exp073BU

Date frozen: 2026-09-04
Scope: DSIR only. Hosted-only support/resource gate. Accounting always `+0/+0`; no Wm_S3 scientific authority may be created.

## Motivation and inherited authority
Exp073CC v0.1 validated the exact stock-write-to OS-mmap downstream chain. Exp073BU remains preregistered and NOT ACTIVATED. This gate sizes the exact full-component stock route and freezes a checkpoint architecture before any DES-scale scientific run.

Inherited frozen science geometry: DES NSIDE=4096; ell=0..12287 inclusive; 39 bands; Wm `TE<-TE`; canonical final `<f8 [39,12288]`; exact arithmetic only.

## Exact deterministic sizing identities
For stock spin-0 x spin-2 coupling, `ncls=2` and `nell=12288`.
Therefore full unbinned MCM logical dimension is `(2*nell) x (2*nell) = 24576 x 24576` doubles.
Frozen exact counts:
- elements = `603979776`;
- raw `<f8` bytes = `4831838208` = exactly `4.5 GiB`;
- one full MCM row = `24576` doubles = `196608` bytes;
- one complete full stock bandpower-window tensor `[2,39,2,12288]` = `1916928` doubles = `15335424` bytes = `14.625 MiB`;
- selected canonical Wm TE payload `[39,12288]` = `479232` doubles = `3833856` bytes.

These are sizing facts, not memory-use measurements and not scientific outputs.

## Frozen resource/checkpoint architecture
Each Exp073BU replica A/B must be independently constructed from immutable S3+lens inputs and may not restore another replica's PCL/MCM/window numerical payload.

Durable stage boundaries, each with canonical SHA256 + provenance/contract fingerprint + source-head identity:
1. `fresh_masks_complete`: fresh replica-local masks/ALMs and input identities.
2. `fresh_workspace_mcm_complete`: stock NaMaster 2.7 workspace has completed the full unbinned MCM; immediately persist with stock `write_to()` to replica-local durable FITS. No `get_coupling_matrix()` materialization.
3. `mcm_fits_verified`: persisted FITS identity/hash and structural metadata verified; workspace may then be destroyed. Restore must fail closed if FITS hash/shape/provenance differ.
4. `full_window_complete`: read-only OS-mmap-backed FITS path feeds exact full-component stock-order downstream construction; complete `[2,39,2,12288]` canonical tensor is persisted and hashed before TE selection.
5. `selected_te_complete`: canonical `<f8 [39,12288]` TE selection persisted and hashed.
6. `replica_receipt_complete`: exact receipt records all stage hashes, NaMaster/GSL lineage, checkpoint namespace and resource telemetry.

A and B use dedicated namespaces `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`; no cross-replica numerical restore is permitted.

## Memory invariants
- The persisted unbinned MCM is file-backed for downstream use; no second full MCM heap copy is allowed after workspace destruction.
- Canonical FITS conversion/streaming must remain bounded and must not materialize a second 4.5-GiB array.
- Nested BLAS/OpenMP/MKL/OpenBLAS threads remain pinned to 1 per outer worker whenever the inherited 8-core architecture is applicable.
- No scientific arithmetic, domain, threshold, binning or exact comparison rule may be changed for resource reasons.

## Frozen outcomes
`D1_DES_SCALE_RESOURCE_CHECKPOINT_DESIGN_PASS`: every exact sizing identity matches, all six stage boundaries and fail-closed restore requirements are machine-checkably present, A/B namespace isolation is explicit, and no forbidden cross-replica or historical-Wm-S3 numerical reuse is allowed.

`D2_SIZING_IDENTITY_FAIL`: any deterministic dimension/byte identity differs.

`D3_CHECKPOINT_CONTRACT_INCOMPLETE`: sizing is correct but one or more required durable stage/provenance/restore/isolation invariants are absent.

`D4_SOURCE_LINEAGE_MISMATCH`: prereg/workflow source identity mismatch.

`D5_INFRASTRUCTURE_INCOMPLETE`: gate cannot be evaluated because of infrastructure/software failure.

Only D1 permits implementation/static audit of the single self-hosted Exp073BU A/B scientific process. D1 does not itself activate home compute or create Wm_S3 scientific authority.
