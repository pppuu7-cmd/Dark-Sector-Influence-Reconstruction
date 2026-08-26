#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import subprocess
import sys
import warnings
from pathlib import Path

import numpy as np
from scipy.integrate import IntegrationWarning, quad
from scipy.interpolate import PchipInterpolator, interp1d

UPSTREAM_PIN = "6302c30d9e70f8e4ff2d4a84a9977b4471705179"
CAMB_PIN = "fa3f097343fbbe427cc04b4f5f0041c22c6ec764"
ARCHIVE_SHA256 = "1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570"
ELL = np.arange(6144, dtype=np.float64)
ZMIN = 0.0
ZMAX = 3.0
KMAX = 10.0
CAMB_KMAX = 12.0
NINT = 96
NZ_CAMB = 128
TOL = 5e-13
PROBE_Z = np.array([0.5, 1.0, 2.0], dtype=np.float64)
PROBE_K = np.array([0.02, 0.10, 0.20], dtype=np.float64)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dsir.act_unwise_projection import compute_raw_no_cleft

TRACER_FILES = {
    "Blue": {
        "xmatch": "aux_data/dndz/unWISE_blue_xmatch_dndz.txt",
        "xcorr": "aux_data/dndz/unWISE_blue_xcorr_bdndz.txt",
        "pcs": "aux_data/dndz/unWISE_blue_delta_bdndz_pcs.dat",
        "n_pcs": 3,
    },
    "Green": {
        "xmatch": "aux_data/dndz/unWISE_green_xmatch_dndz.txt",
        "xcorr": "aux_data/dndz/unWISE_green_xcorr_bdndz.txt",
        "pcs": "aux_data/dndz/unWISE_green_delta_bdndz_pcs.dat",
        "n_pcs": 5,
    },
}


def git_head(repo: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
    ).strip()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def find_data_root(root: Path) -> Path:
    candidates = []
    for p in [root, *root.rglob("*")]:
        if p.is_dir() and all((p / x).is_dir() for x in ("bandpowers", "covariances", "aux_data")):
            candidates.append(p)
    if not candidates:
        raise FileNotFoundError("no extracted ACT x unWISE data root found")
    candidates.sort(key=lambda p: (len(p.parts), str(p)))
    return candidates[0]


def extract_nodes(path: Path, names: set[str], kind):
    tree = ast.parse(path.read_text(), filename=str(path))
    nodes = [n for n in tree.body if isinstance(n, kind) and n.name in names]
    found = {n.name for n in nodes}
    if found != names:
        raise RuntimeError(f"missing source nodes in {path}: expected {sorted(names)}, got {sorted(found)}")
    mod = ast.Module(body=nodes, type_ignores=[])
    ast.fix_missing_locations(mod)
    return mod


