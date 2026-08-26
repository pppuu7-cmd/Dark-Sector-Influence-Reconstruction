#!/usr/bin/env python3
from pathlib import Path

MARK='<!-- DSIR_F26_C6_SYNC_2026_08_26 -->'

def append_once(path,text):
    p=Path(path); s=p.read_text() if p.exists() else ''
    if MARK in s: return False
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(s.rstrip()+('\n\n' if s.strip() else '')+MARK+'\n'+text.strip()+'\n')
    return True

append_once('docs/SCIENTIFIC_FINDINGS_REGISTER.md', r'''
## F26 — withheld-family DCDM response localization moves to earlier epochs with decay rate

**Status: HARD ESTABLISHED for Exp053A; broader characteristic-scale/epoch principle STRONGLY SUPPORTED, not yet a frozen universal law.**

C6 is decaying cold dark matter into dark radiation in pinned official CLASS, a mechanism not used to construct F21/F23/F25. Before the first C6 outputs were inspected, Exp053A froze `Gamma/H0={0.25,0.5,1,2}` and the temporal response-power centroid

\[
1+z_R=\exp\left[\sum_z q_z\ln(1+z)\right],\qquad
q_z=\frac{\sum_k r^2(k,z)}{\sum_{z,k}r^2(k,z)}.
\]

The prediction was `Delta z_R > 1e-3` for every consecutive decay-rate step. Clean run `32915877993` passed with

`z_R={0.6304573,0.6343830,0.6419613,0.6562403}`

and steps

`{0.00392568,0.00757834,0.01427902}`.

Artifact `9588160014`, SHA256 `541e3449801f0e853fa573784fd72685ad407c1a3f041b18884e715017aa5e10`; merged PR #39 at `6c9880e3cc7f3769e08dd6baf29f56186e97ce66`.

The first run `32915553193` is infrastructure-only: all solver outputs were generated, but a background filename assertion failed and the preregistered science step was skipped. Only the filename glob was corrected; the science contract was unchanged.

Post-gate descriptive morphology: `chi_I=0.0820 -> 0.0665`, extreme full-response angle about `2.17 deg`, and a redshift-moving scale-sign pivot near `k~0.0026..0.0067 h/Mpc` that depends only weakly on Gamma/H0.

Standalone record: `docs/SCIENTIFIC_FINDING_F26_DCDM_WITHHELD_FAMILY_TEMPORAL_LOCALIZATION.md`.

**Boundary:** F26 is the first true withheld-family/mechanism validation of the broad characteristic-scale/epoch idea, but it does not retroactively close G8 because G7 still lacks one common preregistered quantitative relation shared across mechanisms.

---

## Research discipline after F26

1. Distinguish `withheld-family support for a hypothesis` from `withheld validation of one frozen universal relation`.
2. Use C6 to formulate the next G7 candidate quantitatively, then test that new formula prospectively.
3. Preserve the new C6 sign-pivot as descriptive until a separate preregistered test.
4. Extend the block-aware atlas additively; do not rewrite frozen Exp051A/052 results.
5. Continue resolving the 18/21 non-reference pairwise hard-evidence gaps identified by Exp052A.
''')

