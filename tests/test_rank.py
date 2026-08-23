import numpy as np
from dsir.rank import effective_rank, variance_rank


def test_exact_rank_one():
    z=np.outer(np.arange(1,8.0),np.arange(1,5.0))
    assert abs(effective_rank(z)-1.0)<1e-10
    assert variance_rank(z,0.999999)==1


def test_zero_matrix():
    z=np.zeros((5,4))
    assert effective_rank(z)==0.0
    assert variance_rank(z,0.99)==0
