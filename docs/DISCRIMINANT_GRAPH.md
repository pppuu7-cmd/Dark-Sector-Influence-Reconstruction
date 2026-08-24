# DSIR discriminant graph

A node is a frozen model instance or response-manifold patch. A degeneracy edge joins instances indistinguishable within a specified response subset/tolerance. Candidate observable channels label edges only when they **demonstrably** break the degeneracy. Finding the minimum additional set is a minimum hitting-set problem (`src/dsir/discriminants.py`).

Evidence rule: a channel is allowed onto an edge only when separating power is established for the specific frozen representatives and validity domain. `possible`, `depends`, generic physical intuition, or implementation-dependent statements remain unknown.

## Hard-evidence graph v0.1 — 2026-08-24

The machine input is `data/derived/comparison_readiness/discriminant_edges_v0_1.json`; Experiment 033 builds the graph and exact hitting set.

### E1 — C0 LambdaCDM vs C4 thermal WDM, low-k blindness

Hard readiness gate established for the 3 keV control:

- `r_T(k=0.1 h/Mpc) = -3.46e-6`;
- `r_T(k=10 h/Mpc) = -0.10375`.

Therefore the validated low-k block is effectively blind to this WDM control while the small-scale transfer block separates it.

**Established separator:** `small_scale_transfer`.

### E2 — C3 GDM sound speed vs viscosity

In low-k matter power the local ray angle is `0.3226 deg`; in Weyl-amplitude response it remains `0.3007 deg` at the smallest calibrated step. Thresholds were frozen before the fresh metric hard rerun. Run `32774501069` passed with `failures=[]`:

- slip angle `137.9432 deg` at `1e-7`;
- slip angle `138.1452 deg` at `1e-6`;
- equalized Weyl+slip angle `56.9632 deg`.

**Established separator:** `metric_slip`.

### E3/E4 — C3 GDM vs C5 designer f(R), scale-only projection

Thresholds were frozen before the first-comparison hard rerun. Run `32774501126` passed with `failures=[]`:

- GDM cs2 vs f(R) leading scale-mode angle `0.07813 deg`;
- GDM cv2 vs f(R) leading scale-mode angle `0.10169 deg`;
- time-mode unoriented angles `25.18 deg` and `25.49 deg`;
- full oriented ray angles `154.82 deg` and `154.51 deg`.

The scale shape alone is almost degenerate, but time evolution / physical response sign separates the controls.

**Established separator:** `time_evolution_or_response_sign`.

## Current minimum hard-evidence separator set

For the four established edges in v0.1, the expected exact minimum hitting set is

\[
\boxed{
\{\text{small-scale transfer},\;\text{metric slip},\;\text{time/sign evolution}\}
}
\]

with cardinality 3.

This statement is intentionally narrow: it is the minimum for the **current hard-established edge catalogue**, not a globally optimal observing program for every dark-sector theory.

## Relationship to law discovery

Law discovery and the discriminant graph are dual. A proposed universal relation is stronger if it survives a channel chosen specifically for maximal degeneracy-breaking power. Conversely, a relation found only inside a degenerate projection (for example scale-shape alone) must not be promoted to a fundamental law until discriminant channels have been tested.
