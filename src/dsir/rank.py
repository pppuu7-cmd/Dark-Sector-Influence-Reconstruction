import numpy as np


def singular_values(z: np.ndarray) -> np.ndarray:
    return np.linalg.svd(np.asarray(z,dtype=float),full_matrices=False,compute_uv=False)


def whiten_features(z: np.ndarray,covariance: np.ndarray) -> np.ndarray:
    """Whiten row-stacked response features: z @ L^{-T}, covariance=L L^T."""
    z=np.asarray(z,dtype=float); covariance=np.asarray(covariance,dtype=float)
    if z.ndim!=2: raise ValueError("z must be a 2D row-stacked response matrix")
    if covariance.shape!=(z.shape[1],z.shape[1]): raise ValueError("covariance shape must match the feature dimension")
    if not np.allclose(covariance,covariance.T,rtol=0.0,atol=1e-12): raise ValueError("covariance must be symmetric")
    try: chol=np.linalg.cholesky(covariance)
    except np.linalg.LinAlgError as exc: raise ValueError("covariance must be positive definite") from exc
    return np.linalg.solve(chol,z.T).T


def effective_rank(z: np.ndarray,atol: float=1e-15) -> float:
    s=singular_values(z); p=s*s; total=p.sum()
    if total<=atol: return 0.0
    p=p/total; p=p[p>atol]
    return float(np.exp(-(p*np.log(p)).sum()))


def variance_rank(z: np.ndarray,fraction: float=0.99) -> int:
    if not (0<fraction<=1): raise ValueError("fraction must lie in (0,1]")
    s=singular_values(z); p=s*s
    if p.sum()==0: return 0
    return int(np.searchsorted(np.cumsum(p)/p.sum(),fraction)+1)


def noise_edge_rank(z: np.ndarray,n_null: int=400,quantile: float=0.95,seed: int=0) -> tuple[int,np.ndarray,float]:
    """Count spikes above a global iid-Gaussian null edge; z must be whitened."""
    z=np.asarray(z,dtype=float); rng=np.random.default_rng(seed); obs=singular_values(z); null=np.empty(n_null)
    for i in range(n_null): null[i]=singular_values(rng.normal(size=z.shape))[0]
    edge=float(np.quantile(null,quantile)); return int(np.sum(obs>edge)),obs,edge


def normalize_prior_weights(row_weights: np.ndarray) -> np.ndarray:
    """Normalize positive theory-sample prior weights to mean one."""
    w=np.asarray(row_weights,dtype=float)
    if w.ndim!=1 or w.size==0: raise ValueError("row_weights must be a non-empty 1D array")
    if np.any(~np.isfinite(w)) or np.any(w<=0): raise ValueError("row_weights must be finite and strictly positive")
    return w*(len(w)/w.sum())


def family_balanced_weights(family_labels, within_family_weights=None) -> np.ndarray:
    """Give every named theory family equal total prior mass.

    By default samples are uniform within each family. Optional positive
    `within_family_weights` encode an explicit intra-family sampling prior;
    those weights are normalized separately inside each family before all
    families are assigned equal total mass. The final vector has mean one so
    it can be passed directly to `weighted_noise_edge_rank`.
    """
    labels=np.asarray(family_labels, dtype=object)
    if labels.ndim!=1 or labels.size==0: raise ValueError("family_labels must be a non-empty 1D sequence")
    if any(str(x)=="" for x in labels): raise ValueError("family labels must be non-empty")
    if within_family_weights is None:
        base=np.ones(labels.size,dtype=float)
    else:
        base=np.asarray(within_family_weights,dtype=float)
        if base.shape!=labels.shape: raise ValueError("within_family_weights must match family_labels")
        if np.any(~np.isfinite(base)) or np.any(base<=0): raise ValueError("within-family weights must be finite and positive")
    out=np.empty(labels.size,dtype=float)
    # Preserve first-seen family identity instead of sorting arbitrary objects.
    families=list(dict.fromkeys(labels.tolist()))
    for fam in families:
        idx=np.flatnonzero(labels==fam)
        local=base[idx]
        out[idx]=(1.0/len(families))*local/local.sum()
    return normalize_prior_weights(out)


def weighted_noise_edge_rank(z: np.ndarray,row_weights: np.ndarray,n_null: int=400,quantile: float=0.95,seed: int=0) -> tuple[int,np.ndarray,float]:
    """Noise-edge rank under an explicit prior over model samples.

    Weights are normalized to mean one and enter as sqrt(weight) row factors.
    Every null realization receives the identical row weights. This does not
    define a preferred theory prior: DSIR must report sensitivity to defensible
    priors/stratifications instead of treating catalog multiplicity as evidence.
    """
    z=np.asarray(z,dtype=float); w=np.asarray(row_weights,dtype=float)
    if z.ndim!=2: raise ValueError("z must be 2D")
    if w.shape!=(z.shape[0],): raise ValueError("row_weights must have one entry per row")
    w=normalize_prior_weights(w); rw=np.sqrt(w)[:,None]; obs=singular_values(z*rw); rng=np.random.default_rng(seed); null=np.empty(n_null)
    for i in range(n_null): null[i]=singular_values(rng.normal(size=z.shape)*rw)[0]
    edge=float(np.quantile(null,quantile)); return int(np.sum(obs>edge)),obs,edge
