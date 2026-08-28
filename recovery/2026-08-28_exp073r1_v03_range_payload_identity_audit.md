# Exp073R1 v0.3 range-payload identity audit — 2026-08-28

## Scope

This record audits only the reproducibility/provenance boundary of the prepared Exp073R1 low-concurrency 32-microshard transport topology. It does **not** alter any frozen scientific acceptance criterion and does **not** score Exp073P, covariance, nuisance, quotient/null, or G8.

Audited implementation head before this record: `22cf2c863390115ba4650e136856312563383eb2`.
Prepared workflow: `.github/workflows/exp073r1-desy1-low-concurrency-microshards-v0-3.yml`.
Shard implementation: `ci/exp073r1_desy1_shard_v0_2.py`.
Merger: `ci/exp073r1_desy1_merge_v0_3.py`.

## Finding

**Finding class: reproducibility/provenance gap; not infrastructure failure and not scientific FAIL.**

The v0.3 preflight binds the run to the frozen checksum record containing the expected full-file SHA256 values

- source: `491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd`
- metacal: `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`

and binds to the genuine Exp073R0 PASS artifact. Each range fetch also requires an exact HTTP `Content-Range` and exact byte count. Each shard records SHA256 digests of the source and metacal **data ranges actually received**, and the merger verifies the individual pixel-record file digests and exact row-universe coverage.

However, the present merger only checks that each recorded range digest is syntactically a SHA256 hex string. It does **not** compare the fetched source/metacal range payloads against an independently frozen per-range digest manifest, nor can the full-file SHA256 be reconstructed from the per-range SHA256 digests alone. Therefore the existing v0.3 contract establishes URL + byte-range + byte-count identity and records payload hashes, but does not by itself cryptographically prove that every payload byte came from the exact full FITS objects whose frozen full-file SHA256 values are cited in the checksum record.

This is stronger than having no provenance because the received bytes are permanently fingerprinted per shard and the row partition is exact, but it is weaker than a complete immutable-input byte binding.

## Consequence

No existing scientific result is invalidated by this audit. Exp073R1 remains reproduction/infrastructure INCOMPLETE while the current attempt is non-terminal. Exp073P and all downstream G7 operations remain blocked exactly as before.

The prepared v0.3 topology must not be described as providing a **cryptographic full-input identity proof** unless an independent payload-binding mechanism is added. Its current transport evidence is appropriately described as exact-range transport with recorded per-range SHA256 fingerprints under a frozen full-file checksum/URL provenance record.

## Admissible repair classes

Any repair must leave the frozen physical selection, mapper, row universe, Exp073P acceptance criteria, and downstream ordering unchanged. Scientifically admissible options include:

1. a preregistered independently generated manifest of expected SHA256 digests for every source/metacal byte interval consumed by the 32 microshards, followed by exact digest equality checks before merge;
2. a byte-preserving immutable mirror/object whose whole-object checksum is verified before local slicing, if such a public and provenance-preserving delivery path is available;
3. another independently auditable mechanism that proves range bytes are from the frozen full-file object rather than merely recording the bytes received.

A transport repair must be classified separately from scientific support-validity scoring. Failure of an identity check is a reproduction/input-integrity failure, **not** Exp073P scientific FAIL.

## Current run guard

At audit time, Exp073R1 workflow run `33135622749` attempt 2 still has shard 0 executing while shards 1–7 are failed. No replacement heavy run should be launched while shard 0 remains active. If attempt 2 terminates without a genuine Exp073R1 PASS, the next recovery iteration should resolve or explicitly bound this payload-identity gap before claiming stronger immutable-input provenance for a v0.3/v0.4 recovery run.

## Gate ordering preserved

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`

Nothing in this audit opens a downstream gate.
