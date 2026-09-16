# Exp069D infrastructure checkpoint — 2026-08-27

Status: SCIENCE NOT YET EXECUTED

## Context

Exp069D is the preregistered C5 designer-zero branch mechanism audit following Exp069C. The frozen scientific contract is unchanged.

## Failed runs before science

Runs `33018285890` and `33018472105` both failed in the workflow's pinned-source verification step before H-EFTCAMB compilation or any Exp069D science case was executed.

Observed failure:

`grep -F 'call dlsoda' .../007p3_Designer_fR.f90` returned exit code 1.

The pinned upstream source is present at the expected commit and contains DLSODA-related code, but the workflow guard was text/case brittle. No summary JSON or science artifact was produced in either failed run.

Classification:

`INFRASTRUCTURE_FAILURE_SOURCE_GUARD`

This is explicitly **not** a scientific FAIL and must not be interpreted as evidence about the C5 zero-limit mechanism.

## Corrective change

Commit `778d5186e253b31de4a63fbc3b7c62115f5362a7` changes only source-presence guards:

- DLSODA presence is checked case-insensitively;
- frozen DLSODA `rtol=1e-12` and `atol=1e-16` values are checked with whitespace-tolerant regexes;
- `model_background_num_points` is checked in the actual pinned designer-f(R) source file where that input is read.

No solver commit, cosmology, branch cases, background-point grid, RGR settings, thresholds, classification rule, or G7 boundary changed.

## Next exact action

Run 3 (`33019085721`) is the first post-fix attempt. Only if it reaches the frozen branch scan and emits the required summary may Exp069D receive a scientific mechanism classification.

Exp069B remains permanent FAIL. Exp069C remains `RAW_POWER_ZERO_LIMIT_RESIDUAL + KGRID_NONCONVERGENCE`. C5 is not provider-certified and the common support-validity mask remains unauthorized.

G7=OPEN. G8=OPEN. G9=OPEN.
