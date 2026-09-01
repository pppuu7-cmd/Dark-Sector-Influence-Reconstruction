# 2026-09-01 — Exp073CC corrected-lifetime PCL QA terminal Q1 PASS

## Authority state

- Exp073BJ remains terminal Track-A exact Wm_S1 authority PASS.
- Exp073AQ remains permanent historical exact-repeatability scientific FAIL.
- Exp073BD remains provisional/incomplete and forbidden downstream.
- Exp073BV source-lineage PASS, Exp073BW exact streaming-equivalence PASS, and Exp073BZ checkpoint/failover PASS remain preserved.
- Article-3 readiness remains **Verified 52.0% | Draft/data 53.7%**.
- Exp073CC is synthetic/nonclassifying infrastructure QA and is always `+0/+0`.

## Actions coordination state

Immediately before recording this result, GitHub Actions reported zero `in_progress` DSIR runs and exactly one queued run: Exp073CA attempt3 run `33448843621`. Its replica B remains queued self-hosted and is not to be revived overnight. The home runner remains **OFFLINE/LOCKED**.

No self-hosted workload, rerun, WSL change, or Exp073CA successor was started.

## Frozen Exp073CC lineage

- preregistration commit: `f451a272bfa060441a523334c48edae20ffa8603`
- helper commit: `583770e3607edb9f0d8168f68e89015c7913205d`
- workflow commit: `c1c44deca56423caa54f61cd8ea70575ea23f02f`
- binding commit: `377bb66f79fe598c8f0b10248bda3c1fb7104a45`
- trigger/head commit: `1622efc76f02876de1871123938d07936fe40cb6`
- hosted run: `33475627726`
- hosted job: `99754170638`
- immutable artifact: `9788075152`
- artifact digest: `sha256:08b0e29e93e9eddaabe7f23de618a7a68b152b2115eb0e1727d7f3d0af8de5d9`

## Frozen classification

The immutable artifact receipt and exact comparator both classify the run as:

**`CC_Q1_EXACT_EQUIVALENCE_PASS`**

All three prospectively frozen cases were complete, finite, `np.array_equal == true`, and canonical `<f8` SHA-256 equal:

| NSIDE | shape | exact SHA-256 (simultaneous = sequential) |
|---:|---:|---|
| 64 | `[192]` | `451f7ca38df2e533468d17b1cf7cecb449f58cc9713652d605393a5359a745d5` |
| 128 | `[384]` | `eeb8e5041d42e39bffe4d807421623c4f963d7058a1140cbb7d27518f8c7b47e` |
| 256 | `[768]` | `7989e075acea10cd62abc3ec26530fa4b006c77212121c058ee51c3344f9c707` |

No tolerance, ULP, rounding, averaging, smoothing, majority vote, or preferred-replica rescue was used.

## RSS receipt — nonclassifying diagnostic

Independent-process `/usr/bin/time -v` measurements were:

| NSIDE | simultaneous max RSS KiB | corrected sequential max RSS KiB | sequential/simultaneous |
|---:|---:|---:|---:|
| 64 | 117652 | 116392 | 0.9892904498 |
| 128 | 130908 | 125888 | 0.9616524582 |
| 256 | 183124 | 164204 | 0.8966820297 |

Thus the corrected sequential lifetime reduced measured peak RSS in every frozen hosted case, with the largest observed reduction at NSIDE=256 (about 10.33%). RSS was diagnostic only and was not an acceptance threshold.

This hosted small/medium-geometry result does **not** establish that full DES NSIDE=4096 fits under the user's 6 GiB WSL cap. It only establishes exact output equivalence for the corrected lifetime construction on the frozen hosted cases and provides directional memory evidence. Full-scale peak SHT workspace remains unmeasured.

## Consequence for the overnight frontier

Exp073CC Q1 removes the implementation-equivalence objection to a future prospectively frozen production memory-lifetime repair: the source maps/fields may be constructed sequentially while preserving exact PCL output in the tested frozen geometries.

It does **not** authorize any overnight home-runner execution. Exp073CA attempt3 remains infrastructure incomplete, and its queued self-hosted replica B remains untouched. No real-survey gate is closed by Exp073CC.

## Exact next gate

While the home runner remains locked, the highest-value permitted work is a read-only/full-scale memory-budget and source-lifetime audit for the production NSIDE=4096 path, including conservative accounting for NaMaster/healpy SHT workspaces and an explicit minimum safe WSL/RSS margin. If a hosted-only synthetic scaling probe can be prospectively frozen without duplicating an already-closed gate, it may refine workspace scaling, but it cannot substitute for full-scale home execution.

Only after the user explicitly re-enables the home runner may a separately prospectively frozen Exp073CA infrastructure successor use the exact-equivalent sequential lifetime repair. Any such successor must preserve frozen scientific inputs/comparators/thread policy/checkpoint semantics and the <=60 s nonclassifying heartbeat rule.
