#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

ALLOWED={"PASS","FAIL","OUTSIDE_DOMAIN","NOT_YET_TESTABLE","NUMERICALLY_UNRESOLVED"}
MANDATORY=[
 "G_DOMAIN_MAPPING","G_ANGULAR_AUTHORITY","G_ORDERED_JOIN","G_RADIAL_SUPPORT",
 "G_PHYSICAL_SUPPORT","G_COV_WHITENING","G_NUISANCE_QUOTIENT","G_RELATION_NULL","G_FINAL_MODEL"
]
REQUIRED_CLASSES={"LCDM_GR","WCDM","W0WA","QUINTESSENCE_CANONICAL","INTERACTING_DARK_SECTOR","F_R","DGP_LIKE","HORNDESKI_EFT_LIKE"}

def aggregate(gates):
    statuses=[gates[g]["status"] for g in MANDATORY]
    if any(s=="FAIL" for s in statuses): return "FAIL"
    if all(s=="PASS" for s in statuses):
        if not all(gates[g].get("authority") for g in MANDATORY):
            raise AssertionError("PASS requires bound authority for every mandatory gate")
        return "PASS"
    if any(s=="OUTSIDE_DOMAIN" for s in statuses): return "OUTSIDE_DOMAIN"
    if any(s=="NUMERICALLY_UNRESOLVED" for s in statuses): return "NUMERICALLY_UNRESOLVED"
    return "NOT_YET_TESTABLE"

def validate(d):
    assert d["schema_version"]=="dsir4-model-funnel-v0.1"
    assert d["scientific_authority_created"] is False
    assert set(d["allowed_statuses"])==ALLOWED
    assert d["mandatory_gates"]==MANDATORY
    dom=d["frozen_domain"]
    assert dom=={"z_min":0.295,"z_max":2.33,"k_min_exclusive_mpc_inv":0.0,"k_max_mpc_inv":0.06664762008318016}
    agg=d["aggregation"]
    for k in ("pass_requires_all_mandatory_pass","any_mandatory_fail_implies_overall_fail","outside_domain_is_not_extrapolated","not_yet_testable_is_never_pass_or_fail","numerically_unresolved_requires_frozen_ambiguity_rule","missing_authority_forbids_overall_pass"):
        assert agg[k] is True,k
    inv=d["inventory"]
    ids=[x["model_class_id"] for x in inv]
    assert len(ids)==len(set(ids))
    assert REQUIRED_CLASSES.issubset(ids)
    for x in inv:
        assert x["mapping_status"] in ALLOWED and x["overall_status"] in ALLOWED
        assert isinstance(x["hypotheses"],list)
        # Pre-DSIR-3 closure: no class-level scientific conclusion is allowed.
        assert x["mapping_status"]=="NOT_YET_TESTABLE"
        assert x["overall_status"]=="NOT_YET_TESTABLE"
        assert x["hypotheses"]==[]
    t=d["hypothesis_record_template"]
    assert t["hypothesis_id"] is None and t["overall_status"]=="NOT_YET_TESTABLE"
    gates=t["gate_results"]
    assert list(gates)==MANDATORY
    for g in MANDATORY:
        assert gates[g]=={"status":"NOT_YET_TESTABLE","authority":None}
    assert aggregate(gates)=="NOT_YET_TESTABLE"
    return True

def negative_tests(d):
    # Premature full PASS with missing authorities must fail closed.
    g={k:{"status":"PASS","authority":None} for k in MANDATORY}
    try: aggregate(g)
    except AssertionError: pass
    else: raise AssertionError("negative test failed: PASS without authorities accepted")
    # One mandatory failure dominates otherwise unavailable gates.
    g={k:{"status":"NOT_YET_TESTABLE","authority":None} for k in MANDATORY}; g["G_RELATION_NULL"]={"status":"FAIL","authority":"authority:test"}
    assert aggregate(g)=="FAIL"
    # Complete authoritative PASS is the only PASS route.
    g={k:{"status":"PASS","authority":"authority:test:"+k} for k in MANDATORY}
    assert aggregate(g)=="PASS"
    # OUTSIDE_DOMAIN remains distinct from FAIL.
    g={k:{"status":"NOT_YET_TESTABLE","authority":None} for k in MANDATORY}; g["G_DOMAIN_MAPPING"]={"status":"OUTSIDE_DOMAIN","authority":"mapping:test"}
    assert aggregate(g)=="OUTSIDE_DOMAIN"
    # Numerical unresolved is not coerced to PASS/FAIL.
    g={k:{"status":"NOT_YET_TESTABLE","authority":None} for k in MANDATORY}; g["G_ANGULAR_AUTHORITY"]={"status":"NUMERICALLY_UNRESOLVED","authority":"ambiguity:test"}
    assert aggregate(g)=="NUMERICALLY_UNRESOLVED"

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("path"); a=ap.parse_args()
    d=json.loads(Path(a.path).read_text())
    validate(d); negative_tests(d)
    print("PASS_DSIR4_MODEL_FUNNEL_MATRIX_VALIDATOR_V0_1")
    print("classification=SUPPORT_PLUS_0_PLUS_0")
    print("scientific_model_authority_created=false")
