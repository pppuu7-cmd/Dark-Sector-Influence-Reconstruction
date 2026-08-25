#!/usr/bin/env python3
from pathlib import Path

MARK='<!-- DSIR_EXP049B_DOC_SYNC_2026_08_26 -->'

sections={
'docs/SCIENTIFIC_FINDINGS_REGISTER.md': r'''

<!-- DSIR_EXP049B_DOC_SYNC_2026_08_26 -->
## F18 — finite-amplitude interaction hierarchy persists while response manifolds curve

**Status: HARD ESTABLISHED descriptive finite-manifold result on sampled C1/C2/C3/C5 low-k rays (Exp047A); broader classification only SUPPORTED.**

Across every retained finite amplitude in Exp047A the sampled interaction-power classes remain non-overlapping in the order

\[
\boxed{\mathrm{IDE}<\mathrm{smooth\mbox{-}w}<\mathrm{GDM}<f(R)}.
\]

At the same time GDM-viscosity and designer-\(f(R)\) response/interaction directions rotate with amplitude. Therefore `chi_I` is **not** a constant model label and tangent dimension must remain distinct from finite-manifold linear span and curvature.

Standalone record: `docs/SCIENTIFIC_FINDING_F18_FINITE_INTERACTION_MANIFOLD.md`.

---

## F19 — interaction-energy localization has complementary scale and time geometry

**Status: HARD ESTABLISHED descriptive operator result for frozen C1/C3/C5 low-k directions (Exp048A).**

For

\[
q_k(k)=\frac{\sum_z I^2}{\|I\|^2},\qquad q_z(z)=\frac{\sum_k I^2}{\|I\|^2},
\]

GDM and designer-\(f(R)\) are almost identical in scale localization (`q_k` angle `0.040-0.051 deg`) but separated in time localization (`20.15-21.52 deg`). Smooth-w and \(f(R)\) show the complementary pattern: `q_z` angle `1.93 deg`, `q_k` angle `79.37 deg`.

GDM cs2/cv2 remain almost degenerate in localization (`q_k=0.0113 deg`, `q_z=1.382 deg`), so metric slip remains the validated microphysical separator.

Standalone record: `docs/SCIENTIFIC_FINDING_F19_INTERACTION_LOCALIZATION_GEOMETRY.md`.

---

## F20 — finite-amplitude GDM viscosity and designer-f(R) localization migrates toward lower k, but temporal flow is not universal

**Status: HARD ESTABLISHED descriptive finite-manifold result (Exp048B); physical window-crossing explanation was initially SUPPORTED only.**

GDM viscosity moves from `k_I_geo≈0.05099` to `0.04063 h/Mpc` as `cv2` grows `1e-8 -> 1e-4`; designer-f(R) moves `0.05109 -> 0.03994 h/Mpc` over `B0=1e-6 -> 1e-3`. Their time centroids differ qualitatively: GDM is nearly monotone upward, whereas f(R) is non-monotone.

Thus a common scale-migration pattern does not imply a universal time trajectory. Exp049B below supplies the first withheld test of the GDM scale-migration interpretation.

Standalone record: `docs/SCIENTIFIC_FINDING_F20_FINITE_LOCALIZATION_FLOW.md`.

---

## F21 — GDM interaction localization follows the pre-frozen window-crossing direction on withheld intermediate amplitudes

**Status: HARD ESTABLISHED for the Exp049B C3 withheld interpolation test; broader physical-window principle SUPPORTED/PARTIAL.**

Before generating any intermediate outputs, Exp049B froze the dynamic-shear quasi-steady proxy

\[
\boxed{k_{v,\mathrm{QS}}=\sqrt{9/8}\,\mathcal H/\sqrt{c_v^2}}
\]

and a single directional prediction on the new grid `cv2={1.5e-5,2e-5,3e-5,5e-5,7e-5}`: once this proxy has entered `k<=0.1 h/Mpc`, the interaction-energy centroid must be non-increasing with increasing `cv2`, allowing only `1e-6 h/Mpc` positive numerical drift.

Run `32904158849` passed. Artifact `9584180621`, SHA256 `892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a`.

Source-derived proxy at fixed `z=1.317`:

`0.084846, 0.073479, 0.059995, 0.046472, 0.039276 h/Mpc`.

Withheld measured localization:

`0.050174, 0.049835, 0.049046, 0.047046, 0.044604 h/Mpc`.

All four measured steps are negative:

`-3.397e-4, -7.890e-4, -2.000e-3, -2.441e-3 h/Mpc`.

Operator controls are clean: reconstruction `0`, core/interaction orthogonality `2.43e-19`, zero-mean residual `7.07e-21`, profile-normalization residual `2.17e-19` against the frozen `1e-12` ceiling.

**Hard interpretation:** the previously observed GDM viscosity scale-localization migration survives a genuinely withheld intermediate-amplitude test in the direction predicted by source-derived window penetration.

**Boundary:** this does not prove `k_v_QS` is the exact viscosity eigenmode scale, does not yet validate the same principle for designer-f(R), does not establish a universal dark-sector law, and does not close G7 or G8.

Standalone record: `docs/SCIENTIFIC_FINDING_F21_GDM_WINDOW_CROSSING_VALIDATION.md`.

---

## Research discipline after F21

1. Treat F21 as independent support for a C3 window-crossing mechanism, not a universal law.
2. Keep `k_v_QS` explicitly labelled quasi-steady until an eigenmode/closure derivation is validated.
3. Use Exp049A exact designer-B diagnostics as the next cross-mechanism test; a mismatch must be retained as a negative result.
4. Do not infer a common temporal trajectory from the scale result.
5. G7 and G8 remain open; universal-model construction remains premature.
''',
'docs/RECOVERY_LATEST.md': r'''

<!-- DSIR_EXP049B_DOC_SYNC_2026_08_26 -->
## 2026-08-26 live overlay — Exp049B withheld GDM window-crossing validation

**New hard result:** `PASS_GDM_WINDOW_CROSSING_VALIDATION_V0_1`.

Provenance:
- workflow run `32904158849`;
- artifact `9584180621`;
- artifact SHA256 `892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a`;
- branch/PR: `research/gdm-window-crossing-validation-v0-1`, PR #30;
- pinned upstream `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`;
- same frozen p8 precision and C3 cosmology as the validated viscosity manifold.

The prediction was frozen **before** any of the five intermediate P(k,z) outputs existed. At fixed frozen `z=1.317`, the source-audited dynamic-shear equations give the quasi-steady proxy

\[
k_{v,QS}=\sqrt{9/8}\,\mathcal H/\sqrt{c_v^2}.
\]

The crossing `k_v_QS=0.1 h/Mpc` occurs near `cv2=1.08e-5`; therefore the withheld grid `1.5e-5,2e-5,3e-5,5e-5,7e-5` was chosen after the predicted entrance into the window.

Pre-frozen scientific gate: `k_I_geo` must be non-increasing with `cv2`, positive-step tolerance `1e-6 h/Mpc`; no prediction for `z_I`, `chi_I`, or shift magnitude.

Results:

| cv2 | k_v_QS(z=1.317) | k_I_geo | chi_I | z_I |
|---:|---:|---:|---:|---:|
| 1.5e-5 | 0.084846 | 0.050174 | 0.037610 | 1.26128 |
| 2e-5 | 0.073479 | 0.049835 | 0.035438 | 1.27208 |
| 3e-5 | 0.059995 | 0.049046 | 0.031145 | 1.29507 |
| 5e-5 | 0.046472 | 0.047046 | 0.023581 | 1.33958 |
| 7e-5 | 0.039276 | 0.044604 | 0.018037 | 1.37157 |

Every `k_I_geo` step is negative, so the withheld prediction passes. This is the first independent validation of the GDM scale-window interpretation. It is not yet a designer-f(R) or universal result.

Current active next test: Exp049A PR #29, exact pinned EFTCAMB `B(a)` / Compton-scale bridge. Do not use its result until the corrected CAMB double-underscore diagnostic naming run completes.
''',
'docs/RECOVERY_MANUAL.md': r'''

<!-- DSIR_EXP049B_DOC_SYNC_2026_08_26 -->
## Recovery addition — Exp049B physical-window validation (2026-08-26)

### Why this experiment exists

Exp048B showed, retrospectively, that GDM viscosity localization moves toward lower k at large amplitude. Exp049A source audit identified a physical diagnostic scale from the exact pinned dynamic-shear equations. Exp049B converts that retrospective pattern into a withheld prediction.

For frozen `w=ca2=0`, flat C3 with `dynamic_shear_gdm=yes`:

\[
\theta'\supset-\mathcal H\theta-k^2\sigma,
\qquad
\sigma'=-3\mathcal H\sigma+\frac{8}{3}c_v^2(\theta+\mathrm{metric\ shear}).
\]

Under a **diagnostic quasi-steady approximation only** (`sigma'≈0`, metric-shear omitted only in this estimate),

\[
\sigma\simeq\frac{8}{9}\frac{c_v^2}{\mathcal H}\theta,
\]

and equality of viscous and Hubble damping gives

\[
\boxed{k_{v,QS}=\sqrt{9/8}\,\mathcal H/\sqrt{c_v^2}}.
\]

Use the same-run CLASS background to obtain `Hconf=aH`; never reconstruct it from a hand-closed Friedmann approximation.

### Frozen independent test

Reference redshift: `z=1.317`; window edge `kmax=0.1 h/Mpc`; crossing amplitude about `1.08e-5`.

Withheld grid: `cv2={1.5e-5,2e-5,3e-5,5e-5,7e-5}`.

Frozen prediction before solver output:

`k_I_geo(cv2[i+1]) <= k_I_geo(cv2[i]) + 1e-6 h/Mpc`.

No time-centroid or magnitude prediction was frozen.

### Result and provenance

Run `32904158849`; artifact `9584180621`; SHA256 `892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a`.

Measured `k_I_geo`:

`0.0501743 -> 0.0498346 -> 0.0490456 -> 0.0470456 -> 0.0446043 h/Mpc`.

All steps negative; operator controls pass by many orders of magnitude. Status: **HARD ESTABLISHED for this withheld C3 interpolation test**.

### Recovery boundary

Do not upgrade this to a universal scale law. `k_v_QS` is not yet an exact eigenmode scale. The required next cross-mechanism check is Exp049A using exact pinned designer-f(R) `B(a)` diagnostics. G7 and G8 remain open.
''',
'docs/STATUS.md': r'''

<!-- DSIR_EXP049B_DOC_SYNC_2026_08_26 -->
## 2026-08-26 update — Exp049B

✅ **PR #27 Exp047A merged** into `main` as merge `a29e44ceca75da5dd9efc997ddfa3dfc9b3d707c`.

✅ **PR #28 Exp048A/B merged** into `main` as merge `282d0d8000ee551ae8f365c55f063e910edab91a`.

✅ **Exp049B withheld GDM window-crossing test PASS**: run `32904158849`, artifact `9584180621`, SHA256 `892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a`. New intermediate `cv2` points obey the pre-frozen non-increasing `k_I_geo` prediction.

🟡 **Exp049A designer-f(R) exact physical-scale bridge remains active** on PR #29. A CAMB output-root double-underscore naming issue was identified before scientific reading and corrected; only the corrected head/run may be interpreted.

❌ **G7 remains OPEN**: no universal residual law has been established.

❌ **G8 remains OPEN**: no withheld-family/model prediction sufficient for discovery/universal-model construction has been completed. Exp049B is withheld within one validated control family, not a withheld dark-sector family.
''',
'docs/GATES.md': r'''

<!-- DSIR_EXP049B_DOC_SYNC_2026_08_26 -->
## Gate update — 2026-08-26 Exp049B

### Physical-window mechanism bridge

**State: SUPPORTED/PARTIAL; not a new top-level PASS gate.**

Exp049B is a genuine pre-frozen interpolation prediction inside C3. After the source-derived dynamic-viscosity proxy enters `k<=0.1 h/Mpc`, all five newly computed intermediate amplitudes satisfy the frozen directional prediction that `k_I_geo` is non-increasing with `cv2`.

This upgrades the C3 **window-crossing mechanism explanation** from retrospective support to independent within-family support.

It does **not** close G7 because:
- the proxy is quasi-steady rather than a validated exact eigenmode scale;
- only C3 has the withheld validation so far;
- designer-f(R) exact `B(a)` bridge is still being tested;
- no common functional law across families has been frozen and validated.

It does **not** close G8 because the withheld points belong to a known C3 ray, not a withheld model family/mechanism.

Therefore top-level state remains: **G7 OPEN, G8 OPEN**.
'''
}

for fn,block in sections.items():
    p=Path(fn)
    s=p.read_text()
    if MARK not in s:
        p.write_text(s.rstrip()+block+'\n')
        print('updated',fn)
    else:
        print('already synced',fn)
