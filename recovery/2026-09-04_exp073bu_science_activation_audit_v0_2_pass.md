# DSIR immutable recovery — Exp073BU science activation hosted audit v0.2 PASS

Date: 2026-09-04. Scope: DSIR only; RTK/RQIR excluded.

## Authoritative hosted audit

- status: `PASS_EXP073BU_SCIENCE_ACTIVATION_HOSTED_AUDIT_V0_2`
- run/job/head: `33884937777 / 101062302450 / 0c97666f11079f1bc21346c6666cc6236c1c5ebd`
- artifact: `9941423648`
- artifact digest: `sha256:72b4de809da69992cee199a036e9b96ee76b9b33b07c28358ffe29e26554340b`
- science workflow: `.github/workflows/exp073bu-wm-s3-fresh-ab-exact-science-v0-2.yml`
- science workflow blob: `359df0f9779425a6fb2241ed477c07650eeec36c`
- activation prereg: `experiments/073bu_wm_s3_selfhosted_science_activation_v0_2_prereg.md`
- activation prereg blob: `58377eb593e7a48302106efa66be576f667ac19a`
- original science prereg blob: `816542c7eb7a8ba4e72d6e01228aa62d05c7c805`
- production driver blob: `5c8d5d3463e455389a1ca3df2639bf06a3b7b603`
- fresh helper blob: `73ef04c479547dc8e2e89c9f511f1a55fae3ed64`
- exact adapter blob: `dafe86086a470c852106f0d4ecccbda1d389e397`
- component lineage blob: `0d6d6e882d1a4cf1ff79fbe8227a4f2b460c7e40`
- full-stock mmap downstream blob: `acafb095deafae7602101d8305e239341010ba79`
- science launcher blob: `1a54ad89d32dd217443bc3062a6215bf10e8b17d`
- inherited CX v0.4 A1 recovery blob: `43b658028f74b7a0b52fca8261beeb58026d8ffc`

Every hosted-audit step completed success: exact blob binding; validation-scope repair; manual-only activation; exact R1 artifact naming; single self-hosted job contract; original exact PASS token and comparator fields; frozen science-boundary preservation; receipt and artifact emission.

## Historical v0.1 infrastructure failure

The historical v0.1 science workflow blob `62774cbbe8073aeeb3f66e04a50c891173f91a23` and validation-level run `33883760874` remain immutable infrastructure history. That workflow was rejected before jobs because it used a `runner` context in job-level `env`. No Exp073BU A/B numerical science ran and no Wm_S3 authority was created. A first hosted-audit-v0.2 attempt `33884780695` was also rejected at workflow validation because the audit source itself contained a literal malformed Actions expression while searching for the forbidden pattern; that audit-shell defect was repaired before any hosted PASS authority or DES-scale numerics existed.

## Consequence

The v0.2 activation shell is authorized for explicit manual dispatch on `main`. The manually dispatched run must still pass its own hosted exact-binding/noncompetition preflight and then the live self-hosted exclusivity/process-ledger gates immediately before numerics. Only one self-hosted job may own `DSIR-HOME-PC`.

If all live gates pass, the single home job executes fresh replica A followed by fresh replica B under the original isolated namespaces and only then scores whole canonical `<f8 [39,12288]` SHA256 equality plus `numpy.array_equal`.

Allowed terminal science classes remain exactly `PASS`, `SCIENTIFIC_REPEATABILITY_FAIL`, `INFRASTRUCTURE_INCOMPLETE`, and `BLOCKED`. No tolerance, ULP, rounding, smoothing, averaging, effective-scale, fiducial-P, preferred-replica, or rerun-to-prefer rescue is allowed.

Classification of this hosted audit: support/activation authority only, accounting `+0/+0`; `science_numerics_executed=false`; `wm_s3_authority_created=false`. Wm_S3 scientific authority remains absent until a valid terminal Exp073BU comparator result exists.
