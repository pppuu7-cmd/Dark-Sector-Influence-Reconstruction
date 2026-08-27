# DSIR-I paper recovery checkpoint — 2026-08-27

## Purpose

This file is the minimum chat-independent recovery record for the first DSIR paper. If the conversation is lost, resume from the repository branch and files listed below.

## Repository state

Repository: `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`

Paper branch: `paper/dsir-i-observable-response-geometry`

Draft PR: `#99` — `Paper: DSIR-I observable-response geometry`

Working title:

**Dark-Sector Influence Reconstruction I: Observable-response geometry, channel-conditional equivalence, and failure-resistant model comparison**

## Author metadata

- Name: **Aleksey Buyanov**
- Affiliation: **Independent Researcher**
- Location: **Moscow, Russia**
- Email: `pppuu7@gmail.com`
- ORCID: `0009-0001-2621-9305`

Publication rule: list the author as an independent researcher; do not display an institutional affiliation unless the author explicitly changes this instruction.

## Authoritative paper files

- `papers/dsir1/manuscript.md` — base manuscript draft v0.1.
- `papers/dsir1/build_manuscript_v0_2.py` — deterministic v0.2 assembler; injects current author metadata and new sections without overwriting v0.1.
- `papers/dsir1/AUTHOR_METADATA.yml` — canonical author metadata for publication preparation.
- `papers/dsir1/CLAIMS_LEDGER.md` — hard boundary between supported claims and prohibited overclaims.
- `papers/dsir1/PROVENANCE_MATRIX.md` — manuscript claim -> experiment -> run -> artifact -> digest -> frozen criterion traceability.
- `papers/dsir1/FIGURE_MANIFEST.md` — publication figure sources and caption boundaries.
- `papers/dsir1/references.bib` — initial bibliography.
- `papers/dsir1/README.md` — figure/table roadmap and reproducibility tasks.
- `papers/dsir1/LITERATURE_POSITIONING.md` — prior-art comparison and journal/publication assessment.
- `papers/dsir1/sections/prospective_falsification.md` — prospective universalization failure text for v0.2.
- `papers/dsir1/sections/data_code_reproducibility.md` — reproducibility section for v0.2.

## Central mathematical statement

For channel set `B`, physical projection `K_B`, covariance whitener `W_B` and nuisance quotient projector `Q_B`, define

`A_B = Q_B W_B K_B`.

The exact channel-conditional equivalence relation is

`r1 ~_B r2 <=> A_B (r1-r2)=0`.

This is an identifiability theorem/definition, not a new fundamental law.

## Central empirical statements currently allowed

1. On the frozen tested response domains, the additive low-k summary
   
   `R(z,k)=mu+T(k)+tau(z)+I(z,k)`
   
   requires a non-negligible irreducible `k x z` component for GDM and especially designer-f(R).

2. The finite-amplitude descriptive hierarchy
   
   `IDE < smooth-DE < GDM < designer-f(R)`
   
   in `chi_I = ||I||^2/||R||^2` has non-overlapping sampled envelopes and survives all 12 single-node deletion tests.

3. GDM pressure and viscosity are near-degenerate in low-k matter response (`~0.3226 deg`) but strongly separated by metric slip (`~137.94 deg`; equalized Weyl+slip `~56.96 deg`).

4. GDM and designer-f(R) are nearly aligned in a leading scale mode (`~0.08-0.10 deg`) but differ substantially in time/full response.

5. Roughly 61% of normalized GDM-f(R) response-shape separation power on the frozen low-k grid is localized in the irreducible interaction component.

6. One-parameter families can curve in response space; sampled full-response turning reaches `~7.18 deg` for GDM viscosity and `~12.14 deg` for designer-f(R). Therefore `N_micro`, `N_manifold`, `N_repr`, and `N_disc` must remain distinct.

7. WDM supplies a strong high-k but nearly time-separable response, while a genuinely withheld DCDM-to-dark-radiation family supplies a distinct temporal-localization pattern.

8. Scientific FAILs remain provenance. Later corrective providers do not overwrite the original failed contracts.

9. Exp054C/F27 prospectively falsified a simple common C3/C5/C7 full-response-centroid law; the failure remains part of the article evidence rather than being retrospectively repaired.

## Prohibited claims

- Do not claim discovery of new fundamental physics.
- Do not claim a universal dark-sector invariant or universal residual law.
- Do not claim a no-hair theorem.
- Do not claim `(G,T,tau,I)` are four fundamental dark-sector parameters.
- Do not infer a universal intrinsic rank from the raw finite catalogue SVD.
- Do not call theory-space angular separation survey-level detectability.
- Do not mark G7, G8 or G9 closed unless separately and prospectively established later.

Current gate boundary: `G7=OPEN`, `G8=OPEN`, `G9=OPEN`.

## Key source documents

- `docs/BUYANOVGPT_TABLE.md`
- `docs/GATES.md`
- `docs/DSIR_METHOD.md`
- `docs/CHANNEL_CONDITIONAL_EQUIVALENCE_QUOTIENT_THEOREMS_2026-08-27.md`
- `docs/SCIENTIFIC_FINDING_F27_COMMON_RESPONSE_CENTROID_WITHHELD_FAILURE.md`
- `recovery/exp070c_provider_checkpoint_2026-08-27.md`
- `recovery/exp069h_c5_provider_certification_checkpoint_2026-08-27.md`
- `recovery/exp071a_g7_common_physical_support_mask_preregistration_2026-08-27.md`

## Literature positioning checkpoint

Targeted search as of 2026-08-27 found no direct prior paper containing the full DSIR-I construction. However, the manuscript overlaps materially with and must cite/contrast:

- Kunz 2007 dark degeneracy;
- modern DESI DR2 dark-degeneracy work (Petri, Marra, von Marttens 2026);
- model-independent IDE reconstruction;
- PPF/EFT/GDM common phenomenological frameworks;
- model-agnostic MG PCA work, including Zanoletti & Leonard 2025;
- observable-space/model-breaking approaches (Amara & Refregier 2014);
- 2026 LambdaCDM fixed-point / dark-sector deformation theory-space work.

The defensible novelty is the **combination** of cross-mechanism atlas + channel-conditioned quotient equivalence + scale-time nonseparability + manifold-curvature bookkeeping + prospective/withheld and failure-preserving validation.

## Publication assessment checkpoint

Current state: **promising but not submission-ready**.

Natural targets: JCAP, Physical Review D, MNRAS.

Highest-value remaining tasks before submission:

1. publication-quality figures generated from immutable artifacts;
2. observation-space closure for at least one flagship degeneracy-breaking example if feasible;
3. expanded prior-art comparison in Introduction/Discussion;
4. adversarial robustness tests under alternative norms/domains/solver settings where justified;
5. final notation audit and journal/arXiv LaTeX conversion.

Already completed in the paper branch: claim -> experiment -> run -> artifact -> digest provenance matrix, figure manifest, prospective-falsification section, reproducibility section, and the first reproducible Figure 3 plotting script.

## Resume instruction

On recovery, first read this checkpoint, then `papers/dsir1/AUTHOR_METADATA.yml`, `papers/dsir1/CLAIMS_LEDGER.md`, `papers/dsir1/PROVENANCE_MATRIX.md`, `papers/dsir1/manuscript.md`, `papers/dsir1/build_manuscript_v0_2.py`, and `papers/dsir1/LITERATURE_POSITIONING.md`. Do not reconstruct the paper from chat memory if these files are available.
