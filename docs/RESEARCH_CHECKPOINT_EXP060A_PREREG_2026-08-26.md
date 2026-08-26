# Research checkpoint — Exp060A preregistration

Date: 2026-08-26

## Starting state

`main` includes Exp059A at `61b3d146186edff36e025ab78f3764d13af660be`.

Exp059A clean source-only run `32942212728` passed for C9 IDM-baryon and produced no matter-power/transfer/perturbation-source/angular-spectrum response. The C9 source grid is frozen as `cross_idm_b={1e-30,1e-29,1e-28,1e-27,1e-26} cm^2`, `n_index_idm_b=0`, `m_idm=1e9 eV`.

Exp058A remains the active preregistered multicoordinate candidate. F29 remains HARD PROSPECTIVE FAIL; F27 remains HARD FAIL; F28 remains retrospective evidence only. G7/G8/G9 remain OPEN.

## Exp060A action

Freeze the complete numerical `(ell,q)` operator using immutable C3/C5/C7/C8 response artifacts only. The implementation uses raw-response `R^2` k-localization as `ell` and centered unit-response PC2 as `q`, with deterministic PC2 sign, training-only positive affine standardization, strict nonzero adjacent motion, non-adjacent segment intersection rejection, and seven leave-one-redshift rebuilds.

Training provenance:

- C3 run `32904158849`;
- C5 run `32907619613`;
- C7 run `32920776596`;
- C8 run `32926084015`.

No C9 response may be generated or inspected in Exp060A.

## Frozen numerical choices

- full grid: 7 redshifts x 5 k nodes;
- `ell=sum_k q_k ln k`, `q_k=sum_z R^2/sum_zk R^2`;
- `q=<unit(R)-mean_train,PC2_train>`;
- PC2 sign: first component with `|v|>1e-12` positive;
- training standardization uses sample SD (`ddof=1`);
- adjacent standardized step norm must exceed `1e-10`;
- segment orientation/on-segment tolerance `1e-10`;
- leave-one-z removes that z from training and future withheld matrices and rebuilds the training-only PC2/standardization.

## Anti-retuning boundary

Once the first C9 `P(k,z)` exists, none of the above choices may be changed for v0.1. C9 points may not be reordered/pruned and failures must be preserved.

## Next executable step

Run the Exp060A training-only workflow. If it passes and remains C9-response clean, merge it. Then preregister a separate C9 response experiment that imports the exact Exp060A implementation unchanged, generates matched reference + five frozen IDM-baryon responses exactly once, and evaluates the full + leave-one-z path verdict.
