# Exp073R1 all-shards transport INCOMPLETE and single-probe rerun

Date: 2026-08-28
Branch: main
Parent sharded run: https://github.com/pppuu7-cmd/Dark-Sector-Influence-Reconstruction/actions/runs/33135622749

## Status

All eight deterministic Exp073R1 shards completed with `failure` before any science classification or downstream G7 stage. The merge job was skipped.

The previously unresolved shard 0 ended with the same transport signature already observed in shards 1–7: repeated HTTP range requests to the DES public metacalibration FITS endpoint timed out after 600 s with zero bytes received (including requests reporting `0 out of 160956416 bytes received`), ending in `RuntimeError: range transport exhausted`.

Therefore this run is classified as:

- **infrastructure INCOMPLETE**
- **not a scientific FAIL**
- **not an Exp073P result**
- **not permission to advance to covariance restriction/whitening**

The physical selection, frozen Exp073P criteria, HEALPix convention, row partition, and G7 ordering remain unchanged.

## Minimal recovery action

After the parent run fully terminated, a rerun was requested for **only shard 0** as a minimal independent transport probe. This intentionally avoids immediately duplicating all eight heavy shards.

Interpretation is frozen in advance:

1. If the single shard succeeds under identical science logic, the prior failure remains transient infrastructure and missing shards may be retried selectively.
2. If the same zero-byte DES range timeout recurs, do not weaken any scientific criterion and do not rerun all shards blindly; repair only transport/checkpoint topology or use an immutable equivalent public-input delivery path with explicit byte/checksum binding.
3. No artifact from a partial/failed shard can satisfy Exp073R1 reproduction PASS.

## G7 lock

Required order remains:

validated physical forward/power-input bridges -> Exp073R1 input reproduction PASS -> preregistered Exp073P physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family.
