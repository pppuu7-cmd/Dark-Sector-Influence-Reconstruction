# DSIR V0.26 R1 — consolidated prospective preregistration

Status: **PROSPECTIVELY FROZEN R1 CANDIDATE — NOT EXECUTABLE PENDING INDEPENDENT R1 AUDIT**  
Date: 2026-09-15  
Scope: DSIR F1 numerical/reproducibility only. Scientific effect remains `+0/+0`.

This R1 document prospectively consolidates the earlier split V0.26 research candidate, its alpha hardening, its route-specific tolerance correction, and the independent hosted response-blind static-audit qualifications. The older split candidate remains historical and is not mutated. R1 is the only candidate intended for promotion. No V0.26 CLASS science solve, 32-lane sentinel, or full 107-row replay is authorized by this file.

## 1. Governing authorities and ceiling

Terminal numerical/scientific parent remains:
`docs/dsir4/authority/LAYERB_BETA_V0_25_PROVENANCE_CORRECTION_V0_1.json` (git blob `20153418850f49d4c23f207787102161f0032d3c`).

Parent classification remains `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`; authorized successor remains exactly `PROSPECTIVELY_FROZEN_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_AUDIT`.

Independent qualification of the split V0.26 static candidate is:
`docs/dsir4/authority/LAYERB_BETA_V0_26_RESPONSE_BLIND_STATIC_AUDIT_QUALIFICATION_V0_1.json` (git blob `dc6075ea3582989909ea8a85abe78eb34381ff2e`), verdict `QUALIFIED`.

R1 addresses every correction required by that authority. Before any sentinel executor/workflow or science launch, R1 preregistration, R1 contract, code/input/provenance bindings and response-blind static identities must receive a separate independent R1 audit and explicit authority.

A future R1 PASS is numerical/reproducibility evidence only. It cannot open covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, statistical/model inference, physical dark-sector inference, or later Core-v1 gates.

## 2. Frozen 107-row denominator

The full replay denominator is exactly the Exp073IQ retained Layer-A object:

- retained rows: 107 exactly;
- DES: 53; BOSS: 54;
- retained-ID SHA256 `44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7`;
- full-order SHA256 `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`;
- parent run/job/artifact `34423479633 / 102703685034 / 10131794281`;
- parent artifact digest `sha256:ac959926639d3b46ecfe114e396ce03cb20a0763ef2781db454408d8ad0759df`.

No row may be selected, removed, reordered, relabelled, or replaced after any V0.26 response is read.

## 3. Frozen response-blind request geometry

Request geometry is the already frozen Exp073JL response-blind object:

- summary authority `docs/dsir4/authority/RECOVERED_EXP073JL_RESPONSE_BLIND_REQUEST_PLAN_V0_2.json`;
- materialization source run `34695347893`, successful `materialize-plan` job `103557768867` only;
- artifact `10298655751`, ZIP SHA256 `9b8bdcf03cb05bc979e8c72135acac92232864a74dc1d510b579d8efb5cbb2a7`;
- inner `plan.json`: 3,953,984 bytes, SHA256 `c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064`;
- production/coarse calls digest `9e829d5127457085f18d79901d4aa621a050ce8406ff30c4d7e157dd069b80b4`;
- fine calls digest `9f5f85e92570b68576bae91f52163cb0c005a1e003bfc09b8ccc80b332f79b36`;
- production: 441 calls, 83,666 target scalars;
- fine: 569 calls, 121,682 target scalars;
- fine prefix calls `0..440` must be bitwise identical to production calls.

The failed overall conclusion of source run `34695347893` is not relabelled; inheritance is restricted to the successful response-blind materialization job and artifact.

Frozen geometry:

- DES production calls `0..376`: 377 calls, 64,658 unique target-k values, zero target overlap between distinct DES calls, 90–244 unique target k per call;
- BOSS production GL64 calls `377..440`: 64 calls sharing one 99-unique-k target set;
- fine-only BOSS GL128 calls: 128 calls sharing that same 99-k set;
- DES and BOSS target sets have zero overlap.

