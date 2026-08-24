# Experiment 033 — hard-evidence discriminant graph v0.1

Date: 2026-08-24
Status: HARD EVIDENCE FROZEN; GRAPH CI REQUESTED

## Goal

Convert the first completed model comparisons into a machine-readable graph of **established** degeneracies and established separator channels. No channel is allowed onto an edge because it merely `could` help.

## Hard-established edges

### E1 — LambdaCDM vs 3 keV WDM in the low-k block

Experiment 030 hard readiness established

\[
|r_T(k=0.1)|\ll10^{-4},
\qquad
|r_T(k=10)|>0.05.
\]

Thus the low-k block is effectively blind to this WDM control, while the small-scale transfer block separates it.

Established separator: `small_scale_transfer`.

### E2 — GDM sound speed vs viscosity in low-k matter/Weyl amplitude

The low-k matter-power response has angle about `0.3226 deg`; the Weyl-amplitude response remains below `0.4 deg`. Thresholds were frozen before the hard rerun. GitHub Actions run `32774501069` passed with `failures=[]`:

\[
\theta_{slip}=137.9432^\circ\;(10^{-7}),
\]

`r_W` angle `0.3007 deg`, and combined equalized channel angle `56.9632 deg`.

Artifact digest: `sha256:4197b9286e53481164f5a842796199ea94ded202d4e62f6cb232186247291d0e`.

Established separator: `metric_slip`.

### E3/E4 — GDM vs designer f(R) in the leading scale-shape projection

Thresholds were frozen before the hard rerun. GitHub Actions run `32774501126` passed with `failures=[]`:

- GDM cs2 vs f(R) scale angle `0.07813 deg`;
- GDM cv2 vs f(R) scale angle `0.10169 deg`;
- time-mode unoriented angles `25.18 deg` and `25.49 deg`;
- full oriented response angles `154.82 deg` and `154.51 deg`.

Artifact digest: `sha256:3d7e86924030ff946da05297174df3bb2db09cf3c0ce534356270177dfa1f7f0`.

Thus the leading scale shape is nearly degenerate, but time evolution / response sign separates the controls.

Established separator: `time_evolution_or_response_sign`.

## Graph rule

The input is `data/derived/comparison_readiness/discriminant_edges_v0_1.json`. Every edge carries a hard-run ID and artifact digest. Candidate or merely plausible separators are forbidden.

`ci/build_discriminant_graph_v0_1.py` uses `src/dsir/discriminants.py` to compute the exact minimum hitting set for this finite established edge catalogue.

## Expected result

Because the three types of established degeneracy require three different proven separators, the current minimum separator set is expected to be

\[
\{\text{small-scale transfer},\;\text{metric slip},\;\text{time/sign evolution}\}.
\]

This is **not** claimed to be a globally minimal observing program for all dark-sector theories. It is only the minimum hitting set for the hard-established edges currently present in DSIR.
