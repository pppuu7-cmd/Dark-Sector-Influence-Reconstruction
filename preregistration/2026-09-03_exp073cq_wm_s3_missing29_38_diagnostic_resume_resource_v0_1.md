# Exp073CQ — Wm_S3 missing-bands 29..38 diagnostic-resume resource qualification v0.1

Date: 2026-09-03
Status: PROSPECTIVELY FROZEN; HOME EXECUTION FORBIDDEN UNTIL POST-IMPLEMENTATION HOSTED STATIC AUDIT PASS AND ACTIVATION AUTHORITY

## Motivation and immutable historical boundary
Exp073CP v0.1 run `33726577654` is immutable infrastructure/software incomplete `+0/+0`: its home job `100556826993` failed inside the full39 compute step after durable admission through band 28; frozen final classification did not run and no authority artifact exists. GitHub's decoded immutable job log remains unavailable (`BlobNotFound`), so the lower-level first causal exception is unknown and MUST NOT be invented.

Valid checkpoint authority is parent namespace `checkpoints/exp073cp-wm-s3-full39-resource-v0-1` at exact head `025629d9bb7b113bd0548ff6a32c6ee5812ae245`. It contains exact complete payload+receipt pairs for every band `0..28`; bands `29..38` are absent. Exp073CQ is a new resource/checkpoint/diagnostic continuation. It may import and rebind already-verified payloads but MUST NOT numerically recompute bands `0..28`.

## Frozen scientific arithmetic and resource criteria
Exactly unchanged from Exp073CP where applicable:
- task `Wm_S3`, source bin 3, signature `(0,2,0,2)`;
- DES `NSIDE=4096`, ell `0..12287`, `L=12288`, all 39 frozen bands;
- Wm `TE <- TE`, canonical little-endian `<f8`;
- immutable PCL SHA256 `ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d`;
- immutable reference bands `[0,8)` SHA256 `36ee9fca9fb276a30d8ebb97cb04fddc7e95cff18fb29248c033bb364ea2d8cf`;
- exact `np.array_equal` plus exact canonical SHA only, no tolerance/ULP/rounding/smoothing/averaging rescue;
- exactly 8 outer worker processes when numerical work is active, nested BLAS/OpenMP/MKL/OpenBLAS/BLIS/NUMEXPR threads pinned to 1;
- dynamic complete-band scheduling; only missing bands `29..38` may be submitted;
- resource PASS still requires exact first-8 equivalence, zero positive swap increase, and `cpu_fraction_of_8_compute >= 0.90` under the prospectively defined resumed numerical segment. No post-hoc interval selection.

Because only ten bands remain, the resumed CPU metric is prospectively defined on exactly the newly computed missing-band numerical segment: earliest numerical worker start among bands 29..38 to latest numerical worker end among bands 29..38, with `effective_cores=sum(worker numerical CPU seconds)/active_span`, then `/8`. Imported parent bands never contribute CPU time and cannot inflate or dilute this metric.

## Parent checkpoint import and new durable namespace
Parent checkpoint is immutable and read-only:
- namespace: `checkpoints/exp073cp-wm-s3-full39-resource-v0-1`
- exact parent head: `025629d9bb7b113bd0548ff6a32c6ee5812ae245`
- expected parent experiment: `Exp073CP`
- required complete bands: exactly `0..28`
- required missing bands: exactly `29..38`.

Dedicated successor namespace: `checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-1`.

Before any numerical submission the successor MUST:
1. restore the parent at the exact frozen head;
2. verify parent contract fingerprint integrity, upstream PCL/reference canonical shape/dtype/SHA, and every band 0..28 payload/receipt SHA, band identity, ell interval and parent contract fingerprint;
3. fail closed if any parent band 29..38 unexpectedly exists at the frozen parent head or any required 0..28 unit is absent/corrupt;
4. create a new successor contract/fingerprint binding source head, prereg, driver, workflow, binding, sync implementation, frozen parent namespace/head/fingerprint, science/resource parameters and exact missing allowlist;
5. import bytes for upstream and bands 0..28 into the new namespace WITHOUT numerical recomputation, writing successor receipts that include exact parent payload SHA, parent receipt SHA/provenance and successor contract fingerprint;
6. exact-validate the imported successor state and durably push it before compute.

Resume logic MUST submit numerical workers for `29..38` only. Each newly completed band is canonicalized, SHA-verified, receipt-written and durably pushed to the successor namespace immediately at a complete-band boundary. Restarts restore the successor first, verify it exactly, and submit only still-missing members of the frozen allowlist. No fabricated intra-band progress.

## Prospective fail-closed durable diagnostic capture
Because the historical GitHub log blob is unavailable, Exp073CQ must capture the first local causal exception prospectively without weakening any gate. On any exception in restore/import/worker-result/materialization/checkpoint-sync/telemetry/finalization control paths, write a canonical diagnostic JSON containing at least: experiment/version, stage, exception type, exact exception string, bounded traceback text, source head, driver/workflow/binding lineage, successor contract fingerprint when available, parent checkpoint head, newly admitted bands, still-missing allowlist and timestamp. Best-effort durable diagnostic sync is allowed only to the successor namespace and MUST NOT mark an unfinished numerical band complete. The original failure remains failure even if diagnostic transport itself also fails; unknown/corrupt transport fails closed.

## PASS and negative classifications
Frozen PASS token: `PASS_EXP073CQ_WM_S3_MISSING29_38_8WORKER_DIAGNOSTIC_RESUME_RESOURCE_V0_1`.

Mandatory PASS:
- parent import exactly verifies all bands 0..28 and never recomputes them;
- all new bands 29..38 complete and are durably exact-valid;
- canonical reassembly contains all 39 exact-valid rows;
- first8 exactly equals frozen reference and SHA equals `36ee9fca9fb276a30d8ebb97cb04fddc7e95cff18fb29248c033bb364ea2d8cf`;
- resumed compute `cpu_fraction_of_8_compute >= 0.90`;
- swap increase during resumed numerical segment is `0 KiB`;
- final telemetry and final receipt are durably checkpointed.

Exact mismatch => numerical/resource FAIL; positive swap => resource FAIL; CPU fraction below 0.90 => resource/performance FAIL. Restore/import/worker/software/transport/diagnostic-control failure before frozen final comparator => infrastructure/software/checkpoint incomplete. All Exp073CQ outcomes are Article-3 `+0/+0`; this experiment cannot itself create Wm_S3 angular scientific authority.

## Authorization order
1. this preregistration commit;
2. implement new successor driver/workflow and immutable binding without mutating Exp073CP;
3. implement hosted static/regression audit over the final files, including an explicit proof-by-inspection that worker submission is restricted to 29..38 and parent 0..28 are import-only;
4. hosted audit must PASS after all implementation files are frozen;
5. create activation authority containing exact audit run/job/artifact or raw-log provenance;
6. immediately before home launch verify zero competing queued/in-progress DSIR Actions;
7. launch exactly one Exp073CQ continuation.

Full fresh-independent-PCL Wm_S3 A/B scientific production remains forbidden until a prospectively frozen resource gate actually PASSes.