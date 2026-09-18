# DSIR-2 Table T2 — angle hierarchy and nuisance-line diagnostics v0.1

**Date:** 2026-08-28  
**Status:** manuscript source table  
**Classification rule:** preregistered primary classifications remain exactly those of Exp071E/F/H/I/J/K/L. The `line-principal angle` column below is a retrospective geometric diagnostic and does **not** retroactively reclassify any experiment.

## Definition

For an oriented unit response `u` and comparator `v`,

\[
\alpha_{\rm ori}(u,v)=\arccos(u\cdot v).
\]

If the physical nuisance object is the one-dimensional line `span(u)`, its sign-invariant principal angle to `v` is

\[
\alpha_{\rm line}(u,v)=\arccos(|u\cdot v|)=\min(\alpha_{\rm ori},180^\circ-\alpha_{\rm ori}).
\]

The second equality holds for normalized one-dimensional directions. It is descriptive here unless the corresponding experiment prospectively froze a line/subspace test.

## T2A. Core hierarchy

| Experiment / response space | Comparison | Oriented angle [deg] | Retrospective line-principal angle [deg] | Frozen primary interpretation |
|---|---|---:|---:|---|
| Exp071E — equalized `(r_W, Delta_slip)` | K2+ vs GDM `cs2` | 18.9257 | 18.9257 | overlap / FAIL |
| Exp071E — equalized `(r_W, Delta_slip)` | K2+ vs GDM `cv2` | 58.9127 | 58.9127 | separated for this axis |
| Exp071F — equalized `(r_P,r_W,Delta_slip)` | K2+ vs GDM `cs2` | 19.0749 | 19.0749 | overlap / FAIL |
| Exp071F — equalized `(r_P,r_W,Delta_slip)` | K2+ vs GDM `cv2` | 50.1667 | 50.1667 | separated for this axis |
| Exp071H — finite-bin temporal matter response | K2+ vs GDM `cs2` | 138.1006 | **41.8994** | primary oriented PASS; no sign-invariant promotion |
| Exp071H — finite-bin temporal matter response | K2+ vs GDM `cv2` | 137.0973 | **42.9027** | primary oriented PASS; no sign-invariant promotion |
| Exp071I — raw CLASS `t_tot` response | K2+ vs GDM `cs2` | 165.9455 | **14.0545** | primary oriented PASS |
| Exp071I — raw CLASS `t_tot` response | K2+ vs GDM `cv2` | 164.7113 | **15.2887** | primary oriented PASS |
| Exp071J — projected velocity shape | K2+ vs GDM `cs2` | 166.4387 | **13.5613** | robust oriented PASS |
| Exp071J — projected velocity shape | K2+ vs GDM `cv2` | 164.9271 | **15.0729** | robust oriented PASS |
| Exp071L — projected velocity shape | K2- vs GDM `cs2` | 13.5503 | 13.5503 | two-sided nuisance-line FAIL |
| Exp071L — projected velocity shape | K2- vs GDM `cv2` | 15.0709 | 15.0709 | two-sided nuisance-line FAIL |

Frozen separator: `45 deg`.

## T2B. Empirical validation of the line interpretation in velocity space

Exp071L measures

- `angle(K2-,K2+) = 179.9078020829 deg`;
- nonlinear antisymmetry error = `0.0029922493`.

The line-principal angles predicted descriptively from K2+ in Exp071J are

- `13.5613055940 deg` to GDM `cs2`;
- `15.0729032698 deg` to GDM `cv2`.

The fresh K2- experiment gives

- `13.5502602743 deg` to GDM `cs2`;
- `15.0708844313 deg` to GDM `cv2`.

Absolute prediction-to-fresh differences are therefore only

- `0.0110453197 deg` (`cs2`);
- `0.0020188384 deg` (`cv2`).

This does **not** mean that a negative displacement can always be inferred without computation. It shows retrospectively that, for the tested K2 velocity-shape response, the local line picture is an excellent approximation and that the large positive-oriented ~165-degree angles are geometrically compatible with a small sign-invariant line angle.

## T2C. Temporal implication and boundary

For Exp071H, the same retrospective line geometry maps the positive-oriented `138.1006/137.0973 deg` angles to `41.8994/42.9027 deg`, both below the frozen 45-degree separator. This is an important manuscript-level geometric observation, but it is **not** a replacement for the planned fresh K2- temporal experiment. The latter remains necessary to test whether the finite negative K2 displacement follows the same near-antisymmetric response line under the frozen temporal operator.

Therefore the paper should distinguish three statements:

1. **Preregistered Exp071H classification:** the positive-oriented K2 temporal response is separated from both positive GDM directions.
2. **Retrospective line diagnostic:** if K2 is treated as the one-dimensional line spanned by the measured positive response, its principal angles are below 45 degrees.
3. **Still-unresolved finite-displacement test:** a fresh negative-K2 temporal response has not yet prospectively validated that line approximation.

## Exact evidence sources

- `data/derived/exp071e_known_sector_joint_metric_direction_summary_v0_1.json`
- `data/derived/exp071f_known_sector_matter_weyl_slip_direction_summary_v0_1.json`
- `data/derived/exp071h_k2_finite_bin_growth_dual_provenance_summary_v0_1.json`
- `data/derived/exp071i_k2_gdm_total_velocity_direction_summary_v0_1.json`
- `data/derived/exp071j_total_velocity_shape_projection_summary_v0_1.json`
- `data/derived/exp071l_two_sided_k2_velocity_shape_nuisance_summary_v0_1.json`

## Paper-safe takeaway

Large oriented response angles can correspond to small nuisance-line principal angles. The DSIR-2 velocity chain provides a prospective empirical falsification of sign-invariant specificity, while the temporal chain already exhibits the same geometric warning retrospectively and therefore requires a dedicated negative-displacement validation before any stronger claim.