# Exp073R1 shard-0 success and failed-only retry checkpoint — 2026-08-28

## Status

Exp073R1 sharded workflow run `33135622749` reached a terminal latest-attempt state with:

- shard 0: `success`;
- shards 1–7: `failure` during the deterministic shard execution step;
- merge: `skipped` because the full shard set was incomplete.

This is **not** a scientific FAIL. The full Exp073R1 reproduction gate remains **INCOMPLETE** because the complete row universe was not reconstructed and the frozen Exp073R1 PASS assertion was never reached.

## Preserved successful artifact

The successful shard-0 artifact is preserved by GitHub Actions:

- artifact name: `exp073r1s-shard-0`
- artifact id: `9681429458`
- artifact size: `1,627,743` bytes
- artifact digest: `sha256:1daa27ba0b8b1194cfddaf43c65fa1e592057d202b48f93ac5e9a74cd8101d62`
- originating workflow run: `33135622749`
- originating head SHA: `70be4d35199d4132a2ca9da912689519e40bcc84`

The artifact is retained as reproduction/provenance evidence only. It is not an Exp073R1 PASS and must not be interpreted as a scientific support-mask result.

## Recovery action taken

Because the parent run is now terminal and shard 0 is already successful, a GitHub Actions **re-run failed jobs** operation was issued on run `33135622749`.

This action is intentionally narrower than starting a new heavy run: it targets failed jobs rather than duplicating the known successful shard-0 computation. No downstream Exp073P, covariance/whitening, nuisance-SVD, quotient/null, or G8 job was launched.

## Frozen constraints preserved

No frozen acceptance criterion was changed. In particular:

1. Exp073R1 remains a reproduction/forward-bridge gate only.
2. Exp073P cannot run until a genuine complete Exp073R1 PASS exists.
3. The previously frozen Exp073P support-validity criteria are unchanged.
4. Covariance restriction/whitening remains downstream of Exp073P.
5. Nuisance tangent rank/SVD remains downstream of covariance restriction/whitening.
6. Quotient/relation/null control remains downstream of nuisance tangent validation.
7. Fresh G8 withheld-family work remains blocked until the full G7 ordering is satisfied.

## Classification

Current classification: **infrastructure/reproduction INCOMPLETE**.

Scientific classification: **not evaluated**.

The successful shard-0 result is useful because it demonstrates that the deterministic shard implementation can complete on at least one disjoint interval under the frozen physics/selection contract. The failures of the remaining shards must continue to be treated as transport/execution failures unless and until evidence shows otherwise.
