#!/usr/bin/env python3
from pathlib import Path

MARK='<!-- DSIR_EXP050B_DOC_SYNC_2026_08_26 -->'

def append_once(path,text):
    p=Path(path)
    s=p.read_text() if p.exists() else ''
    if MARK in s:
        return False
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(s.rstrip()+('\n\n' if s.strip() else '')+MARK+'\n'+text.strip()+'\n')
    return True

append_once('docs/SCIENTIFIC_FINDINGS_REGISTER.md', r'''
## F25 — thermal-WDM free-streaming cutoff scale passes withheld mass ordering

**Status: HARD ESTABLISHED for the frozen Exp050B interpolation test; broader scaling law SUPPORTED only.**

Because F24 showed that the C4 high-k response is nearly time-separable, Exp050B tested a mechanism-native cutoff coordinate rather than the GDM/f(R) interaction centroid:

\[
r_{\rm WDM}(k_{0.1},z)=\ln[P_{\rm WDM}/P_{\rm CDM}]=-0.1.
\]

Before generating the new CLASS outputs, the masses `2.5,3.5,4.0,4.5 keV` and the gate

\[
k_{0.1}(m_{i+1},z)-k_{0.1}(m_i,z)>10^{-4}\ h/{\rm Mpc}
\]

were frozen for every consecutive mass step at all seven DSIR redshifts.

Clean confirmation run `32911928403` passed. Artifact `9586893981`, SHA256 `7c01e71c4223115976dc6887a1bcac06cac99e7fc50d039fae47307dd105ff0e`. At `z=0.295`, `k_0.1={8.386656,12.192829,14.230131,16.473743} h/Mpc`; the minimum mass step over all redshifts is `2.037283 h/Mpc`, far above the frozen sign guard. An earlier independent run `32911710049` also passed.

The redshift drift of each crossing is only `1.57e-4..3.97e-4 h/Mpc` over `z=0.295..2.33`, descriptively reinforcing the scale-dominated/time-stationary F24 picture.

A post-result combined fit of old+new masses gives roughly `k_0.1 proportional to m^1.1434` with <0.8% relative residual, but this exponent was not preregistered and is **not** a hard law.

Standalone record: `docs/SCIENTIFIC_FINDING_F25_WDM_FREE_STREAMING_CUTOFF_WITHHELD.md`.

**Boundary:** withheld interpolation inside C4, not a withheld-family G8 test; no Ly-alpha/nonlinear claim; no G7 closure; no universal parameter-count claim.

---

## Research discipline after F25

1. Use mechanism-native characteristic coordinates: interaction localization for current nonseparable GDM/f(R), cutoff scale for nearly separable WDM.
2. Do not promote the descriptive WDM mass exponent without a new preregistered mass/threshold test.
3. Use the Exp051A block-aware evidence mask for cross-family coverage; never zero-pad C4 into low-k matrices.
4. Next dimensionality work should produce masked bounds/coverage, not a raw zero-imputed SVD rank.
5. G7 and G8 remain open.
''')

append_once('docs/STATUS.md', r'''
## 2026-08-26 update — Exp050B / F25

✅ **Exp050B withheld C4 cutoff-scale prediction PASS.** Frozen masses `{2.5,3.5,4.0,4.5} keV`; on all seven DSIR redshifts every consecutive mass step moves the solver-defined `r_WDM=-0.1` crossing to higher k. Clean run `32911928403`, artifact `9586893981`, SHA256 `7c01e71c4223115976dc6887a1bcac06cac99e7fc50d039fae47307dd105ff0e`; science merged via PR #35 at `7630cf23554bdd9e0bc7c738bb3b0b33d1b67388`.

✅ **F25 HARD for the frozen within-C4 interpolation.** At z=0.295, `k_0.1={8.38666,12.19283,14.23013,16.47374} h/Mpc`. Minimum positive mass-step over all z is `2.03728 h/Mpc`; total redshift drift per mass is only `1.57e-4..3.97e-4 h/Mpc`.

✅ **Exp051A block-aware observability atlas v0.2 merged.** Missing, near-null and solver-limited cells are machine-explicit; C4 high-k stays masked from the low-k matrix.

🟡 **Descriptive only:** old+new WDM points are well summarized by `k_0.1 ~ m^1.1434` at z=0.295, but this exponent was fitted after seeing the new outputs and is not a hard law.

❌ **G7 remains OPEN.** We now have mechanism-specific characteristic-scale motion in C3/C5 and C4, but not one preregistered model-independent functional law across them.

❌ **G8 remains OPEN.** F25 is withheld interpolation within C4, not a withheld family/mechanism.

### Immediate continuation

1. Use the Exp051A evidence mask to compute hard pairwise coverage deficits and a masked separator graph v0.2.
2. Test whether WDM cutoff curves collapse under `k/k_0.1` using a new independent mass/threshold set before calling the C4 manifold self-similar.
3. Seek a genuinely withheld mechanism/family for G8 rather than accumulating only within-family interpolation wins.
4. Continue observational window/covariance projection.
''')

