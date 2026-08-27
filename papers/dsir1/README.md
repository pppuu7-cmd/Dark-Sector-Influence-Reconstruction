# DSIR-I manuscript workspace

Working title:

**Dark-Sector Influence Reconstruction I: Observable-response geometry, channel-conditional equivalence, and failure-resistant model comparison**

## Current files

- `manuscript.md` — article draft v0.1.
- `CLAIMS_LEDGER.md` — hard boundary between supported claims and prohibited overclaims.
- `PROVENANCE_MATRIX.md` — manuscript claim -> experiment -> run -> artifact -> digest -> frozen criterion traceability.
- `FIGURE_MANIFEST.md` — publication figure definitions, exact data sources, and caption boundaries.
- `LITERATURE_POSITIONING.md` — prior-art comparison and publication/journal assessment.
- `references.bib` — initial literature bibliography.
- `figures/fig03_chiI_hierarchy.py` — reproducible builder for the central hierarchy/robustness figure.
- `recovery/dsir1_paper_checkpoint_2026-08-27.md` — chat-independent recovery entry point.

## Scientific center of the paper

The first paper is not a dark-sector discovery paper. It is a response-geometry / identifiability paper establishing that:

1. model equivalence is conditional on the physical/observational channel;
2. the additive `(G,T,tau)` summary fails for mechanisms with material irreducible `k x z` structure;
3. the descriptive nonseparability hierarchy `IDE < smooth-DE < GDM < f(R)` is robust over the frozen finite-amplitude and node-deletion tests;
4. one-parameter families can curve in response space, so linear representation rank is not microscopic parameter count;
5. WDM and withheld DCDM demonstrate qualitatively different scale/time localization mechanisms;
6. scientific FAILs remain provenance even when later providers pass separately frozen corrective contracts;
7. a prospectively frozen common full-response-centroid law was genuinely falsified by withheld IDM-DR (Exp054C/F27), constraining any universality claim.

## Main figures

### Figure 1 — DSIR operator architecture

Three layers: theory -> response -> observational quotient. Show

`r(theta) -> K_B -> W_B -> Q_B -> s_B`

and the equivalence condition `A_B(r1-r2)=0`, `A_B=Q_B W_B K_B`.

### Figure 2 — Failure of the additive scale+time core

Show representative `R`, additive `mu+T+tau`, and irreducible `I(k,z)` for contrasting mechanisms, anchored to Exp045A.

### Figure 3 — Robust chi_I hierarchy

Finite-amplitude `chi_I` envelopes for IDE, smooth-DE, GDM and designer-f(R), with leave-one-node robustness from Exp047B. Reproducible plotting script is already present at `figures/fig03_chiI_hierarchy.py`.

### Figure 4 — Channel-conditional degeneracy breaking

Two panels:

- GDM `cs2` vs `cv2`: low-k matter angle ~0.3226 deg vs metric-slip angle ~137.94 deg;
- GDM vs f(R): leading scale-mode angle ~0.08-0.10 deg vs time/full-response separation.

### Figure 5 — Curved trajectories and mechanism diversity

Compare GDM viscosity and designer-f(R) trajectory bending, WDM cutoff motion, and DCDM temporal-centroid motion.

### Figure 6 — Failure-resistant science

Include both provider correction chains and the prospective universality failure:

- C3 target-grid interpolation FAIL -> mechanism audit -> native-grid provider PASS;
- C5 q=1 GR-limit FAIL -> prospective accuracy ladder -> q=3 provider PASS;
- common C3/C5 centroid calibration -> frozen prediction -> withheld C7/IDM-DR opposite-sign slopes -> FAIL.

The original FAIL nodes remain visible rather than being overwritten.

## Proposed main tables

1. Theory-family atlas C0-C6 and active/blind channels.
2. Representative `chi_I` and `eta_I` values.
3. Channel-conditioned pairwise angles.
4. Finite-amplitude curvature metrics.
5. Hard claim / experiment / artifact provenance table based directly on `PROVENANCE_MATRIX.md`.
6. Prospective PASS/FAIL ledger so the paper cannot become success-selected.

## Reproducibility anchors already present in repository

Core numerical results are documented in machine-readable derived products and the scientific findings register. Late provider-certification evidence is recorded in:

- `recovery/exp070c_provider_checkpoint_2026-08-27.md`;
- `recovery/exp069h_c5_provider_certification_checkpoint_2026-08-27.md`;
- `recovery/exp071a_g7_common_physical_support_mask_preregistration_2026-08-27.md`.

The formal quotient definitions are in:

- `docs/CHANNEL_CONDITIONAL_EQUIVALENCE_QUOTIENT_THEOREMS_2026-08-27.md`.

The prospective universality falsification is in:

- `docs/SCIENTIFIC_FINDING_F27_COMMON_RESPONSE_CENTROID_WITHHELD_FAILURE.md`.

## Preparation status

Completed in the paper branch:

- [x] Full manuscript v0.1.
- [x] Hard claims / prohibited-overclaims ledger.
- [x] Targeted prior-art and journal positioning audit.
- [x] Chat-independent recovery checkpoint.
- [x] Exact claim-to-run/artifact/digest provenance matrix for central quantitative statements.
- [x] Publication figure manifest with source and caption boundaries.
- [x] First reproducible central-figure plotting script.
- [x] Add prospective Exp054C/F27 failure to the paper evidence package.

Remaining before submission:

- [ ] Integrate F27 and a dedicated data/code/reproducibility section into the main manuscript text.
- [ ] Generate and inspect publication-quality Figure 1-6 outputs from immutable inputs.
- [ ] Build the family/block atlas and prospective PASS/FAIL tables.
- [ ] Expand literature review and verify final journal/DOI metadata in the bibliography.
- [ ] Add a dedicated numerical-method appendix with solver versions, gauges, masks, norms, and precision settings.
- [ ] Perform an internal adversarial audit of every Abstract/Conclusions sentence against `PROVENANCE_MATRIX.md`.
- [ ] If scientifically clean and without scope creep, carry one flagship degeneracy-breaking example through common support, covariance whitening, and nuisance quotienting.
- [ ] Convert stable manuscript to journal/arXiv LaTeX after figure numbering and notation are frozen.

## Non-negotiable gate boundary

Keep `G7=OPEN`, `G8=OPEN`, `G9=OPEN` in all manuscript versions unless independently closed by later prospectively frozen work. A theory-response separator is not observational significance, and a failed universal relation must remain failed.
