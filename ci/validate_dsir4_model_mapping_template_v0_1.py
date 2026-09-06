#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,copy
from pathlib import Path

COMPONENTS=[
 "background_density_like","background_pressure_like","scalar_density_perturbation",
 "scalar_momentum_velocity","scalar_isotropic_pressure_perturbation","scalar_anisotropic_stress"
]
MAP_STATES={"NOT_YET_MAPPED","STRUCTURAL_ZERO","NONZERO","DERIVED","OUTSIDE_DOMAIN"}
SCI_STATES={"PASS","FAIL","OUTSIDE_DOMAIN","NOT_YET_TESTABLE","NUMERICALLY_UNRESOLVED"}

def validate_record(d,template_mode=False):
    assert d["schema_version"]=="dsir4-model-mapping-v0.1"
    assert d["scientific_authority_created"] is False
    assert d["common_residual"]["definition"]=="X_munu = M0^2 G_munu - T_known_munu"
    assert d["common_residual"]["total_residual_is_authoritative"] is True
    comps=d["common_residual"]["components"]
    assert list(comps)==COMPONENTS
    for name,c in comps.items():
        assert c["mapping_state"] in MAP_STATES,name
        if c["mapping_state"] in {"NONZERO","DERIVED","STRUCTURAL_ZERO"}:
            assert c["expression_ref"],f"mapped component lacks expression provenance: {name}"
        if c["mapping_state"] in {"NOT_YET_MAPPED","OUTSIDE_DOMAIN"}:
            assert c["expression_ref"] is None
    assert d["sector_bookkeeping"]["total_residual_invariant_under_relabeling_required"] is True
    r=d["readiness"]; assert r["scientific_gate_status"] in SCI_STATES
    if r["mapping_ready"]:
        assert d["hypothesis_identity"]["model_class_id"] and d["hypothesis_identity"]["hypothesis_id"]
        assert all(comps[k]["mapping_state"]!="NOT_YET_MAPPED" for k in COMPONENTS)
    if r["prediction_ready"]:
        assert r["mapping_ready"] is True
        p=d["prediction_artifact"]
        assert p["mapping_artifact_sha256"] and p["payload_sha256"] and p["code_commit_or_expression_id"]
    if r["numerically_evaluated"]:
        assert r["prediction_ready"] is True
    if r["scientific_gate_status"]=="PASS":
        assert r["mapping_ready"] and r["prediction_ready"] and r["numerically_evaluated"]
        raise AssertionError("mapping-artifact validator may not itself authorize scientific PASS")
    if template_mode:
        assert d["hypothesis_identity"]["model_class_id"] is None
        assert d["hypothesis_identity"]["hypothesis_id"] is None
        assert all(comps[k]=={"mapping_state":"NOT_YET_MAPPED","expression_ref":None} for k in COMPONENTS)
        assert r=={"mapping_ready":False,"prediction_ready":False,"numerically_evaluated":False,"scientific_gate_status":"NOT_YET_TESTABLE"}
    return True

def negative_tests(d):
    x=copy.deepcopy(d); x["readiness"]["mapping_ready"]=True
    try: validate_record(x)
    except AssertionError: pass
    else: raise AssertionError("mapping_ready without hypothesis/components accepted")
    x=copy.deepcopy(d); x["common_residual"]["components"]["scalar_anisotropic_stress"]={"mapping_state":"NONZERO","expression_ref":None}
    try: validate_record(x)
    except AssertionError: pass
    else: raise AssertionError("NONZERO component without provenance accepted")
    x=copy.deepcopy(d); x["readiness"]={"mapping_ready":True,"prediction_ready":True,"numerically_evaluated":True,"scientific_gate_status":"PASS"}
    x["hypothesis_identity"]["model_class_id"]="TEST"; x["hypothesis_identity"]["hypothesis_id"]="TEST:P0"
    for c in x["common_residual"]["components"].values(): c.update(mapping_state="STRUCTURAL_ZERO",expression_ref="expr:test")
    x["prediction_artifact"].update(mapping_artifact_sha256="0"*64,payload_sha256="1"*64,code_commit_or_expression_id="test")
    try: validate_record(x)
    except AssertionError: pass
    else: raise AssertionError("mapping audit incorrectly authorized scientific PASS")

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("path"); a=ap.parse_args(); d=json.loads(Path(a.path).read_text())
    validate_record(d,template_mode=True); negative_tests(d)
    print("PASS_DSIR4_MODEL_MAPPING_TEMPLATE_VALIDATOR_V0_1")
    print("classification=SUPPORT_PLUS_0_PLUS_0")
    print("scientific_model_authority_created=false")
