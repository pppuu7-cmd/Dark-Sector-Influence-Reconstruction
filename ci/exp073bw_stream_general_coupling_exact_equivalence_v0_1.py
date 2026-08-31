#!/usr/bin/env python3
from __future__ import annotations

import ctypes
import hashlib
import importlib
import importlib.metadata
import json
from pathlib import Path
import subprocess
import traceback

import numpy as np
import pymaster as nmt

OUT = Path("data/derived/g7/exp073bw_stream_general_coupling_exact_equivalence_result_v0_1.json")
SRC = Path("ci/exp073bw_stream_general_coupling_v0_1.c")
SO = Path("build/exp073bw_stream_general_coupling_v0_1.so")
PREREG_COMMIT = "ba4b28ec9aeca2a465202374e390ba9b43bb3952"
HELPER_COMMIT = "9fb0ecb79986cf5f542760377533a685745b31e2"
BV_ARTIFACT_ID = 9768866582
BV_DIGEST = "sha256:33f013a8c7c06ce2f5f68e62a324b80f2b1911ff2a3cd3ff89a6af4add179cc5"
UPSTREAM_COMMIT = "24365fa59a38c15732f4f37e8b29265b75c442d5"

CASES = [
    (24, [0, 3, 7, 12, 18, 25]),
    (63, [0, 5, 12, 24, 40, 64]),
    (127, [0, 7, 19, 41, 73, 128]),
]
SIGNATURES = {
    "Wm_0_2_0_2": (0, 2, 0, 2),
    "WW_same_2_2_2_2": (2, 2, 2, 2),
    "WW_flip_2_m2_2_m2": (2, -2, 2, -2),
}


def canon(a):
    return np.ascontiguousarray(a, dtype="<f8")


def chash(a):
    x = canon(a)
    return hashlib.sha256(x.tobytes()).hexdigest()


def exact_record(a, b):
    aa = canon(a)
    bb = canon(b)
    eq = bool(np.array_equal(aa, bb))
    sha_a = chash(aa)
    sha_b = chash(bb)
    max_abs = float(np.max(np.abs(aa - bb))) if aa.size else 0.0
    return {
        "array_equal": eq,
        "sha_a": sha_a,
        "sha_b": sha_b,
        "sha_equal": sha_a == sha_b,
        "max_abs_diff_diagnostic_only": max_abs,
    }


def compress_general_stock(G, edges):
    l = G.shape[1]
    A = np.empty((len(edges) - 1, l), dtype=np.float64)
    for ib, (lo, hi) in enumerate(zip(edges[:-1], edges[1:])):
        acc = np.zeros(l, dtype=np.float64)
        for ell in range(int(lo), int(hi)):
            acc += G[ell]
        A[ib] = acc / float(hi - lo)
    return canon(A)


def make_pcl(name, nls):
    if name == "signed_dyadic":
        x = [((ell % 11) - 5) / float(2 ** (3 + (ell % 5))) for ell in range(nls)]
    elif name == "positive_dyadic":
        x = [(1 + (ell % 7)) / float(2 ** (4 + (ell % 6))) for ell in range(nls)]
    else:
        raise AssertionError(name)
    return canon(np.asarray(x, dtype=np.float64))


def compile_helper():
    SO.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "gcc", "-O2", "-shared", "-fPIC", "-fopenmp",
        "-fno-fast-math", "-fno-associative-math", "-ffp-contract=off",
        "-fno-tree-vectorize", str(SRC), "-o", str(SO), "-ldl", "-lm",
    ]
    p = subprocess.run(cmd, text=True, capture_output=True, check=False)
    return cmd, p


def load_helper():
    lib = ctypes.CDLL(str(SO.resolve()))
    dptr = ctypes.POINTER(ctypes.c_double)
    iptr = ctypes.POINTER(ctypes.c_int)
    lib.exp073bw_full.argtypes = [
        ctypes.c_char_p, dptr,
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
        ctypes.c_int, dptr,
    ]
    lib.exp073bw_full.restype = ctypes.c_int
    lib.exp073bw_stream_compress.argtypes = [
        ctypes.c_char_p, dptr,
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
        iptr, ctypes.c_int, ctypes.c_int, dptr,
    ]
    lib.exp073bw_stream_compress.restype = ctypes.c_int
    return lib


