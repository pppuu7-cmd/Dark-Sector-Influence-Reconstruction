# DSIR recovery — C2 prediction provenance recovered; Exp073FS attempt 2 still running

Date: 2026-09-07. Scope: DSIR only.

## Heavy process authority

Exp073FS run `34067352681`, attempt `2`, head `f3e49041a5b869ddf22be8ca7a612901ec9f9458` remains the only in-progress DSIR heavy workflow.

- hosted launch audit job `101592593435`: SUCCESS, support `+0/+0`;
- home job `101592579318`: IN_PROGRESS;
- active step: `Run frozen WW_S1_S2 A/B gate with durable checkpoints`;
- runner: `DSIR-HOME-PC-2`, runner id `22`;
- evidence collection/upload remain pending;
- no partial numerical result/checkpoint inspected;
- no competing home job launched.

Attempt 1 remains historical `INFRASTRUCTURE_RUNNER_ORCHESTRATION_FAIL_PLUS_0_PLUS_0`; no science authority came from it.

## Independent C2 IDE provenance recovery

Created `docs/dsir4/mappings/C2_IDE_PREDICTION_PROVENANCE_RECOVERY_V0_1.md` in commit `1e6f48278cb3398c290df4d08c0d239fab032147`.

Recovered from validated legacy run `32760042765`, job `97536488223`, artifact `9532491954`:

- independent ZIP SHA256 exactly matches GitHub digest: `408322a2ee79907dd98cdd0e532daaed1e1aeeb1b633f42ab5321cb32149ab6d`;
- pinned solver `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- reference `(alpha,beta)=(0,0)`;
- alpha physical left-sided steps `h={1e-4,1e-3,1e-2}`, base step `1e-4`;
- beta central steps `+/-h`, `h={1e-4,1e-3,1e-2}`, base step `1e-4`;
- exact baseline cosmology, redshift nodes, and p8 precision preset recovered;
- legacy k nodes `[0.001,0.003,0.01,0.03,0.1] h/Mpc` convert at frozen `h=0.67` to `[0.00067,0.00201,0.0067,0.0201,0.067] Mpc^-1`; final `0.067` is outside the frozen DSIR maximum `0.06664762008318016 Mpc^-1` and is not rounded/rescued.

Critical interface finding: legacy `r_Delta` was explicitly `ln(P_model/P_zero_interaction)` from raw CLASS `mPk`; it is not relabelled as the newly required common `Delta_m = delta_m + 3(1+w_m)Hconf theta_m/k^2` response. C2 therefore remains `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, `+0/+0`.

## Exact next actions

Priority 1: terminal-consume Exp073FS attempt 2 when it finishes; verify raw logs/artifact, checkpoint restore/new provenance, ordered S1->S2 distinct-field semantics, frozen identities, exact file-backed proof, finiteness and exact A/B equality. Only valid candidate PASS permits Exp073FT admission.

Independent C2 next step while FS runs: prospectively freeze a same-solver `Delta_m` extraction/generation implementation and an output k-grid strictly inside the current DSIR domain, then static-audit it before any scientific gate. No legacy raw-mPk relabelling and no rounding of the `0.067 Mpc^-1` legacy node are permitted.