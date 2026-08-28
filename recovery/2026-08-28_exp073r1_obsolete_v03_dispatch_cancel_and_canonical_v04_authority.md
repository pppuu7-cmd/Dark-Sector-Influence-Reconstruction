# DSIR G7 — obsolete Exp073R1 v0.3 dispatch cancellation and canonical v0.4 authority

Date: 2026-08-28
Scope: G7 validated physical forward/power-input bridge / reproduction only. No physical-support fraction is scored here; covariance, whitening, nuisance SVD, quotient/relation/null, G8 and G9 remain unread and unscored.

## Parent v0.2 terminal state

Parent run `33135622749` is terminal without a genuine full-universe Exp073R1 PASS: shard 0 completed successfully, shards 1–7 failed, and merge was skipped. This remains an infrastructure/reproduction INCOMPLETE state, not a scientific FAIL.

## Orchestration provenance correction

An earlier readiness note referenced `.github/workflows/exp073r1-launch-v0-3-after-v0-2-terminal.yml`, but that launcher file was absent from `main` when re-audited. Commit `27ee404808f4d48703729a63a0db54757d92c951` materialized that previously described v0.3 launcher and it dispatched run `33170314475`.

A wider current-Actions audit immediately afterwards established that a newer, stricter recovery path had already been merged and dispatched before that action: canonical whole-stream-bound v0.4 run `33160570463`, launched by successful one-shot launcher run `33160562744`. Canonical v0.4 closes the previously recorded range-payload identity gap by deriving each 32-way range SHA256 in the same streaming pass that reproduces the authoritative frozen whole-object SHA256.

Therefore v0.3 run `33170314475` was obsolete and a duplicate heavy computation. It was immediately cancelled through one-shot cancellation workflow commit `0af764d1cccd2d4755d374958e4d09a6ddc4531f`, run `33170361612`. The cancellation job completed success. In the cancelled v0.3 run, preflight had succeeded, shard 0 was cancelled while executing, the remaining shard jobs were cancelled/queued-to-cancel, and no shard science assertion or merge result was produced. No v0.3 partial output is admissible for gate advancement.

## Canonical v0.4 authority and live state

The sole authoritative Exp073R1 heavy recovery is run `33160570463`, workflow `.github/workflows/exp073r1-desy1-canonical-microshards-v0-4.yml`.

At this checkpoint:
- preflight: success;
- canonical source whole-stream/range manifest: success;
- canonical metacal whole-stream/range manifest: success;
- both manifests assert `PASS_CANONICAL_WHOLE_AND_MICROSHARD_RANGE_SHA256_BINDING_EXP073R1M`, exact coverage of all table rows once, and range hashes computed in the same stream as the whole SHA256;
- shard 0 is in progress;
- remaining microshards are queued under `max-parallel: 1`;
- no merge has yet produced `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`.

The canonical source whole-object SHA256 remains `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`; metacal remains `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`. These are rebound to the prior authoritative whole-object streaming checksum run before canonical manifests are generated.

## Gate decision

Current state: **Exp073R1 infrastructure/reproduction INCOMPLETE while canonical v0.4 is active**. This is not a scientific FAIL.

No additional Exp073R1 heavy workflow may be launched while run `33160570463` is queued/in progress. Only a genuine complete canonical merge PASS may unblock the already-frozen Exp073P physical support-validity classification.

No frozen acceptance criterion was changed. Scientific ordering remains:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`.
