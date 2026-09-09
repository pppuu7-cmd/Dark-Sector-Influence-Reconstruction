# Exp073IM angular-byte authority materialization audit v0.1

Date: 2026-09-09. Scope: DSIR Article 3 only.

Status: SUPPORT / EXACT INPUT MATERIALIZATION PASS. This does not alter `G_ORDERED_JOIN=PASS`, does not score `G_RADIAL_SUPPORT`, and does not inspect any Exp073IM real radial output.

## Purpose

Before implementing the preregistered real radial executor `EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_1`, determine whether every one of the 14 structurally admitted ordered slots has a uniquely materializable immutable numerical angular object (artifact + canonical array identity) suitable for direct machine consumption.

## WW block — 10/10 materializable

The admitted receipt `docs/dsir4/authority/C2_WW_ANGULAR_AUTHORITY_RECEIPT_V0_3.json` provides all ten required WW pair authorities with exact:

- pair identity;
- relation type;
- admission experiment/token;
- run/job/head;
- source artifact ID;
- source artifact ZIP digest;
- canonical `<f8 [39,12288]` array SHA256.

Thus the WW block is fully materializable for Exp073IM without recomputation or authority selection.

## Wm block — 4/4 materializable

### Wm_S1

Exp073BJ is exact Track-A authority. Recovery record binds:

- run `33379013167`;
- final immutable authority artifact `9758841785`;
- digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`;
- final canonical window SHA256 `1a2be04c40ef434a05edb9d9cb878b718ba906949fe0736ab5ad9e90c90266e3`;
- exact Wm `TE<-TE`, canonical 39x12288 semantics.

Status: MATERIALIZABLE.

### Wm_S2

Exp073CI v0.2 is admitted complete repeatable Track-A authority. Record binds:

- run `33646799130`;
- exact comparator job `100304043991`;
- authority artifact `9853165664`;
- artifact digest `sha256:fcfccb6768948ffe34d28e9ed32da64d3b1d071704028fe6f312c1ab8b440f57`;
- deterministic final window SHA256 `96248e7699a5a12945854db2c9af150affcfe13f4f9dc0bfcbb87b99f92ff087`;
- canonical `<f8 [39,12288]`, Wm `TE<-TE` semantics.

Status: MATERIALIZABLE.

### Wm_S3

Exp073DJ/BU exact authority is admitted. Record binds:

- run `33910213781`;
- hosted job `101144603730`, self-hosted job `101144660519`;
- artifact `9959064322`;
- artifact digest `sha256:4c9cbebdf4be2e901943a738ebb7df9c1040a6d9524bdd359feb3d3331a647c9`;
- A/B selected-TE canonical SHA256 `d282ebdf98dc04e41a8c85f487e209634a8324ce7677107112b8abfd1660f749`;
- exact array equality and no tolerance rescue.

Status: MATERIALIZABLE.

### Wm_S0 — authority succession resolved by Exp073IN

The earlier audit correctly preserved two exact-route identities and refused an ad-hoc numerical choice:

- historical primary-P Wm_S0 canonical SHA256: `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`;
- controlled single-thread Exp073AI/AM canonical SHA256: `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`;
- Exp073AN preserved `DETERMINISTIC_SINGLE_THREAD_ROUTE_BUT_EXACT_AUTHORITY_SHIFT_FROM_PRIMARY_P` and explicitly did not select a new canonical production authority.

The prospectively frozen `EXP073IN_C2_WM_S0_AUTHORITY_SUCCESSION_V0_1` protocol resolves succession from provenance only: absent an explicit admissible supersession event, historical primary-P remains production authority by continuity. No downstream radial/physical/covariance/nuisance/model information and no tolerance/ULP/rounding rule enters the decision.

Current materialization evidence binds primary-P to original Exp073X2 run `33300997298`, head `2403d9680e1d08a3853084034eb2878faa52b4e0`, with two still-unexpired immutable replica artifacts:

- replica A artifact `9730411514`, digest `sha256:34530157cddf594c93728d5e092ab937d16a653665623f00513f4fd58df17555`;
- replica B artifact `9730409129`, digest `sha256:36358663fb1980ad75cb71f7ca7149d06d357cf7de8b29feca4273f4f88c89e5`;
- both expire no earlier than `2026-11-28T08:12:01Z` under current GitHub metadata.

The previously frozen Exp073X2R repair workflow downloaded those exact artifact IDs/names, and the unchanged comparator loaded `exp073x2_replica_a_v0_1.npz` / `exp073x2_replica_b_v0_1.npz`, canonicalized `wm0_te_window` as `<f8 [39,12288]`, verified exact hash equality and `numpy.array_equal(A,B)==True`, producing canonical SHA `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.

Durable decision receipt: `docs/dsir4/authority/EXP073IN_C2_WM_S0_AUTHORITY_SUCCESSION_V0_1.json`.

Classification: `PASS_EXP073IN_C2_WM_S0_AUTHORITY_SUCCESSION_V0_1`.

Status: MATERIALIZABLE.

## Overall materialization result

- WW: `10/10` exact byte authorities available;
- Wm: `4/4` uniquely materializable;
- total: `14/14` uniquely materializable;
- `Exp073IM` preregistration remains valid;
- the sole prior Wm_S0 materialization blocker is closed;
- real Exp073IM execution is now authorized with respect to angular-byte authority/materialization only.

## Downstream boundary

This audit closure does **not** itself score `G_RADIAL_SUPPORT`, does not alter `G_ORDERED_JOIN=PASS`, and does not create a scientific model PASS. The next admissible step is to implement/launch the already-preregistered Exp073IM real radial executor using exactly these 14 admitted authorities and then classify its output under the frozen radial-support rule.
