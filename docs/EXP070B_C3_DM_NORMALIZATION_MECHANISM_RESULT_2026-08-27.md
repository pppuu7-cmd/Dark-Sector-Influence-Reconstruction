# Exp070B result — C3/GDM D_m normalization mechanism audit

Date: 2026-08-27

## Classification

Primary frozen mechanism label:

`INTERPOLATION_DOMINATED`

Exp070A remains permanently `FAIL_C3_GDM_READONLY_DM_PHYSICAL_POWER_BRIDGE_V0_1`. Exp070B is a mechanism audit only and does not reclassify it.

## Immutable execution provenance

- PR: #77
- workflow run: `33016744264`
- workflow artifact id: `9624845938`
- artifact digest: `sha256:92d4bf3624c67dd455ce668e5ab14a04b2ab8c275a892f6715a668498c52bef7`
- solver: `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`
- preregistration commit: `e386c0b742067d309a0116b4629b5f85ce3b55fd`
- implementation head used by the run: `94689db61ce995b4324529443e1dc3ffe102bc80`

## Frozen mechanism results

For every one of the three frozen C3 cases (`cs2=0,1e-6,1e-5`) and every one of the seven frozen redshifts, the primary audit retained 33 common native source/transfer nodes inside `0.001 <= k/(h Mpc^-1) <= 0.1`.

The strict source/transfer node matching itself was at machine precision: maximum relative k mismatch `1.545552650407278e-16`.

### M1 — native-node reconstruction

Maximum relative mismatch between native `pk_lin(k,z)` and

`(2*pi^2/k^3) * P_R(k) * D_m(k,z)^2`

on common native nodes:

- `cs2=0`: `2.6385494041197272e-14`
- `cs2=1e-6`: `2.7665156205510028e-14`
- `cs2=1e-5`: `2.6229046869209216e-14`

Global maximum: `2.7665156205510028e-14`.

Thus the physical source normalization is numerically exact at native nodes to floating-point precision on the frozen domain.

### M2 — interpolation attribution

Reproducing the Exp070A signed-linear-in-log-k interpolation gives the old target-grid mismatch again:

- global target-grid maximum: `0.04753586663767729`
- global native-grid maximum: `2.7665156205510028e-14`

The target/native error ratio is O(`1.7e12` to `1.8e12`) by case, far beyond the preregistered 10x requirement. Therefore the primary classification is unambiguously `INTERPOLATION_DOMINATED`.

### M3 — multiplicative normalization diagnostic

Although the formal common-normalization signature criterion also evaluates true, this is because the native-node ratio is unity to machine precision:

- median `R_raw = P_native/P_recon = 1.0000000000000004` for all three cases;
- `R_raw` coefficient of variation is `6.3e-15` to `8.1e-15`;
- relative spread of model medians is exactly `0.0` at reported precision.

Under the frozen classification precedence M2 dominates. There is no evidence for a nontrivial physical multiplicative normalization offset.

### M4 — source identity

The standard transfer API exposes `d_b`, `d_cdm`, `d_fld`, `d_g`, `d_gdm`, `d_tot`, `d_ur`, `phi`, `psi`, but no public column declared to be the same gauge-invariant `index_tp_delta_m` source. Frozen result: `NOT_PUBLICLY_EXPOSED`.

### M5 — deliberately wrong `d_tot` comparator

Maximum native-node reconstruction errors from `d_tot` are approximately `0.00311123` for all three cases. `d_tot` remains forbidden as a replacement physical source.

### M6 — read-only controls

- accessor repeatability: bitwise PASS in all cases;
- native mPk before/after accessor reads: maximum relative change `0.0`;
- execution integrity: PASS.

## Scientific consequence

The C3 failure mechanism is now localized: the source itself and its primordial normalization are correct; the failed Exp070A bridge was damaged by DSIR-side interpolation of signed `D_m` amplitudes onto the five target k values.

A future corrective C3 bridge may therefore use native-node power reconstruction and only an independently preregistered projection/interpolation operator that is validated at the power/observable level. It may not retroactively convert Exp070A to PASS.

No common support-validity mask is authorized yet because C5 remains unresolved after Exp069B. G7/G8/G9 remain OPEN.