append_once('docs/STATUS.md', r'''
## 2026-08-26 update — Exp052A / Exp053A / F26

✅ **Exp052A masked discriminant coverage PASS and merged.** Run `32915627840`, artifact `9588050351`, SHA256 `433d9447ad4de06774210f1b7a2467469cf654cce54cc1c2522864e3d385d9ac`. Four hard degeneracy edges still require the unique three-type hitting set `{M_highk,S_slip,tau/full-kz}`, but only 3 of 21 non-reference atlas pairs have pair-specific hard-edge evidence; 18/21 remain unresolved.

✅ **Exp053A/F26 first true withheld-family mechanism PASS.** New C6 DCDM->dark-radiation family was not used to construct F21/F23/F25. Pre-frozen `Gamma/H0={0.25,0.5,1,2}` temporal-centroid prediction passed on clean run `32915877993` with `z_R=0.630457,0.634383,0.641961,0.656240` and all steps >`1e-3`.

✅ **C6 provenance:** official CLASS `e85808324f51fc694d12e3ed7439552a3c3f9540`; artifact `9588160014`, SHA256 `541e3449801f0e853fa573784fd72685ad407c1a3f041b18884e715017aa5e10`; merged PR #39, SHA `6c9880e3cc7f3769e08dd6baf29f56186e97ce66`.

🟡 **New descriptive C6 fingerprints:** moderate `chi_I=0.066..0.082`, near-ray curvature up to ~2.17 deg, and a redshift-moving scale-sign pivot. These were not preregistered and require dedicated follow-up.

🟡 **G7 materially closer but still OPEN.** We now have mechanism-specific characteristic-scale/epoch motion in GDM viscosity, designer-f(R), WDM and a truly withheld DCDM family, but not one common mathematical relation frozen prospectively across them.

🟡 **G8 readiness improved but G8 remains OPEN.** The missing ingredient is no longer lack of a withheld family; it is lack of a prior universal G7 relation for that withheld family to validate.

### Immediate continuation

1. Formulate a quantitative source-localization -> response-localization G7 candidate without retroactive thresholding.
2. Preregister a new DCDM interpolation test of that quantitative bridge and/or apply it prospectively to another new mechanism.
3. Resolve high-value pairwise gaps from Exp052A, prioritizing C1-C2 and C2-C5 common blocks.
4. Keep observation-space kernel/covariance projection on the critical path before detectability claims.
''')

append_once('docs/GATES.md', r'''
## Gate update — 2026-08-26 Exp052A / Exp053A

### Masked discriminant coverage

Exp052A hard run `32915627840` confirms the exact minimum hitting set for the **current four-edge hard catalogue** remains three separator types: `M_highk`, `S_slip`, and `tau_or_full_kz`. This is not a universal `N_disc`: 18 of 21 pairs among the seven non-reference Exp051A directions still lack pair-specific hard-edge evidence.

### First withheld-family mechanism test

Exp053A introduces C6 DCDM->dark radiation, which was not used to construct the characteristic-scale findings. The preregistered temporal response-localization prediction passed on clean run `32915877993`:

`z_R={0.6304573,0.6343830,0.6419613,0.6562403}` for `Gamma/H0={0.25,0.5,1,2}`, with all consecutive shifts above the frozen `1e-3` guard.

This is the first genuine withheld-family/mechanism support for the broad DSIR characteristic-scale/epoch organizing idea.

### Why G8 remains OPEN

G8 is defined as survival of a **relation** under withheld prediction. Before Exp053A, DSIR had a broad qualitative characteristic-scale/epoch hypothesis but did not have one single model-independent quantitative G7 relation whose exact mathematical form could be evaluated on DCDM without adapting the observable coordinate.

Therefore F26 cannot retroactively convert the broad hypothesis into a passed G7/G8 law. The correct state is:

- withheld-family evidence now exists;
- constructing a precise G7 candidate is now scientifically justified;
- that candidate must then face a fresh prospective test.

**G7 OPEN, G8 OPEN, G9 OPEN.**
''')

