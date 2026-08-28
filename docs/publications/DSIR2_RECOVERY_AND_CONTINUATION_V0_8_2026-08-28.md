# DSIR-2 recovery and continuation — v0.8

**Date:** 2026-08-28  
**Repository:** `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`  
**Branch:** `article2-manuscript-start-2026-08-28`  
**Draft PR:** #164 — `Start DSIR-2 manuscript with falsification-first recovery package`

## 0. Fast recovery verdict

Article 2 is no longer waiting on another K1/K2 experiment or on publication-build debugging.

Scientific verdict on `main`:

`ARTICLE2_SCIENTIFIC_EVIDENCE_CHAIN_CLOSED_FOR_DECLARED_SCOPE_V0_1`

Current journal-neutral publication verdict on this branch:

`PASS_DETERMINISTIC_WIDTH_SAFE_JOURNAL_NEUTRAL_RELEASE_BASELINE_V0_3`

Do not reopen science merely to add another near-duplicate response angle. Reopen only for a concrete scientific defect: wrong immutable artifact, convention/unit error changing a scored response, failed exact reproduction, frozen-threshold misapplication, or a manuscript claim exceeding its registered comparison object.

## 1. Fresh-session read order

Read in this order:

1. `docs/publications/DSIR2_MANUSCRIPT_V0_5.md`
2. `docs/ARTICLE2_CLAIM_MATRIX_CURRENT.md` on `main`
3. `docs/ARTICLE2_FINAL_SCIENCE_CLOSURE_AUDIT_2026-08-28.md` on `main`
4. `docs/publications/DSIR2_CLAIM_TO_EVIDENCE_AUDIT_V0_2_2026-08-28.md`
5. `docs/publications/DSIR2_SUBMISSION_READINESS_LEDGER_V0_2_2026-08-28.md`
6. `docs/publications/DSIR2_RELEASE_QA_V0_3_2026-08-28.md`
7. `docs/publications/DSIR2_TABLE1_TERMINAL_COMPARISON_MATRIX_V0_1.md`
8. `docs/publications/DSIR2_TABLE2_PROVENANCE_LEDGER_V0_2.md`
9. `docs/publications/DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json`
10. `scripts/publications/make_dsir2_figures_v0_3.py` — accepted visual construction
11. `scripts/publications/make_dsir2_figures_v0_4.py` — deterministic serialization wrapper
12. `docs/publications/latex/article2/dsir2_journal_neutral_v0_3.tex`
13. `docs/publications/DSIR2_NOVELTY_AUDIT_V0_2_2026-08-28.md`
14. `docs/publications/DSIR2_LITERATURE_SCAFFOLD_V0_3.md`
15. `docs/publications/DSIR2_REFERENCES_VERIFIED_V0_1.bib`

Historical v0.1/v0.2/v0.3 files remain audit snapshots and should not be deleted.

## 2. Active scientific thesis

Strongest safe Article-2 thesis:

> Dark-sector response equivalence is conditional on the response representation, on whether the relevant physical directions are resolved in that representation, on the selected channel/operator and metric, and on whether physical nuisance freedom is an oriented ray, a two-sided line, or a higher-dimensional subspace. Known-sector controls demonstrate both false separation and representation-induced false absence.

Compact hierarchy:

`representation -> resolvability -> ray/line/subspace -> channel/operator + metric -> physical support -> finite observation operator -> downstream observational quotient`

Article 2 stops before covariance whitening and observational nuisance quotienting.

## 3. Core formalism

Metric norm:

`||x||_M = sqrt(x^T M x)`

Oriented-ray angle:

`cos(theta_ray) = (r^T M n)/(||r||_M ||n||_M)`

Two-sided nuisance-line angle:

`theta_line = acos(|r^T M n|/(||r||_M ||n||_M))`

Multi-nuisance metric projector:

`P_N = N (N^T M N)^+ N^T M`

Nuisance-orthogonal response fraction:

`eta_N = ||r-P_N r||_M / ||r||_M`

Do not set observational `M=C^-1` until the downstream support/covariance gates are valid.

## 4. Terminal Article-2 science chain

### Exp071C — matter-only known-sector falsification

