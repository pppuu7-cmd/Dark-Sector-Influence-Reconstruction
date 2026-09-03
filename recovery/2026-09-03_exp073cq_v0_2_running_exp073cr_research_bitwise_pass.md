# 2026-09-03 — Exp073CQ v0.2 running checkpoint / Exp073CR research-only regression

DSIR only. This note does not change any frozen scientific/resource criterion and carries Article-3 delta `+0/+0`.

## Authoritative active process

Exp073CQ v0.2 remains the sole live authoritative home process:
- workflow run `33752799918`;
- authorize job `100640020607` SUCCESS;
- self-hosted job `100640079011` IN_PROGRESS;
- workflow/head `011852feb6d40152f4b33bde732b00520cd28f79`;
- checkpoint namespace `checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-2`;
- frozen contract fingerprint `87b58bf120510bec50b21851d7ff21269689db6dcdd906cb3a14102e4a4f5f97`;
- exact read-only seed bands `0..28`; compute allowlist exactly `29..38`;
- latest observed durable head `ad9d79d0b32a6a097669966c8b94b7424521c34e`, commit `checkpoint: band-31-complete`.

The band-31 receipt at that head records `complete=true`, canonical `<f8 [12288]`, `outer_workers=8`, `nested_threads=1`, the frozen contract fingerprint, and payload SHA256 `8fa0d8833867150b49fb34b39e13c491f3425eac9419205fa73412cf1d6af715`. This is checkpoint/provenance evidence only; no partial numerical output is interpreted and no gate is tuned.

No queued DSIR Action existed at the observation point; the sole in-progress run was Exp073CQ v0.2. Home ownership remains exclusive to run/job `33752799918` / `100640079011`.

## Reconciled independent Exp073CR result

A separate research branch produced hosted run `33754644074`, job `100646005106`, head `b67b87168e009a263c91d52c529fb459879b8a00`. Its trigger explicitly states:
- `NON_AUTHORITATIVE_RESEARCH_TRIGGER`;
- scientific credit `+0/+0`;
- resource authority `none`;
- no home runner;
- does not modify Exp073CQ v0.2.

Raw hosted logs reported exact `array_equal=true` and `sha_equal=true` under two ll3 partitions for immutable Exp073CP complete bands 0, 7 and 15, with tokens `PASS_EXP073CR_RESEARCH_LL3_BITWISE_REGRESSION_V0_0` and `PASS_EXP073CR_HOSTED_LL3_BITWISE_REGRESSION_V0_1`. Artifact ID `9892971697`, archive digest `sha256:766184eb42ef696e3c493d55ebb78cbc6c4fab83baf7c0d17bbdb7b3cf104a72`.

Classification: useful implementation/invariance evidence, but strictly research-only `+0/+0`. It does not supersede, rescue, tune, or authorize Exp073CQ and creates no Wm_S3 scientific authority.

## Next action

Do not duplicate the home job. When `100640079011` becomes terminal, consume its raw final receipt/artifact/checkpoint state against the prospectively frozen Exp073CQ v0.2 contract. Only the exact resource PASS token `PASS_EXP073CQ_V0_2_WM_S3_MISSING29_38_8WORKER_HOSTED_SEEDED_RESOURCE`, together with validated durable bands, exact first-8 equality, swap safety and frozen CPU gate, may permit preregistration of the fresh-independent-PCL Wm_S3 A/B scientific successor.
