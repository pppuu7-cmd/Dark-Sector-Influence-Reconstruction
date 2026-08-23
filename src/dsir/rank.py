import numpy as np


def singular_values(z: np.ndarray) -> np.ndarray:
    """Singular values in descending order."""
    return np.linalg.svd(np.asarray(z, dtype=float), full_matrices=False, compute_uv=False)


def whiten_features(z: np.ndarray, covariance: np.ndarray) -> np.ndarray:
    """Whiten observable/features of a row-stacked response matrix.

    Returns z @ L^{-T}, where covariance=L L^T. Rank diagnostics calibrated
    against iid N(0,1) null matrices are meaningful only after this operation
    (or an equivalent covariance whitening).
    """
    z=np.asarray(z,dtype=float); covariance=np.asarray(covariance,dtype=float)
    if z.ndim != 2: raise ValueError("z must be a 2D row-stacked response matrix")
    if covariance.shape != (z.shape[1],z.shape[1]): raise ValueError("covariance shape must match the feature dimension")
    if not np.allclose(covariance,covariance.T,rtol=0.0,atol=1e-12): raise ValueError("covariance must be symmetric")
    try: chol=np.linalg.cholesky(covariance)
    except np.linalg.LinAlgError as exc: raise ValueError("covariance must be positive definite") from exc
    return np.linalg.solve(chol,z.T).T


def effective_rank(z: np.ndarray, atol: float = 1e-15) -> float:
    s=singular_values(z); power=s*s; total=power.sum()
    if total <= atol: return 0.0
    p=power/total; p=p[p>atol]
    return float(np.exp(-(p*np.log(p)).sum()))


def variance_rank(z: np.ndarray, fraction: float = 0.99) -> int:
    if not (0 < fraction <= 1): raise ValueError("fraction must lie in (0,1]")
    s=singular_values(z); power=s*s
    if power.sum()==0: return 0
    cumulative=np.cumsum(power)/power.sum()
    return int(np.searchsorted(cumulative,fraction)+1)


def noise_edge_rank(z: np.ndarray,n_null: int=400,quantile: float=0.95,seed: int=0) -> tuple[int,np.ndarray,float]:
    """Count singular-value spikes above one Monte-Carlo global noise edge.

    Z must already be noise-whitened. Each iid N(0,1) null matrix contributes
    only its largest singular value to the null edge distribution.
    """
    z=np.asarray(z,dtype=float); rng=np.random.default_rng(seed); obs=singular_values(z)
    null_max=np.empty(n_null,dtype=float)
    for i in range(n_null): null_max[i]=singular_values(rng.normal(size=z.shape))[0]
    edge=float(np.quantile(null_max,quantile))
    return int(np.sum(obs>edge)),obs,edge
