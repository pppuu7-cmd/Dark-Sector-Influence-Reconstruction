# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-02  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance/static/diagnostic QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-02_exp073cf_continuation_successor_terminal_finalizer_exact_fail.md`
2. `preregistration/2026-09-02_exp073cg_finalizer_cross_host_determinism_v0_1.md`
3. `experiments/073cg_finalizer_cross_host_determinism_v0_1_binding.json`
4. `ci/exp073cg_finalizer_determinism_v0_1.py`
5. `.github/workflows/exp073cg-finalizer-cross-host-determinism-v0-1.yml`
6. `recovery/2026-09-02_exp073cf_continuation_activation_final_audit_pass.md`
7. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current scientific frontier — Exp073CF terminal

Exp073CF continuation successor run `33601943300`, head `313a8b332dc982154eb14671e68ada9ebd2c10e5`, reached complete A/B authority inputs.

Replica A job `100157400671` and replica B job `100157400821` both completed all 39/39 bands successfully on `DSIR-HOME-PC`.

The full-scale compact A/B comparator is an exact scoped PASS:

- job `100260974130`;
- canonical shape `[39,12288]`;
- `array_equal=true`;
- PCL SHA A=B `4d5516c56aa48b2b169512bb61a0b09ded6982249b4af41677eeac49298fca84`;
- compact SHA A=B `963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd`;
- token `PASS_EXP073CF_WM_S2_COMPACT_EXACT_V0_1`;
- authority artifact `9848084775`, digest `sha256:29ac6e91f703734cfffcbffd1504fda9c861aa12dcb88822b83af50842983dd2`.

The frozen independent finalizer exact comparator is a scientific repeatability FAIL:

- finalizer A job `100261101481`, final artifact `9848151035`, digest `sha256:51c89b5ebbb06138f29b51a7b871f9519aff6c9e72475825e2082610d77eef17`, window SHA `fc94c71f8e004fe3340d7ab3df79a70b93d0236902e7f8d72f7387c33829de84`;
- finalizer B job `100261101527`, final artifact `9848148422`, digest `sha256:a124bd9c796b152cf2536f10ecdaaa2eeb67254f6f80e46aed13adb48f65a1d7`, window SHA `bed762740b625f932f016d0988be17500a2583daee08bee9a5da550de786193e`;
- final exact comparator job `100261645358`;
- `array_equal=false`, `sha_equal=false`, `scientific_authority=false`, no tolerance;
- terminal token `SCIENTIFIC_REPEATABILITY_FAIL_EXP073CF_WM_S2_FINALIZER_EXACT_V0_1`;
- final authority artifact `9848162380`, digest `sha256:f291447e109b2149958114baa30baf37edb6aa75efe9c2b41498d88fe4e193a1`.

The green GitHub workflow conclusion does not override the scientific comparator payload. Exp073CF's finalizer exact FAIL is permanent historical authority. No tolerance/ULP/rounding/averaging/preferred-replica rescue is allowed.

## Current diagnostic frontier — Exp073CG

Exp073CG is a prospectively preregistered hosted-only numerical determinism diagnostic, `+0/+0`. It cannot change Exp073CF's classification.

Frozen components:

- prereg commit `c5ae972cc66e13ff9654988fe10a57bb5019a746`;
- helper commit `4e81313382f993b9ab7d4414fe4d650ddee83867`;
- workflow commit `c06e91ae51832a7d30d2903be2d1baedc21e87c8`;
- binding commit `ce04e90be14a829bc9c2b5a60b094015b56ec24b`;
- trigger/head commit `6b6f85ee611c8fd0b8cde455ab349dd9fcd38b0c`;
- run `33635554899`.

Exp073CG uses the immutable Exp073CF compact-A artifact `9841348367` and exact compact content SHA `963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd`. Four independent GitHub-hosted Ubuntu workers test exact K construction, repeated same-process solves, fresh-process solves and cross-host solves while capturing CPU/NumPy/OpenBLAS runtime. The home runner is not used.

Preregistered diagnostic outcomes distinguish:

- K construction nondeterminism;
- within-worker solve nondeterminism;
- cross-host BLAS/LAPACK solve nondeterminism;
- exact cross-host stability not reproducing the original mismatch.

Every outcome remains diagnostic/nonclassifying `+0/+0`.

## Preserved scientific authority

- **Exp073BJ** run `33379013167`: Track-A exact Wm_S1 authority PASS; artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- **Exp073AQ**: permanent historical exact-repeatability scientific FAIL.
- **Exp073BD**: `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, forbidden downstream.
- **Exp073BV** source-lineage PASS; **Exp073BW** exact streaming-equivalence PASS; **Exp073BZ** checkpoint/failover PASS.
- **Exp073CC/CD/CE**: synthetic/nonclassifying, `+0/+0`.
- **Exp073CF attempt1/attempt2**: infrastructure incomplete, `+0/+0`.
- **Exp073CF continuation successor**: compact exact scoped PASS; finalizer exact scientific repeatability FAIL.

## Frozen Article-3 order/boundaries

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order: `validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`. No G8 jump.

## Exact next gate

Consume run `33635554899` when terminal. Do not rerun Exp073CF full-scale compact A/B: its exact compact repeatability is already established.

If Exp073CG isolates numerical solve nondeterminism, the next permitted scientific-engineering step is a **new prospectively versioned deterministic finalizer**, preregistered before execution and validated against the immutable compact authority. It may establish a new version's repeatability but may never rewrite Exp073CF's historical FAIL.

No self-hosted heavy work is authorized for the Exp073CG diagnosis.

- ✅ A/B full-scale compact exact repeatability established.
- ❌ Exp073CF frozen finalizer exact repeatability failed.
- 🟡 Exp073CG hosted-only determinism diagnosis active/dispatched.
- ❌ G7/G8 remain unauthorized.

**Home runner = FREE for DSIR frontier diagnosis. Verified: 52.0% | Draft/data: 53.7% | readiness delta +0/+0.**
