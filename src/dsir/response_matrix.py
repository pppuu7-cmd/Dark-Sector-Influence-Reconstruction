"""Validity-aware response-matrix helpers for DSIR.

A missing/invalid theory response is never silently replaced by zero or by a
column mean. Rank calculations may operate only on explicitly common valid
subspaces unless a separate missing-data method has passed its own gate.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class CommonSubspace:
    values: np.ndarray
    feature_indices: np.ndarray
    model_indices: np.ndarray


def _validate(values, valid):
    x = np.asarray(values, dtype=float)
    m = np.asarray(valid, dtype=bool)
    if x.ndim != 2 or m.shape != x.shape:
        raise ValueError("values and valid must be same-shape 2D arrays")
    if np.any(m & ~np.isfinite(x)):
        raise ValueError("all entries marked valid must be finite")
    return x, m


def common_valid_features(values, valid, model_indices=None):
    """Return features valid for every selected model.

    Rows are model instances and columns are response coordinates/features.
    Invalid entries may be NaN or arbitrary placeholders, but they are never
    used. The returned array contains only the intersection of valid columns.
    """
    x, m = _validate(values, valid)
    if model_indices is None:
        rows = np.arange(x.shape[0], dtype=int)
    else:
        rows = np.asarray(model_indices, dtype=int)
        if rows.ndim != 1 or rows.size == 0:
            raise ValueError("model_indices must be a non-empty 1D index array")
        if np.any(rows < 0) or np.any(rows >= x.shape[0]):
            raise IndexError("model index outside matrix")
    cols = np.flatnonzero(np.all(m[rows], axis=0))
    if cols.size == 0:
        raise ValueError("selected models have no common valid response feature")
    return CommonSubspace(x[np.ix_(rows, cols)].copy(), cols, rows)


def pairwise_overlap_counts(valid):
    """Number of common valid response coordinates for every model pair."""
    m = np.asarray(valid, dtype=bool)
    if m.ndim != 2:
        raise ValueError("valid must be a 2D boolean array")
    return m.astype(np.int64) @ m.astype(np.int64).T


def overlap_graph(valid, min_common=1):
    """Boolean graph linking model pairs sharing at least min_common features."""
    if int(min_common) != min_common or min_common < 1:
        raise ValueError("min_common must be a positive integer")
    counts = pairwise_overlap_counts(valid)
    g = counts >= int(min_common)
    np.fill_diagonal(g, False)
    return g


def connected_components(adjacency):
    """Connected components of a symmetric boolean overlap graph."""
    a = np.asarray(adjacency, dtype=bool)
    if a.ndim != 2 or a.shape[0] != a.shape[1]:
        raise ValueError("adjacency must be square")
    if not np.array_equal(a, a.T):
        raise ValueError("adjacency must be symmetric")
    n = a.shape[0]
    seen = np.zeros(n, dtype=bool)
    comps = []
    for root in range(n):
        if seen[root]:
            continue
        stack = [root]
        seen[root] = True
        comp = []
        while stack:
            i = stack.pop()
            comp.append(i)
            for j in np.flatnonzero(a[i]):
                if not seen[j]:
                    seen[j] = True
                    stack.append(int(j))
        comps.append(np.array(sorted(comp), dtype=int))
    return comps


def require_overlap_connected(valid, min_common=1):
    """Require a single overlap-connected model catalog.

    Connectivity is necessary but not sufficient for a global rank analysis:
    a global SVD still requires a common feature block. This check is mainly a
    diagnostic that identifies catalogs split into incomparable islands.
    """
    g = overlap_graph(valid, min_common=min_common)
    comps = connected_components(g)
    if len(comps) != 1:
        raise ValueError(
            "response catalog is not overlap-connected; components="
            + repr([c.tolist() for c in comps])
        )
    return g


def forbid_imputation(values, valid):
    """Sanity check: invalid cells must be represented by NaN in stored arrays.

    Production DSIR files use NaN + an explicit validity mask. Requiring this
    representation makes accidental zero/mean imputation observable in tests.
    """
    x, m = _validate(values, valid)
    if np.any(np.isfinite(x[~m])):
        raise ValueError("invalid response cells must be NaN; imputation is forbidden")
    return True
