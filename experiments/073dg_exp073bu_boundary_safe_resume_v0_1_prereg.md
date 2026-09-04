# Exp073DG — boundary-safe Exp073BU checkpoint resume v0.1

Date: 2026-09-04. DSIR only. Support/infrastructure `+0/+0`.

Exp073DE and Exp073DF established split historical-science/resume implementation identity and immutable legacy-complete passthrough. A further source audit found one remaining checkpoint-boundary issue in the inherited v0.1 control flow: if `full_window_complete` exists but `selected_te_complete` does not, the base path would execute the expensive adapter again. That would unnecessarily recompute and overwrite a verified complete stage.

Prospective repair requirements:
- never rewrite any already valid stage manifest;
- if `full_window_complete` exists and `selected_te_complete` is absent, verify the frozen full-window payload SHA/shape and derive only canonical `wins[0,:,0,:] = TE<-TE` into `<f8 [39,12288]`, with exact byte/SHA and `numpy.array_equal` verification; do not rerun the adapter;
- if selected TE already exists, reuse it; if full window is absent, adapter execution remains permitted from the latest prior verified checkpoint;
- valid legacy final receipts remain read-only passthrough with exact cumulative `{1,1}` lineage;
- missing/malformed/source-head/contract-fingerprint/SHA mismatches remain fail-closed;
- all 8-core arithmetic/adapter blobs and exact comparator remain unchanged.

PASS token: `PASS_EXP073DG_BOUNDARY_SAFE_RESUME_V0_1`. Only raw hosted PASS permits construction of the self-hosted resume workflow.
