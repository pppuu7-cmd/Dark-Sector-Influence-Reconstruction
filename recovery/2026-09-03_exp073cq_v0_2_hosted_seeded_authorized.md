# Exp073CQ v0.2 hosted-seeded authorization — 2026-09-03

DSIR only. Repository/actions/checkpoints are authority. Article-3 delta `+0/+0`.

Historical Exp073CQ v0.1 run `33742582807` / home job `100607697336` terminated before durable parent import; it remains `INFRASTRUCTURE_OR_SOFTWARE_INCOMPLETE_AT_PARENT_IMPORT`, not science/resource FAIL. Clean hosted reproducer `33752333426` / `100638517360` PASSed the exact frozen v0.1 import logic.

Prospective v0.2 authority:
- prereg `71800bedbf8c23d7aee4538a0230bdac4bd5c6f3`;
- driver `0bf7ea195bccbb8e6458f1269640c279668d4a1f`;
- home workflow `31c57d7b3565aea7c6ff3edbdf978f51f652abcb`;
- binding `f25cdc25c9e2d4a0f6d1ec673922cda9ca3019fc`;
- sync `c20127b6762c6fc9b21875a321aecd7a4cd5f88e`;
- namespace `checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-2`.

Hosted seed run `33752529085`, job `100639147404` PASSed with token `PASS_EXP073CQ_V0_2_HOSTED_PARENT_IMPORT_SEED`, producing exact durable seed head `4f528424a2d2b3e32aeb4a68d73265ef9de8bd4e`, fingerprint `87b58bf120510bec50b21851d7ff21269689db6dcdd906cb3a14102e4a4f5f97`, exact imported bands 0..28 and no 29..38. Artifact `9892102247`, digest `sha256:8af123e1102f17feae01050c456983e8547306c9f59b4a72f64ccb917b55a2ae`.

Post-seed hosted audit run `33752695840`, job `100639693792` PASSed with token `PASS_EXP073CQ_V0_2_HOSTED_SEED_STATIC_AUDIT`; artifact `9892171765`, digest `sha256:8e9acc8142bf5bc1a441259d6884d2dc54cda8a5690a64cdef81525479c7d68b`. Audit exact-restored seed, validated all imported receipts, missing allowlist 29..38, 8-worker/nested=1 contract, and proved home workflow contains no direct Exp073CP import.

Activation commit `fabb0c601edcb117d7734ba1828da762b585c2db`. Immediately before launch Actions showed zero queued and zero in_progress runs. Single launch commit `011852feb6d40152f4b33bde732b00520cd28f79` created run `33752799918`; authorize job `100640020607` SUCCESS and home job `100640079011` QUEUED at record creation.

While queued/in_progress DSIR-HOME-PC belongs exclusively to run `33752799918` / job `100640079011`. Home must restore seed `4f528424...` first and may compute only bands 29..38. Frozen resource PASS token is `PASS_EXP073CQ_V0_2_WM_S3_MISSING29_38_8WORKER_HOSTED_SEEDED_RESOURCE`.
