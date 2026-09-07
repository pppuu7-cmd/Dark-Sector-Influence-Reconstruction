# DSIR immutable recovery — C2 Exp073GR/GS support PASS while Exp073FW remains active V10

Date: 2026-09-07. Scope: DSIR only; RTK/RQIR excluded.

All previously admitted Wm/WW authority is preserved. `WW_S2_S2` remains NOT ADMITTED. Exp073FW run `34125785882`, home job `101754061309`, remains the single authoritative self-hosted process and was still `IN_PROGRESS` in the frozen `WW_S2_S2` A/B gate at reconciliation. No competing self-hosted run was launched and no partial numerical output was inspected.

## Exp073GR — runtime sampling/provenance contract

Prospective prereg commit: `6cf8a72344a9ea2dfc3877bd1ad46a6331d17d30`.
Machine-readable contract commit: `6fc88c48beb383fb780b23f154c05f8c993e9bb7`.
Hosted workflow commit: `c14861348eca675fa17fd26212509b765ce3fd31`.

Run `34130804754`, hosted job `101770188173`, completed SUCCESS and was independently raw-log inspected. The raw log emitted:

- `canonical_contract_sha256=6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b`;
- `request_count=28`;
- `ordered_unique_pairs=true`;
- `recorder_blob_verified=true`;
- `record_bytes=64`;
- `record_field_count=8`;
- `all_requested_nodes_inside_frozen_support=true`;
- `forbidden_rounded_k_excluded=true`;
- `prohibited_transformations_all_false=true`;
- `classification=SUPPORT_PLUS_0_PLUS_0`;
- exact token `PASS_EXP073GR_C2_IDE_RUNTIME_SAMPLING_PROVENANCE_CONTRACT_V0_1`.

Frozen identities include solver `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`, recorder blob `c6144598b9f75908ee27a517d31eda509f7947f6`, exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, exact k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`, ordering `z_major_k_minor`, exactly 28 Cartesian requests, and all interpolation/extrapolation/smoothing/averaging/tolerance/nearest/rounding/effective-coordinate/fiducial-P rescue flags false.

GR creates no scientific authority: `cosmological_run_started=false`, `self_hosted_science_started=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Exp073GS — deterministic runtime request emitter

Prospective prereg commit: `f72ed7dd8cfc1190981029b06d3ea0eb58be9b6d`.
Emitter fixture commit: `d4ce2e4a30c7e4c061b8b6d2158e661493d66b84`.
Hosted workflow commit: `7be2be010b153e6850b7ae4aeff285bb71a4f3a8`.

Run `34130948407`, hosted job `101770660311`, completed SUCCESS and was independently raw-log inspected. The raw log proved:

- exact request count 28;
- exact ordinals `0..27`;
- exact z-major/k-minor ordering;
- exact contract fingerprint binding to `6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b`;
- mutated contract fails closed before any request emission;
- provenance manifest bound to solver head and recorder blob;
- manifest SHA256 `1448d6d6ac3ef2a018af3df9b732a91d4006263bc2fb8b7d232e1eded87316b0`;
- all prohibited-transformation flags remain false;
- `classification=SUPPORT_PLUS_0_PLUS_0`;
- exact token `PASS_EXP073GS_C2_IDE_RUNTIME_REQUEST_EMITTER_AUDIT_V0_1`.

GS likewise creates no scientific authority and launches no solver or self-hosted science.

## Current heavy authority and next actions

Authoritative heavy workflow remains Exp073FW run `34125785882`, head `1c635f5192d26e76e0ec82a308363b666e5a248b`; hosted audit job `101754018941` SUCCESS with `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_5`; home job `101754061309` IN_PROGRESS on `DSIR-HOME-PC-2`; checkpoint namespace `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`.

Exact heavy next action: terminal-consume FW, inspect raw final logs and artifact, verify GitHub artifact digest/ZIP, complete checkpoint/provenance chain, frozen S2->S2 same-field semantics, exact `19,327,352,832`-byte file-backed proof, canonical finite `<f8 [39,12288] EE<-EE`, and exact A/B equality. Workflow success alone is not scientific PASS. Only separately frozen Exp073FX may create `WW_S2_S2` authority.

Exact independent C2 next action permitted by GS PASS: prospectively freeze a hosted-only dry-run record-envelope assembly gate that binds each of the 28 deterministic requests to the validated 64-byte recorder ABI without running CLASS or generating a cosmological prediction. No real C2 extraction may start while FW owns the home runner.
