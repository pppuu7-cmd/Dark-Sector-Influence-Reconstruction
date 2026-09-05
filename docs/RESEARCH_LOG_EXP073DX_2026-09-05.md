# DSIR research log — Exp073DW exact FAIL / Exp073DX diagnostic

Date: 2026-09-05
Scope: DSIR only.

Exp073DW run/job `33967669396 / 101310531746` completed with frozen token `FAIL_EXP073DW_WW_S0_S1_SERIALIZED_RELOAD_EXACT_ADAPTER_V0_1`. Artifact `9969959852` has GitHub digest and independently recomputed ZIP SHA256 `5dd606e7bf5db19a68f4bcea3ccf33f76d0ba1e77366a2f957a987e180ec6cbf`.

The terminal receipt is `QUALIFIER_FAIL +0/+0`, never science authority. Distinct S0/S1 masks and field objects, reloaded cross-vs-auto distinction, shapes, finiteness and no-tolerance checks all passed. The adapter full/selected arrays and selected SHA did not exactly equal the official serialized→reloaded W01 state. Therefore the prior DU pre-serialization reference defect is not the complete explanation; the current auto-qualified production adapter path is not exact for this distinct spin-2 cross workspace under the frozen qualifier. No post-hoc rescue or tolerance is allowed. Full-resolution WW_S0_S1 activation remains blocked.

Exp073DX is prospectively frozen as a hosted observational diagnostic to isolate whether raw FITS `WSP_PRIMARY` storage orientation differs from official reloaded `get_coupling_matrix()` in cross-field cases. It has no PASS authority and cannot alter DU/DW outcomes or production arithmetic. This commit triggers that diagnostic only. Exp073DT remains sole self-hosted heavy owner.