## 4. Hosted NumPy-1.26.4 GRID896 identity — R1 correction

R1 does **not** define GRID896 merely as an abstract call to `np.geomspace`. The exact binary64 identity is frozen from a response-blind hosted probe under NumPy `1.26.4`:

- workflow `.github/workflows/layerb-beta-v026-r1-static-identity-probe-v0-1.yml`, git blob `0a2f42f70c3d4e8cbe2776f26dc9c5fb3a68bc23`;
- probe `ci/layerb_beta_v026_r1_static_identity_probe_v0_1.py`, git blob `5fffa2fd926eaf3d775213959039577b20b312bd`;
- run `34954905127`, job `104334496210`, terminal success;
- artifact `10390997654`, ZIP SHA256 `5cd19512bef3d9795957fb8105361e4006123ae59794bc94e2e5ded5722436ff`;
- `v026_r1_static_identity.json`: 140,697 bytes, SHA256 `3a9d8375119068063ddcb4ac37d8f3da92444261b0fad356a228ccaedf6292d7`;
- hash receipt: 104 bytes, SHA256 `5c6187a03db04888c4e3bd4f6f98befc1d67ae45a0c362fdbb320fe5dcf70f32`.

Frozen GRID896 identity:

- base n = 896; lower guards = 0; upper guards = 1; common nodes = 897;
- ratio binary64 u64hex `3ff01ddd7148e822`;
- exact common-node payload representation = contiguous little-endian IEEE-754 binary64 values in ascending order;
- payload byte length = 7,176;
- payload SHA256 = `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`;
- big-endian u64hex-lines SHA256 (one 16-hex word per line with final newline) = `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`;
- `.17g` comma-separated common-grid ASCII without terminal NUL = 19,685 bytes, SHA256 `1f706550f03b3fb13f8f3a3511a37a2f5adedb5b6114f888d91102410f193574`.

Any implementation that regenerates GRID896 must compare its exact little-endian binary64 payload SHA256 to the frozen value **before** any CLASS solve. Prefer loading a frozen exact-node representation when an audited implementation supplies one. Mismatch is `INVALID` and forbids sentinel/full execution.

## 5. Parser payload convention and exact static manifests

R1 freezes parser accounting explicitly:

`C_STRING_PAYLOAD_BYTES = len(ASCII comma-separated Python format(float(x), '.17g') values used for k_output_values) + 1 terminal NUL byte`.

Capacity values remain:

- beta k-output node capacity = 1152;
- beta parser capacity = 32768 bytes under the above convention.

The response-blind target-plan hashes remain:

- mixed target-plan canonical SHA256 `59abce49f6338c30b93d11fa462e1ff8642615d6100d23feca4b36505a5cef85`;
- direct target-plan canonical SHA256 `1c98927960e81d7fb55ebc687ef36059d964b233001551dba2aa9a01652c8864`.

Under the frozen GRID896 binary64 identity and payload convention, freeze additionally:

- complete 301-record mixed payload manifest canonical SHA256 `6b0f08b196f6afa2086a4275ec364d527c50786921ef0ca1d77a30edbed91ce6`;
- mixed maximum payload `25063` bytes at `M013`;
- complete 59-record direct payload manifest canonical SHA256 `99a6e4c48d353b05bea5000fc27417731d1c347071254232ed807554ee569da6`;
- direct maximum payload `24262` bytes at `D20`.

The superseded `25062` mixed maximum from the split candidate is not an R1 value and is forbidden as an expected scalar.

## 6. Frozen scientific/runtime state

Common identities:

