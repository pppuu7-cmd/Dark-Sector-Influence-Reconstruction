# DSIR immutable recovery — Exp073BU science activation hosted audit v0.3 PASS

Date: 2026-09-04. Scope: DSIR only; RTK/RQIR excluded.

Authoritative hosted audit:

- run/job `33885745268 / 101064948626`;
- source head `c0d780adb691ee478f986e4e9d7e50aa78cd956d`;
- artifact `9941744878`;
- artifact digest `sha256:284b98eb6476b17c77aa27a2753f971e2269128778e41b86bb7758ddb6c8e48f`.

PASS_EXP073BU_SCIENCE_ACTIVATION_HOSTED_AUDIT_V0_3

science_workflow_blob=b95346a1c8243074a1ca49878919847b675a9269
activation_prereg_blob=022e203d1cb966680e3eaff7fae39cb2234ebd5a
original_science_prereg_blob=816542c7eb7a8ba4e72d6e01228aa62d05c7c805
production_driver_blob=5c8d5d3463e455389a1ca3df2639bf06a3b7b603
fresh_helper_blob=73ef04c479547dc8e2e89c9f511f1a55fae3ed64
exact_adapter_blob=dafe86086a470c852106f0d4ecccbda1d389e397
component_blobs_blob=0d6d6e882d1a4cf1ff79fbe8227a4f2b460c7e40
downstream_blob=acafb095deafae7602101d8305e239341010ba79
science_launcher_blob=1a54ad89d32dd217443bc3062a6215bf10e8b17d
cx_v0_4_a1_recovery_blob=43b658028f74b7a0b52fca8261beeb58026d8ffc

All hosted audit steps completed success: exact immutable blob binding, unique path-scoped push activation, one self-hosted Linux/X64 successor job behind hosted preflight, and preservation of exact Wm_S3 A/B science semantics and terminal vocabulary.

The only change relative to activation shell v0.2 is the prospectively frozen activation mechanism: because the connected GitHub tool exposes repository writes but no new-workflow `workflow_dispatch` action, the explicitly user-authorized launch is represented by a unique push to `control/activate_exp073bu_wm_s3_science_v0_3.txt`. No schedule or broad push trigger exists.

Classification: hosted support/activation audit only, accounting `+0/+0`. No DES-scale Wm_S3 numerical science was executed and no Wm_S3 authority was created by this audit.

The v0.1 validation-level failure and the v0.3 audit's first validation-level attempt remain immutable infrastructure history and are not scientific results. The permitted successor is one fresh activation commit after a clean Actions noncompetition check, followed by the run-local hosted preflight and exactly one self-hosted Exp073BU A-then-B process.
