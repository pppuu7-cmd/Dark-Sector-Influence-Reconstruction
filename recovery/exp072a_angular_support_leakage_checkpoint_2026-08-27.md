# DSIR recovery checkpoint — Exp072A angular support/leakage preregistration

Date: 2026-08-27

Current main before this branch: `f55c69015628ace2c030cdaadd5f61a26e720376`.

## Immutable state

- Exp066B remains permanent hard FAIL; frozen residual/threshold are unchanged.
- Exp067B remains permanent hard FAIL; later precision-aware work does not rewrite it.
- Exp068A remains permanent scientific FAIL.
- Exp068B remains scientific PASS for literal upstream PCA physical forward reproduction only.
- Exp069B remains permanent scientific FAIL.
- Exp069H is the certified C5 q=3 provider.
- Exp069I corrected raw-k provenance without reclassifying prior C5 experiments.
- Exp070A remains permanent scientific FAIL.
- Exp070B localized the C3 target-grid mismatch to interpolation-dominated behavior.
- Exp070C is the certified native-grid C3 provider.
- Exp071A rerun `33027562195` is `PASS_COMMON_PHYSICAL_SUPPORT_MASK_V0_1`; artifact `9629064009`, digest `sha256:4955a3a917992ad38423d9fe2dda3682822c7b86614950467faf5a46a7426675`.
- Exp071A retains 495/495 provider cells: 5 z nodes x 33 k nodes x 3 blocks.
- Exp071A does not authorize covariance restriction directly.

## Active frozen next experiment

`experiments/072a_act_unwise_angular_support_leakage_mask_prereg_v0_1.md`

The file is frozen before any Exp072A leakage fractions are evaluated.

Key locks:

- training families: C3/GDM `cs2={0,1e-6,1e-5}` and C5 designer-f(R) `B0=1e-6`, q=3;
- exact ACT/unWISE upstream/data provenance from Exp068B;
- exactly 26 Exp065B coordinates;
- positive nuisance-envelope survey support weights using absolute released bandwindow/transfer weights;
- nominal invalid-support threshold `<=0.05`;
- nominal retained dimension must be at least 15 and retain at least one gg and kg coordinate in both Blue and Green;
- one-layer support tightening is a frozen robustness diagnostic/control;
- no covariance, nuisance SVD, G7 residual, G8 output, or article-selection quantity may be read.

A PASS only authorizes a separately preregistered covariance-submatrix plus fresh no-repair Cholesky stage. A FAIL blocks this observational G7 route at the current provider support and may not be rescued by threshold retuning.

G7/G8/G9 remain OPEN.
