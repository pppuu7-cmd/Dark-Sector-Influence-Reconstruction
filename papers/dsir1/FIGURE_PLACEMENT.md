# DSIR-I Figure placement plan — v0.2

This file freezes the manuscript-level placement logic for the six principal figures before LaTeX conversion. The deterministic v0.2 assembler inserts textual figure references at these anchors; final float placement may move during journal typesetting without changing scientific ordering.

| Figure | Primary manuscript anchor | Narrative role |
|---|---|---|
| Figure 1 | end of §4.3, before Theory atlas | define the operator/equivalence architecture before numerical examples |
| Figure 4 | end of §6.2 | show both channel-conditional degeneracy examples immediately after they are introduced |
| Figure 2 | end of §6.3 | visualize why the additive `mu+T+tau` core fails before the finite-amplitude hierarchy |
| Figure 3 | end of §6.4 | central hierarchy + 12/12 node-robustness figure |
| Figure 5 | end of §6.8, before prospective falsification | connect curvature, WDM scale localization, and DCDM temporal localization |
| Figure 6 | end of §7, before prior-art discussion | summarize permanent provider FAILs, corrective contracts, and prospective F27 falsification |

## Text references inserted by the v0.2 builder

1. After §4.3: `Figure 1 summarizes the induced signature operator and the compatibility condition for channel refinement.`
2. After §6.2: `Figure 4 juxtaposes the two frozen examples of channel-conditional degeneracy breaking.`
3. After §6.3: `Figure 2 shows the additive projection and irreducible interaction directly for the frozen low-k response atlas.`
4. After §6.4: `Figure 3 summarizes the finite-amplitude hierarchy and its deterministic leave-one-node robustness.`
5. After §6.8: `Figure 5 compares response-manifold curvature with the distinct WDM scale-localization and DCDM time-localization controls.`
6. After §7: `Figure 6 summarizes the failure-resistant chronology, retaining original failed contracts beside separately frozen corrective providers and the prospective F27 falsification.`

## Caption source

Publication-ready captions are canonical in `papers/dsir1/FIGURE_CAPTIONS.md` and are not duplicated in the body during Markdown assembly. The later journal/arXiv LaTeX builder should source or reproduce those captions verbatim unless a caption change is explicitly versioned.

## Ordering rationale

The figure numbering follows the logical argument rather than section-number order: formal operator architecture first; additive-core failure and hierarchy next; channel degeneracy is Figure 4 because Figures 2–3 form the central morphology sequence; mechanism diversity follows; failure provenance closes the empirical/method section. The final LaTeX conversion may reorder Figure 2/4 numbering if required for first-reference order, but such a change must update `FIGURE_MANIFEST.md`, `FIGURE_CAPTIONS.md`, this file, and all manuscript references together.