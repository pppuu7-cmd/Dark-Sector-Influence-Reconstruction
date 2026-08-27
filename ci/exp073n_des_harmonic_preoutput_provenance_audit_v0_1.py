#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

PIN = "21e589a3cfc3e30f1b06a4636ccc2da8aceda5ab"
PARENT = "FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M"
FAIL = "FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def head(root: Path) -> str:
    return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--operator-root", required=True)
    ap.add_argument("--output", required=True)
    a = ap.parse_args()
    root = Path(a.operator_root)
    out = Path(a.output)

    ggl = root / "ggltest.py"
    y1_cfg = root / "etc/y1mcal_csh.yml"
    ell = root / "etc/binNicola2020.txt"
    y3_cfgs = sorted(p.name for p in (root / "etc").glob("y3*.yml"))
    ggl_text = ggl.read_text()
    y1_text = y1_cfg.read_text()

    checks = {
        "operator_pin_exact": head(root) == PIN,
        "ggl_blob_present": ggl.is_file(),
        "y1_ww_config_present": y1_cfg.is_file(),
        "finite_ell_edges_present": ell.is_file(),
        "y3_configs_are_flask_only": bool(y3_cfgs) and all("flask" in x.lower() for x in y3_cfgs),
        "no_public_y3_real_data_ggl_config_at_pin": not any(
            p.name.startswith("y3") and "flask" not in p.name.lower()
            for p in (root / "etc").glob("*.yml")
        ),
        "ggl_execution_is_flask_only": (
            'if conf["type"] == "flask"' in ggl_text
            and "raise NotImplementedError" in ggl_text
        ),
        "y1_config_uses_site_local_absolute_inputs": "/global/cscratch1/" in y1_text,
    }

    # Exp073N section 3 requires exact public files/workspaces or reproducible masks
    # to be bound before any support output. The frozen operator repository contains
    # no real-data Y3 GGL configuration and the frozen GGL driver only executes the
    # FLASK branch. Therefore the exact Y3 Wm workspace/input realization used in
    # the published analysis cannot be reproduced from the frozen public source.
    exact_y3_wm_reproduction = False
    support_output_evaluated = False
    status = FAIL

    result = {
        "experiment": "Exp073N",
        "audit": "pre-output-source-provenance-v0.1",
        "date": "2026-08-27",
        "status": status,
        "parent_exp073m": PARENT,
        "operator_repository": "hocamachoc/3x2hs_measurements",
        "operator_pin": PIN,
        "operator_head": head(root),
        "checks": checks,
        "inventory": {
            "y3_yaml_configs": y3_cfgs,
            "ggltest_sha256": sha256(ggl),
            "y1mcal_csh_sha256": sha256(y1_cfg),
            "binNicola2020_sha256": sha256(ell),
        },
        "exact_y3_wm_real_data_operator_reproducible_from_frozen_public_source": exact_y3_wm_reproduction,
        "support_output_evaluated": support_output_evaluated,
        "support_fraction": None,
        "retained_dimension": None,
        "interpretation": (
            "Frozen public operator source lacks a real-data DES Y3 GGL configuration at the pinned commit; "
            "the public ggltest.py execution path is FLASK-only. Exp073N mandatory pre-output binding therefore "
            "cannot reproduce the exact published Y3 Wm NaMaster workspace/input realization. This is a "
            "reproduction/provenance classification, not a 5% physical-support scientific FAIL."
        ),
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "downstream_authorized": False,
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
