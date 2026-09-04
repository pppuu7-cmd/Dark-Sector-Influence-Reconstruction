# Exp073DK v0.1 — Exp073BU terminal canonical-payload evidence export preregistration

Date: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.
Classification authority: support/evidence `+0/+0` only. This gate cannot create, rescue, reverse, or weaken Wm_S3 scientific authority.

## Motivation
The frozen Exp073DJ terminal evidence artifact copies terminal/replica/adapter receipts and six-stage manifests but does not copy the two canonical `selected_te.bin` payloads. The frozen science launcher itself compares those payloads with whole-file SHA256 equality and `numpy.array_equal`, but independent post-terminal verification from the Actions artifact alone therefore cannot re-run the exact comparison.

## Frozen purpose
After workflow `Exp073DJ checkpoint-preserving Exp073BU resume v0.1` becomes terminal, export the already-computed immutable canonical selected-TE payloads from the preserved historical checkpoint root without recomputation or modification.

## Fail-closed contract
1. Trigger only from completion of `Exp073DJ checkpoint-preserving Exp073BU resume v0.1`.
2. Run on the single DSIR self-hosted runner and acquire the existing DSIR home lock non-blockingly.
3. Require historical checkpoint root `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494` to exist.
4. Require `terminal_science_receipt_resume_v0_1.json` to exist. No terminal receipt means evidence export is BLOCKED/INCOMPLETE and no scientific classification is inferred.
5. Require A and B `selected_te_complete.json`, `replica_receipt.json`, and `exact_route/selected_te.bin` to exist.
6. Require each payload size exactly `39*12288*8 = 3833856` bytes, manifest shape `[39,12288]`, dtype `<f8`, semantics exactly `wins[0,:,0,:] = TE<-TE`, frozen source head `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`, contract fingerprint `b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da`, and correct A/B checkpoint namespace.
7. Recompute SHA256 of both payload files and require exact equality to their manifests and replica receipts.
8. Copy payloads read-only into a new Actions evidence artifact together with terminal receipt, selected-stage manifests, and replica receipts.
9. In the exporter itself, independently memory-map both copied `<f8 [39,12288]` payloads, compute whole-file SHA256 equality and `numpy.array_equal`, and emit a support receipt recording these exact booleans and hashes. No tolerance, rounding, smoothing, averaging, or numerical transformation is permitted.
10. The exporter never writes to the historical checkpoint root and never runs the production driver, NaMaster, downstream MCM calculation, mask reconstruction, workspace calculation, or any scientific arithmetic beyond byte/hash and exact-array equality of already-final payloads.

## Interpretation
- `EVIDENCE_EXPORT_PASS` means a later repository/automation iteration can independently verify the frozen terminal science receipt against the actual canonical A/B payload bytes.
- Payload inequality is not reclassified here; it is simply recorded exactly. Scientific PASS/FAIL remains the frozen Exp073BU terminal gate's authority after independent reconciliation.
- Missing/malformed/mismatched evidence is infrastructure/BLOCKED `+0/+0` and never a scientific FAIL.

## Anti-duplication
This is a deterministic post-terminal evidence successor, not a competing scientific control plane. It must not start before Exp073DJ completes and must not coexist with any other self-hosted DSIR job. It performs no heavy computation.
