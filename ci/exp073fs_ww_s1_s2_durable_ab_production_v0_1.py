#!/usr/bin/env python3
from __future__ import annotations

import gc
import hashlib
import importlib.util
import json
from pathlib import Path

BASE = Path(__file__).with_name('exp073fa_ww_s0_s2_durable_ab_production_v0_1.py')
BASE_SHA256 = 'fe354b95e9aeefe0772f4c7eecbba6e1944fb1f4955fceb3e9e72ed1c06b293a'
SCHEMA = 'dsir.exp073fs.ww_s1_s2.durable_ab_production.v0.1'
CHECKPOINT_ORDER = ['fresh_sources_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete']
NAMESPACES = {'A':'checkpoints/exp073fs-ww-s1-s2-a-v0-1','B':'checkpoints/exp073fs-ww-s1-s2-b-v0-1'}


def load_base():
    raw = BASE.read_bytes()
    got = hashlib.sha256(raw).hexdigest()
    if got != BASE_SHA256:
        raise RuntimeError(f'fail-closed Exp073FA base SHA256 drift {got}')
    spec = importlib.util.spec_from_file_location('exp073fs_base_fa', BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError('fail-closed cannot load frozen Exp073FA base')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.SCHEMA = SCHEMA
    mod.CHECKPOINT_ORDER = CHECKPOINT_ORDER
    mod.NAMESPACES = NAMESPACES
    return mod


def install_s1s2(mod):
    def manifest(root,stage,replica,head,fp,payloads):
        if stage not in CHECKPOINT_ORDER:
            raise RuntimeError(stage)
        r={'schema':SCHEMA+'.checkpoint','stage':stage,'complete':True,'replica':replica,'checkpoint_namespace':NAMESPACES[replica],'source_head':head,'contract_fingerprint':fp,'payloads':payloads,'historical_ww_numerical_import':False,'other_replica_output_read':False}
        mod.atomic_json(root/(stage+'.json'),r)
        return r

    def load_manifest(root,stage,replica,head,fp):
        p=root/(stage+'.json')
        if not p.exists():
            return None
        r=json.loads(p.read_text())
        ok=(r.get('schema')==SCHEMA+'.checkpoint' and r.get('complete') is True and r.get('stage')==stage and r.get('replica')==replica and r.get('checkpoint_namespace')==NAMESPACES[replica] and r.get('source_head')==head and r.get('contract_fingerprint')==fp and r.get('historical_ww_numerical_import') is False and r.get('other_replica_output_read') is False)
        if not ok:
            raise RuntimeError('fail-closed WW_S1_S2 checkpoint identity mismatch')
        return r

    def mmap_payload_sha(p:Path):
        a=mod.np.load(p,mmap_mode='r',allow_pickle=False)
        if a.dtype.str!='<f8' or tuple(a.shape)!=(12*4096*4096,):
            raise RuntimeError('fail-closed source restore geometry')
        h=hashlib.sha256(memoryview(a).cast('B')).hexdigest()
        del a
        return h

    def fresh_or_restore_sources(root,replica,r1_root,r1_digest,head,fp):
        st=load_manifest(root,'fresh_sources_complete',replica,head,fp)
        p1=root/'s1_count_map.npy'; p2=root/'s2_count_map.npy'
        if st is None:
            auth=mod.validate_r1(r1_root,r1_digest)
            s1,m1=mod.source_count_map(r1_root,1); h1=mod.atomic_npy(p1,s1); del s1; gc.collect()
            s2,m2=mod.source_count_map(r1_root,2); h2=mod.atomic_npy(p2,s2); del s2; gc.collect()
            st=manifest(root,'fresh_sources_complete',replica,head,fp,{
                's1_count_map':{'canonical_sha256':h1,'shape':[12*4096*4096],'dtype':'<f8'},
                's2_count_map':{'canonical_sha256':h2,'shape':[12*4096*4096],'dtype':'<f8'},
                'r1_authority':auth,'s1_authority':m1,'s2_authority':m2,
                'ordered_source_indices':[1,2],'reconstruction_counts':{'s1':1,'s2':1},'same_source_map_both_sides':False})
        for p,k in ((p1,'s1_count_map'),(p2,'s2_count_map')):
            if not p.exists():
                raise RuntimeError('fail-closed missing source checkpoint payload')
            if mmap_payload_sha(p)!=st['payloads'][k]['canonical_sha256']:
                raise RuntimeError('fail-closed source restore SHA mismatch')
        if st['payloads'].get('ordered_source_indices')!=[1,2] or st['payloads'].get('reconstruction_counts')!={'s1':1,'s2':1} or st['payloads'].get('same_source_map_both_sides') is not False:
            raise RuntimeError('fail-closed S1S2 source semantics')
        return p1,p2,st

    def strict_validated_finished(root,replica,head,fp):
        final=load_manifest(root,'replica_receipt_complete',replica,head,fp)
        if final is None:
            return None
        stages={}
        for stage in CHECKPOINT_ORDER:
            st=load_manifest(root,stage,replica,head,fp)
            if st is None:
                raise RuntimeError(f'fail-closed missing complete-stage manifest {stage}')
            stages[stage]=st
        p1=root/'s1_count_map.npy'; p2=root/'s2_count_map.npy'; wp=root/'fresh_workspace.fits'; full=root/'exact_route'/'full_window.bin'; ee=root/'exact_route'/'selected_ee.bin'; rp=root/'replica_receipt.json'
        for p in (p1,p2,wp,full,ee,rp):
            if not p.is_file():
                raise RuntimeError(f'fail-closed missing complete-stage payload {p.name}')
        src=stages['fresh_sources_complete']['payloads']
        if mmap_payload_sha(p1)!=src['s1_count_map']['canonical_sha256'] or mmap_payload_sha(p2)!=src['s2_count_map']['canonical_sha256'] or src.get('ordered_source_indices')!=[1,2] or src.get('reconstruction_counts')!={'s1':1,'s2':1}:
            raise RuntimeError('fail-closed S1S2 source complete-stage payload')
        hwp=mod.file_sha(wp); hfull=mod.file_sha(full); hee=mod.file_sha(ee); hrp=mod.file_sha(rp)
        if hwp!=stages['fresh_workspace_mcm_complete']['payloads']['workspace_fits']['sha256'] or hwp!=stages['mcm_fits_verified']['payloads']['workspace_fits']['sha256']:
            raise RuntimeError('fail-closed workspace complete-stage payload hash')
        if hfull!=stages['full_window_complete']['payloads']['full_window']['sha256']:
            raise RuntimeError('fail-closed full-window complete-stage payload hash')
        if hee!=stages['selected_ee_complete']['payloads']['selected_ee']['sha256'] or hee!=final['payloads']['selected_ee']['sha256']:
            raise RuntimeError('fail-closed selected-EE complete-stage payload hash')
        if hrp!=final['payloads']['replica_receipt']['sha256']:
            raise RuntimeError('fail-closed receipt complete-stage payload hash')
        r=json.loads(rp.read_text())
        if Path(r.get('selected_ee_path',''))!=ee or r.get('selected_ee_sha256')!=hee:
            raise RuntimeError('fail-closed completed receipt selected payload identity')
        if r.get('source_pair')!='S1->S2' or r.get('ordered_source_indices')!=[1,2] or r.get('same_field_object_handoff') is not False or r.get('bpw_route')!='public_get_bandpower_windows_after_filebacked_fits_read':
            raise RuntimeError('fail-closed completed receipt S1S2 public-route semantics')
        return r

    def run_replica(replica,args):
        if replica not in NAMESPACES:
            raise RuntimeError(replica)
        v=mod.importlib.metadata.version('pymaster')
        if not (v=='2.7' or v.startswith('2.7.')):
            raise RuntimeError('PyMaster 2.7 required')
        for k,val in mod.THREAD_ENV.items():
            if mod.os.environ.get(k,val)!=val:
                raise RuntimeError(f'{k} must be {val}')
            mod.os.environ[k]=val
        root=Path(args.checkpoint_root)/replica; root.mkdir(parents=True,exist_ok=True)
        done=strict_validated_finished(root,replica,args.source_head,args.contract_fingerprint)
        if done is not None:
            return done
        wp=root/'fresh_workspace.fits'; ws=load_manifest(root,'fresh_workspace_mcm_complete',replica,args.source_head,args.contract_fingerprint)
        if ws is None:
            p1,p2,src=fresh_or_restore_sources(root,replica,Path(args.r1_root),args.r1_artifact_digest,args.source_head,args.contract_fingerprint)
            s1=mod.np.load(p1,mmap_mode='r',allow_pickle=False); f1=mod.nmt.NmtField(s1,None,spin=2); del s1; gc.collect()
            s2=mod.np.load(p2,mmap_mode='r',allow_pickle=False); f2=mod.nmt.NmtField(s2,None,spin=2); del s2; gc.collect()
            if id(f1)==id(f2):
                raise RuntimeError('fail-closed distinct-field identity collision')
            ids=[id(f1),id(f2)]
            b=mod.nmt.NmtBin.from_edges(mod.BAND_EDGES[:-1],mod.BAND_EDGES[1:]); w=mod.nmt.NmtWorkspace()
            w.compute_coupling_matrix(f1,f2,b); w.write_to(str(wp)); wsha=mod.file_sha(wp)
            ws=manifest(root,'fresh_workspace_mcm_complete',replica,args.source_head,args.contract_fingerprint,{
                'workspace_fits':{'sha256':wsha},'same_field_object_handoff':False,'ordered_source_indices':[1,2],
                'field_object_ids':ids,'field_construction_count':2,
                'source_map_sha256':[src['payloads']['s1_count_map']['canonical_sha256'],src['payloads']['s2_count_map']['canonical_sha256']]})
            del w,b,f2,f1; gc.collect()
        else:
            if ws['payloads'].get('same_field_object_handoff') is not False or ws['payloads'].get('ordered_source_indices')!=[1,2] or ws['payloads'].get('field_construction_count')!=2:
                raise RuntimeError('fail-closed restored S1S2 field-order semantics mismatch')
            ids=ws['payloads'].get('field_object_ids',[])
            if len(ids)!=2 or ids[0]==ids[1]:
                raise RuntimeError('fail-closed restored distinct-field identity mismatch')
            if not wp.exists() or mod.file_sha(wp)!=ws['payloads']['workspace_fits']['sha256']:
                raise RuntimeError('fail-closed workspace restore SHA mismatch')
            wsha=ws['payloads']['workspace_fits']['sha256']
        manifest(root,'mcm_fits_verified',replica,args.source_head,args.contract_fingerprint,{'workspace_fits':{'sha256':wsha},'ordered_source_indices':[1,2],'same_field_object_handoff':False})
        ee_st=load_manifest(root,'selected_ee_complete',replica,args.source_head,args.contract_fingerprint); full_st=load_manifest(root,'full_window_complete',replica,args.source_head,args.contract_fingerprint)
        full=root/'exact_route'/'full_window.bin'; ee=root/'exact_route'/'selected_ee.bin'
        if ee_st is not None:
            if not ee.exists() or mod.file_sha(ee)!=ee_st['payloads']['selected_ee']['sha256']:
                raise RuntimeError('fail-closed selected EE restore mismatch')
            if full_st is None or not full.exists() or mod.file_sha(full)!=full_st['payloads']['full_window']['sha256']:
                raise RuntimeError('fail-closed full-window restore mismatch')
            ap=root/'exact_route'/'public_bpw_receipt.json'
            if not ap.is_file():
                raise RuntimeError('fail-closed missing public BPW adapter receipt on restore')
            adapter=json.loads(ap.read_text())
            if adapter.get('route')!='public_get_bandpower_windows_after_filebacked_fits_read' or adapter.get('no_tolerance_rescue') is not True:
                raise RuntimeError('fail-closed restored public BPW adapter receipt')
        else:
            full,ee,adapter=mod.public_bpw_from_serialized_workspace(wp,root/'exact_route')
            manifest(root,'full_window_complete',replica,args.source_head,args.contract_fingerprint,{'full_window':{'sha256':mod.file_sha(full),'shape':list(mod.FULL_SHAPE),'route':adapter['route'],'mcm_filebacked':True}})
            manifest(root,'selected_ee_complete',replica,args.source_head,args.contract_fingerprint,{'selected_ee':{'sha256':mod.file_sha(ee),'shape':list(mod.EE_SHAPE),'dtype':'<f8','semantics':'wins[0,:,0,:] = EE<-EE','route':adapter['route']}})
        rec={'schema':SCHEMA+'.replica','replica':replica,'selected_ee_sha256':mod.file_sha(ee),'selected_ee_path':str(ee),'workspace_fits_sha256':wsha,'adapter_receipt':adapter,'bpw_route':'public_get_bandpower_windows_after_filebacked_fits_read','ordered_source_indices':[1,2],'same_field_object_handoff':False,'source_pair':'S1->S2','source_map_sha256':ws['payloads']['source_map_sha256'],'source_head':args.source_head,'contract_fingerprint':args.contract_fingerprint,'checkpoint_namespace':NAMESPACES[replica],'historical_ww_numerical_import':False,'other_replica_output_read':False,'science_gate_scored':False}
        mod.atomic_json(root/'replica_receipt.json',rec)
        manifest(root,'replica_receipt_complete',replica,args.source_head,args.contract_fingerprint,{'replica_receipt':{'sha256':mod.file_sha(root/'replica_receipt.json')},'selected_ee':{'sha256':rec['selected_ee_sha256']}})
        return rec

    def compare(a,b,out):
        for r in (a,b):
            if r.get('source_pair')!='S1->S2' or r.get('ordered_source_indices')!=[1,2] or r.get('same_field_object_handoff') is not False or r.get('bpw_route')!='public_get_bandpower_windows_after_filebacked_fits_read' or r.get('historical_ww_numerical_import') is not False or r.get('other_replica_output_read') is not False:
                raise RuntimeError('fail-closed A/B S1S2 semantics')
        aa=mod.np.memmap(a['selected_ee_path'],dtype='<f8',mode='r',shape=mod.EE_SHAPE); bb=mod.np.memmap(b['selected_ee_path'],dtype='<f8',mode='r',shape=mod.EE_SHAPE)
        se=a['selected_ee_sha256']==b['selected_ee_sha256']; ae=bool(mod.np.array_equal(aa,bb)); finite=bool(mod.np.isfinite(aa).all() and mod.np.isfinite(bb).all()); del aa,bb
        status='PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1' if se and ae and finite else 'FAIL_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'
        r={'schema':SCHEMA+'.ab_compare','status':status,'classification':'SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION' if status.startswith('PASS_') else 'SCIENTIFIC_FAIL','sha256_equal':se,'numpy_array_equal':ae,'all_finite':finite,'a_sha256':a['selected_ee_sha256'],'b_sha256':b['selected_ee_sha256'],'source_pair':'S1->S2','ordered_source_indices':[1,2],'bpw_route':'public_get_bandpower_windows_after_filebacked_fits_read','same_field_object_handoff':False,'no_tolerance_rescue':True,'historical_ww_numerical_import':False,'other_replica_output_read':False,'science_gate_scored':True,'ww_s1_s2_authority_created':False}
        mod.atomic_json(out,r); return r

    mod.manifest=manifest; mod.load_manifest=load_manifest; mod.fresh_or_restore_sources=fresh_or_restore_sources; mod.validated_finished=strict_validated_finished; mod.run_replica=run_replica; mod.compare=compare
    return mod


def load_s1s2():
    return install_s1s2(load_base())


if __name__=='__main__':
    load_s1s2().main()