def helper_full(lib, ext_path_b, pcl, sig, threads):
    s1, s2, n1, n2 = sig
    lmax = pcl.size - 1
    out = np.zeros((lmax + 1, lmax + 1), dtype=np.float64)
    rc = lib.exp073bw_full(
        ext_path_b,
        pcl.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        lmax, s1, s2, n1, n2, threads,
        out.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    )
    return rc, canon(out)


def helper_compress(lib, ext_path_b, pcl, sig, edges, threads):
    s1, s2, n1, n2 = sig
    lmax = pcl.size - 1
    edges_arr = np.ascontiguousarray(edges, dtype=np.int32)
    nb = len(edges) - 1
    out = np.zeros((nb, lmax + 1), dtype=np.float64)
    rc = lib.exp073bw_stream_compress(
        ext_path_b,
        pcl.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        lmax, s1, s2, n1, n2,
        edges_arr.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
        nb, threads,
        out.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    )
    return rc, canon(out)


receipt = {
    "experiment": "Exp073BW",
    "classification": "NONCLASSIFYING_NUMERICAL_IMPLEMENTATION_EQUIVALENCE_QA",
    "authority": False,
    "scientific_pass_claimed": False,
    "scientific_readiness_increment": 0,
    "draft_data_readiness_increment": 0,
    "Exp073AQ_preserved_as_FAIL": True,
    "Exp073BJ_preserved_as_PASS": True,
    "Exp073BD_provisional_forbidden_downstream": True,
    "prereg_commit": PREREG_COMMIT,
    "helper_commit": HELPER_COMMIT,
    "bv_artifact_id": BV_ARTIFACT_ID,
    "bv_artifact_digest": BV_DIGEST,
    "upstream_namaster_v27_commit": UPSTREAM_COMMIT,
    "compiler_flags": [
        "-O2", "-shared", "-fPIC", "-fopenmp", "-fno-fast-math",
        "-fno-associative-math", "-ffp-contract=off", "-fno-tree-vectorize",
        "-ldl", "-lm",
    ],
    "status": "BW_Q5_INFRASTRUCTURE_OR_DIAGNOSTIC_INCOMPLETE",
    "cases": [],
}