- prereg `4180661fe3187c710c363cdbafac12de2dc70d41`;
- run `33020201997`;
- job `98348450038`;
- artifact `9626235928`;
- digest `ed486effa593a409640577f8cdde614d5fddfc95653eb4ca78c56ae69a234e5e`;
- classification `F30_DARK_SPECIFICITY_WEAKENED_BY_KNOWN_SECTOR_CONTROL`.

K2 passes the frozen F30 matter-morphology gate; K1 does not. Therefore F30/matter morphology is not generically dark-specific.

### Exp071E/F — static augmentation

Exp071E equalized `(r_W, Delta_slip)`:

- K2 vs GDM cs2 `18.925666634781507°`;
- K2 vs GDM cv2 `58.912673573574864°`.

Exp071F:

- matter-only `19.223081503733017° / 19.037102938963482°`;
- `(r_P,r_W,Delta_slip)` `19.07487721786906° / 50.16673498586107°`.

Static extra channels are informative but do not generically remove the cs2-like known-sector ambiguity.

### Exp071H — preregistered positive temporal ray

- positive K2 oriented angles `138.1005853262° / 137.0972592611°`;
- frozen threshold `45°`;
- preregistered oriented result remains PASS;
- retrospective line angles `41.8994147° / 42.9027407°` are descriptive only and do not reclassify the preregistered experiment.

Negative temporal K2 remains an optional extension, not an Article-2 gate.

### Exp071I/J/K — positive velocity ray and robustness

Exp071I raw CLASS total-velocity-transfer response:

- `165.9454940017539° / 164.7113289163152°`;
- GDM mutual `2.3682514521619247°`.

Exp071J removes the per-redshift constant-in-k amplitude mode:

- `166.43869440595827° / 164.92709673022526°`;
- retained norms about `0.83187 / 0.82718 / 0.83724` for K2/cs2/cv2;
- line angles `13.56130559404173° / 15.07290326977474°`.

Exp071K all 24 leave-one-k/z positive-ray tests pass; global minimum `157.8212319078°`.

These establish robust separation of the selected positive K2 ray only.

### Exp071L — two-sided K2 falsification

- K2+ `166.4386944° / 164.9270967°`;
- K2− `13.5502602743° / 15.0708844313°`;
- K2− vs K2+ `179.9078020829°`;
- antisymmetry error `0.002992249341414612`;
- classification `K2_TWO_SIDED_VELOCITY_SHAPE_OVERLAPS_GDM_EXP071L`.

This is the central ray-versus-line falsification. Never claim that the positive ~165° velocity result proves sign-invariant nuisance specificity.

### Exp071M — representation kernel

K1 uses `n_s=0.965 +/- 0.005`.

Both fresh K1 signs give exactly zero transfer-only response:

`Delta ln|t_tot(K1)/t_tot(ref)| = 0`

on the full frozen support.

Terminal status:

`INVALID_FOR_SCIENCE_EXP071M`

Meaning: pure primordial tilt lies in the kernel of this transfer-only representation. No normalized K1/GDM angle is scientifically defined there. Never write that primordial tilt has no physical effect.

### Exp071N — physical K1 recovery

Common physically complete linear velocity-power response:

`r_vv = Delta ln P_R(k) + 2 Delta ln|t_tot(z,k)|`.

Results:

- K1+ vs cs2/cv2 `36.06223725044938° / 37.84581229951204°`;
- K1− `143.93776274955064° / 142.15418770048797°`;
- K1− vs K1+ `179.99999914622634°`;
- antisymmetry error `0.0`;
- physical line angles `36.06223725044938° / 37.84581229951204°`;
- K1 retained norm `0.625535121104866`;
- GDM retained norms `0.8271831838994257 / 0.8372386500341654`;
- fresh reference P and t_tot reproduce parent with max relative difference `0.0` against `1e-10`;
- classification `K1_TWO_SIDED_VELOCITY_POWER_SHAPE_OVERLAPS_GDM_EXP071N`.

Resolving a nuisance is necessary for specificity testing but is not sufficient to produce specificity.

## 5. Provider / finite-observation applicability chain

### Exp071A

