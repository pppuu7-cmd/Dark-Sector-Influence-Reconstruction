# DSIR checkpoint — Exp073P v0.2 byte-freeze guard + live Exp073R1 authority

Recorded 2026-08-29 UTC.

## Authoritative upstream state

- Exp073R1 replacement authority remains run `33222848695`, job `99020389131`, head `98c4b8783a95932949947d9e214706c4ec7eaf8c`.
- The job is still `in_progress` at the preregistered whole-object metacal streaming / unchanged frozen mapper step.
- The terminal genuine-R1 assertion has not run yet.
- Classification therefore remains **reproduction INCOMPLETE**, not scientific FAIL.
- No duplicate Exp073R1 heavy run was started.

## New integrity finding

The prospectively frozen Exp073P aggregate-join v0.2 production route already checked exact hashes of its evaluator, metadata collector, and authority preregistration inside the workflow, but its internal firewall did not itself compare the production workflow file against the prospectively recorded exact workflow SHA256.

This is an operational/reproducibility hardening gap, not a scientific result and not a change to any frozen acceptance criterion. The frozen production workflow itself was not modified.

## Hardening added

Added `ci/exp073p_v02_route_bytefreeze_guard_v0_1.py` and `.github/workflows/exp073p-v02-route-bytefreeze-guard-v0-1.yml`.

The guard independently requires exact byte identity for:

- production aggregate-join workflow: `e29eec8f9459cd361c707265ae858f843f6cf5537d32ac9c5a7a0c9652996307`;
- aggregate evaluator v0.2: `5a17f622a4025eec82541688bded4bfedd3b6b96bc511f7d1a3327e886161cfd`;
- Actions metadata collector v0.2: `aec7215a3b8cce8b1383f4cd8e49c37b22388ac6318088a3df794c8ecbd77810`;
- superseding-R1 authority preregistration: `601f904200d72ebf5d483c973a92261eebd38b065a909220ccd8c6b86c46ad76`.

Its mutation self-test alters each frozen member independently and requires fail-closed rejection. It explicitly carries `scientific_classification=null`, `support_executor_authorized=false`, and all support/covariance/SVD/relation/G8 read/evaluation flags false.

Hosted CI run `33235804992` completed `success`. Exact-byte assertion, independent mutation self-test, no-downstream-leakage assertion, and artifact upload all passed.

## Gate state

Still frozen and unchanged:

`genuine Exp073R1 PASS -> real Exp073P prerequisite join -> physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`.

No physical-support fraction, `f_invalid`, covariance, whitening, nuisance SVD/rank, quotient/relation/null, held-out, or G8 quantity was evaluated in this iteration.
