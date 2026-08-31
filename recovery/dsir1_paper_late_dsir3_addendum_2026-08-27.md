# DSIR-I late-DSIR3/DSIR4 paper addendum — 2026-08-27

This addendum records article changes after the original DSIR-I recovery checkpoint. Read it together with `recovery/dsir1_paper_checkpoint_2026-08-27.md`.

## Current green paper baseline

The current submission-preparation baseline is:

- paper source commit: `8ed955075efdd60a8ae15ef928ba91920a41c514`
- workflow: `DSIR-I paper build v0.2`
- workflow run: `33110035955`
- job: `98650121803`
- conclusion: `SUCCESS`
- build artifact: `9662131867`
- artifact digest: `sha256:7cc5cb3e514a3851d5fe73e30dc1f9ec569fa50e248d08edd205a618a1dd5b21`

The run passed:

- deterministic manuscript v0.2 assembly/audit;
- retrospective known-sector non-overclaim audit;
- Exp072A--Exp073A support-closure audit;
- late support/operator eligibility audit through Exp073R0;
- observation-route ledger semantic audit;
- Figures 1--7;
- checksum generation;
- artifact packaging.

The artifact also contains the numerical-method appendix, referee adversarial audit, literature positioning, route ledger and camera-ready table drafts.

## Hard article state

The paper now treats observation-space admissibility as the fail-closed sequence

`finite positive support measure -> exact reproducible real-data operator/input realization -> physical support eligibility -> physically justified model/provider semantics -> covariance restriction/whitening -> nuisance quotient -> relation/null tests`.

The article still does **not** claim a completed survey quotient. Current gates remain:

- `G7=OPEN`
- `G8=OPEN`
- `G9=OPEN`

## Completed normalizability result

### Exp073L

`EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L`

- run `33049366874`
- artifact `9637070322`
- digest `sha256:03a8f63155c40180c81b6472828210408b472463aec244fff8c442ad7cd7c684`
- Wm `8/8` nonnormalizable, `0` finite
- WW `8/8` nonnormalizable, `0` finite
- local exponents approximately `1.493--1.518`
- dyadic-shell fractions approximately `0.645--0.651`
- half-step discrepancy `1.9428e-6` vs frozen tolerance `0.005`

Interpretation: the frozen absolute-response route has no finite positive normalizer. No retrospective high-ell cutoff or fiducial-power weighting is allowed to manufacture one.

Analytic interpretation retained in the paper:

`f_shell = 1 - 2^(-p)`.

Exp073G remains methodological corroboration only; its formal record is a reproduction/provenance failure, not a scientific-support FAIL.

## DSIR4 exact-realization provenance chain

### Exp073M — candidate class

`FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M`

Finite-positive harmonic class identified using DES Y3 GGL Wm, DES Y1 shear WW and finite BOSS mm. M1--M8 pass at candidate-class level. No support fraction or covariance/nuisance quantity was read.

### Exp073N — exact-realization provenance FAIL

`FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE`

- run `33062650033`
- artifact `9642372335`
- digest `sha256:914d23e9d708a7b8cb9e097a69845e2630ec265b5ccc489ce9a8d389d4e198db`

The frozen operator repository reproduces, but the exact published DES Y3 real-data Wm realization cannot be reconstructed from the frozen public binding. The available Y3 GGL configurations at that pin are flask configurations and the frozen `ggltest.py` route does not execute the required real-data path.

This is **not** a physical-support FAIL. No `f_invalid`, Wm/WW support fraction or retained dimension was evaluated. The future common rectangle, `f_invalid<=0.05` criterion and minimum retained dimension 15 remain unchanged.

### Exp073O — prospective public replacement FOUND

`PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O`

- result commit `3f16dabdbfe9842b928d2fd0e00e481194637583`
- source `Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`
- candidate `COSMOTHEKA_DESY1_GC_X_WL_PSEUDO_CL`

The DES Y1 redMaGiC x Metacal pseudo-`C_ell` replacement passes O1--O8 under unchanged future physical-support criteria. Exp073N remains permanently failed. No support fraction, covariance, nuisance, relation or G8 quantity was read during replacement selection.

