import numpy as np
from dsir.conditioning import conditional_innovation

def test_conditional_innovation_matches_schur_complement():
    c=np.array([[2.0,0.6],[0.6,1.0]])
    r=np.array([1.0,0.4])
    inn,var,beta=conditional_innovation(r,c,target=1,conditioned_on=[0])
    assert np.allclose(beta,[0.3])
    assert np.isclose(inn,0.1)
    assert np.isclose(var,0.82)

def test_independent_channel_is_unchanged():
    c=np.eye(3); r=np.array([0.2,-0.4,0.7])
    inn,var,beta=conditional_innovation(r,c,target=1,conditioned_on=[0,2])
    assert np.isclose(inn,-0.4) and np.isclose(var,1.0)
    assert np.allclose(beta,0)
