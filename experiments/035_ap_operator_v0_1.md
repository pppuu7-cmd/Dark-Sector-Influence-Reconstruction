# Experiment 035 — calibration-free AP operator v0.1

**Date:** 2026-08-24  
**Status before hard run:** operator and thresholds frozen; family background insertion is a later step.

## Goal

Map the frozen DSIR expansion-history response into the directly observable Alcock-Paczynski geometry channel without reintroducing an absolute Hubble calibration.

For flat FLRW,

\[
F_{AP}(z)=\frac{D_M}{D_H}=E(z)\int_0^z\frac{dz'}{E(z')}.
\]

Let

\[
E_{model}(z)=A E_{ref}(z)e^{r_E(z)},
\]

where `A` is an arbitrary constant calibration and `r_E` may be anchored at `z*=0.51`. Then

\[
\frac{F_{AP,model}}{F_{AP,ref}}=
 e^{r_E(z)}
 \frac{\int_0^z e^{-r_E(z')}dz'/E_{ref}(z')}
 {\int_0^z dz'/E_{ref}(z')}.
\]

Thus `A` cancels exactly. The ShapeFit geometry coordinate obeys

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}.
\]

At first order,

\[
\Delta\ln F_{AP}(z)=r_E(z)-
\frac{\int_0^z r_E(z')dz'/E_{ref}(z')}{\int_0^z dz'/E_{ref}(z')}+O(r_E^2).
\]

## Frozen hard controls

Before the first hard run:

1. Direct wCDM calculation and operator prediction must agree in `ln F_AP` to `<1e-11`.
2. Adding a constant `+0.731` to the entire log-E response must change the AP response by `<1e-12`.
3. `ln(D_H/D_M)` response must equal minus the `ln F_AP` response to `<1e-14`.
4. When a small response amplitude is halved, the exact-minus-linear remainder must decrease approximately quadratically; the error ratio must be `<0.27`.
5. No family-separation threshold is defined in this method experiment.

## Important data requirement

The AP operator contains an integral from `z=0` to the measurement redshift. Therefore a family background response history must cover `z=0` through the target bins; the current frozen seven-node structure atlas beginning at `z=0.295` is not by itself sufficient for this geometry integral.

Experiment 035 only validates the observation operator. The next step is to provide validated background histories for the nonzero geometry directions (especially C1 and C2), while preserving exact-zero/background-equivalent controls separately.

## Claim boundary

A PASS is only `PASS_CALIBRATION_FREE_AP_OPERATOR_V0_1`. It does not close G5, does not establish family distinguishability, and does not reopen G7.
