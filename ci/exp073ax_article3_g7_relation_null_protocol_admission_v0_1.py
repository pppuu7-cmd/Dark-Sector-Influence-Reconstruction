#!/usr/bin/env python3
import copy
import hashlib
import json
import re

TOKEN = "PASS_EXP073AX_G7_RELATION_NULL_PROTOCOL_ADMISSION_SYNTHETIC_V0_1"
CLASSIFICATION = "HOSTED_SYNTHETIC_PASS_NON_SCIENTIFIC_PLUS_0_READINESS"
SCHEMA = "exp073ax_article3_g7_relation_null_protocol_admission_v0_1"
ROUTE = "controlled_single_thread_exact_v1"
CHAIN = ["exp073ar", "exp073as", "exp073at", "exp073au", "exp073av", "exp073aw"]
HEX64 = re.compile(r"^[0-9a-f]{64}$")

PROTECTED_KEYS = {
    "schema", "authority_route", "upstream_chain", "real_quotient_authority_required",
    "discovery_manifest_sha256", "discovery_manifest_frozen_before_fit", "discovery_contains_withheld_family",
    "relation_form_id", "relation_form_sha256", "relation_form_frozen_before_fit",
    "statistic_id", "statistic_sha256", "statistic_frozen_before_fit",
    "decision_rule_id", "decision_rule_sha256", "decision_rule_frozen_before_fit",
    "null_control_id", "null_control_sha256", "null_control_frozen_before_fit",
    "fit_rule_id", "fit_rule_sha256", "fit_rule_frozen_before_fit",
    "quotient_authority_requirement_sha256", "quotient_authority_requirement_frozen_before_fit",
    "fit_executed", "target_quotient_read", "withheld_family_selected", "withheld_reads", "G8_reads",
    "relation_freeze_before_g8_required", "target_dependent_nuisance_rank_allowed",
    "unresolved_nuisance_rank_rescue_allowed", "covariance_repairs_allowed",
    "effective_coordinate_shortcut_allowed", "fiducial_P_weighting_allowed",
    "protocol_selected_using_G8_performance", "causal_claim_authorized", "fundamental_law_claim_authorized",
    "article3_scientific_readiness_percent", "readiness_increment", "gate_state"
}

ID_SHA_PAIRS = [
    ("relation_form_id", "relation_form_sha256"),
    ("statistic_id", "statistic_sha256"),
    ("decision_rule_id", "decision_rule_sha256"),
    ("null_control_id", "null_control_sha256"),
    ("fit_rule_id", "fit_rule_sha256"),
]
FROZEN_FLAGS = [
    "discovery_manifest_frozen_before_fit",
    "relation_form_frozen_before_fit",
    "statistic_frozen_before_fit",
    "decision_rule_frozen_before_fit",
    "null_control_frozen_before_fit",
    "fit_rule_frozen_before_fit",
    "quotient_authority_requirement_frozen_before_fit",
]
SHA_FIELDS = [
    "discovery_manifest_sha256", "relation_form_sha256", "statistic_sha256",
    "decision_rule_sha256", "null_control_sha256", "fit_rule_sha256",
    "quotient_authority_requirement_sha256",
]


def h(label):
    return hashlib.sha256(label.encode("utf-8")).hexdigest()


def baseline():
    return {
        "schema": SCHEMA,
        "authority_route": ROUTE,
        "upstream_chain": list(CHAIN),
        "real_quotient_authority_required": True,
        "discovery_manifest_sha256": h("discovery-manifest"),
        "discovery_manifest_frozen_before_fit": True,
        "discovery_contains_withheld_family": False,
        "relation_form_id": "future_concrete_relation_form_v0_1",
        "relation_form_sha256": h("relation-form"),
        "relation_form_frozen_before_fit": True,
        "statistic_id": "future_scalar_statistic_v0_1",
        "statistic_sha256": h("statistic"),
        "statistic_frozen_before_fit": True,
        "decision_rule_id": "future_decision_rule_v0_1",
        "decision_rule_sha256": h("decision-rule"),
        "decision_rule_frozen_before_fit": True,
        "null_control_id": "future_null_control_v0_1",
        "null_control_sha256": h("null-control"),
        "null_control_frozen_before_fit": True,
        "fit_rule_id": "future_fit_rule_v0_1",
        "fit_rule_sha256": h("fit-rule"),
        "fit_rule_frozen_before_fit": True,
        "quotient_authority_requirement_sha256": h("successor-real-quotient-requirement"),
        "quotient_authority_requirement_frozen_before_fit": True,
        "fit_executed": False,
        "target_quotient_read": False,
        "withheld_family_selected": False,
        "withheld_reads": [],
        "G8_reads": [],
        "relation_freeze_before_g8_required": True,
        "target_dependent_nuisance_rank_allowed": False,
        "unresolved_nuisance_rank_rescue_allowed": False,
        "covariance_repairs_allowed": [],
        "effective_coordinate_shortcut_allowed": False,
        "fiducial_P_weighting_allowed": False,
        "protocol_selected_using_G8_performance": False,
        "causal_claim_authorized": False,
        "fundamental_law_claim_authorized": False,
        "article3_scientific_readiness_percent": 52,
        "readiness_increment": 0,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }


