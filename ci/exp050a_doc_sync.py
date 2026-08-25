#!/usr/bin/env python3
from pathlib import Path

MARK='<!-- DSIR_EXP050A_DOC_SYNC_2026_08_26 -->'

def append_once(path, text):
    p=Path(path)
    s=p.read_text()
    if MARK in s:
        return False
    p.write_text(s.rstrip()+"\n\n"+MARK+"\n"+text.strip()+"\n")
    return True

append_once('docs/SCIENTIFIC_FINDINGS_REGISTER.md', r'''
## F22 — source-native transition scales track interaction-localization migration

**Status: source-scale extraction HARD ESTABLISHED for frozen C3/C5; cross-family interpretation SUPPORTED/PARTIAL.**

Exp049A derives characteristic scales directly from pinned solver equations. For GDM, `k_s=Hconf/sqrt(cs2)` and the labelled quasi-steady dynamic-shear proxy is `k_v,QS=sqrt(9/8) Hconf/sqrt(cv2)`. For designer-f(R), the pinned EFTCAMB definition of `B(a)` yields an exact inverse-Compton scale through `f_RR` reconstructed from `B, R, H` derivatives.

GDM pressure scales remain outside the low-k window and `k_I^geo` stays near `0.051 h/Mpc`; GDM viscosity and designer-f(R) both begin migrating to lower `k_I^geo` after their source-derived transition scales enter the frozen window. Run `32904376001`, artifact `9584346604`, SHA256 `6a2c7f4e072fe7ee5d3a125bd798e975ab7031f5e7e92f3c71b47dbe71856f22`.

Standalone record: `docs/SCIENTIFIC_FINDING_F22_PHYSICAL_TRANSITION_SCALE_BRIDGE.md`.

---

## F23 — designer-f(R) passes the pre-frozen window-crossing localization prediction

**Status: HARD ESTABLISHED for Exp049C withheld interpolation; broader universality SUPPORTED/PARTIAL.**

Before generating new C5 outputs, Exp049C froze `B0={1.5,2,3,5,7}e-4` and the single directional prediction `Delta k_I^geo <= 1e-6 h/Mpc` for increasing B0 once the exact source-derived inverse-Compton transition is inside the finite window.

Withheld `k_I^geo` values are `0.0480162, 0.0472514, 0.0459188, 0.0437628, 0.0420339 h/Mpc`; every step is negative. Run `32907619613`, artifact `9585579947`, SHA256 `bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942`.

Together with F21, the same directional finite-window principle now has withheld support in two physically distinct mechanisms: GDM dynamic shear and designer modified gravity. This is not yet a universal law and does not close G7 or G8.

Standalone record: `docs/SCIENTIFIC_FINDING_F23_FR_WINDOW_CROSSING_VALIDATION.md`.

---

## F24 — thermal-WDM high-k response is strongly scale-dominated and nearly time-separable

**Status: HARD ESTABLISHED descriptive response geometry for the frozen C4 thermal-WDM high-k atlas (Exp050A).**

Exp050A fills the previous C4 time-domain gap with solver-native CLASS `P(k,z)` responses for `m={2,3,5} keV`, `k={0.1,0.3,1,3,10,20} h/Mpc`, and the standard seven DSIR redshifts.

At `z=0.295`, `r_WDM(k=20)` is `-1.19344, -0.445167, -0.119171` for `2,3,5 keV`. Yet the maximum redshift drift is only `6.83e-5, 2.26e-5, 5.07e-6`, and the irreducible scale-time interaction fractions are `2.58e-10, 2.21e-10, 2.29e-10`.

Thus a response can be very large while remaining almost exactly separable into scale-dominated plus tiny time dependence. C4 is qualitatively distinct from current low-k C3/C5 examples, especially designer-f(R), where `k x z` interaction is material.

Run `32908751625`, artifact `9585845292`, SHA256 `5d02bdce07da95c2bb9eab01acb2641f110b6b16e4ecf29ac2e8b1619d053139`.

Standalone record: `docs/SCIENTIFIC_FINDING_F24_WDM_HIGHK_TIME_SEPARABILITY.md`.

---

## Research discipline after F24

1. C4 now has a genuine high-k time-dependent solver atlas; do not zero-pad it onto the low-k matrix.
2. Treat WDM `chi_I~1e-10` as a frozen-domain result, not a theorem of universal time separability.
3. The two-family F21/F23 window-crossing prediction is stronger than retrospective support but is still not a universal law.
4. Recompute the discriminant graph / masked comparison geometry with the new C4 time block before any dimensionality claim.
5. Continue observational kernel/covariance projection and withheld-mechanism testing.
6. G7 and G8 remain open; universal-model construction remains premature.
''')

