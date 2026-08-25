#!/usr/bin/env python3
from pathlib import Path

MARK='<!-- EXP049A_F22_SYNC_2026-08-26 -->'

blocks={
'docs/SCIENTIFIC_FINDINGS_REGISTER.md': r'''

<!-- EXP049A_F22_SYNC_2026-08-26 -->
## F22 — source-native transition scales track interaction-localization migration

**Status: source-scale extraction HARD ESTABLISHED for frozen C3/C5; cross-family window-crossing interpretation SUPPORTED / PARTIAL.**

Exp049A derives characteristic scales from pinned solver equations rather than fitting them to localization. For frozen GDM,
\[k_s=\mathcal H/\sqrt{c_s^2},\qquad k_{v,QS}=\sqrt{9/8}\,\mathcal H/\sqrt{c_v^2},\]
where the viscosity expression is explicitly a quasi-steady proxy, not an exact eigenmode scale. For pinned designer f(R), EFTCAMB's exact B definition and diagnostic `B(a),f_R,R/H0^2,E,E',E''` give the inverse Compton scale through
\[\frac{1+f_R}{3f_{RR}H_0^2}=\frac{(R/H_0^2)'}{3B(H'/H)}.\]

Hard provenance: run `32904376001`, artifact `9584346604`, SHA256 `6a2c7f4e072fe7ee5d3a125bd798e975ab7031f5e7e92f3c71b47dbe71856f22`; max terminal B0 relative error `8.75255e-9` versus frozen `1e-6` control.

Observed ordering: GDM pressure stays outside the low-k window and `k_I^geo` stays near `0.051`; dynamic shear enters around `cv2~1e-5` and localization migrates downward. Designer f(R) similarly has `k_C` outside the window for `B0=1e-6,1e-5`, entering on the frozen z range by `1e-4`, with `k_I^geo` moving from `0.0510862` to `0.0399397` by `B0=1e-3`.

The GDM ordering now has an independent withheld confirmation (Exp049B/F21). The f(R) ordering remains retrospective until Exp049C. No universal law, G7 closure, field count, or detectability claim follows. Standalone record: `docs/SCIENTIFIC_FINDING_F22_PHYSICAL_TRANSITION_SCALE_BRIDGE.md`.
''',
'docs/RECOVERY_LATEST.md': r'''

<!-- EXP049A_F22_SYNC_2026-08-26 -->
## 2026-08-26 — Exp049A physical transition-scale bridge / F22

Clean lineage branch: `research/physical-transition-scale-bridge-v0-2`, rebuilt from current `main` after PR #30/F21 merge. The old PR #29 is scientifically superseded only because it carried stacked Exp047/048 ancestry; its successful Exp049A artifact is retained unchanged.

Hard run: `32904376001`, artifact `9584346604`, SHA256 `6a2c7f4e072fe7ee5d3a125bd798e975ab7031f5e7e92f3c71b47dbe71856f22`.

Key equations:
- GDM pressure: `k_s = Hconf/sqrt(cs2)`.
- GDM dynamic-shear quasi-steady proxy: `k_v_QS = sqrt(9/8) Hconf/sqrt(cv2)`.
- designer f(R): `B=f_R'/(1+f_R)*H/H'`; with diagnostic background quantities, `(1+f_R)/(3 f_RR H0^2)=Rbar'/(3 B H'/H)`.

Key exact/derived values:
- GDM `cv2=1e-5`: `k_v_QS(z_I)=0.103107 h/Mpc`, `k_I^geo=0.0504785`.
- GDM `cv2=1e-4`: `k_v_QS(z_I)=0.0331561`, `k_I^geo=0.0406271`.
- f(R) `B0=1e-5`: min frozen-z `k_C=0.222210`, outside low-k window; `k_I^geo=0.0508385`.
- f(R) `B0=1e-4`: min frozen-z `k_C=0.0702692`, inside window; `k_I^geo=0.0488757`.
- f(R) `B0=1e-3`: `k_C(z_I)=0.0550213`, `k_I^geo=0.0399397`.

Interpretation status: exact source-scale extraction HARD; cross-family window-crossing principle SUPPORTED/PARTIAL. GDM has withheld support via F21; f(R) still needs Exp049C. G7/G8 remain OPEN.
''',
'docs/RECOVERY_MANUAL.md': r'''

<!-- EXP049A_F22_SYNC_2026-08-26 -->
## Recovery addendum — physical transition-scale bridge (Exp049A/F22)

When reconstructing the research, do not infer a characteristic scale from fitted localization. Re-derive it from the pinned source equations.

### C3 GDM
For frozen `w_gdm=0`, pressure enters the Euler equation through a `c_s^2 k^2` gradient, giving the labelled Hubble-gradient crossing
\[k_s=\mathcal H/\sqrt{c_s^2}.\]
Pinned dynamic shear satisfies a damping/source equation of the form
\[\sigma'=-3\mathcal H\sigma + (8/3)c_v^2(\theta+\text{metric shear}),\]
while Euler contains `-k^2 sigma`. Neglecting `sigma'` and metric shear only for the diagnostic quasi-steady estimate gives `sigma~(8/9)c_v^2 theta/Hconf`, hence
\[k_{v,QS}=\sqrt{9/8}\,\mathcal H/\sqrt{c_v^2}.\]
Never relabel this as an exact Jeans/eigenmode scale.

### C5 designer f(R)
Pinned EFTCAMB defines
\[B=\frac{f_R'}{1+f_R}\frac{H}{H'}=\frac{f_{RR}R'}{1+f_R}\frac{H}{H'},\]
prime `d/d ln a`. Exp049A adds diagnostic-only output of `x,a,B,R/H0^2,f_R,E,E',E''` without changing the solved equations. With `Rbar=R/H0^2`,
\[\frac{1+f_R}{3f_{RR}H_0^2}=\frac{Rbar'}{3B(H'/H)},\quad Rbar'=3(4E'+E''),\quad H'/H=E'/(2E).\]
The comoving inverse-Compton wavenumber is `a*(100/c)*sqrt((1+f_R)/(3 f_RR H0^2))` in `h/Mpc`; scalaron mass additionally subtracts `Rbar/3` inside the mass-squared expression.

Recovery provenance: run `32904376001`, artifact `9584346604`, artifact digest `6a2c7f4e072fe7ee5d3a125bd798e975ab7031f5e7e92f3c71b47dbe71856f22`; pinned GDM_CLASS `4c87916a...`, pinned H-EFTCAMB `16d9c4e9...`.

Scientific discipline: the Exp049A f(R) alignment is retrospective. Only GDM has a withheld validation so far (Exp049B/F21). Exp049C must be frozen before new intermediate B0 outputs. Do not advance G7 or G8 from F22 alone.
''',
'docs/STATUS.md': r'''

<!-- EXP049A_F22_SYNC_2026-08-26 -->
## Exp049A / F22 status — 2026-08-26

🟢 Source-native physical-scale extraction PASS: run `32904376001`, artifact `9584346604`.

🟢 Exact designer-f(R) diagnostic controls pass; max terminal `B0` relative error `8.75255e-9 < 1e-6`.

🟢 GDM Exp049B/F21 supplies independent withheld confirmation that `k_I^geo` migrates downward after the dynamic-shear proxy enters the low-k window.

🟡 Designer-f(R) shows the same window-entry/localization ordering retrospectively; Exp049C is the required withheld test.

🔴 No G7 residual law, no G8 discovery, no universal-model construction, no intrinsic-rank/no-hair claim.
''',
'docs/GATES.md': r'''

<!-- EXP049A_F22_SYNC_2026-08-26 -->
## Exp049A/F22 gate note — physical transition-scale hypothesis

- **Source/algebra gate:** 🟢 PASS for frozen C3/C5 implementations (Exp049A run `32904376001`).
- **GDM independent prediction gate:** 🟢 PASS via Exp049B/F21.
- **designer-f(R) independent prediction gate:** 🟡 OPEN; Exp049C required.
- **Cross-family universalization:** 🔴 NOT ELIGIBLE. One withheld family is insufficient; C4 and observation-space/domain robustness remain missing.
- **G7:** OPEN.
- **G8:** OPEN.
'''
}

for name, block in blocks.items():
    p=Path(name)
    s=p.read_text()
    if MARK in s:
        print('already synced', name)
        continue
    p.write_text(s.rstrip()+block+'\n')
    print('updated', name)
