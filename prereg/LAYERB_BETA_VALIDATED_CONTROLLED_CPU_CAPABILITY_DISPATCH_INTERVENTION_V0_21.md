# DSIR V0.21 preregistration — validated controlled CPU-capability dispatch intervention

Status: **PROSPECTIVELY FROZEN BEFORE V0.21 IMPLEMENTATION/EXECUTION**. Date: 2026-09-14. Scope: DSIR only.

## Parent authority

Parent terminal authority: `docs/dsir4/authority/LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_V0_20.json`, classification `NUMPY_AVX512_RUNTIME_DISPATCH_MASK_VALIDATED`, authorized successor exactly `PROSPECTIVELY_FROZEN_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT`.

V0.18R and V0.19 were intervention-validation failures and are not salvaged. Their failure-cell response values are forbidden inputs to this preregistration and were not inspected. V0.20 was response-free and validated only the NumPy runtime-dispatch intervention primitive.

## HYPOTHESIS

On the same exact AMD EPYC 9V74 host and identical CLASS/classy binaries, prospectively disabling AVX-512 runtime dispatch changes both frozen V0.17 replay-failure responses from the frozen native-capability branch toward the frozen alternate-capability branch while leaving the anchor stable. NumPy-only and glibc-only interventions prospectively localize the numerical mechanism; the combined intervention remains the primary causal test.

## EXACT VALIDATED NUMPY RUNTIME PROFILE

V0.20 froze and independently reproduced the following exact NumPy 1.26.4 profile on four exact-target hosted runners:

- baseline: `SSE,SSE2,SSE3`
- dispatch list in exact order: `SSSE3,SSE41,POPCNT,SSE42,AVX,F16C,FMA3,AVX2,AVX512F,AVX512CD,AVX512_KNL,AVX512_KNM,AVX512_SKX,AVX512_CLX,AVX512_CNL,AVX512_ICL`
- AVX-512 dispatch targets: `AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX`
- native active AVX-512 dispatch: `AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_SKX`
- native active non-AVX512 dispatch: `AVX,AVX2,F16C,FMA3,POPCNT,SSE41,SSE42,SSSE3`
- validated NumPy mask: `NPY_DISABLE_CPU_FEATURES=AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX`

The glibc intervention remains the already validation-passing V0.18R control:
`GLIBC_TUNABLES=glibc.cpu.hwcaps=-AVX512F,-AVX512DQ,-AVX512CD,-AVX512BW,-AVX512VL`.

## OBJECT

Thirty-two independent GitHub-hosted `ubuntu-24.04` jobs. Each lane builds one exact pinned CLASS/classy binary stack and then performs a response-free four-condition intervention preflight before any DSIR response computation.

A lane is scientifically eligible only if its native state satisfies all of:

1. exact CPU identity `AuthenticAMD / family 25 / model 17 / stepping 1 / AMD EPYC 9V74 80-Core Processor`;
2. `/proc/cpuinfo` AVX512F present;
3. native glibc x86-64-v4 active;
4. NumPy version exactly `1.26.4`;
5. NumPy baseline list exactly equals the frozen V0.20 baseline;
6. NumPy dispatch list exactly equals the frozen V0.20 dispatch list;
7. native active AVX-512 dispatch exactly equals the frozen V0.20 native active AVX-512 dispatch list;
8. native active non-AVX512 dispatch exactly equals the frozen V0.20 active non-AVX512 dispatch list.

Ineligible lanes produce provenance-only SKIP and no response values.

Each eligible lane runs four fresh child-interpreter preflight conditions on the same host/binaries:

1. `NATIVE`: no override.
2. `NUMPY_NO_AVX512`: exact V0.20 validated NumPy mask.
3. `GLIBC_NO_AVX512`: exact validated glibc mask above.
4. `COMBINED_NO_AVX512`: both exact masks.

Only if all four preflight conditions validate does that lane compute substantive paired solver responses for those same four conditions.

## FROZEN PREFLIGHT VALIDATION

For every eligible lane:

- all four conditions have identical CLASS/classy binary identity;
- all four conditions retain NumPy version 1.26.4 and exact frozen baseline/dispatch lists;
- `NATIVE`: active AVX-512 and non-AVX512 dispatch lists exactly equal frozen V0.20 native lists; glibc v4 active; no mask environment variables present;
- `NUMPY_NO_AVX512`: active AVX-512 dispatch empty; active non-AVX512 dispatch exactly preserved; glibc v4 active; NumPy mask string exact;
- `GLIBC_NO_AVX512`: active NumPy dispatch profile exactly native; glibc v4 inactive; glibc mask string exact;
- `COMBINED_NO_AVX512`: active AVX-512 dispatch empty; active non-AVX512 dispatch exactly preserved; glibc v4 inactive; both mask strings exact;
- raw NumPy `__cpu_features__` AVX-512 entries outside `__cpu_dispatch__` are diagnostic only and may remain true;
- physical `/proc/cpuinfo` capability flags are not expected to change and are not intervention-success criteria.

If any eligible preflight fails, that lane computes no substantive response and terminal classification is intervention INVALID before scientific-effect evaluation.

## FROZEN SCIENTIFIC/NUMERICAL INPUTS

Unchanged from the original prospectively frozen V0.18 hypothesis:

