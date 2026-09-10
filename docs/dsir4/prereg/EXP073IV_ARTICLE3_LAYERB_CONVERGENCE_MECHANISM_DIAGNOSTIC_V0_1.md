# Exp073IV — Article 3 Layer-B convergence mechanism diagnostic v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER EXP073IR RETURNED NUMERICALLY_UNRESOLVED, BEFORE ANY EXP073IV NUMERICAL VALUE IS PRODUCED.

## Parent result

Bind exactly repaired Exp073IR run/job `34432102035 / 102729564736`, head `38604061abe6cbcccbf9614b22e3ca0ca6a9ec0f`, artifact `10134905199`, artifact ZIP SHA256 `165a85c8348fc4fc4c52f3926aa1a46989179efc8413a059f9fc2d6aa9dfbb21`, status `NUMERICALLY_UNRESOLVED_EXP073IR`.

The parent has 107/107 production rows finite/nonzero, `f_B=0`, no row-label change and no finite/nonzero-status change, but frozen production-vs-dense max relative component difference `0.9998247463807295 > 1e-3`; covariance restriction remains unauthorized.

## Purpose

Localize the already-observed convergence failure without altering or reinterpreting the frozen Exp073IR scientific gate. Exp073IV is diagnostic/support-only `+0/+0` and cannot itself create Layer-B PASS/FAIL, covariance authority, model authority or manuscript selection authority.

## Frozen diagnostic

Re-execute the exact Exp073IR v0.1 producer with the same pinned CLASS-IV source, audited public `d_m` patch, CAMB source, DES-Y1 radial payloads, angular inputs, BOSS operators, baseline, precision file, `h=1e-4`, production `k_per_decade_for_pk=10`, dense control `20`, domains, interpolation and atomization.

Instrumentation may observe only values already compared by the frozen `compare_response(prod,dense,conv)` operation. It must record the maximum relative discrepancy separately for component 0 (`abs_dDelta_m_dalpha_left`) and component 1 (`abs_dDelta_m_dbeta_symmetric`), including exact dense-call redshift, exact target k in Mpc^-1, production value, dense value, relative discrepancy, and response-vector length. It must also record the global maximum using the same denominator `max(abs(prod),abs(dense))` as Exp073IR.

Instrumentation is observational only: no solver parameter, response arithmetic, interpolation, threshold, atom set, row classification or parent output may be changed. No covariance, whitening, nuisance, relation-null or downstream selection input may be read.

## Accounting

PASS token for the diagnostic itself: `PASS_EXP073IV_LAYERB_CONVERGENCE_MECHANISM_DIAGNOSTIC_V0_1`.

Diagnostic PASS requires: parent rerun status remains exactly `NUMERICALLY_UNRESOLVED_EXP073IR`; rerun convergence max matches the parent value under exact binary64 evaluation; both component diagnostics are finite and identify a sampled maximum; covariance firewall remains intact. Any source/provenance/build/instrumentation mismatch is support/infrastructure INVALID `+0/+0`, never a scientific FAIL.

Exp073IV PASS does not authorize changing `REL_TOL=1e-3`, `h`, k sampling, domains or the scientific classification. Any prospective resolution must be separately preregistered after the mechanism is known.