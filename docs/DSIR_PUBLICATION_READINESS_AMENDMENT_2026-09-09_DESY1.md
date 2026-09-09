# DSIR publication-readiness amendment — DES-Y1 radial correction

Date: 2026-09-09. Scope: DSIR only.

This amendment supersedes only the `DSIR-3 immediate blocker` wording in `docs/DSIR_PUBLICATION_READINESS_2026-09-09.md`. It does not change the frozen publication architecture or categorical scientific gate states.

## Corrected DSIR-3 blocker

The active C2 source/radial authority is DES Y1, not DES Y3.

Recovered/frozen authority now fixes:

1. DES-Y1 Metacalibration source labels `zbin_mcal=0..3`;
2. exact ordinal bridge `S0..S3 -> BIN1..BIN4`;
3. source radial product `y1_redshift_distributions_v1.fits`;
4. Wm identity as DES-Y1 signed galaxy-density x galaxy-shear;
5. five redMaGiC lens bins and lens radial source through `2pt_NG_mcal_1110.fits`;
6. WW identity as DES-Y1 source shear x source shear;
7. historical LOS bookkeeping `k=(ell+1/2)/chi(z)` in physical `Mpc^-1`;
8. historical no-leakage/no-fiducial-P support methodology;
9. exact byte identities for the two compact radial payloads used by the current interface: `y1_redshift_distributions_v1.fits` = 109440 bytes, SHA256 `b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b`; `2pt_NG_mcal_1110.fits` = 6600960 bytes, SHA256 `114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca`;
10. exact normalization/photo-z interface semantics: pinned observation route with `get_nz(dz=0)`, no DSIR-side interpolation/rebinning/effective-coordinate substitution or independent renormalization;
11. exact current 14-slot radial executor interface in `docs/dsir4/contracts/DSIR4_C2_RADIAL_EXECUTOR_INTERFACE_V0_1.md`;
12. exact coordinate/ordinal handoff schema to the later Article-3 physical-support gate;
13. synthetic fail-closed radial-interface QA PASS, run/job `34391645930 / 102601119354`, receipt `docs/dsir4/authority/DSIR4_C2_RADIAL_INTERFACE_SYNTHETIC_QA_PASS_V0_1.md`.

For project tracking only, the decomposed radial-**preparation** task is therefore `13/13 = 100%` complete. This percentage is not a scientific gate status and does not convert `G_RADIAL_SUPPORT=NOT_YET_TESTABLE` into PASS.

## Next Article-3 action

The next admissible step is no longer locator/interface work. It is a separately prospectively preregistered **real** C2 radial execution bound to the admitted Exp073IL ordered join and the exact DES-Y1 radial payloads above. Only that real execution may score the frozen radial criterion and, on an admissible PASS, move the strict Article-3 mandatory-gate closure from `3/9` to `4/9`.

No criterion, threshold, slot order, source bridge, unit convention or leakage boundary may be altered because the synthetic QA passed.

## Publication readiness after current advance

Strict repository science/evidence closure remains:

- DSIR-1: `100%`;
- DSIR-2: `83.3%` pending full G5 data-whitened cross-family stress closure;
- DSIR-3: `33.3%` mandatory final-gate closure (`3/9`), with the current `G_RADIAL_SUPPORT` preparation subtask now `100%` complete and real execution next;
- DSIR-4: `33.3%` project-closure checklist (`2/6`);
- DSIR-5: `0%` final-model publication eligibility (`0/6`) until DSIR-4 establishes a scientific need/gap.

The DES-Y1 correction, exact payload binding, executor-interface freeze and synthetic QA now remove the preparatory radial blocker. Strict Article-3 gate closure can increase only after an admissible real `G_RADIAL_SUPPORT` result.