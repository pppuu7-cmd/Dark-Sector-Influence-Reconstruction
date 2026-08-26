#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import numpy as np
import yaml

PINNED_COMMIT = "6302c30d9e70f8e4ff2d4a84a9977b4471705179"
PINNED_CODE_VERSION = "1.0.2"
PINNED_DATA_VERSION = "1.0"
SAMPLES = ("Blue_ACT", "Green_ACT")


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
        raise FileNotFoundError("no directory contains bandpowers/, covariances/, aux_data/")
    candidates.sort(key=lambda p: (len(p.parts), str(p)))
    return candidates[0]


def finite_matrix(path: Path) -> np.ndarray:
    x = np.asarray(np.loadtxt(path), dtype=float)
    if x.ndim != 2 or not np.all(np.isfinite(x)):
        raise ValueError(f"non-finite/non-matrix data: {path}")
    return x


def pd_stats(x: np.ndarray) -> dict:
    sym = bool(np.allclose(x, x.T, rtol=1e-10, atol=1e-12))
    eig = np.linalg.eigvalsh((x + x.T) / 2.0)
    return {
        "shape": list(x.shape),
        "symmetric": sym,
        "lambda_min": float(eig[0]),
        "lambda_max": float(eig[-1]),
        "positive_definite": bool(sym and eig[0] > 0.0),
        "condition_eig_ratio": float(eig[-1] / eig[0]) if eig[0] > 0 else None,
    }


