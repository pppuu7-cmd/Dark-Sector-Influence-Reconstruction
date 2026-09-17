#!/usr/bin/env python3
"""Response-blind corrected content-addressed producer / cross-host population validity gate."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_V01 = ROOT / "docs/dsir4/canonical/LAYERB_BETA_V0_26_R1_GRID896_U64HEX_V0_1.txt"
DESIGN_AUTHORITY = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_CORRECTED_PRODUCER_CROSS_HOST_POPULATION_VALIDITY_DESIGN_AUTHORITY_V0_1.json"
DESIGN_CRITIC = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_CORRECTED_PRODUCER_CROSS_HOST_POPULATION_VALIDITY_DESIGN_STATIC_CRITIC_V0_1.json"
PAIR_TERMINAL = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_CORRECTED_REPAIR_PAIR_OPERATION_BOUND_QUALIFICATION_TERMINAL_V0_1.json"
PAIR_RUNTIME_CRITIC = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_CORRECTED_REPAIR_PAIR_OPERATION_BOUND_QUALIFICATION_RUNTIME_CRITIC_V0_1.json"
V022_CONTRACT = ROOT / "docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_V0_22.json"
V022_EXECUTOR = ROOT / "ci/layerb_beta_forced_baseline_cross_host_reproducibility_v0_22.py"
DISPATCH_CONSUMPTION = ROOT / "docs/dsir4/runtime/LAYERB_BETA_V0_26_R1_GRID896_DISPATCH_DIAGNOSTIC_CONSUMPTION_V0_1.json"
DISPATCH_CRITIC = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_GRID896_DISPATCH_DIAGNOSTIC_INDEPENDENT_CRITIC_V0_1.json"

DESIGN_AUTHORITY_BLOB = "e45a724eee83418d192b12c64e12b08050aa7011"
DESIGN_CRITIC_BLOB = "b4a67e6339bbe94bcdf64130c334c46e4e007dc2"
PAIR_TERMINAL_BLOB = "3cfc4624a770502bf3b55a4d3768bb1606132e85"
PAIR_RUNTIME_CRITIC_BLOB = "a7d5aaf4e0f388e64d747552f29acfa3473f483a"
V022_CONTRACT_BLOB = "697f40226525c633f76e3269300dbb6d71705d7e"
V022_EXECUTOR_BLOB = "7921f856f468d9b73889130df39148ccca3d048d"
DISPATCH_CONSUMPTION_BLOB = "b3a3a2b68a6d275f29e18c8ed035d49599fd9dbb"
DISPATCH_CRITIC_BLOB = "dce5e48ea065c5fba716a71cc9ff37e4126ddde8"

REPLICATES = [f"R{i:02d}" for i in range(1, 33)]
NATIVE_CLASSES = ["NATIVE_AVX512_ACTIVE", "NATIVE_AVX512_INACTIVE"]
MIN_ELIGIBLE = 6
MIN_PER_CLASS = 3

V01_BLOB = "24fa61685ab45e42e3ab0d453f5cb223c247ced6"
V01_LEN = 15248
V01_SHA256 = "f84d6fa7cf9e5b8014176fd480062b27aaf97947d4a5211c7fbb5c69f93634ba"
INSERT_OFFSET = 13182
INSERT_BYTE = b"e"
CORRECTED_LEN = 15249
CORRECTED_SHA256 = "e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4"
CORRECTED_BLOB = "ded43b233a71a631809111514c9dd35d0419af2d"
LINE_COUNT = 897
PAYLOAD_LEN = 7176
PAYLOAD_SHA256 = "8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d"

FROZEN_NUMPY = "1.26.4"
FROZEN_BASELINE = ["SSE", "SSE2", "SSE3"]
FROZEN_DISPATCH = [
    "SSSE3", "SSE41", "POPCNT", "SSE42", "AVX", "F16C", "FMA3", "AVX2",
    "AVX512F", "AVX512CD", "AVX512_KNL", "AVX512_KNM", "AVX512_SKX",
    "AVX512_CLX", "AVX512_CNL", "AVX512_ICL",
]
FROZEN_AVX512_DISPATCH = [
    "AVX512CD", "AVX512F", "AVX512_CLX", "AVX512_CNL", "AVX512_ICL",
    "AVX512_KNL", "AVX512_KNM", "AVX512_SKX",
]
FROZEN_ACTIVE_NON = ["AVX", "AVX2", "F16C", "FMA3", "POPCNT", "SSE41", "SSE42", "SSSE3"]


class GateError(RuntimeError):
    def __init__(self, classification: str, stage: str, message: str):
        super().__init__(message)
        self.classification = classification
        self.stage = stage


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def blob_of(path: Path) -> str:
    return git_blob(path.read_bytes())


def fail(classification: str, stage: str, message: str) -> None:
    raise GateError(classification, stage, message)


def require_blob(path: Path, expected: str, stage: str) -> None:
    actual = blob_of(path)
    if actual != expected:
        fail("PROVENANCE_FAIL", stage, f"Git blob mismatch for {path}: {actual} != {expected}")


def validate_static_dependencies() -> None:
    for path, expected in [
        (DESIGN_AUTHORITY, DESIGN_AUTHORITY_BLOB),
        (DESIGN_CRITIC, DESIGN_CRITIC_BLOB),
        (PAIR_TERMINAL, PAIR_TERMINAL_BLOB),
        (PAIR_RUNTIME_CRITIC, PAIR_RUNTIME_CRITIC_BLOB),
        (V022_CONTRACT, V022_CONTRACT_BLOB),
        (V022_EXECUTOR, V022_EXECUTOR_BLOB),
        (DISPATCH_CONSUMPTION, DISPATCH_CONSUMPTION_BLOB),
        (DISPATCH_CRITIC, DISPATCH_CRITIC_BLOB),
    ]:
        require_blob(path, expected, "dependency_binding")

    design = json.loads(DESIGN_AUTHORITY.read_text(encoding="utf-8"))
    critic = json.loads(DESIGN_CRITIC.read_text(encoding="utf-8"))
    pair = json.loads(PAIR_TERMINAL.read_text(encoding="utf-8"))
    pair_critic = json.loads(PAIR_RUNTIME_CRITIC.read_text(encoding="utf-8"))
    dispatch = json.loads(DISPATCH_CONSUMPTION.read_text(encoding="utf-8"))
    if design.get("status") != "PROSPECTIVE_DESIGN_ONLY_SCOPED_AUTHORITY":
        fail("PROVENANCE_FAIL", "dependency_binding", "producer design authority status mismatch")
    if critic.get("verdict") != "PASS_SCOPED":
        fail("PROVENANCE_FAIL", "dependency_binding", "producer design Critic is not PASS_SCOPED")
    if pair.get("classification") != "PASS_SCOPED_CORRECTED_REPAIR_PAIR_OPERATIONALLY_QUALIFIED":
        fail("PROVENANCE_FAIL", "dependency_binding", "repair-pair terminal classification mismatch")
    if pair_critic.get("classification") != "CORRECTED_REPAIR_PAIR_OPERATIONAL_PASS_RUNTIME_CONFIRMED":
        fail("PROVENANCE_FAIL", "dependency_binding", "repair-pair runtime Critic classification mismatch")
    if dispatch.get("classification") != "GRID896_NUMPY_DISPATCH_PATH_DEPENDENCE_CONFIRMED":
        fail("PROVENANCE_FAIL", "dependency_binding", "dispatch diagnostic classification mismatch")
    frozen_payload = design.get("frozen_corrected_payload") or {}
    if frozen_payload.get("byte_length") != PAYLOAD_LEN or frozen_payload.get("sha256") != PAYLOAD_SHA256:
        fail("PROVENANCE_FAIL", "dependency_binding", "design frozen payload mismatch")
    pop = design.get("candidate_population_contract") or {}
    if pop.get("replicate_ids") != REPLICATES or int(pop.get("candidate_receipt_count_required", 0)) != 32:
        fail("PROVENANCE_FAIL", "dependency_binding", "design candidate population mismatch")
    if int(pop.get("minimum_eligible_lane_n", 0)) != MIN_ELIGIBLE or int(pop.get("minimum_per_native_class_n", 0)) != MIN_PER_CLASS:
        fail("PROVENANCE_FAIL", "dependency_binding", "design power contract mismatch")


def cpuinfo_record() -> dict:
    fields: dict[str, str] = {}
    flags: set[str] = set()
    p = Path("/proc/cpuinfo")
    if p.exists():
        for line in p.read_text(errors="replace").splitlines():
            if ":" not in line:
                continue
            key, value = [x.strip() for x in line.split(":", 1)]
            if key in {"vendor_id", "cpu family", "model", "stepping", "microcode", "model name"} and key not in fields:
                fields[key] = " ".join(value.split())
            if key in {"flags", "Features"} and not flags:
                flags = set(value.split())
    model = {
        "vendor_id": fields.get("vendor_id", ""),
        "family": fields.get("cpu family", ""),
        "model": fields.get("model", ""),
        "stepping": fields.get("stepping", ""),
        "model_name": fields.get("model name", ""),
    }
    selected = {k: (k in flags) for k in ["avx", "avx2", "avx512f", "avx512dq", "avx512cd", "avx512bw", "avx512vl", "fma", "sse4_2"]}
    return {
        "cpu_model": model,
        "microcode": fields.get("microcode", ""),
        "selected_cpu_features": selected,
        "cpu_flags_sha256": hashlib.sha256(" ".join(sorted(flags)).encode()).hexdigest(),
    }


def numpy_record() -> dict:
    # NumPy is used only for response-free dispatch fingerprinting. It is never used by materialize_payload().
    import numpy as np
    from numpy.core._multiarray_umath import __cpu_features__, __cpu_baseline__, __cpu_dispatch__

    features = {str(k): bool(v) for k, v in dict(__cpu_features__).items()}
    baseline = [str(x) for x in list(__cpu_baseline__)]
    dispatch = [str(x) for x in list(__cpu_dispatch__)]
    active = sorted(x for x in dispatch if features.get(x, False))
    avx512_dispatch = sorted(x for x in dispatch if x.upper().startswith("AVX512"))
    active_avx512 = sorted(x for x in avx512_dispatch if features.get(x, False))
    active_non = sorted(x for x in active if not x.upper().startswith("AVX512"))
    raw_avx512 = {k: v for k, v in features.items() if k.upper().startswith("AVX512")}
    return {
        "numpy": np.__version__,
        "baseline": baseline,
        "dispatch": dispatch,
        "features": features,
        "active_dispatch": active,
        "avx512_dispatch": avx512_dispatch,
        "active_avx512_dispatch": active_avx512,
        "active_non_avx512_dispatch": active_non,
        "avx512_features": raw_avx512,
        "any_avx512_enabled": any(raw_avx512.values()),
    }


def response_free_fingerprint() -> dict:
    n = numpy_record()
    return {
        "cpu": cpuinfo_record(),
        "numpy": n,
        "environment": {
            "NPY_DISABLE_CPU_FEATURES": os.environ.get("NPY_DISABLE_CPU_FEATURES", ""),
            "GLIBC_TUNABLES": os.environ.get("GLIBC_TUNABLES", ""),
        },
        "software": {
            "python": platform.python_version(),
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "numpy": n["numpy"],
        },
        "no_class_import": True,
        "no_dsir_response": True,
        "raw_cpu_capability_bits_validation_target": False,
    }


def native_candidate_ok(fp: dict) -> bool:
    n = fp["numpy"]
    return bool(
        n["numpy"] == FROZEN_NUMPY
        and n["baseline"] == FROZEN_BASELINE
        and n["dispatch"] == FROZEN_DISPATCH
        and n["avx512_dispatch"] == FROZEN_AVX512_DISPATCH
        and n["active_non_avx512_dispatch"] == FROZEN_ACTIVE_NON
        and fp["environment"]["NPY_DISABLE_CPU_FEATURES"] == ""
    )


def native_class(fp: dict) -> str:
    return "NATIVE_AVX512_ACTIVE" if fp["numpy"]["active_avx512_dispatch"] else "NATIVE_AVX512_INACTIVE"


def materialize_payload(output_path: Path) -> tuple[bytes, bytes]:
    # Pure content-addressed byte path. No NumPy, floating point, solver, or scientific response is used here.
    raw = CANONICAL_V01.read_bytes()
    if len(raw) != V01_LEN or sha256(raw) != V01_SHA256 or git_blob(raw) != V01_BLOB:
        fail("PROVENANCE_FAIL", "historical_source", "historical V0.1 identity mismatch")
    if not raw.endswith(b"\n"):
        fail("PROVENANCE_FAIL", "historical_source", "historical V0.1 final LF mismatch")
    historical_lines = raw.splitlines()
    if len(historical_lines) != LINE_COUNT or historical_lines[775] != b"3f9c8a9eea3c9c8":
        fail("PROVENANCE_FAIL", "historical_source", "historical V0.1 structure mismatch")

    corrected = raw[:INSERT_OFFSET] + INSERT_BYTE + raw[INSERT_OFFSET:]
    if len(corrected) != CORRECTED_LEN or sha256(corrected) != CORRECTED_SHA256 or git_blob(corrected) != CORRECTED_BLOB:
        fail("PRODUCER_CONTENT_IDENTITY_FAIL", "corrected_source", "corrected canonical identity mismatch")
    lines = corrected.splitlines()
    if len(lines) != LINE_COUNT or lines[775] != b"3f9c8a9eeea3c9c8":
        fail("PRODUCER_CONTENT_IDENTITY_FAIL", "corrected_source", "corrected canonical structure mismatch")
    if any(len(line) != 16 or any(c not in b"0123456789abcdef" for c in line) for line in lines):
        fail("PRODUCER_CONTENT_IDENTITY_FAIL", "corrected_source", "corrected lowercase hex16 grammar mismatch")

    # Each 16-hex word is serialized as the exact little-endian 8-byte representation.
    payload = b"".join(bytes.fromhex(line.decode("ascii"))[::-1] for line in lines)
    if len(payload) != PAYLOAD_LEN or sha256(payload) != PAYLOAD_SHA256:
        fail("PRODUCER_CONTENT_IDENTITY_FAIL", "materialization", "materialized payload identity mismatch")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(payload)
    reloaded = output_path.read_bytes()
    if len(reloaded) != PAYLOAD_LEN or sha256(reloaded) != PAYLOAD_SHA256:
        fail("PRODUCER_CONTENT_IDENTITY_FAIL", "reload", "reloaded payload identity mismatch")
    return payload, reloaded


def base_receipt(replicate: str) -> dict:
    return {
        "schema": "LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_CORRECTED_PRODUCER_CROSS_HOST_POPULATION_LANE_V0_1",
        "replicate": replicate,
        "candidate": False,
        "eligible": False,
        "native_class": None,
        "native_response_free_fingerprint": None,
        "runner_os": os.environ.get("RUNNER_OS", platform.system()),
        "runner_arch": os.environ.get("RUNNER_ARCH", platform.machine()),
        "python_version": platform.python_version(),
        "numpy_version": None,
        "producer_attempted": False,
        "producer_succeeded": False,
        "output_byte_length": None,
        "output_sha256": None,
        "reload_sha256": None,
        "failure_stage": None,
        "failure_classification": None,
        "failure_message": None,
        "run_id": int(os.environ.get("GITHUB_RUN_ID", "0") or 0),
        "run_number": int(os.environ.get("GITHUB_RUN_NUMBER", "0") or 0),
        "run_attempt": int(os.environ.get("GITHUB_RUN_ATTEMPT", "0") or 0),
        "head_sha": os.environ.get("GITHUB_SHA", ""),
        "class_solver_invoked": False,
        "scientific_response_read": False,
        "covariance_read": False,
        "scientific_classifier_invoked": False,
        "response_dependent_decision": False,
        "raw_cpu_capability_bits_validation_target": False,
        "effect": "+0/+0",
        "interpretation_ceiling": "INFRASTRUCTURE_NUMERICAL_POPULATION_VALIDITY_ONLY",
    }


def write_json(path: Path, doc: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def lane_mode(replicate: str, out: Path, materialized: Path) -> int:
    receipt = base_receipt(replicate)
    try:
        if replicate not in REPLICATES:
            fail("PROVENANCE_FAIL", "replicate_binding", f"unfrozen replicate {replicate}")
        validate_static_dependencies()
        try:
            fp = response_free_fingerprint()
        except Exception as exc:
            receipt["failure_stage"] = "NATIVE_FINGERPRINT"
            receipt["failure_classification"] = "BLOCKED_NATIVE_FINGERPRINT_PROFILE_DRIFT"
            receipt["failure_message"] = f"{type(exc).__name__}: {exc}"
            write_json(out, receipt)
            print(receipt["failure_classification"], replicate)
            return 0

        receipt["native_response_free_fingerprint"] = fp
        receipt["numpy_version"] = fp["numpy"]["numpy"]
        candidate = native_candidate_ok(fp)
        receipt["candidate"] = candidate
        if not candidate:
            receipt["failure_stage"] = "NATIVE_FINGERPRINT"
            receipt["failure_classification"] = "BLOCKED_NATIVE_FINGERPRINT_PROFILE_DRIFT"
            receipt["failure_message"] = "frozen V0.22 response-free NumPy profile mismatch"
            write_json(out, receipt)
            print(receipt["failure_classification"], replicate)
            return 0

        receipt["eligible"] = True
        receipt["native_class"] = native_class(fp)
        receipt["producer_attempted"] = True
        payload, reloaded = materialize_payload(materialized)
        receipt["producer_succeeded"] = True
        receipt["output_byte_length"] = len(payload)
        receipt["output_sha256"] = sha256(payload)
        receipt["reload_sha256"] = sha256(reloaded)
        receipt["failure_classification"] = "LANE_PASS"
        write_json(out, receipt)
        print("LANE_PASS", replicate, receipt["native_class"], receipt["output_sha256"])
        return 0
    except GateError as exc:
        receipt["failure_stage"] = exc.stage
        receipt["failure_classification"] = exc.classification
        receipt["failure_message"] = str(exc)
    except Exception as exc:
        receipt["failure_stage"] = "UNEXPECTED"
        receipt["failure_classification"] = "INVALID_IMPLEMENTATION"
        receipt["failure_message"] = f"{type(exc).__name__}: {exc}"
    write_json(out, receipt)
    print(receipt["failure_classification"], replicate, receipt["failure_stage"])
    return 0


def required_receipt_fields() -> set[str]:
    return {
        "replicate", "candidate", "eligible", "native_class", "native_response_free_fingerprint",
        "runner_os", "runner_arch", "python_version", "numpy_version", "producer_attempted",
        "producer_succeeded", "output_byte_length", "output_sha256", "reload_sha256", "failure_stage",
        "failure_classification", "run_id", "run_attempt", "head_sha", "class_solver_invoked",
        "scientific_response_read", "covariance_read", "scientific_classifier_invoked",
        "response_dependent_decision",
    }


def decision_mode(inputs: list[str], out: Path) -> int:
    decision = {
        "schema": "LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_CORRECTED_PRODUCER_CROSS_HOST_POPULATION_DECISION_V0_1",
        "classification": "INVALID_IMPLEMENTATION",
        "effect": "+0/+0",
        "interpretation_ceiling": "INFRASTRUCTURE_NUMERICAL_POPULATION_VALIDITY_ONLY",
        "candidate_receipt_count": 0,
        "eligible_lane_count": 0,
        "native_class_counts": {c: 0 for c in NATIVE_CLASSES},
        "eligible_replicates": [],
        "producer_success_replicates": [],
        "profile_drift_replicates": [],
        "producer_failure_replicates": [],
        "output_identity_classes": [],
        "class_solver_invoked": False,
        "scientific_response_read": False,
        "covariance_read": False,
        "scientific_classifier_invoked": False,
        "response_dependent_decision": False,
        "science_evaluated": False,
        "errors": [],
    }
    try:
        validate_static_dependencies()
        docs = [json.loads(Path(p).read_text(encoding="utf-8")) for p in inputs]
        expected = set(REPLICATES)
        reps = [d.get("replicate") for d in docs]
        if len(docs) != 32 or set(reps) != expected or len(set(reps)) != 32:
            fail("PROVENANCE_FAIL", "receipt_set", f"expected exact R01-R32 receipts, got {sorted(x for x in set(reps) if x)}")
        required = required_receipt_fields()
        run_id = int(os.environ.get("GITHUB_RUN_ID", "0") or 0)
        run_attempt = int(os.environ.get("GITHUB_RUN_ATTEMPT", "0") or 0)
        head_sha = os.environ.get("GITHUB_SHA", "")
        for d in docs:
            missing = required - set(d)
            if missing:
                fail("PROVENANCE_FAIL", "receipt_schema", f"{d.get('replicate')} missing fields {sorted(missing)}")
            if d.get("run_id") != run_id or d.get("run_attempt") != run_attempt or d.get("head_sha") != head_sha:
                fail("PROVENANCE_FAIL", "receipt_run_binding", f"{d.get('replicate')} run/head binding mismatch")
            if any(bool(d.get(k)) for k in [
                "class_solver_invoked", "scientific_response_read", "covariance_read",
                "scientific_classifier_invoked", "response_dependent_decision",
            ]):
                fail("INVALID_IMPLEMENTATION", "response_blindness", f"{d.get('replicate')} violated response-blind boundary")
            if d.get("raw_cpu_capability_bits_validation_target") is not False:
                fail("INVALID_IMPLEMENTATION", "native_classification", f"{d.get('replicate')} used raw CPU bits as validation target")
            if d.get("eligible") and not d.get("candidate"):
                fail("INVALID_IMPLEMENTATION", "eligibility", f"{d.get('replicate')} eligible without candidate profile")
            if d.get("eligible") and d.get("native_class") not in NATIVE_CLASSES:
                fail("INVALID_IMPLEMENTATION", "native_classification", f"{d.get('replicate')} eligible native class invalid")
            if d.get("eligible") and not d.get("producer_attempted"):
                fail("PRODUCER_POPULATION_CENSORING_PERSISTS", "producer_attempt", f"{d.get('replicate')} eligible lane did not attempt producer")

        decision["candidate_receipt_count"] = len(docs)
        eligible = [d for d in docs if d["eligible"]]
        decision["eligible_lane_count"] = len(eligible)
        decision["eligible_replicates"] = sorted(d["replicate"] for d in eligible)
        counts = {c: sum(d.get("native_class") == c for d in eligible) for c in NATIVE_CLASSES}
        decision["native_class_counts"] = counts
        decision["profile_drift_replicates"] = sorted(d["replicate"] for d in docs if not d["candidate"])

        if not eligible and decision["profile_drift_replicates"]:
            decision["classification"] = "BLOCKED_NATIVE_FINGERPRINT_PROFILE_DRIFT"
        elif len(eligible) < MIN_ELIGIBLE or any(counts[c] < MIN_PER_CLASS for c in NATIVE_CLASSES):
            decision["classification"] = "BLOCKED_INSUFFICIENT_NATIVE_CLASS_POWER"
        else:
            producer_failed = [d for d in eligible if not d["producer_succeeded"]]
            decision["producer_failure_replicates"] = sorted(d["replicate"] for d in producer_failed)
            content_failed = [d for d in producer_failed if d.get("failure_classification") == "PRODUCER_CONTENT_IDENTITY_FAIL"]
            provenance_failed = [d for d in producer_failed if d.get("failure_classification") == "PROVENANCE_FAIL"]
            implementation_failed = [d for d in producer_failed if d.get("failure_classification") == "INVALID_IMPLEMENTATION"]
            if provenance_failed:
                decision["classification"] = "PROVENANCE_FAIL"
            elif implementation_failed:
                decision["classification"] = "INVALID_IMPLEMENTATION"
            elif content_failed:
                decision["classification"] = "PRODUCER_CONTENT_IDENTITY_FAIL"
            elif producer_failed:
                decision["classification"] = "PRODUCER_POPULATION_CENSORING_PERSISTS"
            else:
                bad_identity = [
                    d for d in eligible
                    if d.get("output_byte_length") != PAYLOAD_LEN
                    or d.get("output_sha256") != PAYLOAD_SHA256
                    or d.get("reload_sha256") != PAYLOAD_SHA256
                ]
                if bad_identity:
                    decision["classification"] = "PRODUCER_CONTENT_IDENTITY_FAIL"
                    decision["producer_failure_replicates"] = sorted(d["replicate"] for d in bad_identity)
                else:
                    classes = sorted(set(d["output_sha256"] for d in eligible))
                    decision["output_identity_classes"] = classes
                    if classes != [PAYLOAD_SHA256]:
                        decision["classification"] = "PRODUCER_CONTENT_IDENTITY_FAIL"
                    else:
                        decision["classification"] = "PASS_SCOPED_CORRECTED_PRODUCER_CROSS_HOST_POPULATION_VALID"
                        decision["producer_success_replicates"] = sorted(d["replicate"] for d in eligible)

        decision["powered"] = bool(
            len(eligible) >= MIN_ELIGIBLE and all(counts[c] >= MIN_PER_CLASS for c in NATIVE_CLASSES)
        )
        decision["expected_payload_byte_length"] = PAYLOAD_LEN
        decision["expected_payload_sha256"] = PAYLOAD_SHA256
        decision["historical_native_class_ratio_is_pass_requirement"] = False
        decision["all_32_receipts_present"] = True
        decision["raw_cpu_capability_bits_validation_target"] = False
        decision["next_stage"] = (
            "DESIGN_NUMERICAL_REPRODUCIBILITY_PREREQUISITE"
            if decision["classification"] == "PASS_SCOPED_CORRECTED_PRODUCER_CROSS_HOST_POPULATION_VALID"
            else "NO_DOWNSTREAM_PROMOTION_TERMINALIZE_POPULATION_GATE"
        )
    except GateError as exc:
        decision["classification"] = exc.classification
        decision["errors"].append({"stage": exc.stage, "message": str(exc)})
    except Exception as exc:
        decision["classification"] = "INVALID_IMPLEMENTATION"
        decision["errors"].append({"stage": "unexpected", "message": f"{type(exc).__name__}: {exc}"})

    write_json(out, decision)
    print(decision["classification"], decision.get("eligible_lane_count"), decision.get("native_class_counts"))
    return 0 if decision["classification"] == "PASS_SCOPED_CORRECTED_PRODUCER_CROSS_HOST_POPULATION_VALID" else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["lane", "decision"], required=True)
    parser.add_argument("--replicate")
    parser.add_argument("--inputs", nargs="*")
    parser.add_argument("--out", required=True)
    parser.add_argument("--materialized")
    args = parser.parse_args()
    if args.mode == "lane":
        if not args.replicate or not args.materialized:
            raise SystemExit("lane mode requires --replicate and --materialized")
        return lane_mode(args.replicate, Path(args.out), Path(args.materialized))
    return decision_mode(list(args.inputs or []), Path(args.out))


if __name__ == "__main__":
    raise SystemExit(main())
