# DSIR recovery checkpoint — after Exp070B

Date: 2026-08-27

Current main before merge: `375cbb6eeb08a1fdafe47b77851a49794613b937`.

## Preserved prior failures

- Exp069B: permanent scientific FAIL for C5 exact designer-GR-limit criterion. No threshold retuning.
- Exp070A: permanent scientific FAIL for C3 target-grid D_m->mPk reconstruction (~4.75%) plus historical aggregate patch-scope issue. No reclassification.

## New hard mechanism result

Exp070B preregistration commit: `e386c0b742067d309a0116b4629b5f85ce3b55fd`.

Execution:
- run `33016744264`
- artifact `9624845938`
- digest `sha256:92d4bf3624c67dd455ce668e5ab14a04b2ab8c275a892f6715a668498c52bef7`
- implementation head `94689db61ce995b4324529443e1dc3ffe102bc80`

Primary label: `INTERPOLATION_DOMINATED`.

Native common-node reconstruction max error: `2.7665156205510028e-14`.

Reproduced Exp070A target-grid interpolation error: `0.04753586663767729`.

Each redshift/case retained 33 native nodes in the frozen low-k support. Source/transfer node matching was machine-level (`<=1.545552650407278e-16` relative).

The ratio `P_native / P_recon(D_m)` has median `1.0000000000000004` in all three C3 cases and coefficient of variation O(1e-14). Therefore there is no nontrivial multiplicative normalization defect on native nodes.

Standard transfer output does not publicly expose the same gauge-invariant `index_tp_delta_m` source. `d_tot` remains a wrong-source control and misses native power by about `3.11e-3` on the native support.

Accessor repeatability is bitwise; native mPk mutation is exactly zero at reported precision.

## Consequence for C3

A separately preregistered corrective provider is now justified, but it must preserve Exp070A FAIL. The corrective bridge should operate from native D_m/source nodes and validate any downstream projection/interpolation at the power or observable level; do not reuse signed-linear-in-log-k amplitude interpolation as an assumed exact operator.

## Parallel C5 path

Exp069C was preregistered before its output and is now opened as PR #78. It is descriptive only: test raw-grid mismatch, same-node zero-limit residual, interpolation amplification, and k-grid convergence for the Exp069B B0=0 defect. Exp069B remains FAIL regardless.

## Mandatory ordering to G7

1. close/record Exp070B mechanism result;
2. preregister and validate corrective C3 physical bridge;
3. execute/record Exp069C and, if justified, preregister a corrective C5 bridge with a hard GR-limit criterion;
4. only after both C3 and C5 providers are certified: preregister common physical support-validity mask;
5. covariance restriction/whitening;
6. nuisance tangent rank/SVD;
7. quotient/relation/null control = G7;
8. fresh G8 withheld family;
9. G9 only after the preceding gates.

G7/G8/G9 are OPEN.
