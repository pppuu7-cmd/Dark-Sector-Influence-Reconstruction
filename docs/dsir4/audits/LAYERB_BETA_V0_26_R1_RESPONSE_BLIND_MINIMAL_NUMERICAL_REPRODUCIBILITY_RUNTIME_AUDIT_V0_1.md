# DSIR Funnel Auditor — minimal numerical reproducibility runtime audit V0.1

Date: 2026-09-18. Scope: **DSIR only**. GitHub repository/Actions and immutable GitHub Actions artifacts are the sole durable scientific source of truth.

Reviewed launch head: `6ba39aeade5b0603c02ea3d0fc7f8167c11c240a`.
Reviewed run: `35280281867`, workflow `360911210`, run #1 / attempt #1, terminal `success`.

## Result reviewed

Frozen aggregate artifact `10523772312` reports `PASS_SCOPED_MINIMAL_NUMERICAL_REPRODUCIBILITY_QUALIFIED`. This audit does not treat green CI as scientific evidence; it independently checks authorization, chronology, exact implementation identities, immutable artifacts, raw-witness recomputation, numerical controls, and interpretation ceiling.

## Authorization / chronology

The chain is prospective and ordered:

1. design authority commit `106563b3ee7b31ed6ac25bc8c6606f481cf93aa0`, blob `b09d4f7de24974d7b8052e4b130c8902a57cf68b`;
2. independent design static Critic commit `718697e5a4388604ebbafe6b4a3ce5642569b2d6`, blob `5f4682a3f691b7b533237389ceac10162e8aa721`, PASS_SCOPED;
3. base implementation commit `219a76421c4b3821586eefd6be2c920e7468e08b`, blob `ca4307962c0e92dd4bf5d74e76dd4e6db27c10d1`;
4. audited orchestrator commit `3656fb2aa1e74cf87feb97690d2ce08e17620a1c`, blob `f12ae302f7dce44cac93791f39a4f3e0a29d7d28`;
5. workflow commit `2d181400a16cae1dfafbe6f4f0aede482c21cbf7`, blob `2c47d859741e9b4f13c8e044046f3169e163a1b6`;
6. one-shot execution authority commit `81c6b2fe860d513ddd46c2384256e56238ca7aea`, blob `83eeb4ed967206329edd90d4efe5c349f4311281`;
7. independent implementation static Critic commit `902c9762aeb8e8985b210cfb1a4981860fb03d75`, blob `1f75d64be53e21731ddd7700f7ebf02fccb7e7ef`, PASS_SCOPED;
8. later marker-only launch commit `6ba39aeade5b0603c02ea3d0fc7f8167c11c240a`.

The launch commit changes only `docs/dsir4/launch/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_MINIMAL_NUMERICAL_REPRODUCIBILITY_V0_1.launch.json`. Its marker binds the authority, Critic, base executor, orchestrator and workflow blobs. The run itself is exactly run #1 / attempt #1. An exact-head Actions query returns exactly one run. No rerun/attempt selection or favorable-result retry exists for this identity.

## Frozen object and thresholds

The gate remains bound to V0.26 R1 prereg blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`, plus the terminal corrected-producer population authority `6ce9d30e36ea6627b21fcba1e0e886adfef89765` and runtime Critic `4b990b4b55eed93a2b891470d616a8a133998ce1`.

Frozen numerical identity is unchanged: Python 3.12.3, NumPy 1.26.4, SciPy 1.17.1, CLASS commit `ac627d54e9ce196a08878d1ba33999819925d19c`, beta h=1e-4, `tol_perturb_integration=1e-12`, corrected GRID896 payload SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`, requested-node binding <=1e-12, and the **technical** reproducibility classifier strictly <1e-5. The scientific 1e-3 threshold is explicitly not used.

The 32-lane population and two preregistered execution-order arms are unchanged. Each eligible lane executes exactly 14 beta CLASS constructions: pure beta +/-; M076/M298/M300 beta +/-; D50/D00/D58 beta +/-. No alpha route or full replay is executed.

## Jobs and required lanes

The terminal run contains 34 jobs: one invariant job, all numerical lanes R01..R32, and one aggregate decision job. Every job is terminal success. The matrix is fail-fast false and each lane creates a fallback receipt before heavy setup and uploads its immutable artifact with `always()`.

There are 34 unexpired run artifacts: one invariant bundle, exactly 32 uniquely named lane artifacts, and one decision artifact. No lane is missing.

## Artifact provenance

Decision artifact `10523772312` has GitHub digest / independently downloaded ZIP SHA256:

`24c5901c1cd31e44a8d882672d542a5361e98a9be0cf7a6133b08fff9fcb76ff`.

Its ZIP contains exactly `result.json`. Inner `result.json` SHA256 is:

`aaf10366106bbcefdd7b0569b182d56aa8f70e7462822893a8692350a8a6c93e`.

