# Exp073HT — C2 reference raw runtime producer v0.3

Status: **PROSPECTIVELY FROZEN BEFORE RUNTIME EXECUTION**. Scope: DSIR only. Raw-candidate producer only; no decode/map/prediction/scientific authority.

Authorized parent: Exp073HS `34230896860 / 102076459069 SUCCESS` raw-log token `PASS_EXP073HS_C2_FINAL_APPROXIMATION_INTERVAL_ENDPOINT_GUARD_BUILD_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`. Frozen post-HS hashes: `source/perturbations.c` SHA256 `483b481b48e50a6afb396b15b85258ac6c5a7a39b38fb1c6192e7e4a95c139ae`; `tools/evolver_ndf15.c` SHA256 `3f12121ce2de319453e1ff5fadae9391fd96747731c0df3fa05fae1cd2608aa9`.

Pinned parent remains `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`. Model exactly `reference_alpha0_beta0=(0,0)`. Baseline SHA256 `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`; p8 SHA256 `463a3960d6a955c1e2a561e988562a1fc5486b0b79f120eb634ccca6f86002f9`.

Frozen grid is unchanged: z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`; physical k/Mpc^-1 `[0.00067,0.00201,0.0067,0.0201]`; 28 z-major/k-minor requests; `0.067` forbidden. Each request adds only its exact `k_output_values` line and supplies exact z through `DSIR_C2_EXACT_Z`. Nested OMP/OpenBLAS/MKL threads exactly 1.

Observation remains exact native endpoint only. HS makes the hook eligible only on the approximation interval whose exact `tfinal == dsir_c2_diag_tau_target`; accepted `ynew` and equations/integration arithmetic are unchanged. No tolerance, rounding, nearest-time, interpolation, smoothing, averaging, effective coordinate, changed model/config or scientific rescue is permitted.

HN serializer remains frozen: eight binary64 fields `tau,k,a,H,delta_m,theta_m,rho_idm_iv,rho_iv`, exactly 64 bytes/packet. Exactly 28 packets must concatenate in canonical order to exactly 1792 bytes. Producer may hash raw bytes but must not decode/inspect scientific values.

Terminal artifact must contain aggregate, aggregate SHA256, 28 packet files, plan, endpoint text records, frozen bindings and provenance receipt with exact run/job/head/source/config/count/bytes/order/aggregate-SHA evidence.

Exact producer token: `PASS_EXP073HT_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_3`. PASS ceiling is `RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`, with `raw_record_set_admitted=false`, `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Workflow success/token alone is not admission. Exact terminal run/job/head/artifact/digest/aggregate SHA must be separately bound into frozen admission-receipt contract blob `1c2e30e6563efe3976ee0b1825dfb250a902a529` before any scientific field values may be decoded or inspected.

Any failure here is infrastructure/runtime/provenance `+0/+0`, never scientific FAIL at this boundary.
