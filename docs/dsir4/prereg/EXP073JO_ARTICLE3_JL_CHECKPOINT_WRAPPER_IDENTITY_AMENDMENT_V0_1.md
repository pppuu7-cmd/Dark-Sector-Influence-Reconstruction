# Exp073JO — tested-wrapper identity binding amendment v0.1

Date frozen: 2026-09-10. Scope: DSIR Article III / process provenance only.

Status: FROZEN WHILE THE FIRST EXP073JO PREFLIGHT IS STILL RUNNING, BEFORE ITS RESULT IS KNOWN AND BEFORE ANY JO HEAVY RECOVERY IS ACTIVATED.

The JO preflight was launched from head `374184d1b2e9f31628ab930bc271951569ce2bf9`. At that head, the tested recovery wrapper `ci/exp073jo_article3_jl_durable_response_checkpoint_recovery_v0_1.py` has Git blob SHA `aa4c544c1e3e81137010fcdbd34f20567e1eb894`.

A durable JO preflight PASS authority is admissible only if it records both this exact preflight head SHA and this exact wrapper blob SHA. Before any recovered JL computation, the active main checkout MUST prove that `git hash-object ci/exp073jo_article3_jl_durable_response_checkpoint_recovery_v0_1.py` equals `aa4c544c1e3e81137010fcdbd34f20567e1eb894`.

If the wrapper changes after the tested preflight head, the previous preflight may remain historical +0/+0 evidence but cannot authorize heavy recovery; the changed wrapper requires a new exact-build JO preflight. Documentation/recovery/workflow changes that do not alter the wrapper do not invalidate the tested wrapper identity.

This is a process-provenance guard only. It changes no scientific arithmetic, JL grid, response definition, masks, domain, h, tolerance, result classification, or downstream authorization.
