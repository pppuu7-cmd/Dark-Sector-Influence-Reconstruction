#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gc
import hashlib
import importlib.metadata
import json
from pathlib import Path

import healpy as hp
import numpy as np
import pymaster as nmt

NSIDE=4096
NPIX=12*NSIDE*NSIDE
LMAX_PLUS_ONE=3*NSIDE
BAND_EDGES=np.array([
    0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,
    852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,
    5047,5731,6508,7390,8392,9529,10821,12288
],dtype=np.int64)
PASS='PASS_EXP073AA_DES_ANGULAR_TASK_V0_1'
R1_PASS='PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1'
R1_ARTIFACT_DIGEST='sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd'
R1_SUMMARY_SHA='100458e046088b24cba671db1852112676e487331d5c1f5c5cb55f8a9e011df4'
METACAL_BYTES=84_075_649_920
METACAL_SHA='39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8'
LENS_BYTES=104_595_840
LENS_SHA='a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55'
GATES={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}

SOURCE={
  0:{'selected':7_705_486,'bytes':30_821_944,'record_sha':'5b507215ca961c09b82786e61e681a0178c29e9b593c17b588e366722a021f15','unique':4_305_774,'occupancy_sha':'b6ed74f31540d4041267f94e2f7cdb70b7040d943ba22a4aa7eab62418f8cb32'},
  1:{'selected':7_851_711,'bytes':31_406_844,'record_sha':'752f585125e413c7bd40cc5174cf7ef98e95f970022a351c5d91206f371d2241','unique':4_339_193,'occupancy_sha':'fed1ffdf2ef7a7ae88e42615bd08e207e039239c44fa20b7994258f147a739f1'},
  2:{'selected':8_238_547,'bytes':32_954_188,'record_sha':'259295a1f5a23ad9e5c6b46842bcf612b0eb13dc701ab6d54eb15f0d7bb0105f','unique':4_401_919,'occupancy_sha':'9e2bfb92289ca4a3abb11efabf7ac8d59bb7c68eb63a7104c2b247267733b24d'},
  3:{'selected':4_196_641,'bytes':16_786_564,'record_sha':'3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec','unique':2_943_132,'occupancy_sha':'21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094'},
}

ALL_TASKS=['Wm_S0','Wm_S1','Wm_S2','Wm_S3',
           'WW_S0_S0','WW_S0_S1','WW_S0_S2','WW_S0_S3',
           'WW_S1_S1','WW_S1_S2','WW_S1_S3',
           'WW_S2_S2','WW_S2_S3','WW_S3_S3']

def sha_file(p:Path,chunk:int=8<<20)->str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(chunk),b''):
            h.update(b)
    return h.hexdigest()

def one(root:Path,name:str)->Path:
    hits=list(root.rglob(name))
    if len(hits)!=1:
        raise AssertionError(f'expected exactly one {name}, found {len(hits)}')
    return hits[0]

def canonical_hash(a:np.ndarray,dtype:str='<f8')->dict:
    x=np.ascontiguousarray(np.asarray(a,dtype=np.dtype(dtype)))
    return {'dtype':x.dtype.str,'shape':list(x.shape),'sha256':hashlib.sha256(x.tobytes(order='C')).hexdigest()}

def occupancy_sha_from_counts(counts:np.ndarray)->tuple[int,str]:
    h=hashlib.sha256()
    block=8_388_608
    nbytes=0
    for lo in range(0,counts.size,block):
        hi=min(counts.size,lo+block)
        bits=(np.asarray(counts[lo:hi])>0).astype(np.uint8,copy=False)
        packed=np.packbits(bits,bitorder='little').tobytes()
        h.update(packed)
        nbytes+=len(packed)
    return nbytes,h.hexdigest()

def validate_r1(root:Path,artifact_digest:str)->dict:
    if artifact_digest!=R1_ARTIFACT_DIGEST:
        raise AssertionError('R1 artifact digest argument mismatch')
    summary_path=one(root,'exp073r1_desy1_hosted_wholestream_v0_8_summary.json')
    if sha_file(summary_path)!=R1_SUMMARY_SHA:
        raise AssertionError('R1 summary SHA mismatch')
    d=json.loads(summary_path.read_text(encoding='utf-8'))
    checks={
        'status':d.get('status')==R1_PASS,
        'metacal_bytes':d.get('observed_bytes_metacal')==METACAL_BYTES==d.get('expected_bytes_metacal'),
        'metacal_sha':d.get('metacal_sha256')==METACAL_SHA==d.get('expected_metacal_sha256'),
        'mapper':d.get('mapper')=={'nside':4096,'ordering':'RING','coords':'C','lonlat':True},
        'no_science':d.get('science_gate_scored') is False and d.get('f_invalid_computed') is False and d.get('covariance_read') is False and d.get('G8_read') is False,
    }
    for i,m in SOURCE.items():
        pr=d.get('pixel_records',{}).get(str(i),{})
        mk=d.get('masks',{}).get(str(i),{})
        checks[f'source_{i}']=(
            int(d.get('selected_rows_per_bin',{}).get(str(i),-1))==m['selected']
            and int(pr.get('file_bytes',-1))==m['bytes']
            and pr.get('sha256')==m['record_sha']
            and int(mk.get('unique_pixels',-1))==m['unique']
            and mk.get('sha256')==m['occupancy_sha']
            and int(mk.get('nside',-1))==NSIDE
            and mk.get('ordering')=='RING'
        )
    if not all(checks.values()):
        raise AssertionError(f'R1 authority mismatch {checks}')
    return {'summary_path':str(summary_path),'summary_sha256':R1_SUMMARY_SHA,'checks':checks}

