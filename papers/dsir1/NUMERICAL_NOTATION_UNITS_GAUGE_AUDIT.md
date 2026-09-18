# DSIR-I numerical / notation / units / gauge audit v0.1

**Date:** 2026-08-27  
**Scope:** publication audit of `NUMERICAL_METHODS_APPENDIX.md`, the assembled manuscript conventions, and the frozen provider/support provenance.  
**Verdict:** `PASS_PAPER1_NUMERICAL_NOTATION_UNITS_GAUGE_AUDIT_V0_1` with the explicit unit-boundary rules below. This is a publication/reproducibility PASS, not a new scientific gate.

## 1. Dimensional-response conventions

The central morphology coordinates are logarithmic ratios and therefore dimensionless:

- anchored background response `r_E`;
- matter-power response `r_Delta`;
- additive components `mu`, `T`, `tau`, `I`;
- `chi_I` and `eta_I`.

Response angles are reported in degrees. Turning angles are sampled normalized-direction changes, not continuous Frenet curvature.

No manuscript statement may treat `chi_I`, `eta_I`, an angle, or a PCA fraction as an S/N or likelihood significance.

## 2. Two k-unit conventions are intentionally different

This is the highest-risk notation issue and is frozen explicitly here.

### Theory-response atlas

The low-k atlas and WDM high-k block are expressed in

`h Mpc^-1`.

For example the common low-k theory grid is

`{0.001, 0.003, 0.01, 0.03, 0.1} h Mpc^-1`.

### Physical observation-support audit

The certified common physical provider rectangle uses **physical** wavenumber

`Mpc^-1`,

with frozen upper boundary

`k <= 0.06664762008318016 Mpc^-1`

and redshift rectangle

`0.295 <= z <= 2.33`.

These two conventions must never be compared numerically without the frozen conversion. The C5 raw-k provenance audit established that the upstream raw accessor coordinate is in the corresponding `k/h` convention and that the physical coordinate used by DSIR is obtained as

`k_physical = k_raw * h`,

while the power values themselves are not rescaled by this coordinate conversion.

Therefore a table or figure using `h Mpc^-1` is a theory-response-domain statement unless it explicitly says otherwise; a support threshold written in `Mpc^-1` is an observation/provider-domain statement.

## 3. Redshift and angular conventions

Redshift `z` is dimensionless. The main low-k and WDM atlas uses the seven frozen nodes

`{0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33}`.

For finite harmonic observation operators, angular multipoles are dimensionless and the physical Limber mapping, when invoked by the frozen support route, is

`k = (ell + 1/2) / chi(z)`

under the pinned background convention. Effective-ell substitution is not an authorized replacement for the exact finite bandpower response.

## 4. Gauge convention

The production low-k matter response is based on the **comoving total-matter** source/power response under matched solver/provider settings. Gauge-specific density or velocity variables are not silently substituted for this coordinate.

Gauge/conservation regressions are separate validation controls. A gauge-dependent auxiliary quantity is not promoted to a universal DSIR coordinate merely because it is available from a solver.

## 5. Metric/Weyl and signed-cross conventions

Matter, Weyl/lensing and metric-slip blocks remain distinct physical channels. The manuscript must not infer Weyl information from matter power through an unstated GR closure when an independent metric response is being tested.

For observational Wm production, the final cross response remains **signed**. Positivity is introduced only for the support envelope through the absolute final response. This distinction prevents a support diagnostic from changing the physical sign of the production observable.

## 6. Mask versus zero

An undefined model/channel/domain cell is a **mask**, not the number zero. This applies in particular to disjoint low-k/high-k blocks. Zero imputation would alter distances, angles, rank and the additive projection and is forbidden by the Paper-I block-aware contract.

A literal numerical zero is interpreted as physical only under a provider/model contract that actually defines and validates the zero limit.

## 7. Provider identity and solver-version policy

The paper does not identify a provider merely by a floating package label. Reproducible identity is the tuple of:

1. pinned source/implementation commit where applicable;
2. exact workflow/run;
3. immutable result artifact and digest;
4. frozen numerical/scientific acceptance contract.

This policy is necessary because the C3 and C5 histories each contain an original scientific FAIL followed by a separately frozen corrective/provider PASS. A later provider does not rewrite the earlier result.

Where a journal appendix lists a human-readable solver name/version, that label is descriptive; the immutable source/run/artifact bindings in `PROVENANCE_MATRIX.md` remain authoritative.

## 8. Physical support before statistics

Support selection is upstream of covariance and nuisance quantities. The frozen support rules include:

- physical rectangle `0.295 <= z <= 2.33`, `k <= 0.06664762008318016 Mpc^-1`;
- leakage criterion `f_invalid <= 0.05`;
- minimum retained dimension 15 where specified by the preregistration;
- no fiducial-`P(k)` weighting;
- no post-hoc k/ell cutoff;
- no covariance/SVD/relation/held-out data in support selection;
- no crop-before-normalization;
- signed Wm production with positive absolute support envelope.

The restricted covariance/whitener may be constructed only after a genuine support PASS for the corresponding realized operator.

## 9. Precision and tolerance language

The manuscript correctly avoids one universal numerical epsilon. Distinct contracts use distinct frozen tolerances. Examples include machine/state/repeatability controls around `1e-12`, provider-specific power-closure criteria, and the independent physical-support leakage threshold `0.05`.

No tolerance may be changed because a result narrowly misses it. This is explicitly illustrated by the preserved C5 q=1 exact-GR-limit FAIL and the separately frozen later provider certification.

## 10. Publication wording rules produced by this audit

Use:

- `h Mpc^-1` for the theory-response grids;
- `Mpc^-1` for the certified physical support rectangle;
- “theory-response angle” unless a real survey quotient has actually been completed;
- “masked/undefined” rather than “zero” for absent blocks;
- “signed Wm production response” versus “absolute positive support envelope”;
- “provider/source-run-artifact binding” rather than only a package version.

Do not use:

- a bare `k` number without a unit in cross-domain discussion;
- “observable significance” for raw response angles;
- “GR closure” as a substitute for an independent Weyl/slip channel;
- “support PASS” for reproduction/provenance prerequisites;
- a physical-support fraction after an infrastructure/provenance failure.

## 11. Closure

No unresolved units/gauge inconsistency was found that changes a frozen DSIR-I scientific result. The main publication risk was the coexistence of `h Mpc^-1` theory grids and `Mpc^-1` physical-support coordinates; the distinction and conversion are now frozen explicitly.

This audit closes the Paper-I numerical/notation/units/gauge review for the declared scope. Any later Paper-II observation-space result must run a fresh operator-specific units/provenance audit rather than inherit this PASS automatically.