Final successful scientific binding:

- run `33027562195`;
- job `98372366778`;
- artifact `9629064009`;
- digest `4955a3a917992ad38423d9fe2dda3682822c7b86614950467faf5a46a7426675`;
- 495/495 provider cells retained.

Historical run `33027159066` remains an infrastructure-packaging failure after the unchanged evaluator completed. Keep it separate from the final scientific artifact.

### Exp072A

ACT×unWISE first route:

- 0/26 retained at frozen 5% leakage;
- scientific support FAIL, not infrastructure failure.

### Exp072C

Planning frontier only:

- `z_min = 0.0087345857837422`;
- `k_max = 4.818261097432861 Mpc^-1`;
- 15/26 geometric route.

Do not call this a validated linear science region.

### Exp073A

- retained dimension 0 for `Delta_m^2` thresholds 0.5, 1, 2;
- classification `INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`.

### Exp073J / Exp073L

BOSS finite-matrix component:

- 54/240 retained;
- explicitly non-classifying.

KiDS finite-theta chain:

- Exp073J 0/72 came from numerical-completeness failure and is not a physical support FAIL;
- terminal statement is Exp073L: attempted P-independent absolute positive-support normalization is non-normalizable under the frozen extended asymptotic test.

Provider completeness is not observational admissibility. Theory/provider angles are not survey distinguishability.

## 6. Active manuscript and tables

Active science manuscript:

`docs/publications/DSIR2_MANUSCRIPT_V0_5.md`

Title:

**Dark-Sector Influence Reconstruction II: Falsifying Channel-Conditioned Specificity Across Static, Temporal, and Velocity Response Spaces**

Table 1 prose source:

`DSIR2_TABLE1_TERMINAL_COMPARISON_MATRIX_V0_1.md`

Current LaTeX Table 1:

`latex/article2/table1_terminal_comparison.tex`

It was revised to a width-safe `tabularx` layout after a full-resolution render exposed right-edge clipping. The scientific values are unchanged.

Table 2:

`DSIR2_TABLE2_PROVENANCE_LEDGER_V0_2.md`

LaTeX:

`latex/article2/table2_provenance.tex`

## 7. Figures

Frozen numeric manifest:

`DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json`

Accepted visual construction:

`scripts/publications/make_dsir2_figures_v0_3.py`

v0.3 fixed the earlier layout issues and is the visual/scientific basis.

Deterministic release wrapper:

`scripts/publications/make_dsir2_figures_v0_4.py`

v0.4 imports/reuses the v0.3 constructors unchanged, fixes SVG hash salt, removes volatile PDF/SVG metadata, and emits `_v0_4` files. It changes no scientific number, threshold, label, geometry, or classification.

The final QA generates all v0.4 files twice and requires exact SHA256 equality.

## 8. Journal-neutral LaTeX

Current source:

`docs/publications/latex/article2/dsir2_journal_neutral_v0_3.tex`

Changes relative to v0.2 are publication-engineering only:

- direct v0.4 figure paths;
- long hierarchy equation split over two lines;
- Table 1 width-safe via shared table source;
- reproducibility text updated for deterministic v0.4 serialization.

No scientific result changed.

## 9. Canonical deterministic release QA

Record:

`docs/publications/DSIR2_RELEASE_QA_V0_3_2026-08-28.md`

Workflow:

`.github/workflows/article2-publication-qa-v0-1.yml`

Canonical run:

- run `33197943484`;
- job `98939798625`;
- head `8cc93e3c9165806888c071a624d1364d7ff9595d`;
- artifact `9696572756`;
- artifact digest `sha256:c24514f2e2cbbd81fed425b9f7c4474d226b7cf7eb80719999f446d9b2f5c714`;
- final 10-page PDF SHA256 `ad67168a318ec16c954fb665f5edded79167c3ebe507e2912f368271eed944ff`.

Automated PASS gates:

- pinned Python 3.12.14 / NumPy 2.5.2 / Matplotlib 3.11.1;
- two independent v0.4 figure generations: exact PDF/SVG SHA256 equality;
- fixed `SOURCE_DATE_EPOCH=1787875200` and `FORCE_SOURCE_DATE=1`;
- two clean LaTeX/BibTeX builds: exact PDF byte equality;
- no unresolved citations/references;
- no overfull hbox/vbox;
- immutable artifact upload.