def source_count_map(root:Path,bin_index:int)->tuple[np.ndarray,dict]:
    m=SOURCE[bin_index]
    p=one(root,f'exp073r1_v05_bin{bin_index}_pixel_indices_le_u32.bin')
    if p.stat().st_size!=m['bytes'] or sha_file(p)!=m['record_sha']:
        raise AssertionError(f'S{bin_index} pixel-record authority mismatch')
    pix=np.memmap(p,mode='r',dtype='<u4',shape=(m['selected'],))
    if int(np.max(pix))>=NPIX:
        raise AssertionError(f'S{bin_index} pixel outside NSIDE')
    counts=np.zeros(NPIX,dtype=np.float64)
    chunk=1_000_000
    for lo in range(0,m['selected'],chunk):
        hi=min(m['selected'],lo+chunk)
        np.add.at(counts,np.asarray(pix[lo:hi],dtype=np.int64),1.0)
    del pix
    if float(counts.sum(dtype=np.float64))!=float(m['selected']):
        raise AssertionError(f'S{bin_index} count total mismatch')
    unique=int(np.count_nonzero(counts))
    if unique!=m['unique']:
        raise AssertionError(f'S{bin_index} unique-pixel mismatch {unique}')
    nbytes,occ=occupancy_sha_from_counts(counts)
    if nbytes!=(NPIX+7)//8 or occ!=m['occupancy_sha']:
        raise AssertionError(f'S{bin_index} occupancy SHA mismatch')
    return counts,{
        'bin':bin_index,'selected_rows':m['selected'],'pixel_record_bytes':m['bytes'],
        'pixel_record_sha256':m['record_sha'],'unique_pixels':unique,
        'binary_occupancy_bytes':nbytes,'binary_occupancy_sha256':occ,
        'dense_count_map':canonical_hash(counts)
    }

def lens_mask(path:Path)->tuple[np.ndarray,dict]:
    if path.stat().st_size!=LENS_BYTES or sha_file(path)!=LENS_SHA:
        raise AssertionError('lens public-file authority mismatch')
    m=np.asarray(hp.read_map(path,field=0,dtype=np.float64,nest=False),dtype=np.float64)
    if m.shape!=(NPIX,):
        raise AssertionError(f'lens mask shape mismatch {m.shape}')
    m[m==hp.UNSEEN]=0.0
    if not np.all(np.isfinite(m)):
        raise AssertionError('lens nonfinite after UNSEEN handling')
    m[m<=0.5]=0.0
    if not np.any(m>0):
        raise AssertionError('lens mask empty after >0.5 rule')
    return m,{
        'public_file_bytes':LENS_BYTES,'public_file_sha256':LENS_SHA,
        'threshold_rule':'retain original weight iff mask>0.5',
        'positive_pixels_after_threshold':int(np.count_nonzero(m>0)),
        'sum_weights':float(np.sum(m,dtype=np.float64)),
        'dense_mask':canonical_hash(m)
    }

def parse_task(task:str)->tuple[str,list[int]]:
    if task not in ALL_TASKS:
        raise AssertionError(f'unknown task {task}')
    parts=task.split('_')
    if parts[0]=='Wm':
        return 'Wm',[int(parts[1][1:])]
    i=int(parts[1][1:]); j=int(parts[2][1:])
    if i>j:
        raise AssertionError('WW task must be unordered i<=j')
    return 'WW',[i,j]

