# Exp073IX — Article 3 Layer-B instrumentation-neutrality diagnostic v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER EXP073IW EXACT REPEATABILITY PASS AND BEFORE ANY EXP073IX NUMERICAL VALUE IS PRODUCED.

## Bound authority

Repaired Exp073IR run/job `34432102035 / 102729564736`, artifact `10134905199`, remains `NUMERICALLY_UNRESOLVED_EXP073IR` with exact convergence maximum `0.9998247463807295`, 0 invalid rows, `f_B=0`, retained 107 and covariance restriction unauthorized.

Exp073IV run/job `34435415273 / 102739350045` remains `SUPPORT_INVALID_PLUS_0_PLUS_0` because its instrumented rerun produced convergence maximum `0.9998247463807128`, not exact-binary64 equal to the parent.

Exp073IW run/job `34439055218 / 102750048552`, head `70cf145eae559c57cbc2c8105c9d4c05ce097fb1`, artifact `10137307858`, artifact ZIP SHA256 `836cd19ef5b0c1a1294b995712a16c30920e4beff1c0f5f5b820de8bed8ceac2`, is `REPEATABLE_EXACT_PLUS_0_PLUS_0`: its A/B outputs are byte-identical with SHA256 `6dea43dcc0eadaf91887f181732d20dceef04866d5687aa231b747312fec0cb1`, and both convergence maxima equal exactly `0.9998247463807295`.

## Purpose

Resolve whether the Exp073IV parent mismatch was caused by the observational instrumentation itself or by build/environment drift. This is required before any numerical-resolution experiment. Exp073IX is support-only `+0/+0`; it cannot create Layer-B, covariance, model, or manuscript authority.

## Frozen same-job A/B test

In one GitHub-hosted `ubuntu-24.04` job, with the same pinned CAMB commit, pinned CLASS-IV commit plus audited `d_m` exposure patch, DES-Y1 files and hashes, angular/Exp073IM artifacts, BOSS operators, baseline and precision file used by Exp073IW:

1. Execute the repaired Exp073IR directly once into an independent scratch directory/output.
2. Without rebuilding or changing any input, execute Exp073IR once through the exact existing Exp073IV diagnostic wrapper into a second independent scratch directory/output.
3. Read only the direct and instrumented-parent outputs plus the Exp073IV diagnostic JSON. No covariance, whitening, nuisance, relation-null, selection, or downstream data may be read.
4. Compare exact binary64 convergence maxima and exact output bytes. No tolerance is permitted for this diagnostic comparison.

The scientific gate remains untouched: `REL_TOL=1e-3`, `h=1e-4`, production/dense k sampling, domains, interpolation, atomization and all frozen acceptance criteria remain exactly unchanged.

## Frozen classifications

- `INSTRUMENTATION_CAUSAL_PLUS_0_PLUS_0`: direct output is valid unresolved and its maximum equals parent exactly, while the same-job Exp073IV-instrumented parent differs exactly. This isolates the previous tiny cross-run mismatch to instrumentation, not scientific arithmetic.
- `INSTRUMENTATION_NEUTRAL_PLUS_0_PLUS_0`: both direct and instrumented parent are valid unresolved and are exact-equal on the parent maximum; previous IV mismatch is not reproduced and environment/build provenance remains the next diagnostic target.
- `ENVIRONMENT_DRIFT_PLUS_0_PLUS_0`: the direct same-job output itself does not reproduce the authoritative parent maximum while retaining valid unresolved/firewall state.
- `INVALID_INFRA_PLUS_0_PLUS_0`: lineage/input/build/status/firewall failure prevents the comparison.

All outcomes are support-only. No outcome authorizes covariance restriction or changing the scientific convergence threshold. After `INSTRUMENTATION_CAUSAL_PLUS_0_PLUS_0`, the next permitted work is a prospectively frozen numerical-resolution mechanism test using the uninstrumented producer. After `INSTRUMENTATION_NEUTRAL_PLUS_0_PLUS_0` or `ENVIRONMENT_DRIFT_PLUS_0_PLUS_0`, environment/build provenance must be isolated further before numerical resolution.