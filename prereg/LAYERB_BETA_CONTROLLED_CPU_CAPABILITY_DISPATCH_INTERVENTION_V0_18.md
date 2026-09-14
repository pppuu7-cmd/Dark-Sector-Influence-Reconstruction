# DSIR V0.18 preregistration — controlled CPU-capability dispatch intervention

Status: **PROSPECTIVELY FROZEN BEFORE V0.18 IMPLEMENTATION/EXECUTION**. Date: 2026-09-14. Scope: DSIR only.

## Parent authority

Parent terminal authority: `docs/dsir4/authority/LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_V0_17.json` (`CPU_CAPABILITY_RUNTIME_STATE_STRATIFICATION_SUPPORTED`). Parent-authorized successor exactly: `PROSPECTIVELY_FROZEN_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT`.

## HYPOTHESIS

The V0.17 response branch associated with the AVX-512-capable CPU/runtime state is causally sensitive to runtime dispatch selection rather than to immutable host identity. On the same exact AMD EPYC 9V74 host and the same built CLASS/classy binaries, prospectively forcing AVX-512 dispatch off should move both frozen replay-failure responses from the V0.17 native-capability branch toward the V0.17 alternate-capability branch while leaving the anchor stable. NumPy-only and glibc-only interventions are included prospectively to localize the component; the combined intervention is the primary causal test.

## OBJECT

Thirty-two independent GitHub-hosted jobs. Each job first fingerprints the native host without reading any substantive response. A job is scientifically eligible only if its native host is exactly `AuthenticAMD / family 25 / model 17 / stepping 1 / AMD EPYC 9V74 80-Core Processor`, native `/proc/cpuinfo` reports AVX512F, the native glibc loader exposes `x86-64-v4`, and NumPy native runtime exposes AVX512F. Ineligible jobs produce provenance-only SKIP artifacts and no response values.

Each eligible job uses one exact build of the pinned CLASS source and then executes four fresh child Python processes on that same host/binaries:

1. `NATIVE`: no dispatch override.
2. `NUMPY_NO_AVX512`: `NPY_DISABLE_CPU_FEATURES=AVX512F,AVX512CD,AVX512_KNL,AVX512_KNM,AVX512_SKX,AVX512_CLX,AVX512_CNL,AVX512_ICL`.
3. `GLIBC_NO_AVX512`: `GLIBC_TUNABLES=glibc.cpu.hwcaps=-AVX512F,-AVX512DQ,-AVX512CD,-AVX512BW,-AVX512VL`.
4. `COMBINED_NO_AVX512`: both overrides simultaneously.

Environment variables are set before the child interpreter loads NumPy/classy/glibc-dependent numerical code. The child must record NumPy CPU dispatch state and glibc loader diagnostics so the intervention itself is validated.

Technical source authority for the interventions: NumPy 1.26 CPU/SIMD runtime-dispatch documentation (`NPY_DISABLE_CPU_FEATURES`) and GNU libc hardware-capability tunables documentation (`glibc.cpu.hwcaps`). These source authorities define runtime controls only; they do not supply or alter any DSIR scientific threshold.

## FROZEN INPUTS

- CLASS commit: `ac627d54e9ce196a08878d1ba33999819925d19c`.
- Baseline: `configs/dsir4/c2/ide0_reference_v0_1.ini`.
- Production precision: `configs/dsir4/c2/dsir_ide_p8_v0_1.pre`.
- Production `h=1e-4` remains unchanged.
- Diagnostic cells remain exactly the V0.17 cells:
  - replay failure: `h=2e-4`, `z=3fdab851eb851eb8`, `k=3f890ea7bc915d36`;
  - replay failure: `h=1e-4`, `z=3fe3d70a3d70a3d7`, `k=3f8fc70971921840`;
  - anchor: `h=1e-4`, `z=3fdab851eb851eb8`, `k=3f890ea7bc915d36`.
- GRID1024 identity unchanged: base 1024, one upper guard, 1025 requested nodes.
- `tol_perturb_integration=1e-12`.
- production perturbation sampling `0.00035`.
- replay/intervention relative tolerance `<1e-5`.
- exact target binding `<=1e-12`.
- minimum scientifically eligible paired lanes: `3` independent jobs.
- V0.17 frozen branch references (not tunable after this preregistration):
  - native-capability branch: `h=2e-4 -> -0.32758589441073127`, `h=1e-4 -> 0.1355044923911919`;
  - alternate-capability branch: `h=2e-4 -> -0.32763449098638375`, `h=1e-4 -> 0.13550307244258875`.

