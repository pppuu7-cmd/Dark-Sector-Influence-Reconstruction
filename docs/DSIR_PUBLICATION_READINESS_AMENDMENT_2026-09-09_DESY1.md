# DSIR publication-readiness amendment — DES-Y1 radial correction

Date: 2026-09-09. Scope: DSIR only.

This amendment supersedes only the `DSIR-3 immediate blocker` wording in `docs/DSIR_PUBLICATION_READINESS_2026-09-09.md`. It does not change the frozen publication architecture or categorical scientific gate states.

## Corrected DSIR-3 blocker

The active C2 source/radial authority is DES Y1, not DES Y3.

Recovered authority now fixes:

1. DES-Y1 Metacalibration source labels `zbin_mcal=0..3`;
2. exact ordinal bridge `S0..S3 -> BIN1..BIN4`;
3. source radial product `y1_redshift_distributions_v1.fits`;
4. Wm identity as DES-Y1 signed galaxy-density x galaxy-shear;
5. five redMaGiC lens bins and lens radial source through `2pt_NG_mcal_1110.fits`;
6. WW identity as DES-Y1 source shear x source shear;
7. historical LOS bookkeeping `k=(ell+1/2)/chi(z)` in physical `Mpc^-1`;
8. historical no-leakage/no-fiducial-P support methodology.

Still required before `G_RADIAL_SUPPORT` becomes executable:

1. immutable bytes/SHA256/schema of the exact DES-Y1 radial payloads consumed by the current C2 route;
2. exact normalization/photo-z-shift convention;
3. current 14-slot radial executor interface;
4. exact coordinate/ordinal handoff schema to the later physical-support gate;
5. synthetic fail-closed radial-interface QA.

For project tracking only, this decomposed radial-prerequisite task is therefore `8/(8+5) = 61.5%` resolved by checklist item count. This percentage is not a scientific gate status and does not partially convert `G_RADIAL_SUPPORT=NOT_YET_TESTABLE` into PASS.

## Publication readiness after correction

Strict repository science/evidence closure remains:

- DSIR-1: `100%`;
- DSIR-2: `83.3%`;
- DSIR-3: `33.3%` mandatory final-gate closure (`3/9`), with the current radial-prerequisite subtask `61.5%` resolved;
- DSIR-4: `33.3%` project-closure checklist (`2/6`);
- DSIR-5: `0%` final-model publication eligibility (`0/6`) until DSIR-4 establishes a scientific need/gap.

The DES-Y1 correction improves confidence and expected completion path for DSIR-3 but cannot increase its strict gate-closure percentage until a prospectively frozen `G_RADIAL_SUPPORT` experiment actually receives an admissible result.
