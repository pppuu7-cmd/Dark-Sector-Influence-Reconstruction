# DSIR V0.19 preregistration — repaired controlled CPU-capability dispatch intervention

Status: **PROSPECTIVELY FROZEN BEFORE V0.19 IMPLEMENTATION/EXECUTION**. Date: 2026-09-14. Scope: DSIR only.

## Parent authorities

Scientific parent: `docs/dsir4/authority/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_18R.json`, classification `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID`, effect `+0/+0`.

Validation-diagnosis parent: `docs/dsir4/authority/LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_VALIDATION_DIAGNOSIS_V0_18D.json`, classification/diagnosis `NUMPY_AVX512_MASK_INCOMPLETE_AND_VALIDATOR_OVERBROAD`, authorized successor exactly `PROSPECTIVELY_FROZEN_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT`.

No V0.18R substantive failure-cell response values were inspected while diagnosing the invalid intervention. The diagnosis used only intervention-validation fingerprints, binary identities, anchor/invariant summaries and the terminal decision.

## REPAIR AND NON-REPAIR BOUNDARY

V0.19 changes **only** the NumPy dispatch intervention implementation and its positive-control validation. The V0.18 scientific hypothesis, exact target CPU model, four paired conditions, host-pairing logic, exact diagnostic cells, V0.17 branch references, minimum eligible sample size, numerical thresholds, decision hierarchy and interpretation ceiling are unchanged.

The V0.18R NumPy mask listed only a subset of the AVX-512 dispatch features that were natively active on every one of its seven exact-target eligible hosts, while the validator required all AVX-512 dispatch to be absent. V0.19 prospectively freezes the complete native-active AVX-512 NumPy feature set observed identically on all seven eligible V0.18R hosts and masks every member of that set.

## HYPOTHESIS

On the same exact AMD EPYC 9V74 host and identical CLASS/classy binaries, prospectively forcing AVX-512 runtime dispatch off changes the two frozen V0.17 replay-failure responses from the frozen native-capability branch toward the frozen alternate-capability branch while leaving the anchor stable. NumPy-only and glibc-only interventions localize the numerical mechanism; the combined intervention remains the primary causal test.

## OBJECT

Thirty-two independent GitHub-hosted `ubuntu-24.04` jobs. Each job fingerprints the native host before any substantive response computation.

A job is scientifically eligible only when all of the following hold prospectively:

1. exact CPU identity is `AuthenticAMD / family 25 / model 17 / stepping 1 / AMD EPYC 9V74 80-Core Processor`;
2. `/proc/cpuinfo` reports AVX512F;
3. native glibc loader diagnostics report x86-64-v4 active;
4. native NumPy runtime reports **exactly** the following active AVX-512 feature set, with no additional active AVX-512 feature:

`AVX512BITALG, AVX512BW, AVX512CD, AVX512DQ, AVX512F, AVX512IFMA, AVX512VBMI, AVX512VBMI2, AVX512VL, AVX512VNNI, AVX512VPOPCNTDQ, AVX512_CLX, AVX512_CNL, AVX512_ICL, AVX512_SKX`.

An ineligible job writes provenance-only SKIP and computes no substantive response.

Each eligible job uses one exact build of the pinned CLASS source and executes four fresh child Python processes on the same runner and exact binaries:

1. `NATIVE`: no dispatch override.
2. `NUMPY_NO_AVX512`: `NPY_DISABLE_CPU_FEATURES=AVX512BITALG,AVX512BW,AVX512CD,AVX512DQ,AVX512F,AVX512IFMA,AVX512VBMI,AVX512VBMI2,AVX512VL,AVX512VNNI,AVX512VPOPCNTDQ,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_SKX`.
3. `GLIBC_NO_AVX512`: unchanged validated V0.18R control `GLIBC_TUNABLES=glibc.cpu.hwcaps=-AVX512F,-AVX512DQ,-AVX512CD,-AVX512BW,-AVX512VL`.
4. `COMBINED_NO_AVX512`: both overrides simultaneously.

The override variables must be set before child-interpreter startup and before NumPy/classy numerical code is loaded.

## FROZEN INPUTS AND THRESHOLDS

- CLASS commit `ac627d54e9ce196a08878d1ba33999819925d19c`.
- Baseline `configs/dsir4/c2/ide0_reference_v0_1.ini`.
- Production precision `configs/dsir4/c2/dsir_ide_p8_v0_1.pre`.
- Production `h=1e-4` unchanged.
- GRID1024 unchanged: base 1024, one upper guard, 1025 requested nodes.
- `tol_perturb_integration=1e-12`.
- production perturbation sampling `0.00035`.
- replay/intervention relative tolerance `<1e-5`.
- scientific response tolerance `<1e-3` remains unopened/not used to promote this numerical mechanism audit.
- exact requested-node binding `<=1e-12`.
- minimum scientifically eligible paired lanes: `3` independent jobs.

Exact diagnostic cells remain:
- replay failure: `h=2e-4`, `z=3fdab851eb851eb8`, `k=3f890ea7bc915d36`;
- replay failure: `h=1e-4`, `z=3fe3d70a3d70a3d7`, `k=3f8fc70971921840`;
- anchor: `h=1e-4`, `z=3fdab851eb851eb8`, `k=3f890ea7bc915d36`.

