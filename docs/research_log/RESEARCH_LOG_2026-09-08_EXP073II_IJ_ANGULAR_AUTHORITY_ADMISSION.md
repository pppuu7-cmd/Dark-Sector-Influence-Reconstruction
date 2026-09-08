# Exp073II / Exp073IJ angular-authority admission chain — 2026-09-08

Scope: DSIR only. RTK/RQIR excluded.

## Exp073II inventory
Exp073II run `34252435914`, job `102149881007` terminated SUCCESS and raw log emitted `PASS_EXP073II_C2_WW_ANGULAR_AUTHORITY_INVENTORY_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`. Artifact `10066507621` had GitHub digest `sha256:b5ec1ee01e5bdcb7fcb08190ce773634140f3201e9f9f310afb434869e1d04cb`, independently reproduced from downloaded ZIP. II located repository evidence for the complete ten-pair WW set but created no angular authority.

## Candidate-receipt audit and corrections
A prospective candidate receipt was fail-closed audited against all ten historical frozen source artifacts. Every GitHub ZIP digest matched exactly and the two A/B canonical `selected_ee.bin` payloads within every pair were SHA-identical. Two candidate-local metadata transcription errors were found and corrected without changing historical authority:
- `S1_S1` canonical SHA256 is `ff72ba2229729fc4fb832b31a2e06ec92e746e336af515ffa5d335c14fb03b5c`;
- `S2_S3` canonical SHA256 is `3a787a12152ec023b6747145ec96345bc805ab0c96b5a26d0b528a9d68672de2`.
The resulting frozen candidate receipt is `docs/dsir4/authority/C2_WW_ANGULAR_AUTHORITY_RECEIPT_V0_3.json`, commit `9d2b47394b11212d4df378e8e59dd1d09cc19301`, blob `681503a7ac8376801e997f0e2e4ba2ebdace87da`.

## Exp073IJ infrastructure/self-healing chronology
All failed attempts below are infrastructure/provenance-presentation failures `+0/+0`; none is a scientific angular FAIL and no acceptance criterion was relaxed.
- `34253819439 / 102154447268` and `34253868968 / 102154619161`: GitHub job-log redirect transport returned HTTP 401 through Python urllib before pair scoring. Repair: redirected log transport via fail-closed `curl -fsSL` regression.
- `34254038921 / 102155204873`: old S0_S3 admission log did not print the canonical SHA literal even though its frozen artifact contained the validated payload. Repair: recompute canonical SHA directly from the exact historical source artifact.
- `34254167824 / 102155650677`: direct artifact hashing exposed the S1_S1 candidate receipt transcription error, motivating the complete ten-artifact audit and v0.3 receipt.
- `34254580746 / 102157028926`: authority-created marker differed only in JSON/shell formatting. Repair: exact regex accepting only true-valued admitted marker syntax.
- `34254684214 / 102157376508`: verifier incorrectly required MCM proof to reside inside source ZIP JSON rather than the admitted provenance evidence union. Repair: preserve exact MCM criterion while reading its proof from admitted raw log or frozen artifact receipt.
- `34254767799 / 102157659247`: old FR admission raw log did not print literal `19327352832`; historical FR verifier blob `127beca2392e6b093d08330828a764a3108b646b` independently requires `mcm_backing_bytes==19327352832`, `mcm_filebacked is True`, public `[4,39,4,12288]`, selected `EE<-EE [39,12288]`, and no tolerance rescue. Final verifier therefore binds exact evidence from raw admission plus frozen artifact, never from workflow success alone.

## Final Exp073IJ scientific result
Prospective gate: `docs/dsir4/prereg/EXP073IJ_C2_WW_ANGULAR_AUTHORITY_ADMISSION_V0_2.md`, blob `119369e38465f101b2ff04dafd1fe933beeacaf7`.
Final repair/head commit: `fea645fc591863665f249ba4b74767f0f2d2b8bc`.
Run `34255057685`, job `102158621226` terminated SUCCESS. Raw log contains one exact `BOUND` line for each of the ten required pairs and then:
- `PASS_EXP073IJ_C2_G_ANGULAR_AUTHORITY_V0_2`
- `classification=SCIENTIFIC_GATE_PASS`
- `G_DOMAIN_MAPPING=PASS`
- `G_ANGULAR_AUTHORITY=PASS`
- `angular_authority_receipt_created=true`
- `scientific_model_authority_created=false`
- `overall_status=NOT_YET_TESTABLE`.

The admitted durable receipt is `docs/dsir4/authority/C2_WW_ANGULAR_AUTHORITY_ADMITTED_V0_1.json`, creation commit `9f7c5d9367e3efee97e89106797547e4e6d4d163`.

## Scientific boundary after IJ
C2 has exactly the first two mandatory funnel gates PASS: `G_DOMAIN_MAPPING`, `G_ANGULAR_AUTHORITY`. `G_ORDERED_JOIN` and all later gates remain `NOT_YET_TESTABLE`; no complete model authority exists. No tolerance, rounding, smoothing, averaging, effective-coordinate, fiducial-P, source-pair substitution, or home recomputation was used.
