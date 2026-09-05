# DSIR research log — Exp073EB terminal checkpoint provenance audit

**Date:** 2026-09-05  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Scientific accounting:** support/evidence `+0/+0`; no WW authority created.

## Chronology

1. Exp073DT attempt 4 remained queued under frozen run/job `33940588308 / 101288014666`, so no competing heavy process was allowed.
2. Independent source audit compared the frozen Exp073DT preregistration against the DQ durable driver and Exp073DT terminal classifier.
3. The audit found a prospective evidence gap: the DQ `validated_finished()` fast path verifies the terminal receipt and selected payload but does not reread all earlier checkpoint-stage manifests, while the Exp073DT artifact package does not export those manifests.
4. Because the preregistration explicitly requires all checkpoint provenance and stage-order checks, workflow SUCCESS or a PASS token alone cannot be sufficient authority evidence.
5. Exp073EB was prospectively preregistered before attempt-4 terminal output, without altering frozen arithmetic or thresholds.
6. Exp073EB event-driven support workflow was armed to run only after SUCCESS of exact upstream run `33940588308` / head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`.
7. Exp073EC hosted-only static governance audit run/job `33962004169 / 101295382699` emitted raw token `PASS_EXP073EC_EXP073EB_STATIC_GOVERNANCE_AUDIT_V0_1` and completed SUCCESS.

## Frozen Exp073EB evidence contract

For each replica A/B, independently require the exact ordered stage manifests:

`fresh_s0_mask_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete`.

Every stage must carry the exact replica, checkpoint namespace, frozen source head, contract fingerprint, complete flag, and negative historical-import/other-replica-read flags. Payloads are checked by exact SHA and shape/size semantics; the S0 map is checked by canonical `<f8` array SHA; workspace SHA must agree across workspace creation and MCM verification; selected EE SHA must agree across its stage manifest, replica receipt and terminal manifest.

No tolerance, allclose, rounding, ULP, smoothing or averaging is permitted. Exp073EB is read-only with respect to the durable science root and performs no NaMaster workspace/window computation.

## Authority boundary

Exp073EB PASS is necessary support evidence if Exp073DT reaches scientific PASS through a restore path whose full stage chain is not otherwise independently exported and verified. Exp073EB itself always remains `science_gate_scored=false`, `ww_s0_s0_authority_created=false` and cannot rescue a scientific FAIL.

## Exact next action

Keep Exp073DT attempt 4 as the sole home-runner owner. On terminal SUCCESS, consume both Exp073DT raw science artifact and Exp073EB full provenance artifact before admitting `WW_S0_S0`. On infrastructure failure, diagnose and resume from verified durable checkpoints without scientific reinterpretation.
