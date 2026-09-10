# Exp073IR — Article 3 real Layer-B common-response preregistration v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER LAYER-A PASS AUTHORITY EXISTS, BUT BEFORE ANY REAL LAYER-B RESPONSE VALUE OR CLASSIFICATION IS PRODUCED.

## Purpose

Close the second half of the already-frozen Article-3 physical-support hierarchy on exactly the inherited Layer-A retained set `S_op`. This experiment does not re-score broad geometry. It tests only whether the frozen C2 local tangent model has a finite, nonzero common final-response field on every active in-domain support atom of each retained observation row.

## Immutable parent

Bind exactly `docs/dsir4/authority/EXP073IQ_ARTICLE3_REAL_LAYERA_SUPPORT_PASS_V0_1.json`:

- run/job `34423479633 / 102703685034`;
- artifact `10131794281`;
- artifact digest `sha256:ac959926639d3b46ecfe114e396ce03cb20a0763ef2781db454408d8ad0759df`;
- token `PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1`;
- inherited candidate count `1410`;
- inherited `S_op` count `107` = 53 DES + 54 BOSS;
- inherited retained-ID SHA256 `44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7`;
- full-order SHA256 `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`.

No Layer-A row may be added, removed, reordered, recentered or reweighted by Layer B.

## Frozen response components

The ordered real Layer-B component vector is fixed to the two pre-existing C2 local-tangent directions:

1. `abs_dDelta_m_dalpha_left`;
2. `abs_dDelta_m_dbeta_symmetric`.

These names are not chosen from the observed `S_op`. They instantiate the derivative definitions already frozen in `C2_IDE_LOCAL_TANGENT_CONE_PREDICTION_V0_1.md`:

- `h = 1e-4` exactly;
- alpha: `(Delta_m(alpha=-h,beta=0)-Delta_m(ref))/(-h)`;
- beta: `(Delta_m(alpha=0,beta=+h)-Delta_m(alpha=0,beta=-h))/(2h)`.

No component may be dropped after numerical inspection.

## Gauge/source-route supersession

The pinned solver remains exactly `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

The prior native-source audit proved that standard CLASS-IV `index_tp_delta_m` / public transfer `d_m` is already the gauge-invariant total-matter overdensity. Therefore Exp073IR prospectively selects the mathematically equivalent route explicitly anticipated by that audit: consume the already gauge-invariant `d_m` directly and DO NOT apply the external `+3 aH theta_m/k^2` correction a second time.

This supersedes only the source-input binding of the support-only Exp073GK arithmetic generator for Exp073IR. It does not change the C2 physical model, coupling directions, baseline cosmology, finite-difference steps or gauge-invariant target variable.

Raw `delta_idm_iv`, `index_tp_delta_tot`, or a second gauge correction are forbidden.

## Exact atom geometry

Layer B uses the broad-row atom semantics frozen in `ARTICLE3_BROAD_ROW_LAYERB_SCHEMA_AMENDMENT_2026-08-30.md`.

For each inherited row `i in S_op`, the active atom set remains exactly

`A_i^D = {a: operator_abs_weight[a] > 0 and (z[a],k[a]) in D}`

with

`D = {0.295 <= z <= 2.33, 0 < k <= 0.06664762008318016 Mpc^-1}`.

No effective `ell`, `z` or `k` is permitted.

DES atom geometry/weights must be reconstructed from the exact same angular authorities and DES-Y1 radial kernels used by Exp073IQ. BOSS atom geometry/weights must inherit the exact Exp073W `C=W@M` true-k support and frozen z3 survey-bin support used by Exp073IQ. Layer B may not inspect covariance to define atoms.

## Transfer evaluation at atom coordinates

`class_iv` public `get_transfer(z, output_format='class')` with output containing `mTk` is the admitted source of gauge-invariant `d_m` transfer samples. Requested redshifts must be evaluated directly by the pinned solver with `z_pk` covering the full frozen domain.

Because the finite survey atoms do not generally coincide with the solver's native k sampling, the only admitted k evaluation is a prospectively controlled interpolation of the solver-native `d_m(k,z)` transfer table in `ln k`, separately for each of the four frozen model points. The production route uses piecewise-linear interpolation in `ln k`; no extrapolation is allowed.

Interpolation is an implementation of this new broad-atom Layer-B producer only. It does not retroactively interpolate the old 28-point C2 prediction artifact.

A convergence control must rerun with a prospectively denser CLASS k sampling. Scientific Layer-B classification is admissible only if:

- every active atom remains bracketed by native solver k samples in both runs;
- every row's valid/invalid label is identical between production and dense control;
- no component changes finite/nonzero status;
- max relative component difference over cells with magnitude safely above numerical zero is <= 1e-3.

Otherwise classify `NUMERICALLY_UNRESOLVED_EXP073IR`, not PASS/FAIL.

## Layer-B classification

For every active in-domain atom, compute the two absolute finite-difference components above.

A row is Layer-B valid iff:

- its active set is non-empty; and
- BOTH frozen components are finite and strictly greater than zero on EVERY active in-domain atom.

No epsilon may turn a zero into a positive value. Exact zero, NaN or Inf invalidates that row.

Let

`f_B = N_invalid_rows / 107`.

Scientific PASS requires inclusively:

- `f_B <= 0.05`; and
- at least 15 rows remain after Layer-B invalid rows are removed.

Tokens:

- `PASS_PHYSICAL_SUPPORT_ARTICLE3`;
- `FAIL_PHYSICAL_SUPPORT_ARTICLE3`;
- `NUMERICALLY_UNRESOLVED_EXP073IR`;
- `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT`.

A scientific FAIL is emitted only for a valid execution in which the frozen common-response rule fails. Schema/provenance/hash/dependency failures are INVALID/INCOMPLETE, never scientific FAIL.

## Downstream firewall

Exp073IR must not read covariance, inverse covariance, whitening, nuisance vectors/SVD/rank, relation/null statistics, G7/G8/G9 conclusions, DSIR-4 matrix outcomes, or manuscript selection metadata.

Only `PASS_PHYSICAL_SUPPORT_ARTICLE3` on the exact inherited Layer-A authority authorizes Article-3 covariance restriction/whitening.
