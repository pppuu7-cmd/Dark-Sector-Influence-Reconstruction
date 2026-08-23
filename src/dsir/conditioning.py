"""Gaussian conditional-innovation operators for DSIR response channels."""
from __future__ import annotations
import numpy as np


def conditional_innovation(residual, covariance, target, conditioned_on):
    """Return target innovation after conditioning on correlated channels.

    For a joint Gaussian residual r with covariance C,
      r_t^perp = r_t - C_tN C_NN^{-1} r_N
      Var(r_t^perp) = C_tt - C_tN C_NN^{-1} C_Nt.

    The output is an observational innovation. It does not imply a causal or
    physical separation unless additional assumptions justify that reading.
    """
    r=np.asarray(residual,dtype=float)
    c=np.asarray(covariance,dtype=float)
    N=list(conditioned_on); t=int(target)
    cnn=c[np.ix_(N,N)]
    ctn=c[t,N]
    beta=np.linalg.solve(cnn,ctn).T
    innovation=float(r[t]-beta@r[N])
    var=float(c[t,t]-ctn@np.linalg.solve(cnn,c[N,t]))
    if var <= 0:
        raise ValueError("conditional variance is not positive")
    return innovation, var, np.asarray(beta)