- CLASS commit `ac627d54e9ce196a08878d1ba33999819925d19c`.
- Baseline `configs/dsir4/c2/ide0_reference_v0_1.ini`.
- Production precision `configs/dsir4/c2/dsir_ide_p8_v0_1.pre`.
- Production `h=1e-4` unchanged.
- GRID1024: base 1024, one upper guard, 1025 requested nodes.
- `tol_perturb_integration=1e-12`.
- production perturbation sampling `0.00035`.
- intervention/replay relative tolerance `<1e-5`.
- scientific response tolerance `<1e-3` remains unopened for this numerical mechanism audit.
- exact requested-node binding `<=1e-12`.
- minimum scientifically eligible paired lanes: `3` independent jobs.

Exact diagnostic cells:
- replay failure: `h=2e-4`, `z=3fdab851eb851eb8`, `k=3f890ea7bc915d36`;
- replay failure: `h=1e-4`, `z=3fe3d70a3d70a3d7`, `k=3f8fc70971921840`;
- anchor: `h=1e-4`, `z=3fdab851eb851eb8`, `k=3f890ea7bc915d36`.

Frozen V0.17 branch references:
- native-capability: `h=2e-4 -> -0.32758589441073127`, `h=1e-4 -> 0.1355044923911919`;
- alternate-capability: `h=2e-4 -> -0.32763449098638375`, `h=1e-4 -> 0.13550307244258875`.

## POSITIVE CONTROLS

- invariant identity/hash audit passes;
- all 32 host lanes terminal and uniquely identified;
- at least 3 eligible exact-target/V0.20-profile lanes;
- every eligible lane passes response-free four-condition preflight;
- same exact binary identity across paired conditions;
- all substantive eligible responses finite;
- exact requested-node mismatch `<=1e-12`;
- anchor pairwise condition spread `<1e-5` in every eligible lane;
- production h/sampling/tolerance unchanged;
- no forbidden downstream object touched.

## NEGATIVE CONTROLS

- ineligible hosts never compute response;
- invalid-preflight eligible hosts never compute response;
- ephemeral runner/job/PID/address/timing are forbidden classifiers;
- V0.18R/V0.19 failure-cell responses are forbidden historical inputs;
- green CI is not scientific PASS;
- validated dispatch manipulation is not itself evidence of a DSIR branch effect;
- a supported numerical mechanism is not full Layer-B validation and not dark-sector evidence.

## FROZEN DECISION

Decision hierarchy remains the original V0.18 scientific hierarchy, with corrected prospectively validated intervention semantics.

1. `INVALID_INTERVENTION`: any eligible lane fails the frozen four-condition preflight or paired binary identity -> `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID`; no scientific promotion; validation diagnosis only.
2. `INCONCLUSIVE`: any frozen identity/hash fails, any eligible substantive response is non-finite, exact binding exceeds `1e-12`, anchor pairwise condition spread reaches `1e-5`, or any prohibited object is touched -> `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INCONCLUSIVE`; no promotion.
3. `UNDERPOWERED`: fewer than 3 eligible preflight-valid paired jobs -> `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_UNDERPOWERED`; expanded prospective paired replication only.

For an intervention condition to count as a branch-switch effect, in **every** eligible lane and on **both** replay-failure cells:
(a) `NATIVE` is within `<1e-5` relative of the frozen V0.17 native branch;
(b) the intervention is within `<1e-5` relative of the frozen V0.17 alternate branch;
(c) native-versus-intervention relative separation is `>=1e-5`.

- NumPy-only satisfies branch switch and glibc-only does not -> `NUMPY_AVX512_DISPATCH_INTERVENTION_SUPPORTED`.
- glibc-only satisfies branch switch and NumPy-only does not -> `GLIBC_AVX512_DISPATCH_INTERVENTION_SUPPORTED`.
- both component interventions independently satisfy branch switch -> `NUMPY_AND_GLIBC_AVX512_DISPATCH_INTERVENTIONS_SUPPORTED`.
- neither component alone switches but combined does -> `COMBINED_CPU_CAPABILITY_DISPATCH_INTERVENTION_SUPPORTED_NOT_COMPONENT_ISOLATED`.
- all validations pass but combined remains within `<1e-5` relative of native on either replay-failure cell in every eligible lane -> `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_NO_EFFECT`.
- otherwise -> `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_MIXED`.

Any supported intervention classification authorizes only `PROSPECTIVELY_FROZEN_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_AUDIT`.
`NO_EFFECT` authorizes only `PROSPECTIVELY_FROZEN_PROCESS_INITIALIZATION_MEMORY_LAYOUT_AUDIT`.
`MIXED` authorizes only `PROSPECTIVELY_FROZEN_CONTROLLED_DISPATCH_INTERVENTION_REPLICATION_AUDIT`.
`INVALID` authorizes validation diagnosis only. `INCONCLUSIVE` gives no promotion. `UNDERPOWERED` authorizes only expanded prospective paired replication.

## INTERPRETATION CEILING

V0.21 can establish whether a prospectively validated runtime-dispatch intervention causally changes the already-known numerical response branch and can localize such an effect to NumPy, glibc, both, or a combined-only state. It cannot validate full Layer-B, open covariance/whitening/nuisance/relation-null, open `Wm_S3`, authorize global 65537, establish dark-sector inference, or claim a physical signal. Even a supported causal numerical mechanism has effect `+0/+0` until a separately frozen reproducibility repair and later science gate pass.
