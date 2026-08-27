# DSIR-I manuscript workspace

Working title:

**Dark-Sector Influence Reconstruction I: Observable-response geometry, channel-conditional equivalence, and failure-resistant model comparison**

## Current files

- `manuscript.md` — article draft v0.1.
- `CLAIMS_LEDGER.md` — hard boundary between supported claims and prohibited overclaims.
- `references.bib` — initial literature positioning bibliography.

## Scientific center of the paper

The first paper is not a dark-sector discovery paper. It is a response-geometry / identifiability paper establishing that:

1. model equivalence is conditional on the physical/observational channel;
2. the additive `(G,T,tau)` summary fails for mechanisms with material irreducible `k x z` structure;
3. the descriptive nonseparability hierarchy `IDE < smooth-DE < GDM < f(R)` is robust over the frozen finite-amplitude and node-deletion tests;
4. one-parameter families can curve in response space, so linear representation rank is not microscopic parameter count;
5. WDM and withheld DCDM demonstrate qualitatively different scale/time localization mechanisms;
6. scientific FAILs remain provenance even when later providers pass separately frozen corrective contracts.

## Proposed main figures

### Figure 1 — DSIR operator architecture

Three layers: theory -> response -> observational quotient. Show

`r(theta) -> K_B -> W_B -> Q_B -> s_B`

and the equivalence condition `A_B(r1-r2)=0`, `A_B=Q_B W_B K_B`.

### Figure 2 — Irreducible scale-time response morphology

Heatmaps or residual panels for representative smooth-DE, IDE, GDM and designer-f(R) directions showing `I(z,k)` after subtracting the best additive `mu + T(k) + tau(z)` model.

### Figure 3 — Robust chi_I hierarchy

Finite-amplitude `chi_I` envelopes for IDE, smooth-DE, GDM and designer-f(R), with the 12 leave-one-node robustness results indicated separately.

### Figure 4 — Channel-conditional degeneracy breaking

Two panels:

- GDM `cs2` vs `cv2`: low-k matter angle ~0.3226 deg vs metric-slip angle ~137.94 deg.
- GDM vs f(R): leading scale-mode angle ~0.08-0.10 deg vs time/full-response separation.

### Figure 5 — Response-manifold curvature and localization mechanisms

Compare normalized trajectory bending for GDM viscosity and designer-f(R), then place WDM cutoff motion and DCDM temporal-centroid motion as qualitatively distinct localization controls.

### Figure 6 — Failure-resistant provenance

Two audit paths:

- C3 target-grid interpolation FAIL -> mechanism audit -> native-grid provider PASS;
- C5 q=1 GR-limit FAIL -> prospective accuracy ladder -> q=3 provider PASS.

The original FAIL nodes remain visible rather than being overwritten.

## Proposed main tables

1. Theory-family atlas C0-C6 and active/blind channels.
2. Representative `chi_I` and `eta_I` values.
3. Channel-conditioned pairwise angles.
4. Finite-amplitude curvature metrics.
5. Hard claim / experiment / artifact provenance table for the supplement.

## Reproducibility anchors already present in repository

Core numerical results are documented in `docs/BUYANOVGPT_TABLE.md`, `docs/GATES.md`, and experiment/recovery records. Late provider-certification evidence is recorded in:

- `recovery/exp070c_provider_checkpoint_2026-08-27.md`;
- `recovery/exp069h_c5_provider_certification_checkpoint_2026-08-27.md`;
- `recovery/exp071a_g7_common_physical_support_mask_preregistration_2026-08-27.md`.

The formal quotient definitions are in:

- `docs/CHANNEL_CONDITIONAL_EQUIVALENCE_QUOTIENT_THEOREMS_2026-08-27.md`.

## Remaining paper tasks

- Generate publication-quality figures directly from immutable experiment products.
- Build an explicit experiment-to-claim provenance table with run IDs, artifact IDs, digests, and frozen thresholds.
- Expand literature review and verify journal/DOI metadata for bibliography.
- Convert the stable manuscript to journal/arXiv LaTeX after figure numbering and notation are frozen.
- Add a dedicated numerical-method appendix with solver versions, gauges, masks, norms, and precision settings.
- Perform an internal adversarial audit: attempt to falsify every paper-level statement from repository evidence.
- Keep `G7=OPEN`, `G8=OPEN`, `G9=OPEN` in all versions unless independently closed by later prospectively frozen work.