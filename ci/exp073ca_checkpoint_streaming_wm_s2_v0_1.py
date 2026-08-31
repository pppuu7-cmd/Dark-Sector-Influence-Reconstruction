#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ctypes
import hashlib
import importlib
import json
import os
from pathlib import Path
import subprocess
import time

import numpy as np

from dsir_remote_band_checkpoint_v0_1 import BandCheckpointStore, CheckpointContract, print_progress

PREREG_COMMIT = "564a8d48f2af26d4394521f3fb55d51d80bcafe9"
HELPER_COMMIT = "fa971eb4ef8c47e81eb0bb4e13eeb76f7cf42e22"
BW_HELPER_COMMIT = "9fb0ecb79986cf5f542760377533a685745b31e2"
CHECKPOINT_UTILITY_COMMIT = "0b0324afb69acb16cbea97bb924b9be48f303dde"
CHECKPOINT_SYNC_COMMIT = "96886916b41dce7f0a40807622928c841ef5fc58"
L = 12288
LMAX = L - 1
EDGES = np.array([0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288], dtype=np.int32)
NB = len(EDGES) - 1
THREADS = 8
CHUNK = 4
SIGNATURE = (0, 2, 0, 2)


def canon(a):
    return np.ascontiguousarray(np.asarray(a, dtype="<f8"))


def chash(a):
    return hashlib.sha256(canon(a).tobytes(order="C")).hexdigest()


def runtime_nmtlib() -> bytes:
    ext = importlib.import_module("_nmtlib")
    return str(Path(ext.__file__).resolve()).encode()


def load_bw(path: Path):
    lib = ctypes.CDLL(str(path.resolve()))
    dptr = ctypes.POINTER(ctypes.c_double)
    iptr = ctypes.POINTER(ctypes.c_int)
    f = lib.exp073bw_stream_compress
    f.argtypes = [ctypes.c_char_p, dptr, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, iptr, ctypes.c_int, ctypes.c_int, dptr]
    f.restype = ctypes.c_int
    return f


def load_ca(path: Path):
    lib = ctypes.CDLL(str(path.resolve()))
    dptr = ctypes.POINTER(ctypes.c_double)
    iptr = ctypes.POINTER(ctypes.c_int)
    f = lib.exp073ca_stream_compress_range
    f.argtypes = [ctypes.c_char_p, dptr, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, iptr, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, dptr]
    f.restype = ctypes.c_int
    return f


