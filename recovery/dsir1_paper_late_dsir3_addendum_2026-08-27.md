# DSIR-I late-DSIR3 paper addendum — 2026-08-27

This addendum records article changes made after the earlier DSIR-I recovery checkpoint. It must be read together with `recovery/dsir1_paper_checkpoint_2026-08-27.md`.

## Current expanded reproducible build

The late-DSIR3 article extension has passed the complete fail-closed paper pipeline.

- paper source commit: `27d46820a87e8c20634c8476fd23cf292f6ee66d`
- workflow: `DSIR-I paper build v0.2`
- workflow run: `33093501161`
- job: `98592285140`
- result: `SUCCESS`
- build artifact: `9655385461`
- artifact digest: `sha256:f31425b040ecda3c613566b4d633770cd936b35b7110e532cc397f2516e3b083`

The run passed the central manuscript audit, retrospective known-sector audit, Exp072A--Exp073E observation-space support/provider/model audit, the late support-operator audit, Figures 1--7, checksum generation, and artifact upload. The generated v0.2 Abstract/Introduction/Conclusions now surface the support-normalizability result while preserving the pre-support status of the finite-positive DES/BOSS candidate. `papers/dsir1/LITERATURE_POSITIONING.md` has also been reframed so the publication strategy follows the same fail-closed eligibility sequence rather than requiring a covariance quotient after a failed support gate.

This supersedes the earlier six-figure baseline for current development, but it does not alter the gate state `G7=OPEN`, `G8=OPEN`, `G9=OPEN`.

## New article-level methodological result

The observation-space eligibility chain now contains two independent preconditions before covariance whitening or nuisance quotienting:

1. **physical-domain closure** — the observation kernel must lie inside a physically certified theory/provider domain;
2. **support-measure normalizability** — the prospectively chosen positive measure used to define a support fraction must have a finite, non-zero normalizer.

The second condition was added from late DSIR3 work.

### Exp073L — completed normalizability result

Status: `EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L`.

- run: `33049366874`
- artifact: `9637070322`
- digest: `sha256:03a8f63155c40180c81b6472828210408b472463aec244fff8c442ad7cd7c684`
- cutoffs: `ell=120000,240000,480000`
- Wm: `8/8` nonnormalizable, `0` finite
- WW: `8/8` nonnormalizable, `0` finite
- final local exponents: approximately `1.493--1.518`
- final dyadic-shell fractions: approximately `0.645--0.651`
- half-step max relative difference: `1.9428e-6` against frozen tolerance `0.005`

Article interpretation: the absolute-response support fraction is undefined for that frozen route. Do **not** impose a retrospective high-ell cutoff or fiducial-power weighting to force finite normalization.

The analytic interpretation recorded in the project is

`f_shell = 1 - 2^(-p)`

for a dyadic power-law cumulative normalization. With `p~1.5`, every new ultraviolet shell retains an order-unity contribution, consistent with nonnormalizability.

### Exp073G — corroboration only

Status: `FAIL_EXP073G_REPRODUCTION_OR_PROVENANCE`.

Its BOSS Fourier--Bessel operator analysis gives `K_l(k;s) proportional to k^2 j_l(ks)` and `j_l(ks)=O(1/k)`, hence a generic `O(k)` absolute-response tail. The record explicitly has `scientific_support_fail=false`; do not promote Exp073G itself into a scientific support FAIL.

## Constructive path after the negative result

### Exp073M — finite-positive candidate

Status: `FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M`.

Selected three-block route:

- Wm: DES Y3 harmonic galaxy--galaxy lensing
- WW: DES Y1 harmonic cosmic shear
- mm: existing finite BOSS matrix component

All frozen M1--M8 preconditions pass, including finite positive normalization by construction and no downstream leakage. **No physical support fraction has yet been evaluated.** G7/G8/G9 remain OPEN.

### Exp073P2 — exact public-input binding

Status: `PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2`.

Every DES Y1 release object frozen by the route is now SHA256-bound before support output. This includes the `84,075,649,920` byte metacalibration catalogue and the `2,738,626,560` byte source-redshift-binning file.

### Exp073S0 — exact mask/n(z) reproduction

Status: `PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0`.

- run: `33086762750`
- artifact: `9652504743`
- digest: `sha256:c6f84c35e7ade17a6054ad77d4117b64a6c69fbbefe0d0f89e6491bbe88b358e`
- native mask: `Nside=4096`
- retained mask pixels above 0.5: `6,536,725`
- retained sky fraction: `0.0324682643`
- lens n(z): 400 rows, 5 bins
- source n(z): 400 rows, 4 bins

This closes input reproduction prerequisites only. `support_fraction_computed=false`; covariance, nuisance/SVD, and G8 were not read.

## Pending exclusion

Exp073R0 is currently being retried after an infrastructure timeout. Retry configuration commit: `5ee34c3fc80ab1091b7e925d321d880dbadade3c`; latest observed checkpoint documenting the timeout/retry state: `0eea0909b6e286a14d28716211953829203796b0`. Its frozen scientific criteria are unchanged, but it is **not** an article result until a completed result is frozen.

## Paper files added/updated

- `papers/dsir1/evidence/support_operator_eligibility_v0_1.json`
- `papers/dsir1/SUPPORT_OPERATOR_PROVENANCE.md` with P24--P26
- `papers/dsir1/audit_support_operator_eligibility.py`
- `papers/dsir1/sections/observation_space_support_closure.md`
- `papers/dsir1/sections/data_code_reproducibility.md`
- `papers/dsir1/CLAIMS_LEDGER.md`
- `papers/dsir1/build_manuscript_v0_2.py` — Abstract/Introduction/Conclusions now expose the two-stage support-eligibility rule
- `papers/dsir1/LITERATURE_POSITIONING.md` — publication strategy now respects the support gate before covariance
- `.github/workflows/paper-dsir1-build-v0-2.yml`

## Hard boundary

The article still does not claim a completed survey quotient. The required order is now explicit:

`finite positive support measure -> physical support eligibility -> physically justified theory providers -> covariance restriction/whitening -> nuisance quotient -> relation/null tests`.

Current gates: `G7=OPEN`, `G8=OPEN`, `G9=OPEN`.