append_once('docs/RECOVERY_LATEST.md', r'''
# Live recovery overlay — Exp052A / Exp053A / F26

Current main scientific head after PR #39: `6c9880e3cc7f3769e08dd6baf29f56186e97ce66` (later docs-only commits may advance main).

Exp052A: masked hard-edge graph PASS. Four hard degeneracy edges total; unique current hitting set `{M_highk,S_slip,tau/full-kz}`; only 3/21 non-reference pairs have pair-specific hard edge evidence, so 18/21 are unresolved.

Exp053A/F26: first true withheld-family mechanism validation. C6 = DCDM -> dark radiation in pinned official CLASS. Frozen before first C6 science output: `Gamma/H0={0.25,0.5,1,2}`, standard low-k and z grids, response-power temporal centroid `z_R`, prediction each consecutive `Delta z_R>1e-3`.

Clean run `32915877993` PASS; artifact `9588160014`; SHA256 `541e3449801f0e853fa573784fd72685ad407c1a3f041b18884e715017aa5e10`.

Result: `z_R={0.6304573,0.6343830,0.6419613,0.6562403}`; steps `{0.00392568,0.00757834,0.01427902}`.

The initial failed run `32915553193` is infrastructure-only: background filename assertion failed before the science step; no preregistered result was exposed. Only filename glob was corrected.

Descriptive C6 follow-ups: `chi_I~0.066..0.082`, extreme ray angle ~2.17 deg, scale-sign pivot near `0.0026..0.0067 h/Mpc` moving mainly with redshift.

Important gate state: genuine withheld-family support now exists, but G7/G8 remain open because no one common quantitative relation was frozen before C6. Next action is to formulate that relation and test it prospectively, not retroactively.
''')

append_once('docs/RECOVERY_MANUAL.md', r'''
## Recovery update — Exp052A / Exp053A / F26 (2026-08-26)

### Exp052A masked discriminant coverage

Use `data/derived/comparison_readiness/block_aware_observability_atlas_v0_2.json` plus `discriminant_edges_v0_1.json`. Final run `32915627840` PASS, artifact `9588050351`, SHA256 `433d9447ad4de06774210f1b7a2467469cf654cce54cc1c2522864e3d385d9ac`.

The exact hitting set over all four hard edges (including external C0-vs-C4) is uniquely `{M_highk,S_slip,tau_or_full_kz}`. Among seven non-reference directions, only 3/21 pairs are represented by pair-specific hard degeneracy/separator edges; 18/21 remain unresolved. Never interpret absent edges as either separation or degeneracy.

### C6 DCDM source equations

Pinned official CLASS: `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`.

Background source:

`d rho_dcdm/d ln a = -3 rho_dcdm - (Gamma/H) rho_dcdm`

`d rho_dr/d ln a = -4 rho_dr + (Gamma/H) rho_dcdm`.

Perturbation code contains explicit DCDM decay terms and sourced DR multipoles.

Frozen C6 setup: stable reference `omega_cdm=0.1200`; DCDM `omega_ini_dcdm=0.1200`, `omega_cdm=0`; `Gamma/H0={0.25,0.5,1,2}`. Standard seven z and five low-k nodes.

Response `r=ln(P_DCDM/P_CDM)`. Temporal power weights `q_z=sum_k r^2/sum_zk r^2`. Centroid `1+z_R=exp(sum q_z ln(1+z))`. Pre-frozen criterion: every consecutive `z_R` step > `1e-3`, with `||r||_2>1e-4`.

Initial run `32915553193` generated solver outputs but failed a too-specific background filename assertion. The science step was skipped. Only the filename glob was corrected; all science definitions stayed frozen.

Clean run `32915877993` PASS. `z_R={0.6304573,0.6343830,0.6419613,0.6562403}` and steps `{0.00392568,0.00757834,0.01427902}`. Artifact `9588160014`, SHA256 `541e3449801f0e853fa573784fd72685ad407c1a3f041b18884e715017aa5e10`.

### C6 post-gate descriptors

`chi_I={0.08202,0.07969,0.07513,0.06646}`; extreme full-response angle ~`2.165 deg`. Every sampled model has a low-k sign pivot: positive response at `k=0.001`, negative at sufficiently larger k. The first zero crossing shifts from roughly `0.0026 h/Mpc` at z=.295 to `0.0067 h/Mpc` at z=2.33, with weak Gamma dependence. This pivot is descriptive only.

### Gate discipline after F26

F26 is true withheld-family support for the broad characteristic-scale/epoch hypothesis, but G8 still requires a common quantitative G7 relation frozen *before* a fresh prospective validation. Do not close G7/G8 retroactively.
''')

