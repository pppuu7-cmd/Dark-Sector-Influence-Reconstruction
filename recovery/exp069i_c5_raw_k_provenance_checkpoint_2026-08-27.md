# Recovery checkpoint — post Exp069I

Date: 2026-08-27

Current decisive state:

- C3/GDM provider: certified by Exp070C.
- C5/designer-f(R) provider: certified by Exp069H at q=3.
- Exp069I: `PASS_C5_RAW_K_UNIT_PROVENANCE_AUDIT_V0_1`.
- Historical Exp069F/H raw coordinate field named `raw_k_Mpc^-1` actually contains `k/h`; immutable artifacts stay unchanged.
- Physical target-grid science from Exp069F/H is preserved because target interpolation already used explicit `k_hunit=False`.
- Exp069B remains a permanent scientific FAIL.
- Exp069F remains `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`.

Exact continuation order:

1. Execute the already frozen common physical support-validity mask from `recovery/exp071a_g7_common_physical_support_mask_preregistration_2026-08-27.md` using explicit physical k semantics for both certified providers.
2. If and only if that mask passes, freeze and execute covariance restriction/whitening on that mask.
3. Then nuisance tangent rank/SVD.
4. Then quotient/relation/null control.
5. Only then fresh G8 withheld family.
6. Then G9.

Do not ingest the historical mislabeled raw k field verbatim into the support mask. Do not loosen support predicates using covariance, rank, residual, relation, or held-out information.

G7=OPEN; G8=OPEN; G9=OPEN.
