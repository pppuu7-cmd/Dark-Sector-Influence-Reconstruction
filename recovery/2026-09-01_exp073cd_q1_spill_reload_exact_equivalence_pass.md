# Exp073CD — first-mask-ALM spill/reload exact-equivalence PASS

**Date:** 2026-09-01  
**Scope:** hosted-only synthetic/nonclassifying infrastructure QA; Article-3 readiness delta `+0/+0`.

## Frozen lineage

- prereg: `1017d46081c030427dc111d42bc0a7e89ddd4b3f`
- helper: `bdcd1d8be90c0e47377cd49d823d2f9cf31b4ef1`
- workflow: `c6a44c295409a5f2a5d1e16390a62af0299dd22f`
- binding: `1be90b332e8505771f0752ebb40c09d8ec3f489c`
- trigger/head: `ad10dad8c78b9931d78d21c446993fdcf03ab0a1`
- hosted run: `33495127089`
- job: `99815424166`
- immutable artifact: `9795414546`
- artifact digest: `sha256:9c88bb95c796e4a0220856f93574e14aa1873dbcd00b714c2e37693edfa5c069`

## Frozen terminal classification

**`CD_Q1_SPILL_RELOAD_EXACT_EQUIVALENCE_PASS`**

The frozen receipt reports `verified_delta=0.0`, `draft_data_delta=0.0`, `science_gate_scored=false`.

## Exact identity evidence

For each frozen `NSIDE={64,128,256}` case, the first mask ALM was canonicalized as `<c16>`, written to storage, SHA-256 recorded, released, then reopened read-only for the unchanged final `hp.alm2cl` path. All cases passed both the ALM-byte identity requirement and the final PCL exact comparator.

- NSIDE 64: saved/reloaded ALM SHA `88629866c0ff3b631cb824c0faf8599c18c9fd959756247520852b97f0658256`; oracle/spill PCL SHA `451f7ca38df2e533468d17b1cf7cecb449f58cc9713652d605393a5359a745d5`; `alm_exact_identity=true`, `np.array_equal=true`.
- NSIDE 128: saved/reloaded ALM SHA `1b26cc12aa36b17447636da2dd1ba0fed087c22bde02f2baae992bc28bc28ae6`; oracle/spill PCL SHA `eeb8e5041d42e39bffe4d807421623c4f963d7058a1140cbb7d27518f8c7b47e`; `alm_exact_identity=true`, `np.array_equal=true`.
- NSIDE 256: saved/reloaded ALM SHA `66cf2772de65e74140b3c593218b799407a918ee47b39dd85545065048184ebc`; oracle/spill PCL SHA `7989e075acea10cd62abc3ec26530fa4b006c77212121c058ee51c3344f9c707`; `alm_exact_identity=true`, `np.array_equal=true`.

No tolerance, ULP, rounding, averaging, smoothing, majority vote, or preferred-replica rescue was used.

## RSS diagnostic

Independent-process maximum RSS from the immutable receipt:

- NSIDE 64: corrected-sequential oracle `116260 KiB`; spill/reload `116456 KiB` (`1.0016859x`).
- NSIDE 128: oracle `125832 KiB`; spill/reload `125712 KiB` (`0.9990463x`).
- NSIDE 256: oracle `164264 KiB`; spill/reload `164336 KiB` (`1.0004383x`).

These small/medium hosted RSS values are diagnostic only. They show no material RSS reduction at these geometries, where fixed interpreter/library/SHT overhead dominates. They must not be extrapolated into a claim that DES `NSIDE=4096` fits under the 6 GiB WSL cap.

## Interpretation

Exp073CD removes the exact-byte-equivalence objection to a future prospectively frozen first-mask-ALM spill/reload implementation. Together with Exp073CC, it establishes on the frozen hosted geometries that both (1) one-target-at-a-time lifetime and (2) canonical first-ALM storage/reload can preserve the exact PCL output.

This does **not** authorize any real-survey Wm_S2 scientific classification and does **not** authorize the home runner overnight. Exp073CA attempt3 remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`, and its queued self-hosted replica B must remain dormant.

## Next scientifically permitted gate while home runner is locked

Do not run full-scale Wm_S2. Perform a repository-side production-integration audit for a future memory-stable successor: identify exact production insertion/deletion points for first-ALM spill/reload, prove that file serialization/mmap does not alter dtype/order/indexing, specify disk-space/failure/checkpoint cleanup semantics, and preserve the <=60 s heartbeat contract. If a hosted QA is later needed, it must be prospectively frozen and remain synthetic/nonclassifying.

**Authority unchanged:** Exp073BJ PASS; Exp073AQ permanent scientific FAIL; Exp073BD no-downstream; Exp073BV/BW/BZ PASS.  
**Article-3 readiness unchanged:** **Verified 52.0% | Draft/data 53.7%**.  
**Home runner:** **OFFLINE/LOCKED**.
