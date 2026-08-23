# DSIR — Dark-Sector Influence Reconstruction

DSIR is a separate research program for model-agnostic inverse reconstruction of the cosmic dark sector.

## Core question
Instead of assuming what dark matter (DM), dark energy (DE), or modified gravity (MG) are, infer the minimal set of observable influence modes required by data, map known theories into that common response space, and search for robust relations/invariants between those influences.

## Project boundary
This repository is intentionally independent from the RTK research program. RTK is not imported, edited, or used as a prior. A mature external model may later be embedded into DSIR as one candidate theory under the same gates as all others.

## Scientific status
DSIR v0.x is an inference/reconstruction framework, not yet a fundamental physical theory. It becomes a candidate physical model only if robust residual relations lead to a consistent dynamics/action and new withheld/future predictions.

## Three-layer architecture
1. **Data layer**: likelihood-level observables and covariances.
2. **Response layer**: gauge-/frame-robust reconstructed responses (expansion, metric potentials, growth, lensing, tensor propagation, couplings, nonlinear responses).
3. **Theory layer**: embeddings such as effective residual stress tensor X_{mu nu}, generalized dark matter (GDM), PPF, EFT of DE/MG, interacting-sector models, and concrete microphysical theories.

Law discovery is performed primarily in the response layer and accepted only after invariance and holdout tests.

## Initial milestones
- G0: recover LambdaCDM exactly in the bookkeeping layer.
- G1: conservation/Bianchi and gauge-invariance tests.
- G2: define the DSIR response basis and observational covariance metric.
- G3: embed six control theory classes.
- G4: recover synthetic latent rank in Experiment 001.
- G5: define data-driven influence rank with noise calibration.
- G6: search for cross-channel relations with holdout prediction.

See `docs/DSIR_METHOD.md`, `docs/GATES.md`, and `docs/RESEARCH_LOG.md`.