def call_bw(f, pcl, edges, threads=THREADS):
    pcl = canon(pcl)
    edges = np.ascontiguousarray(edges, dtype=np.int32)
    nb = len(edges) - 1
    out = np.zeros((nb, pcl.size), dtype=np.float64)
    s1, s2, n1, n2 = SIGNATURE
    rc = f(runtime_nmtlib(), pcl.ctypes.data_as(ctypes.POINTER(ctypes.c_double)), pcl.size - 1, s1, s2, n1, n2, edges.ctypes.data_as(ctypes.POINTER(ctypes.c_int)), nb, threads, out.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
    if rc != 0:
        raise RuntimeError(f"BW helper rc={rc}")
    return canon(out)


def call_ca(f, pcl, edges, ib_lo, ib_hi, threads=THREADS):
    pcl = canon(pcl)
    edges = np.ascontiguousarray(edges, dtype=np.int32)
    nb = len(edges) - 1
    out = np.zeros((ib_hi - ib_lo, pcl.size), dtype=np.float64)
    s1, s2, n1, n2 = SIGNATURE
    rc = f(runtime_nmtlib(), pcl.ctypes.data_as(ctypes.POINTER(ctypes.c_double)), pcl.size - 1, s1, s2, n1, n2, edges.ctypes.data_as(ctypes.POINTER(ctypes.c_int)), nb, ib_lo, ib_hi, threads, out.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
    if rc != 0:
        raise RuntimeError(f"CA helper rc={rc} range={ib_lo}:{ib_hi}")
    return canon(out)


def pcl_family(name, nls):
    if name == "signed_dyadic":
        return canon(np.array([((ell % 11) - 5) / float(2 ** (3 + (ell % 5))) for ell in range(nls)], dtype=np.float64))
    if name == "positive_dyadic":
        return canon(np.array([(1 + (ell % 7)) / float(2 ** (4 + (ell % 6))) for ell in range(nls)], dtype=np.float64))
    raise ValueError(name)


def preflight(bw_so: Path, ca_so: Path, out_json: Path):
    edges = np.array([0, 7, 19, 41, 73, 128], dtype=np.int32)
    bw = load_bw(bw_so)
    ca = load_ca(ca_so)
    cases = []
    ok = True
    for fam in ("signed_dyadic", "positive_dyadic"):
        pcl = pcl_family(fam, 128)
        ref = call_bw(bw, pcl, edges, THREADS)
        got = np.zeros_like(ref)
        for lo in range(0, len(edges) - 1, 2):
            hi = min(len(edges) - 1, lo + 2)
            got[lo:hi] = call_ca(ca, pcl, edges, lo, hi, THREADS)
        eq = bool(np.array_equal(ref, got))
        hr, hg = chash(ref), chash(got)
        case = {"family": fam, "array_equal": eq, "sha_ref": hr, "sha_range": hg, "sha_equal": hr == hg, "max_abs_diff_diagnostic_only": float(np.max(np.abs(ref-got)))}
        cases.append(case)
        ok = ok and eq and hr == hg
    rec = {"experiment": "Exp073CA", "stage": "checkpoint_boundary_exact_preflight", "prereg_commit": PREREG_COMMIT, "helper_commit": HELPER_COMMIT, "bw_helper_commit": BW_HELPER_COMMIT, "signature": list(SIGNATURE), "lmax": 127, "threads": THREADS, "cases": cases, "status": "CA_PREFLIGHT_EXACT_PASS" if ok else "CA_PREFLIGHT_EXACT_MISMATCH"}
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")
    print(json.dumps(rec, indent=2, sort_keys=True), flush=True)
    if not ok:
        raise SystemExit(41)


def remote_push(checkpoint_dir: Path, branch: str, label: str):
    subprocess.run(["bash", "ci/dsir_checkpoint_git_sync_v0_1.sh", "push", str(checkpoint_dir), branch, label], check=True)


def run_full(pcl_path: Path, ca_so: Path, checkpoint_dir: Path, checkpoint_branch: str, replica: str, out_npz: Path, out_json: Path):
    pcl = canon(np.load(pcl_path, allow_pickle=False))
    if pcl.shape != (L,) or not np.all(np.isfinite(pcl)):
        raise RuntimeError(f"invalid Wm_S2 PCL {pcl.shape}")
    pcl_sha = chash(pcl)
    source_commit = os.environ.get("GITHUB_SHA", "UNKNOWN")
    contract = CheckpointContract(
        experiment="Exp073CA",
        source_commit=source_commit,
        helper_commit=HELPER_COMMIT,
        prereg_commit=PREREG_COMMIT,
        task="Wm_S2",
        lmax=LMAX,
        nbands=NB,
        row_length=L,
        threads=THREADS,
        extra={
            "replica": replica,
            "pcl_sha256": pcl_sha,
            "bw_helper_commit": BW_HELPER_COMMIT,
            "checkpoint_utility_commit": CHECKPOINT_UTILITY_COMMIT,
            "checkpoint_sync_commit": CHECKPOINT_SYNC_COMMIT,
            "chunk_bands": CHUNK,
            "edges": [int(x) for x in EDGES],
            "signature": list(SIGNATURE),
            "checkpoint_boundary": "complete_band_only",
        },
    )
    store = BandCheckpointStore(checkpoint_dir, contract)
    matrix, completed = store.restore_matrix()
    completed_set = set(completed)
    f = load_ca(ca_so)
    started = time.monotonic()
    print_progress(store, started, THREADS)

    while len(completed_set) < NB:
        lo = next(b for b in range(NB) if b not in completed_set)
        if any(b not in completed_set for b in range(lo)):
            raise RuntimeError("non-prefix checkpoint state; fail closed")
        hi = min(NB, lo + CHUNK)
        if any(b in completed_set for b in range(lo, hi)):
            raise RuntimeError("checkpoint gap inside next chunk; fail closed")
        t0 = time.monotonic()
        rows = call_ca(f, pcl, EDGES, lo, hi, THREADS)
        elapsed = time.monotonic() - t0
        per_band = elapsed / float(hi - lo)
        for j, band in enumerate(range(lo, hi)):
            row = canon(rows[j])
            matrix[band] = row
            store.save_completed_band(band, row, ell_lo=int(EDGES[band]), ell_hi_exclusive=int(EDGES[band+1]), wall_seconds=per_band)
            completed_set.add(band)
        remote_push(checkpoint_dir, checkpoint_branch, f"Exp073CA {replica} bands {lo}-{hi-1}")
        print_progress(store, started, THREADS)

    matrix, completed = store.restore_matrix()
    if completed != list(range(NB)):
        raise RuntimeError(f"not all bands complete: {completed}")
    matrix = canon(matrix)
    if matrix.shape != (NB, L) or not np.all(np.isfinite(matrix)):
        raise RuntimeError("invalid final compact matrix")
    out_npz.parent.mkdir(parents=True, exist_ok=True)
    np.savez(out_npz, A=matrix)
    meta = {
        "experiment": "Exp073CA",
        "stage": "full_scale_checkpoint_streaming_compact",
        "task": "Wm_S2",
        "replica": replica,
        "shape": [NB, L],
        "dtype": "<f8",
        "sha256": chash(matrix),
        "pcl_sha256": pcl_sha,
        "completed_bands": completed,
        "checkpoint_branch": checkpoint_branch,
        "checkpoint_contract_fingerprint": contract.fingerprint(),
        "threads": THREADS,
        "chunk_bands": CHUNK,
        "prereg_commit": PREREG_COMMIT,
        "helper_commit": HELPER_COMMIT,
        "bw_helper_commit": BW_HELPER_COMMIT,
        "status": "COMPLETE_VALID_COMPARATOR_INPUT_EXP073CA_WM_S2_COMPACT_V0_1",
    }
    out_json.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
    print(json.dumps(meta, indent=2, sort_keys=True), flush=True)


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("preflight")
    p.add_argument("--bw-so", required=True)
    p.add_argument("--ca-so", required=True)
    p.add_argument("--out-json", required=True)
    p = sp.add_parser("run")
    p.add_argument("--pcl-npy", required=True)
    p.add_argument("--ca-so", required=True)
    p.add_argument("--checkpoint-dir", required=True)
    p.add_argument("--checkpoint-branch", required=True)
    p.add_argument("--replica", required=True, choices=["A", "B"])
    p.add_argument("--out-npz", required=True)
    p.add_argument("--out-json", required=True)
    a = ap.parse_args()
    if a.cmd == "preflight":
        preflight(Path(a.bw_so), Path(a.ca_so), Path(a.out_json))
    else:
        run_full(Path(a.pcl_npy), Path(a.ca_so), Path(a.checkpoint_dir), a.checkpoint_branch, a.replica, Path(a.out_npz), Path(a.out_json))


if __name__ == "__main__":
    main()
