# C8 mechanism selection rationale — IDM–photon — 2026-08-26

## Decision

Use pinned CLASS interacting dark matter–photon scattering (`idm_g`) as C8 for the next **mechanism-level prospective** test of the F28 endpoint-normalized transition coordinate.

Do not use IDM–baryon as C8; reserve it as a possible later stress test.

## Why IDM–photon is preferable for the first clean follow-up

Pinned CLASS gives a transparent source-native IDM drag:

\[
\Gamma_{idm\leftarrow\gamma}=S_{idm\gamma}\,d\mu_{idm\gamma},
\qquad
S_{idm\gamma}=\frac43\frac{\rho_\gamma}{\rho_{idm}}.
\]

For fixed `n_index_idm_g`, `dmu_idm_g` is exactly linear in `u_idm_g`. Therefore a desired source scale can be selected from background/thermodynamic quantities without looking at any perturbation response.

In contrast, the IDM–baryon rate `R_idm_b` depends explicitly on baryon and IDM temperatures and on the rms relative-velocity prescription. That is scientifically useful for a later hard stress test but less clean for the first attempt to separate operator validity from source-selector ambiguity.

## Why C8 is not just C7 repeated

C7 IDM–DR couples IDM to a hidden relativistic component. C8 IDM–photon couples IDM to the visible photon bath. In pinned CLASS the latter:

- adds `dmu_idm_g` to the photon scattering rate/shear treatment;
- adds `-S_idm_g dmu_idm_g (theta_idm-theta_g)` to the IDM Euler equation;
- has no extra IDR background component;
- uses the photon-to-IDM density ratio in its drag conversion.

Thus C8 is a genuinely new interaction **mechanism/channel** relative to C7.

## Independence boundary

C7 and C8 nevertheless share the multi-interacting-DM implementation scaffold in CLASS. Therefore:

- a C8 prospective PASS would be meaningful fresh mechanism-level evidence for F28;
- it should **not by itself** be described as maximally independent cross-family confirmation;
- strong G8 wording should remain conservative until a later fresh mechanism from a more structurally distinct family also survives, or until the repository gate definition explicitly justifies mechanism-level closure.

This boundary is fixed before any C8 matter-power response.

## External implementation provenance

The public multi-interacting-DM CLASS implementation is described by Becker, Hooper, Kahlhoefer, Lesgourgues & Schöneberg (2021), arXiv:2010.04074. That work treats DM interactions with photons, baryons and dark radiation as distinct channels and reports their cosmological effects as largely additive. This supports using IDM–photon as a physically distinct channel, while the shared-code caveat above is retained.
