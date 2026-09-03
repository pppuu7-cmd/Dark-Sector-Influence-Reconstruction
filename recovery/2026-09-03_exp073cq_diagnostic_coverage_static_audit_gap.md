# Exp073CQ diagnostic-coverage static-audit gap

Date: 2026-09-03
Status: LIVE GOVERNANCE / CONTROL AUDIT FINDING; +0/+0

This note does NOT modify the frozen Exp073CQ implementation, launch, thresholds, numerical arithmetic, checkpoint authority, or current run `33742582807`. The active run must not be patched in place.

## Finding

Exp073CQ preregistration requires prospective canonical diagnostic capture for exceptions in restore/import/worker-result/materialization/checkpoint-sync/telemetry/finalization control paths.

The frozen Python driver `ci/exp073cq_wm_s3_missing29_38_diagnostic_resume_resource_v0_1.py` implements `diagnostic(...)` and correctly invokes it for:

- Python-command exceptions caught by `main()` for `init`, `import-parent`, `validate`, and `finalize`;
- exceptions inside `compute`, including worker-result handling and the Python `sync(...)` calls used for complete numerical-band durability.

However the frozen home workflow `.github/workflows/exp073cq-wm-s3-missing29-38-diagnostic-resume-resource-v0-1.yml` also performs several prereg-relevant operations directly in shell under `set -euo pipefail`, outside the driver's diagnostic wrapper:

1. successor checkpoint `restore` before Python `init`;
2. immutable Exp073CP parent checkpoint `restore` before Python `import-parent`;
3. successor checkpoint `push` labelled `imported-parent-band00-28`;
4. helper compilation/materialization shell path;
5. successor checkpoint `push` labelled `compiled-helper`;
6. final successor checkpoint `push` labelled `frozen-final` after Python finalization.

A nonzero exit from one of these shell operations stops the step before `diagnostic(...)` can create or durably push `diagnostics/first_failure.json`.

Therefore the implementation does NOT fully guarantee the preregistered statement that any restore/checkpoint-sync/materialization control-path exception receives canonical diagnostic capture.

## Why hosted audit missed it

Hosted static/regression audit run `33742223874` is historically immutable and did PASS with token `PASS_EXP073CQ_STATIC_PARENT_IMPORT_DIAGNOSTIC_RESUME_AUDIT_V0_1`.

Inspection of the frozen audit workflow shows that it asserts diagnostic-related strings such as `diagnostic-first-failure` and `still_missing_allowlist` exist in the Python driver, and asserts that restore/checkpoint labels exist in the workflow. It does NOT prove that every shell-level restore/push/materialization failure is routed through the Python diagnostic mechanism or an equivalent shell trap.

The historical PASS token remains an immutable fact, but it must no longer be described as proving complete exception-path diagnostic coverage.

## Interpretation of the live CQ run

No terminal CQ classification is changed by this note.

- If a vulnerable shell restore/push/materialization path fails, the run is infrastructure/control incomplete `+0/+0`; absence of the promised canonical diagnostic is itself evidence that the frozen diagnostic contract was incompletely implemented. The underlying lower-level exception must not be invented if logs are unavailable.
- If all vulnerable shell paths complete successfully and the run reaches the frozen numerical comparator, this latent diagnostic-path defect was not exercised. The numerical/resource telemetry may still be inspected exactly, but any statement of full prereg diagnostic-compliance must be qualified by this audit finding.
- No successful or failed current run may be retroactively patched. Any repair requires a NEW version/experiment with prospective binding and hosted audit.

## Required repair for any successor

A future successor must make diagnostic coverage structural rather than string-based. Acceptable designs include:

- route every restore/push/materialization operation through a driver command that catches the exact subprocess exception and writes the canonical diagnostic; or
- install a shell `ERR` trap that calls a separately frozen diagnostic writer with stage, command, exit status and lineage, then best-effort durably syncs without ever turning the original failure into success.

The hosted audit must explicitly enumerate every prereg-relevant external command and prove that its nonzero path reaches diagnostic capture. Merely searching for diagnostic-related strings is insufficient.

This is governance/control evidence only and changes Article-3 readiness by `+0/+0`.
