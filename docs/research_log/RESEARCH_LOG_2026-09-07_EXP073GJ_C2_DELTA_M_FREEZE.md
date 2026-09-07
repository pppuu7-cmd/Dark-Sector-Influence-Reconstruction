# DSIR research log — Exp073GJ C2 IDE Delta_m generation freeze

Date: 2026-09-07

While Exp073FS attempt 2 remained the sole active heavy DSIR computation, an independent C2 IDE prediction-interface step was completed without reading partial FS numerical output.

Exp073GJ prospectively froze the same-solver common matter response bridge, pinned solver lineage, base tangent points, seven inherited redshift nodes, and the exact four-node in-domain subset `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`. The legacy converted node `0.067 Mpc^-1` remains excluded because it exceeds frozen DSIR `k_max=0.06664762008318016`; no rounding or replacement endpoint was introduced.

The freeze explicitly prohibits relabelling legacy raw `mPk` or raw `delta_idm_iv` as the required common `Delta_m` prediction. It also freezes fail-closed solver-native variable identities, physical branch masks, canonical JSON serialization and payload SHA256 requirements.

Prereg creation commit: `668031cade3455e795e299056c9d98334b4ad0e3`.

Hosted static-audit runs `34081553496`, `34081596871`, and `34081626964` were implementation/static FAIL `+0/+0`, all before any self-hosted science. Diagnostic logs isolated the first causal defect to the audit harness: it expected square-bracket `ln[...]` syntax while the immutable prereg froze parenthesized `ln(...)`. Minimal repair commit `1b977af76a7ca2de438156a7ceb88c4e1a29844c` changed only that support literal.

Repaired run/job `34081658093 / 101617944759` produced exact token `PASS_EXP073GJ_C2_IDE_DELTA_M_GENERATION_FREEZE_STATIC_AUDIT_V0_1` with `classification=SUPPORT_PLUS_0_PLUS_0`, `self_hosted_science_started=false`, and `scientific_model_authority_created=false`.

Therefore C2 remains `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, contribution `+0/+0`. The next independent C2 step is implementation/static audit of a generator that obeys Exp073GJ exactly; heavy priority remains terminal consumption of Exp073FS attempt 2.