def load_exact_upstream(repo: Path):
    package = repo / "unWISExLens_lklh"
    model_path = package / "theory_modules" / "unWISExkappa_model.py"
    helper_path = package / "theory_modules" / "model_helpers_unWISExLens.py"
    dndz_path = package / "auxiliary" / "dN_dz_aux.py"
    aux_path = package / "auxiliary" / "auxiliary_functions.py"

    # Exact pinned evaluate_pk_kmax.
    aux_mod = extract_nodes(aux_path, {"evaluate_pk_kmax"}, (ast.FunctionDef, ast.AsyncFunctionDef))
    aux_ns = {"np": np}
    exec(compile(aux_mod, str(aux_path), "exec"), aux_ns)

    # Exact pinned raw model class, stripping only module imports as in Exp066A.
    model_tree = ast.parse(model_path.read_text(), filename=str(model_path))
    model_tree.body = [n for n in model_tree.body if not isinstance(n, (ast.Import, ast.ImportFrom))]
    ast.fix_missing_locations(model_tree)
    model_ns = {"np": np, "evaluate_pk_kmax": aux_ns["evaluate_pk_kmax"]}
    exec(compile(model_tree, str(model_path), "exec"), model_ns)

    # Exact pinned geometry + tracer container classes only; do not import Cobaya package wrapper.
    helper_mod = extract_nodes(helper_path, {"cosmo_from_camb", "dNdz"}, ast.ClassDef)
    helper_ns = {"np": np}
    exec(compile(helper_mod, str(helper_path), "exec"), helper_ns)

    # Exact pinned dN/dz normalisation helper.
    dndz_mod = extract_nodes(dndz_path, {"dN_dz_Helper"}, ast.ClassDef)
    dndz_ns = {
        "np": np,
        "interp1d": interp1d,
        "integrate": quad,
        "IntegrationWarning": IntegrationWarning,
        "warnings": warnings,
    }
    exec(compile(dndz_mod, str(dndz_path), "exec"), dndz_ns)

    source_contract = {
        "compute_raw_spectra_present": "def compute_raw_spectra" in model_path.read_text(),
        "evaluate_pk_kmax_present": "def evaluate_pk_kmax" in aux_path.read_text(),
        "cosmo_from_camb_present": "class cosmo_from_camb" in helper_path.read_text(),
        "dNdz_present": "class dNdz" in helper_path.read_text(),
        "dN_dz_Helper_present": "class dN_dz_Helper" in dndz_path.read_text(),
    }
    source_contract["pass"] = bool(all(source_contract.values()))
    return (
        model_ns["unWISExLens_theory_model"],
        helper_ns["cosmo_from_camb"],
        helper_ns["dNdz"],
        dndz_ns["dN_dz_Helper"],
        source_contract,
    )


def build_camb_physical():
    import camb
    from camb import model

    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=67.0,
        ombh2=0.0224,
        omch2=0.1200,
        omk=0.0,
        mnu=0.0,
        nnu=3.046,
        TCMB=2.7255,
        YHe=0.24,
        tau=0.0,
    )
    pars.InitPower.set_params(As=2.10e-9, ns=0.965, pivot_scalar=0.05)
    pars.set_dark_energy(w=-1.0)
    pars.WantCls = False
    zgrid = np.logspace(np.log10(1.0 + ZMIN), np.log10(1.0 + ZMAX), NZ_CAMB) - 1.0
    pars.set_matter_power(redshifts=list(zgrid[::-1]), kmax=CAMB_KMAX, silent=True)
    pars.NonLinear = model.NonLinear_none
    results = camb.get_results(pars)
    common = dict(nonlinear=False, hubble_units=False, k_hunit=False, extrap_kmax=None)
    pww = results.get_matter_power_interpolator(var1="Weyl", var2="Weyl", **common)
    pwm = results.get_matter_power_interpolator(var1="Weyl", var2="delta_nonu", **common)
    pmm = results.get_matter_power_interpolator(var1="delta_nonu", var2="delta_nonu", **common)
    return results, pww, pwm, pmm


def build_real_tracers(data_root: Path, Dndz, DndzHelper):
    tracers = []
    records = {}
    for sample in ("Blue", "Green"):
        cfg = TRACER_FILES[sample]
        paths = {key: data_root / cfg[key] for key in ("xmatch", "xcorr", "pcs")}
        exists = all(p.is_file() for p in paths.values())
        finite_files = True
        file_shapes = {}
        file_hashes = {}
        for key, p in paths.items():
            if not p.is_file():
                finite_files = False
                continue
            arr = np.asarray(np.loadtxt(p), dtype=np.float64)
            finite_files &= bool(np.all(np.isfinite(arr)))
            file_shapes[key] = list(arr.shape)
            file_hashes[key] = sha256(p)
        if not exists:
            raise FileNotFoundError(f"released tracer files missing for {sample}")

        xmatch, _, _ = DndzHelper.get_dn_dz(str(paths["xmatch"]))
        xcorr, _, _ = DndzHelper.get_dn_dz(str(paths["xcorr"]))
        pcs_data = np.asarray(np.loadtxt(paths["pcs"]), dtype=np.float64)
        pcs_interp = PchipInterpolator(pcs_data[:, 0], pcs_data[:, 1:])
        tracer = Dndz(xmatch, xcorr, pcs_interp)
        tracers.append(tracer)
        records[sample] = {
            "exists": exists,
            "finite_files": bool(finite_files),
            "file_shapes": file_shapes,
            "sha256": file_hashes,
            "expected_n_pcs": int(cfg["n_pcs"]),
            "observed_n_pcs": int(tracer.n_pcs),
        }
    return tracers, records


