# Exp073IW — Article-3 Layer-B exact repeatability diagnostic v0.1

Scope: DSIR only. Support-only +0/+0. Prospectively frozen before execution.

## Motivation
Exp073IV run 34435415273 reproduced repaired Exp073IR as NUMERICALLY_UNRESOLVED with the same qualitative mechanism and component maxima, but its rerun maximum was 0.9998247463807128 rather than the parent 0.9998247463807295. Because Exp073IV prospectively required exact equality, Exp073IV is SUPPORT_INVALID_PLUS_0_PLUS_0. This tiny mismatch MUST NOT be converted into a tolerance-based PASS and MUST NOT alter the frozen Layer-B scientific gate.

## Frozen question
Under one hosted job, one pinned software/build/input environment, execute the unchanged repaired Exp073IR computation twice from fresh independent scratch directories. Determine whether the two complete JSON results are byte-identical and whether the exact convergence accounting values are binary64-identical.

## Frozen execution
- Use ci/exp073ir_article3_real_layerb_common_response_v0_1.py unchanged.
- Preserve the exact pinned baseline, precision, CAMB, patched CLASS-IV d_m route, DES radial files, admitted angular artifacts, Exp073IM manifest, Exp073IP Wm_S3 override and BOSS operators used by Exp073IV.
- Execute two complete runs A and B sequentially in the same GitHub-hosted job, with independent scratch directories and output paths.
- Require both statuses to equal NUMERICALLY_UNRESOLVED_EXP073IR.
- Record SHA256 of each complete JSON file; compare bytes exactly with cmp.
- Record exact max_relative_component_difference from A and B and compare Python float equality exactly. No tolerance, rounding, smoothing or averaging is permitted.
- Preserve covariance_read=false, whitening_read=false, nuisance_read=false and relation_null_read=false in both outputs.

## Outcomes
REPEATABLE_EXACT_PLUS_0_PLUS_0: both complete output files are byte-identical, exact convergence maxima are equal, statuses are NUMERICALLY_UNRESOLVED_EXP073IR and firewalls are intact.

NONREPEATABLE_EXACT_PLUS_0_PLUS_0: both runs are valid NUMERICALLY_UNRESOLVED_EXP073IR with intact firewalls but exact output bytes and/or exact maxima differ. This is a support finding requiring localization of nondeterministic numerical state; it is not a scientific FAIL and does not authorize tolerance.

INVALID_INFRA_PLUS_0_PLUS_0: lineage/input/build/execution/provenance failure or either rerun does not satisfy the frozen status/firewall conditions.

## Scientific firewall
Exp073IW cannot create Layer-B authority, cannot authorize covariance restriction, cannot change h=1e-4, production/dense settings, domains, interpolation, atomization, REL_TOL=1e-3, retained-dimension rule or any frozen DSIR boundary. The repaired Exp073IR scientific state remains NUMERICALLY_UNRESOLVED unless a separately preregistered resolution experiment passes its own frozen scientific contract.