All 32 lane artifacts were independently downloaded. Each downloaded outer ZIP SHA256 matches its GitHub Actions digest. Each ZIP contains exactly its corresponding `receipt_Rxx.json` and `witness_Rxx.npz`. For every lane, the receipt's `solver_receipt.witness_npz_sha256` equals the independently hashed witness bytes.

The invariant artifact is `10522366691`, GitHub digest `sha256:74a1694ebe774641ca5585cd8612aa9c3cd1d68a2bb807ea4ec67269a2fa0df9`.

## Independent raw-witness recomputation

I independently recomputed the aggregate numerical metrics from the 32 downloaded lane artifacts rather than trusting `result.json`.

Population:
- 32/32 receipts present and `LANE_PASS`;
- 32/32 eligible;
- native classes: 10 `NATIVE_AVX512_ACTIVE` + 22 `NATIVE_AVX512_INACTIVE`;
- order arms: 16 A + 16 B;
- each receipt binds 14 constructions, max live CLASS instances 1, corrected GRID896 SHA `8499...`, and all science/covariance/classifier flags false;
- every witness member set is identical across lanes and contains 536 raw arrays.

Independent metrics exactly reproduce the frozen decision:
- cross-host same-logical-operand max pairwise relative spread = `0.0`;
- native-class mean relative separation = `7.215823672842194e-16`, argmax `mixed_common__M300__beta_plus__call393`;
- execution-order-arm mean relative separation = `0.0`;
- mixed-vs-direct exact-target raw-value relative difference = `0.0`;
- mixed-common-vs-pure-common raw-value relative difference = `0.0`;
- maximum requested-node coordinate relative mismatch = `1.6568353692813133e-16`.

All are within the prospectively frozen numerical criteria; the binding metric is also far below <=1e-12.

The raw witness NPZ identity itself forms two deterministic serialization identities, one per frozen execution arm: all 16 arm-A witnesses share SHA256 `1fc65ef247109ef606eb6431811dad54827575cb51ae779fc78a8bbe76640ae3`, and all 16 arm-B witnesses share SHA256 `9e910416a40efb9330b89c1dd4baaad07d750064a9c497fd1656c95262e33cf3`. This difference is container/member ordering from reversed construction order, not a raw-value discrepancy: independent key-wise comparison gives zero order-arm relative separation.

## Counterexample search

- **Interpolation / grid artifact:** the gate consumes the exact corrected content-addressed GRID896 payload and checks exact mixed/direct and common/pure raw requested-node values. No observed numerical discrepancy survives these controls.
- **Solver tolerance artifact:** beta `tol_perturb_integration` is prospectively frozen at 1e-12 and the implementation rejects 3e-10 inheritance. No post-result tolerance change exists.
- **Execution-order / state dependence:** A and exact reverse-B orders were frozen before execution; independent raw-value recomputation yields order-arm separation 0.0. The solver lifecycle enforces at most one live CLASS instance.
- **Native dispatch dependence:** native host class is fingerprinted in a separate clean process, while the solver uses the frozen forced mask before NumPy import. Both native classes are powered and raw solver witnesses agree.
- **Serialization artifact:** every lane verifies reload bitwise identity and SHA identity; the independent audit also verifies receipt-to-witness SHA binding.
- **Selection / look-elsewhere:** R01..R32, class-power minima, selected M/D batches, two order arms, metrics, and thresholds were all frozen before the one-shot run. No retry or posthoc lane replacement occurred.
- **Technical-vs-scientific threshold substitution:** the gate intentionally uses only the frozen technical <1e-5 criterion. It does not claim or test the scientific <1e-3 response criterion.
- **Nuisance/covariance/systematics:** not evaluated here and cannot be inferred from this numerical gate.

No explicit numerical or provenance counterexample to the frozen result was found.

## Interpretation ceiling

The result establishes only scoped numerical reproducibility of the frozen beta exact-target raw numerical path on this preregistered 32-lane hosted sample, under the frozen forced solver-dispatch/runtime/order/serialization conditions.

It does **not** establish a scientific beta response, exact scientific-threshold PASS, full 107-row validity, covariance/whitening validity, nuisance removal, relation-null validity, statistical/model validity, identifiability, systematic exclusion, or physical dark-sector evidence.

## Verdict

`CONFIRMED_SCOPED`.

The exact terminal classification `PASS_SCOPED_MINIMAL_NUMERICAL_REPRODUCIBILITY_QUALIFIED` is independently confirmed only at the numerical/reproducibility layer. Scientific effect remains `+0/+0`.

The run identity `35280281867` is consumed. Same-identity rerun/retry is forbidden.

A separate **design-only** minimal scientific response gate may now be authored prospectively because the frozen execution authority explicitly allows that next step only after terminal runtime Critic closure. No scientific execution is authorized by this audit, and full107 plus all downstream gates remain closed.