def discover_redshift_files(aux: Path) -> list[str]:
    out = []
    for p in aux.rglob("*"):
        if not p.is_file():
            continue
        s = p.name.lower()
        if ("dndz" in s or "redshift" in s or re.search(r"(^|[_-])nz([_.-]|$)", s)):
            out.append(str(p.relative_to(aux)))
    return sorted(set(out))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--external-repo", required=True)
    ap.add_argument("--extracted-root", required=True)
    ap.add_argument("--archive", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    repo = Path(args.external_repo).resolve()
    extracted = Path(args.extracted_root).resolve()
    archive = Path(args.archive).resolve()
    outpath = Path(args.output).resolve()
    checks: dict[str, dict] = {}

    # Exact external source provenance.
    git_head = (repo / ".git" / "HEAD").read_text().strip() if (repo / ".git" / "HEAD").exists() else ""
    import subprocess
    commit = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    checks["pinned_git_commit"] = {"pass": commit == PINNED_COMMIT, "observed": commit, "expected": PINNED_COMMIT, "git_HEAD": git_head}

    init_text = (repo / "unWISExLens_lklh" / "__init__.py").read_text()
    m_code = re.search(r'__version__\s*=\s*[\"\']([^\"\']+)', init_text)
    m_data = re.search(r'__data_version__\s*=\s*[\"\']([^\"\']+)', init_text)
    code_version = m_code.group(1) if m_code else None
    data_version = m_data.group(1) if m_data else None
    checks["declared_versions"] = {
        "pass": code_version == PINNED_CODE_VERSION and data_version == PINNED_DATA_VERSION,
        "code_version": code_version,
        "data_version": data_version,
        "expected_code": PINNED_CODE_VERSION,
        "expected_data": PINNED_DATA_VERSION,
    }

    archive_digest = sha256(archive)
    data_root = find_data_root(extracted)
    checks["data_root"] = {"pass": True, "path": str(data_root), "archive_sha256": archive_digest}

    cfg = repo / "unWISExLens_lklh" / "config_files"
    data_names = yaml.safe_load((cfg / "data_filenames.yaml").read_text())
    cov_names = yaml.safe_load((cfg / "covmat_filenames_cmbmarg.yaml").read_text())
    binning = yaml.safe_load((cfg / "binning_setup.yaml").read_text())

    bp_summary = {}
    bp_pass = True
    for s in SAMPLES:
        p = data_root / "bandpowers" / data_names[s]
        try:
            d = finite_matrix(p)
            ok = d.shape[1] >= 4 and d.shape[0] >= 2 and bool(np.all(np.diff(d[:, 0]) > 0))
            bp_pass &= ok
            bp_summary[s] = {
                "path": str(p.relative_to(data_root)),
                "shape": list(d.shape),
                "ell_min": float(d[0, 0]),
                "ell_max": float(d[-1, 0]),
                "strictly_increasing_ell": bool(np.all(np.diff(d[:, 0]) > 0)),
                "columns_at_least_4": bool(d.shape[1] >= 4),
                "gg_nonzero_count": int(np.count_nonzero(d[:, 1])),
                "kg_nonzero_count": int(np.count_nonzero(d[:, 3])),
                "pass": bool(ok),
            }
        except Exception as e:
            bp_pass = False
            bp_summary[s] = {"path": str(p), "pass": False, "error": repr(e)}
    checks["bandpowers_gg_kg"] = {"pass": bool(bp_pass), "samples": bp_summary}

    covs = {}
    cov_pass = True
    loaded = {}
    for s in SAMPLES:
        p = data_root / "covariances" / cov_names[s]
        try:
            c = finite_matrix(p)
            st = pd_stats(c)
            loaded[s] = c
            covs[s] = {"path": str(p.relative_to(data_root)), **st}
            cov_pass &= st["positive_definite"]
        except Exception as e:
            cov_pass = False
            covs[s] = {"path": str(p), "positive_definite": False, "error": repr(e)}

    cross_key = "Blue_ACT_X_Green_ACT"
    cp = data_root / "covariances" / cov_names[cross_key]
    try:
        x = finite_matrix(cp)
        shape_ok = "Blue_ACT" in loaded and "Green_ACT" in loaded and x.shape == (loaded["Blue_ACT"].shape[0], loaded["Green_ACT"].shape[0])
        cross_rec = {"path": str(cp.relative_to(data_root)), "shape": list(x.shape), "shape_compatible": bool(shape_ok)}
        cov_pass &= bool(shape_ok)
        if shape_ok:
            combined = np.block([[loaded["Blue_ACT"], x], [x.T, loaded["Green_ACT"]]])
            combined_stats = pd_stats(combined)
            cov_pass &= combined_stats["positive_definite"]
        else:
            combined_stats = {"positive_definite": False}
    except Exception as e:
        cov_pass = False
        cross_rec = {"path": str(cp), "shape_compatible": False, "error": repr(e)}
        combined_stats = {"positive_definite": False}
    checks["covariance_binding"] = {"pass": bool(cov_pass), "samples": covs, "cross": cross_rec, "combined": combined_stats}

    # Exact band-window and transfer operators selected by the pinned ACT config.
    operator_pass = True
    operator = {"samples": {}}
    for s in SAMPLES:
        rec = binning[s]
        tr = data_root / "aux_data" / "transfer_functions" / rec["transfer_path"]
        bw = data_root / "aux_data" / "bandwindow_matrices" / rec["bandwindow_matrix_path"]
        srec = {"transfer": str(tr.relative_to(data_root)), "bandwindow": str(bw.relative_to(data_root))}
        try:
            t = finite_matrix(tr)
            tok = t.shape[1] >= 3 and t.shape[0] >= 2
            srec["transfer_shape"] = list(t.shape)
            srec["transfer_columns_at_least_3"] = bool(tok)
            operator_pass &= bool(tok)
        except Exception as e:
            operator_pass = False
            srec["transfer_error"] = repr(e)
        try:
            obj = np.load(bw, allow_pickle=True).item()
            detail = {}
            bok = True
            for ch in ("gg", "kg"):
                bok &= ch in obj
                detail[ch] = {}
                if ch in obj:
                    for key in ("coupling", "bandwindow"):
                        bok &= key in obj[ch]
                        if key in obj[ch]:
                            a = np.asarray(obj[ch][key], dtype=float)
                            finite = bool(a.ndim == 2 and np.all(np.isfinite(a)))
                            bok &= finite
                            detail[ch][key] = {"shape": list(a.shape), "finite_matrix": finite}
            srec["bandwindow_detail"] = detail
            srec["bandwindow_pass"] = bool(bok)
            operator_pass &= bool(bok)
        except Exception as e:
            operator_pass = False
            srec["bandwindow_error"] = repr(e)
        operator["samples"][s] = srec
    operator["pass"] = bool(operator_pass)
    checks["bandwindow_transfer_operators"] = operator

    redshift_files = discover_redshift_files(data_root / "aux_data")
    checks["redshift_auxiliary"] = {
        "pass": len(redshift_files) >= 2,
        "count": len(redshift_files),
        "files": redshift_files[:100],
    }

    source = (repo / "unWISExLens_lklh" / "unWISExLensLklh.py").read_text()
    source_tests = {
        "loads_gg_column": "_data_gg.append(data[ell_selection_gg, 1])" in source,
        "loads_kg_column": "_data_kg.append(data[ell_selection_kg, 3])" in source,
        "loads_cross_covariance": "cross_cov = select_from_matrix" in source,
        "warns_missing_cross_covariance": "Cross covariance between" in source,
    }
    checks["likelihood_source_contract"] = {"pass": all(source_tests.values()), **source_tests}

    failures = [k for k, v in checks.items() if not bool(v.get("pass"))]
    status = "PASS_ACT_UNWISE_OBSERVATIONAL_BINDING_ELIGIBLE_V0_1" if not failures else "FAIL_ACT_UNWISE_OBSERVATIONAL_BINDING_ELIGIBILITY_V0_1"
    summary = {
        "experiment": "Exp065A",
        "status": status,
        "pinned_external_repo": "ACTCollaboration/unWISExLens_lklh",
        "pinned_commit": PINNED_COMMIT,
        "archive_sha256": archive_digest,
        "checks": checks,
        "failures": failures,
        "interpretation": "Eligibility/provenance only; no DSIR law search or theory-family response evaluated.",
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    outpath.parent.mkdir(parents=True, exist_ok=True)
    outpath.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
