# Exp073IY — Article 3 Layer-B cross-build reproducibility diagnostic v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER EXP073IX INSTRUMENTATION-NEUTRAL PASS AND BEFORE ANY EXP073IY NUMERICAL OUTPUT IS PRODUCED.

## Bound authority

Exp073IR run/job `34432102035 / 102729564736`, artifact `10134905199`, remains `NUMERICALLY_UNRESOLVED_EXP073IR` with exact convergence maximum `0.9998247463807295`, 0 invalid rows, `f_B=0`, retained 107, and covariance restriction unauthorized.

Exp073IX run/job `34443359314 / 102762823702`, artifact `10138827841`, is `INSTRUMENTATION_NEUTRAL_PLUS_0_PLUS_0`: direct and IV-wrapped outputs are byte-identical, both SHA256 `6dea43dcc0eadaf91887f181732d20dceef04866d5687aa231b747312fec0cb1`, with exact maximum `0.9998247463807295`.

Historical Exp073IV remains `SUPPORT_INVALID_PLUS_0_PLUS_0` with a tiny cross-run mismatch. Its logged semantic environment matches the repaired Exp073IR/IX lineage: Ubuntu 24.04.5 / image `20260907.300.1`, provisioner `20260828.587`, numpy 1.26.4, Cython 0.29.37, scipy 1.17.1, astropy 7.2.2, CAMB source `fa3f097343fbbe427cc04b4f5f0041c22c6ec764`, CLASS-IV source `ac627d54e9ce196a08878d1ba33999819925d19c`, audited `d_m` exposure patch, and the same input hashes. CAMB wheel archive SHA varies between builds, including builds that reproduce the parent exactly, so archive SHA difference alone is not scientific evidence.

## Purpose

Determine prospectively whether independently rebuilt hosted environments reproduce the authoritative uninstrumented Exp073IR output exactly. This isolates cross-build reproducibility before any numerical-resolution experiment. This diagnostic is support-only `+0/+0` and cannot create Layer-B, covariance, model, or manuscript authority.

## Frozen execution

Run two independent GitHub-hosted `ubuntu-24.04` jobs, `A` and `B`. Each job must independently:

1. install the exact frozen software stack used by Exp073IX;
2. fetch exact CAMB commit `fa3f097343fbbe427cc04b4f5f0041c22c6ec764` and CLASS-IV commit `ac627d54e9ce196a08878d1ba33999819925d19c`;
3. apply the exact audited compatibility and public gauge-invariant `d_m` exposure patches;
4. verify the same DES/BOSS/angular/Exp073IM input hashes and authorities;
5. execute the repaired Exp073IR directly, uninstrumented, with the unchanged frozen scientific arithmetic;
6. record output bytes/SHA256, exact convergence maximum, environment identifiers, package versions, source SHAs, and hashes of the installed/built CAMB and CLASS-IV Python extension/binary payloads that can be located deterministically.

A verifier job must compare A, B and the authoritative repaired Exp073IR artifact. Exact output-byte equality is required; no tolerance is permitted for reproducibility comparison.

## Science firewall

The scientific gate is unchanged: `REL_TOL=1e-3`, `h=1e-4`, production/dense k sampling, source definitions, interpolation, redshift/k domain, atomization, row set and all acceptance criteria remain unchanged. No covariance, whitening, nuisance, relation-null or manuscript selection data may be used. Varying a frozen scientific parameter to obtain agreement is forbidden.

## Frozen classifications

- `CROSS_BUILD_EXACT_PLUS_0_PLUS_0`: A and B are valid unresolved executions, each is byte-identical to the authoritative repaired Exp073IR artifact, and their exact convergence maxima equal `0.9998247463807295`.
- `CROSS_BUILD_DRIFT_PLUS_0_PLUS_0`: both executions are otherwise valid unresolved but at least one output is not exact-equal to the authoritative parent or to the other rebuild. Record the first differing provenance/binary field if available; do not alter science.
- `INVALID_INFRA_PLUS_0_PLUS_0`: lineage, dependency, input hash, build, artifact, firewall or verifier failure prevents valid comparison.

All outcomes are support-only. No outcome by itself authorizes covariance restriction. After `CROSS_BUILD_EXACT_PLUS_0_PLUS_0`, the historical IV mismatch is bounded as a non-reproduced transient outside the frozen semantic inputs, and the next permitted work is a prospectively frozen uninstrumented numerical-resolution mechanism diagnostic. After `CROSS_BUILD_DRIFT_PLUS_0_PLUS_0`, isolate the first reproducible binary/environment source of drift before numerical-resolution work.
