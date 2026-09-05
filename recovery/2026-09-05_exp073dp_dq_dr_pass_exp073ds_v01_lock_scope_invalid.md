# DSIR immutable recovery — Exp073DP/DQ/DR PASS; Exp073DS v0.1 lock-scope invalid

Date: 2026-09-05. DSIR only.

## Preserved authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact PASS remain unchanged. `WW_S0_S0` still has no scientific authority.

## Exp073DP repaired exact-equivalence PASS `+0/+0`
Attempt 1 run/job `33938315128 / 101230515264` was infrastructure/dependency FAIL before any comparator because PyPI does not publish `pymaster==2.7.0`. Prospective dependency-only repair commit `b2dc8a395991963885d47a964d44c50c3ef2927e` bound official NaMaster tag v2.7.

Repaired run/job `33938446310 / 101230897808` terminal SUCCESS; artifact `9960969007`; GitHub and independent ZIP SHA256 `e34b545b21fc93f8948ad328084afd405885c1045313d7162b553a45583af7a8`. Raw token `PASS_EXP073DP_WW_EXACT_ADAPTER_SMALLNSIDE_EQUIVALENCE_V0_1`; NaMaster source commit `24365fa59a38c15732f4f37e8b29265b75c442d5`. All three synthetic spin-2 auto cases have exact full-array SHA equality, exact `numpy.array_equal=true`, full max absolute difference `0.0`, and the same exact equality for selected EE. Support only `+0/+0`.

## Exp073DQ durable A/B driver static PASS `+0/+0`
Prereg commit `6901518f6655d61f9d234a0d8380e0c4336e2222`; durable driver commit `31b961ff62153cf2fbde446f8167e0f274103c8b`; static audit commit `30f847e58e048199c48ed658f19e90a84a83dd87`; workflow/head `3e2487ecb0ee69ec65872eae8483986a41ae60d9`.

Run/job `33938583879 / 101231302981` terminal SUCCESS; artifact `9961000737`; GitHub and independent ZIP SHA256 `93a3db6b27ee9fba9f4d0549b9d6e03c2a50cb7f6ad224c41e773a85b969682c`. Raw token `PASS_EXP073DQ_WW_S0_S0_DURABLE_AB_DRIVER_STATIC_ADMISSION_V0_1`; driver SHA256 `0b7a0a2336a89dcea63060d4049d09fabacc9c5e75fad870d2599efd27d0e63b`. Dedicated A/B namespaces and complete-stage checkpoint order are frozen; exact A/B comparator uses SHA equality and `numpy.array_equal`; no home/science authorization.

## Exp073DR hosted activation/resource PASS `+0/+0`
Prereg commit `95af8fc099c4e6543a096739cd05d332c767b3bf`; audit commit `b90f33940ea88eb72b4efcfaf241895c22b6de10`; workflow/head `d2fda7b7937451dcea05bef1f55fcc08dfbc5203`.

Run/job `33938637212 / 101231459805` terminal SUCCESS; artifact `9961019381`; GitHub and independent ZIP SHA256 `eb7b74adabedc01a2f0212bc04fe612c0ae53d8156d2c904f02bc02e58d5a6c6`. Raw token `PASS_EXP073DR_WW_S0_S0_HOSTED_ACTIVATION_RESOURCE_PREFLIGHT_V0_1`; `home_readiness_preflight_authorized=true`, `home_science_execution_authorized=false`. It prospectively admits the full stock workspace as a durable complete-stage boundary only after atomic FITS+manifest SHA verification; verified completed workspace must never be recomputed.

## Exp073DS v0.1 governance invalidation `+0/+0`
Prereg commit `a0453b1d785a87c86c6cde445877993e90198a37` requires a dedicated nonblocking flock for the entire self-hosted readiness section. Initial workflow/head `ba46107f7eb4d6bef0947b9a2b03c69e1be87424` implemented lock acquisition in a standalone Actions step, then performed exclusivity/environment/R1/runtime/readiness checks in later steps. Shell file descriptors do not persist across Actions step processes, so FD9 and its flock are released at the end of the lock-acquisition step.

This is a prospective infrastructure/governance defect discovered before accepting any terminal receipt. Therefore run `33938720719` / home job `101231724345` is **not eligible to create Exp073DS readiness authority even if every workflow step reports SUCCESS**. It remains support/infrastructure `+0/+0`; it computes no full-resolution workspace and no selected WW payload.

Smallest allowed repair: preserve the frozen preregistration and readiness criteria, but move the entire self-hosted readiness body under one shell process holding one nonblocking flock continuously. R1 artifact transport must also occur inside that locked shell (e.g. direct artifact download through GitHub API) or before it only if the locked body revalidates exact payload authority and no mutable readiness state is touched beforehand. The repaired run must be a prospectively versioned workflow and independently consumed artifact. Do not weaken noncompetition or science boundaries.