def component_map(outputs):
    out = {}
    for i, rec in enumerate(outputs):
        for section in ("kg", "gg"):
            for key, value in rec[section].items():
                out[f"sample{i}/{section}/{key}"] = np.asarray(value, dtype=np.float64)
        out[f"sample{i}/bdndz_norm"] = np.asarray(rec["bdndz_norm"], dtype=np.float64)
    return out


def compare_maps(ref_map, dsir_map):
    if set(ref_map) != set(dsir_map):
        return False, {"key_mismatch": {"reference": sorted(ref_map), "dsir": sorted(dsir_map)}}
    all_ok = True
    records = {}
    for key in sorted(ref_map):
        a = np.asarray(ref_map[key], dtype=np.float64)
        b = np.asarray(dsir_map[key], dtype=np.float64)
        shape_ok = a.shape == b.shape
        if shape_ok:
            finite_a = np.isfinite(a)
            finite_b = np.isfinite(b)
            finite_pattern_ok = bool(np.array_equal(finite_a, finite_b))
            finite = finite_a & finite_b
            if np.any(finite):
                max_ref = float(np.max(np.abs(a[finite])))
                max_abs = float(np.max(np.abs(a[finite] - b[finite])))
                threshold = TOL * max(1.0, max_ref)
                value_ok = max_abs <= threshold
            else:
                max_ref = 0.0
                max_abs = 0.0
                threshold = TOL
                value_ok = True
        else:
            finite_pattern_ok = False
            max_ref = max_abs = threshold = None
            value_ok = False
        zero_ref = bool(shape_ok and np.count_nonzero(a) == 0)
        zero_dsir = bool(shape_ok and np.count_nonzero(b) == 0)
        zero_ok = (not zero_ref) or zero_dsir
        ok = bool(shape_ok and finite_pattern_ok and value_ok and zero_ok)
        all_ok &= ok
        records[key] = {
            "shape_reference": list(a.shape),
            "shape_dsir": list(b.shape),
            "finite_pattern_equal": finite_pattern_ok,
            "max_abs_reference": max_ref,
            "max_abs_difference": max_abs,
            "threshold": threshold,
            "reference_identically_zero": zero_ref,
            "dsir_identically_zero": zero_dsir,
            "pass": ok,
        }
    return bool(all_ok), records


def provider_probe(pww, pwm, pmm):
    cells = []
    passed = True
    for z in PROBE_Z:
        for k in PROBE_K:
            ww = float(pww.P(float(z), float(k)))
            wm = float(pwm.P(float(z), float(k)))
            mm = float(pmm.P(float(z), float(k)))
            ok = bool(np.isfinite(ww) and np.isfinite(wm) and np.isfinite(mm) and ww > 0.0 and mm > 0.0 and wm != 0.0)
            passed &= ok
            cells.append({"z": float(z), "k_Mpc^-1": float(k), "P_WW": ww, "P_Wm": wm, "P_mm": mm, "pass": ok})
    return bool(passed), cells


