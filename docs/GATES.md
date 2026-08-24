# DSIR research gates

| Gate | Requirement | Status |
|---|---|---|
| N0 | Prior-art/non-duplication audit of the complete DSIR architecture | **PASS-PROVISIONAL** — individual ingredients have substantial prior art, but no exact duplicate of the complete `heterogeneous atlas -> solver-controlled response -> whitened/prior-sensitive rank -> identity quotient -> cross-channel law -> withheld prediction` chain was identified in the 2026-08-24 audit. This is not proof of global novelty; see `docs/NOVELTY_AUDIT_N0.md`. |
| N1 | Citation-graph/full-text audit of the closest competitors and adjacent terminology | OPEN — required before manuscript novelty claims. |
| G0 | LambdaCDM embedding reproduces reference observables | PARTIAL — multiple solver-specific LambdaCDM/control limits pass; a broader solver-independent reference suite remains desirable |
| G1 | Bianchi/conservation and gauge-invariant bookkeeping verified | **PASS for v0.1.1 scope** — covariant conservation contract frozen; comoving total-matter construction source-audited; Newtonian/synchronous hard gauge regression passes at `5e-6`; cross-solver response bridge passes at `1e-9` |
| G2 | Response basis and conventions frozen | **PASS v0.1.1** — background rules retained from v0.1; perturbation coordinate upgraded to same-solver comoving total-matter response `r_Delta`; Experiment 018/020 |
| G3A | Six control classes embedded at background/AP level | PASS/PARTIAL — representatives and exact intersections documented |
| G3B | Control classes embedded beyond background | PARTIAL — LambdaCDM, smooth wCDM, thermal WDM, GDM and IDE controls are available; old BZ-like f(R) is now restricted to its QS-safe sub-block and must be replaced by a full linear MG solver before a complete five-k-node production matrix |
| G4 | Synthetic low-rank recovery test passes | PASS — corrected global noise-edge criterion recovers injected rank 3 |
| G5 | Rank robust to noise null, feature scaling, covariance coordinates, and model sampling | PARTIAL — Exp. 011: rank 3 in 30/30 after covariance whitening; Exp. 012: theory-catalog multiplicity prior can hide a real mode, so `R_model` must be reported as `R_model(pi)`; broader stress tests remain |
| G6A | First real-data response reconstruction | PASS — DESI DR2 AP calibration quotient and relative expansion reconstruction |
| G6B | First real multi-channel response reconstruction | PASS — corrected DESI DR1 ShapeFit vectors jointly provide geometry, growth, and shape with covariance; Experiment 009 |
| G7 | First nontrivial residual cross-channel relation after quotienting known identities/measurement degeneracies | OPEN — current conditional-innovation aggregate is null-consistent; law search resumes only after the production six-family matrix is complete |
| G8 | Relation survives withheld prediction | OPEN |
| G9 | Candidate underlying dynamics/action reconstructed or ruled out | OPEN |

## N0 novelty contract

N0 explicitly records that the following are **prior art and cannot be claimed as DSIR inventions**: effective dark-sector stress tensors, dark degeneracy, GDM stress closure, PPF/EFT theory dictionaries, PCA/SVD of cosmological theory banks, entropy effective rank, LambdaCDM-reference/reaction ratios, model-independent interacting-dark-sector reconstruction, symbolic regression in cosmology, and LambdaCDM-as-theory-space/fixed-point organization.

The current **provisional** DSIR-specific combination is narrower:

`heterogeneous DM+DE+interaction+MG response atlas`
` -> same-solver model/reference quotient + cross-solver bridge`
` -> covariance-whitened/noise-calibrated latent dimension`
` -> theory-family-prior profile R_model(pi)`
` -> quotient of exact identities/calibration/measurement-degeneracy directions`
` -> cross-channel relation discovery`
` -> withheld physical-channel prediction`.

N0 must be reopened if a prior work is found implementing substantially this same chain under any terminology. N1 full-text/citation-graph audit remains OPEN, so manuscript-level novelty wording is not yet authorized.

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

A threshold `5e-6` was frozen before the final comoving hard rerun; the hard run passed. Thus the earlier mismatch was a mixture of gauge-sensitive transfer quantities and numerical precision. Raw `mPk` is not categorically forbidden, but production use requires proof that it is constructed from the audited comoving source plus a high-precision validation.

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

A nontrivial smooth-wCDM deformation (`w0=-0.9`, `wa=0`, `cs2=1`) was computed relative to each solver's own LambdaCDM reference in pinned GDM_CLASS and repaired pinned class_iv.

Asymmetric numerical precision produced `max |Delta r_bridge|=1.0475e-5`. After the same p8 precision preset was applied to both lineages, calibration collapsed to

`max |Delta r_bridge|=2.3747404043e-10`,

while the physical response itself was about `5.02e-2`.

A conservative hard threshold `1e-9` was frozen before the clean rerun. The hard regression passed. This validates the **same-solver response quotient** architecture for this overlapping deformation; it does not assert universal `1e-9` agreement for every theory/code.

## Current G3B numerical sub-gates

- **IDE-S0 PASS:** pinned `kaeonikc/class_iv@ac627d54...`; zero coupling gives CDM + constant vacuum and synchronous perturbation limit reduces to CDM.
- **IDE-S1 PASS:** hard linear-core tolerance `2e-8` and semantic-background tolerance `2e-12` both passed. The pinned source needs a provenance-tracked compile-only one-brace repair plus legacy compiler/linker semantics; no physics equation is changed.
- **GDM-S0 PASS:** pinned `s-ilic/gdm_class_public@4c87916...`; zero closure gives `rho~a^-3`, pressureless perturbation equations, zero shear and leading CDM IC.
- **GDM-S1 PASS:** p8 hard core regression passed the pre-frozen `5e-6` threshold with actual `1.471014806e-6`; `k<1e-3` remains a separate finite-start diagnostic sector.
- **f(R) toy scope restricted (Exp. 019):** the BZ-like QS control has minimum `k/(aH/c)` only about `2.9` at `k=0.001` and `8.7` at `0.003`; production QS use is therefore restricted to `{0.01,0.03,0.1} h/Mpc`. A full designer-f(R) solver is the next G3B requirement.

## Hard scientific rule

No discovery claim is permitted before G8 withheld prediction. No broad methodological novelty claim is permitted before N1 citation-graph/full-text audit.