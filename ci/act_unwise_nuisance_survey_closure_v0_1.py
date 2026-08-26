#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import subprocess
import sys
from copy import deepcopy
from pathlib import Path

import healpy as hp
import numpy as np
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dsir.act_unwise_closure import combine_raw_components, selected_survey_bandpowers

PINNED_COMMIT = "6302c30d9e70f8e4ff2d4a84a9977b4471705179"
PINNED_ARCHIVE_SHA256 = "1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570"
SAMPLES = ("Blue_ACT", "Green_ACT")
RANGES = {"gg": [100, 402], "kg": [51, 402]}
BIAS = [1.37, 1.82]
S_MAG = [0.31, 0.47]
PCA_USER = [np.array([], float), np.array([0.23], float)]
CLEFT_VECTOR = np.array([0.71, -0.29, 0.43], float)
SHOT = [2.4e-7, 3.1e-7]
TOL = 5e-13
NSIDE = 2048


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def find_data_root(root: Path) -> Path:
    candidates = []
    for p in [root, *root.rglob("*")]:
        if p.is_dir() and all((p / q).is_dir() for q in ("bandpowers", "covariances", "aux_data")):
            candidates.append(p)
    if not candidates:
        raise FileNotFoundError("official data root not found")
    candidates.sort(key=lambda p: (len(p.parts), str(p)))
    return candidates[0]


def load_upstream_model(repo: Path):
    p = repo / "unWISExLens_lklh" / "theory_modules" / "unWISExkappa_model.py"
    source = p.read_text()
    tree = ast.parse(source, filename=str(p))
    tree.body = [n for n in tree.body if not isinstance(n, (ast.Import, ast.ImportFrom))]
    ast.fix_missing_locations(tree)
    ns = {"np": np}
    exec(compile(tree, str(p), "exec"), ns)
    return ns["unWISExLens_theory_model"], source


def load_upstream_binning(repo: Path):
    p = repo / "unWISExLens_lklh" / "auxiliary" / "binning_helpers.py"
    source = p.read_text()
    tree = ast.parse(source, filename=str(p))
    tree.body = [n for n in tree.body if not isinstance(n, (ast.Import, ast.ImportFrom))]
    ast.fix_missing_locations(tree)
    ns = {"np": np, "bin_spectrum": lambda *args, **kwargs: None}
    exec(compile(tree, str(p), "exec"), ns)
    return ns["NaMasterPowerSpectrumBinning"], source


class FakeCleft:
    def assemble_cleft_coeff(self, **kwargs):
        return CLEFT_VECTOR.copy()


def smooth(ell, phase=0.0):
    x = (np.asarray(ell, float) + 1.0) / (float(np.max(ell)) + 2.0)
    return 1.0 + 0.12 * x + 0.017 * np.sin(7.0 * x + phase)


def make_raw(ell, n_pcs, sample_index):
    n = len(ell)
    nc = n_pcs + 1
    L = len(CLEFT_VECTOR)
    f = smooth(ell, 0.4 * sample_index)
    def cols(scale, count, step):
        return scale * f[:, None] * (1.0 + step * np.arange(count)[None, :])
    kg_b = cols(2.0e-6 * (1 + 0.1 * sample_index), nc, 0.11)
    kg_nob = cols(1.1e-7, L, 0.07)
    gg_bsq = cols(3.2e-6, nc * nc, 0.035)
    gg_b = 8.0e-8 * f[:, None, None] * (1.0 + 0.06 * np.arange(nc)[None, :, None]) * (1.0 + 0.05 * np.arange(L)[None, None, :])
    gg_nob = cols(5.5e-8, L, 0.08)
    gmu_b = cols(7.2e-8, nc, 0.09)
    gmu_nob = cols(2.4e-8, L, 0.06)
    if n_pcs == 0:
        norm = np.array([1.17])
    else:
        norm = np.array([1.21, 0.08, -0.035])
    return {
        "kg": {"kg_b": kg_b, "kg_nob": kg_nob, "kmu": 3.1e-7 * f},
        "gg": {
            "gg_bsq": gg_bsq,
            "gg_b": gg_b,
            "gg_nob": gg_nob,
            "gmu_b": gmu_b,
            "gmu_nob": gmu_nob,
            "mumu": 4.3e-8 * f,
        },
        "bdndz_norm": norm,
    }


