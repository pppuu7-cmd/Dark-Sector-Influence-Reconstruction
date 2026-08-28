#!/usr/bin/env python3
"""Fail-closed non-science aggregate prerequisite join for Exp073P.

The evaluator binds provenance and reproduction parents only.  It never builds
support rows, computes f_invalid, counts retained coordinates, reads covariance
or nuisance information, or classifies the Exp073P physical-support gate.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
from typing import Any

from exp073p_r1_admissibility_interlock_v0_1 import (
    EXPECTED_GATE_STATE,
    EXPECTED_METACAL_SHA256,
    EXPECTED_SOURCE_SHA256,
    InterlockError,
    _valid_fixture as valid_r1_fixture,
    validate_r1_summary,
)

ROOT = Path(__file__).resolve().parents[1]

PASS = "PASS_EXP073P_PREREQUISITE_BINDING_V0_1"
REJECTED = "REJECTED_EXP073P_PREREQUISITE_BINDING_V0_1"
INCOMPLETE = "INCOMPLETE_EXP073P_PREREQUISITE_BINDING_V0_1"
SYNTHETIC_PASS = "PASS_EXP073P_AGGREGATE_JOIN_SYNTHETIC_SELFTEST_V0_1"

REPOSITORY = "pppuu7-cmd/Dark-Sector-Influence-Reconstruction"
COSMOTHEKA_PIN = "7bde066626f66cd7bbe79cc46224d2342840e463"
R1_ARTIFACT_NAME = (
    "exp073r1-v06-selfhosted-longrun-"
    "79abf2a9694e57e7a2ba1fbb563a0f6413e891f9"
)

FROZEN_SUPPORT = {
    "z_min": 0.295,
    "z_max": 2.33,
    "k_max_Mpc^-1": 0.06664762008318016,
    "f_invalid_max": 0.05,
    "minimum_retained_dimension": 15,
    "nside_classifying": 4096,
}

OBJECTS = {
    "DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits": {
        "bytes": 104_595_840,
        "sha256": "a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55",
    },
    "DES_Y1A1_3x2pt_redMaGiC_zerr_CATALOG.fits": {
        "bytes": 31_383_360,
        "sha256": "4a0ed31a128c34aa0da17e1d826c76b5ac829ba1c2c2087b965977b89d43a177",
    },
    "2pt_NG_mcal_1110.fits": {
        "bytes": 6_600_960,
        "sha256": "114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca",
    },
    "y1_redshift_distributions_v1.fits": {
        "bytes": 109_440,
        "sha256": "b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b",
    },
    "y1_source_redshift_binning_v1.fits": {
        "bytes": 2_738_626_560,
        "sha256": EXPECTED_SOURCE_SHA256,
    },
    "mcal-y1a1-combined-riz-unblind-v4-matched.fits": {
        "bytes": 84_075_649_920,
        "sha256": EXPECTED_METACAL_SHA256,
    },
}

COSMOTHEKA_SOURCES = {
    "cosmotheka/mappers/mapper_DESY1gc.py": "c4b5e114b47b5a8b7ff0f5e7007e9f9fae6e2b9274532be5f9fc946966784dc7",
    "cosmotheka/mappers/mapper_DESY1wl.py": "f44ce29a6f73ea5d315bbd17f38fc72f22521cb923fdec972fa1e093f818e9df",
    "cosmotheka/cls/cl.py": "6f35e54d9042457dcad1bc65d15297865e854ceca0b4898490ef0d62b45109cc",
    "input/DESY1_eBOSS_P18CMBK.yml": "6ee2aa89f4a968062caa36726fed3f1c0f29b0dbf4ef3a4f3f78631abe4494f9",
}

STATIC_FILE_SHA256 = {
    "preflight": "e3429fff6786437aef68d2c5930341fd2b1752c193fd99f1c917e636859636f1",
    "s0": "abc41cfb16daece655e61b2fb8c592b2a09c9384943184272d59d63703eaef49",
    "boss": "dfe8861cd62e82297d9ce733d79585f7c5eca93d9bdbcef445b9f578105b2029",
}

LOCAL_CONTRACT_SHA256 = {
    "ci/exp073p_frozen_contract_selftest_v0_1.py": "ae8c4000af46c30ffb1059dab8f01758d2b21471cb7eac93fefba2f4d8093eeb",
    "ci/exp073p_r1_admissibility_interlock_v0_1.py": "c05bd94e44d80b37a7cea9db0b5321df3a16b05383ee280a3db04fd6d91c497c",
    "ci/exp073p_split_provenance_join_contract_selftest_v0_1.py": "649b074487b148715b5727091013d26170d7f463d3e99a98e1cc304187c1de41",
    "ci/exp073r1_v0_6_protocol_guard.py": "bd31cdae6f2e18aebcbfc06a96505c7061559fe00c970b6890052d20de8bc971",
    "experiments/073p_aggregate_prerequisite_join_evaluator_prereg_v0_1.md": "5e4a64ac47204f82261b9aa9f1a46250f5cc86bf654f001ee4f8db4a80603c4f",
}


def artifact(
    artifact_id: int | None,
    name: str,
    digest: str | None,
) -> dict[str, Any]:
    return {"id": artifact_id, "name": name, "digest": digest}


EXPECTED_RUNS: dict[str, dict[str, Any]] = {
    "preflight": {
        "id": 33076320686,
        "head": "a23843376ac4301327d23f3844b7fa658d9492c1",
        "path": ".github/workflows/exp073p-des-public-input-checksum-preflight-v0-1.yml",
        "name": "Exp073P DES public-input checksum preflight v0.1",
        "jobs": {98531327704: "pre-support-input-binding"},
        "artifacts": [artifact(9648001733, "exp073p-des-public-input-preflight-a23843376ac4301327d23f3844b7fa658d9492c1", "sha256:7ca856e24a1c03b11101cca278e6f631c86ba8ab28c744ef352c77dbe4b55266")],
    },
    "large_des": {
        "id": 33081571259,
        "head": "372997bf1240a224c2a915fd0d1a5ae50476ba7a",
        "path": ".github/workflows/exp073p-large-des-input-streaming-checksum-binding-v0-1.yml",
        "name": "Exp073P large DES input streaming checksum binding v0.1",
        "jobs": {98549908746: "source-bin-full-sha256", 98549908881: "metacal-full-sha256"},
        "artifacts": [
            artifact(9650284556, "exp073p-source-bin-full-sha256-372997bf1240a224c2a915fd0d1a5ae50476ba7a", "sha256:0eb1fdc7bc2d9f5816e0a003418a41b540cd7281af1f5ceb24a37af82187f5d4"),
            artifact(9650627630, "exp073p-metacal-full-sha256-372997bf1240a224c2a915fd0d1a5ae50476ba7a", "sha256:5a80c70568a6ed114e4e32990c5399bc8109df10f4d2910abd73441edb122a2b"),
        ],
    },
    "p2": {
        "id": 33086291753,
        "head": "fbcd8eb0a46a566b2510081f7f90714b534e7252",
        "path": ".github/workflows/exp073p2-remaining-desy1-checksums-v0-1.yml",
        "name": "Exp073P2 remaining DES Y1 checksum binding v0.1",
        "jobs": {98566715352: "remaining-des-checksums"},
        "artifacts": [artifact(9652278804, "exp073p2-remaining-des-checksums-fbcd8eb0a46a566b2510081f7f90714b534e7252", "sha256:3eaed2f182b885c360a73ad3a6bfefac088a000acd05bef07bdfe5a852a246b9")],
    },
    "s0": {
        "id": 33086762750,
        "head": "82c5804b1fcbbdc100f09a9878643ddc51975d8e",
        "path": ".github/workflows/exp073s0-desy1-redmagic-mask-nz-v0-1.yml",
        "name": "Exp073S0 DES Y1 redMaGiC mask and n(z) v0.1",
        "jobs": {98568401949: "reproduce-small-inputs"},
        "artifacts": [artifact(9652504743, "exp073s0-redmagic-mask-nz-82c5804b1fcbbdc100f09a9878643ddc51975d8e", "sha256:c6f84c35e7ade17a6054ad77d4117b64a6c69fbbefe0d0f89e6491bbe88b358e")],
    },
    "r1": {
        "id": 33212521957,
        "head": "79abf2a9694e57e7a2ba1fbb563a0f6413e891f9",
        "path": ".github/workflows/exp073r1-desy1-selfhosted-longrun-stageb-v0-6.yml",
        "name": "Exp073R1 DESY1 self-hosted long-run Stage-B v0.6",
        "jobs": {98988824629: "metacal-map-longrun"},
        "artifacts": [artifact(None, R1_ARTIFACT_NAME, None)],
    },
    "boss": {
        "id": 33042052616,
        "head": "1bd022ffca543361d265a72b782ef96fe069d2ce",
        "path": ".github/workflows/exp073j-boss-finite-matrix-component-support-v0-1.yml",
        "name": "Exp073J BOSS finite-matrix component support v0.1",
        "jobs": {98417620281: "boss-component-support"},
        "artifacts": [artifact(9634226231, "exp073j-boss-component-support-1bd022ffca543361d265a72b782ef96fe069d2ce", "sha256:239b198c1adfc21333779ef1efb597885710bddd593b380a67ac6dd1399daa65")],
    },
    "support_contract": {
        "id": 33132472587,
        "head": "637ecc89422fa1eb02a4254044ce57b45de7df51",
        "path": ".github/workflows/exp073p-frozen-contract-selftest-v0-1.yml",
        "name": "Exp073P frozen contract self-test v0.1",
        "jobs": {},
        "artifacts": [],
    },
    "split_join_contract": {
        "id": 33166411136,
        "head": "d4e0ba1b9a9e0342e763a715cd9b1db9b906affc",
        "path": ".github/workflows/exp073p-split-provenance-join-contract-selftest-v0-1.yml",
        "name": "Exp073P split-provenance join contract self-test v0.1",
        "jobs": {},
        "artifacts": [],
    },
    "r1_interlock": {
        "id": 33215180917,
        "head": "7be369dec4469dd9f6390eb5225ff4366ded9488",
        "path": ".github/workflows/exp073p-r1-admissibility-interlock-selftest-v0-1.yml",
        "name": "Exp073P R1 admissibility interlock selftest v0.1",
        "jobs": {},
        "artifacts": [],
    },
    "v06_protocol_guard": {
        "id": 33215131178,
        "head": "e92d40f8aabe636414827655bfd165b093f2073e",
        "path": ".github/workflows/exp073r1-v06-protocol-guard.yml",
        "name": "Exp073R1 v0.6 frozen protocol guard",
        "jobs": {},
        "artifacts": [],
    },
}


class JoinError(ValueError):
    pass


class JoinIncomplete(JoinError):
    pass


def need(condition: bool, message: str) -> None:
    if not condition:
        raise JoinError(f"{REJECTED}: {message}")


def available(condition: bool, message: str) -> None:
    if not condition:
        raise JoinIncomplete(f"{INCOMPLETE}: {message}")


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def valid_digest(value: Any) -> bool:
    if not isinstance(value, str) or not value.startswith("sha256:"):
        return False
    payload = value.removeprefix("sha256:")
    if len(payload) != 64:
        return False
    try:
        int(payload, 16)
    except ValueError:
        return False
    return True


def load_record(path: Path) -> tuple[dict[str, Any], str]:
    available(path.is_file(), f"record unavailable: {path}")
    raw = path.read_bytes()
    try:
        obj = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise JoinError(f"{REJECTED}: invalid JSON in {path}: {exc}") from exc
    need(isinstance(obj, dict), f"record is not an object: {path}")
    return obj, sha256_bytes(raw)


def no_leakage_flags(record: dict[str, Any], keys: tuple[str, ...], where: str) -> None:
    for key in keys:
        need(record.get(key) is False, f"{where}: no-leakage flag {key!r} is not false")


def validate_metadata(meta: dict[str, Any]) -> dict[str, Any]:
    need(meta.get("schema") == "dsir.exp073p.aggregate-prerequisite-metadata.v0.1", "metadata schema drift")
    need(meta.get("repository") == REPOSITORY, "metadata repository drift")
    parents = meta.get("parents")
    need(isinstance(parents, dict), "metadata parents missing")
    need(set(parents) == set(EXPECTED_RUNS), "metadata parent set drift")

    bound: dict[str, Any] = {}
    for key, expected in EXPECTED_RUNS.items():
        parent = parents[key]
        need(isinstance(parent, dict), f"metadata parent {key} is not an object")
        run = parent.get("run")
        need(isinstance(run, dict), f"metadata run {key} missing")
        need(run.get("id") == expected["id"], f"{key}: run id drift")
        need(run.get("head_sha") == expected["head"], f"{key}: head drift")
        need(run.get("path") == expected["path"], f"{key}: workflow path drift")
        need(run.get("name") == expected["name"], f"{key}: workflow name drift")
        available(run.get("status") == "completed", f"{key}: run not completed")
        available(run.get("conclusion") == "success", f"{key}: run did not succeed")

        jobs = parent.get("jobs", [])
        need(isinstance(jobs, list), f"{key}: jobs is not a list")
        by_job_id = {j.get("id"): j for j in jobs if isinstance(j, dict)}
        for job_id, job_name in expected["jobs"].items():
            available(job_id in by_job_id, f"{key}: required job {job_id} unavailable")
            job = by_job_id[job_id]
            need(job.get("name") == job_name, f"{key}: job name drift")
            available(job.get("status") == "completed", f"{key}: job incomplete")
            available(job.get("conclusion") == "success", f"{key}: job unsuccessful")

        artifacts = parent.get("artifacts", [])
        need(isinstance(artifacts, list), f"{key}: artifacts is not a list")
        artifact_summary = []
        for exp in expected["artifacts"]:
            matches = [a for a in artifacts if isinstance(a, dict) and a.get("name") == exp["name"]]
            available(len(matches) == 1, f"{key}: unique artifact {exp['name']} unavailable")
            got = matches[0]
            if exp["id"] is None:
                need(isinstance(got.get("id"), int) and got["id"] > 0, f"{key}: dynamic artifact id invalid")
            else:
                need(got.get("id") == exp["id"], f"{key}: artifact id drift")
            if exp["digest"] is None:
                need(valid_digest(got.get("digest")), f"{key}: dynamic artifact digest invalid")
            else:
                need(got.get("digest") == exp["digest"], f"{key}: artifact digest drift")
            available(got.get("expired") is False, f"{key}: artifact expired")
            wr = got.get("workflow_run")
            need(isinstance(wr, dict), f"{key}: artifact workflow binding missing")
            need(wr.get("id") == expected["id"], f"{key}: artifact run drift")
            need(wr.get("head_sha") == expected["head"], f"{key}: artifact head drift")
            artifact_summary.append({"id": got["id"], "name": got["name"], "digest": got["digest"]})
        bound[key] = {
            "run_id": expected["id"],
            "head_sha": expected["head"],
            "artifacts": artifact_summary,
        }
    return bound


def validate_local_contracts() -> dict[str, str]:
    observed: dict[str, str] = {}
    for rel, expected in LOCAL_CONTRACT_SHA256.items():
        path = ROOT / rel
        available(path.is_file(), f"local contract missing: {rel}")
        got = sha256_bytes(path.read_bytes())
        need(got == expected, f"local contract drift: {rel}")
        observed[rel] = got
    return observed


def validate_preflight(d: dict[str, Any]) -> dict[str, Any]:
    need(d.get("experiment") == "Exp073P-preflight", "preflight experiment drift")
    need(d.get("status") == "BLOCKED_PRE_SUPPORT_INPUT_CHECKSUM_BINDING_EXP073P_PREFLIGHT", "legacy preflight boundary drift")
    need(d.get("scientific_classification") is None, "preflight scientific classification present")
    need(d.get("all_checksum_bound") is False, "legacy all-checksum flag unexpectedly true")
    need(d.get("support_evaluation_authorized") is False, "legacy READY flag resurrected")
    need(d.get("support_fraction_evaluated") is False, "preflight support fraction evaluated")
    need(d.get("retained_dimension_evaluated") is False, "preflight dimension evaluated")
    need(d.get("gate_state") == EXPECTED_GATE_STATE, "preflight gate state drift")

    cosmo = d.get("cosmotheka")
    need(isinstance(cosmo, dict) and cosmo.get("pass") is True, "Cosmotheka preflight absent")
    need(cosmo.get("expected_pin") == COSMOTHEKA_PIN == cosmo.get("observed_pin"), "Cosmotheka pin drift")
    need(cosmo.get("config_names_pass") is True, "Cosmotheka config-name binding failed")
    got_sources = {x.get("path"): x.get("sha256") for x in cosmo.get("source_records", []) if isinstance(x, dict) and x.get("exists") is True}
    need(got_sources == COSMOTHEKA_SOURCES, "Cosmotheka source hash set drift")

    parent = d.get("frozen_parent")
    need(isinstance(parent, dict) and parent.get("pass") is True, "Exp073O parent absent")
    need(parent.get("status_expected") == "PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O", "Exp073O expected status drift")
    need(parent.get("status_observed") == parent.get("status_expected"), "Exp073O status mismatch")
    need(d.get("frozen_contract_preserved") == {
        "G8_read": False,
        "covariance_read": False,
        "f_invalid_max": 0.05,
        "k_max_Mpc^-1": 0.06664762008318016,
        "minimum_retained_dimension": 15,
        "nside_classifying": 4096,
        "nuisance_read": False,
        "relation_null_read": False,
        "z_max": 2.33,
        "z_min": 0.295,
    }, "preflight frozen contract drift")

    objects = {x.get("name"): x for x in d.get("public_objects", []) if isinstance(x, dict)}
    need(set(objects) == set(OBJECTS), "preflight release-name set drift")
    for name, expected in OBJECTS.items():
        rec = objects[name]
        need(rec.get("content_length") == expected["bytes"], f"preflight {name}: byte count drift")
        if name in {"y1_source_redshift_binning_v1.fits", "mcal-y1a1-combined-riz-unblind-v4-matched.fits"}:
            need(rec.get("checksum_bound") is False and rec.get("sha256") is None, f"preflight {name}: legacy cap semantics drift")
        else:
            need(rec.get("checksum_bound") is True, f"preflight {name}: checksum not bound")
            need(rec.get("sha256") == expected["sha256"], f"preflight {name}: SHA256 drift")
    return {"cosmotheka_pin": COSMOTHEKA_PIN, "release_names": sorted(objects)}


def validate_large_record(d: dict[str, Any], name: str) -> dict[str, Any]:
    expected = OBJECTS[name]
    need(d.get("experiment") == "Exp073P-large-input-binding", f"large {name}: experiment drift")
    need(d.get("name") == name, f"large {name}: name drift")
    need(d.get("status") == "PASS_FULL_OBJECT_STREAMING_SHA256_BINDING", f"large {name}: PASS absent")
    need(d.get("expected_bytes") == expected["bytes"] == d.get("observed_bytes"), f"large {name}: byte count drift")
    need(d.get("sha256") == expected["sha256"], f"large {name}: SHA256 drift")
    need(d.get("byte_count_pass") is True, f"large {name}: byte-count control failed")
    no_leakage_flags(d, ("support_fraction_evaluated", "retained_dimension_evaluated", "covariance_read", "nuisance_read", "relation_null_read", "G8_read"), f"large {name}")
    need(d.get("gate_state") == EXPECTED_GATE_STATE, f"large {name}: gate state drift")
    return {"bytes": expected["bytes"], "sha256": expected["sha256"]}


def validate_p2(d: dict[str, Any]) -> dict[str, Any]:
    need(d.get("experiment") == "Exp073P2", "P2 experiment drift")
    need(d.get("status") == "PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2", "P2 PASS absent")
    need(d.get("science_gate_scored") is False, "P2 scored science")
    need(d.get("gate_state") == EXPECTED_GATE_STATE, "P2 gate state drift")
    expected_names = set(OBJECTS) - {"y1_source_redshift_binning_v1.fits", "mcal-y1a1-combined-riz-unblind-v4-matched.fits"}
    objects = {x.get("name"): x for x in d.get("objects", []) if isinstance(x, dict)}
    need(set(objects) == expected_names, "P2 object set drift")
    for name in sorted(expected_names):
        rec = objects[name]
        expected = OBJECTS[name]
        need(rec.get("status") == "PASS_FULL_OBJECT_SHA256_BINDING", f"P2 {name}: PASS absent")
        need(rec.get("observed_bytes") == expected["bytes"], f"P2 {name}: bytes drift")
        need(rec.get("sha256") == expected["sha256"], f"P2 {name}: SHA256 drift")
    return {name: OBJECTS[name] for name in sorted(expected_names)}


def validate_s0(d: dict[str, Any]) -> dict[str, Any]:
    need(d.get("experiment") == "Exp073S0", "S0 experiment drift")
    need(d.get("status") == "PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0", "S0 PASS absent")
    need(d.get("workflow_run") == 33086762750 and d.get("workflow_job") == 98568401949, "S0 execution drift")
    need(d.get("execution_sha") == "82c5804b1fcbbdc100f09a9878643ddc51975d8e", "S0 head drift")
    need(d.get("artifact_id") == 9652504743, "S0 artifact id drift")
    need(d.get("artifact_digest") == "sha256:c6f84c35e7ade17a6054ad77d4117b64a6c69fbbefe0d0f89e6491bbe88b358e", "S0 artifact digest drift")
    parent = d.get("parent_state")
    need(isinstance(parent, dict) and parent.get("Exp073P2") == "PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2", "S0 P2 parent drift")
    need(parent.get("science_gate_scored") is False, "S0 parent scored science")
    mask = d.get("mask")
    need(isinstance(mask, dict), "S0 mask missing")
    need(mask.get("input_nside") == 4096 and mask.get("npix") == 201_326_592, "S0 mask geometry drift")
    need(mask.get("same_nside_ud_grade_exact_identity") is True, "S0 same-NSIDE identity failed")
    need(mask.get("retained_pixels_gt_0p5") == 6_536_725, "S0 retained pixels drift")
    need(mask.get("dense_numeric_sha256") == "7eb243d77febe59d1fb327095b385b40084f4b6140ae4421f1c45c787088e918", "S0 dense mask hash drift")
    need(mask.get("sparse_pixel_value_sha256") == "c1449c30efb31ce0b7f6cab01f2ea11faad8156a3021033518015b3e853abd3b", "S0 sparse mask hash drift")
    lens, source = d.get("lens_nz"), d.get("source_nz")
    need(isinstance(lens, dict) and isinstance(source, dict), "S0 n(z) records missing")
    need(lens.get("rows") == 400 and lens.get("bins") == [f"BIN{i}" for i in range(1, 6)], "S0 lens n(z) schema drift")
    need(source.get("rows") == 400 and source.get("bins") == [f"BIN{i}" for i in range(1, 5)], "S0 source n(z) schema drift")
    need(lens.get("numeric_sha256") == "395e043566c3c06e960c95d8b7b617b29a42f5d4fa4e65d5dd66f2e5f674a383", "S0 lens n(z) hash drift")
    need(source.get("numeric_sha256") == "ab4d447dc72e0fdf9cdd470b2eb9cb4d5aa5a6a1bd89f1b55bd047a18f972f97", "S0 source n(z) hash drift")
    boundary = d.get("interpretation_boundary")
    need(isinstance(boundary, dict), "S0 boundary missing")
    no_leakage_flags(boundary, ("support_fraction_computed", "covariance_read", "nuisance_or_SVD_read", "G8_read"), "S0")
    need({k: boundary.get(k) for k in ("G7", "G8", "G9")} == EXPECTED_GATE_STATE, "S0 gate state drift")
    return {
        "mask_sha256": mask["dense_numeric_sha256"],
        "lens_nz_sha256": lens["numeric_sha256"],
        "source_nz_sha256": source["numeric_sha256"],
    }


def validate_boss(d: dict[str, Any]) -> dict[str, Any]:
    need(d.get("experiment") == "Exp073J", "BOSS experiment drift")
    need(d.get("record_type") == "BOSS_FINITE_MATRIX_COMPONENT_SUPPORT_KEY_METRICS_NONCLASSIFYING", "BOSS record type drift")
    need(d.get("implementation_merge_sha") == "1bd022ffca543361d265a72b782ef96fe069d2ce", "BOSS head drift")
    need(d.get("workflow_run") == 33042052616 and d.get("workflow_job") == 98417620281, "BOSS execution drift")
    need(d.get("artifact_id") == 9634226231, "BOSS artifact id drift")
    need(d.get("artifact_digest") == "sha256:239b198c1adfc21333779ef1efb597885710bddd593b380a67ac6dd1399daa65", "BOSS artifact digest drift")
    frozen = d.get("frozen")
    need(isinstance(frozen, dict), "BOSS frozen block missing")
    need(frozen.get("z_min") == 0.295 and frozen.get("z_max") == 2.33, "BOSS z support drift")
    need(frozen.get("k_max_Mpc^-1") == 0.06664762008318016, "BOSS k support drift")
    need(frozen.get("max_positive_invalid_fraction") == 0.05, "BOSS threshold drift")
    result = d.get("result")
    need(isinstance(result, dict), "BOSS result missing")
    need(result.get("component_total_coordinates") == 240, "BOSS total coordinate drift")
    need(result.get("component_retained_coordinates") == 54, "BOSS retained coordinate drift")
    for cap in ("NGC", "SGC"):
        block = result.get(cap)
        need(isinstance(block, dict) and block.get("retained") == 27, f"BOSS {cap} retained drift")
        for multipole in ("P0", "P2", "P4"):
            row = block.get(multipole)
            need(isinstance(row, dict) and row.get("count") == 40 and row.get("retained") == 9, f"BOSS {cap}/{multipole} drift")
    controls = d.get("controls")
    need(isinstance(controls, dict) and controls.get("implementation_checks_all_pass") is True, "BOSS implementation controls failed")
    no_leakage_flags(controls, ("covariance_values_read", "nuisance_rank_read", "relation_residual_read", "G8_read", "pk_weighting_used", "posthoc_k_cut_used"), "BOSS")
    boundary = d.get("interpretation_boundary")
    need(isinstance(boundary, dict) and boundary.get("scientific_classification_authorized") is False, "BOSS nonclassifying boundary drift")
    need({k: boundary.get(k) for k in ("G7", "G8", "G9")} == EXPECTED_GATE_STATE, "BOSS gate state drift")
    return {"retained": 54, "total": 240, "per_cap_retained": 27, "per_multipole_retained": 9}


def base_receipt(status: str, *, synthetic: bool, error: str | None = None) -> dict[str, Any]:
    out: dict[str, Any] = {
        "experiment": "Exp073P-aggregate-prerequisite-join-v0.1",
        "status": status,
        "synthetic": synthetic,
        "scientific_classification": None,
        "support_executor_authorized": False,
        "support_fraction_evaluated": False,
        "f_invalid_computed": False,
        "retained_dimension_evaluated": False,
        "covariance_read": False,
        "whitening_read": False,
        "nuisance_svd_read": False,
        "relation_null_read": False,
        "heldout_read": False,
        "G8_read": False,
        "gate_state": copy.deepcopy(EXPECTED_GATE_STATE),
        "frozen_support_contract": copy.deepcopy(FROZEN_SUPPORT),
    }
    if error is not None:
        out["error"] = error
    return out


def validate_join(
    metadata: dict[str, Any],
    records: dict[str, tuple[dict[str, Any], str]],
    *,
    synthetic: bool,
) -> dict[str, Any]:
    need(set(records) == {"preflight", "large_source", "large_metacal", "p2", "s0", "r1", "boss"}, "record set drift")
    bound_metadata = validate_metadata(metadata)
    local_contracts = validate_local_contracts()

    if not synthetic:
        for key in ("preflight", "s0", "boss"):
            need(records[key][1] == STATIC_FILE_SHA256[key], f"canonical static record bytes drift: {key}")

    preflight = validate_preflight(records["preflight"][0])
    large_source = validate_large_record(records["large_source"][0], "y1_source_redshift_binning_v1.fits")
    large_metacal = validate_large_record(records["large_metacal"][0], "mcal-y1a1-combined-riz-unblind-v4-matched.fits")
    p2 = validate_p2(records["p2"][0])
    s0 = validate_s0(records["s0"][0])
    try:
        r1 = validate_r1_summary(records["r1"][0])
    except InterlockError as exc:
        raise JoinError(f"{REJECTED}: R1 interlock rejected summary: {exc}") from exc
    boss = validate_boss(records["boss"][0])

    combined = dict(p2)
    combined["y1_source_redshift_binning_v1.fits"] = large_source
    combined["mcal-y1a1-combined-riz-unblind-v4-matched.fits"] = large_metacal
    need(combined == OBJECTS, "complete six-object identity join drift")
    need(r1["source_sha256"] == large_source["sha256"], "R1/source large-object cross-binding failed")
    need(r1["metacal_sha256"] == large_metacal["sha256"], "R1/metacal large-object cross-binding failed")

    status = SYNTHETIC_PASS if synthetic else PASS
    out = base_receipt(status, synthetic=synthetic)
    out.update({
        "support_executor_authorized": False if synthetic else True,
        "parent_metadata": bound_metadata,
        "record_sha256": {key: raw_sha for key, (_, raw_sha) in records.items()},
        "local_contract_sha256": local_contracts,
        "cosmotheka": preflight,
        "release_objects": combined,
        "s0": s0,
        "r1": r1,
        "boss": boss,
        "authorization_boundary": (
            "synthetic validation only; no real executor authorization"
            if synthetic
            else "the separately preregistered Exp073P physical-support executor is eligible to start; covariance remains blocked"
        ),
    })
    return out


def valid_metadata_fixture() -> dict[str, Any]:
    parents: dict[str, Any] = {}
    for key, expected in EXPECTED_RUNS.items():
        jobs = [
            {"id": job_id, "name": job_name, "status": "completed", "conclusion": "success"}
            for job_id, job_name in expected["jobs"].items()
        ]
        artifacts = []
        for i, exp in enumerate(expected["artifacts"]):
            artifacts.append({
                "id": exp["id"] if exp["id"] is not None else 9_999_000 + i,
                "name": exp["name"],
                "digest": exp["digest"] if exp["digest"] is not None else "sha256:" + "a" * 64,
                "expired": False,
                "workflow_run": {"id": expected["id"], "head_sha": expected["head"]},
            })
        parents[key] = {
            "run": {
                "id": expected["id"],
                "head_sha": expected["head"],
                "path": expected["path"],
                "name": expected["name"],
                "status": "completed",
                "conclusion": "success",
            },
            "jobs": jobs,
            "artifacts": artifacts,
        }
    return {
        "schema": "dsir.exp073p.aggregate-prerequisite-metadata.v0.1",
        "repository": REPOSITORY,
        "parents": parents,
    }


def valid_preflight_fixture() -> dict[str, Any]:
    public = []
    large = {"y1_source_redshift_binning_v1.fits", "mcal-y1a1-combined-riz-unblind-v4-matched.fits"}
    for name, expected in OBJECTS.items():
        public.append({
            "name": name,
            "content_length": expected["bytes"],
            "checksum_bound": name not in large,
            "sha256": None if name in large else expected["sha256"],
        })
    return {
        "experiment": "Exp073P-preflight",
        "status": "BLOCKED_PRE_SUPPORT_INPUT_CHECKSUM_BINDING_EXP073P_PREFLIGHT",
        "scientific_classification": None,
        "all_checksum_bound": False,
        "support_evaluation_authorized": False,
        "support_fraction_evaluated": False,
        "retained_dimension_evaluated": False,
        "gate_state": copy.deepcopy(EXPECTED_GATE_STATE),
        "cosmotheka": {
            "pass": True,
            "expected_pin": COSMOTHEKA_PIN,
            "observed_pin": COSMOTHEKA_PIN,
            "config_names_pass": True,
            "source_records": [{"path": p, "sha256": h, "exists": True} for p, h in COSMOTHEKA_SOURCES.items()],
        },
        "frozen_parent": {
            "pass": True,
            "status_expected": "PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O",
            "status_observed": "PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O",
        },
        "frozen_contract_preserved": {
            "G8_read": False,
            "covariance_read": False,
            "f_invalid_max": 0.05,
            "k_max_Mpc^-1": 0.06664762008318016,
            "minimum_retained_dimension": 15,
            "nside_classifying": 4096,
            "nuisance_read": False,
            "relation_null_read": False,
            "z_max": 2.33,
            "z_min": 0.295,
        },
        "public_objects": public,
    }


def valid_large_fixture(name: str) -> dict[str, Any]:
    expected = OBJECTS[name]
    return {
        "experiment": "Exp073P-large-input-binding",
        "name": name,
        "status": "PASS_FULL_OBJECT_STREAMING_SHA256_BINDING",
        "expected_bytes": expected["bytes"],
        "observed_bytes": expected["bytes"],
        "sha256": expected["sha256"],
        "byte_count_pass": True,
        "support_fraction_evaluated": False,
        "retained_dimension_evaluated": False,
        "covariance_read": False,
        "nuisance_read": False,
        "relation_null_read": False,
        "G8_read": False,
        "gate_state": copy.deepcopy(EXPECTED_GATE_STATE),
    }


def valid_p2_fixture() -> dict[str, Any]:
    names = set(OBJECTS) - {"y1_source_redshift_binning_v1.fits", "mcal-y1a1-combined-riz-unblind-v4-matched.fits"}
    return {
        "experiment": "Exp073P2",
        "status": "PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2",
        "science_gate_scored": False,
        "gate_state": copy.deepcopy(EXPECTED_GATE_STATE),
        "objects": [
            {
                "name": name,
                "status": "PASS_FULL_OBJECT_SHA256_BINDING",
                "observed_bytes": OBJECTS[name]["bytes"],
                "sha256": OBJECTS[name]["sha256"],
            }
            for name in sorted(names)
        ],
    }


def valid_s0_fixture() -> dict[str, Any]:
    return {
        "experiment": "Exp073S0",
        "status": "PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0",
        "workflow_run": 33086762750,
        "workflow_job": 98568401949,
        "execution_sha": "82c5804b1fcbbdc100f09a9878643ddc51975d8e",
        "artifact_id": 9652504743,
        "artifact_digest": "sha256:c6f84c35e7ade17a6054ad77d4117b64a6c69fbbefe0d0f89e6491bbe88b358e",
        "parent_state": {"Exp073P2": "PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2", "science_gate_scored": False},
        "mask": {
            "input_nside": 4096,
            "npix": 201_326_592,
            "same_nside_ud_grade_exact_identity": True,
            "retained_pixels_gt_0p5": 6_536_725,
            "dense_numeric_sha256": "7eb243d77febe59d1fb327095b385b40084f4b6140ae4421f1c45c787088e918",
            "sparse_pixel_value_sha256": "c1449c30efb31ce0b7f6cab01f2ea11faad8156a3021033518015b3e853abd3b",
        },
        "lens_nz": {"rows": 400, "bins": [f"BIN{i}" for i in range(1, 6)], "numeric_sha256": "395e043566c3c06e960c95d8b7b617b29a42f5d4fa4e65d5dd66f2e5f674a383"},
        "source_nz": {"rows": 400, "bins": [f"BIN{i}" for i in range(1, 5)], "numeric_sha256": "ab4d447dc72e0fdf9cdd470b2eb9cb4d5aa5a6a1bd89f1b55bd047a18f972f97"},
        "interpretation_boundary": {
            "support_fraction_computed": False,
            "covariance_read": False,
            "nuisance_or_SVD_read": False,
            "G8_read": False,
            "G7": "OPEN",
            "G8": "OPEN",
            "G9": "OPEN",
        },
    }


def valid_boss_fixture() -> dict[str, Any]:
    block = {
        "retained": 27,
        "P0": {"count": 40, "retained": 9},
        "P2": {"count": 40, "retained": 9},
        "P4": {"count": 40, "retained": 9},
    }
    return {
        "experiment": "Exp073J",
        "record_type": "BOSS_FINITE_MATRIX_COMPONENT_SUPPORT_KEY_METRICS_NONCLASSIFYING",
        "implementation_merge_sha": "1bd022ffca543361d265a72b782ef96fe069d2ce",
        "workflow_run": 33042052616,
        "workflow_job": 98417620281,
        "artifact_id": 9634226231,
        "artifact_digest": "sha256:239b198c1adfc21333779ef1efb597885710bddd593b380a67ac6dd1399daa65",
        "frozen": {"z_min": 0.295, "z_max": 2.33, "k_max_Mpc^-1": 0.06664762008318016, "max_positive_invalid_fraction": 0.05},
        "result": {"component_total_coordinates": 240, "component_retained_coordinates": 54, "NGC": copy.deepcopy(block), "SGC": copy.deepcopy(block)},
        "controls": {
            "implementation_checks_all_pass": True,
            "covariance_values_read": False,
            "nuisance_rank_read": False,
            "relation_residual_read": False,
            "G8_read": False,
            "pk_weighting_used": False,
            "posthoc_k_cut_used": False,
        },
        "interpretation_boundary": {"scientific_classification_authorized": False, "G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }


def valid_record_fixture() -> dict[str, tuple[dict[str, Any], str]]:
    data = {
        "preflight": valid_preflight_fixture(),
        "large_source": valid_large_fixture("y1_source_redshift_binning_v1.fits"),
        "large_metacal": valid_large_fixture("mcal-y1a1-combined-riz-unblind-v4-matched.fits"),
        "p2": valid_p2_fixture(),
        "s0": valid_s0_fixture(),
        "r1": valid_r1_fixture(),
        "boss": valid_boss_fixture(),
    }
    return {key: (value, sha256_bytes(json.dumps(value, sort_keys=True).encode())) for key, value in data.items()}


def must_reject(mutator) -> None:
    metadata = valid_metadata_fixture()
    records = valid_record_fixture()
    mutator(metadata, records)
    try:
        validate_join(metadata, records, synthetic=True)
    except JoinError:
        return
    raise AssertionError("mutant unexpectedly crossed Exp073P aggregate join")


def selftest() -> dict[str, Any]:
    out = validate_join(valid_metadata_fixture(), valid_record_fixture(), synthetic=True)
    assert out["status"] == SYNTHETIC_PASS
    assert out["support_executor_authorized"] is False
    assert out["support_fraction_evaluated"] is False
    assert out["covariance_read"] is False and out["G8_read"] is False
    assert PASS != SYNTHETIC_PASS

    for parent in EXPECTED_RUNS:
        must_reject(lambda m, r, parent=parent: m["parents"][parent]["run"].__setitem__("head_sha", "0" * 40))
    for parent in ("preflight", "large_des", "p2", "s0", "r1", "boss"):
        must_reject(lambda m, r, parent=parent: m["parents"][parent]["artifacts"][0].__setitem__("expired", True))

    mutations = [
        lambda m, r: r["preflight"][0]["cosmotheka"].__setitem__("observed_pin", "0" * 40),
        lambda m, r: r["preflight"][0].__setitem__("support_evaluation_authorized", True),
        lambda m, r: r["large_source"][0].__setitem__("sha256", "0" * 64),
        lambda m, r: r["large_metacal"][0].__setitem__("observed_bytes", 84_075_649_919),
        lambda m, r: r["p2"][0].__setitem__("status", "success"),
        lambda m, r: r["p2"][0]["objects"][0].__setitem__("sha256", "0" * 64),
        lambda m, r: r["s0"][0]["mask"].__setitem__("dense_numeric_sha256", "0" * 64),
        lambda m, r: r["s0"][0]["interpretation_boundary"].__setitem__("covariance_read", True),
        lambda m, r: r["r1"][0].__setitem__("status", "success"),
        lambda m, r: r["r1"][0].__setitem__("f_invalid_computed", True),
        lambda m, r: r["boss"][0]["result"].__setitem__("component_retained_coordinates", 55),
        lambda m, r: r["boss"][0]["controls"].__setitem__("G8_read", True),
    ]
    for mutation in mutations:
        must_reject(mutation)
    return out


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--classifying", action="store_true")
    ap.add_argument("--metadata", type=Path)
    ap.add_argument("--preflight", type=Path)
    ap.add_argument("--large-source", type=Path)
    ap.add_argument("--large-metacal", type=Path)
    ap.add_argument("--p2", type=Path)
    ap.add_argument("--s0", type=Path)
    ap.add_argument("--r1", type=Path)
    ap.add_argument("--boss", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    if args.selftest:
        if args.classifying:
            ap.error("--selftest and --classifying are mutually exclusive")
        receipt = selftest()
        write_json(args.out, receipt)
        print(SYNTHETIC_PASS)
        return

    if not args.classifying:
        ap.error("real evidence evaluation requires explicit --classifying")
    required = ("metadata", "preflight", "large_source", "large_metacal", "p2", "s0", "r1", "boss")
    for name in required:
        if getattr(args, name) is None:
            ap.error(f"--{name.replace('_', '-')} is required with --classifying")

    try:
        metadata, _ = load_record(args.metadata)
        records = {
            "preflight": load_record(args.preflight),
            "large_source": load_record(args.large_source),
            "large_metacal": load_record(args.large_metacal),
            "p2": load_record(args.p2),
            "s0": load_record(args.s0),
            "r1": load_record(args.r1),
            "boss": load_record(args.boss),
        }
        receipt = validate_join(metadata, records, synthetic=False)
    except JoinIncomplete as exc:
        receipt = base_receipt(INCOMPLETE, synthetic=False, error=str(exc))
        write_json(args.out, receipt)
        print(INCOMPLETE)
        raise SystemExit(3) from exc
    except (JoinError, OSError) as exc:
        receipt = base_receipt(REJECTED, synthetic=False, error=str(exc))
        write_json(args.out, receipt)
        print(REJECTED)
        raise SystemExit(2) from exc

    write_json(args.out, receipt)
    print(PASS)


if __name__ == "__main__":
    main()