append_once('docs/BUYANOVGPT_TABLE.md', r'''
## 14. C6 DCDM withheld-family extension — F26

C6 introduces a mechanism qualitatively different from C1-C5: cold dark matter decays into dark radiation with lifetime control `Gamma/H0`.

| C6 channel | Current status |
|---|---|
| background | active; dedicated AP angle not yet hard-audited |
| low-k structure | active |
| temporal localization | **active + preregistered withheld-family PASS** |
| `I(k,z)` | active, `chi_I~0.066..0.082` descriptive range |
| metric slip | unknown |
| high-k transfer | unknown |
| density-velocity compression | unknown |

Pre-frozen temporal centroid moves `0.63046 -> 0.65624` as `Gamma/H0` grows `0.25 -> 2`, passing every `Delta z_R>1e-3` step.

New descriptive C6 fingerprint: redshift-moving scale-sign pivot around `k~0.0026..0.0067 h/Mpc`, approximately insensitive to decay-rate amplitude along the sampled ray.

### Updated cross-mechanism picture

The current common abstraction is increasingly **motion/localization of response features**, not a universal fixed coordinate:

- GDM viscosity: spatial transition + interaction localization;
- designer f(R): Compton transition + interaction localization;
- WDM: free-streaming cutoff with nearly time-separable response;
- DCDM: lifetime/epoch control + temporal response localization, plus a descriptive scale-sign pivot.

This is now supported by a truly withheld family, but remains an organizing principle rather than a frozen G7 law.
''')

append_once('docs/UNIVERSAL_MODEL_READINESS.md', r'''
## 2026-08-26 readiness update after F26

A major prerequisite has improved: DSIR now has a **genuine withheld-family/mechanism validation** (C6 DCDM, Exp053A) for the broad characteristic-scale/epoch organizing idea.

This does **not** satisfy the universal-model readiness criterion for withheld validation of a universal relation, because the relation was not yet formulated as one common quantitative equation before C6. The result changes readiness from `no withheld family evidence` to `withheld-family hypothesis support exists; common-law validation still missing`.

Universal-model construction therefore remains blocked. Required next steps include:

- formulate a common quantitative relation without fitting C6 post hoc;
- validate it prospectively on fresh points/mechanisms;
- continue masked pairwise atlas coverage and observation-space validation;
- keep solver/gauge/domain robustness explicit.
''')

append_once('docs/RESEARCH_LOG_2026-08-26_EXP053A.md', r'''
# Research log — 2026-08-26 — Exp053A

C6 DCDM->dark-radiation chosen as a genuinely withheld family because it was absent from construction of F21/F23/F25 and has a lifetime/epoch scale rather than a primary spatial cutoff.

Before outputs: froze `Gamma/H0={0.25,0.5,1,2}`, five standard low-k nodes, seven redshifts, temporal response-power centroid `z_R`, and prediction each consecutive `Delta z_R>1e-3`.

Run `32915553193`: CLASS build/config/runs/P(k,z) all succeeded; background filename assertion failed before science step. Scientific gate skipped. Infrastructure failure only.

Corrected only background filename glob. No science settings changed.

Run `32915842684`: first science execution PASS.
Run `32915877993`: clean-current-main confirmation PASS.

Final clean result: `z_R=0.6304573,0.6343830,0.6419613,0.6562403`; steps `0.00392568,0.00757834,0.01427902`. Artifact `9588160014`, SHA256 `541e3449801f0e853fa573784fd72685ad407c1a3f041b18884e715017aa5e10`.

F26 records first true withheld-family support for the broad characteristic-scale/epoch DSIR hypothesis. G7/G8 intentionally remain open pending a common frozen quantitative relation.
''')
