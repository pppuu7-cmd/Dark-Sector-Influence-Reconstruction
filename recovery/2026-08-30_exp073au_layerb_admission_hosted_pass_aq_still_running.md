# DSIR recovery checkpoint — Exp073AU hosted PASS, AQ still running

Date: 2026-08-30.

## Duplicate/heavy audit

Before this iteration, `docs/RECOVERY_LATEST.md`, recent commits, Exp073AQ jobs and artifacts were inspected.

Real heavy Exp073AQ run `33327372191` remained active:

- replica A job `99299799192`: IN PROGRESS on exact controlled Wm_S1 computation;
- replica B job `99299799338`: IN PROGRESS on exact controlled Wm_S1 computation;
- no AQ artifact existed at the time Exp073AU was frozen and triggered.

Therefore no duplicate Wm_S1, no Wm_S2, and no other heavy angular workflow was launched.

## Independent downstream audit

The frozen broad-row Layer-B science semantics (`docs/ARTICLE3_BROAD_ROW_LAYERB_SCHEMA_AMENDMENT_2026-08-30.md`, Exp073V) remain valid and route-agnostic. However, they predate the execution-qualified successor authority chain and therefore did not require a future Layer-B execution to prove that its `S_op` came from the same real Exp073AS candidate manifest admitted under Exp073AT and classified by real Layer A.

Exp073AU prospectively closes only that provenance/release boundary. It does not alter Layer-A or Layer-B mathematics.

## Exp073AU frozen chain

- prereg: `f9f65423587fd18e96851a237cd92c9b6f9a053f`;
- validator/self-test: `990df78aee6665234d3ad329347802a875618121`;
- workflow: `862dee0b04848d1b172672f925050f7f68798ff1`;
- workflow freeze: `755f9bcd4971c3ecc944393618a69233d380b744`;
- trigger/head: `49618bc580722122f04edc6941b487cca649cb0c`.

The freeze and trigger occurred before any AQ comparator authority, real successor aggregate, real candidate manifest, real Layer-A score or covariance read.

## Hosted result

- run: `33332508516`;
- job: `99313536899`;
- status: completed / success;
- artifact: `9738046768`;
- digest: `sha256:de46bc1da44df1abe7a997b91258f8615c15b027d28b1873c545f6111f2b2ec8`;
- token: `PASS_EXP073AU_EXECUTION_QUALIFIED_LAYERB_ADMISSION_SYNTHETIC_V0_1`;
- frozen synthetic matrix: `26/26` passed.

Classification:

`HOSTED_SYNTHETIC_PASS_NON_SCIENTIFIC_PLUS_0_READINESS`

## What Exp073AU now protects

A future Layer-B execution may be released only from a real Layer-A PASS receipt that binds:

- authority route `controlled_single_thread_exact_v1`;
- Exp073AS successor candidate join;
- Exp073AT candidate-to-Layer-A admission;
- exact complete 1410-row candidate authority;
- unchanged Exp073U ordered-ID authority;
- controlled Wm_S0 anchor `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`;
- immutable candidate-manifest and Layer-A result hashes;
- retained `S_op` count `15..1410`;
- `S_op` inherited Exp073U order;
- exact frozen Layer-A threshold/domain metadata;
- zero unresolved exact-threshold ambiguity.

Historical route classes, Layer-A FAIL/INVALID, incomplete or different manifests, reordered/modified `S_op`, covariance/whitening/nuisance/relation/G8 leakage, effective-coordinate shortcuts and fiducial-P weighting are blocked.

## Scientific state

Unchanged:

- strict Article-3 scientific repository readiness: **52%**;
- readiness increment from Exp073AU: **0**;
- Layer A: OPEN;
- Layer B: OPEN;
- covariance/whitening: BLOCKED;
- G7/G8/G9: OPEN;
- no scientific model PASS claimed.

Frozen thresholds remain unchanged:

- `0.295 <= z <= 2.33` inclusive;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A `operator_f_invalid <= 0.05` inclusive;
- Layer-B invalid row fraction `<= 0.05` inclusive;
- minimum final retained observation dimension `15`;
- exact-threshold ambiguity remains `numerically_unresolved`, never rounded to PASS/FAIL.

## Authorized order

`resolve Exp073AQ Wm_S1`

`-> if exact PASS, prospectively freeze/run Wm_S2 controlled twins`

`-> complete all remaining independent exact-twin angular admissions`

`-> real Exp073AR 14-window aggregate`

`-> real Exp073AS complete 1410-row candidate manifest`

`-> Exp073AT admission -> real Layer A`

`-> Exp073AU admission -> real Layer B`

`-> only after real Layer-A PASS + real Layer-B PASS on the same chain: covariance restriction / unrescued Cholesky whitening`

`-> nuisance geometry -> quotient/relation/null -> fresh withheld G8 after G7 relation freeze`.