def compute_window(kind:str,maps:list[np.ndarray])->tuple[np.ndarray,dict]:
    b=nmt.NmtBin.from_edges(BAND_EDGES[:-1],BAND_EDGES[1:])
    if b.get_n_bands()!=39:
        raise AssertionError('band count mismatch')
    w=nmt.NmtWorkspace()
    if kind=='Wm':
        lens,src=maps
        f0=nmt.NmtField(lens,None,spin=0)
        f2=nmt.NmtField(src,None,spin=2)
        w.compute_coupling_matrix(f0,f2,b)
        wins=np.asarray(w.get_bandpower_windows(),dtype=np.float64)
        expected=(2,39,2,LMAX_PLUS_ONE)
        selected_semantics={'output':'TE','input':'TE','full_component_order':['TE','TB']}
        if wins.shape!=expected:
            raise AssertionError(f'Wm full window shape {wins.shape} != {expected}')
    else:
        a,bmap=maps
        fa=nmt.NmtField(a,None,spin=2)
        if bmap is a:
            fb=fa
        else:
            fb=nmt.NmtField(bmap,None,spin=2)
        w.compute_coupling_matrix(fa,fb,b)
        wins=np.asarray(w.get_bandpower_windows(),dtype=np.float64)
        expected=(4,39,4,LMAX_PLUS_ONE)
        selected_semantics={'output':'EE','input':'EE','full_component_order':['EE','EB','BE','BB']}
        if wins.shape!=expected:
            raise AssertionError(f'WW full window shape {wins.shape} != {expected}')
    selected=np.ascontiguousarray(wins[0,:,0,:],dtype='<f8')
    if selected.shape!=(39,LMAX_PLUS_ONE) or not np.all(np.isfinite(selected)):
        raise AssertionError('selected window invalid')
    norms=np.sum(np.abs(selected),axis=1,dtype=np.float64)
    if not np.all(np.isfinite(norms)) or not np.all(norms>0):
        raise AssertionError('selected absolute-response normalization invalid')
    meta={
        'full_window_shape':list(wins.shape),
        'selected_window_shape':list(selected.shape),
        'selected_component':selected_semantics,
        'absolute_response_norms':[float(x) for x in norms],
        'selected_window_authority':canonical_hash(selected)
    }
    del wins,w
    gc.collect()
    return selected,meta

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--task',required=True)
    ap.add_argument('--r1-root',required=True)
    ap.add_argument('--r1-artifact-digest',required=True)
    ap.add_argument('--lens-mask')
    ap.add_argument('--output-json',required=True)
    ap.add_argument('--output-npz',required=True)
    a=ap.parse_args()

    version=importlib.metadata.version('pymaster')
    if not (version=='2.7' or version.startswith('2.7.')):
        raise AssertionError(f'expected PyMaster 2.7 lineage, got {version}')
    kind,bins=parse_task(a.task)
    root=Path(a.r1_root)
    r1=validate_r1(root,a.r1_artifact_digest)

    source_maps=[]
    source_meta=[]
    for i in sorted(set(bins)):
        m,meta=source_count_map(root,i)
        source_maps.append((i,m))
        source_meta.append(meta)
    src_by_bin={i:m for i,m in source_maps}

    lens_meta=None
    if kind=='Wm':
        if not a.lens_mask:
            raise AssertionError('Wm requires --lens-mask')
        lens,lens_meta=lens_mask(Path(a.lens_mask))
        maps=[lens,src_by_bin[bins[0]]]
    else:
        if a.lens_mask:
            raise AssertionError('WW must not receive/read lens mask')
        maps=[src_by_bin[bins[0]],src_by_bin[bins[1]]]

    window,wmeta=compute_window(kind,maps)

    result={
        'experiment':'Exp073AA','status':PASS,'task':a.task,'kind':kind,
        'pymaster_version':version,'nside':NSIDE,'npix':NPIX,
        'ell_axis':{'first':0,'last':LMAX_PLUS_ONE-1,'count':LMAX_PLUS_ONE},
        'bandpower_edges':BAND_EDGES.tolist(),'bandpower_count':39,
        'r1_authority':{
            'run':33270843577,'job':99148916507,
            'head_sha':'ef783ca941fb9b9b5f5eae537986c56ff06e6536',
            'artifact_id':9720335366,'artifact_digest':R1_ARTIFACT_DIGEST,
            'summary_sha256':R1_SUMMARY_SHA,'checks':r1['checks']
        },
        'source_masks':source_meta,'lens_mask':lens_meta,'workspace':wmeta,
        'radial_kernel_read':False,'physical_k_computed':False,
        'physical_support_evaluated':False,'retained_coordinates_evaluated':False,
        'fiducial_P_weighting_used':False,'science_gate_scored':False,
        'covariance_read':False,'nuisance_geometry_read':False,
        'relation_null_read':False,'G8_read':False,
        'article3_scientific_readiness_percent':52,'gate_state':GATES
    }
    oj=Path(a.output_json); oj.parent.mkdir(parents=True,exist_ok=True)
    oj.write_text(json.dumps(result,indent=2,sort_keys=True,allow_nan=False)+'\n',encoding='utf-8')
    on=Path(a.output_npz); on.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(on,window=window)
    print(PASS,a.task,wmeta['selected_window_authority']['sha256'])

if __name__=='__main__':
    main()
