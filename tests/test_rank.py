import numpy as np
from dsir.rank import effective_rank,variance_rank,singular_values,whiten_features


def test_exact_rank_one():
    z=np.outer(np.arange(1,8.0),np.arange(1,5.0)); assert abs(effective_rank(z)-1.0)<1e-10; assert variance_rank(z,0.999999)==1

def test_zero_matrix():
    z=np.zeros((5,4)); assert effective_rank(z)==0.0; assert variance_rank(z,0.99)==0

def test_covariance_whitening_is_invariant_to_invertible_feature_transform():
    rng=np.random.default_rng(1234); z=rng.normal(size=(80,12)); scales=10.0**rng.uniform(-1.0,1.0,size=12); q,_=np.linalg.qr(rng.normal(size=(12,12))); A=np.diag(scales)@q
    raw=z@A.T; cov=A@A.T; rew=whiten_features(raw,cov)
    assert np.allclose(singular_values(rew),singular_values(z),rtol=1e-10,atol=1e-10)

def test_whitening_rejects_non_spd_covariance():
    import pytest
    with pytest.raises(ValueError): whiten_features(np.ones((4,2)),np.array([[1.0,2.0],[2.0,1.0]]))
