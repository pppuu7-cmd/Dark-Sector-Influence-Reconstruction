#!/usr/bin/env python3
import json,sys
p=sys.argv[1]
d=json.load(open(p))
assert d['schema_version']=='dsir4-model-mapping-v0.1'
assert d['scientific_authority_created'] is False
assert d['hypothesis_identity']['model_class_id']=='LCDM_GR'
assert d['hypothesis_identity']['hypothesis_id']=='LCDM_GR_SYMBOLIC_BASELINE_V0_1'
assert d['common_residual']['definition']=='X_munu = M0^2 G_munu - T_known_munu'
assert d['common_residual']['total_residual_is_authoritative'] is True
c=d['common_residual']['components']; assert len(c)==6
for k,v in c.items():
    assert v['mapping_state'] in {'DERIVED_NONZERO','STRUCTURAL_ZERO'}
    assert v['expression_ref']
assert c['scalar_isotropic_pressure_perturbation']['mapping_state']=='STRUCTURAL_ZERO'
assert c['scalar_anisotropic_stress']['mapping_state']=='STRUCTURAL_ZERO'
s=d['sector_bookkeeping']; assert s['has_interacting_sector_partition'] is False; assert s['transfer_current_convention']=='Q_c^mu=Q_Lambda^mu=0'
m=d['modified_gravity_bookkeeping']; assert m['effective_source_rearrangement_used'] is False; assert m['original_field_equation_ref']; assert m['algebraic_equivalence_proof_ref']
dom=d['certified_domain']; assert dom['z_min']==0.295 and dom['z_max']==2.33 and dom['k_min_exclusive_mpc_inv']==0.0 and dom['k_max_mpc_inv']==0.06664762008318016
assert dom['linear_regime'] is True and dom['quasi_static_assumption'] is False and dom['sub_horizon_assumption'] is False
r=d['readiness']; assert r=={'mapping_ready':True,'prediction_ready':False,'numerically_evaluated':False,'scientific_gate_status':'NOT_YET_TESTABLE'}
print('PASS_DSIR4_LCDM_GR_MAPPING_VALIDATOR_V0_1')
print('classification=SUPPORT_PLUS_0_PLUS_0')
print('scientific_model_authority_created=false')
