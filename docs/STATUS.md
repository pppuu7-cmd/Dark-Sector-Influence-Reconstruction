# DSIR status snapshot — 2026-08-24

DSIR remains a reconstruction/meta-inference framework, not a fundamental theory.

| Item | Status | Evidence |
|---|---|---|
| Project separation from RTK | PASS | dedicated DSIR repository; RTK excluded from this research line |
| Recovery/manual backup | PASS and live | `docs/RECOVERY_MANUAL.md` + `docs/RECOVERY_LATEST.md` + gates/log/provenance |
| Conservation/gauge contract | **PASS for v0.1.1 scope (G1)** | source-level Bianchi/exchange bookkeeping + hard Newtonian/synchronous comoving-matter regression |
| Response basis v0.1.1 | **PASS G2** | `P_Delta`/`r_Delta` same-solver quotient; Experiments 018/020; cross-solver hard bridge `1e-9` PASS |
| Synthetic latent-rank recovery | PASS | injected rank 3 recovered with corrected global noise edge |
| Rank coordinate/covariance robustness | PASS on tested suite; G5 PARTIAL | Exp. 011: 30/30 after whitening; naive raw ranks 20–35 |
| Theory-catalog prior sensitivity | FAILURE MODE IDENTIFIED + control PASS | Exp. 012: multiplicity prior can hide a real mode; report `R_model(pi)` |
| DESI DR2 BAO/AP response | PASS G6A | calibration-free AP and relative expansion |
| DESI DR1 corrected ShapeFit response | PASS G6B | geometry-growth-shape covariance from 2026 erratum |
| Conditional innovation quotient | PASS as G7 preparation | aggregate remains null-consistent (`chi2~5.53/5`, `p~0.355`) |
| Interacting-vacuum source/full solver | PASS IDE-S0/S1 | source convention + hard `2e-8` power and `2e-12` semantic-background gates |
| GDM source/full solver | PASS GDM-S0/S1 | source zero closure + p8 hard core actual `1.471e-6` under frozen `5e-6` gate |
| GDM ultra-large-scale sector | SEPARATE DIAGNOSTIC | `k<1e-3 h/Mpc` finite-start/IC sensitive; retained but excluded from first common rank block |
| Raw matter gauge audit | FAILURE MODE RESOLVED | default raw mismatch `~9.84e-5`; p8 raw `~5.1e-6`; explicit comoving Delta_m `2.5514e-6`; hard `5e-6` PASS |
| class_iv synchronous vTk header | UPSTREAM DEFECT IDENTIFIED | velocity title block inserts `d_idm_iv` although theta source is absent; species-level vTk excluded from common basis |
| Cross-solver response bridge | **PASS** | matched p8 smooth-wCDM same-solver quotients agree to `2.3747e-10`; frozen hard gate `1e-9` PASS |
| Old BZ-like f(R) control | DIAGNOSTIC ONLY at low k | Exp. 019 restricts QS production use to `k>=0.01 h/Mpc`; full MG solver required for five-node matrix |
| Full designer-f(R) solver | NEXT G3B FRONT | H-EFTCAMB `eftcamb` branch selected for clean-room GR/designer-limit audit |
| Common six-family perturbation matrix | PARTIAL G3B | common response coordinate is now ready; full MG member remains the main blocker |
| New residual law | OPEN G7 | none claimed |
| Withheld prediction | OPEN G8 | required before discovery |

## Immediate continuation

1. Merge response-basis v0.1.1 only after unit tests/diff review.
2. Pin and clean-build H-EFTCAMB `eftcamb` branch.
3. Establish GR/designer-f(R) zero/small-`B0` limit before choosing a nonzero MG control.
4. Generate full-solver `r_Delta(k,z)` on all frozen nodes.
5. Compare full f(R) against the historical BZ-like toy only on its QS-safe `{0.01,0.03,0.1}` sub-block.
6. Assemble first common six-family matrix, whiten, and estimate `R_model(pi)`.
7. Resume G7 law search only after matrix stability checks.
