# DSIR recovery V58 — Exp073IR numerically unresolved; Exp073IV diagnostic running

Updated: 2026-09-10. Scope: DSIR only.

## Newly closed
Repaired Exp073IR Layer-B run/job `34432102035 / 102729564736`, head `38604061abe6cbcccbf9614b22e3ca0ca6a9ec0f`, completed workflow SUCCESS but scientific classification is exactly `NUMERICALLY_UNRESOLVED_EXP073IR`, not PASS/FAIL. Artifact `10134905199`, ZIP SHA256 `165a85c8348fc4fc4c52f3926aa1a46989179efc8413a059f9fc2d6aa9dfbb21`.

Raw result: invalid rows 0/107, `f_B=0`, retained 107; finite/nonzero status unchanged; row labels unchanged; BOSS dense-z disagreement false; frozen convergence max relative component difference `0.9998247463807295` exceeds `1e-3`, therefore convergence PASS is false and covariance restriction remains unauthorized. The audited gauge-invariant public `d_m` route and covariance firewall are intact.

## Current process
Exp073IV support-only convergence-mechanism diagnostic v0.1 is prospectively frozen at commit `1e3398631973bc410a4c36a1bf06dd558a925863`; diagnostic implementation commit `c41ecdcca7fea456975868aa16bee38ecdda4ce4`; workflow commit `628daeb44c84a8844f50540ec852222a95a2834d`; trigger/head `f20b31bef9178ab3097ed606d8fcc983952222c8`.

Authoritative active run/job: `34435415273 / 102739350045`, GitHub-hosted ubuntu-24.04, state QUEUED at latest inspection, checkpoint N/A, home/self-hosted ownership none. The diagnostic re-executes the frozen IR arithmetic and only records per-component argmax location/value for the already-required production-vs-dense comparison. It is `+0/+0` only and cannot authorize covariance or alter `REL_TOL`, h, domains, atomization, interpolation or scientific classification.

## Next transition
Terminal-consume Exp073IV: inspect raw log and artifact/digest. A valid diagnostic PASS must reproduce parent `NUMERICALLY_UNRESOLVED_EXP073IR` and exact max `0.9998247463807295`, identify both component maxima and preserve the covariance firewall. Then use only that mechanism evidence to prospectively define the smallest scientifically neutral numerical-resolution test. Never weaken `1e-3` or treat the diagnostic as scientific Layer-B PASS.

All earlier admitted DSIR authority and frozen global boundaries remain unchanged.