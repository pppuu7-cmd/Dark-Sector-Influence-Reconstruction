# Exp069G — C5 corrective-provider minimum certification contract v0.1

Date: 2026-08-27  
Status: **PROSPECTIVE META-PREREGISTRATION / MINIMUM CONTRACT — NOT AUTHORIZATION TO RUN, NOT A PROVIDER PASS**

## Purpose

Freeze, before the still-running Exp069F general-accuracy result is inspected, the minimum scientific requirements that **any** future C5 designer-f(R) corrective physical-power provider must satisfy before C5 can become eligible for the next G7 stage.

This contract is outcome-independent. It does not predict Exp069F, does not alter Exp069B, and does not authorize the common support-validity mask.

The mandatory DSIR ordering remains

`validated C3 + C5 physical providers -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`.

## Frozen historical facts

1. Exp069B is permanently
   `FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`.
2. Its frozen hard designer-zero versus ordinary-GR target-grid closure scale is
   `max abs(P_designer0/P_GR - 1) <= 5e-6`.
3. Exp069C found a persistent raw same-node zero-limit residual and ruled out matter-power k-grid density as an authorized explanation.
4. Exp069D did not complete a full causal separation because the skip-RGR case is unstable; it cannot certify C5.
5. Exp069E found source-native exact-zero RGR subset amplitude
   `F0 = 4.7401579076280133e-17`, below one float64 epsilon in its frozen normalized coordinates, while the all-block power residual remained
   `M0 = 5.302921926164412e-6`.
   Therefore the observed ppm power floor is not explained directly by a finite EFT-function residue of comparable amplitude.
6. The source-derived analytic boundary note proves that the pinned LCDM designer equations possess an exact `A=0` GR solution, while `EFTB0=0` is routed through generic numerical `B0(A)=0` inversion rather than an exact-zero dispatch.
7. Exp069F is a mechanism audit only. Regardless of its outcome, Exp069F cannot itself certify C5.

These statements are frozen as provenance; no future corrective experiment may rewrite the classification of Exp069B/C/D/E/F.

## Scope of this contract

A future C5 provider may arise from either broad route:

- an unmodified upstream numerical route using a prospectively chosen higher-accuracy setting justified by Exp069F; or
- a separately justified exact-boundary / branch-handling route motivated by pinned-source semantics and further mechanism evidence.

The route may differ, but the minimum certification obligations below do not.

## Minimum acceptance obligations for a future C5 provider

A future separately numbered provider-certification experiment must freeze all implementation choices and parameter points before solver output and must satisfy **all** of the following.

### C1. Independent exact-zero closure

At literal theoretical `B0=0`, compare the candidate C5 provider against an ordinary-GR reference under the same cosmology and physical sampling.

The hard acceptance scale may not be weaker than the already frozen Exp069B scale:

`M0 = max_{z,k,blocks} abs(P_C5(B0=0)/P_GR - 1) <= 5e-6`.

The blocks must include

- `P_mm`,
- signed `P_Wm`,
- `P_WW`.

If solver-native grids are compared directly, their equality requirements must be preregistered. Interpolation may not be used to hide a failing same-node closure.

### C2. Positive-B0 continuity controls

The experiment must include a prospectively frozen sequence of strictly positive `B0` values approaching zero and at least one nontrivial production-scale positive `B0` point.

The purpose is to demonstrate that an exact-boundary treatment, if used, is not merely a discontinuous software special case that destroys the physical positive-B0 branch.

The positive sequence and continuity diagnostics must be frozen before output. No point may be inserted or removed after seeing spectra.

### C3. Nontrivial signal requirement

At the frozen production-scale positive `B0`, the provider must return a finite nonzero physical response relative to GR in at least one preregistered block/node summary.

A provider that achieves zero-limit closure by collapsing all positive-B0 spectra to the GR branch is invalid even if C1 passes.

The exact nontrivial-signal metric and threshold must be preregistered in the concrete provider experiment; this meta-contract does not select them after the fact.

### C4. Signed cross-power semantics

`P_Wm` must preserve its physical sign. No `abs(P_Wm)`, square-root reconstruction that loses sign, or post-hoc sign assignment is allowed.

`P_mm`, signed `P_Wm`, and `P_WW` must come from one explicitly documented solver/provider convention with units, k convention, redshift ordering and variable definitions frozen in provenance.

### C5. Repeatability and state integrity

At minimum, the concrete certification must preregister and verify:

- repeated-accessor or repeated-run numerical repeatability at a justified tolerance;
- no unintended solver-state mutation caused by extracting one block before another;
- exact requested/readback model settings;
- pinned upstream commit before and after execution;
- no upstream source modification unless the corrective route explicitly preregisters a source patch as the object under test.

A source-patched route cannot be described as an unmodified-upstream provider.

### C6. No retrospective floor correction

The provider may not obtain closure by any unpreregistered operation such as

- subtracting the observed B0=0 residual floor;
- renormalizing one spectrum to another;
- fitting a residual correction from the certification outputs;
- smoothing away discrepant cells;
- selecting support cells because they reduce the zero-limit error;
- relaxing the `5e-6` closure criterion after inspection.

A physically motivated transformation is allowed only if frozen prospectively and justified independently of the outputs it will be judged on.

### C7. Distinguish theory boundary from numerical provider

The analytic theorem that `A=0` is an exact GR solution is a theory/implementation fact, not itself a power-provider validation.

If a future route uses an analytic `A=0` boundary or exact-zero dispatch, the experiment must separately show C1-C6 and must test the positive-B0 side. The theorem cannot substitute for those data.

### C8. Preserve failure semantics

Infrastructure/case failures are not scientific FAILs. Conversely, a completed run that violates a frozen scientific criterion remains a scientific FAIL even if the workflow itself is green.

Every future result must carry both execution status and scientific classification explicitly.

## Conditional relation to Exp069F

### If Exp069F reports `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`

The first passing q in the already frozen ladder may be used as a **candidate** accuracy setting in a separately preregistered provider certification. That future experiment must still satisfy C1-C8; the diagnostic Exp069F output cannot be promoted directly to provider PASS.

### If Exp069F reports `GENERAL_ACCURACY_DOES_NOT_RECOVER_FROZEN_GR_LIMIT`

No q from Exp069F is an authorized corrective explanation. The next scientific work remains a mechanism audit of the explicit-EFT early-background/thermal/transfer handoff or another independently justified solver-native route. A future provider may only be certified after a new prospective experiment satisfying C1-C8.

### If Exp069F has infrastructure/case failure

Do not infer the scientific branch. Preserve the infrastructure classification and repair/re-run only under the frozen Exp069F protocol unless a new preregistration explicitly supersedes it for justified reasons.

## G7 authorization boundary

This file does **not** make C5 eligible.

Until a separately numbered C5 physical-provider certification satisfies its own frozen criteria and this minimum contract:

- C3 native physical provider: eligible from Exp070C;
- C5 physical provider: NOT ELIGIBLE;
- common physical support-validity mask: NOT AUTHORIZED;
- covariance restriction/whitening: NOT AUTHORIZED;
- nuisance tangent rank/SVD: NOT AUTHORIZED;
- quotient/relation/null control: NOT AUTHORIZED;
- fresh G8 withheld family: NOT AUTHORIZED;
- G7=OPEN; G8=OPEN; G9=OPEN.

## Integrity statement

This contract was added while Exp069F run 33023027901 was still `in_progress` and before its scientific output was available in `main`. Its purpose is specifically to prevent the eventual Exp069F outcome from weakening the minimum provider-certification burden.