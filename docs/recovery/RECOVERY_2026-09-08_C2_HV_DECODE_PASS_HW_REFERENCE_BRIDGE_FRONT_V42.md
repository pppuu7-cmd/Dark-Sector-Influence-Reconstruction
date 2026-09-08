# DSIR immutable recovery V42 — Exp073HV decode PASS / Exp073HW reference bridge front

Date: 2026-09-08. Scope: **DSIR only**. RTK/RQIR excluded.

## Preserved scientific authority

All earlier DSIR scientific authority remains unchanged, including scientifically admitted `WW_S3_S3`. C2 still creates no scientific/model authority.

## Newly closed decode authority — Exp073HV

Exp073HV run `34242333899`, job `102115404956`, head `0687ca5ac973dc50340090213ceaaff70ecc6e04` completed `SUCCESS`. Raw job log and artifact were independently consumed.

Raw log exact PASS token: `PASS_EXP073HV_C2_RAW_RECORD_ABI_DECODE_V0_1`.

Boundary:

- `classification=DECODED_RECORD_SET_PLUS_0_PLUS_0`
- `raw_record_set_admitted=true`
- `decoded=true`
- `mapped=false`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

The gate verified the admitted HU/HT identities, frozen recorder/serializer blobs, little-endian 8-byte IEEE-754 binary64 ABI, finite 28×8 decoded values, and bitwise equality of every decoded packet with the producer exact-hex endpoint evidence. The canonical 28-row exact-hex JSONL SHA256 is `95c5b71d5bbbe3492f5bddccaea572644ff84823b244c3c3bc46fd18b389d552`.

Decoded artifact:

- artifact ID `10062495891`;
- name `exp073hv-c2-decoded-record-set-v0-1`;
- GitHub and independently verified ZIP digest `sha256:8ea9cf3baca04f181b97f58f19f04c798bfb14b02af271580c83e82f2900c49e`.

Durable authority file `docs/dsir4/authority/EXP073HV_C2_RAW_RECORD_ABI_DECODE_AUTHORITY_V0_1.txt` was created in commit `e49ea8d89e810cdccba7f681bf8acf6079e9b57d`, blob `36df02975587d7c1b456cee982b01210185dbda2`.

## Prospectively frozen next gate — Exp073HW reference Delta_m bridge v0.1

The next gate is derived only from pre-existing frozen C2 mapping contracts, not from result-dependent numerical tuning. Those contracts require the pressureless-matter common bridge exactly once on pre-transform native variables:

`Delta_m = delta_m + 3*a*H*theta_m/k^2`.

Exp073HW is reference-point `(alpha,beta)=(0,0)` only. It cannot create tangent derivatives, prediction readiness, G-domain mapping or scientific/model authority.

- prereg `docs/dsir4/prereg/EXP073HW_C2_REFERENCE_DELTAM_BRIDGE_V0_1.md`;
- prereg creation commit `70bd7fb5dbe43fffa10394f245ea38ca4864ee15`;
- prereg blob `017ecaa735398e8e1515003c1a8092d61f5e284a`;
- workflow `.github/workflows/exp073hw-c2-reference-deltam-bridge-v0-1.yml`;
- workflow implementation commit `ab4f764418566a39c03a002eee9e2703b76aadf5`;
- workflow blob `19ef77c74162462843c66c7350c59d354a5727d9`;
- binding/head commit `0cc263daa9dafe22fecb29aa640a034caee1db3e`;
- run `34242852819`;
- job `102117188431`;
- GitHub-hosted `ubuntu-24.04`; home/self-hosted owner none;
- state at note creation: `IN_PROGRESS`; binding and bridge-contract verification already passed, admitted decoded artifact verification executing.

Frozen HW arithmetic order is `hconf=a*H`, then `velocity_term=((3.0*hconf)*theta_m)/(k*k)`, then `Delta_m=delta_m+velocity_term`, using decoded native `k`; no tolerance, rounding, smoothing, averaging or reassociation rescue. Sampled `rho_idm_iv>0` and `rho_iv>=0` checks are node diagnostics only and cannot be promoted to the stronger required-history branch proof.

Expected token: `PASS_EXP073HW_C2_REFERENCE_DELTAM_BRIDGE_V0_1` with maximum classification `REFERENCE_DELTAM_BRIDGE_PLUS_0_PLUS_0`.

## Exact next transition

On HW terminal, inspect raw log and artifact. Only exact PASS allows durable reference-bridge authority. Even then `tangent_response_ready=false`, `prediction_ready=false`, and `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`; the next scientifically permitted branch is prospective generation/admission of the still-missing nonzero alpha/beta tangent records and matched-reference response required by the frozen C2 extraction contract.

Global frozen DSIR boundaries remain unchanged.