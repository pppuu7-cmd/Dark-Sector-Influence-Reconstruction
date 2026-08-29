#!/usr/bin/env python3
from __future__ import annotations

import argparse, collections, hashlib, json, re
from pathlib import Path

PASS='PASS_EXP073AB_DES_ROW_OPERATOR_MAPPING_V0_1'
T_SHA='55f55d21eedd3779a729af387205ec7db360617c5e026406d21b3b542f355309'
U_SHA='a6b9eaa697edd63d5b5ca698341c35578d395201ff3e0e0bcffff7f5ba94f534'
Z2_SHA='3cb25beed23193a94e10d590296349713d1d83f92771215b72c10ea2e6f82c1a'
WM_ID_SHA='dc20ff104c707d006992c1579ce9175295fae426b1c32ff47e56c53d9300603a'
WW_ID_SHA='e0cc92706598a8ac6360d0fd669451e4816091f83c01e8744940e94a2b8593b5'
DES_ID_SHA='736f80a6dd407b1a3891cb34f35262e415a4f0c9bbb200a9f376102b05988ee4'
FULL_U_SHA='bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75'
MAP_SHA='092bb2e83a0ad0d7ad5359110465eccfe2c6096e593c60c459c52c9a2b7e4319'
WM_MAP_SHA='4dc85efa2372242d8c612a84a8066dc0bd5774ef8260b5c15b3e5378c8800422'
WW_MAP_SHA='ffe84463b276030a6248ab289255b472f0d809882d0a577c26fb5e12e34912bf'
GATES={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}
WM_RE=re.compile(r'^Wm\|DESgc__(\d)\|DESwl__(\d)\|TE\|component=0\|bp=(\d\d)\|ell=(\d+):(\d+)$')
WW_RE=re.compile(r'^WW\|DESwl__(\d)\|DESwl__(\d)\|EE\|component=0\|bp=(\d\d)\|ell=(\d+):(\d+)$')
WW_PAIRS=[(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]

def sha_file(p:Path)->str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def order_sha(ids:list[str])->str:
    return hashlib.sha256(('\n'.join(ids)+'\n').encode()).hexdigest()

def lines_sha(lines:list[str])->str:
    return hashlib.sha256(('\n'.join(lines)+'\n').encode()).hexdigest()

def load_exact(path:str,expected:str)->dict:
    p=Path(path); got=sha_file(p)
    if got!=expected: raise AssertionError(f'{p.name} SHA mismatch {got}')
    return json.loads(p.read_text())

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--inventory',required=True)
    ap.add_argument('--skeleton',required=True)
    ap.add_argument('--radial',required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()

    inv=load_exact(a.inventory,T_SHA)
    u=load_exact(a.skeleton,U_SHA)
    z2=load_exact(a.radial,Z2_SHA)

    assert inv['status']=='PASS_EXP073T_PINNED_COSMOTHEKA_INVENTORY_V0_1'
    assert u['status']=='PASS_EXP073U_ARTICLE3_PRESUPPORT_COORDINATE_SKELETON_V0_1'
    assert z2['status']=='PASS_EXP073Z2_DES_RADIAL_KERNEL_STABLE_DIRECT_V0_2'
    assert u['ordered_coordinate_id_sha256']==FULL_U_SHA
    assert u['blocks']['Wm']['offset']==[0,780] and u['blocks']['WW']['offset']==[780,1170]
    wm=inv['Wm_coordinate_ids']; ww=inv['WW_coordinate_ids']
    assert len(wm)==780 and len(ww)==390
    assert order_sha(wm)==inv['Wm_coordinate_order_sha256']==WM_ID_SHA
    assert order_sha(ww)==inv['WW_coordinate_order_sha256']==WW_ID_SHA
    assert order_sha(wm+ww)==inv['DES_coordinate_order_sha256']==DES_ID_SHA
    assert u['ordered_coordinate_ids'][:1170]==wm+ww

    edges=inv['bandpower_edges']; assert len(edges)==40 and inv['bandpowers_per_pair']==39
    assert inv['Wm_pairs']==[[f'DESgc__{l}',f'DESwl__{s}'] for l in range(5) for s in range(4)]
    assert inv['WW_pairs']==[[f'DESwl__{i}',f'DESwl__{j}'] for i,j in WW_PAIRS]
    expected_wm_radial=[f'L{l+1}xS{s+1}' for l in range(5) for s in range(4)]
    expected_ww_radial=[f'S{i+1}xS{j+1}' for i,j in WW_PAIRS]
    assert z2['kernel_order']['Wm']==expected_wm_radial
    assert z2['kernel_order']['WW']==expected_ww_radial
    assert z2['fine_authority']['Wm_radial']['sha256']=='414f47620071c1df6c23abe25d45312796af53a37102c34e1d844308d915efe1'
    assert z2['fine_authority']['WW_radial']['sha256']=='56edaaf9ef6b03d00e7b83f158b204fc27171bef34a6a7bf3afbd8c71ed5cc0e'

    rows=[]; lines=[]
    for ordinal,cid in enumerate(wm):
        m=WM_RE.fullmatch(cid)
        if not m: raise AssertionError(f'bad Wm ID {cid}')
        l,s,b,lo,hi=map(int,m.groups())
        assert 0<=l<5 and 0<=s<4 and 0<=b<39
        assert [lo,hi]==[edges[b],edges[b+1]]
        ridx=4*l+s; task=f'Wm_S{s}'
        rec={'global_des_ordinal':ordinal,'coordinate_id':cid,'block':'Wm','angular_task':task,
             'radial_index':ridx,'radial_name':expected_wm_radial[ridx],
             'band_index':b,'ell_lo':lo,'ell_hi':hi}
        rows.append(rec); lines.append(f'{ordinal}\t{cid}\t{task}\t{ridx}\t{b}\t{lo}\t{hi}')
    for local,cid in enumerate(ww):
        m=WW_RE.fullmatch(cid)
        if not m: raise AssertionError(f'bad WW ID {cid}')
        i,j,b,lo,hi=map(int,m.groups())
        pair=(i,j)
        if pair not in WW_PAIRS: raise AssertionError(f'bad WW pair {pair}')
        assert 0<=b<39 and [lo,hi]==[edges[b],edges[b+1]]
        ridx=WW_PAIRS.index(pair); ordinal=780+local; task=f'WW_S{i}_S{j}'
        rec={'global_des_ordinal':ordinal,'coordinate_id':cid,'block':'WW','angular_task':task,
             'radial_index':ridx,'radial_name':expected_ww_radial[ridx],
             'band_index':b,'ell_lo':lo,'ell_hi':hi}
        rows.append(rec); lines.append(f'{ordinal}\t{cid}\t{task}\t{ridx}\t{b}\t{lo}\t{hi}')

    assert len(rows)==1170 and len({r['coordinate_id'] for r in rows})==1170
    assert lines_sha(lines)==MAP_SHA
    assert lines_sha(lines[:780])==WM_MAP_SHA
    assert lines_sha(lines[780:])==WW_MAP_SHA

    task_counts=collections.Counter(r['angular_task'] for r in rows)
    radial_wm=collections.Counter(r['radial_index'] for r in rows if r['block']=='Wm')
    radial_ww=collections.Counter(r['radial_index'] for r in rows if r['block']=='WW')
    assert task_counts==collections.Counter({**{f'Wm_S{s}':195 for s in range(4)},**{f'WW_S{i}_S{j}':39 for i,j in WW_PAIRS}})
    assert radial_wm==collections.Counter({i:39 for i in range(20)})
    assert radial_ww==collections.Counter({i:39 for i in range(10)})
    for block,nrad in [('Wm',20),('WW',10)]:
        for ridx in range(nrad):
            bs=sorted(r['band_index'] for r in rows if r['block']==block and r['radial_index']==ridx)
            assert bs==list(range(39))

    result={
      'experiment':'Exp073AB','status':PASS,'record_type':'DES_ROW_TO_FACTORIZED_OPERATOR_MAPPING_NONCLASSIFYING',
      'parent_authority':{
        'exp073t':{'run':33272691162,'artifact':9720563095,'artifact_digest':'sha256:4332ffa9d6b4385a48d3022a8afcedf0bf00a742cee8444fd6ca83842bf1e642','internal_sha256':T_SHA},
        'exp073u':{'run':33274852199,'artifact':9721184683,'artifact_digest':'sha256:d44e628e9312fb5a919a6681b69d9e06e18418cdd299de641e6465e60dadfd68','internal_sha256':U_SHA},
        'exp073z2':{'run':33279208949,'artifact':9722468056,'artifact_digest':'sha256:3eb8b025711e8df6d5452a3a57002f36c9d7de2b9116734b71d15d6822dd20be','internal_sha256':Z2_SHA}
      },
      'counts':{'DES':1170,'Wm':780,'WW':390,'Wm_radial':20,'WW_radial':10,'angular_tasks':14},
      'mapping_sha256':MAP_SHA,'Wm_mapping_sha256':WM_MAP_SHA,'WW_mapping_sha256':WW_MAP_SHA,
      'inherited_coordinate_order_sha256':{'Wm':WM_ID_SHA,'WW':WW_ID_SHA,'DES':DES_ID_SHA,'full_Exp073U_1410':FULL_U_SHA},
      'task_counts':dict(sorted(task_counts.items())),'Wm_radial_counts':{str(k):radial_wm[k] for k in range(20)},'WW_radial_counts':{str(k):radial_ww[k] for k in range(10)},
      'rows':rows,
      'angular_window_values_read':False,'physical_k_computed':False,'physical_support_evaluated':False,'retained_coordinates_evaluated':False,'science_gate_scored':False,
      'covariance_read':False,'nuisance_geometry_read':False,'relation_null_read':False,'G8_read':False,
      'article3_scientific_readiness_percent':52,'gate_state':GATES,
      'next_authorized_step':'After exact 14-window angular authority exists, join by this mapping with Exp073Z2 and BOSS authority into one immutable pre-support candidate manifest; still do not score Layer A before that manifest is frozen.'
    }
    out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(PASS,MAP_SHA)

if __name__=='__main__': main()