def validate(x):
    if set(x) != PROTECTED_KEYS:
        return False, "PROTECTED_SCHEMA_KEY_DRIFT"
    if x["schema"] != SCHEMA:
        return False, "WRONG_SCHEMA"
    if x["authority_route"] != ROUTE:
        return False, "WRONG_AUTHORITY_ROUTE"
    if x["upstream_chain"] != CHAIN:
        return False, "WRONG_OR_REORDERED_SUCCESSOR_CHAIN"
    if x["real_quotient_authority_required"] is not True:
        return False, "REAL_QUOTIENT_AUTHORITY_NOT_REQUIRED"
    for flag in FROZEN_FLAGS:
        if x[flag] is not True:
            return False, f"NOT_FROZEN_BEFORE_FIT:{flag}"
    for ident, sha in ID_SHA_PAIRS:
        if not isinstance(x[ident], str) or not x[ident].strip():
            return False, f"MISSING_ID:{ident}"
        if not isinstance(x[sha], str) or not HEX64.fullmatch(x[sha]):
            return False, f"MALFORMED_SHA256:{sha}"
    for sha in SHA_FIELDS:
        if not isinstance(x[sha], str) or not HEX64.fullmatch(x[sha]):
            return False, f"MALFORMED_SHA256:{sha}"
    if x["discovery_contains_withheld_family"] is not False:
        return False, "WITHHELD_IN_DISCOVERY_MANIFEST"
    if x["withheld_family_selected"] is not False:
        return False, "WITHHELD_FAMILY_PRESELECTED"
    if x["withheld_reads"] != []:
        return False, "WITHHELD_READ_BEFORE_G7_FREEZE"
    if x["G8_reads"] != []:
        return False, "G8_READ_BEFORE_G7_FREEZE"
    if x["fit_executed"] is not False:
        return False, "FIT_ALREADY_EXECUTED_AT_PROTOCOL_REGISTRATION"
    if x["target_quotient_read"] is not False:
        return False, "TARGET_QUOTIENT_READ_AT_PROTOCOL_REGISTRATION"
    if x["relation_freeze_before_g8_required"] is not True:
        return False, "RELATION_FREEZE_BEFORE_G8_NOT_REQUIRED"
    if x["target_dependent_nuisance_rank_allowed"] is not False:
        return False, "TARGET_DEPENDENT_NUISANCE_RANK_ALLOWED"
    if x["unresolved_nuisance_rank_rescue_allowed"] is not False:
        return False, "UNRESOLVED_NUISANCE_RANK_RESCUE_ALLOWED"
    if x["covariance_repairs_allowed"] != []:
        return False, "COVARIANCE_REPAIR_ALLOWED"
    if x["effective_coordinate_shortcut_allowed"] is not False:
        return False, "EFFECTIVE_COORDINATE_SHORTCUT_ALLOWED"
    if x["fiducial_P_weighting_allowed"] is not False:
        return False, "FIDUCIAL_P_WEIGHTING_ALLOWED"
    if x["protocol_selected_using_G8_performance"] is not False:
        return False, "PROTOCOL_SELECTED_USING_G8"
    if x["causal_claim_authorized"] is not False:
        return False, "CAUSAL_CLAIM_PREMATURELY_AUTHORIZED"
    if x["fundamental_law_claim_authorized"] is not False:
        return False, "FUNDAMENTAL_LAW_PREMATURELY_AUTHORIZED"
    if x["article3_scientific_readiness_percent"] != 52 or x["readiness_increment"] != 0:
        return False, "SCIENTIFIC_READINESS_ACCOUNTING_DRIFT"
    if x["gate_state"] != {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"}:
        return False, "GATE_PREMATURELY_CLOSED"
    return True, "PASS"


def mutated(**changes):
    x = baseline()
    for key, value in changes.items():
        x[key] = value
    return x


def expect(name, obj, should_pass):
    ok, reason = validate(obj)
    if ok != should_pass:
        raise AssertionError(f"{name}: expected pass={should_pass}, got {ok}, reason={reason}")
    return {"name": name, "pass_expected": should_pass, "validator_ok": ok, "reason": reason}


def main():
    cases = []
    cases.append(expect("baseline", baseline(), True))
    cases.append(expect("wrong_authority_route", mutated(authority_route="canonical_exp073x2"), False))
    cases.append(expect("reordered_chain", mutated(upstream_chain=["exp073as", "exp073ar", "exp073at", "exp073au", "exp073av", "exp073aw"]), False))
    cases.append(expect("real_quotient_not_required", mutated(real_quotient_authority_required=False), False))
    cases.append(expect("discovery_not_frozen", mutated(discovery_manifest_frozen_before_fit=False), False))
    cases.append(expect("relation_not_frozen", mutated(relation_form_frozen_before_fit=False), False))
    cases.append(expect("statistic_not_frozen", mutated(statistic_frozen_before_fit=False), False))
    cases.append(expect("decision_not_frozen", mutated(decision_rule_frozen_before_fit=False), False))
    cases.append(expect("null_not_frozen", mutated(null_control_frozen_before_fit=False), False))
    cases.append(expect("fit_rule_not_frozen", mutated(fit_rule_frozen_before_fit=False), False))
    cases.append(expect("malformed_sha", mutated(relation_form_sha256="abc"), False))
    cases.append(expect("withheld_in_discovery", mutated(discovery_contains_withheld_family=True), False))
    cases.append(expect("withheld_preselected", mutated(withheld_family_selected=True), False))
    cases.append(expect("withheld_read", mutated(withheld_reads=["family_x"]), False))
    cases.append(expect("g8_read", mutated(G8_reads=["withheld_result"]), False))
    cases.append(expect("fit_already_executed", mutated(fit_executed=True), False))
    cases.append(expect("target_quotient_read", mutated(target_quotient_read=True), False))
    cases.append(expect("relation_freeze_not_required", mutated(relation_freeze_before_g8_required=False), False))
    cases.append(expect("target_dependent_rank", mutated(target_dependent_nuisance_rank_allowed=True), False))
    cases.append(expect("rank_rescue", mutated(unresolved_nuisance_rank_rescue_allowed=True), False))
    cases.append(expect("covariance_repair", mutated(covariance_repairs_allowed=["jitter"]), False))
    cases.append(expect("causal_claim", mutated(causal_claim_authorized=True), False))
    cases.append(expect("fundamental_claim", mutated(fundamental_law_claim_authorized=True), False))
    cases.append(expect("readiness_increment", mutated(readiness_increment=1), False))
    cases.append(expect("gate_closed", mutated(gate_state={"G7": "PASS", "G8": "OPEN", "G9": "OPEN"}), False))
    cases.append(expect("selected_using_g8", mutated(protocol_selected_using_G8_performance=True), False))
    cases.append(expect("effective_coordinate_shortcut", mutated(effective_coordinate_shortcut_allowed=True), False))
    cases.append(expect("fiducial_p_shortcut", mutated(fiducial_P_weighting_allowed=True), False))
    x = baseline(); x["unknown_firewall_override"] = True
    cases.append(expect("unknown_protected_key", x, False))

    if len(cases) != 29:
        raise AssertionError(f"unexpected test count {len(cases)}")

    out = {
        "token": TOKEN,
        "classification": CLASSIFICATION,
        "schema": SCHEMA,
        "tests_passed": len(cases),
        "tests": cases,
        "article3_scientific_readiness_percent": 52,
        "readiness_increment": 0,
        "scientific_pass_claimed": False,
        "real_quotient_read": False,
        "G7_fit_executed": False,
        "G8_read": False,
        "withheld_family_selected": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "next_real_requirement": "prospectively frozen concrete G7 relation/statistic/decision/null/fit protocol after real successor quotient authority exists",
    }
    print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
