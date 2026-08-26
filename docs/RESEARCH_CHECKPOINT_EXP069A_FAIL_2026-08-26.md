# DSIR research checkpoint — Exp069A FAIL — 2026-08-26

## Frozen result

Exp069A produced the first science-evaluable C5 direct physical-power bridge result and is permanently recorded as

`FAIL_C5_DESIGNER_FR_PHYSICAL_POWER_BRIDGE_V0_1`.

Workflow run: `33009561221`  
Job: `98311997044`  
Artifact: `9622218451`  
Artifact ZIP SHA256: `8f10f440634e68e7cb732c82e07bbf2e533df5c73f69c87c8687c2d80a2295f9`  
Frozen preregistration commit: `370eaf8e34344ff93a0bb52e1d516ee151177bc2`.

This is a scientific FAIL of the frozen bridge implementation, not an infrastructure exception. The FAIL must not be overwritten by a later corrective experiment.

## What passed

The pinned H-EFTCAMB source contract was verified for direct CAMB power variables `delta_nonu` and `Weyl`, with

\[
W = k^2(\phi+\psi)/2.
\]

The direct physical-unit convention passed its independent roundtrip at maximum relative error

\[
5.463145055090619\times10^{-15}
\]

against the frozen threshold `2e-8`.

The exact designer `B0=0` output agreed bitwise with the GR reference in all three direct power blocks,

\[
P_{mm},\qquad P_{Wm},\qquad P_{WW},
\]

so the measured maximum relative difference was `0.0` for each block, well within the preregistered `5e-6` limit.

Signed single-mode coherence also passed:

\[
\rho^2=\frac{P_{Wm}^2}{P_{WW}P_{mm}},
\]

with maximum `|rho^2-1| = 1.5189047264385636e-7` versus the frozen `2e-5` threshold. The cross power retained negative sign; it was not replaced by an absolute value.

The deliberately wrong missing-`k^2` transfer-table convention was decisively rejected, with maximum relative discrepancies approximately `1.2345679011e10` in `WW` and `1.1111011111e5` in `Wm`.

## What failed

Every nonzero designer point

\[
B_0\in\{10^{-6},10^{-5},10^{-4},10^{-3}\}
\]

was bitwise identical to the exact-zero control in all three power blocks. Therefore the preregistered production nondegeneracy check A8 failed with

\[
\max |\ln |P_X(B_0)/P_X(0)||=0
\]

for `X in {mm,Wm,WW}` at every production point.

Designer child processes returned code zero and produced valid arrays but emitted no required `EFTCAMB: theory stable` marker, so A2 also failed. A3 was defined to inherit A2 and therefore failed at aggregate level even though its individual power-array finiteness/sign conditions were satisfied.

## Root-cause audit

The same designer `.ini` settings previously generated nonzero C5 responses through the pinned native H-EFTCAMB `./camb` executable. This strongly localizes Exp069A to the Python ingestion route rather than to the physical C5 settings.

Pinned upstream `camb/eftcamb.py` exposes the explicit API

`CAMBparams.EFTCAMB.initialize_parameters(camb_parameters, EFTCAMB_params, ...)`.

Pinned upstream `material/test_eftcamb_tree_MR.py` demonstrates this exact pattern: construct `model.CAMBparams()`, set ordinary CAMB cosmology, then call `pars.EFTCAMB.initialize_parameters(pars, eftcamb_params, ...)` before calculation.

Exp069A instead used ordinary `camb.read_ini(..., no_validate=True)` and then `camb.get_results(pars)`. The additional EFTCAMB model dictionary was never explicitly initialized. The observed exact-zero production response is therefore consistent with a no-op EFT layer in this Python path.

This diagnosis does **not** retroactively convert Exp069A into PASS.

## Corrective experiment boundary

A new Exp069B may test the official explicit EFTCAMB Python initialization path, but it must be preregistered before its first new numerical output. The corrective experiment must preserve the Exp069A physical content:

- same pinned H-EFTCAMB commit;
- same cosmology;
- same designer and stability settings;
- same `B0` points;
- same physical `(z,k)` grid;
- same direct `P_WW/P_Wm/P_mm` variable pairs;
- same physical-unit flags;
- same A4/A5/A6/A7 thresholds;
- same production nondegeneracy requirement.

Only the additional-parameter ingestion mechanism may change from ordinary `read_ini` to the upstream explicit `EFTCAMB.initialize_parameters` contract. Exp069B must also record the EFTCAMB `read_parameters()` dictionary/model name so that the active model state is independently auditable.

## G7 sequencing

Current top-level state remains:

- G7: OPEN
- G8: OPEN
- G9: OPEN

The valid order remains:

1. certify C5 and C3 physical power-input bridges;
2. preregister and evaluate the common ACT physical support/leakage mask;
3. restrict covariance and construct the no-repair whitener for the retained coordinates;
4. only then measure nuisance tangent rank/SVD and quotient;
5. fit/freeze one training-only G7 relation plus null/permutation control;
6. only after that select a fresh G8 withheld family.
