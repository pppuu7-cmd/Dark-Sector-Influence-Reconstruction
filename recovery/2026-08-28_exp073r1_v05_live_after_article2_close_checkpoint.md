# DSIR checkpoint — Exp073R1 v0.5 live after Article 2 evidence close

Date: 2026-08-28
Branch authority at inspection: `main` @ `2d532f6fa26e74b519e72eaa879a546734f71b30`

## Canonical G7 prerequisite status

Canonical run: Exp073R1 DESY1 sequential whole-stream reconstruction v0.5, run `33175886694`.

Observed state at checkpoint:

- `source-index`: **PASS / success**.
- Stage-A authoritative source stream and exact row-aligned z-bin index completed.
- Frozen no-Range identity contract assertion completed successfully.
- `metacal-map`: **in progress**.
- Exp073R0 immutable parent binding completed successfully.
- Current active step: sequential authoritative metacal stream + frozen mapper.
- True Exp073R1 reproduction assertion has **not** yet executed.
- No downstream Exp073P / covariance / nuisance-SVD / quotient-null / G8 work is admissible yet.

Classification: **infrastructure/reproduction INCOMPLETE**, not scientific FAIL.

No duplicate heavy run was launched in this iteration.

## Independent scientific branch status

`main` has advanced through Exp071N and the Article 2 evidence audit is now explicitly closed. The current head commit message is `Close Article 2 scientific evidence audit after Exp071N`.

This independent branch does not alter G7 ordering and does not authorize any downstream G7 stage.

## Frozen sequencing rule retained

The only admissible G7 order remains:

1. validated physical forward/power-input bridges;
2. preregistered physical support-validity mask;
3. covariance restriction / whitening;
4. nuisance tangent rank / SVD;
5. quotient / relation / null control;
6. only then a fresh G8 withheld family.

For the active DESY1 path specifically, canonical Exp073R1 must reach a genuine reproduction PASS before Exp073P can execute.

## Next admissible action

- If run `33175886694` reaches genuine Exp073R1 PASS, verify terminal artifacts/provenance and only then dispatch the already-preregistered Exp073P physical support-validity stage.
- If it terminates in infrastructure failure, preserve the failure as infrastructure evidence and repair only the transport/execution mechanism without changing frozen scientific acceptance criteria.
- If the mapper remains live, do not launch a competing heavy reconstruction.

Negative scientific outcomes, if any emerge later, must be retained as results and never relabeled as infrastructure failures.
