# Recovery checkpoint — Exp073H Fourier mm source inventories — 2026-08-27

## Parent

Exp073G is preserved as `FAIL_EXP073G_REPRODUCTION_OR_PROVENANCE`, not a 5%-support scientific FAIL. Exp073H is governed by `experiments/073h_fourier_space_mm_operator_source_binding_prereg_v0_1.md`.

## Official Grieb archive

Run `33036439243` completed successfully. Archive SHA256:

`bbf7433bdb547819e86d16a1bb2d93c725d12aa5bd43058bf17c3e61ad020c0d`

The archive contains six Fourier-wedge measurement tables (NGC/SGC × z1/z2/z3) with k centers `0.0225...0.1975`, best-fit tables and covariance files, but **no window/operator objects**. Covariance numerical contents were not read. Therefore this archive alone is insufficient to establish H1-H3 even though the SDSS results page describes window functions for the analysis.

## Official Beutler fallback

Run `33036540053` completed successfully. Archive SHA256:

`23bb7813a7b6ae0e041f070f40716511ff21243e11f6c2783fec64d72de5b823`

The archive contains 90 objects, including explicit pre-reconstruction `P0/P2/P4(k)` measurements and six non-hidden window files `Beutleretal_window_z{1,2,3}_{NGC,SGC}.dat` plus metadata/figures. Measurement k centers cover approximately `0.0156...0.145 h/Mpc` for P0/P2 and `0.0156...0.0951 h/Mpc` for P4.

This is promising but **not yet `PASS_FOURIER_MM_OPERATOR_SOURCE_BINDING_EXP073H`**. The exact semantic mapping of the window-file columns, their true-k support/mixing, the k units and z-bin identity must be bound before H1-H8 classification. No support fraction has been computed.

## Frozen invariants

- physical rectangle remains `z=[0.295,2.33]`, `k=[0.000704833374744468,0.06664762008318016] Mpc^-1`;
- maximum positive invalid-support fraction remains `0.05`;
- no covariance numerical values, nuisance rank, relation residual or G8 output have been read;
- covariance restriction is still forbidden.

## Next exact action

Audit the Beutler archive documentation/source semantics for `Beutleretal_window_z*_*.dat`: identify columns, coordinate units and how the survey window acts on the true Fourier multipoles. Demonstrate whether this finite released operator admits a non-negative finite true-k support envelope without theory weighting or a post-hoc cutoff. Then classify Exp073H H1-H8. Do not compute common KiDS+BNT support fractions until Exp073H has passed and a separate common-support preregistration exists.

G7 OPEN. G8 OPEN. G9 OPEN.