append_once('docs/GATES.md', r'''
## Gate update — 2026-08-26 Exp050B / F25

### C4 withheld interpolation

**State: HARD PASS within the frozen thermal-WDM family.**

Exp050B froze new masses `2.5,3.5,4.0,4.5 keV` and the directional cutoff-scale criterion before generating their CLASS outputs. The solver-defined first `ln(P_WDM/P_CDM)=-0.1` crossing increases with mass at all seven frozen redshifts; clean run `32911928403` passed.

This strengthens the C4 mechanism atlas and shows that the free-streaming response has a stable scale coordinate. It does **not** close G8 because the held-out points are interpolation inside an already represented family.

### G7 boundary after F21/F23/F25

There are now preregistered directional successes in three response directions/mechanisms:

- C3 GDM viscosity: interaction-localization scale moves with the source-derived viscous transition;
- C5 designer-f(R): interaction-localization scale moves with the exact inverse-Compton transition;
- C4 thermal WDM: solver cutoff `k_0.1` moves monotonically with relic mass.

However the observable coordinates and microscopic control variables are not yet unified by one frozen model-independent equation. Therefore **G7 remains OPEN**. A common qualitative phrase such as “characteristic scales move through the response window” is not yet a residual law.

### Exp051A mask

The block-aware observability atlas v0.2 is now the required input for future rank/coverage claims. Unknown, solver-limited and near-null cells cannot be filled with zeros. Any future `N_repr` or `N_disc` gate must state which fully observed submatrix or masked bound it uses.

Top-level state: **G7 OPEN, G8 OPEN, G9 OPEN**.
''')

append_once('docs/RECOVERY_LATEST.md', r'''
# Live recovery overlay — Exp050B / F25

Latest hard scientific result: Exp050B/F25 withheld thermal-WDM cutoff-scale ordering PASS.

Definition:

`r_WDM(k,z)=ln[P_WDM(k,z)/P_CDM(k,z)]`, with `k_0.1` the first downward crossing `r_WDM=-0.1`.

Frozen before outputs: masses `2.5,3.5,4.0,4.5 keV`; every consecutive `k_0.1` mass step had to exceed `1e-4 h/Mpc` at each of the seven DSIR redshifts.

Hard run `32911928403`; artifact `9586893981`; SHA256 `7c01e71c4223115976dc6887a1bcac06cac99e7fc50d039fae47307dd105ff0e`; merged science SHA `7630cf23554bdd9e0bc7c738bb3b0b33d1b67388`.

At z=0.295: `k_0.1=8.386656,12.192829,14.230131,16.473743 h/Mpc`. Minimum step over all redshifts `2.037283 h/Mpc`. Redshift drift per mass only `1.57e-4..3.97e-4 h/Mpc`.

F24+F25 current C4 picture: strong high-k suppression, almost no irreducible k-z interaction, stable cutoff-scale motion with mass. Do not replace this by `k_I^geo`; WDM uses its own mechanism-native coordinate.

Exp051A block-aware evidence mask is merged and should be used for cross-family bookkeeping. No zero imputation.

G7/G8 remain open. Next: masked pairwise coverage and a truly independent test of WDM scale-collapse or a withheld family/mechanism.
''')

