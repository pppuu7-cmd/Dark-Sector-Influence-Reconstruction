# Experiment 050A — thermal-WDM high-k time atlas v0.1

**Status:** calibration / missing-domain completion. No scientific threshold on time dependence is frozen.

## Goal

Replace the current C4 transfer-only fingerprint with a genuine Boltzmann `P(k,z)` atlas on the already frozen WDM high-k domain, without inserting WDM zeros into the low-k common matrix.

## Frozen domains

- masses: `m_WDM={2,3,5} keV` (same control masses as Exp023/024);
- k nodes: `{0.1,0.3,1,3,10,20} h/Mpc`;
- z nodes: `{0.295,0.51,0.706,0.934,1.317,1.491,2.33}`;
- matched reference: baryons + CDM with the same total dark-matter physical density.

## Solver

Official CLASS pinned at

`lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`.

Use `pk_ref.pre` from the same commit for the first high-precision calibration. This includes the high-precision ncdm hierarchy/fluid settings supplied upstream.

## Thermal-relic mapping

Use one Fermi-Dirac ncdm species. For the instantaneous-decoupling normalization `m/omega=94.1 eV` at neutrino temperature,

\[
\frac{T_x}{T_\nu}=\left(\frac{94.1\,{\rm eV}\,\omega_x}{m_x}\right)^{1/3},\qquad
\frac{T_\nu}{T_\gamma}=\left(\frac4{11}\right)^{1/3}.
\]

With `omega_x=0.1200`, freeze:

| m [keV] | T_ncdm/T_gamma | Delta N_eff | N_ur for total 3.046 |
|---:|---:|---:|---:|
| 2 | 0.127097222536539 | 0.001005358988397 | 3.044994641011603 |
| 3 | 0.111029650730162 | 0.000585507981540 | 3.045414492018459 |
| 5 | 0.093646034242863 | 0.000296301934456 | 3.045703698065544 |

Here `Delta N_eff=(T_x/T_nu)^4` for the single FD family. Both `m_ncdm` and `omega_ncdm=0.1200` are supplied; CLASS is allowed to apply its documented PSD normalization so the late-time density is matched exactly.

The CDM reference has `omega_cdm=0.1200`, `N_ncdm=0`, `N_ur=3.046`.

## Response

For each mass,

\[
r_{WDM}(k,z)=\ln\frac{P_{m,\,WDM}(k,z)}{P_{m,\,CDM}(k,z)}.
\]

Compute the same additive/interacting decomposition on this *separate high-k matrix*:

\[
R(z,k)=\mu+T(k)+\tau(z)+I(z,k),\qquad
\chi_I=\frac{\|I\|^2}{\|R\|^2}.
\]

Also report per-k redshift drift and comparison with the legacy Viel-type transfer fingerprint. No agreement threshold with the fitting formula is imposed: the Boltzmann model is not defined by that fit.

## Hard controls

Only bookkeeping/provenance may fail:

- exact pinned upstream SHA;
- explicit seven redshift headers shared by WDM/reference;
- requested k nodes inside every output range;
- finite positive P(k);
- identical k/z response shapes;
- additive reconstruction/orthogonality/profile-normalization algebra at `1e-12`.

No post-hoc threshold is placed on `chi_I`, redshift drift, fitting-form residual, or mass ordering.

## Boundary

This experiment fills C4's missing high-k time domain. It does not make C4 commensurate with low-k C1/C2/C3/C5 by zero padding, is not a Ly-alpha likelihood, is not nonlinear WDM power, and does not by itself establish G7/G8, a universal rank, or a universal model.
