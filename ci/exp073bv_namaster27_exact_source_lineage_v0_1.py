#!/usr/bin/env python3
import hashlib
import importlib
import importlib.metadata
import json
import os
from pathlib import Path
import re
import subprocess
import traceback

OUT = Path("data/derived/g7/exp073bv_namaster27_exact_source_lineage_result_v0_1.json")
UPSTREAM = Path(os.environ.get("NAMASTER_V27_SOURCE", "upstream_namaster_v27")).resolve()
EXPECTED_HEAD = "24365fa59a38c15732f4f37e8b29265b75c442d5"


def sha256_file(path: Path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def run_capture(cmd):
    try:
        p = subprocess.run(cmd, text=True, capture_output=True, check=False)
        return {
            "ok": True,
            "cmd": cmd,
            "returncode": p.returncode,
            "stdout": p.stdout,
            "stderr": p.stderr,
        }
    except Exception as e:
        return {"ok": False, "cmd": cmd, "error": repr(e)}


receipt = {
    "experiment": "Exp073BV",
    "classification": "NONCLASSIFYING_SOURCE_LINEAGE_IMPLEMENTATION_PROVENANCE_DIAGNOSTIC",
    "authority": False,
    "scientific_pass_claimed": False,
    "scientific_readiness_increment": 0,
    "draft_data_readiness_increment": 0,
    "Exp073AQ_preserved_as_FAIL": True,
    "Exp073BJ_preserved_as_PASS": True,
    "Exp073BD_provisional_forbidden_downstream": True,
    "bv_prereg_commit": "d71f8715c9b680c2cf80226853366b9803853a7e",
    "expected_upstream_commit": EXPECTED_HEAD,
    "probes": {},
    "status": "BV_Q5_DIAGNOSTIC_INCOMPLETE",
}

try:
    probes = receipt["probes"]

    # 1. Installed version/package path.
    try:
        version = importlib.metadata.version("pymaster")
        pymaster = importlib.import_module("pymaster")
        probes["installed_package"] = {
            "ok": True,
            "version": version,
            "pymaster_file": str(Path(pymaster.__file__).resolve()),
        }
    except Exception as e:
        version = None
        pymaster = None
        probes["installed_package"] = {"ok": False, "error": repr(e)}

    # 2-3. Correct runtime extension/wrapper relationship.
    ext = None
    wrapper = None
    try:
        ext = importlib.import_module("_nmtlib")
        probes["top_level_extension"] = {
            "ok": True,
            "module_name": ext.__name__,
            "file": str(Path(ext.__file__).resolve()),
        }
    except Exception as e:
        probes["top_level_extension"] = {"ok": False, "error": repr(e)}

    try:
        wrapper = importlib.import_module("pymaster.nmtlib")
        wrapper_low = getattr(wrapper, "_nmtlib", None)
        probes["pymaster_nmtlib_wrapper"] = {
            "ok": True,
            "module_name": wrapper.__name__,
            "file": str(Path(wrapper.__file__).resolve()),
            "has__nmtlib_attr": wrapper_low is not None,
            "same_extension_object": bool(ext is not None and wrapper_low is ext),
            "wrapped_extension_name": getattr(wrapper_low, "__name__", None),
            "wrapped_extension_file": str(Path(wrapper_low.__file__).resolve()) if getattr(wrapper_low, "__file__", None) else None,
        }
    except Exception as e:
        probes["pymaster_nmtlib_wrapper"] = {"ok": False, "error": repr(e)}

    # 4. Exact installed/upstream SWIG-wrapper byte identity.
    try:
        installed_wrapper = Path(wrapper.__file__).resolve()
        upstream_wrapper = UPSTREAM / "pymaster" / "nmtlib.py"
        sha_inst = sha256_file(installed_wrapper)
        sha_up = sha256_file(upstream_wrapper)
        probes["wrapper_byte_identity"] = {
            "ok": True,
            "installed_path": str(installed_wrapper),
            "upstream_path": str(upstream_wrapper),
            "installed_sha256": sha_inst,
            "upstream_sha256": sha_up,
            "byte_equal": installed_wrapper.read_bytes() == upstream_wrapper.read_bytes(),
        }
    except Exception as e:
        probes["wrapper_byte_identity"] = {"ok": False, "error": repr(e)}

    # 5-6. Immutable upstream commit and frozen topology predicates.
    head_probe = run_capture(["git", "-C", str(UPSTREAM), "rev-parse", "HEAD"])
    probes["upstream_head"] = head_probe
    head = head_probe.get("stdout", "").strip() if head_probe.get("returncode") == 0 else None
    probes["upstream_head"]["value"] = head
    probes["upstream_head"]["exact_match"] = (head == EXPECTED_HEAD)

    try:
        field_text = (UPSTREAM / "pymaster" / "field.py").read_text()
        wrapper_text = (UPSTREAM / "pymaster" / "nmtlib.py").read_text()
        setup_text = (UPSTREAM / "setup.py").read_text()
        make_text = (UPSTREAM / "Makefile.am").read_text()
        utils_text = (UPSTREAM / "src" / "utils.c").read_text()

        topology = {
            "field_imports_pymaster_nmtlib": "from pymaster import nmtlib as lib" in field_text,
            "wrapper_imports_top_level__nmtlib": bool(re.search(r"(?m)^\s*import\s+_nmtlib\s*$", wrapper_text)),
            "setup_builds_top_level__nmtlib": bool(re.search(r"Extension\(\s*[\"']_nmtlib[\"']", setup_text)),
            "setup_links_libnmt_archive": "./_deps/lib/libnmt.a" in setup_text,
            "makefile_libnmt_includes_utils_c": "libnmt_la_SOURCES" in make_text and "src/utils.c" in make_text,
            "utils_defines_drc3jj": bool(re.search(r"\bint\s+drc3jj\s*\(", utils_text)),
        }
        topology["all_frozen_predicates"] = all(topology.values())
        probes["upstream_source_topology"] = {"ok": True, **topology}
    except Exception as e:
        probes["upstream_source_topology"] = {"ok": False, "error": repr(e)}

    # 7. Best-effort runtime symbol-table evidence. Not classifying by itself.
    if ext is not None and getattr(ext, "__file__", None):
        ext_path = str(Path(ext.__file__).resolve())
        probes["runtime_symbol_tables"] = {
            "nm_all": run_capture(["nm", "-a", ext_path]),
            "nm_dynamic": run_capture(["nm", "-D", ext_path]),
            "readelf_symbols": run_capture(["readelf", "-Ws", ext_path]),
        }
        for key, val in probes["runtime_symbol_tables"].items():
            text = (val.get("stdout", "") + "\n" + val.get("stderr", ""))
            val["contains_drc3jj"] = "drc3jj" in text
    else:
        probes["runtime_symbol_tables"] = {"ok": False, "error": "runtime extension path unresolved"}

    version_ok = version == "2.7" or (isinstance(version, str) and version.startswith("2.7."))
    runtime_ok = (
        probes.get("top_level_extension", {}).get("ok") is True
        and probes.get("pymaster_nmtlib_wrapper", {}).get("ok") is True
        and probes.get("pymaster_nmtlib_wrapper", {}).get("same_extension_object") is True
    )
    upstream_exact = probes.get("upstream_head", {}).get("exact_match") is True
    topology_ok = probes.get("upstream_source_topology", {}).get("all_frozen_predicates") is True
    wrapper_probe_ok = probes.get("wrapper_byte_identity", {}).get("ok") is True
    wrapper_equal = probes.get("wrapper_byte_identity", {}).get("byte_equal") is True

    if version_ok and runtime_ok and upstream_exact and topology_ok and wrapper_probe_ok and wrapper_equal:
        receipt["status"] = "BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED"
    elif version_ok and runtime_ok and upstream_exact and topology_ok and wrapper_probe_ok and not wrapper_equal:
        receipt["status"] = "BV_Q2_SOURCE_TOPOLOGY_CONFIRMED_WRAPPER_BYTES_DIFFER"
    elif upstream_exact and topology_ok and not runtime_ok:
        receipt["status"] = "BV_Q3_RUNTIME_LAYOUT_INCOMPLETE"
    elif upstream_exact and probes.get("upstream_source_topology", {}).get("ok") is True and not topology_ok:
        receipt["status"] = "BV_Q4_UPSTREAM_TOPOLOGY_MISMATCH"
    else:
        receipt["status"] = "BV_Q5_DIAGNOSTIC_INCOMPLETE"

except Exception as e:
    receipt["top_level_error"] = repr(e)
    receipt["top_level_traceback"] = traceback.format_exc()
    receipt["status"] = "BV_Q5_DIAGNOSTIC_INCOMPLETE"
finally:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(OUT.read_text())
