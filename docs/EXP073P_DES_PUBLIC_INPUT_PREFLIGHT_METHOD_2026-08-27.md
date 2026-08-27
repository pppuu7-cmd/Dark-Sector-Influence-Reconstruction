# Exp073P DES public-input checksum preflight method

**Date:** 2026-08-27

This is an implementation/provenance preflight under the already-frozen Exp073P contract. It is not a new experiment classification and does not evaluate any physical-support fraction.

The preflight verifies the exact frozen `Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463` source, binds the Exp073O parent result, probes every DES Y1 release object named in Exp073P, and SHA256-binds only public objects small enough to download within the implementation-only 200 MiB preflight cap.

The cap is **not** a scientific acceptance criterion and does not change Exp073P. Its sole purpose is to prevent a provenance probe from becoming an uncontrolled ~100 GB data transfer. If any required public object lacks an exact checksum after this preflight, Exp073P P2 remains incomplete and support fractions remain forbidden.

The frozen scientific criteria remain unchanged:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05`;
- minimum retained full-coordinate dimension `15`;
- classifying `nside=4096`;
- signed Wm in the observable, with absolute value only for the positive support envelope;
- no covariance, nuisance SVD/rank, quotient/relation/null, G8 or article-selection information before support PASS.

A preflight status `BLOCKED_PRE_SUPPORT_INPUT_CHECKSUM_BINDING_EXP073P_PREFLIGHT` is neither an Exp073P scientific FAIL nor an infrastructure FAIL. It means only that P2 has not yet been made complete enough to authorize support evaluation.
