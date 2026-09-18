#!/usr/bin/env python3
"""DSIR V0.26 R1 BOSS M300 cross-survey response replication.

Read-only consumer of immutable numerical witnesses.
No CLASS import, no solver execution, no covariance/nuisance/full107 access.
All frozen provenance bindings pass before any beta +/- response arithmetic.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import io
import itertools
import json
import os
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PREREG = ROOT / "prereg/LAYERB_BETA_V0_26_R1_BOSS_M300_CROSS_SURVEY_RESPONSE_REPLICATION_V0_1.md"
DESIGN = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_BOSS_M300_CROSS_SURVEY_RESPONSE_REPLICATION_DESIGN_AUTHORITY_V0_1.json"
DESIGN_CRITIC = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_BOSS_M300_CROSS_SURVEY_RESPONSE_REPLICATION_DESIGN_STATIC_CRITIC_V0_1.json"
AUTHORING_AUTHORITY = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_BOSS_M300_CROSS_SURVEY_RESPONSE_REPLICATION_IMPLEMENTATION_AUTHORING_AUTHORITY_V0_1.json"
NUMERICAL_RUNTIME_CRITIC = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_MINIMAL_NUMERICAL_REPRODUCIBILITY_RUNTIME_CRITIC_V0_1.json"
IMPLEMENTATION_CRITIC = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_BOSS_M300_CROSS_SURVEY_RESPONSE_REPLICATION_IMPLEMENTATION_STATIC_CRITIC_V0_1.json"
EXECUTION_AUTHORITY = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_BOSS_M300_CROSS_SURVEY_RESPONSE_REPLICATION_EXECUTION_AUTHORITY_V0_1.json"
WORKFLOW = ROOT / ".github/workflows/dsir-v026-r1-boss-m300-cross-survey-response-replication-v0-1.yml"
LAUNCH_MARKER = ROOT / "docs/dsir4/launch/LAYERB_BETA_V0_26_R1_BOSS_M300_CROSS_SURVEY_RESPONSE_REPLICATION_V0_1.launch.json"

PREREG_BLOB = "983f039f0bcf410d629a78332c2be2b6b85a95ff"
DESIGN_BLOB = "8ebb5ea32b28d9ac38625bdb1c1f999663d113cb"
DESIGN_CRITIC_BLOB = "acf0cf8ab62f586ac9b771f29b2a2202caaf87bb"
AUTHORING_AUTHORITY_BLOB = "9fd2c5faddbb98bed67a0edf8e89ef582068616a"
NUMERICAL_RUNTIME_CRITIC_BLOB = "9f19f8cc643bc978d0dbbcdd58f80fdf04395e24"

SOURCE_RUN_ID = 35280281867
H = 1e-4
TECH_TOL = 1e-5
SCI_TOL = 1e-3
CALLS = list(range(377, 441))
ENTRY_COUNT = 297
UNIQUE_TARGET_COUNT = 99
UNIQUE99_SHA256 = "a44a8921e3c10b17cdf222b97d18524454e927dadeea30b13e75c3a0d6fc42fc"
RAW297_SHA256 = "e5bcdcb7fbb802b24469d8e3f1965013dc35b3b9249868476cf22490456f344a"
REPLICATES = [f"R{i:02d}" for i in range(1, 33)]
ACTIVE = "NATIVE_AVX512_ACTIVE"
INACTIVE = "NATIVE_AVX512_INACTIVE"
ALLOWED_NATIVE_CLASSES = {ACTIVE, INACTIVE}

ALLOWED_TAXONOMY = {
    "PASS_SCOPED_BOSS_M300_CROSS_SURVEY_RESPONSE_REPLICATION",
    "SCIENTIFIC_RESPONSE_ZERO_OR_NONFINITE",
    "SCIENTIFIC_RESPONSE_REPRODUCIBILITY_FAIL",
    "SCIENTIFIC_RESPONSE_CONSTRUCTION_MISMATCH",
    "PROVENANCE_FAIL",
    "INVALID_IMPLEMENTATION",
}
PASS = "PASS_SCOPED_BOSS_M300_CROSS_SURVEY_RESPONSE_REPLICATION"

LANE_ARTIFACTS = {
  "R01": {
    "artifact_id": 10523240392,
    "name": "layerb-beta-v026-r1-minimal-numerical-R01-v0-1",
    "sha256": "ee95f22766aad94ecbea4b246b0b52918af3b271174a7021541948e41989ad19"
  },
  "R02": {
    "artifact_id": 10524117130,
    "name": "layerb-beta-v026-r1-minimal-numerical-R02-v0-1",
    "sha256": "5de470b8339f8f82dbf8d04bef727ba12ee15b01b12ef45b86dcc7680b14946a"
  },
  "R03": {
    "artifact_id": 10523105313,
    "name": "layerb-beta-v026-r1-minimal-numerical-R03-v0-1",
    "sha256": "05910abbb7ace4e45354be79502a4b4d7a721a4c4855132e62622edbba72a032"
  },
  "R04": {
    "artifact_id": 10523143744,
    "name": "layerb-beta-v026-r1-minimal-numerical-R04-v0-1",
    "sha256": "af04d485963f95db476eac902a974680bf58052cec391060b300e8eb3360d44e"
  },
  "R05": {
    "artifact_id": 10523060327,
    "name": "layerb-beta-v026-r1-minimal-numerical-R05-v0-1",
    "sha256": "017f2f91ae7a06e1cde8c7522a9cb768ff107df775b57988fb68de7a5717fcd6"
  },
  "R06": {
    "artifact_id": 10522119938,
    "name": "layerb-beta-v026-r1-minimal-numerical-R06-v0-1",
    "sha256": "2bcd0b1ed6c4b3da2ae0001ffc39a3591aed1dc1a376da024f5a6ed72ef80eb8"
  },
  "R07": {
    "artifact_id": 10521889308,
    "name": "layerb-beta-v026-r1-minimal-numerical-R07-v0-1",
    "sha256": "7de18e6a3e38da9e6afa6a3ae31f8b4fa5785a4a2774c00f3706b176b9f29841"
  },
  "R08": {
    "artifact_id": 10523686811,
    "name": "layerb-beta-v026-r1-minimal-numerical-R08-v0-1",
    "sha256": "0b4e3e42a2adfa174c0b766c28a14d9fb0e348abcd05cd13b1133cb95bffb244"
  },
  "R09": {
    "artifact_id": 10523533058,
    "name": "layerb-beta-v026-r1-minimal-numerical-R09-v0-1",
    "sha256": "9e4848945074b47b1e6f2bd1da2b51839a160247ac0b66ea6dc19e6fbe9e0f46"
  },
  "R10": {
    "artifact_id": 10523571519,
    "name": "layerb-beta-v026-r1-minimal-numerical-R10-v0-1",
    "sha256": "c238391b558d89ff82f69c3d2d705142c8bf4c66c7f7b31be5c9cafa9c17abc6"
  },
  "R11": {
    "artifact_id": 10523455046,
    "name": "layerb-beta-v026-r1-minimal-numerical-R11-v0-1",
    "sha256": "d24db04361f00c9ae2f34c36afe5482e982a33c6dcfea78415d8f93d40f0981f"
  },
  "R12": {
    "artifact_id": 10523452556,
    "name": "layerb-beta-v026-r1-minimal-numerical-R12-v0-1",
    "sha256": "d05aaef8e5b643caf340a3d7b7cdc12be71d8b743f84a5fce2e97b8922231a00"
  },
  "R13": {
    "artifact_id": 10523680602,
    "name": "layerb-beta-v026-r1-minimal-numerical-R13-v0-1",
    "sha256": "05fbcdbd9557403e0df611e578e0d5982dec26bca49cd41dd240afad688549d4"
  },
  "R14": {
    "artifact_id": 10523692853,
    "name": "layerb-beta-v026-r1-minimal-numerical-R14-v0-1",
    "sha256": "7b410a3fd4bb8fcd56d0ea22c26dc60387a8444d5387e37ff7b0562fd4180efe"
  },
  "R15": {
    "artifact_id": 10523455059,
    "name": "layerb-beta-v026-r1-minimal-numerical-R15-v0-1",
    "sha256": "03d7e73a5dde118e22effb15b718119a11cbceda9a55dee34a3ee927f9cd5d7b"
  },
  "R16": {
    "artifact_id": 10521988921,
    "name": "layerb-beta-v026-r1-minimal-numerical-R16-v0-1",
    "sha256": "ae640737ac5f0f1f252c08f1a0d5f98bc12d55ad1026b52e224100b4a9cd8b49"
  },
  "R17": {
    "artifact_id": 10523415017,
    "name": "layerb-beta-v026-r1-minimal-numerical-R17-v0-1",
    "sha256": "c6eaa3c2eb3d31b709fcc8fbd583e643c36164c45dc5fdf353095e3c63834473"
  },
  "R18": {
    "artifact_id": 10523295503,
    "name": "layerb-beta-v026-r1-minimal-numerical-R18-v0-1",
    "sha256": "ce9482417ac01b23c50069d67072c54cfa6bac7cbdb91677760ea92087b6c3bc"
  },
  "R19": {
    "artifact_id": 10522783710,
    "name": "layerb-beta-v026-r1-minimal-numerical-R19-v0-1",
    "sha256": "5f367d29309fd137bf47431b891547a798680d4efb19d5143eb23a5f8f1e2286"
  },
  "R20": {
    "artifact_id": 10523767086,
    "name": "layerb-beta-v026-r1-minimal-numerical-R20-v0-1",
    "sha256": "e2d66412d8d1e014ed991752743256a2fc04c17f1711683c23fc174cfaa53811"
  },
  "R21": {
    "artifact_id": 10522839934,
    "name": "layerb-beta-v026-r1-minimal-numerical-R21-v0-1",
    "sha256": "21723f39486d483018a137475846c5e70f93d06b32334adacab54218aa56b79e"
  },
  "R22": {
    "artifact_id": 10523352424,
    "name": "layerb-beta-v026-r1-minimal-numerical-R22-v0-1",
    "sha256": "0951c25939d49b149956be4d5f2f728e237887d7b72fc711b2d486bcb3481403"
  },
  "R23": {
    "artifact_id": 10524042336,
    "name": "layerb-beta-v026-r1-minimal-numerical-R23-v0-1",
    "sha256": "4a3ff182f934bef832763856b7beab67c9f942c282f69d57dd6a7e9015798d7e"
  },
  "R24": {
    "artifact_id": 10522633290,
    "name": "layerb-beta-v026-r1-minimal-numerical-R24-v0-1",
    "sha256": "27b5b5ea9ad6fa9835551aa7bee52dc824197e5a6641e44a64c927504ff6b930"
  },
  "R25": {
    "artifact_id": 10523550658,
    "name": "layerb-beta-v026-r1-minimal-numerical-R25-v0-1",
    "sha256": "b4f97670abf70aefa18553443a9896b2bffaa65659c7cdf6d64bfebb0d61b324"
  },
  "R26": {
    "artifact_id": 10522813881,
    "name": "layerb-beta-v026-r1-minimal-numerical-R26-v0-1",
    "sha256": "e41cb15f93d6fb44b032d0f2205a53527786fa87594ad8f5a5019920dadbac7a"
  },
  "R27": {
    "artifact_id": 10523740117,
    "name": "layerb-beta-v026-r1-minimal-numerical-R27-v0-1",
    "sha256": "308f23f03e7ebfbc622f6307d4c174a08b720a3f4f84dabf1681e3ba706f13a6"
  },
  "R28": {
    "artifact_id": 10522698898,
    "name": "layerb-beta-v026-r1-minimal-numerical-R28-v0-1",
    "sha256": "d8d35ce3f263ce2bbd265f477e3d544492f7f03f5552992b28eac8a4c62ec80d"
  },
  "R29": {
    "artifact_id": 10523132184,
    "name": "layerb-beta-v026-r1-minimal-numerical-R29-v0-1",
    "sha256": "89035658a7d751b74d21660f5d333c8db9679506118c64ac4106ae09fb42b872"
  },
  "R30": {
    "artifact_id": 10523112892,
    "name": "layerb-beta-v026-r1-minimal-numerical-R30-v0-1",
    "sha256": "474dacd17ad1f4dd7a0e35a76377b271ba3118252a7c7b7fba4d8c2fede17fb8"
  },
  "R31": {
    "artifact_id": 10522938361,
    "name": "layerb-beta-v026-r1-minimal-numerical-R31-v0-1",
    "sha256": "69d4deed0c6201e08022ec1a85e29c87480c03040bb07c993df21c803edad6c8"
  },
  "R32": {
    "artifact_id": 10523743733,
    "name": "layerb-beta-v026-r1-minimal-numerical-R32-v0-1",
    "sha256": "964acae9ceea1c5b53c9d1d5346e63c81dd3a1d6bb9046633b85cfac062fa887"
  }
}


class GateError(RuntimeError):
    def __init__(self, classification: str, stage: str, message: str):
        super().__init__(message)
        self.classification = classification
        self.stage = stage


def fail(classification: str, stage: str, message: str) -> None:
    if classification not in ALLOWED_TAXONOMY:
        raise RuntimeError(f"unfrozen classification {classification}")
    raise GateError(classification, stage, message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def blob_of(path: Path) -> str:
    return git_blob(path.read_bytes())


def canonical_sha(obj) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256(raw)


def normalize_digest(value: object) -> str:
    s = str(value or "")
    return s.split(":", 1)[1] if s.startswith("sha256:") else s


def require_blob(path: Path, expected: str, label: str) -> None:
    if not path.is_file():
        fail("PROVENANCE_FAIL", "authority_binding", f"missing {label}: {path}")
    actual = blob_of(path)
    if actual != expected:
        fail("PROVENANCE_FAIL", "authority_binding", f"{label} blob {actual} != {expected}")


def expected_keys() -> dict[str, tuple[str, str, int]]:
    out = {}
    for call in CALLS:
        for kind in ("mixed_target", "direct_target"):
            for role in ("beta_plus", "beta_minus"):
                key = f"{kind}__M300__{role}__call{call:03d}"
                out[key] = (kind, role, call)
    return out


EXPECTED_KEYS = expected_keys()


def validate_static_chain() -> dict:
    require_blob(PREREG, PREREG_BLOB, "preregistration")
    require_blob(DESIGN, DESIGN_BLOB, "design authority")
    require_blob(DESIGN_CRITIC, DESIGN_CRITIC_BLOB, "design static Critic")
    require_blob(AUTHORING_AUTHORITY, AUTHORING_AUTHORITY_BLOB, "implementation authoring authority")
    require_blob(NUMERICAL_RUNTIME_CRITIC, NUMERICAL_RUNTIME_CRITIC_BLOB, "numerical runtime Critic")

    design = json.loads(DESIGN.read_text(encoding="utf-8"))
    critic = json.loads(DESIGN_CRITIC.read_text(encoding="utf-8"))
    authoring = json.loads(AUTHORING_AUTHORITY.read_text(encoding="utf-8"))
    numerical = json.loads(NUMERICAL_RUNTIME_CRITIC.read_text(encoding="utf-8"))

    if design.get("status") != "PROSPECTIVE_DESIGN_ONLY_SCOPED_AUTHORITY":
        fail("PROVENANCE_FAIL", "authority_binding", "design status mismatch")
    if critic.get("verdict") != "PASS_SCOPED":
        fail("PROVENANCE_FAIL", "authority_binding", "design Critic not PASS_SCOPED")
    if authoring.get("status") != "PROSPECTIVE_IMPLEMENTATION_AUTHORING_AUTHORITY":
        fail("PROVENANCE_FAIL", "authority_binding", "authoring authority status mismatch")
    authz = authoring.get("authorization", {})
    if authz.get("implementation_authoring_authorized") is not True:
        fail("PROVENANCE_FAIL", "authority_binding", "implementation authoring not authorized")
    if authz.get("implementation_execution_authorized") is not False:
        fail("PROVENANCE_FAIL", "authority_binding", "authoring authority unexpectedly opens execution")
    if authz.get("M300_response_read_authorized") is not False:
        fail("PROVENANCE_FAIL", "authority_binding", "authoring authority unexpectedly opens response read")
    if numerical.get("verdict") != "CONFIRMED_SCOPED":
        fail("PROVENANCE_FAIL", "authority_binding", "numerical runtime Critic not CONFIRMED_SCOPED")
    if numerical.get("reviewed_run", {}).get("run_id") != SOURCE_RUN_ID:
        fail("PROVENANCE_FAIL", "authority_binding", "source run mismatch")

    obj = authoring.get("frozen_object", {})
    checks = {
        "selection": obj.get("mixed_selection") == "M300",
        "direct": obj.get("direct_batch") == "D58",
        "calls": obj.get("call_start") == 377 and obj.get("call_end") == 440 and obj.get("call_count") == 64,
        "unique_targets": obj.get("unique_exact_coordinates") == UNIQUE_TARGET_COUNT,
        "entries": obj.get("persisted_source_entries_per_call") == ENTRY_COUNT,
        "unique_hash": obj.get("unique_99_target_identity_sha256") == UNIQUE99_SHA256,
        "raw_hash": obj.get("raw_297_target_identity_sha256") == RAW297_SHA256,
        "h": obj.get("h") == H,
        "tech_tol": obj.get("technical_relative_tolerance_strict_lt") == TECH_TOL,
        "sci_tol": obj.get("mixed_direct_relative_tolerance_strict_lt") == SCI_TOL,
    }
    if not all(checks.values()):
        fail("PROVENANCE_FAIL", "authority_binding", f"frozen object mismatch {checks}")
    return authoring


def validate_execution_chain() -> None:
    validate_static_chain()
    for path, label in [
        (IMPLEMENTATION_CRITIC, "implementation static Critic"),
        (EXECUTION_AUTHORITY, "execution authority"),
        (WORKFLOW, "workflow"),
        (LAUNCH_MARKER, "launch marker"),
    ]:
        if not path.is_file():
            fail("PROVENANCE_FAIL", "execution_binding", f"missing {label}: {path}")

    critic = json.loads(IMPLEMENTATION_CRITIC.read_text(encoding="utf-8"))
    authority = json.loads(EXECUTION_AUTHORITY.read_text(encoding="utf-8"))
    marker = json.loads(LAUNCH_MARKER.read_text(encoding="utf-8"))

    if critic.get("verdict") != "PASS_SCOPED":
        fail("PROVENANCE_FAIL", "execution_binding", "implementation Critic not PASS_SCOPED")
    if authority.get("status") != "PROSPECTIVE_ONE_SHOT_EXECUTION_AUTHORITY":
        fail("PROVENANCE_FAIL", "execution_binding", "execution authority status mismatch")
    if authority.get("authorized_run_count") != 1:
        fail("PROVENANCE_FAIL", "execution_binding", "authorized run count mismatch")
    if authority.get("authorized_run_number") != 1 or authority.get("authorized_run_attempt") != 1:
        fail("PROVENANCE_FAIL", "execution_binding", "authorized run identity mismatch")
    if authority.get("source_run_id") != SOURCE_RUN_ID:
        fail("PROVENANCE_FAIL", "execution_binding", "execution source run mismatch")
    if authority.get("preregistration_git_blob_sha1") != PREREG_BLOB:
        fail("PROVENANCE_FAIL", "execution_binding", "prereg blob mismatch")
    if authority.get("design_authority_git_blob_sha1") != DESIGN_BLOB:
        fail("PROVENANCE_FAIL", "execution_binding", "design blob mismatch")
    if authority.get("design_static_critic_git_blob_sha1") != DESIGN_CRITIC_BLOB:
        fail("PROVENANCE_FAIL", "execution_binding", "design Critic blob mismatch")
    if authority.get("implementation_authoring_authority_git_blob_sha1") != AUTHORING_AUTHORITY_BLOB:
        fail("PROVENANCE_FAIL", "execution_binding", "authoring authority blob mismatch")
    if authority.get("numerical_runtime_critic_git_blob_sha1") != NUMERICAL_RUNTIME_CRITIC_BLOB:
        fail("PROVENANCE_FAIL", "execution_binding", "numerical Critic blob mismatch")
    if authority.get("implementation_git_blob_sha1") != blob_of(Path(__file__).resolve()):
        fail("PROVENANCE_FAIL", "execution_binding", "implementation blob mismatch")
    if authority.get("workflow_git_blob_sha1") != blob_of(WORKFLOW):
        fail("PROVENANCE_FAIL", "execution_binding", "workflow blob mismatch")
    if authority.get("implementation_static_critic_git_blob_sha1") != blob_of(IMPLEMENTATION_CRITIC):
        fail("PROVENANCE_FAIL", "execution_binding", "implementation Critic blob mismatch")
    if authority.get("terminal_taxonomy") != sorted(ALLOWED_TAXONOMY):
        fail("PROVENANCE_FAIL", "execution_binding", "terminal taxonomy mismatch")
    if marker.get("execution_authority_git_blob_sha1") != blob_of(EXECUTION_AUTHORITY):
        fail("PROVENANCE_FAIL", "execution_binding", "marker authority blob mismatch")
    if marker.get("source_run_id") != SOURCE_RUN_ID:
        fail("PROVENANCE_FAIL", "execution_binding", "marker source run mismatch")
    if marker.get("launch_once") is not True:
        fail("PROVENANCE_FAIL", "execution_binding", "marker launch_once mismatch")

    if os.environ.get("GITHUB_RUN_NUMBER") not in {None, "1"}:
        fail("INVALID_IMPLEMENTATION", "workflow_identity", "workflow run number is not 1")
    if os.environ.get("GITHUB_RUN_ATTEMPT") not in {None, "1"}:
        fail("INVALID_IMPLEMENTATION", "workflow_identity", "workflow run attempt is not 1")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def api_json(url: str, token: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "dsir-boss-m300-response-v0-1",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            if response.status != 200:
                fail("PROVENANCE_FAIL", "artifact_metadata", f"metadata HTTP {response.status}")
            return json.loads(response.read())
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403}:
            fail("INVALID_IMPLEMENTATION", "artifact_metadata_auth", f"GitHub metadata HTTP {exc.code}")
        fail("PROVENANCE_FAIL", "artifact_metadata_transport", f"GitHub metadata HTTP {exc.code}")
    except urllib.error.URLError as exc:
        fail("PROVENANCE_FAIL", "artifact_metadata_transport", f"GitHub metadata URL error: {exc.reason}")


def download_artifact_zip(api: str, repo: str, token: str, artifact_id: int) -> bytes:
    archive = f"{api}/repos/{repo}/actions/artifacts/{artifact_id}/zip"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "dsir-boss-m300-response-v0-1",
    }
    opener = urllib.request.build_opener(NoRedirect())
    location = None
    try:
        opener.open(urllib.request.Request(archive, headers=headers), timeout=60)
        fail("PROVENANCE_FAIL", "artifact_transport", "archive endpoint did not redirect")
    except urllib.error.HTTPError as exc:
        if exc.code in {301, 302, 303, 307, 308}:
            location = exc.headers.get("Location")
        elif exc.code in {401, 403}:
            fail("INVALID_IMPLEMENTATION", "artifact_archive_auth", f"GitHub archive API HTTP {exc.code}")
        else:
            fail("PROVENANCE_FAIL", "artifact_archive_transport", f"GitHub archive API HTTP {exc.code}")
    except urllib.error.URLError as exc:
        fail("PROVENANCE_FAIL", "artifact_archive_transport", f"GitHub archive URL error: {exc.reason}")
    if not location:
        fail("PROVENANCE_FAIL", "artifact_transport", "artifact redirect Location missing")
    parsed = urllib.parse.urlsplit(location)
    if parsed.scheme != "https" or not parsed.hostname:
        fail("PROVENANCE_FAIL", "artifact_transport", "invalid storage redirect")
    storage = urllib.request.Request(
        location,
        headers={"Accept": "application/octet-stream", "User-Agent": "dsir-boss-m300-response-v0-1"},
    )
    if any(k.lower() == "authorization" for k, _ in storage.header_items()):
        fail("INVALID_IMPLEMENTATION", "artifact_transport", "repository Authorization leaked to storage")
    try:
        with urllib.request.urlopen(storage, timeout=120) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403}:
            fail("INVALID_IMPLEMENTATION", "artifact_storage_auth", f"redirected storage HTTP {exc.code}")
        fail("PROVENANCE_FAIL", "artifact_storage_transport", f"redirected storage HTTP {exc.code}")
    except urllib.error.URLError as exc:
        fail("PROVENANCE_FAIL", "artifact_storage_transport", f"redirected storage URL error: {exc.reason}")


def validate_manifest_entry(meta: dict, key: str, kind: str, role: str, call: int) -> None:
    if meta.get("kind") != kind:
        fail("PROVENANCE_FAIL", "selected_array_binding", f"{key} kind mismatch")
    if meta.get("selection") != "M300":
        fail("PROVENANCE_FAIL", "selected_array_binding", f"{key} selection mismatch")
    if kind == "direct_target" and meta.get("direct_batch") != "D58":
        fail("PROVENANCE_FAIL", "selected_array_binding", f"{key} direct batch mismatch")
    if meta.get("role") != role:
        fail("PROVENANCE_FAIL", "selected_array_binding", f"{key} role mismatch")
    if meta.get("call_index") != call:
        fail("PROVENANCE_FAIL", "selected_array_binding", f"{key} call mismatch")
    if not isinstance(meta.get("z_u64hex"), str) or not meta["z_u64hex"]:
        fail("PROVENANCE_FAIL", "selected_array_binding", f"{key} z identity missing")
    if meta.get("target_u64hex_sha256") != RAW297_SHA256:
        fail("PROVENANCE_FAIL", "selected_array_binding", f"{key} raw target identity mismatch")
    if meta.get("shape") != [ENTRY_COUNT]:
        fail("PROVENANCE_FAIL", "selected_array_binding", f"{key} shape mismatch")
    if meta.get("dtype") != "<f8":
        fail("PROVENANCE_FAIL", "selected_array_binding", f"{key} dtype mismatch")
    if meta.get("byte_length") != ENTRY_COUNT * 8:
        fail("PROVENANCE_FAIL", "selected_array_binding", f"{key} byte length mismatch")
    h = meta.get("sha256")
    if not isinstance(h, str) or len(h) != 64:
        fail("PROVENANCE_FAIL", "selected_array_binding", f"{key} array SHA256 malformed")


def stage_all_sources() -> tuple[dict, list[dict]]:
    """Bind all 8192 selected arrays before any beta +/- arithmetic."""
    import numpy as np

    token = os.environ.get("GITHUB_TOKEN", "")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    api = os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/")
    if not token or not repo:
        fail("PROVENANCE_FAIL", "runtime_environment", "GITHUB_TOKEN/GITHUB_REPOSITORY missing")

    staged = {}
    provenance = []
    seen_classes = {ACTIVE: 0, INACTIVE: 0}
    seen_arms = {"A": 0, "B": 0}
    reference_z = None

    for rep in REPLICATES:
        spec = LANE_ARTIFACTS[rep]
        meta = api_json(f"{api}/repos/{repo}/actions/artifacts/{spec['artifact_id']}", token)
        if int(meta.get("id", -1)) != spec["artifact_id"]:
            fail("PROVENANCE_FAIL", "artifact_metadata", f"{rep} artifact id mismatch")
        if meta.get("name") != spec["name"]:
            fail("PROVENANCE_FAIL", "artifact_metadata", f"{rep} artifact name mismatch")
        if bool(meta.get("expired")):
            fail("PROVENANCE_FAIL", "artifact_metadata", f"{rep} artifact expired")
        if normalize_digest(meta.get("digest")) != spec["sha256"]:
            fail("PROVENANCE_FAIL", "artifact_metadata", f"{rep} GitHub digest mismatch")

        zip_bytes = download_artifact_zip(api, repo, token, spec["artifact_id"])
        if sha256(zip_bytes) != spec["sha256"]:
            fail("PROVENANCE_FAIL", "artifact_transport", f"{rep} downloaded ZIP SHA256 mismatch")

        receipt_name = f"receipt_{rep}.json"
        witness_name = f"witness_{rep}.npz"
        with zipfile.ZipFile(io.BytesIO(zip_bytes), "r") as zf:
            members = sorted(n for n in zf.namelist() if not n.endswith("/"))
            if members != sorted([receipt_name, witness_name]):
                fail("PROVENANCE_FAIL", "lane_archive", f"{rep} members mismatch")
            receipt_bytes = zf.read(receipt_name)
            witness_bytes = zf.read(witness_name)

        receipt = json.loads(receipt_bytes)
        if receipt.get("replicate") != rep:
            fail("PROVENANCE_FAIL", "lane_receipt", f"{rep} receipt replicate mismatch")
        if receipt.get("classification") != "LANE_PASS" or receipt.get("eligible") is not True:
            fail("PROVENANCE_FAIL", "lane_receipt", f"{rep} is not eligible LANE_PASS")
        native_class = receipt.get("native_class")
        if native_class not in ALLOWED_NATIVE_CLASSES:
            fail("PROVENANCE_FAIL", "lane_receipt", f"{rep} native class invalid")
        expected_arm = "A" if rep <= "R16" else "B"
        if receipt.get("order_arm") != expected_arm:
            fail("PROVENANCE_FAIL", "lane_receipt", f"{rep} order arm mismatch")
        seen_classes[native_class] += 1
        seen_arms[expected_arm] += 1

        solver = receipt.get("solver_receipt")
        if not isinstance(solver, dict):
            fail("PROVENANCE_FAIL", "lane_receipt", f"{rep} solver receipt missing")
        if solver.get("solver_construction_count") != 14:
            fail("PROVENANCE_FAIL", "lane_receipt", f"{rep} solver construction count mismatch")
        if solver.get("corrected_grid896_payload_sha256") != "8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d":
            fail("PROVENANCE_FAIL", "lane_receipt", f"{rep} GRID896 identity mismatch")
        for flag in (
            "derived_beta_response_constructed",
            "scientific_response_read",
            "covariance_read",
            "scientific_classifier_invoked",
            "response_dependent_decision",
            "full_107_row_execution",
        ):
            if solver.get(flag) is not False:
                fail("PROVENANCE_FAIL", "lane_receipt", f"{rep} forbidden parent flag true: {flag}")

        witness_sha = sha256(witness_bytes)
        if receipt.get("witness_npz_sha256") != witness_sha or solver.get("witness_npz_sha256") != witness_sha:
            fail("PROVENANCE_FAIL", "witness_binding", f"{rep} witness NPZ SHA256 mismatch")
        manifest = solver.get("witness_manifest")
        if not isinstance(manifest, dict):
            fail("PROVENANCE_FAIL", "witness_binding", f"{rep} witness manifest missing")
        if canonical_sha(manifest) != solver.get("witness_manifest_canonical_sha256"):
            fail("PROVENANCE_FAIL", "witness_binding", f"{rep} manifest canonical SHA256 mismatch")

        selected_manifest_keys = {
            k for k in manifest
            if k.startswith("mixed_target__M300__") or k.startswith("direct_target__M300__")
        }
        if selected_manifest_keys != set(EXPECTED_KEYS):
            fail("PROVENANCE_FAIL", "selected_array_binding", f"{rep} exact 256-key M300 set mismatch")

        lane = {"native_class": native_class, "order_arm": expected_arm, "mixed": {}, "direct": {}}
        lane_z = {}
        with np.load(io.BytesIO(witness_bytes), allow_pickle=False) as handle:
            if set(handle.files) != set(manifest):
                fail("PROVENANCE_FAIL", "witness_binding", f"{rep} NPZ member set mismatch")
            for key, (kind, role, call) in EXPECTED_KEYS.items():
                m = manifest[key]
                validate_manifest_entry(m, key, kind, role, call)
                lane_z.setdefault(call, set()).add(m["z_u64hex"])
                arr0 = handle[key]
                if arr0.dtype.str != "<f8":
                    fail("PROVENANCE_FAIL", "selected_array_binding", f"{rep} {key} runtime dtype mismatch")
                if list(arr0.shape) != [ENTRY_COUNT]:
                    fail("PROVENANCE_FAIL", "selected_array_binding", f"{rep} {key} runtime shape mismatch")
                arr = np.ascontiguousarray(arr0, dtype="<f8")
                if sha256(arr.tobytes()) != m["sha256"]:
                    fail("PROVENANCE_FAIL", "selected_array_binding", f"{rep} {key} array SHA256 mismatch")
                bucket = lane["mixed"] if kind == "mixed_target" else lane["direct"]
                bucket[(role, call)] = arr.copy()

        z_map = {}
        for call, zs in lane_z.items():
            if len(zs) != 1:
                fail("PROVENANCE_FAIL", "selected_array_binding", f"{rep} call {call} z identity disagreement")
            z_map[call] = next(iter(zs))
        if set(z_map) != set(CALLS):
            fail("PROVENANCE_FAIL", "selected_array_binding", f"{rep} call z-map mismatch")
        if reference_z is None:
            reference_z = z_map
        elif z_map != reference_z:
            fail("PROVENANCE_FAIL", "selected_array_binding", f"{rep} cross-lane z-map mismatch")

        staged[rep] = lane
        provenance.append({
            "replicate": rep,
            "artifact_id": spec["artifact_id"],
            "artifact_name": spec["name"],
            "outer_zip_sha256": spec["sha256"],
            "receipt_sha256": sha256(receipt_bytes),
            "witness_npz_sha256": witness_sha,
            "witness_manifest_canonical_sha256": solver.get("witness_manifest_canonical_sha256"),
            "native_class": native_class,
            "order_arm": expected_arm,
            "selected_array_count": len(EXPECTED_KEYS),
            "raw_297_target_identity_sha256": RAW297_SHA256,
            "unique_99_target_identity_sha256": UNIQUE99_SHA256,
            "z_u64hex_by_call": {str(k): v for k, v in sorted(z_map.items())},
            "selected_array_sha256": {k: manifest[k]["sha256"] for k in sorted(EXPECTED_KEYS)},
        })

    if set(staged) != set(REPLICATES):
        fail("PROVENANCE_FAIL", "population_binding", "exact R01..R32 staged set mismatch")
    if seen_classes != {ACTIVE: 10, INACTIVE: 22}:
        fail("PROVENANCE_FAIL", "population_binding", f"native-class population mismatch {seen_classes}")
    if seen_arms != {"A": 16, "B": 16}:
        fail("PROVENANCE_FAIL", "population_binding", f"order-arm population mismatch {seen_arms}")
    if sum(x["selected_array_count"] for x in provenance) != 8192:
        fail("PROVENANCE_FAIL", "population_binding", "selected array total is not 8192")

    return staged, provenance


def exact_rel_array(a, b):
    import numpy as np
    aa = np.asarray(a, dtype=np.float64)
    bb = np.asarray(b, dtype=np.float64)
    den = np.maximum(np.maximum(np.abs(aa), np.abs(bb)), np.finfo(np.float64).tiny)
    return np.abs(aa - bb) / den


def max_rel_with_index(a, b):
    import numpy as np
    q = exact_rel_array(a, b)
    if np.any(~np.isfinite(q)):
        return float("inf"), None
    idx = np.unravel_index(int(np.argmax(q)), q.shape)
    return float(q[idx]), tuple(int(x) for x in idx)


def construct_and_classify(staged: dict):
    """First function allowed to perform beta +/- response arithmetic."""
    import numpy as np

    mixed_rows = []
    direct_rows = []
    for rep in REPLICATES:
        lane = staged[rep]
        mixed_calls = []
        direct_calls = []
        for call in CALLS:
            mp = np.ascontiguousarray(lane["mixed"][("beta_plus", call)], dtype=np.float64)
            mm = np.ascontiguousarray(lane["mixed"][("beta_minus", call)], dtype=np.float64)
            dp = np.ascontiguousarray(lane["direct"][("beta_plus", call)], dtype=np.float64)
            dm = np.ascontiguousarray(lane["direct"][("beta_minus", call)], dtype=np.float64)
            mixed_calls.append(np.ascontiguousarray(np.abs((mp - mm) / (2.0 * H)), dtype="<f8"))
            direct_calls.append(np.ascontiguousarray(np.abs((dp - dm) / (2.0 * H)), dtype="<f8"))
        mixed_rows.append(np.stack(mixed_calls))
        direct_rows.append(np.stack(direct_calls))

    mixed = np.stack(mixed_rows)
    direct = np.stack(direct_rows)
    if list(mixed.shape) != [32, 64, ENTRY_COUNT] or list(direct.shape) != [32, 64, ENTRY_COUNT]:
        fail("INVALID_IMPLEMENTATION", "response_construction", "response tensor shape mismatch")

    mixed_good = np.isfinite(mixed) & (mixed > 0.0)
    direct_good = np.isfinite(direct) & (direct > 0.0)
    finite_positive_ok = bool(np.all(mixed_good) and np.all(direct_good))

    counterexample = None
    if not finite_positive_ok:
        for ri, rep in enumerate(REPLICATES):
            for ci, call in enumerate(CALLS):
                for ei in range(ENTRY_COUNT):
                    if not mixed_good[ri, ci, ei]:
                        counterexample = {
                            "failure_class":"SCIENTIFIC_RESPONSE_ZERO_OR_NONFINITE",
                            "replicate":rep,"construction":"mixed","call":call,"source_entry_index":ei,
                            "value":float(mixed[ri,ci,ei]),
                        }
                        break
                    if not direct_good[ri, ci, ei]:
                        counterexample = {
                            "failure_class":"SCIENTIFIC_RESPONSE_ZERO_OR_NONFINITE",
                            "replicate":rep,"construction":"direct","call":call,"source_entry_index":ei,
                            "value":float(direct[ri,ci,ei]),
                        }
                        break
                if counterexample:
                    break
            if counterexample:
                break

    metrics = {
        "mixed_cross_host_max_pairwise_rel": None,
        "direct_cross_host_max_pairwise_rel": None,
        "mixed_native_class_mean_rel_separation": None,
        "direct_native_class_mean_rel_separation": None,
        "mixed_direct_response_max_rel": None,
        "execution_order_arm_mean_rel_separation_descriptive_mixed": None,
        "execution_order_arm_mean_rel_separation_descriptive_direct": None,
    }
    metric_argmax = {}

    if not finite_positive_ok:
        classification = "SCIENTIFIC_RESPONSE_ZERO_OR_NONFINITE"
    else:
        max_m = (-1.0, None)
        max_d = (-1.0, None)
        for ia, ib in itertools.combinations(range(len(REPLICATES)), 2):
            qm, idxm = max_rel_with_index(mixed[ia], mixed[ib])
            qd, idxd = max_rel_with_index(direct[ia], direct[ib])
            if qm > max_m[0]:
                max_m = (qm, (REPLICATES[ia], REPLICATES[ib], idxm))
            if qd > max_d[0]:
                max_d = (qd, (REPLICATES[ia], REPLICATES[ib], idxd))
        metrics["mixed_cross_host_max_pairwise_rel"] = max_m[0]
        metrics["direct_cross_host_max_pairwise_rel"] = max_d[0]
        metric_argmax["mixed_cross_host"] = max_m[1]
        metric_argmax["direct_cross_host"] = max_d[1]

        active_idx = [i for i,r in enumerate(REPLICATES) if staged[r]["native_class"] == ACTIVE]
        inactive_idx = [i for i,r in enumerate(REPLICATES) if staged[r]["native_class"] == INACTIVE]
        m_active = np.mean(mixed[active_idx], axis=0)
        m_inactive = np.mean(mixed[inactive_idx], axis=0)
        d_active = np.mean(direct[active_idx], axis=0)
        d_inactive = np.mean(direct[inactive_idx], axis=0)
        metrics["mixed_native_class_mean_rel_separation"], metric_argmax["mixed_native_class"] = max_rel_with_index(m_active, m_inactive)
        metrics["direct_native_class_mean_rel_separation"], metric_argmax["direct_native_class"] = max_rel_with_index(d_active, d_inactive)

        arm_a = list(range(16))
        arm_b = list(range(16,32))
        metrics["execution_order_arm_mean_rel_separation_descriptive_mixed"], metric_argmax["order_arm_mixed"] = max_rel_with_index(
            np.mean(mixed[arm_a],axis=0), np.mean(mixed[arm_b],axis=0))
        metrics["execution_order_arm_mean_rel_separation_descriptive_direct"], metric_argmax["order_arm_direct"] = max_rel_with_index(
            np.mean(direct[arm_a],axis=0), np.mean(direct[arm_b],axis=0))

        repro_metrics = [
            metrics["mixed_cross_host_max_pairwise_rel"],
            metrics["direct_cross_host_max_pairwise_rel"],
            metrics["mixed_native_class_mean_rel_separation"],
            metrics["direct_native_class_mean_rel_separation"],
        ]
        if not all(float(x) < TECH_TOL for x in repro_metrics):
            classification = "SCIENTIFIC_RESPONSE_REPRODUCIBILITY_FAIL"
            for ri, rep in enumerate(REPLICATES):
                for rj in range(ri+1, len(REPLICATES)):
                    qm = exact_rel_array(mixed[ri], mixed[rj])
                    bad = np.argwhere(qm >= TECH_TOL)
                    if bad.size:
                        ci, ei = map(int,bad[0])
                        counterexample = {
                            "failure_class":classification,"metric":"mixed_cross_host",
                            "replicate_a":rep,"replicate_b":REPLICATES[rj],
                            "call":CALLS[ci],"source_entry_index":ei,"relative_difference":float(qm[ci,ei])
                        }
                        break
                    qd = exact_rel_array(direct[ri], direct[rj])
                    bad = np.argwhere(qd >= TECH_TOL)
                    if bad.size:
                        ci, ei = map(int,bad[0])
                        counterexample = {
                            "failure_class":classification,"metric":"direct_cross_host",
                            "replicate_a":rep,"replicate_b":REPLICATES[rj],
                            "call":CALLS[ci],"source_entry_index":ei,"relative_difference":float(qd[ci,ei])
                        }
                        break
                if counterexample:
                    break
        else:
            qmd = exact_rel_array(mixed, direct)
            idx = np.unravel_index(int(np.argmax(qmd)), qmd.shape)
            metrics["mixed_direct_response_max_rel"] = float(qmd[idx])
            metric_argmax["mixed_direct"] = {
                "replicate":REPLICATES[idx[0]],"call":CALLS[idx[1]],"source_entry_index":int(idx[2])
            }
            if not metrics["mixed_direct_response_max_rel"] < SCI_TOL:
                classification = "SCIENTIFIC_RESPONSE_CONSTRUCTION_MISMATCH"
                bad = np.argwhere(qmd >= SCI_TOL)[0]
                ri, ci, ei = map(int,bad)
                counterexample = {
                    "failure_class":classification,
                    "replicate":REPLICATES[ri],"call":CALLS[ci],"source_entry_index":ei,
                    "mixed_value":float(mixed[ri,ci,ei]),
                    "direct_value":float(direct[ri,ci,ei]),
                    "relative_difference":float(qmd[ri,ci,ei])
                }
            else:
                classification = PASS

    result = {
        "schema":"LAYERB_BETA_V0_26_R1_BOSS_M300_CROSS_SURVEY_RESPONSE_REPLICATION_DECISION_V0_1",
        "classification":classification,
        "effect":"+0/+0",
        "interpretation_ceiling":"CROSS_SURVEY_RESPONSE_EXISTENCE_REPRODUCIBILITY_AND_CONSTRUCTION_STABILITY_ONLY",
        "source_run_id":SOURCE_RUN_ID,
        "survey":"BOSS",
        "mixed_selection":"M300",
        "direct_batch":"D58",
        "calls":CALLS,
        "call_count":len(CALLS),
        "unique_exact_coordinates":UNIQUE_TARGET_COUNT,
        "persisted_source_entries_per_call":ENTRY_COUNT,
        "replicate_count":len(REPLICATES),
        "h":H,
        "response_formula":"abs((beta_plus-beta_minus)/(2*h))",
        "response_tensor_shape_per_construction":[32,64,ENTRY_COUNT],
        "atoms_per_construction":int(mixed.size),
        "combined_atoms":int(mixed.size+direct.size),
        "finite_positive_status":finite_positive_ok,
        "mixed_response_min":float(np.min(mixed)) if np.all(np.isfinite(mixed)) else None,
        "mixed_response_max":float(np.max(mixed)) if np.all(np.isfinite(mixed)) else None,
        "direct_response_min":float(np.min(direct)) if np.all(np.isfinite(direct)) else None,
        "direct_response_max":float(np.max(direct)) if np.all(np.isfinite(direct)) else None,
        "technical_relative_tolerance_strict_lt":TECH_TOL,
        "scientific_construction_agreement_tolerance_strict_lt":SCI_TOL,
        "metrics":metrics,
        "metric_argmax":metric_argmax,
        "smallest_exact_counterexample":counterexample,
        "provenance_complete_before_response_arithmetic":True,
        "new_CLASS_solves":0,
        "M300_response_read":True,
        "scientific_classifier_invoked":True,
        "covariance_read":False,
        "whitening_read":False,
        "nuisance_read":False,
        "relation_null_read":False,
        "Wm_S3_opened":False,
        "global_65537_opened":False,
        "full107_execution":False,
        "response_dependent_selection":False,
        "statistical_inference_authorized":False,
        "physical_inference_authorized":False,
        "DES_BOSS_amplitude_equality_tested":False,
    }
    return result, mixed, direct


def write_json(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def static_contract_report(out: Path) -> int:
    validate_static_chain()
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module)
    checks = {
        "no_classy_module_import":"classy" not in imported,
        "no_subprocess_module_import":"subprocess" not in imported,
        "exact_call_range":CALLS == list(range(377,441)),
        "exact_64_calls":len(CALLS) == 64,
        "exact_297_entries":ENTRY_COUNT == 297,
        "exact_99_unique_targets":UNIQUE_TARGET_COUNT == 99,
        "exact_256_selected_arrays_per_lane":len(EXPECTED_KEYS) == 256,
        "exact_8192_selected_arrays_population":len(EXPECTED_KEYS)*len(REPLICATES) == 8192,
        "exact_h":H == 1e-4,
        "exact_technical_tolerance":TECH_TOL == 1e-5,
        "exact_scientific_tolerance":SCI_TOL == 1e-3,
        "raw_target_hash_exact":RAW297_SHA256 == "e5bcdcb7fbb802b24469d8e3f1965013dc35b3b9249868476cf22490456f344a",
        "unique_target_hash_exact":UNIQUE99_SHA256 == "a44a8921e3c10b17cdf222b97d18524454e927dadeea30b13e75c3a0d6fc42fc",
    }
    if not all(checks.values()):
        fail("INVALID_IMPLEMENTATION", "static_contract", f"static check failure {checks}")
    write_json(out, {
        "schema":"LAYERB_BETA_V0_26_R1_BOSS_M300_STATIC_CONTRACT_REPORT_V0_1",
        "classification":"PASS_STATIC_CONTRACT",
        "checks":checks,
        "M300_response_read":False,
        "scientific_classifier_invoked":False,
        "new_CLASS_solves":0,
    })
    return 0


def execute(outdir: Path) -> int:
    import numpy as np
    outdir.mkdir(parents=True, exist_ok=True)
    base = {
        "schema":"LAYERB_BETA_V0_26_R1_BOSS_M300_CROSS_SURVEY_RESPONSE_REPLICATION_DECISION_V0_1",
        "classification":"INVALID_IMPLEMENTATION",
        "effect":"+0/+0",
        "source_run_id":SOURCE_RUN_ID,
        "M300_response_read":False,
        "scientific_classifier_invoked":False,
        "covariance_read":False,
        "nuisance_read":False,
        "full107_execution":False,
        "new_CLASS_solves":0,
        "provenance_complete_before_response_arithmetic":False,
    }
    try:
        validate_execution_chain()
        staged, provenance = stage_all_sources()
        write_json(outdir/"provenance.json",{
            "schema":"LAYERB_BETA_V0_26_R1_BOSS_M300_PROVENANCE_V0_1",
            "source_run_id":SOURCE_RUN_ID,
            "exact_lane_count":len(provenance),
            "exact_lane_set":REPLICATES,
            "selected_array_bindings_verified":sum(x["selected_array_count"] for x in provenance),
            "all_bindings_passed_before_response_arithmetic":True,
            "records":provenance,
        })
        result, mixed, direct = construct_and_classify(staged)
        np.savez_compressed(
            outdir/"response_evidence.npz",
            R_mixed=np.ascontiguousarray(mixed,dtype="<f8"),
            R_direct=np.ascontiguousarray(direct,dtype="<f8"),
        )
        result["response_evidence_npz_sha256"] = sha256((outdir/"response_evidence.npz").read_bytes())
        result["provenance_json_sha256"] = sha256((outdir/"provenance.json").read_bytes())
        write_json(outdir/"result.json",result)
        return 0
    except GateError as exc:
        base["classification"]=exc.classification
        base["failure_stage"]=exc.stage
        base["error"]=str(exc)
        write_json(outdir/"result.json",base)
        return 0
    except Exception as exc:
        base["classification"]="INVALID_IMPLEMENTATION"
        base["failure_stage"]="unexpected"
        base["error"]=f"{type(exc).__name__}: {exc}"
        write_json(outdir/"result.json",base)
        return 0


def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument("--mode",choices=["static-contract","execute"],required=True)
    p.add_argument("--out")
    p.add_argument("--outdir")
    a=p.parse_args()
    if a.mode=="static-contract":
        if not a.out:
            raise SystemExit("--out required")
        return static_contract_report(Path(a.out))
    if not a.outdir:
        raise SystemExit("--outdir required")
    return execute(Path(a.outdir))


if __name__ == "__main__":
    raise SystemExit(main())
