# DSIR-I final scientific-remainder audit

**Date:** 2026-08-28  
**Scope:** scientific calculations/evidence required for the first article only.  
**Verdict:** `NO_UNRESOLVED_SCIENTIFIC_CALCULATION_REQUIRED_FOR_DSIR_I_DECLARED_SCOPE_V0_2`.

## 1. Audit question

After the historical 72/28 review, ask a deliberately strict question:

> Is there any unresolved scientific calculation which must be completed before the first DSIR article can honestly support its frozen thesis?

The answer after the 2026-08-28 completion pass is **no**.

This statement is narrower than saying the whole DSIR programme is complete and narrower than saying the manuscript is already ready to submit.

## 2. Final remainder matrix

| Candidate remainder | Result after final pass | Classification |
|---|---|---|
| Unified block-aware response map | multi-family response atlas, masks/nulls and channel-conditioned formalism already frozen | ✅ **CLOSED FOR PAPER I** |
| Amplitude / zero / transition geometry | finite-amplitude curvature, interaction localization, WDM cutoff, DCDM epoch/zero structure and moving-scale bridge already frozen | ✅ **CLOSED FOR PAPER I** |
| Cross-model translator | 2026-08-28 metric/scaling/coordinate-ablation robustness audit added; full-coordinate cycle closure exactly `2/5` for all `9/9` tested variants; scale removal collapses cross-family discrimination | ✅ **CLOSED FOR PAPER I AS RETROSPECTIVE LOCAL/CHANNEL-CONDITIONAL CONSTRUCTION** |
| Withheld/prospective validation | WDM withheld interpolation PASS; genuinely withheld DCDM PASS; C8 hard prospective FAIL robust to all seven leave-one-z deletions; genuinely withheld C9 multicoordinate prospective PASS with all seven leave-one-z rebuilds passing | ✅ **CLOSED FOR PAPER I** |
| Known-sector specificity guard | baryon control already shows matter-space simplicity is not dark-specific | ✅ **CLOSED / NEGATIVE SPECIFICITY CONTROL** |
| Prior-art / novelty boundary | earlier dark-degeneracy, EFT/PPF/GDM/PCA/fingerprinting precedents explicitly acknowledged; DSIR novelty kept combinatorial/operational | ✅ **CLOSED SCIENTIFICALLY**, final citation metadata remains editorial |
| Physical eligibility before covariance | fail-closed support/perturbativity/normalizability/exact-realization chain already demonstrates the methodological ordering | ✅ **CLOSED AS PAPER-I METHODOLOGICAL RESULT** |
| Referee attack: arbitrary `chi_I` / grid | finite-amplitude envelopes + 12/12 deterministic leave-one-node tier preservation, with smooth-w sensitivity explicitly retained | ✅ **ADDRESSED** |
| Referee attack: translator metric arbitrariness | new 9-variant metric/scaling robustness + coordinate ablations | ✅ **ADDRESSED** |
| Referee attack: withheld tests not independent | evidence classes explicitly separated; genuine withheld/prospective positive and negative tests exist | ✅ **ADDRESSED** |
| Observational G7 relation/null | frozen roadmap assigns full observation-space quotient/G7 to DSIR-3 | ➡️ **OPEN, OUTSIDE PAPER I** |
| Fresh post-G7 G8 | frozen roadmap assigns genuinely withheld post-G7 falsification to DSIR-4 | ➡️ **OPEN, OUTSIDE PAPER I** |
| G9 / new-physics interpretation | requires later gates | ➡️ **OPEN, OUTSIDE PAPER I** |

## 3. Translator robustness result

The new audit uses only immutable frozen C3 GDM-viscosity and C5 designer-f(R) summaries and the coordinate

`q = [ln(k_geo), z_centroid, ln(chi_I)]`.

It tests three common coordinate scalings

- pooled z-score;
- pooled min-max;
- pooled median/MAD;

against three norms

- `L1`;
- `L2`;
- `Linf`.

### Full coordinate

All **9/9** variants return exactly **2/5** C3 cycle closures under `C3 -> C5 -> C3`.

Eight of nine variants map the first four sampled C3 amplitudes to the lowest sampled C5 `B0=1e-6`, while the largest C3 amplitude maps to `B0=1e-3`. The large-amplitude endpoint `cv2=1e-4 -> B0=1e-3` is stable in **9/9** variants.

### Coordinate ablation

