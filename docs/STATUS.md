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
| Theory-catalog prior sensitivity | FAILURE MODE IDENTIFIED + control PASS | Exp. 012 + family-balanced atlas sampling; report `R_model(pi)` |
| Missing-response handling | PASS method gate | explicit validity masks/common-subspace rule; no zero/mean imputation |
| DESI DR2 BAO/AP response | PASS G6A | calibration-free AP and relative expansion |
| DESI DR1 corrected ShapeFit response | PASS G6B | geometry-growth-shape covariance from 2026 erratum |
| Conditional innovation quotient | PASS as G7 preparation | aggregate remains null-consistent (`chi2~5.53/5`, `p~0.355`) |
| Interacting-vacuum source/full solver | PASS IDE-S0/S1 | source convention + hard `2e-8` power and `2e-12` semantic-background gates |
| GDM source/full solver | PASS GDM-S0/S1 | source zero closure + p8 hard core actual `1.471e-6` under frozen `5e-6` gate |
| GDM nonzero manifold | CALIBRATION RUNNING | first one-axis scan varies constant `cs2` at `w=cv2=0` with the validated p8 preset |
| GDM ultra-large-scale sector | SEPARATE DIAGNOSTIC | `k<1e-3 h/Mpc` finite-start/IC sensitive; excluded from first common rank block |
| Raw matter gauge audit | FAILURE MODE RESOLVED | default raw mismatch `~9.84e-5`; p8 raw `~5.1e-6`; explicit comoving Delta_m `2.5514e-6`; hard `5e-6` PASS |
| class_iv synchronous vTk header | UPSTREAM DEFECT IDENTIFIED | velocity title block inserts `d_idm_iv` although theta source is absent; species-level vTk excluded from common basis |
| Cross-solver response bridge | **PASS** | matched p8 smooth-wCDM same-solver quotients agree to `2.3747e-10`; frozen hard gate `1e-9` PASS |
| Old BZ-like f(R) control | DIAGNOSTIC ONLY | QS production comparison restricted to `k>=0.01 h/Mpc` |
| H-EFTCAMB designer-f(R) GR limit | **PASS MG-S0** | exact `B0=0` hard rerun: max stock-export `|r_Delta|=1.092696e-6 < 2e-6`; `|B0_found|=2.221e-17 < 1e-12`; theory stability PASS |
| H-EFTCAMB small-B0 boundary | IMPLEMENTATION BOUNDARY IDENTIFIED | pinned solver uses `EFTCAMB_GR_threshold=1e-8`; `B0<=1e-8` is not treated as an independent nonzero atlas point |
| WDM small-scale response | PASS method block | separate linear-transfer block retained; WDM invisibility on `k<=0.1` is not interpreted as absence of physics |
| Common six-family perturbation matrix | PARTIAL G3B | C5 zero-limit is now validated; next blockers are nonzero multi-z f(R), GDM/IDE manifold sampling, and overlap assembly |
| New residual law | OPEN G7 | none claimed |
| Withheld prediction | OPEN G8 | required before discovery |

## Immediate continuation

1. Freeze MG-S0 PASS in gates/recovery and merge the H-EFTCAMB control branch after diff review.
2. Run MG-S1: nonzero stable designer-f(R) values on all frozen `z x k` nodes using same-solver GR quotients.
3. Complete the p8 nonzero GDM `cs2` manifold calibration and add a nonzero IDE interaction manifold.
4. Sample balanced model instances per family with explicit validity masks and separate low-k/small-scale blocks.
5. Assemble the first six-family response atlas, quotient identities/nuisance directions, whiten, and estimate `R_model(pi)` under multiple defensible priors.
6. Resume G7 law search only after rank/manifold stability checks; no discovery claim before G8 withheld prediction.
