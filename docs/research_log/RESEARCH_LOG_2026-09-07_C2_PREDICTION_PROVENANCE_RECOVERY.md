# DSIR research log — C2 IDE prediction provenance recovery

Date: 2026-09-07

While Exp073FS attempt 2 remained the sole in-progress heavy DSIR process, independent C2 IDE provenance recovery was performed without inspecting partial Exp073FS numerical output.

Validated legacy run/job/artifact `32760042765 / 97536488223 / 9532491954` was re-opened. The artifact was downloaded independently and its ZIP SHA256 `408322a2ee79907dd98cdd0e532daaed1e1aeeb1b633f42ab5321cb32149ab6d` exactly matched the GitHub digest.

Recovered immutable C2 tangent provenance includes reference `(alpha,beta)=(0,0)`, alpha left-sided physical steps and beta central steps at `h={1e-4,1e-3,1e-2}`, frozen base step `1e-4`, baseline `h=0.67` cosmology, exact seven redshift nodes, and the p8 precision preset. The legacy k nodes convert to `[0.00067,0.00201,0.0067,0.0201,0.067] Mpc^-1`; the final node exceeds frozen DSIR `k_max=0.06664762008318016 Mpc^-1` and is not admitted by rounding.

A critical interface distinction was verified from raw legacy logs/artifact: old `r_Delta` was defined as raw `ln(P_model/P_zero_interaction)` from CLASS mPk outputs. Current DSIR-4 requires the separately frozen gauge-aware `Delta_m` response construction, so the old array is not promoted or relabelled. This keeps C2 `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, scientific contribution `+0/+0`.

Detailed immutable record: `docs/dsir4/mappings/C2_IDE_PREDICTION_PROVENANCE_RECOVERY_V0_1.md`, creation commit `1e6f48278cb3398c290df4d08c0d239fab032147`.

Recovery note: `docs/recovery/RECOVERY_2026-09-07_C2_PREDICTION_PROVENANCE_RECOVERED_FS_ATTEMPT2_RUNNING.md`, creation commit `04f780f71be968521ec087c2eecf2daa5ba5cbb5`.

Current-process ledger update commit: `22f52155002457ad9c9a3e8bfab38bded5e7e577`.

Heavy next action remains terminal consumption of Exp073FS attempt 2; C2 independent next action is prospectively freezing a same-solver `Delta_m` extraction/generation implementation and a k-grid wholly inside the frozen common domain, followed by hosted/static provenance audit before any scientific gate.