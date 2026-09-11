#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
PASS="LAYERB_32769_RESOURCE_AUTHORITY_PROMOTION_REVIEW_PASS_PLUS_0_PLUS_0"; FAIL="LAYERB_32769_RESOURCE_AUTHORITY_PROMOTION_REVIEW_FAIL_PLUS_0_PLUS_0"; RESOURCE_PASS="LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS_PLUS_0_PLUS_0"; READY="LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_READY_PLUS_0_PLUS_0"; PROV_PASS="LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_PACKAGING_PASS_PLUS_0_PLUS_0"; CONTRACT="331cf499627a3673ce88c483e7afcfd4f731d105"
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def blob(b):return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def digest(x):return x[7:] if isinstance(x,str) and x.startswith('sha256:') else x if isinstance(x,str) else None
def synth(d):return d.get('synthetic_fixture') is True or d.get('synthetic_only') is True
def pos(x):return isinstance(x,int) and x>0
def main():
 ap=argparse.ArgumentParser()
 for k in ('contract','candidate-run','candidate-artifacts','candidate-artifact-zip','artifact-manifest','candidate-receipt','resource-candidate','provenance','downstream-repair-authority','out'):ap.add_argument('--'+k,required=True)
 a=ap.parse_args();e=[];cb=Path(a.contract).read_bytes();c=json.loads(cb)
 if blob(cb)!=CONTRACT:e.append('contract_blob')
 if c.get('promotion_review_requires_real_non_synthetic_candidate') is not True or c.get('promotion_is_exact_byte_copy_only') is not True or c.get('review_output_creates_no_repository_authority') is not True or c.get('review_output_authorizes_no_science') is not True:e.append('contract_safety')
 run=load(a.candidate_run); arts=load(a.candidate_artifacts); man=load(a.artifact_manifest); rec=load(a.candidate_receipt); cand=load(a.resource_candidate); prov=load(a.provenance); da=load(a.downstream_repair_authority)
 if run.get('name')!=c['required_candidate_workflow_name'] or run.get('path')!=c['required_candidate_workflow_path'] or run.get('status')!='completed' or run.get('conclusion')!='success' or not pos(run.get('id')):e.append('candidate_run')
 rid=run.get('id'); prefix=c['required_candidate_artifact_name_prefix']; matches=[x for x in arts.get('artifacts',[]) if isinstance(x,dict) and str(x.get('name','')).startswith(prefix)]
 art=matches[0] if len(matches)==1 else None
 if art is None:e.append('candidate_artifact_count_'+str(len(matches)))
 else:
  if art.get('expired') is True:e.append('candidate_artifact_expired')
  if art.get('name')!=f'{prefix}{rid}':e.append('candidate_artifact_name')
 zsha=sha(a.candidate_artifact_zip)
 if art is not None and digest(art.get('digest')) not in (None,zsha):e.append('candidate_artifact_digest')
 files=man.get('files',[])
 for req in c['required_exact_files_in_candidate_artifact']:
  if sum(1 for x in files if isinstance(x,str) and Path(x).name==req)!=1:e.append('artifact_file_'+req)
 csha=sha(a.resource_candidate); psha=sha(a.provenance); rsha=sha(a.candidate_receipt)
 for label,d in (('candidate',cand),('provenance',prov),('receipt',rec)):
  if synth(d):e.append(label+'_marked_synthetic')
 if rec.get('classification')!=READY or rec.get('candidate_only') is not True or rec.get('durable_repository_authority_created') is not False or rec.get('resource_authority_candidate_sha256')!=csha or rec.get('provenance_sha256')!=psha or rec.get('candidate_classification')!=RESOURCE_PASS:e.append('receipt_binding')
 if rec.get('parser_capacity')!=1048576 or rec.get('class_build_authority_git_blob')!=c['required_class_build_authority_git_blob']:e.append('receipt_parser_build')
 if any(rec.get(k) is not False for k in ('scientific_execution_authorized','covariance_restriction_authorized','Wm_S3_opened')):e.append('receipt_downstream')
 if cand.get('schema')!=c['required_candidate_schema'] or cand.get('classification')!=RESOURCE_PASS:e.append('candidate_identity')
 for k,v in c['required_candidate_bits'].items():
  if cand.get(k)!=v:e.append('candidate_bit_'+k)
 frozen=c['required_frozen_identities']
 if cand.get('materialization_contract_git_blob')!=frozen['materialization_contract_git_blob'] or cand.get('parser_capacity')!=1048576 or cand.get('class_build_authority_git_blob')!=c['required_class_build_authority_git_blob']:e.append('candidate_parser_build')
 if not isinstance(cand.get('candidate_memtotal_kb'),int) or cand['candidate_memtotal_kb']<=c['candidate_memtotal_kb_must_be_strictly_greater_than']:e.append('candidate_memory')
 if cand.get('provenance_receipt_json_sha256')!=psha or cand.get('required_custom_label')!='dsir-32769-highmem':e.append('candidate_provenance_label')
 for k in ('source_run_id','source_job_id','source_artifact_id','independent_run_id','independent_job_id','independent_artifact_id'):
  if cand.get(k)!=prov.get(k) or not pos(prov.get(k)):e.append('candidate_provenance_'+k)
 for k in ('source_artifact_zip_sha256','independent_artifact_zip_sha256','source_head_sha','independent_head_sha'):
  if cand.get(k)!=prov.get(k):e.append('candidate_provenance_'+k)
 if prov.get('classification')!=PROV_PASS or prov.get('valid') is not True or prov.get('errors')!=[] or prov.get('candidate_only') is not True or prov.get('durable_repository_authority_created') is not False or prov.get('packaging_contract_git_blob')!=frozen['packaging_contract_git_blob'] or prov.get('parser_capacity')!=1048576 or prov.get('class_build_authority_git_blob')!=c['required_class_build_authority_git_blob'] or prov.get('scientific_execution_authorized') is not False:e.append('provenance_validity')
 if da.get('classification')!='LAYERB_32769_V03_DOWNSTREAM_CHAIN_FINAL_AUDIT_PASS_PLUS_0_PLUS_0' or da.get('candidate_packaging_workflow_git_blob')!=c['required_candidate_workflow_git_blob'] or da.get('candidate_packaging_contract_v02_git_blob')!=frozen['packaging_contract_git_blob'] or da.get('candidate_packager_v02_git_blob')!=frozen['packager_git_blob'] or da.get('materialization_contract_v02_git_blob')!=frozen['materialization_contract_git_blob'] or da.get('materializer_v02_git_blob')!=frozen['materializer_git_blob'] or da.get('required_parser_capacity')!=1048576 or da.get('required_class_build_authority_git_blob')!=c['required_class_build_authority_git_blob'] or da.get('repository_write_forbidden') is not True or da.get('actual_resource_authority_exists') is not False or da.get('scientific_execution_authorized') is not False:e.append('downstream_repair_authority')
 ok=not e;cls=PASS if ok else FAIL
 out={'schema':'LAYERB_32769_RESOURCE_AUTHORITY_PROMOTION_REVIEW_V0_2','classification':cls,'effect':'+0/+0','valid':ok,'errors':e,'promotion_target_path':c['promotion_target_path'],'promotion_is_exact_byte_copy_only':True,'exact_resource_authority_candidate_sha256':csha,'candidate_receipt_sha256':rsha,'provenance_sha256':psha,'candidate_run_id':rid,'candidate_head_sha':run.get('head_sha'),'candidate_artifact_id':art.get('id') if art else None,'candidate_artifact_zip_sha256':zsha,'exact_candidate_classification':cand.get('classification'),'candidate_memtotal_kb':cand.get('candidate_memtotal_kb'),'parser_capacity':cand.get('parser_capacity'),'class_build_authority_git_blob':cand.get('class_build_authority_git_blob'),'review_creates_no_repository_authority':True,'high_memory_resource_lifecycle_preflight_pass_created_by_review':False,'scientific_execution_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':cls}
 Path(a.out).parent.mkdir(parents=True,exist_ok=True);Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(cls)
 if e:print('ERRORS',','.join(e))
 return 0 if ok else 31
if __name__=='__main__':raise SystemExit(main())