## Public-input / operator reproduction chain

### Exp073P2

`PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2`

Every frozen DES Y1 release object is checksum-bound before support output, including the 84,075,649,920-byte metacalibration catalogue and 2,738,626,560-byte source-redshift-binning file.

### Exp073S0

`PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0`

- run `33086762750`
- artifact `9652504743`
- digest `sha256:c6f84c35e7ade17a6054ad77d4117b64a6c69fbbefe0d0f89e6491bbe88b358e`
- native `Nside=4096`
- 6,536,725 mask pixels above 0.5
- `f_sky=0.0324682643`
- lens/source `n(z)` each 400 rows, 5/4 bins

### Exp073R0

`PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`

- workflow run `33103083736`
- execution `94b05d307295d5e9263646983ece9514f9fa2e88`
- artifact `9661445512`
- digest `sha256:bfa97a88218cda6e6e6c58d915e8e5b21500fa677a484205691f2f01662ed4d0`
- 16 frozen windows x 8192 rows = 131,072 sampled rows
- parent catalogue rows 136,930,995
- `Nside=4096`, `coords=C`
- exact required source/metacalibration fields
- exact HEALPix indices in all four source bins
- selected rows `7674, 7667, 7272, 3618`
- unique pixels `4300, 4277, 4178, 2650`

The R0 artifact explicitly has `science_gate_scored=false`. R0 is a reproduction/equivalence prerequisite PASS, **not** the physical-support result. Earlier R0 infrastructure/transport-incomplete attempts remain provenance and are not reclassified as scientific failures.

## Exp073R1 boundary

Exp073R1 was preregistered before the relevant R0 output at commit `71d61efc17535f45a81f45d1a037abfdb8aaaeeb`, its gated implementation was merged at `4b466f1c27019438c76a92dd7830ac6a2cc3fe7d`, and it was launched after genuine R0 PASS from main commit `af0b3c40ac37a8847d3f7b5f2c38dda6f7f09da4`.

At the article snapshot used for this baseline, workflow run `33108733415` was still in progress. Therefore Exp073R1 is **not** an article result. Do not infer PASS, FAIL, support fraction or survey-level eligibility from its preregistration, implementation or launch.

## Submission-preparation files now present

- `papers/dsir1/CLAIMS_LEDGER.md`
- `papers/dsir1/PROVENANCE_MATRIX.md`
- `papers/dsir1/SUPPORT_OPERATOR_PROVENANCE.md` — P24--P29
- `papers/dsir1/OBSERVATION_ROUTE_LEDGER.md`
- `papers/dsir1/NUMERICAL_METHODS_APPENDIX.md`
- `papers/dsir1/REFEREE_ADVERSARIAL_AUDIT.md`
- `papers/dsir1/TABLES_DRAFT.md`
- `papers/dsir1/LITERATURE_POSITIONING.md`
- `papers/dsir1/FIGURE_MANIFEST.md`
- `papers/dsir1/FIGURE_CAPTIONS.md`
- `papers/dsir1/FIGURE_PLACEMENT.md`
- `papers/dsir1/evidence/support_operator_eligibility_v0_1.json`
- `papers/dsir1/audit_support_operator_eligibility.py`
- `papers/dsir1/audit_observation_route_ledger.py`
- `papers/dsir1/sections/observation_space_support_closure.md`
- `papers/dsir1/sections/data_code_reproducibility.md`
- `papers/dsir1/build_manuscript_v0_2.py`

## Non-collapsible status semantics

Never collapse these statuses:

- Exp073M = candidate-class FOUND;
- Exp073N = exact-realization provenance FAIL;
- Exp073O = prospective replacement FOUND;
- Exp073P2/S0/R0 = prerequisite PASSes;
- Exp073R1 = pre-result until a completed frozen output exists.

A prerequisite PASS is not a physical-support PASS. A physical-support PASS would still not by itself imply covariance/nuisance/G7 completion.
