# DSIR research gates

| Gate | Requirement | Status |
|---|---|---|
| G0 | LambdaCDM embedding reproduces reference observables | PARTIAL — multiple solver-specific LambdaCDM/control limits pass; a broader solver-independent reference suite remains desirable |
| G1 | Bianchi/conservation and gauge-invariant bookkeeping verified | **PASS for v0.1.1 scope** — covariant conservation contract frozen; comoving total-matter construction source-audited; Newtonian/synchronous hard gauge regression passes at `5e-6`; cross-solver response bridge passes at `1e-9` |
| G2 | Response basis and conventions frozen | **PASS v0.1.1** — perturbation coordinate is the same-solver comoving total-matter response `r_Delta`; Experiments 018/020 |
| G3A | Six control classes embedded at background/AP level | PASS/PARTIAL — representatives and exact intersections documented |
| G3B | Control classes embedded beyond background | **PARTIAL, advanced** — LambdaCDM, smooth wCDM, WDM, GDM, IDE and full H-EFTCAMB designer-f(R) now have validated solver/control paths; MG-S0 hard GR limit passes. Remaining work is nonzero multi-z manifold sampling and common atlas assembly |
| G4 | Synthetic low-rank recovery test passes | PASS — corrected global noise-edge criterion recovers injected rank 3 |
| G5 | Rank robust to noise null, feature scaling, covariance coordinates, missing channels, and model sampling | PARTIAL — whitening robustness passes; catalog-prior failure mode is controlled via `R_model(pi)`; validity masks/common-subspace and family-balanced sampling are implemented; broader stress tests remain |
| G6A | First real-data response reconstruction | PASS — DESI DR2 AP calibration quotient and relative expansion reconstruction |
| G6B | First real multi-channel response reconstruction | PASS — corrected DESI DR1 ShapeFit vectors jointly provide geometry, growth, and shape with covariance; Experiment 009 |
| G7 | First nontrivial residual cross-channel relation after quotienting known identities/measurement degeneracies | OPEN — current conditional-innovation aggregate is null-consistent; law search resumes only after production six-family manifold/rank stability |
| G8 | Relation survives withheld prediction | OPEN |
| G9 | Candidate underlying dynamics/action reconstructed or ruled out | OPEN |

## G1 conservation and gauge contract

For internal interactions,

`nabla_mu T_i^{mu nu}=Q_i^nu`, `sum_i Q_i^nu=0`, hence `nabla_mu T_tot^{mu nu}=0`.

Exact Bianchi/conservation identities are quotient directions, not candidate discoveries. At first order, gauge changes act at tensor level as `delta T -> delta T - L_xi Tbar`; raw gauge-specific `delta`, `theta` and metric variables are not common DSIR coordinates without an invariant mapping.

The production matter variable is

`Delta_m = delta_m + 3 (1+w_m) Hconf theta_m/k^2`, with `w_m=p_m/rho_m` and `Hconf=aH`.

For pressureless matter this becomes `Delta_m=delta_m+3 Hconf theta_m/k^2`.

Pinned GDM_CLASS and class_iv source audits confirm the same total-matter concept. GDM_CLASS explicitly retains the `(1+p_m/rho_m)` factor when GDM has pressure.

### Gauge hard regression

Identical CDM cosmology was run in Newtonian and synchronous gauges in pinned GDM_CLASS. At default precision raw `mPk` differed by `~9.84e-5` in the linear core. At p8 precision the raw mismatch fell to `~5.1e-6`; explicit comoving `Delta_m` reconstruction gave `2.5514e-6`.

A threshold `5e-6` was frozen before the final comoving hard rerun; the hard run passed. Production DSIR therefore uses the audited comoving source rather than relying on ambiguous raw transfer variables.

## G2 response basis v0.1.1

Frozen background coordinate:

`r_E(z;z*) = ln[(H(z)/H(z*))/(H_ref(z)/H_ref(z*))]`, `z*=0.51`.

Frozen perturbation coordinate:

`r_Delta(k,z) = ln[P_Delta_model^S(k,z)/P_Delta_ref^S(k,z)]`,

where `P_Delta=P[Delta_m]` and model/reference are generated in the same solver lineage `S` with matched numerical settings whenever possible.

Frozen nodes:

- `z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`;
- `k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

### Cross-solver bridge — Experiment 020

A nontrivial smooth-wCDM deformation (`w0=-0.9`, `wa=0`, `cs2=1`) was computed relative to each solver's own LambdaCDM reference in pinned GDM_CLASS and repaired pinned class_iv. With the same p8 precision preset, calibration gave

`max |Delta r_bridge|=2.3747404043e-10`,

while the physical response was about `5.02e-2`. A hard threshold `1e-9` was frozen before the clean rerun and passed.

## Current G3B numerical sub-gates

- **IDE-S0 PASS:** pinned `kaeonikc/class_iv@ac627d54...`; zero coupling gives CDM + constant vacuum and the synchronous perturbation limit reduces to CDM.
- **IDE-S1 PASS:** hard linear-core tolerance `2e-8` and semantic-background tolerance `2e-12` both passed. The pinned source needs a provenance-tracked compile-only one-brace repair plus legacy compiler/linker semantics; no physics equation is changed.
- **GDM-S0 PASS:** pinned `s-ilic/gdm_class_public@4c87916...`; zero closure gives `rho~a^-3`, pressureless perturbation equations, zero shear and leading CDM IC.
- **GDM-S1 PASS:** p8 hard core regression passed the pre-frozen `5e-6` threshold with actual `1.471014806e-6`; `k<1e-3` remains a separate finite-start diagnostic sector.
- **GDM nonzero manifold CALIBRATION:** first one-axis scan fixes `w=cv2=0` and varies constant `cs2={1e-8,1e-7,1e-6,1e-5,1e-4}` at the validated p8 precision. No manifold/rank claim is made until the scan is inspected.
- **f(R) toy scope restricted (Exp. 019):** historical BZ-like QS control remains diagnostic and is restricted to `{0.01,0.03,0.1} h/Mpc`.
- **MG-S0 PASS (Exp. 021):** official H-EFTCAMB `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`, designer `EFTflag=3`, `DesignerEFTmodel=1`, LambdaCDM background `EFTwDE=0`. Calibration established exact `B0=0` support and the pinned `EFTCAMB_GR_threshold=1e-8`. Before the hard rerun DSIR froze `max_core |r_Delta(B0=0)| <= 2e-6` plus `|B0_found| <= 1e-12` and required stability PASS. The fresh stock-export hard run returned `1.0926960404e-6`, `|B0_found|=2.221e-17`, stability PASS. **MG-S0 is closed.**
- **H-EFTCAMB small-B0 validity rule:** `B0<=1e-8` is not treated as an independent nonzero f(R) atlas point in this pinned implementation because it lies on/inside the solver GR-return threshold. MG-S1 must use explicitly nonzero stable points above that boundary.
- **Missingness/scale rule:** undefined theory/channel cells remain masked, never zero-imputed. Low-k cosmological and WDM small-scale transfer blocks are reported separately unless an overlap-connected analysis is explicitly constructed.

## Hard scientific rule

No discovery claim is permitted before G8 withheld prediction.
