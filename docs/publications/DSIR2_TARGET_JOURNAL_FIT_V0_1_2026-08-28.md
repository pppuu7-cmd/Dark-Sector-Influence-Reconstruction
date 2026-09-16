# DSIR-2 target-journal fit memo — v0.1

**Date:** 2026-08-28  
**Purpose:** choose the submission target without prematurely rewriting the deterministic journal-neutral baseline.

## Recommendation

### 1. JCAP — strongest topical fit

**Journal of Cosmology and Astroparticle Physics (JCAP)** is the current first-choice target for DSIR-2.

Why:

- scope explicitly covers cosmology and particle astrophysics, including dark matter, large-scale structure, theoretical, observational, computational and simulation work;
- DSIR-2 is fundamentally a cosmological-response / dark-sector-identifiability methods paper rather than a survey-data release;
- GDM, dark matter, perturbation response, cosmological degeneracy and solver-based methodology are all native to the readership;
- the present title/abstract already reads naturally as a JCAP cosmology-methods article.

Submission framing for JCAP should emphasize:

1. the cosmological inverse-identifiability problem;
2. known-sector falsification of apparent dark-sector specificity;
3. the representation-resolvability and ray/line/subspace hierarchy;
4. reproducible CLASS/GDM response construction;
5. strict separation between provider-space results and downstream observational claims.

Do not frame DSIR-2 as a discovery paper. Its strongest contribution is methodological and falsification-first.

Official source checked 2026-08-28: IOP Publishing Support, JCAP author-guideline/scope page.

## 2. Physical Review D — strong alternative

PRD is the strongest alternative if the manuscript is positioned more as a general physics/cosmology methodology paper.

Current PRD scope explicitly includes gravity, cosmology, astrophysics, cosmological constraints on fundamental/particle physics, cosmology/galaxy formation, and computational/data-science techniques in cosmology. Regular Research Articles have no fixed length limit.

Advantages for DSIR-2:

- strong fit to model discrimination, gravitation/cosmology and fundamental-physics interpretation;
- the ray/line/subspace and representation-kernel logic can be foregrounded as a general inference problem;
- regular-article format can accommodate the complete negative-control/provenance story.

Potential disadvantage relative to JCAP:

- the manuscript would benefit from slightly stronger emphasis on the general physics significance beyond the specific cosmology solver chain;
- a PRD version should make the connection to broader parameter-identifiability/model-manifold literature especially crisp.

Official sources checked 2026-08-28: APS PRD About/Scope and Information for Authors pages.

## 3. MNRAS — viable but currently third choice

MNRAS publishes original theoretical and observational astronomy/astrophysics research, has no page limit for normal Papers, and supports LaTeX submissions.

It is viable if DSIR-2 is reframed toward practical cosmological inference and implications for interpreting large-scale-structure observables.

Why it ranks below JCAP/PRD for the present draft:

- Article 2 deliberately stops before covariance-whitened survey inference, so its center of gravity is presently more fundamental/methodological than observational;
- MNRAS asks authors to keep Papers concise and its house style uses a two-column layout, requiring a more substantial presentation conversion;
- MNRAS is currently fully Open Access and its author instructions list an APC for Papers, which may be a practical consideration depending on funding/waiver arrangements.

Official source checked 2026-08-28: Oxford Academic MNRAS Instructions to Authors.

## Current ranking

| Rank | Journal | Fit | Best framing |
|---|---|---|---|
| 1 | JCAP | **Excellent** | dark-sector/cosmology identifiability and falsification workflow |
| 2 | Physical Review D | **Very strong** | general cosmological/fundamental-physics response identifiability |
| 3 | MNRAS | **Good** | cosmological inference / LSS interpretation |

## Recommended next manuscript action

Preserve `dsir2_journal_neutral_v0_3.tex` and the deterministic release artifact unchanged.

If JCAP is accepted as the target, create a **new** target-specific source rather than modifying the neutral baseline, for example:

`docs/publications/latex/article2/jcap/dsir2_jcap_v0_1.tex`

Then perform a target-specific pass covering:

- JCAP template/class and bibliography conventions;
- author/affiliation metadata;
- abstract/keywords requirements;
- figure/table placement under JCAP layout;
- data/code availability statement;
- acknowledgements and author-contribution/disclosure text as required;
- final submission-date novelty/citation graph audit;
- deterministic compile and render-first QA of the JCAP package.

## Decision boundary

No journal selection changes the Article-2 scientific closure. Target-journal conversion is publication engineering only. Do not strengthen the claims to make the paper sound more dramatic for a particular venue.