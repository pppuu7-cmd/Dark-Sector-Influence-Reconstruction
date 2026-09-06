#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
CMP=HERE/'exp073fg_compare_terminal_receipts_v0_1.py'
HEAD='de83e20a68f79ccf25b89b0d33eb4206e294c757'
FP='b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251'
STAGES=['fresh_sources_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete']
NS={'A':'checkpoints/exp073fg-ww-s0-s3-a-v0-1','B':'checkpoints/exp073fg-ww-s0-s3-b-v0-1'}
PASS='PASS_EXP073FG_WW_S0_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'
FAIL='FAIL_EXP073FG_WW_S0_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'

def sha(p:Path): return hashlib.sha256(p.read_bytes()).hexdigest()
def writej(p:Path,o): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')

def build_rep(root:Path,rep:str,mismatch:bool=False):
    rr=root/'checkpoints'/rep; (rr/'exact_route').mkdir(parents=True,exist_ok=True)
    a=np.zeros((39,12288),dtype='<f8')
    if mismatch and rep=='B': a[0,0]=np.nextafter(np.float64(0.0),np.float64(1.0))
    ep=rr/'exact_route'/'selected_ee.bin'; a.tofile(ep); hee=sha(ep)
    rp=rr/'replica_receipt.json'
    rec={'replica':rep,'source_pair':'S0->S3','ordered_source_indices':[0,3],'same_field_object_handoff':False,'bpw_route':'public_get_bandpower_windows_after_filebacked_fits_read','source_head':HEAD,'contract_fingerprint':FP,'checkpoint_namespace':NS[rep],'historical_ww_numerical_import':False,'other_replica_output_read':False,'science_gate_scored':False,'selected_ee_sha256':hee,'selected_ee_path':str(ep)}
    writej(rp,rec); hrp=sha(rp)
    manifest_sha={}
    for st in STAGES:
        payloads={}
        if st=='replica_receipt_complete': payloads={'selected_ee':{'sha256':hee},'replica_receipt':{'sha256':hrp}}
        p=rr/(st+'.json'); writej(p,{'schema':'synthetic','stage':st,'complete':True,'replica':rep,'checkpoint_namespace':NS[rep],'source_head':HEAD,'contract_fingerprint':FP,'payloads':payloads}); manifest_sha[st]=sha(p)
    pp=rr/'post_receipt_prune.json'
    writej(pp,{'replica':rep,'checkpoint_namespace':NS[rep],'source_head':HEAD,'contract_fingerprint':FP,'source_pair':'S0->S3','ordered_source_indices':[0,3],'complete_chain_verified_before_prune':True,'preserved_complete_receipt':True,'pruned_only_after_receipt':True,'no_tolerance_rescue':True,'selected_ee_sha256':hee,'replica_receipt_sha256':hrp,'stage_manifest_sha256':manifest_sha,'verified_payload_sha256':{'selected_ee':hee,'replica_receipt':hrp}})

def build(root:Path,mismatch=False):
    build_rep(root,'A',mismatch); build_rep(root,'B',mismatch)

def run(root:Path):
    out=root/'ab.json'
    return subprocess.run([sys.executable,str(CMP),'--root',str(root),'--out',str(out)],text=True,capture_output=True),out

def main():
    with tempfile.TemporaryDirectory() as td:
        base=Path(td)/'pass'; build(base,False); q,out=run(base)
        if q.returncode!=0 or q.stdout.strip()!=PASS: raise RuntimeError(f'exact PASS fixture failed: {q.stdout} {q.stderr}')
        d=json.loads(out.read_text()); assert d['sha256_equal'] is True and d['numpy_array_equal'] is True and d['all_finite'] is True and d['terminal_compare_restored_replica'] is False

        ulp=Path(td)/'ulp'; build(ulp,True); q,out=run(ulp)
        if q.returncode!=0 or q.stdout.strip()!=FAIL: raise RuntimeError(f'1-ULP fixture not exact scientific FAIL: {q.stdout} {q.stderr}')
        d=json.loads(out.read_text()); assert d['sha256_equal'] is False and d['numpy_array_equal'] is False and d['all_finite'] is True

        payload=Path(td)/'payload'; build(payload,False)
        ep=payload/'checkpoints'/'B'/'exact_route'/'selected_ee.bin'
        with ep.open('r+b') as f: f.seek(0); b=f.read(1); f.seek(0); f.write(bytes([b[0]^1]))
        q,_=run(payload)
        if q.returncode==0: raise RuntimeError('tampered selected payload was not rejected fail-closed')

        stage=Path(td)/'stage'; build(stage,False)
        sp=stage/'checkpoints'/'A'/'fresh_workspace_mcm_complete.json'; o=json.loads(sp.read_text()); o['tamper']=1; writej(sp,o)
        q,_=run(stage)
        if q.returncode==0: raise RuntimeError('tampered stage manifest was not rejected fail-closed')

    print('PASS_EXP073FI_EXP073FG_TERMINAL_COMPARE_SYNTHETIC_HARDENING_V0_1')
    print('classification=SUPPORT_PLUS_0_PLUS_0')
    print('ww_s0_s3_authority_created=false')

if __name__=='__main__': main()
