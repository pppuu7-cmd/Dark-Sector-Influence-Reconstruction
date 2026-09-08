# DSIR Recovery V46 — HZ/IA PASS; IB v0.2 exact map PASS; IC response front

Date: 2026-09-08 UTC. Scope DSIR only; RTK/RQIR excluded.

## Preserved authority
All pre-existing DSIR scientific authority is unchanged, including admitted `WW_S3_S3` run `34218457380 / 102035691774`, GA artifact `10051382493`, SHA256 `a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`. C2 still creates no scientific model authority.

## Exp073HY / HZ
HY run `34243515299` remains the validated nine-model raw candidate. HZ run `34248477503`, job `102136488451`, head `edaa94d42b18f45a6e0659dc23399793e0228830` raw-log PASS `PASS_EXP073HZ_C2_TANGENT_RAW_SET_PROVENANCE_ADMISSION_V0_1`; classification `TANGENT_RAW_SET_ADMITTED_PLUS_0_PLUS_0`; `tangent_raw_set_admitted=true`, `decoded=false`, no mapping/prediction/scientific authority.

## Exp073IA exact ABI decode PASS
Prereg creation commit `c0b060377ff7490d00601d119300d39e00017583`, blob `138627ebd0a53dc0118c8908e40d329427430e0e`. Workflow/head `c0e738d271954c6eb936e2b418165e0b1500b593`; run `34248722000`, job `102137324616`, artifact `10065081303`, independently verified ZIP SHA256 `6bf115c76d538f0691c1fcfa9d9a26721b9b593f26aceb2a7a59bdb7cc9aa0ce`. Raw PASS `PASS_EXP073IA_C2_TANGENT_RAW_ABI_DECODE_V0_1`, classification `TANGENT_DECODED_RECORD_SET_PLUS_0_PLUS_0`. Every 64-byte packet was decoded as exact native `=8d` binary64 and round-tripped byte-exactly; no mapping was performed.

Canonical per-model decoded JSONL SHA256:
- alpha_m1e4 `6fa9d0b0bc106b554359bfcf98cf6b2b18ef7427f659f1a415bcc3a4fdb84bb1`
- alpha_m1e3 `99983545cf0788c437eefcd0fce78b7ccfabd9b856ca0c799dd3fa84df86215c`
- alpha_m1e2 `524e4fd59fd5183b5d805e4d2bf8a56222c2ee3cf34037aa8b69196124f175f8`
- beta_p1e4 `29e5a714a5ae798c569dea790bbab23df8deae6cb6c98c1f09cc2269f02340b2`
- beta_m1e4 `9e0bef37662f305265bd2462567368193014178fce1b12db3504e061cf7c491d`
- beta_p1e3 `fa3e9049b8976ee7b94a04d70db52d99e5d0c3665e580977f6378b67a53d9287`
- beta_m1e3 `f87dc82b2c2cec1d99cd1b92638a38b723f3b758a95421026e79b643aa983a8c`
- beta_p1e2 `90fbbc7015ab92f9a3da7ee9f9b91cf86ee4bc0ae361c8e368cbed5581fbfe73`
- beta_m1e2 `c17291f40156d769306288138847ec3fc09a00cd75abc137dafb1a1ba7b441a3`.

## Exp073IB v0.1 historical implementation/provenance FAIL +0/+0
IB v0.1 prereg/workflow produced run `34248841106`, job `102137736842`, artifact `10065129526`, ZIP SHA256 `b0725f47946c0abacff21e4e686fe9d746be26d6249ae9c6a36cce34683639c7`. Workflow emitted a mapping PASS token, but terminal consumption found that its source expression did not explicitly reproduce the already-authoritative HW receipt arithmetic order `hconf_then_velocity_term_then_add`. Therefore workflow success was not promoted to authority. Classification is historical `IMPLEMENTATION_PROVENANCE_FAIL_PLUS_0_PLUS_0`, not scientific FAIL. Independent audit found 0/252 realized binary64 output differences versus exact HW order, so no numerical/scientific negative result is inferred.