append_once('docs/STATUS.md', r'''
## 2026-08-26 update — Exp049A/049C/050A

✅ **Exp049A/F22 merged via clean PR #31**: source-native GDM and designer-f(R) characteristic-scale bridge is hard at the solver-definition level.

✅ **Exp049C/F23 withheld designer-f(R) prediction PASS**: run `32907619613`, artifact `9585579947`, SHA256 `bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942`. Together with GDM F21, the same directional window-crossing prediction has passed in two distinct tested mechanisms.

✅ **Exp050A/F24 thermal-WDM high-k time atlas PASS**: run `32908751625`, artifact `9585845292`, SHA256 `5d02bdce07da95c2bb9eab01acb2641f110b6b16e4ecf29ac2e8b1619d053139`. C4 now has a solver-native time-dependent high-k response block. `chi_I` is about `2.2e-10..2.6e-10` despite large high-k suppression, so WDM is strongly scale-dominated / nearly time-separable on this frozen linear domain.

✅ **Scientific findings live through F24**: standalone F22-F24 plus synchronized main register.

🟡 **G3B is strengthened, not redefined**: C4 is no longer time-domain missing, but remains a separate high-k block and is never zero-imputed into low-k comparisons.

❌ **G7 remains OPEN**: two-family directional window-crossing support is not yet a model-independent residual law.

❌ **G8 remains OPEN**: the successful withheld points are within already represented mechanisms/families; no withheld-family discovery gate has passed.

### Immediate continuation

1. Fold the new C4 high-k `(k,z)` block into the masked BuyanovGPT observability atlas and recompute pairwise discriminant coverage without forcing a common k-domain.
2. Test WDM mass-flow stability / free-streaming-scale localization with pre-frozen intermediate masses or an independent high-k operator.
3. Revisit masked representation/discrimination dimension only after the C4 block is included; do not call raw SVD mode count intrinsic rank.
4. Continue observational window/covariance projection and exact-null/channel-reversal searches.
5. Keep universal-model construction blocked until readiness criteria are genuinely satisfied.
''')

append_once('docs/GATES.md', r'''
## Gate update — 2026-08-26 Exp049C / Exp050A

### Two-mechanism withheld window-crossing support

**State: HARD for the two frozen withheld tests; broader G7 interpretation remains SUPPORTED/PARTIAL.**

Exp049B/F21 (GDM dynamic shear) and Exp049C/F23 (designer-f(R)) independently froze the same directional statement before their new intermediate outputs: after the relevant source-derived transition lies inside the finite response window, moving that transition toward smaller k with increasing microscopic parameter is accompanied by non-increasing `k_I^geo`. Both tests passed with every measured step negative.

This is stronger than retrospective correlation, but G7 remains OPEN because no model-independent functional relation has been frozen across a sufficiently broad set of mechanisms/operators and quotient identities.

G8 remains OPEN because these are withheld interpolation points within mechanisms already represented in the atlas, not a truly withheld model family/mechanism used for discovery validation.

### C4 time-domain completion

Exp050A hard run `32908751625` fills the previous C4 high-k time-dependent response gap with pinned CLASS for thermal WDM masses 2, 3 and 5 keV on six high-k nodes and seven redshifts. Operator/provenance controls pass.

This strengthens **G3B block-aware comparison readiness**: C4 is no longer represented only by a static transfer proxy. However, C4 remains a distinct high-k block; it is not valid to zero-pad it into the low-k C1/C2/C3/C5 matrix.

The new C4 response is nearly time-separable (`chi_I ~ 2e-10`) on the frozen linear domain, which is a scientific feature, not a new gate closure.

Top-level state remains: **G7 OPEN, G8 OPEN, G9 OPEN**.
''')

append_once('docs/RECOVERY_LATEST.md', r'''
# Live recovery overlay — Exp050A / F24

Current main scientific frontier after F21-F24:

- F21: withheld GDM dynamic-shear window-crossing direction PASS.
- F22: source-native GDM and designer-f(R) characteristic-scale bridge HARD at solver-definition level.
- F23: withheld designer-f(R) window-crossing direction PASS; same directional principle now succeeds in two distinct tested mechanisms.
- F24: C4 thermal-WDM high-k time-dependent CLASS atlas PASS. WDM high-k suppression is large but scale-time interaction is tiny (`chi_I ~ 2.2e-10..2.6e-10`).

Exp050A frozen grid: masses `2,3,5 keV`; `k=0.1,0.3,1,3,10,20 h/Mpc`; standard seven DSIR redshifts. Run `32908751625`; artifact `9585845292`; SHA256 `5d02bdce07da95c2bb9eab01acb2641f110b6b16e4ecf29ac2e8b1619d053139`.

Important boundary: C4 now has time dependence measured, but remains a separate high-k block. Missing/common-domain cells stay masked, never zero. No universal WDM separability theorem, no Ly-alpha likelihood, no G7/G8 closure.

Next reconstruction step: recompute the block-aware influence/discriminant atlas including C4 time geometry, then design a withheld high-k/free-streaming validation rather than forcing C4 onto low-k nodes.
''')

