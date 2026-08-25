#!/usr/bin/env python3
from pathlib import Path

blocks = {
'docs/SCIENTIFIC_FINDINGS_REGISTER.md': r'''

<!-- F23_FR_WINDOW_CROSSING_SYNC_2026-08-26 -->
## F23 — withheld designer-f(R) validation extends the finite-window prediction to a second mechanism

**Status: HARD ESTABLISHED for the frozen Exp049C test; two-family predictive support HARD for the tested GDM/f(R) rays; broader universality SUPPORTED / PARTIAL only.**

Exp049C froze five previously uncomputed designer-f(R) amplitudes before solver output,

\[
B_0=\{1.5,2,3,5,7\}\times10^{-4},
\]

and predicted only

\[
k_I^{geo}(B_{0,i+1})-k_I^{geo}(B_{0,i})\le10^{-6}\;h/{\rm Mpc}.
\]

Run `32907619613`, artifact `9585579947`, SHA256 `bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942` passed source eligibility, operator controls and the scientific prediction.

Withheld `k_I^geo` values are

`0.0480162, 0.0472514, 0.0459188, 0.0437628, 0.0420339 h/Mpc`,

with consecutive steps

`-7.6481e-4, -1.33256e-3, -2.15603e-3, -1.72888e-3 h/Mpc`.

Minimum exact frozen-z inverse-Compton scales decrease simultaneously from `0.0573747` to `0.0265600 h/Mpc`. Maximum terminal B0 relative error is `7.50777e-11`; all operator residuals are below `5.7e-20` versus the frozen `1e-12` algebraic ceiling.

Combined with GDM Exp049B/F21, the same directional finite-window statement has now survived two independently frozen interpolation tests in physically distinct mechanisms. This is **not** a universal function, a dark-sector theorem, a field count, a no-hair result, G7 closure, G8 discovery, or survey detectability.

Standalone record: `docs/SCIENTIFIC_FINDING_F23_FR_WINDOW_CROSSING_VALIDATION.md`.
''',
'docs/RECOVERY_LATEST.md': r'''

<!-- F23_FR_WINDOW_CROSSING_SYNC_2026-08-26 -->
## 2026-08-26 — Exp049C / F23 withheld designer-f(R) validation

Hard result: `PASS_FR_WINDOW_CROSSING_VALIDATION_V0_1`.

Provenance: run `32907619613`, scientific head `a575a2e78b21eab36b88db8622e14509a30cae5a`, artifact `9585579947`, digest `bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942`, pinned EFTCAMB `16d9c4e9f85751e30efd0a53b177941713078904`.

Frozen before output:
- B0 grid `{1.5e-4,2e-4,3e-4,5e-4,7e-4}`;
- source eligibility: terminal B0 error `<=1e-6`, exact min frozen-z k_C `<=0.1 h/Mpc` for every model, and decreasing min k_C with B0;
- single scientific prediction: consecutive `k_I^geo` steps `<=+1e-6 h/Mpc`;
- no prediction for z_I, chi_I, exact magnitude or survey significance.

Result:
- `k_I^geo={0.0480162,0.0472514,0.0459188,0.0437628,0.0420339}` h/Mpc;
- all four steps negative;
- min frozen-z `k_C={0.0573747,0.0496881,0.0405703,0.0314259,0.0265600}` h/Mpc;
- max terminal B0 error `7.50777e-11`;
- operator controls max `5.68411e-20`.

Interpretation: two tested mechanisms (GDM dynamic shear and designer f(R)) now have genuine withheld directional support for transition-scale motion through a finite response window being accompanied by non-increasing interaction-energy scale localization. Broader universality remains unproven. G7/G8 remain OPEN.

Active next domain-completion task: Exp050A constructs the missing C4 thermal-WDM high-k time-dependent Boltzmann atlas. Never insert C4 low-k or missing high-k entries as zero.
''',
'docs/RECOVERY_MANUAL.md': r'''

<!-- F23_FR_WINDOW_CROSSING_SYNC_2026-08-26 -->
## Recovery addendum — F23 second withheld window-crossing validation

To reproduce F23, use the frozen Exp049C contract, not the production anchors used to motivate F22.

1. Pin H-EFTCAMB at `16d9c4e9f85751e30efd0a53b177941713078904`.
2. Use the established high-precision seven-redshift comoving-density response extractor `ci/eftcamb_fr_multiz.py` and low-k nodes `{0.001,0.003,0.01,0.03,0.1} h/Mpc`.
3. Generate only the pre-frozen withheld B0 grid `{1.5e-4,2e-4,3e-4,5e-4,7e-4}` plus matched GR and designer B0=0 controls.
4. Diagnostic-only source instrumentation writes `a,B,R/H0^2,f_R,E,E',E''`; equations remain unchanged.
5. Derive exact inverse-Compton scale from
\[
B=\frac{f_R'}{1+f_R}\frac{H}{H'},\qquad
\frac{1+f_R}{3f_{RR}H_0^2}=\frac{(R/H_0^2)'}{3B(H'/H)}.
\]
6. Source contract must pass before interpreting localization: terminal B0 relative error `<=1e-6`, every model has min frozen-z k_C `<=0.1`, and those minima decrease strictly with B0.
7. Decompose `R(B0)=r_Delta(B0)-r_Delta(B0=0)` into additive core plus irreducible interaction and require reconstruction/orthogonality/zero-mean/profile controls `<=1e-12`.
8. The pre-frozen prediction is only `Delta k_I^geo <= +1e-6 h/Mpc` between consecutive amplitudes. Do not back-fill predictions for chi_I or z_I.

Immutable successful artifact: run `32907619613`, artifact `9585579947`, SHA256 `bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942`.

Combined evidence discipline: F21+F23 establish the directional result only on the tested GDM/f(R) rays. Keep G7/G8 open; do not infer universal field count or no-hair theorem. C4 remains a separate high-k domain until Exp050A or successors build an overlap-connected time atlas.
''',
'docs/STATUS.md': r'''

<!-- F23_FR_WINDOW_CROSSING_SYNC_2026-08-26 -->
## F23 status — second withheld mechanism

🟢 Exp049C designer-f(R) withheld prediction PASS: run `32907619613`, artifact `9585579947`.

🟢 Exact source-scale contract PASS; max terminal B0 error `7.51e-11`, every withheld exact k_C enters `k<=0.1` on the frozen z grid, and min k_C decreases with B0.

🟢 `k_I^geo` decreases at every withheld step: `0.0480162 -> 0.0420339 h/Mpc`.

🟢 Together with GDM F21, the finite-window directional prediction is independently supported in **two physically distinct frozen mechanisms**.

🟡 Cross-family universality remains unestablished; C4 high-k time atlas, broader family/domain tests and observation-space kernels remain missing.

🔴 G7 OPEN. G8 OPEN. Universal-model construction remains deferred.
''',
'docs/GATES.md': r'''

<!-- F23_FR_WINDOW_CROSSING_SYNC_2026-08-26 -->
## F23 gate note — finite-window transition/localization hypothesis

- C3 GDM independent withheld prediction: 🟢 PASS (F21 / Exp049B).
- C5 designer-f(R) independent withheld prediction: 🟢 PASS (F23 / Exp049C).
- Two-mechanism directional replication: 🟢 HARD for the exact tested rays/domains.
- Universal cross-family law: 🟡 NOT ESTABLISHED. Two mechanisms are insufficient; C4 and observation-space/domain robustness are missing.
- Exact universal collapse function in `k_transition/k_window`: not tested.
- G7: OPEN.
- G8: OPEN.
''',
'docs/BUYANOVGPT_TABLE.md': r'''

<!-- F23_ATLAS_UPDATE_2026-08-26 -->
## Atlas update through F23 — 2026-08-26

This section supersedes older provisional localization wording where it conflicts.

| Family/direction | Geometry/AP | low-k structure | irreducible k-z interaction | physical transition-scale status | independent localization prediction |
|---|---|---|---|---|---|
| C1 smooth-w | active | active | weak but grid-sensitive | no source scale assigned in current atlas | not tested |
| C2 IDE alpha/beta | active; alpha/beta AP-near-degenerate | active and separating | near-null on current local rays | no transition-scale claim | not tested |
| C3 GDM cs2 | exact AP/background null | active; density nearly collinear with cv2 | moderate | pressure Hubble-gradient scale source-derived; remains outside current low-k window for sampled cs2 | not applicable to current sampled crossing |
| C3 GDM cv2 | exact AP/background null | active; slip separates microphysics | moderate | dynamic-shear quasi-steady `k_v,QS=sqrt(9/8) Hconf/sqrt(cv2)` | 🟢 withheld PASS F21 |
| C4 thermal WDM | background geometry not represented by static transfer control | low-k nearly blind; high-k transfer strongly active | **unknown in time-dependent high-k block** | half-mode/free-streaming block separate | **running Exp050A; missing is not zero** |
| C5 designer f(R) B0 | exact AP/background null on frozen designer branch | active and scale-dependent | strong | exact EFTCAMB B-derived inverse-Compton scale | 🟢 withheld PASS F23 |

Current mechanism-level statement: when the source-derived transition lies inside the finite low-k window, moving it to smaller k predicts non-increasing interaction-energy scale localization on the tested C3-cv2 and C5-B0 withheld rays. This is two-family replicated evidence, **not a universal dark-sector law**.

Current missing blocks that prevent family-complete rank/law claims:
1. C4 genuine high-k `(k,z)` response (Exp050A running);
2. observation/window/covariance projection for the interaction/localization descriptors;
3. additional withheld families/directions rather than interpolation only within C3/C5;
4. validated GDM velocity/RSD channel remains blocked by gauge bridge;
5. no common block may be filled by zero for a missing family.
''',
'docs/LITERATURE_MAP.md': r'''

<!-- F23_LITERATURE_UPDATE_2026-08-26 -->
## Source anchors added for Exp049A/F23 and Exp050A

### f(R) Compton-wavelength parameter

- Song, Hu & Sawicki, **The Large Scale Structure of f(R) Gravity**, arXiv:astro-ph/0610532. Establishes the stable `B>0` branch and parameterization of linear f(R) deviations by the B quantity tied to `d^2f/dR^2`.
  - https://arxiv.org/abs/astro-ph/0610532
- Hu & Sawicki, **Models of f(R) Cosmic Acceleration that Evade Solar-System Tests**, Phys. Rev. D 76, 064004 (2007), arXiv:0705.1158. Describes B as the Compton-wavelength parameter and states that its square-root is essentially the scalaron Compton wavelength in horizon units in the relevant limit.
  - https://arxiv.org/abs/0705.1158

These references independently support the physical interpretation of the exact B definition audited in pinned EFTCAMB; DSIR still derives its numerical scale from the pinned source rather than importing a fitted approximation.

### thermal/non-cold relic Boltzmann implementation

- Official CLASS pinned for Exp050A: `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`.
- The pinned `explanatory.ini` explicitly states that the ncdm sector covers massive neutrinos, warm dark matter and other non-cold relics; if both `m_ncdm` and `omega_ncdm` are supplied, CLASS renormalizes the phase-space distribution to satisfy both; `T_ncdm` is independently specified.
- Exp050A uses the pinned upstream `pk_ref.pre` as the initial high-precision ncdm calibration, where `ncdm_fluid_approximation=3` corresponds to `ncdmfa_none` in the same pinned source enum.

This is a solver/provenance anchor, not an observational WDM constraint.
''',
'docs/UNIVERSAL_MODEL_READINESS.md': r'''

<!-- F23_READINESS_UPDATE_2026-08-26 -->
## Readiness update after F21/F23

The withheld-validation criterion has improved materially: the same pre-frozen directional finite-window prediction has now passed on independent interpolation grids in C3 GDM dynamic shear and C5 designer f(R).

This **does not trigger universal-model construction**. Remaining blockers include at least:

- C4 has no validated time-dependent high-k atlas yet (Exp050A running);
- interaction/localization geometry is not yet projected through complete observation/window/covariance operators;
- no stable family-complete representational dimensionality has been established;
- GDM velocity/RSD remains gauge-validation limited;
- G7 residual-law closure and G8 withheld model-level prediction remain open.

Status: **NOT READY**. Continue the comparative atlas and independent falsification program.
'''
}

for name, block in blocks.items():
    p = Path(name)
    s = p.read_text()
    marker = block.splitlines()[2] if len(block.splitlines()) > 2 else ''
    # Each block includes a unique HTML marker; detect it directly.
    html = next((line for line in block.splitlines() if line.startswith('<!-- ')), None)
    if html and html in s:
        print('already synchronized', name)
        continue
    p.write_text(s.rstrip() + block + '\n')
    print('updated', name)
