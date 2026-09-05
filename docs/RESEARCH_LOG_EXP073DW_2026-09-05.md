# DSIR research log — Exp073DU diagnosis / Exp073DW repair qualifier

Date: 2026-09-05
Scope: DSIR only.

Exp073DU run/job `33955300558 / 101277450615` was consumed from raw job logs and artifact `9966167115`. Artifact ZIP digest independently matched GitHub SHA256 `34a90ebe024c53c1bb833465346bd0ef6ca3196184bb49a8ba18e543eca8bba1`.

Exp073DU v0.1 is classified `QUALIFIER_FAIL +0/+0`, not science. Required distinct-mask/object, cross-vs-auto, shape, finiteness and no-tolerance checks passed. The only failed gates were adapter full/selected exact equality and selected SHA against the pre-serialization in-memory `W01` reference. The frozen production adapter consumed serialized `w01.fits`; Exp073EA had already established that the official serialized→reloaded workspace is the exact authority for the saved-LU route and may differ from the pre-serialization in-memory state at last bits. Therefore the first causal defect is the DU qualifier reference-state contract, not WW arithmetic.

Historical Exp073DU v0.1 is immutable and remains FAIL `+0/+0`.

Exp073DW was prospectively preregistered as the minimal support-only repair. It retains the same synthetic cross-field geometry and exact production adapter but compares only against official `NmtWorkspace.read_from(w01.fits)` state. Pre-serialization vs reloaded equality is diagnostic only. No tolerance rescue is allowed. Exp073DW cannot create WW authority or interfere with Exp073DT.

This commit intentionally triggers the hosted-only Exp073DW workflow. Self-hosted DSIR ownership remains reserved exclusively for Exp073DT attempt 4 while queued/in_progress.