def tracer_node_check(cosmo, tracers, tracer_records):
    gx, _ = np.polynomial.legendre.leggauss(NINT)
    chi_min, chi_max = cosmo.chi(ZMIN), cosmo.chi(ZMAX)
    chi = (chi_max - chi_min) / 2.0 * gx + (chi_max + chi_min) / 2.0
    z = np.asarray(cosmo.z_of_chi(chi), dtype=np.float64)
    all_ok = True
    for i, sample in enumerate(("Blue", "Green")):
        tr = tracers[i]
        x = np.asarray(tr.dNdz(z), dtype=np.float64)
        b = np.asarray(tr.bdNdz(z, pcs=True), dtype=np.float64)
        expected_cols = TRACER_FILES[sample]["n_pcs"] + 1
        ok = bool(
            tracer_records[sample]["exists"]
            and tracer_records[sample]["finite_files"]
            and tracer_records[sample]["observed_n_pcs"] == TRACER_FILES[sample]["n_pcs"]
            and x.shape == z.shape
            and b.shape == (z.size, expected_cols)
            and np.all(np.isfinite(x))
            and np.all(np.isfinite(b))
            and np.count_nonzero(x) > 0
            and np.count_nonzero(b) > 0
        )
        all_ok &= ok
        tracer_records[sample].update({
            "projection_node_xmatch_shape": list(x.shape),
            "projection_node_bdNdz_shape": list(b.shape),
            "projection_node_xmatch_nonzero": int(np.count_nonzero(x)),
            "projection_node_bdNdz_nonzero": int(np.count_nonzero(b)),
            "pass": ok,
        })
    return bool(all_ok), tracer_records


