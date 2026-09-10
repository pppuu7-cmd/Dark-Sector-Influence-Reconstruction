# Exp073JH — Article 3 Layer-B full-support grid-invariant feasibility audit v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER VALIDATED EXP073JG AND BEFORE ANY EXP073JH NUMERICAL OUTPUT.

## Bound authority
Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 107 retained Layer-A rows, f_B=0 under its native production response, but production-vs-dense maximum 0.9998247463807295 > REL_TOL=1e-3. Covariance restriction and Wm_S3 remain unauthorized.

Exp073JG is validated support-only `LOCAL_INTERPOLATION_CURVATURE_OBSERVED_PLUS_0_PLUS_0`, run/job `34485992147 / 102900288767`, artifact `10155745915`, independently verified ZIP SHA256 `e3282ea5f145a273aff63cd70ff74e23cbf6f19960bb83f8390c2c855ae70dbb`. At N=512, all three prospectively frozen higher-order local interpolation rules satisfy the unchanged 1e-3 exact-k probe criterion at both historical worst probes and are exactly invariant between kpd=10 and 20. Linear interpolation does not. This creates no Layer-B scientific authority.

## Purpose
Test whether a structurally selected grid-invariant evaluation architecture can cover the complete already-frozen real Layer-B atomic support of all 107 retained Layer-A coordinate rows while preserving the original finite/nonzero row accounting and kpd=10 versus 20 convergence rule. This is a feasibility audit only; it cannot authorize covariance or replace Exp073IR.

## Prospective architecture selection
Use `cubic_centered` at N=512. This rule is selected prospectively because it is the only JG candidate with a balanced two-sided four-node stencil and therefore does not privilege the left or right side of the target cell. Selection is structural, not because it had the smallest probe error. The fixed nodes remain exactly `np.geomspace(1e-4,0.06664762008318016,512,dtype=float64)` and target k values are never inserted into this shared grid.

For every call to the Layer-B response engine, obtain d_m only at the exact requested shared nodes, verify node identity to LOOKUP_REL_TOL=1e-12, and evaluate each target in x=ln(k) with direct binary64 four-node Lagrange interpolation through `{lo-1,lo,hi,hi+1}`. Targets lacking the complete four-node stencil are not clipped, extrapolated, rounded or silently omitted: their response is non-finite and therefore propagates through the original row-accounting logic as a feasibility failure for any affected row.

## Frozen execution
Reuse the unchanged Exp073IR real-support reconstruction and exact authorities: the same validated Layer-A parent and retained-ID hash, the same Exp073IM radial authority, DES Y1 radial payloads and hashes, BOSS z3 operators and hashes, angular authorities including the admitted Wm_S2/Wm transport authority, exact CAMB pin, exact CLASS-IV pin `ac627d54e9ce196a08878d1ba33999819925d19c`, audited public gauge-invariant d_m exposure, exact baseline and precision files, h=1e-4, z/k domain, atomization and row labels.

The only response-engine substitution is the prospectively frozen shared N=512 cubic-centered interpolation architecture above. Infrastructure capacity patches are exactly `_MAX_NUMBER_OF_K_FILES_ 30 -> 512` and `_ARGUMENT_LENGTH_MAX_ 1024 -> 32768`; no equation, cosmological parameter, finite-difference arithmetic, atom support, operator, z/k boundary, source definition or acceptance threshold changes.

Production density remains k_per_decade_for_pk=10 and dense cross-check remains 20. REL_TOL remains exactly 1e-3. Layer-B invalid-row fraction threshold remains <=0.05 and retained dimension remains >=15. The original Exp073IR response arithmetic and real-support row accounting are reused unchanged apart from the response-engine substitution.

## Frozen interpretation
The audit is `FULL_SUPPORT_GRID_INVARIANT_FEASIBLE_PLUS_0_PLUS_0` only if all of the following hold: the exact 107-row identity/order authority is preserved; no row labels change between kpd10 and kpd20; production/dense finite/nonzero status agrees; max relative component difference is <1e-3; Layer-B invalid-row fraction <=0.05; retained-after-Layer-B >=15; and every target contributing to every retained row has a complete requested-node cubic stencil. No covariance, whitening, nuisance, relation/null or held-out quantity may be read.

If any target lacks the full stencil, any row becomes invalid beyond the frozen fraction, or the kpd convergence criterion fails, classify `FULL_SUPPORT_GRID_INVARIANT_NOT_FEASIBLE_PLUS_0_PLUS_0`; this is a support result, not a scientific failure. If lineage/hash/build/interface/parent identity fails, classify `INVALID_INFRA_PLUS_0_PLUS_0`.

Even a feasible result creates no Layer-B scientific authority. It only permits a later separately preregistered scientific rerun that rebinds the estimator prospectively and reruns the complete frozen Layer-B gate from scratch. A non-feasible result requires further grid-domain/boundary mechanism work; no density extrapolation or tolerance rescue is permitted.

All outcomes are +0/+0. Global frozen DSIR boundaries remain unchanged: 0.295<=z<=2.33; 0<k<=0.06664762008318016 Mpc^-1; Layer-A operator_f_invalid<=0.05; Layer-B invalid-row fraction<=0.05; retained dimension>=15; DES NSIDE=4096; ell=0..12287; 39 bands; Wm TE<-TE; WW EE<-EE; canonical <f8 [39,12288]; exact-threshold ambiguity numerically_unresolved; no effective ell/z/k, fiducial-P, tolerance, rounding, smoothing or averaging rescue.
