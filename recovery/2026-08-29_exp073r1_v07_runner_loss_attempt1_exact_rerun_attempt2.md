# DSIR recovery checkpoint — Exp073R1 v0.7 attempt 1 runner-loss classification and exact rerun

Date: 2026-08-29
Branch: `main`
Scope: DSIR only; no RTK content.

## Authoritative observation

GitHub Actions run `33240490287`, job `99068879596`, workflow `Exp073R1 DESY1 transport-stabilized exact-byte replay v0.7`, attempt 1 reached step 10 `Acquire authoritative object by full-from-zero no-Range retries` after steps 1–9 completed successfully.

The workflow run then terminated with overall conclusion `failure` while the job/step summary still reported step 10 as `in_progress`; later `always()` cleanup and artifact-upload steps did not execute and the run exposed no artifacts. The run lasted approximately 90 minutes (created 07:17:25Z, updated 08:47:31Z).

This termination pattern is classified as:

`INFRASTRUCTURE_RUNNER_LOSS_DURING_REMOTE_WHOLE_OBJECT_ACQUISITION`

It is **not** a scientific FAIL, not a G7 support-validity result, and not a reproduction-identity FAIL. No genuine Exp073R1 mapper PASS/FAIL assertion was reached.

## Frozen-contract preservation

No scientific evaluator, mapper, selection, parent authority, expected byte count, expected SHA256, no-Range requirement, whole-object-from-zero rule, or acceptance criterion is changed by this checkpoint.

The v0.7 route remains fail-closed:

- each remote attempt starts from byte 0;
- no `Range` or resume is authorized;
- HTTP 200 and absence of `Content-Range` are required;
- exact byte count `84075649920` is required;
- exact SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8` is required before replay;
- unchanged frozen Exp073R1 v0.5 mapper is the only scientific evaluator;
- downstream G7 quantities remain forbidden until genuine R1 PASS.

## Action taken

Because no heavy run remained active after attempt 1, one exact job rerun of job `99068879596` was requested through GitHub Actions. This is an exact rerun of the already-preregistered v0.7 route, not a new scientific route and not a duplicate concurrent heavy run.

## Current gate state

`Exp073R1 reproduction: INCOMPLETE`

`Scientific FAIL: NO`

`Infrastructure failure observed: YES`

`Downstream G7 authorization: NO`

Frozen sequence remains:

1. genuine Exp073R1 PASS;
2. preregistered Exp073P physical support-validity mask;
3. covariance restriction/whitening;
4. nuisance tangent rank/SVD;
5. quotient/relation/null control;
6. only then fresh G8 withheld family.