try:
    version = importlib.metadata.version("pymaster")
    if not (version == "2.7" or version.startswith("2.7.")):
        raise RuntimeError(f"unexpected pymaster version {version}")
    ext = importlib.import_module("_nmtlib")
    ext_path = Path(ext.__file__).resolve()
    receipt["pymaster_version"] = version
    receipt["runtime_extension_path"] = str(ext_path)

    cmd, cp = compile_helper()
    receipt["compile"] = {
        "cmd": cmd,
        "returncode": cp.returncode,
        "stdout": cp.stdout,
        "stderr": cp.stderr,
    }
    if cp.returncode != 0:
        raise RuntimeError("helper compilation failed")

    lib = load_helper()
    ext_path_b = str(ext_path).encode("utf-8")

    any_thread_mismatch = False
    any_full_stock_mismatch = False
    any_comp_stock_mismatch = False

    for lmax, edges in CASES:
        for pcl_name in ("signed_dyadic", "positive_dyadic"):
            pcl = make_pcl(pcl_name, lmax + 1)
            for sig_name, sig in SIGNATURES.items():
                s1, s2, n1, n2 = sig
                case = {
                    "lmax": lmax,
                    "edges": edges,
                    "pcl_family": pcl_name,
                    "pcl_sha256": chash(pcl),
                    "signature_name": sig_name,
                    "signature": [s1, s2, n1, n2],
                }

                stock = canon(nmt.get_general_coupling_matrix(pcl, s1, s2, n1, n2))
                stock_comp = compress_general_stock(stock, edges)
                case["stock_full_sha256"] = chash(stock)
                case["stock_compressed_sha256"] = chash(stock_comp)

                rc_f1, full1 = helper_full(lib, ext_path_b, pcl, sig, 1)
                rc_f2, full2 = helper_full(lib, ext_path_b, pcl, sig, 2)
                rc_f2r, full2r = helper_full(lib, ext_path_b, pcl, sig, 2)
                rc_c1, comp1 = helper_compress(lib, ext_path_b, pcl, sig, edges, 1)
                rc_c2, comp2 = helper_compress(lib, ext_path_b, pcl, sig, edges, 2)
                rc_c2r, comp2r = helper_compress(lib, ext_path_b, pcl, sig, edges, 2)
                rcs = [rc_f1, rc_f2, rc_f2r, rc_c1, rc_c2, rc_c2r]
                case["helper_return_codes"] = rcs
                if any(rc != 0 for rc in rcs):
                    raise RuntimeError(f"helper nonzero return code in {sig_name}/{lmax}/{pcl_name}: {rcs}")

                case["full_1_vs_stock"] = exact_record(full1, stock)
                case["full_2_vs_stock"] = exact_record(full2, stock)
                case["full_1_vs_2"] = exact_record(full1, full2)
                case["full_2_repeat"] = exact_record(full2, full2r)
                case["compressed_1_vs_stock_compress"] = exact_record(comp1, stock_comp)
                case["compressed_2_vs_stock_compress"] = exact_record(comp2, stock_comp)
                case["compressed_1_vs_2"] = exact_record(comp1, comp2)
                case["compressed_2_repeat"] = exact_record(comp2, comp2r)

                thread_checks = [
                    case["full_1_vs_2"], case["full_2_repeat"],
                    case["compressed_1_vs_2"], case["compressed_2_repeat"],
                ]
                full_checks = [case["full_1_vs_stock"], case["full_2_vs_stock"]]
                comp_checks = [
                    case["compressed_1_vs_stock_compress"],
                    case["compressed_2_vs_stock_compress"],
                ]
                thread_ok = all(x["array_equal"] and x["sha_equal"] for x in thread_checks)
                full_ok = all(x["array_equal"] and x["sha_equal"] for x in full_checks)
                comp_ok = all(x["array_equal"] and x["sha_equal"] for x in comp_checks)
                case["thread_repeatability_exact"] = thread_ok
                case["full_stock_exact"] = full_ok
                case["stream_compressed_stock_exact"] = comp_ok
                any_thread_mismatch |= not thread_ok
                any_full_stock_mismatch |= not full_ok
                any_comp_stock_mismatch |= not comp_ok
                receipt["cases"].append(case)

    receipt["summary"] = {
        "case_count": len(receipt["cases"]),
        "all_thread_repeatability_exact": not any_thread_mismatch,
        "all_full_stock_exact": not any_full_stock_mismatch,
        "all_stream_compressed_stock_exact": not any_comp_stock_mismatch,
    }

    if any_thread_mismatch:
        receipt["status"] = "BW_Q4_THREAD_REPEATABILITY_EXACT_MISMATCH"
    elif any_full_stock_mismatch:
        receipt["status"] = "BW_Q2_FULL_MATRIX_EXACT_MISMATCH"
    elif any_comp_stock_mismatch:
        receipt["status"] = "BW_Q3_STREAM_COMPRESSED_EXACT_MISMATCH_AFTER_FULL_PASS"
    else:
        receipt["status"] = "BW_Q1_FULL_AND_STREAM_COMPRESSED_EXACT_EQUIVALENCE_PASS"

except Exception as e:
    receipt["status"] = "BW_Q5_INFRASTRUCTURE_OR_DIAGNOSTIC_INCOMPLETE"
    receipt["error"] = repr(e)
    receipt["traceback"] = traceback.format_exc()
finally:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(OUT.read_text())
