# DSIR checkpoint — Exp073R1 v0.7 attempt 2 runner shutdown

Date: 2026-08-29
Branch: `main`

## Event

Canonical workflow run:

- run id: `33240490287`
- workflow: `Exp073R1 DESY1 transport-stabilized exact-byte replay v0.7`
- frozen head: `9a4606fb37d5aaa071aa57322ebb7c05eca905d7`
- attempt: `2`
- job id: `99080934021`
- runner: `DSIR-HOME-PC`

Attempt 2 completed with workflow conclusion `failure` at 2026-08-29T18:28:53Z.

## Exact failure classification

Steps 1–9 passed, including:

1. checkout;
2. frozen evaluator/prereg firewall;
3. local storage capacity gate (`1021924311040` bytes available, required >= `100000000000`);
4. isolated pinned mapper runtime (`numpy==2.5.2`, `healpy==1.20.0`);
5. immutable Stage-A / Exp073R0 metadata rebinding;
6. both parent artifact downloads with expected artifact digests;
7. downloaded-parent internal-contract rebinding.

The first failing step was:

`Acquire authoritative object by full-from-zero no-Range retries`

The acquisition process terminated with `KeyboardInterrupt`, exit code `130`. The job log then states:

`The runner has received a shutdown signal. This can happen when the runner service is stopped, or a manually started runner is canceled.`

Therefore this is classified as an **execution/infrastructure interruption**, not a scientific failure and not an exhausted transport-retry decision.

The loopback exact-byte endpoint, unchanged frozen mapper, genuine Exp073R1 PASS assertion, and artifact publication were all skipped.

## Scientific state

Unchanged:

- `reproduction=INCOMPLETE`
- `scientific_FAIL=false`
- `G7=OPEN`
- `G8=OPEN`
- `G9=OPEN`
- no physical-support mask execution is authorized.

A retry of the same frozen workflow/job is allowed because it does not alter the preregistration, evaluator blob, expected 84-GB byte count/hash, selection, HEALPix mapping, or downstream gates.

## Automated-mode progress retained

The automatic research loop added prospective Exp073P v0.3 reproducibility controls without changing science semantics, including:

- production-route byte-freeze guard PASS (`fcd771a286301d811ec4f4dd9aa759df746d5371` checkpoint);
- strict JSON evidence ambiguity guard PASS (`81977beabd9c9d84204ebf8fd6167045f2307a3c` checkpoint);
- evidence schema-closure guard, hosted run `33267947264`, job `99141254295`, conclusion `success`;
- canonical v0.3 guards integrated into `main` through merge commit `e3eaa47dea29a20bf6bb8330ac77607197097f81` and subsequent current-main validation/checkpoints.

These controls strengthen provenance/fail-closed authority handling only. They do **not** constitute a G7 PASS.

## Frozen downstream order

`genuine Exp073R1 PASS -> real attempt-aware Exp073P v0.3 prerequisite join -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`

Next action: re-run only the failed frozen Exp073R1 job; do not launch a competing heavy authority run.