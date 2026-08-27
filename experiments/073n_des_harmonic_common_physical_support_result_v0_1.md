# Exp073N — DES harmonic Wm+WW + BOSS mm common physical-support result v0.1

**Date:** 2026-08-27  
**Classification:** `FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE`

## Immutable execution

- implementation merge: `6868ed9113e2697675756f23fae8d350a9239bf6`;
- workflow run: `33062650033`;
- workflow job: `98484967582`;
- artifact: `9642372335`;
- artifact digest: `sha256:914d23e9d708a7b8cb9e097a69845e2630ec265b5ccc489ce9a8d389d4e198db`;
- extracted JSON SHA256: `e4eb6cd10ac964030e84596ee352f22c5c2d4fae91e917a68db567cef2b6adeb`.

The workflow completed successfully. This classification is therefore the frozen Exp073N reproduction/provenance outcome, not an infrastructure interruption.

## Pre-output audit result

Exp073N section 3 required every public input needed for the exact DES harmonic operator to be reproducibly bound before evaluating any physical-support fraction.

The frozen operator repository `hocamachoc/3x2hs_measurements@21e589a3cfc3e30f1b06a4636ccc2da8aceda5ab` reproduced exactly. However:

- the only Y3 YAML configurations at the frozen pin are `y3flask_csh.yml` and `y3flask_gcl.yml`;
- there is no public real-data Y3 GGL configuration at that pin;
- frozen `ggltest.py` executes only `type == "flask"` and raises `NotImplementedError` otherwise;
- consequently the exact published DES Y3 real-data Wm NaMaster workspace/input realization cannot be reproduced from the frozen public source binding;
- the Y1 WW configuration exists but itself points to site-local `/global/cscratch1/...` inputs, reinforcing why Exp073N correctly demanded explicit public-file rebinding before support output.

Pinned file hashes from the successful audit:

- `ggltest.py`: `8d62e76981f452ccad697dab8087bf7857cd7af605343611d74f99c1961e1b5b`;
- `etc/y1mcal_csh.yml`: `a25cd5c6e9fc692bce96c8e2ff3faa58045bb9cbaef43966ec1cd449a1daba77`;
- `etc/binNicola2020.txt`: `05224053479e7d103cca640ab2629fc07bfdef5781612a08dae6bf97d74c812e`.

The DES Y3 harmonic-space publication independently states that the Y3 lens/source catalogues and redshift distributions are publicly released and points to this measurement repository. That publication-level availability does not supply the missing exact real-data GGL configuration/workspace provenance required by the stricter frozen Exp073N contract.

## Scientific boundary

This is **not** `FAIL_DES_HARMONIC_COMMON_PHYSICAL_SUPPORT_EXP073N`.

No `f_invalid`, no DES Wm/WW support fraction and no combined retained dimension were evaluated. Therefore no statement is made about whether the DES route would pass or fail the unchanged 5% physical-support threshold if a fully reproducible exact operator realization were available.

The parent Exp073M landscape result remains preserved: it established an operator-class candidate, while Exp073N shows that the exact frozen public realization is insufficient for the mandatory reproducibility gate.

No threshold, rectangle or parent classification is weakened:

- common rectangle remains `0.295 <= z <= 2.33`, `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05` remains unchanged;
- minimum retained dimension remains 15;
- BOSS mm remains 54/240 retained and non-classifying;
- covariance/whitening, nuisance SVD, relation/null and G8 remain unauthorized.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
