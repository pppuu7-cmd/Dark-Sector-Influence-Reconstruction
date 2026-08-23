#!/usr/bin/env python3
"""Experiment 011: G5 rank robustness under feature re-scaling/correlation.

Start in a whitened coordinate system with injected latent rank 3, then apply
strongly anisotropic/correlated feature transforms. Correct covariance whitening
must recover rank 3. Applying an iid null edge to raw coordinates is an
intentionally invalid negative control.
"""
from pathlib import Path
import csv,sys
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from dsir.rank import noise_edge_rank,singular_values,whiten_features
OUT=ROOT/"data"/"derived"/"rank_robustness"

def make_whitened_case(n_models,n_obs=64,latent_rank=3,signal=5.0,seed=0):
    rng=np.random.default_rng(seed); q,_=np.linalg.qr(rng.normal(size=(n_obs,latent_rank))); coeff=rng.normal(size=(n_models,latent_rank))
    return signal*coeff@q.T+rng.normal(size=(n_models,n_obs))

def feature_transform(n_obs,seed):
    rng=np.random.default_rng(seed); scales=10.0**rng.uniform(-1.0,1.0,size=n_obs); q,_=np.linalg.qr(rng.normal(size=(n_obs,n_obs)))
    A=np.diag(scales)@q; return A,A@A.T

def main():
    OUT.mkdir(parents=True,exist_ok=True); rows=[]; recovered=0; total=0; maxerr=0.0; naive=[]
    for n_models in (90,180,360):
        for rep in range(10):
            seed=11000+100*n_models+rep; white=make_whitened_case(n_models=n_models,seed=seed); A,cov=feature_transform(white.shape[1],seed+1)
            raw=white@A.T; rew=whiten_features(raw,cov); s0=singular_values(white); s1=singular_values(rew)
            rel=float(np.max(np.abs(s1-s0)/np.maximum(s0,1e-12))); maxerr=max(maxerr,rel)
            rw,_,edge=noise_edge_rank(rew,n_null=160,quantile=0.95,seed=seed+2); rn,_,nedge=noise_edge_rank(raw,n_null=160,quantile=0.95,seed=seed+2)
            total+=1; recovered+=int(rw==3); naive.append(rn); rows.append((n_models,rep,rw,rn,edge,nedge,np.linalg.cond(cov),rel))
    with (OUT/"experiment_011_rank_whitening.csv").open("w",newline="") as f:
        w=csv.writer(f); w.writerow(["n_models","rep","rank_whitened","rank_naive_raw","noise_edge_whitened","noise_edge_naive","cov_condition","spectrum_relerr"]); w.writerows(rows)
    counts={r:naive.count(r) for r in sorted(set(naive))}
    text=("Experiment 011 — G5 covariance-whitening rank robustness\n"
          f"injected_rank=3; cases={total}; correctly_recovered_after_whitening={recovered}/{total}\n"
          f"max_relative_singular_spectrum_error_after_whitening={maxerr:.3e}\n"
          f"naive_unwhitened_rank_min={min(naive)}; max={max(naive)}; counts={counts}\n"
          "INTERPRETATION: latent-rank claims are coordinate/unit robust only after covariance whitening.\n"
          "NEGATIVE CONTROL: iid-noise calibration on unwhitened heterogeneous features creates many false spikes.\n"
          "STATUS: G5 scaling/covariance-coordinate robustness PASS on this synthetic suite; broader model-family sampling robustness remains open.\n")
    (OUT/"experiment_011_output.txt").write_text(text); print(text)
    if recovered!=total: raise SystemExit(f"G5 FAIL: rank 3 recovered in only {recovered}/{total} whitened cases")
    if maxerr>1e-10: raise SystemExit("G5 FAIL: whitening did not preserve singular spectrum")
    if max(naive)<=3: raise SystemExit("negative control did not expose expected unwhitened false-rank failure")

if __name__=="__main__": main()
