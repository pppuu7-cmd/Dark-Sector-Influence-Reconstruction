import pytest
from dsir.discriminants import minimal_separating_channel_sets


def test_minimal_hitting_set():
    edges={"A~B":["growth","velocity"],"A~C":["growth","lensing"],"B~C":["small_scale"]}
    assert minimal_separating_channel_sets(edges)==[("growth","small_scale")]


def test_unknown_edge_is_not_silently_imputed():
    with pytest.raises(ValueError):
        minimal_separating_channel_sets({"A~B":[]})
