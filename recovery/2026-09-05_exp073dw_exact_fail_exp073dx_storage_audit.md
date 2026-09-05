# Exp073DW exact qualifier FAIL; Exp073DX storage/orientation diagnostic dispatched

Date: 2026-09-05
Scope: DSIR only.

Exp073DW run/job `33967669396 / 101310531746` completed with qualifier failure. Artifact `9969959852` was downloaded; GitHub digest and independently recomputed ZIP SHA256 both equal `5dd606e7bf5db19a68f4bcea3ccf33f76d0ba1e77366a2f957a987e180ec6cbf`.

Raw receipt: `classification=QUALIFIER_FAIL`, token `FAIL_EXP073DW_WW_S0_S1_SERIALIZED_RELOAD_EXACT_ADAPTER_V0_1`, `science_gate_scored=false`, `ww_s0_s1_authority_created=false`, accounting `+0/+0`. Passed: distinct masks/fields, cross-vs-auto distinction, expected shapes, finiteness, no tolerance rescue. Failed exactly: adapter full exact vs official serialized→reloaded W01, adapter selected EE exact vs reloaded W01, and selected SHA equality. Reloaded selected SHA is `02d0fc53059de8fa3af61337cb58dfe53fd0f288bceef131c7a9b8be83769a93`; adapter selected SHA is `239a80aaf552f9fcfb4523a7b6e409b9570fd82503a2672fb498e530dbe4bc11`. Pre-serialization selected SHA is separately `75e144d4654b1c867b09865d32958733b2829510878ba8f39143910264b5dbc6`.

Therefore Exp073DU's pre-serialization reference defect was real but not sufficient: the current production adapter route itself is not exact for this distinct spin-2 cross workspace under the frozen qualifier. This is a genuine support/readiness negative result `+0/+0`, not infrastructure and not a WW science FAIL. No tolerance or post-hoc rescue is permitted. Exp073DV full-resolution WW_S0_S1 activation is blocked pending a prospectively justified cross-workspace adapter architecture.

Exp073DX was preregistered before its output as diagnostic-only `+0/+0` to compare raw FITS `WSP_PRIMARY` storage with official reloaded `get_coupling_matrix()` for W01/W10/W00/W11 and determine whether orientation/storage is the first structural cause. Prereg commit `012c461df4b8351f509ad511438ebe4423ac99a5`; implementation commit `4e9d39f5e230203a2ec107d46bd7ede8b254bd1c`; workflow commit `8c32ee8ac8f919bb1718e973d999504f822a1d71`; activation/log head `4375ee5daa387e8bcb018cd949beb737c6c6c228`. Hosted run `33967888245` was queued at dispatch. It cannot create authority or modify DU/DW outcomes.

Exp073DT attempt 4 remains sole self-hosted heavy owner, run/job `33940588308 / 101288014666`, and DSIR-HOME-PC remains reserved while queued/in_progress.