def make_noise(ell, n_cleft, phase):
    f = smooth(ell, phase)
    return {
        "kg": {"kg_b": 1.3e-8 * f},
        "gg": {
            "gg_bsq": 1.7e-8 * f,
            "gg_b": 4.0e-9 * f[:, None] * (1.0 + 0.04 * np.arange(n_cleft)[None, :]),
            "gmu_b": 3.0e-9 * f,
        },
    }


def maxdiff(a, b):
    a = np.asarray(a, float); b = np.asarray(b, float)
    if a.shape != b.shape or not (np.all(np.isfinite(a)) and np.all(np.isfinite(b))):
        return False, None, None
    d = float(np.max(np.abs(a - b))) if a.size else 0.0
    threshold = TOL * max(1.0, float(np.max(np.abs(a))) if a.size else 0.0)
    return d <= threshold, d, threshold


def load_survey(data_root, binning_cfg, Binning):
    pix = hp.pixwin(NSIDE)
    survey = {}
    for s in SAMPLES:
        ins = binning_cfg[s]
        transfer = np.asarray(np.loadtxt(data_root / "aux_data" / "transfer_functions" / ins["transfer_path"]), float)
        bw = np.load(data_root / "aux_data" / "bandwindow_matrices" / ins["bandwindow_matrix_path"], allow_pickle=True).item()
        edges = np.asarray(ins["ell_bin_edges"][: transfer.shape[0] + 1], float)
        fgg = Binning(bw["gg"]["coupling"], bw["gg"]["bandwindow"], edges, transfer_function=transfer[:, 1])
        fkg = Binning(bw["kg"]["coupling"], bw["kg"]["bandwindow"], edges, transfer_function=transfer[:, 2])
        igg = np.asarray(fgg.get_input_ells(), int)
        ikg = np.asarray(fkg.get_input_ells(), int)
        cond_gg = (RANGES["gg"][0] <= edges[:-1]) & (edges[1:] < RANGES["gg"][1])
        cond_kg = (RANGES["kg"][0] <= edges[:-1]) & (edges[1:] < RANGES["kg"][1])
        survey[s] = {"transfer": transfer, "bw": bw, "edges": edges, "fgg": fgg, "fkg": fkg, "igg": igg, "ikg": ikg, "cond_gg": cond_gg, "cond_kg": cond_kg, "pix": pix}
    return survey


def reference_survey(theory_ell, gg, kg, setup, shot):
    igg, ikg = setup["igg"], setup["ikg"]
    pix = setup["pix"]
    gg_in = np.interp(igg, theory_ell, gg) * pix[igg] ** 2
    kg_in = np.interp(ikg, theory_ell, kg) * pix[ikg]
    gg_all = setup["fgg"](gg_in, white_noise=float(shot))
    kg_all = setup["fkg"](kg_in)
    return {"gg_all": gg_all, "kg_all": kg_all, "gg_selected": gg_all[setup["cond_gg"]], "kg_selected": kg_all[setup["cond_kg"]]}


def dsir_survey(theory_ell, gg, kg, setup, shot):
    igg, ikg = setup["igg"], setup["ikg"]
    if not np.array_equal(igg, ikg):
        raise RuntimeError("Exp066B prereg assumes the released ACT gg/kg NaMaster input-ell grids are identical")
    ell_in = igg
    return selected_survey_bandpowers(
        np.interp(ell_in, theory_ell, gg), np.interp(ell_in, theory_ell, kg),
        coupling_gg=setup["bw"]["gg"]["coupling"], bandwindow_gg=setup["bw"]["gg"]["bandwindow"],
        coupling_kg=setup["bw"]["kg"]["coupling"], bandwindow_kg=setup["bw"]["kg"]["bandwindow"],
        transfer_gg=setup["transfer"][:, 1], transfer_kg=setup["transfer"][:, 2],
        pixwin=setup["pix"][ell_in], select_gg=setup["cond_gg"], select_kg=setup["cond_kg"], shot_noise=float(shot),
    )


