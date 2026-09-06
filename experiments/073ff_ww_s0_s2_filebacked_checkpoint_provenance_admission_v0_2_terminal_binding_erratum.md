# Exp073FF v0.2 — terminal binding erratum

Prospective base: `experiments/073ff_ww_s0_s2_filebacked_checkpoint_provenance_admission_v0_1_prereg.md`, blob `c6f1fd11c4a0dc68bb17669a58854979fe84869e`. This erratum binds only terminal provenance discovered after Exp073FA completed; it does not alter any frozen scientific criterion.

Authoritative candidate producer:
- run `34020756634`, hosted envelope job `101452788638`, home science job `101452805620`;
- run head `894885b2c2b811954d1724c2733d2a810a486d70`;
- artifact id `9988291781`, name `exp073fa-ww-s0-s2-filebacked-ab-v0-1`;
- GitHub artifact digest and independently recomputed downloaded-ZIP SHA256: `70fd7e9ff320ba0dee9d0036c9777963b530ef605919c964484ea6cc3cb841a6`;
- candidate token `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- classification `SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION`;
- selected A/B canonical `<f8 [39,12288]` SHA256 `f7c02a13e746008c7b2099c2900787fb58ff39c2cc4cb0903ef11cb32fc9f07e`;
- full public BPW SHA256 `bb8d3c2c647ca62b341008acfa4f523b0af1c66a3779baafc9ffa26ee3c83a89`;
- serialized workspace FITS SHA256 `74831fe9aa7d7d85c2d91f5e9c0fc53e3c2ae9d5709f866034b8825b010005a4`.

The artifact was independently consumed before this binding was written: both six-stage checkpoint chains are complete; the ordered pair is `S0->S2` with indices `[0,2]`; `same_field_object_handoff=false`; the file-backed MCM receipt records exactly `19327352832` bytes and `/proc/self/maps` evidence; public `read_from(..., read_unbinned_MCM=True) -> get_bandpower_windows()` is used; A/B SHA equality, `numpy.array_equal`, finiteness, and no-tolerance-rescue are exact. Post-receipt pruning is acceptable only under the base preregistration's retained-evidence rule.

This candidate still creates no `WW_S0_S2` authority. Only `PASS_EXP073FF_WW_S0_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1` after the independent hosted admission may do so.
