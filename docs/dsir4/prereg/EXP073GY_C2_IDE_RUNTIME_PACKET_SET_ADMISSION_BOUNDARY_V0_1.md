# Exp073GY — C2 IDE runtime packet-set admission boundary v0.1

Status: PROSPECTIVELY FROZEN after Exp073GX hosted support PASS. Scope: DSIR only. Scientific contribution ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Frozen upstream authority

Exp073GX hosted run `34141138190`, job `101803172545`, completed `success` on head `10da5f412f1d5a5b01f4a10e3c78bb046bab0860`. Upstream receipt schema is exactly `dsir.c2.packet_set_provenance_receipt.v0.1`; packet count 28; total record bytes 1792; coordinate order `z-major/k-minor`; solver head `ac627d54e9ce196a08878d1ba33999819925d19c`; recorder blob `c6144598b9f75908ee27a517d31eda509f7947f6`. The GX aggregate `a98f9ca1f10a9b2bfc957fac81ed837d85bbb203a5f5f0d7ff369a2061bc78b7` is synthetic fixture evidence only and MUST NOT be admitted as a runtime scientific packet set.

## Purpose

Freeze the admission boundary that a future real C2 runtime packet set must cross before any decoded field values can be inspected or any scientific mapping can be applied. This experiment does not run CLASS, does not consume self-hosted compute, and does not create scientific model authority.

## Exact runtime admission requirements

A candidate runtime packet set is admissible for later decoding only if all conditions below hold exactly:

1. A GX-valid provenance receipt is present and independently digest-verified from the canonical LF-terminated key stream.
2. `packet_count=28`, `record_bytes_total=1792`, `coordinate_order=z-major/k-minor`, and all frozen GT/GR/solver/recorder/GU identities match exactly.
3. `decoded_field_values_inspected=false` and `scientific_mapping_applied=false` at admission time.
4. The packet-set aggregate SHA256 is 64 lowercase hexadecimal characters and is NOT the frozen GX synthetic fixture aggregate.
5. Runtime producer provenance is bound exactly: GitHub run ID, job ID, commit SHA, artifact ID, artifact digest, and terminal producer status. Missing or malformed provenance is fail-closed.
6. Producer status must be terminal-success for infrastructure execution. A cancelled, skipped, queued, in-progress or infrastructure-failed producer is not scientifically interpretable.
7. No interpolation, smoothing, averaging, tolerance rescue, coordinate repair, reorder, deletion, duplication, float reformatting or post-hoc replacement is permitted between producer artifact and admission receipt.
8. Admission is a provenance/structure gate only. It does not imply a scientific PASS, does not make `prediction_ready=true`, and does not change any frozen hypothesis ID, threshold, contract or domain.

## Classification

All failures of this boundary are `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0` or `INVALID_FOR_SCIENCE +0/+0` as appropriate. They are never scientific model FAIL.

A successful hosted static audit of this boundary is only `SUPPORT_PLUS_0_PLUS_0` with `scientific_record_set_admitted=false`, `cosmological_run_started=false`, `self_hosted_science_started=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Exact PASS token for the hosted static audit: `PASS_EXP073GY_C2_IDE_RUNTIME_PACKET_SET_ADMISSION_BOUNDARY_V0_1`.

## Heavy-run exclusion

While `Exp073FW / WW_S2_S2` run `34135965569` remains active, Exp073GY MUST remain hosted/static only. It MUST NOT start a second heavy-run or a C2 cosmological extraction.
