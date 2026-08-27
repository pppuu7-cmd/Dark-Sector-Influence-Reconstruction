# Exp073J — KiDS-BNT component support result v0.1

**Date:** 2026-08-27  
**Component status:** `FAIL_EXP073J_KIDS_COMPONENT_REPRODUCTION_OR_NUMERICAL_COMPLETENESS`  
**Full Exp073J scientific classification:** NOT AUTHORIZED

## Immutable provenance

- implementation merge: `55a9fa869e79a0aac11c54aac0115ff281352f24`;
- workflow run: `33045812989`;
- workflow job: `98429422683`;
- artifact: `9635628042`;
- artifact digest: `sha256:907ac6130afb2292eac6e8cdd03493bb0f3b4507d5042e1ac15c282bbb901d3b`;
- extracted JSON SHA256: `7edbbc6d842ddfee63e59bcdf71f5cb1074fdf9a50ec0656ffd4c522a10b2a35`.

The run completed successfully as infrastructure. The negative component status is produced by the prospectively frozen numerical-completeness controls, not by CI interruption.

## Passed controls

K1–K5 and K8–K10 passed. In particular:

- exact KiDS and CAMB provenance reproduced;
- the frozen BNT rows `[2,3,4]` reproduced and satisfied their nulling controls;
- the released `xi2bandpow` production semantics and default `pfrac=0.5` reproduced;
- all tested positive envelope normalizations were finite and positive at finite ell cutoff;
- physical `k=(ell+0.5)/chi` and the unchanged common C3+C5 rectangle were used;
- signed `P_Wm` semantics remained separate from the absolute support envelope;
- no fiducial `P(k)`, covariance, nuisance rank/SVD, relation/null result, G8 output, GR matter-to-Weyl closure or post-hoc cutoff was used;
- all 72 planned KiDS component coordinates were emitted machine-readably.

## Failed numerical-completeness controls

K6 failed decisively. Coarse and fine angular integrations restricted to `ell<=30000` agree at roughly `1e-5` relative level or better, so ordinary step-size convergence is excellent. Nevertheless the fine positive envelope accumulated between `ell=30000` and `60000` is enormous:

- GGL / `Wm`: `0.6541 ... 0.7140` of the full positive normalization;
- shear / `WW`: `0.6434 ... 0.7015`.

The frozen allowed tail was `2e-3`. This is therefore not a near-threshold numerical miss.

K7 also failed: maximum coarse/fine support-fraction discrepancy was `0.001723739486547582`, above the frozen `1e-3` trust tolerance. The finite-cutoff evaluator reported `0/24` Wm and `0/48` WW coordinates below the 5% support threshold, but those counts are **not scientific support results** because K6/K7 failed first.

## Mechanism indicated by the result

The observed tail is quantitatively consistent with the asymptotic behavior of a finite discrete theta-to-bandpower transform. The released operator is a finite sum of sampled Bessel terms. For fixed non-zero theta,

`J_n(ell theta) ~ sqrt(2/(pi ell theta)) cos(ell theta - phase)`.

The direct response includes the Hankel prefactor `ell`, so each uncancelled discrete endpoint/node contribution scales in envelope as approximately `sqrt(ell)`. Its absolute integral therefore grows approximately as `ell_max^(3/2)` rather than approaching a finite normalization.

A simple `sqrt(ell)` envelope predicts the fraction accumulated from `L` to `2L` to approach

`1 - 2^(-3/2) = 0.646446...`,

which is strikingly close to the measured 30k→60k tail fractions. This is a mechanism hypothesis, not yet a frozen classification: the next experiment must test the asymptotic scaling prospectively and distinguish the discrete released estimator from any mathematically continuous/apodized idealization.

## Scientific boundary

Do **not** convert this result into `FAIL_KIDS_BOSS_BNT_PHYSICAL_SUPPORT_EXP073J`. The current result says that the preregistered P-independent positive absolute-response measure for the released finite-theta KiDS estimator has not been shown to possess a cutoff-independent normalization.

Do not cure this by choosing an ell cutoff after seeing the output, by multiplying by fiducial `C_ell/P(k)`, or by allowing oscillatory cancellations inside the positive support measure. Such changes would alter the frozen support question.

The BOSS component result remains unchanged at `54/240` and remains non-classifying. Covariance restriction/whitening remains unauthorized.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