Frozen V0.17 branch references remain exactly:
- native-capability: `h=2e-4 -> -0.32758589441073127`, `h=1e-4 -> 0.1355044923911919`;
- alternate-capability: `h=2e-4 -> -0.32763449098638375`, `h=1e-4 -> 0.13550307244258875`.

## POSITIVE CONTROLS

For every eligible lane:

- native active NumPy AVX-512 set must equal the frozen 15-feature set exactly;
- `NATIVE`: glibc x86-64-v4 active and all 15 frozen NumPy AVX-512 features active;
- `NUMPY_NO_AVX512`: glibc x86-64-v4 remains active and **every** frozen 15-feature NumPy AVX-512 feature is false; no NumPy AVX-512 feature may remain active;
- `GLIBC_NO_AVX512`: glibc x86-64-v4 is inactive while the exact frozen native 15-feature NumPy AVX-512 set remains active;
- `COMBINED_NO_AVX512`: glibc x86-64-v4 is inactive and every frozen 15-feature NumPy AVX-512 feature is false; no NumPy AVX-512 feature may remain active;
- exact environment-variable strings match the frozen condition;
- same CLASS/classy binary identity across all four paired child processes;
- all eligible responses finite;
- exact requested-node mismatch `<=1e-12`;
- anchor pairwise condition spread `<1e-5`;
- no production h/sampling/tolerance mutation.

## NEGATIVE CONTROLS

- ineligible hosts cannot enter the scientific classifier;
- physical `/proc/cpuinfo` AVX512 flags are not expected to change and are not intervention-success evidence;
- job IDs, runner IDs, PIDs, addresses and timing are forbidden classifiers;
- green CI alone is not a scientific PASS;
- no V0.18R failure-cell result may be used to tune this repaired mask, thresholds, branch references or classifier;
- no post-hoc salvage of the valid V0.18R glibc condition is allowed;
- a supported runtime intervention is a numerical mechanism finding only, not full Layer-B validation or dark-sector evidence.

## FROZEN DECISION

Decision order is unchanged from the V0.18 preregistration.

`INVALID_INTERVENTION`: If any eligible lane fails its frozen native or masked dispatch definition, if its exact condition environment is wrong, or if paired binary identity differs, classify `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID`; no scientific promotion; diagnose only.

`INCONCLUSIVE`: If any frozen source identity/hash fails, any eligible response is non-finite, requested-node binding exceeds `1e-12`, anchor pairwise condition spread reaches `1e-5`, or any prohibited downstream object is touched, classify `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INCONCLUSIVE`; no promotion.

`UNDERPOWERED`: If fewer than three eligible exact-target/native-profile paired jobs are obtained, classify `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_UNDERPOWERED`; authorize only expanded prospective paired replication.

For an intervention condition to count as a branch-switch effect, in **every** eligible lane and on **both** replay-failure cells: (a) `NATIVE` is within `<1e-5` relative of the frozen V0.17 native branch; (b) the intervention is within `<1e-5` relative of the frozen V0.17 alternate branch; and (c) native-versus-intervention relative separation is `>=1e-5`.

- NumPy-only switches and glibc-only does not -> `NUMPY_AVX512_DISPATCH_INTERVENTION_SUPPORTED`.
- glibc-only switches and NumPy-only does not -> `GLIBC_AVX512_DISPATCH_INTERVENTION_SUPPORTED`.
- both component interventions independently switch -> `NUMPY_AND_GLIBC_AVX512_DISPATCH_INTERVENTIONS_SUPPORTED`.
- neither component alone switches but combined switches -> `COMBINED_CPU_CAPABILITY_DISPATCH_INTERVENTION_SUPPORTED_NOT_COMPONENT_ISOLATED`.
- if all validations pass but `COMBINED_NO_AVX512` remains within `<1e-5` relative of `NATIVE` on either replay-failure cell in every eligible lane -> `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_NO_EFFECT`.
- otherwise -> `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_MIXED`.

Supported intervention classifications authorize only `PROSPECTIVELY_FROZEN_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_AUDIT`.
`NO_EFFECT` authorizes only `PROSPECTIVELY_FROZEN_PROCESS_INITIALIZATION_MEMORY_LAYOUT_AUDIT`.
`MIXED` authorizes only `PROSPECTIVELY_FROZEN_CONTROLLED_DISPATCH_INTERVENTION_REPLICATION_AUDIT`.
`INVALID` authorizes validation diagnosis only; `INCONCLUSIVE` no promotion; `UNDERPOWERED` expanded prospective replication only.

## INTERPRETATION CEILING

V0.19 can establish whether prospectively controlled runtime dispatch masking causally changes the already-known numerical response branch and can localize the effect to NumPy, glibc, both, or a combined-only state. It cannot validate full Layer-B, open covariance/whitening/nuisance/relation-null, open `Wm_S3`, authorize global 65537, establish a dark-sector inference, or claim a physical signal. Even a supported causal numerical mechanism has scientific effect `+0/+0` until a separately frozen reproducibility repair and later science gate pass.