- CLASS-IV commit `ac627d54e9ce196a08878d1ba33999819925d19c`;
- baseline `configs/dsir4/c2/ide0_reference_v0_1.ini`, git blob `cd2beb01ce6575f97f2e3203226ed6d4f048dcaa`;
- precision `configs/dsir4/c2/dsir_ide_p8_v0_1.pre`, git blob `fea602547cfb74e187cf9aedd5a9b0c316c626be`;
- perturbation step `h=1e-4`;
- native `k_per_decade_for_pk=20`;
- `perturb_sampling_stepsize=0.00035`;
- scientific relative threshold strict `<1e-3`;
- technical cross-host threshold strict `<1e-5`;
- requested-node coordinate binding `<=1e-12`;
- hosted runner class `ubuntu-24.04`;
- numerical software witness/pin: Python `3.12.3`, NumPy `1.26.4`, SciPy `1.17.1`;
- scientific job BLAS thread controls: `OMP_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`.

Forced NumPy runtime mask for beta sentinel/full jobs:
`NPY_DISABLE_CPU_FEATURES=AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX`.

Required forced active AVX512 dispatch is empty; required forced active non-AVX512 dispatch exactly:
`AVX,AVX2,F16C,FMA3,POPCNT,SSE41,SSE42,SSSE3`.

### Route-specific tolerance correction

The precision file itself contains `tol_perturb_integration=3e-10`. R1 freezes:

- **alpha canonical-32769 route:** inherit precision value `3e-10`; no V0.25 beta tolerance override is applied;
- **beta pure/mixed/direct exact-target route:** override `tol_perturb_integration` to exactly `1e-12`, preserving V0.25 beta-remedy semantics.

This distinction is mandatory and must be asserted before solve. Applying `1e-12` globally is INVALID. Applying `3e-10` to beta is INVALID.

## 7. Alpha route — preserve the validated canonical 32769 method

Operand-localization authority:
`docs/dsir4/authority/LAYERB_OPERAND_LOCALIZATION_DIAGNOSTIC_V0_2.json`, git blob `17666008f491ef841cb2ef511a6b5b964ccaa784`.

It established:

- alpha maximum coarse→fine relative difference `0.0006776803529834111 < 1e-3`;
- beta maximum `0.007384797439715474 > 1e-3`.

Therefore R1 remedies beta only. Alpha is not moved onto GRID896.

Alpha exact route:

- roles: reference `(alpha,beta)=(0,0)` and alpha-minus `(-h,0)`;
- response component `abs_dDelta_m_dalpha_left`;
- canonical 32769 node payload SHA256 `82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599`;
- canonical text SHA256 `7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2`;
- eight frozen slices: `[0,4097]`, `[4097,8193]`, `[8193,12289]`, `[12289,16385]`, `[16385,20481]`, `[20481,24577]`, `[24577,28673]`, `[28673,32769]`;
- per-chunk point capacity 4608; parser capacity 131072;
- all 569 response-blind calls required, including BOSS GL128 dense-z controls;
- maximum live CLASS instances per alpha acquisition job = 1;
- total alpha CLASS constructions = `2 roles * 8 chunks = 16`.

Method evidence:

- `docs/dsir4/authority/LAYERB_32769_EIGHT_CHUNK_RESPONSE_BLIND_RESOURCE_PILOT_V0_1.json`, git blob `edbb20eb798a188e88a49a6cde14d3c37c31c04c`;
- `docs/dsir4/authority/LAYERB_32769_BLINDED_PARTITION_INVARIANCE_V0_1.json`, git blob `38a0f394e8f609298d9a33ca3c007405f7f95850`, which found bitwise-identical responses between two prospectively different partitions across all tested roles/z probes.

R1 claims no alpha remedy and opens no 65537 rung.

## 8. Beta exact-target-union route

Roles are beta-plus `(0,+h)` and beta-minus `(0,-h)` only. Beta response is `abs_dDelta_m_dbeta_symmetric`.

### 8.1 Pure common control

Use exactly the frozen GRID896 binary64 object in Section 4. Pure common control constructs two beta models. Cubic interpolation from pure GRID896 is a node-set-side-effect control only and never the remedy value.

