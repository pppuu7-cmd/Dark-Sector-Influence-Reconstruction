# Exp073R1 low-concurrency microshard repair preregistration — 2026-08-28

Run 33135622749 attempt 2 is still in progress. Shards 1–7 failed at transport; shard 0 remains active. This is classified as INFRASTRUCTURE INCOMPLETE, not scientific FAIL. Exp073P science classification has not run.

If the current run terminates without an Exp073R1 reproduction PASS, the next admissible recovery topology is `.github/workflows/exp073r1-desy1-low-concurrency-microshards-v0-3.yml`.

Only execution topology changes: the same immutable DES public inputs, row universe, byte layouts, selection, HEALPix nside=4096 RING mapping, and deterministic row partition rule are retained. The partition count changes from 8 to 32 and `max-parallel` is fixed to 1, reducing public-server concurrency and making each retry unit smaller. Every completed microshard remains non-science: it cannot compute `f_invalid`, read covariance, or access G8.

The v0.3 workflow must not be dispatched while run 33135622749 has an active shard, to avoid duplicating heavy work.

Downstream remains locked in this order: Exp073R1 reproduction PASS -> frozen Exp073P support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family. Frozen acceptance criteria are unchanged.