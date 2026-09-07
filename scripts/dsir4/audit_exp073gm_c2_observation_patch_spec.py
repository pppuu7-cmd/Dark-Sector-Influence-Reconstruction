#!/usr/bin/env python3
from pathlib import Path
import re, sys
EXPECTED='ac627d54e9ce196a08878d1ba33999819925d19c'
TOKEN='PASS_EXP073GM_C2_IDE_OBSERVATION_ONLY_EXTRACTION_PATCH_SPEC_STATIC_AUDIT_V0_1'
if len(sys.argv)!=4: raise SystemExit('usage: audit <class_iv> <reported_commit> <prereg>')
root=Path(sys.argv[1]); reported=sys.argv[2].strip(); prereg=Path(sys.argv[3]).read_text()
if reported!=EXPECTED: raise SystemExit('FAIL source commit identity')
text=(root/'source'/'perturbations.c').read_text()
def req(p,l,h=text,flags=re.S):
    m=re.search(p,h,flags)
    if not m: raise SystemExit('FAIL missing '+l)
    return m
req(r'delta_rho_m\s*\+=\s*ppw->pvecback\s*\[\s*pba->index_bg_rho_idm_iv\s*\]\s*\*\s*y\s*\[\s*ppw->pv->index_pt_delta_idm_iv\s*\]', 'IDE density arithmetic')
req(r'rho_plus_p_theta_m\s*\+=\s*ppw->pvecback\s*\[\s*pba->index_bg_rho_idm_iv\s*\]\s*\*\s*y\s*\[\s*ppw->pv->index_pt_theta_idm_iv\s*\]', 'IDE momentum arithmetic')
helper=req(r'int\s+perturb_total_stress_energy\s*\([^)]*\)\s*\{(?P<b>.*?)(?=\nint\s+[A-Za-z_])','helper').group('b')
req(r'ppw->delta_m\s*=\s*delta_rho_m\s*/\s*rho_m\s*;', 'current delta_m',helper)
req(r'ppw->theta_m\s*=\s*rho_plus_p_theta_m\s*/\s*rho_plus_p_m\s*;', 'current theta_m',helper)
ein=req(r'int\s+perturb_einstein\s*\([^)]*\)\s*\{(?P<b>.*?)(?=\nint\s+perturb_total_stress_energy)','einstein').group('b')
a=req(r'perturb_total_stress_energy\s*\(', 'helper call',ein).start()
b=req(r'ppw->delta_m\s*\+=', 'native delta correction',ein).start()
if not a<b: raise SystemExit('FAIL tap ordering')
for s in ['index_bg_a','index_bg_H','k2']:
    if s not in ein: raise SystemExit('FAIL missing caller identity '+s)
for phrase in ['observation-only','must not mutate','must never apply a second correction','SUPPORT_PLUS_0_PLUS_0']:
    if phrase not in prereg: raise SystemExit('FAIL prereg marker '+phrase)
print('classification=SUPPORT_PLUS_0_PLUS_0')
print('prediction_ready=false')
print('scientific_model_authority_created=false')
print('G_DOMAIN_MAPPING=NOT_YET_TESTABLE')
print(TOKEN)
