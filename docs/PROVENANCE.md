# Data provenance and correction ledger

## DESI DR1 ShapeFit compressed responses

**Accepted source:** the February 2026 erratum to DESI 2024 V (JCAP 02 (2026) E02; DOI 10.1088/1475-7516/2026/02/E02).

The erratum states that a numerical implementation error in Appendix A of the original paper affected all measurements involving `f sigma_s8` and the associated covariance entries. Figures, tables, conclusions, and the underlying analysis were not affected. DSIR therefore rejects the original Appendix-A growth datavectors/covariances and stores only the corrected values in `data/observations/desi_dr1_shapefit_erratum_2026.json`.

A regression test explicitly checks that the corrected LRG1 value `f_sigma_s8=0.513635` is used rather than the obsolete Appendix-A value `0.318967`.

The BGS `DH/DM` component is not used in the AP-growth stability diagnostic because the DESI paper warns it is strongly influenced by the bounded AP prior at low redshift.

## Claim discipline
A correction to an input product is not a DSIR discovery. Any result that changes when switching between superseded and corrected source products is classified as provenance-sensitive and cannot pass G7/G8.
