# DESI DR2 compressed BAO data provenance

This directory contains the compressed DESI DR2 BAO likelihood vector and covariance, not raw spectra or redshift catalogs.

Cobaya's current DESI DR2 all-tracer BAO likelihood points to `bao_data/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt` and `desi_gaussian_bao_ALL_GCcomb_cov.txt` with `rs_fid: 1 Mpc`. A public MontePython likelihood mirror (`tkarwal/cosmo_likelihoods`, commit `04d673e9ececf7b5174410c7bdaea94819a5c7ef`) contains the matching files used here. Pinned blob SHAs: mean `8df6f1d2d0c02da3bcf6d0a959a01077c67cfd97`; covariance `fd8e5697ab61379b07b52efb781ea6713417a4d9`.

DSIR forms `F_AP=(D_M/r_d)/(D_H/r_d)=D_M/D_H` for paired anisotropic measurements. The sound-horizon calibration cancels algebraically, but the result still inherits the upstream BAO compression and FLRW distance interpretation.
