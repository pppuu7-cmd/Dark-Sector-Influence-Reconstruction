# DSIR recovery — Exp073P v0.3 production-route byte-freeze guard

**Recorded:** 2026-08-29 UTC

## Trigger

Exp073R1 v0.7 authoritative run `33240490287`, attempt `2`, job `99080934021` remains queued on the self-hosted runner. No R1 attempt-2 terminal artifact exists, so no real Exp073P v0.3 join may be dispatched and no downstream physical-support work is authorized.

While the heavy run is blocked, a reproducibility audit found one independent launch-time gap in the merged Exp073P v0.3 production route: the route hashes its evaluator, metadata collector, payload validator, artifact downloader, authority preregistration, R1 workflow and acquisition helper, but it did not independently freeze the bytes of the production workflow file itself.

This is a reproducibility/TOCTOU issue only. It is not a scientific failure and does not change any frozen scientific acceptance criterion.

## Prospective launch-control fix

Added `ci/exp073p_v03_production_route_byte_freeze_v0_1.py` without modifying the frozen production workflow `.github/workflows/exp073p-aggregate-prerequisite-join-actual-v0-3.yml`.

The guard freezes:

- production route path: `.github/workflows/exp073p-aggregate-prerequisite-join-actual-v0-3.yml`;
- exact Git blob SHA1: `2950750312c153f75fe79c2c16fca6f74c7df5dc`;
- authority preregistration Git blob SHA1: `6dd4ba0df9ed2be321b7f69966d7636d940e40d1`;
- authority preregistration SHA256: `e27761b2db4a81283bb9fbac1decb95f62fadb785c40cb3e3f676f8651711f40`.

Any byte change to the production workflow or frozen preregistration must reject this launch-control identity. It must not be silently accepted as the same v0.3 route.

The guard includes independent mutations of the production route: append newline, first-byte flip, one-byte truncation, and prepended comment. Every mutation must change the Git blob identity and fail closed.

## Hosted validation receipt

Hosted workflow: `.github/workflows/exp073p-v03-production-route-byte-freeze-selftest-v0-1.yml`.

Run `33259873639`, job `99119863197`: `completed/success`.

Successful steps:

1. checkout;
2. verify exact frozen production-route identity;
3. run four byte-mutation negative controls;
4. assert `support_executor_authorized=false` and `G7=OPEN G8=OPEN G9=OPEN`.

This hosted PASS is only a reproducibility/launch-control receipt. It is not a real prerequisite PASS and cannot authorize the physical-support executor.

## Current authority state

- Exp073R1 v0.7 run `33240490287`, attempt `2`, job `99080934021`: still queued;
- no attempt-2 R1 terminal artifact;
- Exp073P v0.3 real join: not dispatched;
- `support_executor_authorized=false`;
- no physical support-validity mask execution;
- no covariance/whitening, nuisance SVD/rank, quotient/relation/null, or G8 access;
- no scientific FAIL has been observed in this iteration.

## Frozen continuation order

Do not alter:

validated physical forward/power-input bridges -> prerequisite authority join -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> only then fresh G8 withheld family.

Before any future real Exp073P v0.3 dispatch, require both genuine admissible R1 attempt-2 evidence and a PASS of the exact production-route byte-freeze guard. If the production route bytes differ, do not dispatch under v0.3; preserve the mismatch and preregister a new route version prospectively.