def changed(a, b):
    return bool(np.max(np.abs(np.asarray(a) - np.asarray(b))) > 1e-15)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--external-repo", required=True)
    ap.add_argument("--archive", required=True)
    ap.add_argument("--extracted-root", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    repo = Path(args.external_repo).resolve()
    archive = Path(args.archive).resolve()
    data_root = find_data_root(Path(args.extracted_root).resolve())
    outpath = Path(args.output).resolve()
    commit = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    digest = sha256(archive)

    UpstreamModel, model_source = load_upstream_model(repo)
    Binning, bin_source = load_upstream_binning(repo)
    lklh_source = (repo / "unWISExLens_lklh" / "unWISExLensLklh.py").read_text()
    cfg = yaml.safe_load((repo / "unWISExLens_lklh" / "config_files" / "binning_setup.yaml").read_text())
    survey = load_survey(data_root, cfg, Binning)

    # Use the exact released input ell support as the common synthetic theory grid.
    ell_parts = []
    for s in SAMPLES:
        ell_parts.extend([survey[s]["igg"], survey[s]["ikg"]])
    ell = np.sort(np.unique(np.concatenate(ell_parts))).astype(float)

    raw = [make_raw(ell, 0, 0), make_raw(ell, 2, 1)]
    noise = [make_noise(ell, len(CLEFT_VECTOR), 0.2), make_noise(ell, len(CLEFT_VECTOR), 0.6)]

    fake = FakeCleft()
    up = UpstreamModel(cleft_interp_helper=fake, ell_vals=ell, want_gg_cross=False)
    ref_gg, ref_kg = up.evaluate(
        raw, get="all", want_gg_cross=False, noise_bias=noise,
        bias=BIAS, s_mag=S_MAG, pca_coeff=PCA_USER, do_dndz_pca=True,
        cleft_coeff=[{}, {}],
    )

    dsir_combined = [
        combine_raw_components(raw[i], bias=BIAS[i], s_mag=S_MAG[i], cleft_coeff=CLEFT_VECTOR,
                               pca_coeff=PCA_USER[i], noise_bias=noise[i], do_dndz_pca=True)
        for i in range(2)
    ]

    nuisance_records = {}
    nuisance_pass = True
    for i, s in enumerate(SAMPLES):
        okgg, dgg, tgg = maxdiff(ref_gg[i], dsir_combined[i]["gg"])
        okkg, dkg, tkg = maxdiff(ref_kg[i], dsir_combined[i]["kg"])
        nuisance_pass &= okgg and okkg
        nuisance_records[s] = {"gg": {"pass": okgg, "max_abs_difference": dgg, "threshold": tgg}, "kg": {"pass": okkg, "max_abs_difference": dkg, "threshold": tkg}, "pca_coeff_final": dsir_combined[i]["pca_coeff_final"].tolist(), "normalized_bias": dsir_combined[i]["normalized_bias"]}

    survey_records = {}
    survey_pass = True
    baseline = {}
    for i, s in enumerate(SAMPLES):
        ref = reference_survey(ell, ref_gg[i], ref_kg[i], survey[s], SHOT[i])
        ds = dsir_survey(ell, dsir_combined[i]["gg"], dsir_combined[i]["kg"], survey[s], SHOT[i])
        r = {}
        for key in ("gg_all", "kg_all", "gg_selected", "kg_selected"):
            ok, d, t = maxdiff(ref[key], ds[key])
            survey_pass &= ok
            r[key] = {"pass": ok, "max_abs_difference": d, "threshold": t, "shape": list(np.asarray(ds[key]).shape)}
        counts_ok = len(ds["gg_selected"]) == 6 and len(ds["kg_selected"]) == 7
        survey_pass &= counts_ok
        r["selected_counts"] = {"gg": len(ds["gg_selected"]), "kg": len(ds["kg_selected"]), "pass": counts_ok}
        survey_records[s] = r
        baseline[s] = ds

    # Frozen locality/sensitivity controls on the DSIR closure path.
    # 1) Green shot noise only.
    shot_changed = dsir_survey(ell, dsir_combined[1]["gg"], dsir_combined[1]["kg"], survey["Green_ACT"], SHOT[1] * 1.1)
    c_shot = changed(baseline["Green_ACT"]["gg_selected"], shot_changed["gg_selected"]) and not changed(baseline["Green_ACT"]["kg_selected"], shot_changed["kg_selected"])

    # 2) Green kg_nob only.
    raw_kg = deepcopy(raw[1]); raw_kg["kg"]["kg_nob"] = raw_kg["kg"]["kg_nob"] * 1.1
    comb_kg = combine_raw_components(raw_kg, bias=BIAS[1], s_mag=S_MAG[1], cleft_coeff=CLEFT_VECTOR, pca_coeff=PCA_USER[1], noise_bias=noise[1])
    surv_kg = dsir_survey(ell, comb_kg["gg"], comb_kg["kg"], survey["Green_ACT"], SHOT[1])
    c_kg = changed(baseline["Green_ACT"]["kg_selected"], surv_kg["kg_selected"]) and not changed(baseline["Green_ACT"]["gg_selected"], surv_kg["gg_selected"])

    # 3) Blue mumu only.
    raw_mu = deepcopy(raw[0]); raw_mu["gg"]["mumu"] = raw_mu["gg"]["mumu"] * 1.1
    comb_mu = combine_raw_components(raw_mu, bias=BIAS[0], s_mag=S_MAG[0], cleft_coeff=CLEFT_VECTOR, pca_coeff=PCA_USER[0], noise_bias=noise[0])
    surv_mu = dsir_survey(ell, comb_mu["gg"], comb_mu["kg"], survey["Blue_ACT"], SHOT[0])
    c_mu = changed(baseline["Blue_ACT"]["gg_selected"], surv_mu["gg_selected"]) and not changed(baseline["Blue_ACT"]["kg_selected"], surv_mu["kg_selected"])

    # 4) Green PCA user coefficient only; Blue closure is not recomputed and is invariant by construction.
    comb_pca = combine_raw_components(raw[1], bias=BIAS[1], s_mag=S_MAG[1], cleft_coeff=CLEFT_VECTOR, pca_coeff=np.array([0.31]), noise_bias=noise[1])
    surv_pca = dsir_survey(ell, comb_pca["gg"], comb_pca["kg"], survey["Green_ACT"], SHOT[1])
    c_pca = changed(baseline["Green_ACT"]["gg_selected"], surv_pca["gg_selected"]) and changed(baseline["Green_ACT"]["kg_selected"], surv_pca["kg_selected"])
    sensitivity = {"shot_noise_local_to_gg": c_shot, "kg_nob_local_to_kg": c_kg, "mumu_local_to_gg": c_mu, "green_pca_changes_green_gg_and_kg_only": c_pca}
    sensitivity_pass = all(sensitivity.values())

    source_tokens = {
        "bias_normalization": "b /= np.dot(raw_spectra[i]['bdndz_norm'], pca_coeff_final)" in model_source,
        "kg_cleft": "raw_spectra['kg']['kg_nob']" in model_source,
        "magnification": "(5 * s - 2)" in model_source,
        "gg_pca_outer": "np.outer(pca_coeff, pca_coeff).flatten()" in model_source,
        "namaster_decoupling": "bandpower_windows@np.linalg.inv(self.__coupling_matrix)" in bin_source,
        "transfer_after_bin": "return self.bin(cells, white_noise=white_noise) * self.__transfer" in bin_source,
        "gg_pixwin_then_bin": "_pixwin_correction_gg" in lklh_source and "white_noise=n_shot_list[i]" in lklh_source,
        "kg_pixwin_then_bin": "_pixwin_correction_kg" in lklh_source,
        "released_transfer_columns": "transfer_function=transfer_function[:, 1]" in lklh_source and "transfer_function=transfer_function[:, 2]" in lklh_source,
    }
    source_pass = all(source_tokens.values())
    provenance_pass = commit == PINNED_COMMIT and digest == PINNED_ARCHIVE_SHA256

    passed = provenance_pass and source_pass and nuisance_pass and survey_pass and sensitivity_pass
    status = "PASS_ACT_UNWISE_NUISANCE_SURVEY_CLOSURE_V0_1" if passed else "FAIL_ACT_UNWISE_NUISANCE_SURVEY_CLOSURE_V0_1"
    result = {
        "experiment": "Exp066B",
        "status": status,
        "scope": "synthetic algebraic nuisance/CLEFT plus released survey-operator closure; no data fit and no dark-sector response",
        "pinned_commit": commit,
        "archive_sha256": digest,
        "frozen": {"bias": BIAS, "s_mag": S_MAG, "green_pca_user": [0.23], "cleft_vector": CLEFT_VECTOR.tolist(), "shot_noise": SHOT, "nside": NSIDE, "tolerance": TOL, "cuts": RANGES},
        "checks": {"provenance": provenance_pass, "source_contract": {"pass": source_pass, **source_tokens}, "nuisance_combination": {"pass": nuisance_pass, "samples": nuisance_records}, "survey_operator": {"pass": survey_pass, "samples": survey_records}, "sensitivity": {"pass": sensitivity_pass, **sensitivity}},
        "selected_dimension": 26,
        "next_step": "If PASS, run one fixed reference-cosmology end-to-end backend regression before preregistering any G7 relation.",
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    outpath.parent.mkdir(parents=True, exist_ok=True)
    outpath.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