- `(ln k_geo, z_centroid)`: `2/5` closure and the same C3->C5 mapping in **9/9** variants;
- `(z_centroid, ln chi_I)`: only `1/5` closure; all five C3 points map to `B0=1e-3` in **9/9** variants;
- `(ln k_geo, ln chi_I)`: `2/5` closure in `7/9`, `3/5` in `2/9`.

This closes the Paper-I translator question at the correct strength: **translation is local, multicoordinate, response-subspace/channel conditional and non-bijective on the sampled finite rays**. It does not establish a universal microscopic parameter identity.

A reproducible audit implementation is now stored as

`papers/dsir1/audit_cross_model_translator_robustness.py`

with machine-readable result summary

`papers/dsir1/evidence/cross_model_translator_robustness_audit_v0_1.json`.

## 4. Withheld/prospective validation is sufficient for Paper I

The first article does not require a post-G7 observational discovery test. Its scientific requirement is that candidate response-language generalizations are exposed to non-training mechanisms without retroactive repair and that both positive and negative outcomes are preserved.

The current record satisfies that requirement in multiple ways:

1. WDM withheld-mass interpolation succeeds within-family;
2. genuinely withheld DCDM->dark-radiation passes a pre-frozen characteristic-epoch direction;
3. the C8 IDM-photon test hard-fails the prior retrospective half-transition relation despite all frozen rows having unique crossings, and the sign failure survives every one-redshift deletion;
4. genuinely withheld C9 IDM-baryon passes the preregistered multicoordinate path test, with every leave-one-redshift operator rebuild agreeing.

This mixed PASS/FAIL record is positive evidence for the methodology's falsifiability and failure resistance; it is not evidence for a universal dark-sector law.

## 5. Adversarial-referee remainder

The existing referee audit's scientific attacks are already defended by frozen evidence or accepted limitations. The remaining active items are editorial scope risks:

- response geometry versus survey-reproducibility balance;
- excessive claim count / manuscript compression.

These require editing, not new science.

The 5% support threshold remains correctly described as a frozen analysis contract rather than a law of nature. A prospective threshold-sensitivity study could be useful in a later completed observation route, but no current Paper-I claim depends on producing one.

## 6. Exp073 / DSIR4 intake rule

Ongoing Exp073 observational-route work must remain fail-closed and scientifically active on `main`, but Paper I does not wait for it.

A future Exp073 result may enter Paper I only if it materially changes an explicit limitation already stated in the manuscript. No PRE-RESULT/queued/infrastructure outcome can change Paper-I claims.

## 7. Historical 72/28 reconciliation

The earlier ~72% estimate named six Paper-I science blocks. After this completion pass:

- H1 unified response map — CLOSED;
- H2 amplitude/zero/transition atlas — CLOSED;
- H3 cross-model translator — CLOSED FOR PAPER-I STRENGTH;
- H4 withheld-family validation — CLOSED FOR PAPER-I STRENGTH;
- H5 scientific narrative — CLOSED;
- H6 figures/tables as scientific evidence carriers — CLOSED.

Because exact historical weights were never archived, the transparent equal-block audit is now **6/6 = 100%** for the named first-article science blocks.

The previously reported ~92% v0.1 audit was intentionally conservative because it still charged prospective observational translator/G7->G8 ambitions against Paper I. The frozen series roadmap shows that those stronger ambitions belong to later articles.

## 8. What still remains before submission

Only publication/reproducibility work can remain for DSIR-I itself, including final prose/layout compression, bibliography metadata verification, final fresh literature check, exact release-candidate numerical/notation/claim audit, clean JCAP build, offline archive, visual/hash audit and RC/tag freeze.

These tasks can discover an error that reopens science. Until such an error is found, however, they do not justify inventing another scientific calculation merely to increase a completion percentage.

## 9. Gate statement

- **Paper-I declared scientific core:** ✅ CLOSED.
- **Historical six Paper-I science blocks:** ✅ 6/6 CLOSED FOR ARTICLE SCOPE.
- **Unresolved mandatory Paper-I scientific calculations:** ✅ NONE IDENTIFIED.
- **G7:** 🔴 OPEN, later paper.
- **G8:** 🔴 OPEN, later paper.
- **G9:** 🔴 OPEN, later paper.

Final status:

`NO_UNRESOLVED_SCIENTIFIC_CALCULATION_REQUIRED_FOR_DSIR_I_DECLARED_SCOPE_V0_2`
