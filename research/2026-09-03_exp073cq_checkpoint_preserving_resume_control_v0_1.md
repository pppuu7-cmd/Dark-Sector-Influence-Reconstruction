# DSIR research/control note — Exp073CQ checkpoint-preserving resume v0.1

Date: 2026-09-03  
Scope: infrastructure/resource-control research only; nonclassifying `+0/+0`; no readiness change and no Wm_S3 scientific authority.

Exp073CP stopped after exact durable admission through band 28, while the lower-level causal exception remains unavailable from GitHub's immutable decoded job-log endpoint. The scientifically neutral continuation principle is therefore to separate *payload authority* from *failed process authority*: complete band payloads with valid receipts remain reusable even when their producing process later fails, while absent bands and absent final telemetry remain unclassified.

Exp073CQ freezes this principle operationally. Parent head `025629d9bb7b113bd0548ff6a32c6ee5812ae245` is read-only; bands 0..28 are verified and imported byte-for-byte into a new contract namespace, and only bands 29..38 are eligible for numerical submission. New receipts bind the parent payload SHA, parent receipt-file SHA, frozen parent contract fingerprint/head and the successor contract fingerprint. Thus resumption changes checkpoint/control provenance but not the numerical definition of any completed band.

The new version also freezes prospective causal-diagnostic capture. An exception record may be durably synchronized, but diagnostic durability cannot mark an unfinished numerical unit complete and cannot convert a failed attempt to PASS. This makes an otherwise externally unavailable process exception recoverable without weakening exact numerical/resource acceptance criteria.

The hosted static audit run `33742223874`, job `100606527087`, raw token `PASS_EXP073CQ_STATIC_PARENT_IMPORT_DIAGNOSTIC_RESUME_AUDIT_V0_1`, verified the exact parent tree, import/compute partition and successor control architecture before home execution. This note records the design rationale only. Exp073CQ remains `+0/+0` regardless of outcome; only its prospectively frozen resource token can authorize the later fresh-independent-PCL Wm_S3 A/B preregistration.
