#!/usr/bin/env python3
from __future__ import annotations
import json,sys
from pathlib import Path

COMP=["background_density_like","background_pressure_like","scalar_density_perturbation","scalar_momentum_velocity","scalar_isotropic_pressure_perturbation","scalar_anisotropic_stress"]
DOM={"z_min":0.295,"z_max":2.33,"k_min_exclusive_mpc_inv":0.0,"k_max_mpc_inv":0.06664762008318016}

def check(path,hid):
 d=json.loads(Path(path).read_text())
 assert d['schema_version']=='dsir4-model-mapping-v0.1'
 assert d['scientific_authority_created'] is False
 assert d['hypothesis_identity']['hypothesis_id']==hid
 assert d['common_residual']['definition']=='X_munu = M0^2 G_munu - T_known_munu'
 assert d['common_residual']['total_residual_is_authoritative'] is True
 assert list(d['common_residual']['components'])==COMP
 for k,v in d['common_residual']['components'].items():
  assert v['mapping_state'] in {'DERIVED','STRUCTURAL_ZERO'}
  assert v['expression_ref']
 dom=d['certified_domain']
 for k,v in DOM.items(): assert dom[k]==v,(hid,k,dom[k],v)
 assert dom['linear_regime'] is True
 assert d['readiness']=={'mapping_ready':True,'prediction_ready':False,'numerically_evaluated':False,'scientific_gate_status':'NOT_YET_TESTABLE'}
 assert d['sector_bookkeeping']['total_residual_invariant_under_relabeling_required'] is True
 assert d['modified_gravity_bookkeeping']['effective_source_rearrangement_used'] is False
 return d

if __name__=='__main__':
 if len(sys.argv)!=3: raise SystemExit('usage: validator C0.json C1.json')
 c0=check(sys.argv[1],'C0_LCDM_REFERENCE'); c1=check(sys.argv[2],'C1_SMOOTH_W_LOCAL_EPS1E4')
 assert c0['hypothesis_identity']['model_class_id']=='LCDM_GR'
 assert c1['hypothesis_identity']['model_class_id']=='WCDM'
 assert c1['hypothesis_identity']['parameter_values']=={'epsilon_w':0.0001,'w':-0.9999,'smooth_de_control':True}
 c0c=c0['common_residual']['components']; c1c=c1['common_residual']['components']
 assert c0c['scalar_isotropic_pressure_perturbation']['mapping_state']=='STRUCTURAL_ZERO'
 assert c0c['scalar_anisotropic_stress']['mapping_state']=='STRUCTURAL_ZERO'
 assert c1c['scalar_isotropic_pressure_perturbation']['mapping_state']=='STRUCTURAL_ZERO'
 assert c1c['scalar_anisotropic_stress']['mapping_state']=='STRUCTURAL_ZERO'
 assert c0['conventions']['T_known_definition']==c1['conventions']['T_known_definition']
 assert c0['conventions']['M0_definition']==c1['conventions']['M0_definition']
 print('PASS_DSIR4_C0_C1_MAPPING_STATIC_VALIDATOR_V0_1')
 print('classification=SUPPORT_PLUS_0_PLUS_0')
 print('mapping_ready_count=2')
 print('scientific_gate_authority_created=false')
