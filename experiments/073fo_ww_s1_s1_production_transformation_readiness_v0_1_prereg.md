# Exp073FO — WW_S1_S1 production transformation readiness v0.1 preregistration

Date: 2026-09-06. Scope: **DSIR only**.

Purpose: hosted-only readiness gate before any Exp073FM self-hosted science. It must verify that the already admitted cross-pair production/checkpoint architecture can be prospectively transformed to the frozen S1S1 same-field semantics without weakening checkpoint, public-BPW, exact-equality, provenance or no-rescue boundaries. It performs no heavy numerical science and creates no WW_S1_S1 authority.

Frozen inputs:

- Exp073FM science prereg file `experiments/073fm_ww_s1_s1_filebacked_full_resolution_ab_science_v0_1_prereg.md`;
- Exp073FL S1S1 driver-generation static prereg file `experiments/073fl_ww_s1_s1_driver_generation_static_audit_v0_1_prereg.md`;
- admitted cross-pair base `ci/exp073fa_ww_s0_s2_durable_ab_production_v0_1.py`;
- hardened complete-chain reference `ci/exp073fg_ww_s0_s3_durable_ab_production_v0_1.py`.

PASS requires all of the following machine-checkable invariants:

1. Exp073FM freezes authoritative `[1,1]`, exactly one S1 reconstruction per replica, exactly one spin-2 field object, same-object `fb=fa` coupling, canonical `<f8 [39,12288]` `EE<-EE`, NSIDE=4096, ell `0..12287`, 39 bands, exact A/B SHA + `numpy.array_equal`, and a separate later provenance admission.
2. Exp073FL freezes equal-but-distinct second-field rejection and no stale S0/S2/S3 or tolerance-rescue semantics for the generated S1S1 driver.
3. The base production code contains the complete six-stage durable checkpoint order, dedicated A/B namespaces, `get_bandpower_windows()`, `read_unbinned_MCM=True`, exact `np.array_equal`, and no `np.allclose`/`np.isclose` rescue.
4. The hardened reference contains complete-stage restore validation and prospective prune-before-compare protections that must be carried into Exp073FM.
5. No self-hosted science is launched by this gate.

PASS token:

`PASS_EXP073FO_WW_S1_S1_PRODUCTION_TRANSFORMATION_READINESS_V0_1`

Classification: `SUPPORT_PLUS_0_PLUS_0`; `ww_s1_s1_authority_created=false`; `self_hosted_science_started=false`.

Any mismatch is fail-closed. A future production driver must be committed and separately audited before a home envelope can launch Exp073FM.