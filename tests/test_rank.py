import numpy as np
from dsir.rank import (
    effective_rank,
    variance_rank,
    singular_values,
    whiten_features,
    noise_edge_rank,
    weighted_noise_edge_rank,
    family_balanced_weights,
    normalize_prior_weights,
)

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

def test_family_balanced_weights_remove_catalog_multiplicity_prior():
    labels=np.array(['A']*6+['B']*2+['C'])
    w=family_balanced_weights(labels)
    # The returned vector has mean one, but each family has equal total mass.
    totals=[w[labels==fam].sum() for fam in ['A','B','C']]
    assert np.allclose(totals,totals[0])
    assert np.isclose(w.mean(),1.0)
    assert np.isclose(w[labels=='A'][0]*3.0,w[labels=='B'][0])
    assert np.isclose(w[labels=='B'][0]*2.0,w[labels=='C'][0])

def test_family_balanced_weights_preserve_explicit_within_family_prior():
    labels=np.array(['A','A','B','B'])
    local=np.array([1.,3.,2.,2.])
    w=family_balanced_weights(labels,local)
    assert np.isclose(w[1]/w[0],3.0)
    assert np.isclose(w[2],w[3])
    assert np.isclose(w[:2].sum(),w[2:].sum())

def test_prior_weight_normalization_rejects_invalid():
    import pytest
    assert np.allclose(normalize_prior_weights(np.array([1.,2.,3.])),np.array([0.5,1.0,1.5]))
    with pytest.raises(ValueError): normalize_prior_weights(np.array([1.,np.nan]))
