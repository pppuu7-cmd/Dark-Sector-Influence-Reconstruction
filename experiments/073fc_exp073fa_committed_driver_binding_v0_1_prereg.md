# Exp073FC — Exp073FA committed-driver binding audit v0.1

Date: 2026-09-06. DSIR only.

Purpose: fail-closed bind the repository-resident Exp073FA S0_S2 durable drivers to the exact generated implementation evidence that passed repaired Exp073FB before any self-hosted science envelope is allowed.

Frozen upstream:
- Exp073FA science prereg blob `edc044792be8ac7b796c8469943924942ae91932`;
- Exp073FB repaired run/job `34018241319 / 101445845648` = SUCCESS;
- Exp073FB artifact `9984600349`, name `exp073fb-exp073fa-s0-s2-generated-drivers-v0-1`;
- GitHub digest and independently downloaded ZIP SHA256 `b371821a77cb4a62051ceee45f82764a5486ea3b0bcf0939a9bcac0eff624cda`;
- generated base-driver SHA256 `fe354b95e9aeefe0772f4c7eecbba6e1944fb1f4955fceb3e9e72ed1c06b293a`;
- generated file-backed wrapper SHA256 `77f321e22c923d8d5996105487cae9afb6eecc5863174d849b092164a26824ba`;
- Exp073FB raw token `PASS_EXP073FB_EXP073FA_S0_S2_DRIVER_TRANSFORMATION_STATIC_AUDIT_V0_1`.

The audit must independently re-download artifact `9984600349`, recompute ZIP SHA256, verify the transformation receipt, and require repository files `ci/exp073fa_ww_s0_s2_durable_ab_production_v0_1.py` and `..._v0_2.py` to be byte-for-byte SHA256-identical to the generated source files in that artifact. It must compile both repository files and repeat the critical frozen semantic assertions for `(S0,S2)`, namespaces, shapes, exact equality, public file-backed BPW route and no tolerance rescue.

No numerical science is run. PASS token: `PASS_EXP073FC_EXP073FA_COMMITTED_DRIVER_BINDING_V0_1`. Classification support/governance `+0/+0`; `ww_s0_s2_authority_created=false`. Only after PASS may a dedicated home execution envelope be frozen and audited.