append_once('docs/RECOVERY_MANUAL.md', r'''
## Recovery update — Exp050B / F25 (2026-08-26)

### Why WDM uses a different scale coordinate

Exp050A/F24 found `chi_I ~ 2e-10` on the solver-native high-k C4 atlas. Therefore an interaction-energy centroid is numerically inappropriate as the primary mechanism coordinate. Exp050B instead defines

`k_0.1(z): r_WDM(k_0.1,z)=-0.1`,

where `r_WDM=ln(P_WDM/P_CDM)` and the first downward crossing is interpolated in log k between native CLASS samples.

### Frozen withheld contract

Masses `m={2.5,3.5,4.0,4.5} keV`. Same pinned CLASS and matched density/N_eff setup as Exp050A. At every standard DSIR redshift require

`k_0.1(m[i+1],z)-k_0.1(m[i],z) > 1e-4 h/Mpc`.

No exact values or scaling exponent were frozen.

### Result

Clean run `32911928403` PASS; artifact `9586893981`; SHA256 `7c01e71c4223115976dc6887a1bcac06cac99e7fc50d039fae47307dd105ff0e`.

At z=0.295 the crossings are `8.386656,12.192829,14.230131,16.473743 h/Mpc`. All 21 consecutive mass-step checks across the seven redshifts are positive (three steps per redshift); minimum step `2.037283 h/Mpc`.

A post-result combined fit with Exp050A masses 2,3,5 keV gives `k_0.1 ~ m^1.1434` with max relative residual ~0.77%, but this is descriptive only and must be independently preregistered before hardening.

### Current mechanism geometry

- C3 GDM viscosity: moderate low-k k-z interaction; characteristic motion tracked by interaction localization/source viscous scale.
- C5 designer f(R): strong low-k k-z interaction; characteristic motion tracked by interaction localization/exact Compton scale.
- C4 thermal WDM: strong high-k but nearly time-separable response; characteristic motion tracked by a transfer cutoff scale.

This supports characteristic-scale thinking but does not yet provide a common universal residual equation.

### Recovery discipline

Use `data/derived/comparison_readiness/block_aware_observability_atlas_v0_2.json` for masks. Missing/unknown/solver-limited cells are not zeros. G7/G8 remain open.
''')

append_once('docs/BUYANOVGPT_TABLE.md', r'''
## 13. Exp050B/F25 update — C4 free-streaming scale flow

C4 now has a validated mechanism-native finite-amplitude coordinate:

`k_0.1(z)` defined by `ln(P_WDM/P_CDM)=-0.1`.

Withheld masses `2.5,3.5,4.0,4.5 keV` passed the preregistered prediction that `k_0.1` increases with mass at every one of the seven DSIR redshifts.

At z=0.295:

| m [keV] | k_0.1 [h/Mpc] |
|---:|---:|
| 2.5 | 8.38666 |
| 3.5 | 12.19283 |
| 4.0 | 14.23013 |
| 4.5 | 16.47374 |

This sharpens the C4 atlas label from merely `M/high-k active` to:

**strong scale-dominated free-streaming response + nearly time-separable shape + monotonic cutoff-scale manifold.**

Descriptive, not hard: all old+new masses at z=0.295 fit roughly `k_0.1 ~ m^1.1434` to <0.8% relative residual. A new preregistered test is required before treating that exponent as stable.

### Cross-family lesson

The current useful common abstraction is not “one universal k_I”. It is **characteristic response-scale motion with mechanism-dependent coordinates**:

- GDM viscosity / f(R): nonseparable interaction localization;
- WDM: nearly separable transfer cutoff.

Whether these can be mapped to a common residual-law coordinate is an open G7 problem.
''')

append_once('docs/RESEARCH_LOG_2026-08-26_EXP050B.md', r'''
# Research log — 2026-08-26 — Exp050B

Exp050B preregistered thermal-WDM masses 2.5, 3.5, 4.0, 4.5 keV and a mechanism-native cutoff scale `r_WDM(k_0.1,z)=-0.1`. Frozen gate: every consecutive mass step in `k_0.1` must exceed `1e-4 h/Mpc` at all seven DSIR redshifts.

Run `32911710049` passed. After clean incorporation of Exp050A/main lineage, run `32911928403` independently passed the same contract. Official artifact: `9586893981`, SHA256 `7c01e71c4223115976dc6887a1bcac06cac99e7fc50d039fae47307dd105ff0e`.

At z=0.295 crossings are 8.386656, 12.192829, 14.230131, 16.473743 h/Mpc. Minimum measured mass step over all z is 2.037283 h/Mpc. Redshift drift is only ~1e-4 h/Mpc.

F25 hardens mass-ordering of the C4 cutoff coordinate, not a universal scaling exponent. G7/G8 remain open.
''')
