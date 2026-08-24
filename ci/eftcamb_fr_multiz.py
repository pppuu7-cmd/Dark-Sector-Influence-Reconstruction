#!/usr/bin/env python3
"""Extract a frozen-grid multi-z H-EFTCAMB designer-f(R) response matrix."""
from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

import numpy as np

CORE_K = np.array([0.001, 0.003, 0.01, 0.03, 0.1], dtype=float)
Z_NODES = np.array([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], dtype=float)


def load_pk(path: str) -> tuple[np.ndarray, np.ndarray]:
    arr = np.loadtxt(path, comments="#")
    if arr.ndim != 2 or arr.shape[1] < 2:
        raise ValueError(f"Expected >=2 columns in {path}")
    k = np.asarray(arr[:, 0], float)
    p = np.asarray(arr[:, 1], float)
    mask = np.isfinite(k) & np.isfinite(p) & (k > 0) & (p > 0)
    k, p = k[mask], p[mask]
    order = np.argsort(k)
    k, p = k[order], p[order]
    if k.size < 4 or np.any(np.diff(k) <= 0):
        raise ValueError(f"Invalid k grid in {path}")
    return k, p


def interp_logp(k: np.ndarray, p: np.ndarray, nodes: np.ndarray) -> np.ndarray:
    if nodes.min() < k.min() or nodes.max() > k.max():
        raise ValueError(f"Requested k nodes outside [{k.min()}, {k.max()}]")
    return np.exp(np.interp(np.log(nodes), np.log(k), np.log(p)))


def find_one(root: Path, token: str, index: int) -> str:
    patt = str(root / f"**/*{token}*z{index}*matterpower*.dat")
    hits = sorted(glob.glob(patt, recursive=True))
    if len(hits) != 1:
        raise ValueError(f"Expected one file for token={token!r}, z-index={index}; got {hits}")
    return hits[0]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--gr-token", required=True)
    ap.add_argument("--model-token", required=True)
    ap.add_argument("--B0", type=float, required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    root = Path(args.root)
    matrix = np.empty((len(Z_NODES), len(CORE_K)))
    files = []
    for iz, z in enumerate(Z_NODES, start=1):
        gp = find_one(root, args.gr_token, iz)
        mp = find_one(root, args.model_token, iz)
        kg, pg = load_pk(gp)
        km, pm = load_pk(mp)
        pgc = interp_logp(kg, pg, CORE_K)
        pmc = interp_logp(km, pm, CORE_K)
        matrix[iz - 1] = np.log(pmc / pgc)
        files.append({"z": float(z), "gr": gp, "model": mp})

    out = {
        "definition": "r_Delta(k,z)=ln(P_designer_fR/P_GR), same H-EFTCAMB solver and matched settings",
        "B0": args.B0,
        "z_nodes": Z_NODES.tolist(),
        "k_h_mpc": CORE_K.tolist(),
        "r_Delta": matrix.tolist(),
        "max_abs_r_Delta": float(np.max(np.abs(matrix))),
        "max_abs_by_z": np.max(np.abs(matrix), axis=1).tolist(),
        "max_abs_by_k": np.max(np.abs(matrix), axis=0).tolist(),
        "files": files,
        "status": "EXTRACTED_NOT_A_GATE",
    }
    Path(args.json).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
