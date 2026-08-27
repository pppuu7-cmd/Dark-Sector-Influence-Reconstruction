# DSIR-I late-DSIR3/DSIR4 paper addendum — 2026-08-27

This addendum records article changes after the original DSIR-I recovery checkpoint. It must be read together with `recovery/dsir1_paper_checkpoint_2026-08-27.md`.

## Current article state

The paper branch now treats observation-space admissibility as a fail-closed sequence rather than a single projection step. The central rule is:

`finite positive support measure -> exact reproducible real-data operator/input realization -> physical support eligibility -> physically justified model/provider semantics -> covariance restriction/whitening -> nuisance quotient -> relation/null tests`.

The article still does **not** claim a completed survey quotient. `G7=OPEN`, `G8=OPEN`, `G9=OPEN`.

A complete paper build including the DSIR4 Exp073N/O/R0 material passed as workflow run `33109097423` on source commit `b5fcfd559309f33ace4264735e986d5b40a0f80d`. The run conclusion is `SUCCESS` and includes the deterministic manuscript audit, support/operator audits, Figures 1--7, checksums, and artifact packaging. A later build adds the supplementary observation-route ledger and its own semantic audit; use the latest successful paper run when recovering after this file's commit.

## Completed normalizability result

### Exp073L

Status: `EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L`.

- run `33049366874`
- artifact `9637070322`
- digest `sha256:03a8f63155c40180c81b6472828210408b472463aec244fff8c442ad7cd7c684`
- Wm `8/8` nonnormalizable, `0` finite
- WW `8/8` nonnormalizable, `0` finite
- local exponents approximately `1.493--1.518`
- dyadic-shell fractions approximately `0.645--0.651`
- half-step discrepancy `1.9428e-6` vs frozen tolerance `0.005`

Interpretation: the frozen absolute-response route has no finite positive normalizer. No retrospective high-ell cutoff or fiducial-power weighting is permitted to manufacture one.

Analytic interpretation retained in the paper:

`f_shell = 1 - 2^(-p)`.

Exp073G remains methodological corroboration only; its formal record is a reproduction/provenance failure, not a scientific support FAIL.

## DSIR4 exact-realization provenance chain

### Exp073M — candidate class

Status: `FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M`.

A finite-positive harmonic class was identified using DES Y3 GGL Wm, DES Y1 shear WW, and finite BOSS mm. M1--M8 pass at the candidate-class level. No support fraction or downstream covariance/nuisance quantity was read.

### Exp073N — exact public realization FAIL

Status: `FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE`.

- run `33062650033`
- artifact `9642372335`
- digest `sha256:914d23e9d708a7b8cb9e097a69845e2630ec265b5ccc489ce9a8d389d4e198db`

The frozen operator repository itself reproduces, but the exact published DES Y3 real-data Wm realization cannot be reproduced from the frozen public binding: the available Y3 GGL configurations at that pin are flask configurations and the frozen `ggltest.py` path does not execute a real-data route.

This is **not** a physical-support FAIL. No `f_invalid`, Wm/WW support fraction, or retained dimension was evaluated. The future rectangle, `f_invalid<=0.05` criterion, and minimum retained dimension 15 remain unchanged.

### Exp073O — prospective public replacement FOUND

Status: `PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O`.

- result commit `3f16dabdbfe9842b928d2fd0e00e481194637583`
- source `Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`
- candidate `COSMOTHEKA_DESY1_GC_X_WL_PSEUDO_CL`

The DES Y1 redMaGiC x Metacal pseudo-`C_ell` Wm replacement passes O1--O8: immutable public provenance, finite NaMaster operator, bindable exact public inputs, signed Wm semantics, no hidden GR closure, no downstream/model weighting, redshift information, and later support-audit feasibility. Exp073N remains permanently failed. No physical support fraction was read during replacement selection.

## Public-input / operator reproduction chain

### Exp073P2

`PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2`.

Every frozen DES Y1 release object is checksum-bound before support output, including the 84,075,649,920-byte metacalibration catalogue and the 2,738,626,560-byte source-redshift-binning file.

### Exp073S0

`PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0`.

- run `33086762750`
- artifact `9652504743`
- digest `sha256:c6f84c35e7ade17a6054ad77d4117b64a6c69fbbefe0d0f89e6491bbe88b358e`
- native `Nside=4096`
- 6,536,725 mask pixels above 0.5
- `f_sky=0.0324682643`
- lens/source `n(z)` each 400 rows, with 5/4 bins

### Exp073R0

`PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`.

- workflow run `33103083736`
- execution `94b05d307295d5e9263646983ece9514f9fa2e88`
- artifact `9661445512`
- digest `sha256:bfa97a88218cda6e6e6c58d915e8e5b21500fa677a484205691f2f01662ed4d0`
- 16 frozen windows x 8192 rows = 131,072 sampled rows
- parent catalogue rows: 136,930,995
- `Nside=4096`, `coords=C`
- exact required source/metacalibration fields
- exact HEALPix indices in all four source bins
- selected rows `7674, 7667, 7272, 3618`
- unique pixels `4300, 4277, 4178, 2650`

The R0 artifact explicitly has `science_gate_scored=false`. R0 is a reproduction/equivalence prerequisite PASS, **not** the physical-support result.

Two earlier R0 transport/infrastructure-incomplete attempts remain provenance and are not rewritten as scientific failures.

## Exp073R1 boundary

Exp073R1 was preregistered before the relevant R0 output (`71d61efc17535f45a81f45d1a037abfdb8aaaeeb`), its gated implementation was merged at `4b466f1c27019438c76a92dd7830ac6a2cc3fe7d`, and it was launched after genuine R0 PASS from main commit `af0b3c40ac37a8847d3f7b5f2c38dda6f7f09da4`.

At the article snapshot used for these edits, workflow run `33108733415` was still in progress. It is therefore **not** an article result. Do not infer PASS, FAIL, support fraction, or survey-level eligibility from its preregistration, implementation, or launch.

## Paper files now binding this chain

- `papers/dsir1/evidence/support_operator_eligibility_v0_1.json` — manuscript evidence snapshot v0.2
- `papers/dsir1/SUPPORT_OPERATOR_PROVENANCE.md` — P24--P29
- `papers/dsir1/OBSERVATION_ROUTE_LEDGER.md` — supplementary fail-closed status table
- `papers/dsir1/audit_support_operator_eligibility.py`
- `papers/dsir1/audit_observation_route_ledger.py`
- `papers/dsir1/sections/observation_space_support_closure.md`
- `papers/dsir1/sections/data_code_reproducibility.md`
- `papers/dsir1/CLAIMS_LEDGER.md`
- `papers/dsir1/build_manuscript_v0_2.py` — Abstract/Introduction/Conclusions expose normalizability + exact-realization + physical-support prerequisites
- `.github/workflows/paper-dsir1-build-v0-2.yml`

## Hard recovery boundary

Never collapse these statuses:

- Exp073M = candidate-class FOUND;
- Exp073N = exact-realization provenance FAIL;
- Exp073O = prospective replacement FOUND;
- Exp073P2/S0/R0 = prerequisite PASSes;
- Exp073R1 = pre-result until a completed frozen output exists.

A prerequisite PASS is not a physical-support PASS, and a physical-support PASS would still not by itself be a covariance/nuisance/G7 result.
