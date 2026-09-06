#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path

MANDATORY=["G_DOMAIN_MAPPING","G_ANGULAR_AUTHORITY","G_ORDERED_JOIN","G_RADIAL_SUPPORT","G_PHYSICAL_SUPPORT","G_COV_WHITENING","G_NUISANCE_QUOTIENT","G_RELATION_NULL","G_FINAL_MODEL"]
EXPECTED={
 "C0_LCDM_REFERENCE","C1_SMOOTH_W_LOCAL_EPS1E4","C2_IDE_LOCAL_TANGENT_CONE","C3_GDM_CS2_CV2_LOCAL_PAIR",
 "C4_WDM_3KEV","C5_FR_B0_1E5","C5_FR_B0_1E4","C6_DCDM_DR_GAMMA_H0_1"
}
ALLOWED={"PASS","FAIL","OUTSIDE_DOMAIN","NOT_YET_TESTABLE","NUMERICALLY_UNRESOLVED"}

def main(path):
 d=json.loads(Path(path).read_text())
 assert d["schema_version"]=="dsir4-existing-model-pilot-v0.1"
 assert d["scientific_model_authority_created"] is False
 assert d["source_authority"]=={"path":"docs/GATES.md","blob":"f0127d3f8ab4e7e9bd3ce88ce823c17d9404a285"}
 assert d["mandatory_gates"]==MANDATORY
 hs=d["hypotheses"]; ids=[h["hypothesis_id"] for h in hs]
 assert set(ids)==EXPECTED and len(ids)==len(EXPECTED)
 for h in hs:
  assert h["overall_status"]=="NOT_YET_TESTABLE",h["hypothesis_id"]
  assert h["legacy_evidence"]["status"] not in ALLOWED, "legacy support must not masquerade as DSIR scientific gate status"
  assert set(h["gate_results"])==set(MANDATORY)
  assert all(h["gate_results"][g]=="NOT_YET_TESTABLE" for g in MANDATORY)
  assert h["mapping_conversion_status"].endswith("REQUIRED")
 # Frozen numerical legacy anchors.
 by={h["hypothesis_id"]:h for h in hs}
 assert "structure_angle_deg=58.9338" in by["C2_IDE_LOCAL_TANGENT_CONE"]["legacy_evidence"]["facts"]
 assert "low_k_matter_angle_deg=0.322616" in by["C3_GDM_CS2_CV2_LOCAL_PAIR"]["legacy_evidence"]["facts"]
 assert "metric_slip_angle_deg=137.9432" in by["C3_GDM_CS2_CV2_LOCAL_PAIR"]["legacy_evidence"]["facts"]
 assert "rT_k0p1=-3.46e-6" in by["C4_WDM_3KEV"]["legacy_evidence"]["facts"]
 assert "rT_k10=-0.10375" in by["C4_WDM_3KEV"]["legacy_evidence"]["facts"]
 assert by["C5_FR_B0_1E5"]["frozen_object"].endswith("B0=1e-5")
 assert by["C5_FR_B0_1E4"]["frozen_object"].endswith("B0=1e-4")
 assert by["C6_DCDM_DR_GAMMA_H0_1"]["frozen_object"].endswith("Gamma/H0=1")
 # Explicitly forbid misleading pilot conclusions.
 raw=Path(path).read_text().lower()
 for bad in ('"overall_status": "pass"','"overall_status": "fail"','fractional_pass','percent_pass','percentage_pass'):
  assert bad not in raw,bad
 print("PASS_DSIR4_EXISTING_MODEL_PILOT_VALIDATOR_V0_1")
 print("classification=SUPPORT_PLUS_0_PLUS_0")
 print("scientific_model_authority_created=false")
 print("pilot_hypotheses=8")

if __name__=='__main__':
 ap=argparse.ArgumentParser(); ap.add_argument('path'); a=ap.parse_args(); main(a.path)
