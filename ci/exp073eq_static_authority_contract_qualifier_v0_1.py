#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,re,subprocess,sys
from pathlib import Path

EN_HEAD='4d1cbd504067a64a94b038292793e5e8bffba911'
EN_WORKFLOW='.github/workflows/exp073en-ww-s0-s0-filebacked-ab-network-retry-v0-2.yml'
EN_WORKFLOW_BLOB='6cdd07a839d620d39f12cf083fce5ac81692cb9d'
EN_PREREG='experiments/073en_ww_s0_s0_filebacked_full_resolution_ab_science_v0_1_prereg.md'
EN_PREREG_BLOB='02f22926705cca05d128b1cea8ca7a3a3c73ef3b'
EO_PREREG='experiments/073eo_ww_s0_s0_filebacked_provenance_authority_admission_v0_1_prereg.md'
EO_PREREG_BLOB='c495e8d51d53d3c83abdd411e3a3ed4602ae1375'
EN_HOME='ci/exp073en_home_filebacked_fullres_v0_1.sh'
PASS='PASS_EXP073EQ_EN_EO_STATIC_AUTHORITY_CONTRACT_V0_1'
FAIL='FAIL_EXP073EQ_EN_EO_STATIC_AUTHORITY_CONTRACT_V0_1'

EXPECTED={
 'FROZEN_SOURCE_HEAD':'de83e20a68f79ccf25b89b0d33eb4206e294c757',
 'CONTRACT_FP':'b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251',
 'R1_ARTIFACT_ID':'9720335366',
 'R1_DIGEST':'sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd',
 'PATCH_SHA256':'9a80a756960afa8b4ddf61b5fbba7fba6ad5ed9ac919e093bb1365a636c789f0',
 'NAMASTER_HEAD':'24365fa59a38c15732f4f37e8b29265b75c442d5',
 'EM_ARTIFACT_ID':'9977333691',
 'EM_ARTIFACT_DIGEST':'sha256:0ece75e489b6f413d96e85a099e42db96b5d5acdc03c3ee6901273357762cda1',
}

def git(*args:str)->str:
 return subprocess.check_output(['git',*args],text=True).strip()
def show(ref:str,path:str)->str:
 return subprocess.check_output(['git','show',f'{ref}:{path}'],text=True)
def env_value(text:str,key:str):
 m=re.search(r'^\s*'+re.escape(key)+r":\s*'([^']+)'\s*$",text,re.M)
 return m.group(1) if m else None

def main():
 checks={}
 checks['en_workflow_blob']=(git('rev-parse',f'{EN_HEAD}:{EN_WORKFLOW}')==EN_WORKFLOW_BLOB)
 checks['en_prereg_blob']=(git('rev-parse',f'{EN_HEAD}:{EN_PREREG}')==EN_PREREG_BLOB)
 checks['eo_prereg_blob']=(git('hash-object',EO_PREREG)==EO_PREREG_BLOB)
 enwf=show(EN_HEAD,EN_WORKFLOW); enpr=show(EN_HEAD,EN_PREREG); eopr=Path(EO_PREREG).read_text(); enhome=show(EN_HEAD,EN_HOME)
 bound={}
 for k,v in EXPECTED.items():
  got=env_value(enwf,k); bound[k]={'workflow':got,'expected':v,'workflow_exact':got==v,'present_in_en_prereg':v in enpr,'present_in_eo_prereg':v in eopr}
 checks['frozen_bindings_exact']=all(x['workflow_exact'] and x['present_in_en_prereg'] and x['present_in_eo_prereg'] for x in bound.values())
 candidate='PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1'
 local='PASS_EXP073EM_NAMASTER27_FILEBACKED_MMAP_EXACT_STORAGE_V0_1'
 checks['candidate_token_bound']=(candidate in enpr and candidate in eopr and candidate in enhome)
 checks['local_storage_token_bound']=(local in enpr and local in eopr and local in enhome)
 nl=12288; ncls=4; nb=39; rows=ncls*nl; mcm_bytes=rows*rows*8; selected_bytes=nb*nl*8; full_bpw_bytes=ncls*nb*ncls*nl*8
 geometry={'nl':nl,'ncls':ncls,'nb':nb,'mcm_rows':rows,'mcm_bytes':mcm_bytes,'selected_shape':[nb,nl],'selected_bytes':selected_bytes,'full_bpw_shape':[ncls,nb,ncls,nl],'full_bpw_bytes':full_bpw_bytes}
 checks['mcm_geometry_exact']=(rows==49152 and mcm_bytes==19327352832 and '19,327,352,832' in enpr and '19,327,352,832' in eopr and 'EXPECTED_MCM_BYTES=19327352832' in enhome and 'EXPECTED_MCM_ROWS=49152' in enhome)
 checks['selected_geometry_exact']=(selected_bytes==3833856 and '<f8 [39,12288]' in enpr and '<f8 [39,12288]' in eopr)
 checks['full_bpw_geometry_exact']=(full_bpw_bytes==61341696 and '[4,39,4,12288]' in enpr and '[4,39,4,12288]' in eopr)
 checks['exact_only_contract']=all(s in enpr for s in ['numpy.array_equal','no tolerance','allclose']) and all(s in eopr for s in ['numpy.array_equal','no `allclose`','tolerance'])
 checks['eo_authority_fail_closed']=('science_gate_scored=true' in eopr and 'ww_s0_s0_authority_created=true' in eopr and 'BLOCKED_EXP073EO_PROVENANCE +0/+0' in eopr and 'Only EO authority PASS advances' in eopr)
 ok=all(checks.values())
 rec={'experiment':'Exp073EQ','classification':'STATIC_AUTHORITY_CONTRACT_EXACT' if ok else 'STATIC_AUTHORITY_CONTRACT_FAIL','token':PASS if ok else FAIL,'accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,'en_head':EN_HEAD,'en_workflow_blob':EN_WORKFLOW_BLOB,'en_prereg_blob':EN_PREREG_BLOB,'eo_prereg_blob':EO_PREREG_BLOB,'checks':checks,'bindings':bound,'geometry':geometry,'no_tolerance_rescue':True}
 out=Path(sys.argv[1] if len(sys.argv)>1 else 'exp073eq_terminal_receipt.json'); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
 print(rec['token']); print(json.dumps(rec,indent=2,sort_keys=True)); raise SystemExit(0 if ok else 3)
if __name__=='__main__': main()
