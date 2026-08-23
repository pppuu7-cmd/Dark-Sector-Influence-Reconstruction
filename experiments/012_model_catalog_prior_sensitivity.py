#!/usr/bin/env python3
"""Experiment 012: catalog multiplicity can hide a rare influence mode.

Three model families occupy three independent response modes but are represented
by 900, 90, and 10 samples. Compare the implicit catalog-frequency prior with an
equal-family prior; the null edge is recalibrated under the same row weights.
"""
from pathlib import Path
import csv,sys
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from dsir.rank import noise_edge_rank,weighted_noise_edge_rank
OUT=ROOT/"data"/"derived"/"rank_robustness"

def make_imbalanced_catalog(counts=(900,90,10),n_obs=64,signal=5.0,seed=3):
    rng=np.random.default_rng(seed); q,_=np.linalg.qr(rng.normal(size=(n_obs,3))); blocks=[]; fam=[]
    for j,n in enumerate(counts):
        amp=rng.normal(size=n); blocks.append(signal*amp[:,None]*q[:,j][None,:]+rng.normal(size=(n,n_obs))); fam.extend([j]*n)
    return np.vstack(blocks),np.asarray(fam)

def equal_family_weights(families):
    unique,counts=np.unique(families,return_counts=True); c=dict(zip(unique,counts)); return np.asarray([1.0/c[x] for x in families])

def main():
    z,fam=make_imbalanced_catalog(); raw_rank,raw_sv,raw_edge=noise_edge_rank(z,n_null=240,quantile=0.95,seed=4)
    bal_rank,bal_sv,bal_edge=weighted_noise_edge_rank(z,equal_family_weights(fam),n_null=240,quantile=0.95,seed=4); counts=np.bincount(fam)
    OUT.mkdir(parents=True,exist_ok=True)
    with (OUT/"experiment_012_prior_sensitivity.csv").open("w",newline="") as f:
        w=csv.writer(f); w.writerow(["scheme","rank","noise_edge","sv1","sv2","sv3","sv4","sv3_over_sv1"]); w.writerow(["catalog_multiplicity",raw_rank,raw_edge,*raw_sv[:4],raw_sv[2]/raw_sv[0]]); w.writerow(["equal_family_prior",bal_rank,bal_edge,*bal_sv[:4],bal_sv[2]/bal_sv[0]])
    text=("Experiment 012 — model-catalog prior sensitivity\n"
          f"family_counts={counts.tolist()}\n"
          f"catalog_multiplicity_rank={raw_rank}; edge={raw_edge:.6f}; top4={','.join(f'{x:.6f}' for x in raw_sv[:4])}\n"
          f"equal_family_prior_rank={bal_rank}; edge={bal_edge:.6f}; top4={','.join(f'{x:.6f}' for x in bal_sv[:4])}\n"
          f"sv3/sv1 raw={raw_sv[2]/raw_sv[0]:.6f}; equal_family={bal_sv[2]/bal_sv[0]:.6f}\n"
          "INTERPRETATION: catalog multiplicity is an implicit theory prior and can hide a rare independent response mode.\n"
          "RULE: DSIR must publish R_model prior-sensitivity/stratified-bootstrap results, not a single catalog-frequency rank.\n"
          "STATUS: G5 model-catalog-prior failure mode demonstrated and controlled synthetically; real theory-manifold robustness remains open.\n")
    (OUT/"experiment_012_output.txt").write_text(text); print(text)
    if raw_rank!=2 or bal_rank!=3: raise SystemExit(f"unexpected control outcome: raw={raw_rank}, balanced={bal_rank}")

if __name__=="__main__": main()
