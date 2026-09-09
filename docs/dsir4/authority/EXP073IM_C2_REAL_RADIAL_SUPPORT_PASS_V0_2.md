# Exp073IM — C2 real radial-support PASS v0.2

Date: 2026-09-10. Scope: DSIR Article 3 only.

Status: **PASS_EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_2**.

This receipt records the first valid classifying Exp073IM execution after transport-only carrier repairs. Earlier INVALID_FOR_SCIENCE attempts remain immutable infrastructure outcomes and are not scientific FAILs.

## Valid classifying execution

- workflow: `.github/workflows/exp073im-c2-real-radial-support-v0-2.yml`;
- run/job: `34419165956 / 102690618922`;
- head: `c469a9aab56f99822fd65c7027877275c1247d4d`;
- result artifact: `10130241439`;
- GitHub artifact digest: `sha256:3325bab0faa821c5ca3b13b4cd64d3d58c323e56a6f3e44952be84bfbc477156`;
- input manifest: `EXP073IM_C2_REAL_INPUT_MANIFEST_V0_4`;
- representation: `FACTORIZED_BROAD_SUPPORT_V0_2`.

## Frozen result

- `scientific_radial_pass=true`;
- angular authorities verified: `14`;
- Wm rows: `780`;
- WW rows: `390`;
- total DES broad-support rows: `1170`;
- Wm radial-index count: `20`;
- WW radial-index count: `10`;
- minimum Wm radial normalization: `2.667960373417456e-06`;
- minimum WW radial normalization: `451.6753186145717`;
- ordered broad-row manifest SHA256: `ea471772cf8b09597115445b8be5e5362a6fccba2099d6f00e011d1dd997d450`;
- deterministic permutation replay: `true`.

## Firewall evidence

The classifying receipt records:

- `effective_ell_override=false`;
- `effective_z_override=false`;
- `effective_k_override=false`;
- `physical_support_evaluated=false`;
- `covariance_read=false`;
- `nuisance_read=false`;
- `relation_null_read=false`.

Thus no downstream Article-3 result was used to rescue or tune the radial gate.

## Gate consequence

`G_RADIAL_SUPPORT=PASS` for the frozen C2 Article-3 route.

Article-3 mandatory-gate closure advances from `3/9 = 33.3%` to **`4/9 = 44.4%`**.

This PASS authorizes prospective execution of the separately frozen `G_PHYSICAL_SUPPORT` gate. It does not itself score physical support, covariance whitening, nuisance quotient, relation/null, final observational validation, or any DSIR-4 model-comparison conclusion.