## Exp073IB v0.2 repaired exact map PASS
Prospective minimal repair prereg creation commit `7e209226e3f609fee55a39b9d09baf3e45bf8b4c`, blob `69c8e313cbe95ee426ba23112d63548c9ab26556`; workflow/head `f2196c40d1608aa66b20bf4431ce3e7763970a38`. Run `34249229753`, job `102139059309`, artifact `10065286473`, GitHub artifact ZIP SHA256 `965e921224f516e76e9cf2d2ac84ed51a5027b97d79c73c87620d55a83011201`.

Raw PASS `PASS_EXP073IB_C2_TANGENT_DELTAM_COMMON_COORDINATE_MAP_V0_2`, classification `TANGENT_MAPPED_COMMON_COORDINATE_PLUS_0_PLUS_0`. v0.2 binds HW artifact `10062705321` and explicitly executes: `hconf=a*H`; `velocity_term=3.0*hconf*theta_m/(k*k)`; `Delta_m=delta_m+velocity_term`. Exact regression reports `EXP073IB_V0_2_REGRESSION_EXACT_EQUAL_RECORDS=252`. Independently downloaded v0.2 artifact verifies exact ZIP digest, authority receipt, 9×28 ordered finite mapped rows and per-model SHA manifest. State: `mapped_tangent_coordinate=true`, `tangent_response_ready=false`, `prediction_ready=false`, no scientific authority.

Mapped per-model SHA256:
- alpha_m1e4 `e119867714d892d09a862f5edd2eca08adc3a64f9ce8f728707ff44dce6da3c3`
- alpha_m1e3 `287c6925e5ec85b714125e9e55b02a3ebd5a14d13cf492a317f5aad619d6c290`
- alpha_m1e2 `34aa4f0ec86f38a5258eeeb0fddbf9268d3325c270c860ff94cf664ad498c8d1`
- beta_p1e4 `3e2a659328e509a357e8291c469ed711108ec7d126a56c10d15aa07285ea419f`
- beta_m1e4 `165691d43d02002a04afb75333cf7f54fbb48865b4b4fb0ef2443c6a85b1b735`
- beta_p1e3 `1d01532756f1ae25c07bfad819a6e2572050cb74ce04a0751198c897f5f9a5a6`
- beta_m1e3 `a79d65b8b80d304c1e9a92f31d86e92aca6c38a39d6a34788aec55deebe6c0b8`
- beta_p1e2 `aad9aabfc72dd5746f38a0360d9831ace407328ad7e4a53f9d163b62adcb3574`
- beta_m1e2 `f76fcee55a18e9ba234854f353b25f74d1ea771a9ffdf77b0ad9391aefd5de58`.

## Current front — Exp073IC finite-difference response candidate v0.1
Prereg creation commit `7d94f9f9bfaa3b320250c7b046d2a6c7a37309b5`, blob `9e1235a48a4288bb2083d69084f1cae7d79847bb`; workflow/head `f3475f5d409a50c31fb1eda3870837542797e091`; run `34249380208`, job `102139612475`, GitHub-hosted ubuntu-24.04; home/self-hosted runner free. State at note creation: QUEUED.

IC is prospectively frozen candidate calculation only. It uses HX-frozen one-sided alpha and symmetric beta definitions at exact scales 1e-4,1e-3,1e-2; h=1e-4 is base, larger scales controls. It applies no convergence threshold, no scale selection, no extrapolation, no prediction and no scientific authority. Expected PASS `PASS_EXP073IC_C2_TANGENT_FINITE_DIFFERENCE_RESPONSE_CANDIDATE_V0_1`; on PASS `response_candidate_created=true` but `tangent_response_ready=false`.

## Exact next transition
Consume IC terminal raw log and artifact. On exact candidate PASS, freeze a separate response-stability/admission contract before inspecting scale relations for acceptance. Do not post-hoc choose a favorable scale or threshold. On IC infrastructure/provenance failure, repair only the first causal defect while preserving HW/IA/IB v0.2 authorities.

Global frozen DSIR boundaries remain unchanged.