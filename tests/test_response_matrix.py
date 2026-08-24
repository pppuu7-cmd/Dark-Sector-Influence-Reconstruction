import numpy as np
import pytest

from dsir.response_matrix import (
    common_valid_features,
    connected_components,
    forbid_imputation,
    overlap_graph,
    pairwise_overlap_counts,
    require_overlap_connected,
)


def test_common_subspace_uses_intersection_not_imputation():
    x = np.array([
        [1.0, 2.0, np.nan, 4.0],
        [1.1, 2.1, 3.1, 4.1],
        [0.9, 1.9, np.nan, 3.9],
    ])
    valid = np.isfinite(x)
    sub = common_valid_features(x, valid)
    assert sub.feature_indices.tolist() == [0, 1, 3]
    assert sub.values.shape == (3, 3)
    assert np.all(np.isfinite(sub.values))


def test_pair_subset_can_use_larger_overlap_without_claiming_global_block():
    x = np.array([
        [1.0, np.nan, 3.0],
        [2.0, 2.0, 4.0],
        [np.nan, 3.0, 5.0],
    ])
    valid = np.isfinite(x)
    ab = common_valid_features(x, valid, [0, 1])
    bc = common_valid_features(x, valid, [1, 2])
    all3 = common_valid_features(x, valid)
    assert ab.feature_indices.tolist() == [0, 2]
    assert bc.feature_indices.tolist() == [1, 2]
    assert all3.feature_indices.tolist() == [2]


def test_imputation_is_explicitly_rejected():
    valid = np.array([[True, False], [True, True]])
    bad = np.array([[1.0, 0.0], [1.0, 2.0]])
    with pytest.raises(ValueError, match="imputation"):
        forbid_imputation(bad, valid)
    good = np.array([[1.0, np.nan], [1.0, 2.0]])
    assert forbid_imputation(good, valid)


def test_overlap_connectivity_detects_incomparable_islands():
    valid = np.array([
        [True, True, False, False],
        [True, False, False, False],
        [False, False, True, True],
        [False, False, True, False],
    ])
    counts = pairwise_overlap_counts(valid)
    assert counts[0, 1] == 1
    assert counts[0, 2] == 0
    graph = overlap_graph(valid)
    comps = connected_components(graph)
    assert [c.tolist() for c in comps] == [[0, 1], [2, 3]]
    with pytest.raises(ValueError, match="not overlap-connected"):
        require_overlap_connected(valid)
