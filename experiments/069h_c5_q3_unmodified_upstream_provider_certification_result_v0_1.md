# Exp069H — C5 q=3 unmodified-upstream physical-provider certification result v0.1

**Date:** 2026-08-27  
**Execution status:** `COMPLETE_C5_Q3_UNMODIFIED_UPSTREAM_PROVIDER_CERTIFICATION_V0_1`  
**Scientific classification:** `PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1`

## Immutable provenance

- prospective protocol: `experiments/069h_c5_q3_unmodified_upstream_provider_certification_prereg_v0_1.md`;
- implementation merge: `26162b0f2472dc1862eeb60b564a3563eaae12f9`;
- workflow run: `33024638764`;
- artifact: `9628053962`;
- artifact digest: `sha256:fa61b504d31edeba2afcbed0f4b14bda688df82a96d2cba55eac034682b5382f`;
- pinned upstream: `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

The full immutable artifact contains the summary, all seven fresh case JSON/log pairs and the matched baseline configuration. Repository key metrics are mirrored in
`data/derived/g7/exp069h_c5_q3_unmodified_upstream_provider_certification_v0_1_key_metrics.json`.

## Frozen C1 — exact-zero closure

At literal designer `B0=0` versus a fresh ordinary-GR reference under frozen q=3 accuracy:

- target-grid maximum: `M0 = 1.7011186858522977e-6`;
- same-node raw maximum: `R0 = 2.8421302380756537e-6`;
- frozen hard limit for each: `5e-6`.

**C1 PASS.**

## Frozen C2 — positive-B0 continuity

For every pre-frozen tiny-positive point relative to the fresh `B0=0` branch:

| B0 | target maximum | raw same-node maximum |
|---:|---:|---:|
| `1e-12` | `0.0` | `0.0` |
| `1e-10` | `0.0` | `0.0` |
| `1e-8` | `0.0` | `0.0` |

Frozen limit: `5e-6` for target and raw.

**C2 PASS.**

The exact zeros are numerical equality in the returned arrays at these tested points; they are not promoted to a statement that the physical modified-gravity response is mathematically identical to GR for every arbitrarily small positive `B0`.

## Frozen C3 — nontrivial production signal

At the pre-frozen production point `B0=1e-6`:

`S_prod(target) = 0.013249122882007408`.

Frozen minimum: `1e-3`.

The descriptive raw same-node maximum relative to GR is `0.027566146352511606`.

**C3 PASS.** The provider does not obtain zero-limit closure by collapsing the positive branch to GR.

## Frozen C4 — signed cross-power and accessor semantics

**C4 PASS.** The workflow preserved direct signed `P_Wm`; no absolute value or auto-power reconstruction was used. In the immutable case payloads, every one of the 35 frozen target cells has negative `P_Wm` for each of the fresh GR/designer/repeat cases, with zero positive or zero cells. Forward and reverse accessor traversal passed exact array repeatability.

This sign statement is a provider/convention result, not evidence for dark-sector physics.

## Frozen C5 — repeatability/state integrity

Independent fresh `B0=0` rerun:

- `D_repeat_target = 0.0`;
- `D_repeat_raw = 0.0`;
- frozen limit: `1e-12`.

All case processes and analyses completed, all q=3 accuracy and designer settings read back correctly, pinned upstream SHA was unchanged, and repeated accessors passed.

**C5 PASS.**

## Frozen C6/C7

- no floor subtraction, renormalization, smoothing, source patch or post-hoc criterion movement was used;
- literal public `EFTB0=0` provider branch was used rather than replacing it with the analytic `A=0` theorem.

**C6 PASS. C7 PASS.**

## Overall provider consequence

All hard C1–C7 checks pass, satisfying the previously frozen Exp069G minimum-provider contract. Therefore the q=3 unmodified-upstream route is a **certified C5 physical provider** for the tested contract.

This does not rewrite prior experiments:

- Exp069B remains permanent `FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`;
- Exp069F remains `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT` mechanism evidence;
- Exp069H is the separate prospective provider certification.

Together with the already certified Exp070C C3 provider, the scientific prerequisite `validated C3 + certified C5` is now satisfied.

## Post-run raw-k provenance defect discovered before support-mask construction

A repository/source audit after Exp069H classification found a schema-level unit issue in the stored raw-grid key.

Exp069H calls

`get_linear_matter_power_spectrum(..., hubble_units=False, nonlinear=False)`

without explicitly setting `k_hunit`. In the pinned upstream source, `get_linear_matter_power_spectrum` defaults to `k_hunit=True`; the underlying spectrum accessor then returns

`kh = ks / (H0/100)`

when that flag is true. Therefore the values stored under the Exp069H field name

`raw_k_Mpc^-1`

are not yet authorized to be interpreted as physical `1/Mpc` coordinates. The field name is misleading and must not be propagated into the common support mask.

This does **not** retroactively change the Exp069H PASS on current evidence:

1. the primary target-grid path explicitly used `get_matter_power_interpolator(..., k_hunit=False)` and the frozen target nodes are physical `1/Mpc`;
2. the raw closure checks are dimensionless GR/designer ratios on exactly identical raw nodes, so a common k-axis unit relabeling does not by itself alter those residuals;
3. no support mask has yet been applied from the mislabeled raw field.

However, because physical support selection depends on correctly bound k units, the next step is **not** yet the common support mask. A separate prospective Exp069I raw-k unit/provenance audit must pass first.

## Gate boundary

After Exp069H:

- C3 physical provider: `CERTIFIED`;
- C5 physical provider: `CERTIFIED`;
- common physical support mask: `NOT YET APPLIED`;
- support-mask construction: temporarily blocked by Exp069I unit/provenance audit;
- G7: `OPEN`;
- G8: `OPEN`;
- G9: `OPEN`.

No observational residual law or new-physics claim is authorized by this provider PASS.