Render-first audit after download:

- 10/10 pages render;
- no clipping, overlap, broken glyphs, or missing figure/table objects;
- page 2 hierarchy equation fully inside the text block;
- page 4 Table 1 fully visible including Interpretation;
- Figures 1–4 visually accepted;
- Table 2/bibliography visible.

## 10. Bibliography / novelty

Bibliography:

`DSIR2_REFERENCES_VERIFIED_V0_1.bib`

Important corrections/current state:

- CLASS II is arXiv `1104.2933`, DOI `10.1088/1475-7516/2011/07/034`;
- arXiv `2005.01057` authors corrected to Eileen Giesel, Robert Reischke, Björn Malte Schäfer, Dominic Chia;
- Adam 2026 arXiv `2608.18224` remains a submission-date recheck item.

Novelty audit:

`DSIR2_NOVELTY_AUDIT_V0_2_2026-08-28.md`

Do not claim novelty for:

- nuisance projection/hardening;
- principal angles/subspace geometry;
- Fisher/information geometry;
- SVD/model-specific subspaces;
- Fisher-preserving compression;
- the generic idea that compression can hide new physics;
- generic dark-matter nuisance geometry.

Safe workflow-level positioning:

> Our contribution is not a new projection or information-geometric formalism, but a fail-closed response-comparison workflow that makes representation resolvability and the physical nuisance object explicit before assigning specificity, and tests that workflow prospectively with independent known-sector falsification controls.

Avoid `first` / `to our knowledge` priority wording in the Abstract until the submission-date full-text/citation-graph audit is complete.

## 11. Forbidden scientific upgrades

Do not state:

- dark-sector detection;
- unique dark-sector fingerprint;
- unique microscopic identification;
- proof of modified gravity;
- F30 is dark-specific;
- temporal response is tracer RSD;
- `t_tot` is tracer RSD, theta_m, f, or f sigma8;
- `r_vv` is a tracer-level observable;
- theory/provider angle is survey significance;
- more channels guarantee specificity;
- positive K2 ~165° implies sign-invariant nuisance specificity;
- Exp071M proves primordial tilt has no physical effect;
- Exp072C frontier is a validated linear science region;
- Exp073J BOSS 54/240 is a survey classification;
- Exp073J KiDS 0/72 is a physical support FAIL;
- G7/G8/G9 are closed.

## 12. Current submission readiness

Use:

`DSIR2_SUBMISSION_READINESS_LEDGER_V0_2_2026-08-28.md`

Current status:

`SCIENCE_CLOSED_JOURNAL_NEUTRAL_BUILD_BASELINED_SUBMISSION_FORMATTING_OPEN_V0_2`

No active Article-2 scientific blocker is identified.

Remaining critical path:

1. select target journal;
2. rerun final full-text/citation-graph novelty audit at actual submission date;
3. map v0.3 journal-neutral source into journal template;
4. insert author/affiliation/acknowledgement metadata;
5. final journal-specific language/style pass;
6. final deterministic/render-first audit of the submission package.

## 13. Article-3 handoff

Article 2 sharpens but does not execute the downstream observational nuisance quotient.

Article 3 should:

1. validate the finite observation reconstruction;
2. score physical support;
3. restrict covariance to retained coordinates;
4. whiten;
5. construct every resolved signed nuisance direction in the same observation space;
6. form the metric nuisance projector/subspace;
7. test the surviving nuisance-orthogonal dark-sector response.

A nuisance that is null in an intermediate theory representation must not be declared harmless; it must be tested in the final representation where primordial, transfer, window, calibration, tracer, or other factors may restore it.

G7/G8/G9 remain OPEN.

## 14. Immediate next action for a new chat

Do **not** rerun K1/K2 merely to make progress. The highest-value Article-2 action is now target-journal selection and final submission-date literature/novelty audit. If no journal is yet selected, keep the current deterministic journal-neutral baseline intact rather than changing science or layout speculatively.