### 8.2 Mixed packing

GRID896 has 897 common nodes and leaves 255 target slots. DES target sets are pairwise disjoint and each DES call has at least 90 targets, so no three DES calls fit.

Freeze mixed packing:

1. DES calls `0..376`: form `(unique_target_count, call_index)`;
2. sort ascending by that tuple;
3. two-pointer: pair smallest remaining with largest remaining iff summed target count `<=255`, otherwise emit largest singleton;
4. sort call indices within each batch;
5. order final DES batches by `(minimum_call_index, call_index_tuple)`;
6. mixed node set is sorted exact union of frozen GRID896 binary64 nodes and all exact target k values of calls in that batch;
7. add one BOSS batch with calls `377..440` and the shared 99-k target set.

Frozen result:

- 300 DES batches = 77 pairs + 223 singletons;
- one BOSS batch;
- total 301 mixed batches `M000..M300`;
- target count range 99–255;
- requested-node range 996–1152;
- mixed target-plan SHA and payload-manifest SHA exactly as Section 5;
- beta mixed constructions = `301*2=602`.

### 8.3 Fresh direct target-only reference

DES direct packing is first-fit decreasing:

1. order calls by `(-unique_target_count, call_index)`;
2. place each whole call into first existing bin whose target union remains `<=1152`, otherwise open new bin;
3. call splitting forbidden;
4. BOSS is a separate target-only batch.

Frozen result: 58 DES + 1 BOSS = 59 direct batches `D00..D58`; direct target-plan SHA and payload-manifest SHA exactly as Section 5; beta direct constructions `59*2=118`.

Exact remedy/direct values are obtained only by exact requested-node extraction with coordinate mismatch `<=1e-12`. Cubic interpolation is forbidden for remedy/direct target values.

## 9. Full solver accounting and sharding

Frozen full-run physical CLASS construction count:

- alpha canonical 32769 = 16;
- beta pure GRID896 = 2;
- beta mixed = 602;
- beta direct = 118;
- **total = 738**.

Any different scientific construction count is INVALID absent a new prospective superseding preregistration.

Frozen response-blind sharding:

- alpha: two role jobs; each sequentially executes eight frozen chunks;
- beta mixed: 16 shards by `int(batch_id[1:]) mod 16`, batch counts `[19,19,19,19,19,19,19,19,19,19,19,19,19,18,18,18]`;
- beta direct: 4 shards by `int(batch_id[1:]) mod 4`, batch counts `[15,15,15,14]`;
- beta pure common: one job;
- shard operands never classify; one finalizer alone reassembles exact inherited call/row order and classifies.

## 10. Pre-full 32-lane sentinel — preregistered, not yet authorized

An independent R1 audit must explicitly authorize construction/launch before this sentinel may exist as an executable workflow.

If later authorized, sentinel runner is `ubuntu-24.04`, 32 lanes. Each lane verifies exact R1 software/dispatch/static identities and evaluates three response-blind selections:

- `M076`: DES calls `[76,78]`, 255 targets, 1152 mixed nodes; direct comparator `D50`, 1146 target-only nodes;
- `M298`: DES call `[375]`, 244 targets, 1141 mixed nodes; direct comparator `D00`, 1152 target-only nodes;
- `M300`: BOSS calls `[377..440]`, 99 targets, 996 mixed nodes; direct comparator `D58`, 99 target-only nodes.

Per lane: 2 pure beta + 6 mixed beta + 6 direct beta = 14 CLASS constructions.

Power gate: >=6 eligible lanes; >=3 native-AVX512-active and >=3 native-AVX512-inactive lanes; both classes required. No science retry solely to obtain favorable class mix.

Technical gates: each primitive beta response cross-host max pairwise relative spread `<1e-5`; native-class mean separation `<1e-5`.

Scientific numerical gates: every sentinel exact-vs-direct relative difference `<1e-3`; every mixed-common-vs-pure-common relative difference `<1e-3`; requested-node binding `<=1e-12`. Any invalid/underpowered/blocked sentinel forbids full replay.

