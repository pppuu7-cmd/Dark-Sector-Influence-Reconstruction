# Exp073H — official Grieb Fourier-wedge archive binding v0.1

**Date:** 2026-08-27  
**Scope:** source/operator inventory only under the frozen Exp073H preregistration; no support fraction is computed.

## Official source

The SDSS-III BOSS publications/results page identifies the final-sample Fourier-space clustering-wedge analysis by Grieb et al. and links its Fourier-space wedges, covariance matrices, window functions and figures to the SDSS SAS.

The exact official archive target frozen for the first Exp073H binding run is:

`https://data.sdss.org/sas/dr12/boss/papers/clustering/GRIEB_ET_AL_2016_COMBINEDDR12_power_spectrum_wedges.tar.gz`

The first successful workflow retrieval must record the archive SHA256 and SHA256 of each extracted object before any support calculation. That digest becomes immutable provenance for subsequent Exp073H classification.

## No-leakage rule

The binding workflow may inventory covariance-like filenames because they may be inseparable from the archive manifest, but it must not read covariance numerical contents. It may read small non-covariance ASCII objects only to identify explicit k coordinates, measurement tables, window/operator tables and documentation.

No support fraction, covariance weighting, nuisance rank, relation/null residual or G8 information is allowed in this binding phase.

## Decision after inventory

After the immutable archive inventory exists, Exp073H may classify only against the already-frozen H1-H8 criteria. In particular, a PASS requires an explicit finite Fourier k coordinate/window with a finite non-negative operator support measure that does not require a fiducial P(k), nonlinear damping or post-hoc k cutoff.

G7 OPEN. G8 OPEN. G9 OPEN.
