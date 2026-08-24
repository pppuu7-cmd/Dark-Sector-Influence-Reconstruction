# Experiment 026b — H-EFTCAMB designer-f(R) MG-S1 hard regression

Date: 2026-08-24
Status: **PASS**
Gate: MG-S1 / G3B C5 production-manifold admission

## Why a second run was required

Experiment 026 first established the common-baseline, multi-redshift designer-f(R) manifold. The initial run exposed two infrastructure issues rather than a physical failure: CAMB requires transfer redshifts in decreasing order, and a shell pipeline without `pipefail` could hide a non-zero solver exit code. Both were corrected without changing the physical model or B0 scan.

The first successful common-baseline calibration also showed that the pinned CAMB text writer uses `E15.6` formatting for matter-power output. A text-output-only high-precision audit changed the writer format to `E25.16` before compilation, with equations and cosmological/model parameters unchanged. The exact-zero residual fell from about `4.38e-6` to about `1.06e-6`, demonstrating that ASCII quantization was a material part of the apparent floor.

The high-precision calibration was then used only to choose hard thresholds. Those thresholds were frozen in `ci/eftcamb_fr_mgs1_gate.py` **before** the fresh hard run reported here.

## Frozen hard criteria

The hard regression requires:

1. exact-zero closure over the full frozen 7x5 response grid,

\[
\max_{z,k}|r_\Delta(B_0=0)|\le 2\times10^{-6};
\]

2. production designer instances satisfy

\[
B_0\ge10^{-6};
\]

3. every production instance has resolved response amplitude

\[
\max|r_\Delta|\ge10^{-4};
\]

4. maximum response amplitude is strictly increasing across the ordered production B0 grid;

5. every designer run is finite, reports the upstream `EFTCAMB: theory stable` marker and contains no `ERROR STOP`.

`B0=1e-7` is deliberately retained as a solver-threshold transition control and excluded from the production gate.

## Fresh hard run

GitHub Actions run:

`32759477319`

Head commit:

`57d7362a0564468ba6d0caee7e992e103723acc2`

Pinned upstream:

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`

Hard artifact digest:

`sha256:9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`

## Hard result

Exact zero:

\[
\boxed{\max|r_\Delta(B_0=0)|=1.0606553430541908\times10^{-6}}
\]

which passes the pre-frozen `2e-6` threshold.

Transition control:

| B0 | max |r_Delta| | role |
|---:|---:|---|
| `1e-7` | `3.8975820224e-6` | solver/GR-threshold transition control; excluded from production |

Production set:

| B0 | max |r_Delta| | gate |
|---:|---:|---|
| `1e-6` | `8.9041074888e-4` | PASS |
| `1e-5` | `6.2109886780e-3` | PASS |
| `1e-4` | `4.2905258691e-2` | PASS |
| `1e-3` | `1.5434412318e-1` | PASS |

All response arrays are finite and the production amplitudes increase strictly with B0.

The machine-readable gate returned:

`pass=true`, `failures=[]`, `status=PASS`.

## Interpretation

MG-S1 admits the four stable nonzero designer-f(R) instances

\[
\boxed{B_0=10^{-6},10^{-5},10^{-4},10^{-3}}
\]

to the C5 production perturbation atlas on the frozen 7x5 grid.

The `1e-7` point is not used as a production sample because its response lies in the transition region close to the pinned solver's GR-return threshold and is not a smooth multi-cell deformation at the precision resolved by this setup.

This is a validated known-model response manifold, not a new law and not evidence for an additional microscopic degree of freedom. Because the family is one-parameter, multiple global SVD modes over the finite B0 scan are interpreted as curvature/compression structure unless a local Jacobian analysis says otherwise.

## Gate decision

**MG-S1 PASS.** C5 is production-ready for the DSIR linear perturbation atlas over the stated common baseline and frozen grid, with `B0>=1e-6`.

The remaining C5 work is cross-family atlas assembly, validity-mask propagation, and later comparison against independent observational channels. The old BZ-like quasistatic toy remains restricted to its audited QS-safe subset and is not used to fill low-k H-EFTCAMB cells.
