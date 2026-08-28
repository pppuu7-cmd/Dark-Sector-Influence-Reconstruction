# Exp071J attempt 1 — evaluator root-routing failure

**Date:** 2026-08-28

## Terminal status

Exp071J run `33182476372`, job `98886907771`, did **not** produce a science classification.

The immutable Exp071I parent was correctly identity-bound and downloaded:

- parent run `33181895623`
- artifact `9690064470`
- digest `sha256:ba41e25e6bcdfd2c23c4c9c8bc48bf9ddd85d7776a2e5bb7976e2e061d531e14`

Execution then failed before any projected angle was calculated with:

`ValueError: no tk.dat files for prefix=cs1em7_ under inputs/exp071i/fresh/k2`

## Diagnosis

The Exp071J helper `vecs(root, field)` incorrectly tried to load both K2 (`ref_`, `bar*`) and GDM (`gdm0_`, `cs1em7_`, `cv1em7_`) transfer files from a single root. The immutable Exp071I artifact correctly stores them under separate directories:

- `fresh/k2`
- `fresh/gdm`

This is an evaluator path-routing defect, not a solver, artifact, transfer-definition, projection, threshold, or science failure.

## Consequence

- Exp071J attempt 1: **INVALID_FOR_SCIENCE**
- no projected angle was inspected;
- no threshold or projection rule may be changed;
- original preregistration commit `306c19a4286ffc459fc2886097a8b70fa6df89e9` remains authoritative;
- the 45-degree separator remains frozen;
- the primary projection remains exactly
  `R_shape(z,k) = R(z,k) - mean_k R(z,k)`;
- primary K2 point remains bar1.

## Allowed repair

Patch only the evaluator data routing so that K2 vectors are loaded from `fresh/k2` and GDM vectors from `fresh/gdm`, then rerun against the exact same immutable Exp071I artifact.

No science criterion may be altered.

## Gate state

- G7 OPEN
- G8 OPEN
- G9 OPEN
- no covariance / nuisance scoring authorized