def nontriviality(ref_map, dsir_map):
    nonzero_suffixes = {"kg/kg_b", "kg/kmu", "gg/gg_bsq", "gg/gmu_b", "gg/mumu", "bdndz_norm"}
    zero_suffixes = {"kg/kg_nob", "gg/gg_b", "gg/gg_nob", "gg/gmu_nob"}
    records = {}
    all_ok = True
    for i, sample in enumerate(("Blue", "Green")):
        srec = {"nonzero": {}, "zero": {}}
        for suffix in sorted(nonzero_suffixes):
            key = f"sample{i}/{suffix}"
            a = ref_map[key]
            b = dsir_map[key]
            ok = bool(np.all(np.isfinite(a)) and np.all(np.isfinite(b)) and np.count_nonzero(a) > 0 and np.count_nonzero(b) > 0)
            srec["nonzero"][suffix] = {"pass": ok, "reference_nonzero": int(np.count_nonzero(a)), "dsir_nonzero": int(np.count_nonzero(b))}
            all_ok &= ok
        for suffix in sorted(zero_suffixes):
            key = f"sample{i}/{suffix}"
            a = ref_map[key]
            b = dsir_map[key]
            ok = bool(np.count_nonzero(a) == 0 and np.count_nonzero(b) == 0)
            srec["zero"][suffix] = {"pass": ok}
            all_ok &= ok
        srec["pass"] = bool(all(v["pass"] for group in (srec["nonzero"], srec["zero"]) for v in group.values()))
        records[sample] = srec
    return bool(all_ok), records


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--upstream-repo", required=True)
    ap.add_argument("--camb-repo", required=True)
    ap.add_argument("--extracted-root", required=True)
    ap.add_argument("--archive", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    upstream_repo = Path(args.upstream_repo).resolve()
    camb_repo = Path(args.camb_repo).resolve()
    extracted_root = Path(args.extracted_root).resolve()
    archive = Path(args.archive).resolve()
    output = Path(args.output).resolve()

    upstream_head = git_head(upstream_repo)
    camb_head = git_head(camb_repo)
    archive_hash = sha256(archive)
    provenance = {
        "upstream_commit": upstream_head,
        "expected_upstream_commit": UPSTREAM_PIN,
        "CAMB_commit": camb_head,
        "expected_CAMB_commit": CAMB_PIN,
        "archive_sha256": archive_hash,
        "expected_archive_sha256": ARCHIVE_SHA256,
    }
    provenance["pass"] = bool(upstream_head == UPSTREAM_PIN and camb_head == CAMB_PIN and archive_hash == ARCHIVE_SHA256)

    UpstreamModel, CosmoFromCamb, Dndz, DndzHelper, source_contract = load_exact_upstream(upstream_repo)
    data_root = find_data_root(extracted_root)
    tracers, tracer_records = build_real_tracers(data_root, Dndz, DndzHelper)

    camb_results, pww, pwm, pmm = build_camb_physical()
    cosmo = CosmoFromCamb(camb_results, include_nu_OmegaM=True)
    tracer_pass, tracer_records = tracer_node_check(cosmo, tracers, tracer_records)
    provider_pass, provider_cells = provider_probe(pww, pwm, pmm)

    ref_model = UpstreamModel(
        zmax=ZMAX,
        zmin=ZMIN,
        k_max=KMAX,
        N_integration=NINT,
        cross_correlation_redshift_correction=None,
        cleft_interp_helper=None,
        ell_vals=ELL,
        want_gg_cross=False,
        ell_vals_clkk=None,
    )
    reference = ref_model.compute_raw_spectra(
        cosmo,
        tracers,
        pww,
        pwm,
        pmm,
        cleft_interpolations_dtot_dnonu=None,
        cleft_interpolations_dnonu_dnonu=None,
        fid_bias_evol_list=None,
    )
    dsir = compute_raw_no_cleft(
        cosmo,
        tracers,
        pww,
        pwm,
        pmm,
        ell_vals=ELL,
        zmin=ZMIN,
        zmax=ZMAX,
        kmax=KMAX,
        n_integration=NINT,
    )

    ref_map = component_map(reference)
    dsir_map = component_map(dsir)
    equivalence_pass, equivalence = compare_maps(ref_map, dsir_map)
    nontrivial_pass, nontrivial = nontriviality(ref_map, dsir_map)

    passed = bool(
        provenance["pass"]
        and source_contract["pass"]
        and tracer_pass
        and provider_pass
        and equivalence_pass
        and nontrivial_pass
    )
    status = "PASS_ACT_UNWISE_PHYSICAL_FORWARD_REPRODUCTION_V0_1" if passed else "FAIL_ACT_UNWISE_PHYSICAL_FORWARD_REPRODUCTION_V0_1"

    result = {
        "experiment": "Exp068A",
        "date": "2026-08-26",
        "status": status,
        "scope": "physical linear/no-CLEFT ACT x unWISE raw forward-adapter reproduction; no G7 law and no G8 family",
        "provenance": provenance,
        "source_contract": source_contract,
        "frozen_domain": {
            "ell_first": int(ELL[0]),
            "ell_last": int(ELL[-1]),
            "ell_count": int(ELL.size),
            "zmin": ZMIN,
            "zmax": ZMAX,
            "projector_kmax_Mpc^-1": KMAX,
            "CAMB_internal_kmax_Mpc^-1": CAMB_KMAX,
            "Gauss_Legendre_order": NINT,
            "CAMB_redshift_grid_size": NZ_CAMB,
            "linear_no_CLEFT": True,
        },
        "R0_cosmology": {
            "H0_km_s_Mpc": 67.0,
            "ombh2": 0.0224,
            "omch2": 0.1200,
            "omk": 0.0,
            "mnu_eV": 0.0,
            "nnu": 3.046,
            "TCMB_K": 2.7255,
            "YHe": 0.24,
            "As": 2.10e-9,
            "ns": 0.965,
            "pivot_Mpc^-1": 0.05,
            "w": -1.0,
        },
        "tracer_binding": {"pass": tracer_pass, "data_root": str(data_root), "samples": tracer_records},
        "physical_provider_sanity": {"pass": provider_pass, "cells": provider_cells},
        "raw_component_equivalence": {"pass": equivalence_pass, "tolerance_factor": TOL, "components": equivalence},
        "nontrivial_physical_signal_control": {"pass": nontrivial_pass, "samples": nontrivial},
        "interpretation": (
            "PASS validates the physical R0 CAMB + released Blue/Green tracer raw forward adapter on all 6144 input multipoles; "
            "FAIL blocks nuisance quotient construction and must be diagnosed separately."
        ),
        "next_step_if_pass": (
            "Preregister the 26D selected-space nuisance tangent quotient using Exp067A whitening and the frozen selected ordering; "
            "freeze the SVD rank rule before fitting any G7 relation."
        ),
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))

    # The workflow preserves either scientific outcome. Do not hide a hard FAIL
    # behind a nonzero exit status; infrastructure exceptions still fail the job.


if __name__ == "__main__":
    main()
