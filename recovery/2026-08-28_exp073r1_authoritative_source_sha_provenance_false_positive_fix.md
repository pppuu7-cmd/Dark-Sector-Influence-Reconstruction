# DSIR recovery checkpoint — Exp073R1 authoritative source SHA provenance fix

Date: 2026-08-28
Scope: Exp073R1 / G7 prerequisite audit

## Finding

A provenance audit found a real false-positive checksum-binding bug in the prepared Exp073R1 v0.3 path.

`docs/EXP073P2_REMAINING_DESY1_CHECKSUM_RESULT_2026-08-27.md` contains a 2026-08-28 correction establishing the authoritative SHA256 for:

`y1_source_redshift_binning_v1.fits`

as:

`491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`

The previously transcribed value:

`491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd`

is explicitly documented there as obsolete/wrong.

However, the prepared v0.3 workflow still grepped for the obsolete value and the v0.3 merger used it as `EXPECTED_SOURCE`. Because the corrected provenance note necessarily mentions the obsolete value while explaining the correction, the old `grep` could pass despite binding the wrong checksum. This was therefore a genuine false-positive provenance assertion.

## Impact

- No G7/G8/G9 science score had been evaluated through this path.
- The issue does **not** falsify the mapper or a dark-sector hypothesis.
- The issue would have made a future Exp073R1 PASS provenance statement too weak/incorrect if left unfixed.
- Exp073R1 remains a prerequisite/transport reconstruction with `G7/G8/G9 = OPEN`.

## Fixes committed

1. Added `ci/exp073r1_desy1_merge_v0_3p1.py`
   - commit `d2362b0c17aa8ebf4e7003ab6c13faf95e32396f`
   - patches only the obsolete source-object checksum constant to the authoritative Exp073P2 value;
   - mapper/merge semantics are otherwise unchanged.

2. Hardened `.github/workflows/exp073r1-desy1-low-concurrency-microshards-v0-3.yml`
   - commit `38bdf6448cb4adb1e30e9371145cdba7b4ea0879`
   - workflow display version now `v0.3p1`;
   - preflight requires the authoritative source SHA and metacal SHA;
   - merge uses `exp073r1_desy1_merge_v0_3p1.py`;
   - final assertion requires the output `input_identity_binding.source_sha256` to equal the authoritative SHA.

3. Corrected the stale/dead source SHA constant in `ci/exp073r1_desy1_shard_v0_2.py`
   - commit `ce616fb0a47c8c32409b3e1220f91a39f76a7071`.

## Remaining provenance limitation

Even after this correction, shard outputs record SHA256 values of the byte ranges actually received, but the merge does not compare those range hashes against a precomputed trusted per-range checksum manifest. The full-file SHA identity is bound independently by Exp073P2. Therefore the next full transport design should preserve the corrected authoritative file identity and, where practical, strengthen range-level identity binding without changing the preregistered science selection or mapper semantics.

## Parallel transport probe

The targeted small-range transport probe v0.4 is running as Actions run `33170454493`. At this checkpoint its probe step remains `in_progress`.

Gate state remains:

- G7: OPEN
- G8: OPEN
- G9: OPEN
