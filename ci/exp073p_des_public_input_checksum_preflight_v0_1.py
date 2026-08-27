#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import urllib.error
import urllib.request
from pathlib import Path

PIN = "7bde066626f66cd7bbe79cc46224d2342840e463"
PARENT_STATUS = "PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O"
MAX_DOWNLOAD_BYTES = 200 * 1024 * 1024

OBJECTS = [
    {
        "name": "DES_Y1A1_3x2pt_redMaGiC_zerr_CATALOG.fits",
        "url": "https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/redmagic/DES_Y1A1_3x2pt_redMaGiC_zerr_CATALOG.fits",
    },
    {
        "name": "DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits",
        "url": "https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/redmagic/DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits",
    },
    {
        "name": "mcal-y1a1-combined-riz-unblind-v4-matched.fits",
        "url": "https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/shear_catalogs/mcal-y1a1-combined-riz-unblind-v4-matched.fits",
    },
    {
        "name": "y1_source_redshift_binning_v1.fits",
        "url": "https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/redshift_bins/y1_source_redshift_binning_v1.fits",
    },
    {
        "name": "y1_redshift_distributions_v1.fits",
        "url": "https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/redshift_bins/y1_redshift_distributions_v1.fits",
    },
    {
        "name": "2pt_NG_mcal_1110.fits",
        "url": "https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/chains/2pt_NG_mcal_1110.fits",
    },
]

SOURCE_PATHS = [
    "cosmotheka/mappers/mapper_DESY1gc.py",
    "cosmotheka/mappers/mapper_DESY1wl.py",
    "cosmotheka/cls/cl.py",
    "input/DESY1_eBOSS_P18CMBK.yml",
]


def git_head(root: Path) -> str:
    return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def probe(url: str):
    headers = None
    status = None
    final_url = None
    err = None
    for method, extra in (("HEAD", {}), ("GET", {"Range": "bytes=0-0"})):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": "DSIR-Exp073P/0.1", **extra})
            with urllib.request.urlopen(req, timeout=60) as r:
                headers = dict(r.headers.items())
                status = getattr(r, "status", None)
                final_url = r.geturl()
                if method == "GET":
                    r.read(1)
                break
        except Exception as e:
            err = f"{type(e).__name__}: {e}"
    size = None
    if headers:
        cl = headers.get("Content-Length") or headers.get("content-length")
        cr = headers.get("Content-Range") or headers.get("content-range")
        if cr and "/" in cr:
            try:
                size = int(cr.rsplit("/", 1)[1])
            except Exception:
                pass
        if size is None and cl:
            try:
                size = int(cl)
            except Exception:
                pass
    return status, final_url, headers or {}, size, err


def download_and_hash(url: str, dest: Path):
    h = hashlib.sha256()
    n = 0
    req = urllib.request.Request(url, headers={"User-Agent": "DSIR-Exp073P/0.1"})
    with urllib.request.urlopen(req, timeout=120) as r, dest.open("wb") as f:
        while True:
            chunk = r.read(1 << 20)
            if not chunk:
                break
            n += len(chunk)
            if n > MAX_DOWNLOAD_BYTES:
                raise RuntimeError("download exceeded frozen preflight cap")
            h.update(chunk)
            f.write(chunk)
    return n, h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cosmotheka-root", required=True)
    ap.add_argument("--parent", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--download-dir", required=True)
    args = ap.parse_args()

    root = Path(args.cosmotheka_root)
    parent_path = Path(args.parent)
    out = Path(args.output)
    dl = Path(args.download_dir)
    dl.mkdir(parents=True, exist_ok=True)

    parent = json.loads(parent_path.read_text())
    parent_ok = parent.get("status") == PARENT_STATUS
    pin_ok = git_head(root) == PIN
    source_records = []
    for rel in SOURCE_PATHS:
        p = root / rel
        source_records.append({
            "path": rel,
            "exists": p.is_file(),
            "sha256": sha256_file(p) if p.is_file() else None,
        })
    source_ok = all(x["exists"] for x in source_records)

    cfg = (root / "input/DESY1_eBOSS_P18CMBK.yml").read_text(errors="replace") if source_ok else ""
    config_names_ok = all(o["name"] in cfg for o in OBJECTS)

    records = []
    for obj in OBJECTS:
        status, final_url, headers, size, error = probe(obj["url"])
        rec = {
            **obj,
            "http_status": status,
            "final_url": final_url,
            "content_length": size,
            "last_modified": headers.get("Last-Modified") or headers.get("last-modified"),
            "etag": headers.get("ETag") or headers.get("etag"),
            "probe_error": error,
            "downloaded": False,
            "downloaded_bytes": None,
            "sha256": None,
            "checksum_bound": False,
        }
        if status is not None and size is not None and size <= MAX_DOWNLOAD_BYTES:
            try:
                dest = dl / obj["name"]
                n, digest = download_and_hash(obj["url"], dest)
                rec.update(downloaded=True, downloaded_bytes=n, sha256=digest, checksum_bound=(n == size))
                dest.unlink(missing_ok=True)
            except Exception as e:
                rec["download_error"] = f"{type(e).__name__}: {e}"
        elif size is not None and size > MAX_DOWNLOAD_BYTES:
            rec["checksum_block_reason"] = "public object exceeds implementation-only 200 MiB preflight download cap; Exp073P support fractions remain forbidden until an immutable checksum source or byte-identical smaller derived release is prospectively bound"
        records.append(rec)

    all_reachable = all(r["http_status"] is not None and r["content_length"] is not None for r in records)
    all_checksum_bound = all(r["checksum_bound"] for r in records)
    support_evaluation_authorized = bool(parent_ok and pin_ok and source_ok and config_names_ok and all_checksum_bound)
    status = (
        "READY_FOR_EXP073P_SUPPORT_IMPLEMENTATION"
        if support_evaluation_authorized
        else "BLOCKED_PRE_SUPPORT_INPUT_CHECKSUM_BINDING_EXP073P_PREFLIGHT"
    )

    result = {
        "experiment": "Exp073P-preflight",
        "date": "2026-08-27",
        "status": status,
        "scientific_classification": None,
        "support_fraction_evaluated": False,
        "retained_dimension_evaluated": False,
        "frozen_parent": {"status_expected": PARENT_STATUS, "status_observed": parent.get("status"), "pass": parent_ok},
        "cosmotheka": {"expected_pin": PIN, "observed_pin": git_head(root), "pass": pin_ok, "source_records": source_records, "config_names_pass": config_names_ok},
        "public_objects": records,
        "all_reachable_with_size": all_reachable,
        "all_checksum_bound": all_checksum_bound,
        "support_evaluation_authorized": support_evaluation_authorized,
        "frozen_contract_preserved": {
            "z_min": 0.295,
            "z_max": 2.33,
            "k_max_Mpc^-1": 0.06664762008318016,
            "f_invalid_max": 0.05,
            "minimum_retained_dimension": 15,
            "nside_classifying": 4096,
            "covariance_read": False,
            "nuisance_read": False,
            "relation_null_read": False,
            "G8_read": False,
        },
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "next_admissible_step": "Resolve exact checksum binding for every large public DES object without changing the frozen Exp073P operator/threshold. No support fraction may be evaluated before P2 is complete.",
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": status,
        "all_reachable_with_size": all_reachable,
        "all_checksum_bound": all_checksum_bound,
        "support_evaluation_authorized": support_evaluation_authorized,
        "objects": [{"name": r["name"], "size": r["content_length"], "checksum_bound": r["checksum_bound"]} for r in records],
    }, indent=2))


if __name__ == "__main__":
    main()
