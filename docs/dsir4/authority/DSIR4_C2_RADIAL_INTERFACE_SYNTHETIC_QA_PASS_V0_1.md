# DSIR-4 C2 radial interface synthetic QA — PASS v0.1

Date: 2026-09-09. Scope: DSIR only.

Status: IMPLEMENTATION QA PASS / NON-SCIENTIFIC.

This receipt records completion of the synthetic fail-closed prerequisite for the prospectively frozen radial executor interface. It does **not** score `G_RADIAL_SUPPORT`, does not authorize covariance/nuisance/relation access, and does not create scientific model authority.

## Bound interface

- contract: `docs/dsir4/contracts/DSIR4_C2_RADIAL_EXECUTOR_INTERFACE_V0_1.md`;
- interface blob at PASS-time lineage: `26c8e9c9622f6dc727edcb61844e0cd21088aaa7`;
- self-test: `ci/dsir4_c2_radial_interface_selftest_v0_1.py`;
- self-test blob: `8fe71f765954ff05cfb67cbe4208367dabd5da4f`;
- workflow: `.github/workflows/dsir4-c2-radial-interface-selftest-v0-1.yml`;
- workflow blob: `fce82dbec32fcb754e10e93648764694ed209c4b`.

## GitHub Actions receipt

- head SHA: `f2fbbd433e78ca0c36140c058a065e8cebb2d64b`;
- workflow run: `34391645930`;
- job: `102601119354`;
- runner: GitHub Actions `ubuntu-latest`;
- run conclusion: `success`;
- job conclusion: `success`;
- `Run fail-closed radial interface QA`: `success`;
- `Assert exact PASS token`: `success`;
- exact expected token: `PASS_DSIR4_C2_RADIAL_INTERFACE_SYNTHETIC_QA_V0_1`.

## Tested fail-closed properties

The synthetic QA covers the prospectively frozen requirements for:

1. exact 14-slot ordering and permutation rejection;
2. exact source bridge `zbin_mcal 0..3 -> BIN1..BIN4`;
3. compact DES-Y1 radial payload SHA mismatch rejection;
4. `photoz_shift_dz=0` enforcement;
5. `Mpc^-1` unit enforcement and `h/Mpc` rejection;
6. non-finite/zero radial normalization rejection;
7. duplicate coordinate-ID/ordinal rejection;
8. canonical output ordering and input-permutation invariant digest;
9. forbidden interpolation/effective-coordinate metadata rejection;
10. covariance/whitening/nuisance/relation/G7/G8/article-selection leakage rejection.

## Project implication

The decomposed **preparation** checklist for the current C2 `G_RADIAL_SUPPORT` route is now complete: `13/13 = 100%`.

This is preparation readiness only. The scientific gate remains:

- `G_RADIAL_SUPPORT=NOT_YET_TESTABLE` until a separate prospectively preregistered **real** radial execution consumes the admitted ordered-join authority and exact DES-Y1 radial payloads and produces a classifiable real result.

The next admissible action is therefore namespace verification followed by a real radial-execution preregistration. No scientific criterion may be changed as a consequence of this synthetic PASS.