append_once('docs/RECOVERY_MANUAL.md', r'''
## Recovery update — Exp049A through Exp050A (2026-08-26)

### Window-crossing result chain

Exp048B first observed that finite-amplitude GDM-viscosity and designer-f(R) interaction localization moves toward smaller `k_I^geo`. Exp049A then derived characteristic scales from pinned source equations rather than fitting the response:

- GDM pressure: `k_s=Hconf/sqrt(cs2)`;
- GDM dynamic-shear labelled quasi-steady proxy: `k_v,QS=sqrt(9/8) Hconf/sqrt(cv2)`;
- designer-f(R): exact inverse-Compton scale from the pinned EFTCAMB `B(a)` definition through `f_RR`.

Exp049B froze new GDM amplitudes before output and predicted non-increasing `k_I^geo`; run `32904158849` passed. Exp049C then froze new designer-f(R) `B0={1.5,2,3,5,7}e-4` before output and the same directional prediction; run `32907619613` passed. Therefore two physically distinct represented mechanisms now have genuine withheld interpolation support for the finite-window directional principle. This is still not G7 or G8.

### C4 high-k time completion — Exp050A

Use pinned official CLASS solver output, not the old static Viel fit, for production `P_WDM(k,z)/P_CDM(k,z)` comparisons.

Frozen domain:

- masses `m={2,3,5} keV`;
- `k={0.1,0.3,1,3,10,20} h/Mpc`;
- `z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`.

Response:

`r_WDM(k,z)=ln[P_WDM(k,z)/P_CDM(k,z)]`.

Hard run `32908751625`, artifact `9585845292`, SHA256 `5d02bdce07da95c2bb9eab01acb2641f110b6b16e4ecf29ac2e8b1619d053139`.

At `z=0.295`, `r(k=20)` is `-1.1934447, -0.4451668, -0.1191708` for `2,3,5 keV`. Maximum redshift drift is only `6.83e-5, 2.26e-5, 5.07e-6`.

Applying `R=mu+T(k)+tau(z)+I(k,z)` gives `chi_I={2.5826e-10,2.2081e-10,2.2916e-10}`. Hence current linear high-k thermal-WDM is strongly scale-dominated and nearly time-separable. Do not generalize this beyond the frozen domain.

Legacy Viel comparison is descriptive only; the solver atlas is the DSIR production time-dependent C4 block.

### Recovery discipline

- Never zero-pad C4 into low-k matrices.
- Keep C4 high-k and C1/C2/C3/C5 low-k as masked blocks until an operator genuinely maps them to common observation coordinates.
- Keep `N_micro`, `N_manifold`, `N_repr`, `N_disc` distinct.
- G7/G8 remain open; universal-model construction stays blocked.
''')

append_once('docs/BUYANOVGPT_TABLE.md', r'''
## 12. Exp050A update — C4 high-k time geometry

The previous C4 entry `I unknown until high-k time atlas exists` is superseded by Exp050A.

| C4 quantity | Hard result on frozen high-k linear atlas |
|---|---|
| masses | `2,3,5 keV` |
| k-domain | `0.1,0.3,1,3,10,20 h/Mpc` |
| z-domain | standard seven DSIR nodes |
| high-k suppression | strong; e.g. at z=0.295, k=20: `r=-1.193,-0.445,-0.119` |
| redshift drift | tiny: max `6.83e-5,2.26e-5,5.07e-6` |
| irreducible interaction `chi_I` | `2.58e-10,2.21e-10,2.29e-10` |
| atlas interpretation | **domain-localized free-streaming / scale-dominated; nearly time-separable on this frozen linear domain** |

This gives the current response-class contrast:

`IDE`: near-separable low-k exchange response;
`smooth-w`: weak low-k interaction;
`GDM`: moderate low-k interaction, viscosity curvature/window flow;
`WDM`: strong high-k scale signature with almost no `k x z` interaction;
`designer-f(R)`: strong low-k scale-time interaction and curved window flow.

Do not compare these `chi_I` numbers as if they came from one common k-domain; the atlas remains block-aware/masked.

### Updated continuation

1. Recompute block-aware discriminant coverage including the C4 time block.
2. Design a withheld/intermediate WDM free-streaming test before proposing any generalized transition-window law involving C4.
3. Preserve metric slip for GDM pressure/viscosity and high-k transfer for WDM as distinct channel requirements.
4. Continue observation-space mapping before any `N_repr`/`N_disc` hard claim.
''')

append_once('docs/RESEARCH_LOG_2026-08-26_EXP050A.md', r'''
# Research log — 2026-08-26 — Exp050A

Exp050A first hard run `32908751625` passed. Artifact `9585845292`, SHA256 `5d02bdce07da95c2bb9eab01acb2641f110b6b16e4ecf29ac2e8b1619d053139`.

C4 thermal-WDM is now represented by a solver-native high-k `(k,z)` atlas rather than only the legacy static transfer fit. The strongest new descriptive result is that large free-streaming suppression is nearly time-separable over the frozen linear domain: `chi_I~2e-10` for all three masses.

This closes the *time-domain missing-data issue* for the current C4 block, but not any universal-law or observation-space gate. Next step is a block-aware atlas/discriminant recomputation and an independent withheld WDM free-streaming validation.
''')
