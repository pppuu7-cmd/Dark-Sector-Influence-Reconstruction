import numpy as np
from dsir.rank import effective_rank,variance_rank,singular_values,whiten_features,noise_edge_rank,weighted_noise_edge_rank

def test_exact_rank_one():
    z=np.outer(np.arange(1,8.0),np.arange(1,5.0)); assert abs(effective_rank(z)-1.0)<1e-10; assert variance_rank(z,0.999999)==1

def test_zero_matrix():
    z=np.zeros((5,4)); assert effective_rank(z)==0.0; assert variance_rank(z,0.99)==0

def test_covariance_whitening_is_invariant_to_invertible_feature_transform():
    rng=np.random.default_rng(1234); z=rng.normal(size=(80,12)); scales=10.0**rng.uniform(-1,1,size=12); q,_=np.linalg.qr(rng.normal(size=(12,12))); A=np.diag(scales)@q; rew=whiten_features(z@A.T,A@A.T)
    assert np.allclose(singular_values(rew),singular_values(z),rtol=1e-10,atol=1e-10)

def test_whitening_rejects_non_spd_covariance():
    import pytest
    with pytest.raises(ValueError): whiten_features(np.ones((4,2)),np.array([[1.,2.],[2.,1.]]))

def test_weighted_noise_rank_uniform_weights_matches_unweighted():
    rng=np.random.default_rng(99); z=rng.normal(size=(45,12)); a=noise_edge_rank(z,n_null=60,seed=7); b=weighted_noise_edge_rank(z,np.ones(z.shape[0]),n_null=60,seed=7)
    assert a[0]==b[0] and np.allclose(a[1],b[1]) and np.isclose(a[2],b[2])

def test_weighted_noise_rank_rejects_nonpositive_weights():
    import pytest
    with pytest.raises(ValueError): weighted_noise_edge_rank(np.ones((3,2)),np.array([1.,0.,1.]),n_null=5)
