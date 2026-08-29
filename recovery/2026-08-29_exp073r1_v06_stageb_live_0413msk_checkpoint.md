# DSIR recovery checkpoint — Exp073R1 v0.6 canonical Stage-B live

Date: 2026-08-29 (Europe/Moscow)
Repository: `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`
Branch: `main`

## Authoritative live run

- Workflow: `Exp073R1 DESY1 self-hosted long-run Stage-B v0.6`
- Run: https://github.com/pppuu7-cmd/Dark-Sector-Influence-Reconstruction/actions/runs/33222848695
- Status at checkpoint: `in_progress`
- Job: `metacal-map-longrun` (`99020389131`)

Completed successfully before the active mapper step:

1. job setup;
2. checkout;
3. preregistered unchanged evaluator + execution firewall assertion;
4. immutable Stage-A and Exp073R0 Actions metadata binding before download;
5. isolated/frozen mapper runtime installation on the long-lived runner;
6. both required artifact downloads;
7. downloaded Stage-A and Exp073R0 internal-contract re-binding.

Active step at checkpoint:

- `Sequentially stream authoritative 84GB metacal object and execute unchanged frozen mapper` — `in_progress`.

Still pending:

- `Assert genuine Exp073R1 reproduction PASS with no downstream science leakage`;
- authoritative result artifact upload.

## Scientific / infrastructure classification

This state is **reproduction INCOMPLETE**. It is **not a scientific FAIL** and it is not yet a scientific PASS. No downstream G7 quantity is authorized from this live state.

No duplicate heavy run was launched in this iteration. The canonical self-hosted Stage-B run remains the sole authoritative heavy execution path.

## Frozen G7 order

The order remains unchanged and must not be bypassed:

1. validated physical forward / power-input bridges;
2. genuine Exp073R1 reproduction PASS;
3. preregistered physical support-validity mask (Exp073P real route);
4. covariance restriction / whitening;
5. nuisance tangent rank / SVD;
6. quotient / relation / null control;
7. only then a fresh G8 withheld family.

Until the genuine Exp073R1 PASS assertion succeeds, do not compute or interpret real support-mask fractions, restricted covariance, whitening, nuisance rank/SVD, quotient/null statistics, or fresh G8 results.

## Next autonomous action

On the next iteration, first inspect run `33222848695`. If it has completed, classify the terminal outcome from the frozen evaluator and artifacts before any downstream action. If it is still active, do not launch a competing heavy mapper; use only independent low-cost integrity/reproducibility work that cannot leak downstream science.
