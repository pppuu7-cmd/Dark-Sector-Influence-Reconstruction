# Experiment 047B — scale-time interaction leave-one-node stability v0.1

**Date:** 2026-08-25  
**Status:** `PASS_INTERACTION_LEAVE_ONE_NODE_OPERATOR_CONTROLS_V0_1`  
**Parent result:** Exp046.  
**Scope:** common C1/C2/C3/C5 frozen low-k structure atlas; C4 remains outside this domain.

## Question

Are

\[
\chi_I=\frac{\|I\|^2}{\|R\|^2}
\]

and

\[
\eta_I(A,B)=\frac{\|d_I\|^2}{\|d\|^2}
\]

robust to the exact choice of the seven frozen redshift nodes and five frozen k nodes, or dominated by one sample point?

This is deterministic internal grid robustness, not independent confirmation.

## Frozen perturbations

Starting from the full `7 x 5` response matrix, exactly 12 reduced grids were generated:

- five leave-one-k-out variants;
- seven leave-one-z-out variants.

No node was selected after looking at target output and no reweighting was introduced. The decomposition

\[
R=\mu+T+\tau+I
\]

was recomputed from scratch on every reduced grid.

## Hard controls

Only algebraic controls could fail:

1. reconstruction relative error `<=1e-12`;
2. normalized core/interaction orthogonality `<=1e-12`;
3. pairwise Pythagorean residual `<=1e-12`;
4. finite outputs/nonzero pair distances.

No scientific drift threshold was frozen.

### Execution provenance

The first workflow attempt failed after all calculations but before scientific output was retained because `numpy.longdouble` was not JSON serializable. The fix changed serialization only; formulas, grids and thresholds were unchanged.

Successful run:

- run `32894616114`;
- source head `9a05c451401ac2cede3a56ef4ca2a1923eecb9c3`;
- artifact ID `9580724793`;
- artifact SHA256 `948038245e4eeea9ca569a48e138f5bdddaede19f0ff98ea941fc91a00272bb7`;
- repo summary `data/derived/comparison_readiness/experiment_047b_interaction_leave_one_node_stability_v0_1.json`.

Controls:

- max reconstruction error `0`;
- max normalized core/I orthogonality `8.3946e-14`;
- max pairwise Pythagorean residual `2.3505e-17`.

All pass the frozen `1e-12` ceilings.

## Direction-level leave-one-node ranges

| Direction | full `chi_I` | min | max | interpretation |
|---|---:|---:|---:|---|
| C1 smooth-w | `1.0805e-3` | `3.9123e-5` | `1.3436e-3` | tier remains weak, but magnitude strongly grid-sensitive |
| C2 IDE alpha | `1.5727e-11` | `1.9927e-13` | `7.3605e-11` | always far below `1e-6` morphology floor |
| C2 IDE beta | `5.4945e-11` | `3.6576e-13` | `7.4540e-11` | always far below floor |
| C3 GDM cs2 | `0.045305` | `0.027945` | `0.052453` | moderate interaction persists |
| C3 GDM cv2 | `0.043634` | `0.026493` | `0.050517` | moderate interaction persists |
| C5 designer f(R) | `0.299856` | `0.223336` | `0.349694` | strong interaction persists |

### Descriptive hierarchy

The ordering

\[
\boxed{\text{IDE near-null} < \text{smooth-w} < \text{GDM} < f(R)}
\]

was preserved in **all 12/12 reduced grids**. Both IDE directions stayed below the pre-existing `chi_I=1e-6` morphology floor in **12/12** grids.

This is a hard descriptive robustness fact for this atlas, but not an independently preregistered classification law.

## Important non-robust detail: smooth-w magnitude

Removing the largest-scale node `k=0.001 h/Mpc` changes smooth-w

\[
\chi_I: 1.0805\times10^{-3}\rightarrow3.9123\times10^{-5},
\]

leaving only `0.0362` of the full-grid value (about a factor `27.6` decrease).

Therefore **the smooth-w tier is robust, but its absolute `chi_I` is not grid-insensitive**. Any future use of the magnitude itself must explicitly test low-k/domain dependence.

For comparison:

- GDM cs2 remains `0.0279-0.0525`;
- GDM cv2 remains `0.0265-0.0505`;
- f(R) remains `0.2233-0.3497`.

These are much less fragile under a single-node deletion than smooth-w.

## Pairwise `eta_I` stability

| Pair | full | leave-one-node range | max abs drift |
|---|---:|---:|---:|
| GDM cs2/cv2 | `0.731139` | `0.652493-0.737735` | `0.078646` |
| GDM cs2/f(R) | `0.611982` | `0.550371-0.653858` | `0.061611` |
| GDM cv2/f(R) | `0.613829` | `0.551973-0.655406` | `0.061856` |
| IDE-alpha/f(R) | `0.571946` | `0.527512-0.694617` | `0.122671` |
| IDE alpha/beta | `1.486e-11` | `1.491e-13-2.728e-11` | `1.471e-11` |

### Strongest useful robustness result

For both GDM/f(R) comparisons, removing any single node leaves

\[
\boxed{\eta_I > 0.55}.
\]

Thus on every leave-one-node grid, **more than half of the normalized GDM/f(R) response-shape separation power remains localized in irreducible scale-time interaction**.

Because no `eta_I>0.5` scientific threshold was preregistered, this is reported descriptively rather than promoted to a formal pass gate.

### GDM pressure/viscosity caveat remains

GDM cs2/cv2 keep `eta_I=0.652-0.738`, but their total response angle remains tiny. A large interaction share of a tiny distance is not detectability. Exp046's conclusion remains unchanged: interaction does not replace metric slip for this microphysical distinction.

## Scientific interpretation

**HARD descriptive robustness:** the mechanism-tier ordering `IDE near-null < smooth-w < GDM < f(R)` is not caused by any one frozen k or z node; it survives all twelve single-node deletions.

**HARD descriptive robustness:** GDM/f(R) interaction localization remains high (`eta_I=0.550-0.655`) under every single-node deletion.

**HARD limitation:** smooth-w's absolute interaction strength is highly sensitive to the lowest-k node. Therefore `chi_I` should currently be treated more safely as a coarse mechanism tier than as a precise family invariant.

**Supported next hypothesis:** GDM and designer f(R) possess genuinely more persistent scale-time coupling than the current IDE directions on this low-k response domain. This still requires parameter-amplitude, solver/domain and observation-kernel validation before broader physical interpretation.

## Claim boundary

This is internal grid robustness of unwhitened theory response. It is not independent-data confirmation, survey distinguishability, a universal mechanism classification, intrinsic dimension, no-hair theorem, residual law or discovery. C4 is missing by domain contract, not zero.
