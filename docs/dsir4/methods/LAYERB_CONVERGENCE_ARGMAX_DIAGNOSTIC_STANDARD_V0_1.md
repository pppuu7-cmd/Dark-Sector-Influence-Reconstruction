# Layer-B convergence argmax diagnostic standard v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / numerical support diagnostics only.

## Purpose
For any future Layer-B common-grid convergence run launched after Exp073JL, record the location and absolute scale of the atom that attains the already-frozen maximum relative component difference. This is diagnostic metadata only. It MUST NOT modify the convergence statistic, acceptance threshold, physical domain, masks, interpolation rule, finite-difference arithmetic, retained-row accounting, or any scientific classification.

## Frozen diagnostic fields
Alongside the unchanged scalar
`abs(a-b)/max(abs(a),abs(b))`, record for the maximizing valid atom:
- observational block: DES or BOSS;
- coordinate_id when uniquely attributable, otherwise union/support context;
- response component: alpha-left or beta-symmetric;
- physical z and k in Mpc^-1;
- coarse value and fine value;
- absolute difference;
- denominator `max(abs(coarse),abs(fine))`;
- relative difference;
- grid identities and requested-node counts;
- whether the same atom also maximizes absolute difference.

Also report response-blind summary diagnostics over all compared positive finite atoms: minimum, median and selected fixed quantiles of the denominator, plus the number of atoms whose denominator is below fixed powers of ten (`1e-12`, `1e-10`, `1e-8`, `1e-6`, `1e-4`). These summaries are explanatory only and cannot exclude atoms from the frozen maximum.

## Interpretation boundary
A maximum associated with a very small denominator may explain slow convergence of the relative maximum, but it does not authorize clipping, flooring, averaging, dropping atoms, changing the metric or weakening `REL_TOL=1e-3`. Any alternative numerical architecture would require a separate prospective preregistration and cannot retroactively alter Exp073IR/JJ/JK/JL.

This standard is frozen before any Exp073JL numerical result is inspected. It does not apply retroactively to Exp073JL and does not change its decision rule.
