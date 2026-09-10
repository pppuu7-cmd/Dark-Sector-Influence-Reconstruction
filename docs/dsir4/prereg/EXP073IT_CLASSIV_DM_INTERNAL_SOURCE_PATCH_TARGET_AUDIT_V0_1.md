# Exp073IT — CLASS-IV internal gauge-invariant d_m patch-target audit v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER Exp073IS showed that the pinned public transfer writer does not expose `d_m`.

## Purpose
Prove a minimal implementation-only repair target for Exp073IR without changing its frozen physical variable. At exact `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`, statically verify that:

1. `index_tp_delta_m` and `index_tp_delta_tot` are distinct source indices.
2. The exact upstream comment identifies `delta_m` as the total matter overdensity, gauge-invariant and defined as in arXiv:1307.1459.
3. When `has_source_delta_m` is true, the source table assignment is exactly `_set_source_(ppt->index_tp_delta_m) = ppw->delta_m;`.
4. The public CLASS transfer writer currently lacks both a `d_m` title and an `index_tp_delta_m` data column while retaining `d_tot/index_tp_delta_tot`; this absence explains Exp073IR INVALID_FOR_SCIENCE and is not a scientific response result.
5. Therefore any later repair must only expose this already-computed `index_tp_delta_m`/`ppw->delta_m` through the transfer interface and enable its source flag for the transfer request. It may not alias `d_tot`, alter `ppw->delta_m`, add a gauge correction, change coupling/cosmology/finite differences/interpolation/domain/thresholds, or inspect Layer-B numerical output.

No cosmological computation is authorized by this audit.

PASS token: `PASS_EXP073IT_CLASSIV_DM_INTERNAL_SOURCE_PATCH_TARGET_AUDIT_V0_1`.
Classification: `SUPPORT_PLUS_0_PLUS_0` only.

Only PASS authorizes a separate prospectively frozen build/static audit of a minimal public-exposure patch before any Exp073IR numerical rerun.