## POSITIVE CONTROLS

- all 32 host jobs terminal and uniquely identified;
- at least 3 eligible exact-target AVX512-native jobs;
- same CLASS/classy and numerical-library hashes for all four conditions within each eligible job;
- native condition validates AVX512F in `/proc/cpuinfo`, glibc x86-64-v4 active, and NumPy AVX512F active;
- NumPy-mask conditions validate AVX512 dispatch disabled in NumPy runtime state;
- glibc-mask conditions validate x86-64-v4 no longer active in the glibc loader diagnostics;
- all responses finite;
- exact requested-node coordinate mismatch `<=1e-12`;
- anchor native/intervention pairwise spread `<1e-5` within every eligible job;
- no production h/sampling/tolerance mutation.

## NEGATIVE CONTROLS

- ineligible hosts cannot enter the scientific classifier;
- `/proc/cpuinfo` physical AVX512 flag itself is not expected to change under dispatch masking and is not used as proof the intervention worked;
- job/runner IDs, PIDs, addresses and timing are forbidden classifiers;
- branch closeness is evaluated only against the frozen V0.17 branch references above;
- green CI is not scientific PASS;
- an intervention effect is a numerical-runtime mechanism result, not Layer-B validation and not dark-sector evidence.

## FROZEN DECISION

`INVALID_INTERVENTION`: If the native or masked dispatch validation does not match the frozen condition definition, or within-job binaries differ across conditions, classify `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID`; no scientific promotion.

`INCONCLUSIVE`: If any frozen identity/hash fails, any eligible response is non-finite, exact binding exceeds `1e-12`, anchor pairwise spread reaches `1e-5`, or any prohibited downstream object is touched, classify `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INCONCLUSIVE`; no promotion.

`UNDERPOWERED`: If fewer than three eligible exact-target AVX512-native paired jobs are obtained, classify `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_UNDERPOWERED`; authorize only expanded prospective paired replication.

For an intervention condition to count as a branch-switch effect, in **every** eligible lane and on **both** replay-failure cells: (a) `NATIVE` is within `<1e-5` relative of the frozen V0.17 native branch; (b) the intervention is within `<1e-5` relative of the frozen V0.17 alternate branch; and (c) native-versus-intervention relative separation is `>=1e-5`.

- If `NUMPY_NO_AVX512` satisfies branch-switch effect and `GLIBC_NO_AVX512` does not, classify `NUMPY_AVX512_DISPATCH_INTERVENTION_SUPPORTED`.
- If `GLIBC_NO_AVX512` satisfies branch-switch effect and `NUMPY_NO_AVX512` does not, classify `GLIBC_AVX512_DISPATCH_INTERVENTION_SUPPORTED`.
- If both component interventions independently satisfy branch-switch effect, classify `NUMPY_AND_GLIBC_AVX512_DISPATCH_INTERVENTIONS_SUPPORTED`.
- If neither component alone satisfies branch-switch effect but `COMBINED_NO_AVX512` does, classify `COMBINED_CPU_CAPABILITY_DISPATCH_INTERVENTION_SUPPORTED_NOT_COMPONENT_ISOLATED`.
- If all intervention validations pass but `COMBINED_NO_AVX512` remains within `<1e-5` of `NATIVE` on either replay-failure cell in every eligible lane, classify `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_NO_EFFECT`.
- Otherwise classify `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_MIXED`.

Any supported intervention classification authorizes only `PROSPECTIVELY_FROZEN_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_AUDIT`. `NO_EFFECT` authorizes only `PROSPECTIVELY_FROZEN_PROCESS_INITIALIZATION_MEMORY_LAYOUT_AUDIT`. `MIXED` authorizes only `PROSPECTIVELY_FROZEN_CONTROLLED_DISPATCH_INTERVENTION_REPLICATION_AUDIT`.

## INTERPRETATION CEILING

V0.18 can establish whether prospectively controlled runtime dispatch masking causally changes the already-known numerical response branch and can localize that effect to NumPy, glibc, both, or a combined-only state. It cannot validate full Layer-B, open covariance/whitening/nuisance/relation-null, open `Wm_S3`, authorize global 65537, establish dark-sector inference, or claim any physical signal. Even a causal numerical mechanism changes scientific effect by `+0/+0` until a separately frozen reproducibility repair and subsequent science gate pass.