## 11. Full 107-row replay predicates

Reuse exact inherited Exp073IR row traversal, geometry, active masks, coordinate IDs, ordinals, blocks and row-order hashes. `ci/exp073ir_article3_real_layerb_common_response_v0_1.py` is the semantic parent (git blob `6ef2516dfcae8a8ae92f5b7dbe792274138c0f6f`).

R1 response adapter:

- alpha column = fresh forced-baseline canonical-32769 reference/alpha-minus response with alpha `tol_perturb_integration=3e-10`;
- beta column = fresh forced-baseline exact-target-union beta-plus/beta-minus response with beta `tol_perturb_integration=1e-12`.

For every beta target scalar, including BOSS GL128 controls:

- mixed and direct target values finite;
- mixed/direct finite/nonzero status identical;
- requested-node coordinate mismatch `<=1e-12`;
- exact-target-union vs direct beta-response relative difference strict `<1e-3`;
- beta response produced by cubic interpolation of the mixed model's frozen GRID896 common-node subset vs pure frozen GRID896 beta control strict `<1e-3`.

Full row gates:

- denominator exactly 107 in inherited order and hash identities;
- zero invalid rows; retained-after-Layer-B exactly 107;
- no row-label change relative to inherited all-valid Layer-B state;
- BOSS GL64-vs-GL128 row-label disagreement false;
- every active alpha and beta atom response finite and >0;
- covariance/whitening/nuisance/relation-null/`Wm_S3` access remains false.

Historical floating-point response values are non-gating; only frozen identities and fresh R1 responses gate.

## 12. Decision hierarchy

Priority order exactly:

`INVALID -> INCONCLUSIVE -> SENTINEL_UNDERPOWERED -> SENTINEL_REPRODUCIBILITY_BLOCKED -> SENTINEL_NODE_SET_SIDE_EFFECT_BLOCKED -> SENTINEL_DIRECT_REFERENCE_BLOCKED -> FULL_NODE_SET_SIDE_EFFECT_BLOCKED -> FULL_DIRECT_REFERENCE_BLOCKED -> FULL_ROW_REPLAY_BLOCKED -> PASS`.

PASS classification exactly:
`FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_SUPPORTED`.

PASS remains `+0/+0` numerical/reproducibility evidence only and creates no automatic downstream authority.

## 13. Provenance requirements

Any later authorized implementation must preserve and bind:

- R1 preregistration, contract, executor, workflow and launch git blobs;
- terminal parent and independent R1 audit authority;
- exact source-plan artifact identities;
- exact GRID896 node identity and both target-plan/payload-manifest hashes;
- all sentinel lane artifacts and complete primitive metrics;
- alpha role operands, beta pure operand, all mixed/direct shard operands;
- exact code/input blobs, CLASS source commit, build patches, compiled `classy` hashes and runtime fingerprints;
- run/job/artifact IDs, artifact ZIP SHA256, inner filenames, byte lengths and SHA256 values;
- final complete row/atom summary and decision JSON.

Repository terminal materialization must be byte-identical to the authoritative decision artifact or explicitly labelled derived. Primitive metrics may not be omitted.

## 14. Firewalls

Forbidden before or during V0.26 R1 unless a new prospective preregistration supersedes it before response execution:

- response-informed row/target selection;
- target-local or batch construction changes after responses;
- batch repacking after responses;
- grid, h, sampling, route-specific tolerance, dispatch-mask or threshold mutation;
- use of superseded split-candidate scalar `25062` as R1 expected mixed maximum;
- silent scientific retry;
- sentinel executor/workflow construction before independent R1 audit authority;
- full replay before sentinel PASS and separate launch authorization;
- covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 or downstream physical interpretation.

R1 remains non-executable until a separate independent audit explicitly promotes this consolidated preregistration together with its immutable machine-readable contract.
