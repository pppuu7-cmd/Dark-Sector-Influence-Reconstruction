# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-01  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-01_exp073cd_q1_spill_reload_exact_equivalence_pass.md`
2. `recovery/2026-09-01_exp073cc_fullscale_memory_budget_audit.md`
3. `recovery/2026-09-01_exp073cc_q1_corrected_lifetime_exact_equivalence_pass.md`
4. `recovery/2026-09-01_exp073cb_helper_rss_semantics_audit.md`
5. `recovery/2026-09-01_exp073ca_attempt3_infra_incomplete_exp073cb_hosted_memory_qa_active.md`
6. `recovery/2026-09-01_exp073bz_remote_checkpoint_failover_pass.md`
7. `recovery/2026-08-31_exp073bv_q1_exp073bw_q1_streaming_equivalence_terminal.md`
8. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
9. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
10. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current overnight frontier

- Home runner is **OFFLINE/LOCKED** until the user explicitly re-enables it.
- Exp073CA attempt3 run `33448843621`: replica A job `99673921219` terminal infrastructure failure during fresh Wm_S2 PCL; replica B job `99673921530` remains queued self-hosted and must not be revived overnight.
- Frozen Exp073CA classification remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`.
- Compile, checkpoint preflight/restore, heavy 39-band streaming, exact compact comparator and finalizer did not run in replica A.
- Current coordination check: zero `in_progress` DSIR runs; Exp073CA attempt3 is the sole queued run.

## Exp073CD terminal first-mask-ALM spill/reload QA

Prospectively frozen hosted-only synthetic/nonclassifying QA. Frozen lineage:
- prereg `1017d46081c030427dc111d42bc0a7e89ddd4b3f`;
- helper `bdcd1d8be90c0e47377cd49d823d2f9cf31b4ef1`;
- workflow `c6a44c295409a5f2a5d1e16390a62af0299dd22f`;
- binding `1be90b332e8505771f0752ebb40c09d8ec3f489c`;
- trigger/head `ad10dad8c78b9931d78d21c446993fdcf03ab0a1`.

Hosted run `33495127089`, job `99815424166` is terminal. Immutable artifact `9795414546`, digest `sha256:9c88bb95c796e4a0220856f93574e14aa1873dbcd00b714c2e37693edfa5c069`.

Frozen classification: **`CD_Q1_SPILL_RELOAD_EXACT_EQUIVALENCE_PASS`**.

For every frozen `NSIDE={64,128,256}` case, canonical `<c16>` first-mask ALM saved/reloaded SHA-256 was exactly identical, and the final spill/reload PCL passed both `np.array_equal` and canonical `<f8` SHA equality against the corrected-sequential oracle. Shared final PCL SHAs were:
- NSIDE 64: `451f7ca38df2e533468d17b1cf7cecb449f58cc9713652d605393a5359a745d5`;
- NSIDE 128: `eeb8e5041d42e39bffe4d807421623c4f963d7058a1140cbb7d27518f8c7b47e`;
- NSIDE 256: `7989e075acea10cd62abc3ec26530fa4b006c77212121c058ee51c3344f9c707`.

Independent-process RSS oracle -> spill/reload was 116260 -> 116456 KiB (NSIDE64), 125832 -> 125712 KiB (128), and 164264 -> 164336 KiB (256). RSS is diagnostic only and shows no material small/medium-geometry reduction; do not extrapolate it to full DES memory safety. Exp073CD is `+0/+0` and closes no real-survey/scientific gate.

## Exp073CC and full-scale memory audit

Exp073CC run `33475627726`, job `99754170638`, immutable artifact `9788075152`, digest `sha256:08b0e29e93e9eddaabe7f23de618a7a68b152b2115eb0e1727d7f3d0af8de5d9` remains **`CC_Q1_EXACT_EQUIVALENCE_PASS`**: corrected one-target-at-a-time PCL is exactly identical to simultaneous oracle on frozen NSIDE 64/128/256.

For DES `NSIDE=4096`, `NPIX=201,326,592`: one float64 map is 1.500 GiB; one complex128 mask-alm through ell=12287 is about 1.12509 GiB. The current simultaneous lifetime is already about **8.25018 GiB** persistent payload before SHT workspace/process overhead, structurally unsafe under the 6 GiB WSL cap. Corrected sequential lifetime lowers the worst deterministic persistent baseline to about **4.12509 GiB** before SHT workspace. The Exp073CD-supported first-ALM spill design can remove the retained first ALM from the second-SHT phase, giving a prospective deterministic second-SHT baseline near **2.62509 GiB** plus workspace/resident mmap pages. Full-scale safety remains unproven until a future production integration and full-scale infrastructure execution are prospectively controlled.

## Exp073CB terminal/helper audit

Exp073CB run `33464547851`, job `99721585397` remains `CB_Q3_INFRASTRUCTURE_INCOMPLETE`, `+0/+0`: PyPI had no `pymaster==2.7`, so numerical/comparator/RSS stages never ran. Its frozen helper cannot support RSS evidence because `_` retained the unwanted companion mask. Do not reuse that helper as memory evidence.

## Preserved scientific authority

- **Exp073BJ** run `33379013167`: terminal Track-A exact Wm_S1 authority PASS; artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- **Exp073AQ**: permanent historical hosted exact-repeatability scientific FAIL.
- **Exp073BD**: `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, forbidden downstream.
- **Exp073BV**: `BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED`, artifact `9768866582`.
- **Exp073BW**: `BW_Q1_FULL_AND_STREAM_COMPRESSED_EXACT_EQUIVALENCE_PASS`, artifact `9774112002`.
- **Exp073BZ**: remote checkpoint/failover exact-byte PASS, artifact `9776592370`.

No tolerance, ULP, rounding, averaging, smoothing, majority vote or preferred-replica rescue is permitted.

## Frozen Article-3 boundaries and order

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No G8 jump.

## Exact next gate

While home runner remains locked, do not touch or revive Exp073CA replica B. After Exp073CD Q1, the highest-value permitted work is a **repository-side production integration audit** for a future memory-stable Wm_S2 infrastructure successor: bind exact insertion/deletion points for first-mask-ALM spill/reload in the production PCL path; preserve dtype/order/indexing and unchanged `hp.alm2cl`; specify immutable SHA verification, local-disk capacity, atomic write/rename, cleanup/failure/checkpoint semantics, and <=60 s heartbeat behavior. Any additional hosted QA must be prospectively frozen, synthetic/nonclassifying, and `+0/+0`.

Only after the user explicitly re-enables the home runner may a separately prospectively frozen Exp073CA infrastructure successor use the Exp073CC/Exp073CD-supported memory-lifetime repairs. Scientific inputs, comparators, thread policy, checkpoint semantics, and frozen criteria must remain unchanged.

- ✅ Exp073CD = `CD_Q1_SPILL_RELOAD_EXACT_EQUIVALENCE_PASS`; immutable artifact `9795414546`.
- ✅ Exp073CC = `CC_Q1_EXACT_EQUIVALENCE_PASS`; immutable artifact `9788075152`.
- ✅ Exp073BJ exact Track-A Wm_S1 authority PASS preserved.
- ✅ Exp073BV/BW/BZ prerequisite authority preserved.
- 🟡 Exp073CA remains infrastructure incomplete; self-hosted replica B queued but locked out.
- ❌ Exp073AQ permanent historical scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Verified: 52.0% | Draft/data: 53.7%**
