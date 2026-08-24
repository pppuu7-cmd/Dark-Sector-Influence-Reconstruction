# Experiment 024 — WDM small-scale response block

Date: 2026-08-24
Status: METHOD/IDENTIFIABILITY CONTROL
Gate relevance: G3B, future discriminant graph and R_model(pi)

## Question

Does the frozen cosmological linear core k<=0.1 h/Mpc contain enough information to represent thermal-WDM deviations, or does WDM require a separate response block?

## Control transfer model

Use the standard thermal-relic fitting form

\[
T_{\rm WDM}(k)=\left[1+(\alpha k)^{2\nu}\right]^{-5/\nu},\qquad \nu=1.12,
\]

with

\[
\alpha=0.049\left(\frac{m_{\rm WDM}}{1\,{\rm keV}}\right)^{-1.11}
\left(\frac{\Omega_{\rm WDM}}{0.25}\right)^{0.11}
\left(\frac{h}{0.7}\right)^{1.22} h^{-1}{\rm Mpc}.
\]

Define a transfer-only log-power fingerprint

\[
r_T(k)=\ln\frac{P_{\rm WDM}}{P_{\rm CDM}}=2\ln T_{\rm WDM}(k).
\]

This is not interpreted as nonlinear z=0 matter power and is not a Ly-alpha likelihood.

The half-mode scale is defined by T^2(k_hm)=1/2, hence

\[
k_{\rm hm}=\alpha^{-1}\left(2^{\nu/10}-1\right)^{1/(2\nu)}.
\]

For the default Omega_WDM=0.25 and h=0.7:

- m=2 keV: k_hm = 14.3221 h/Mpc;
- m=3 keV: k_hm = 22.4629 h/Mpc;
- m=5 keV: k_hm = 39.6021 h/Mpc.

## Numerical visibility check

For m=3 keV:

- r_T(0.1) = -3.895e-6;
- r_T(0.3) = -4.563e-5;
- r_T(1) = -6.768e-4;
- r_T(3) = -7.926e-3;
- r_T(10) = -1.1686e-1;
- r_T(20) = -5.3906e-1.

For m=2 keV:

- r_T(10) = -3.1668e-1;
- r_T(20) = -1.4061.

For m=5 keV:

- r_T(10) = -3.2969e-2;
- r_T(20) = -1.5468e-1.

Thus the existing k<=0.1 cosmological core is almost blind to representative thermal WDM while a high-k transfer block contains an O(0.1-1) signature.

## Decision

Freeze two distinct response domains rather than stretching one matrix across incompatible regimes:

1. cosmological linear core: k={0.001,0.003,0.01,0.03,0.1} h/Mpc;
2. small-scale linear-transfer block: k={0.1,0.3,1,3,10,20} h/Mpc.

The shared k=0.1 anchor checks continuity of bookkeeping. Missing high-k predictions in other families remain NaN+mask and must never be zero-imputed.

## Consequence for rank claims

A low R_model measured only on k<=0.1 cannot be promoted to a statement about the full dark sector. It must be labeled a low-k observable dimensionality. A broader rank requires either a common valid high-k solver block or blockwise/overlap-connected inference with explicit masks.

No discovery claim.
