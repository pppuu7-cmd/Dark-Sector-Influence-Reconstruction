#!/usr/bin/env python3
from __future__ import annotations
import argparse,gc,hashlib,importlib.metadata,json,os,stat
from pathlib import Path
import numpy as np
import pymaster as nmt
EXPECTED=294912
ER_FULL='bf656c5f0493dc44d6c42b31b804f04f6893b7fc4895e92b99cefc356b10b884'
ER_EE='336a0b57fe734a2f17a4a0844db1a18fc43887abf7556fb63009ee4a3de5f607'
EDGES=np.asarray([0,6,12,18,24,30,36,42,48],dtype=np.int32)

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def sha(x): return hashlib.sha256(memoryview(canon(x)).cast('B')).hexdigest()
def masks(n=16):
 p=np.arange(12*n*n,dtype=np.int64)
 a=(((p*17+3)%101)<61).astype(float); a*=1+(((p*13+5)%7)/7.0)
 b=(((p*29+11)%103)<57).astype(float); b*=1+(((p*19+2)%11)/11.0)
 return canon(a),canon(b)
def proof(d:Path):
 rp=str(d.resolve()); files=[]
 for p in sorted(d.glob('dsir-nmt-mcm-*')):
  s=p.stat(); files.append({'path':str(p.resolve()),'size':int(s.st_size),'regular':stat.S_ISREG(s.st_mode)})
 maps=[]
 try: maps=[x for x in Path('/proc/self/maps').read_text(errors='replace').splitlines() if 'dsir-nmt-mcm-' in x and rp in x]
 except OSError: pass
 return {'valid':len(files)==1 and files[0]['regular'] and files[0]['size']==EXPECTED and len(maps)>=1,'files':files,'maps':maps,'expected_bytes':EXPECTED}
def cleanup(d:Path|None): return True if d is None else not any(d.glob('dsir-nmt-mcm-*'))
def save(out:Path,prefix:str,mcm,bpw,ee):
 np.save(out/f'{prefix}_mcm.npy',canon(mcm),allow_pickle=False); np.save(out/f'{prefix}_bpw.npy',canon(bpw),allow_pickle=False); np.save(out/f'{prefix}_ee.npy',canon(ee),allow_pickle=False)
 return {'mcm_sha256':sha(mcm),'bpw_sha256':sha(bpw),'ee_sha256':sha(ee),'mcm_shape':list(mcm.shape),'bpw_shape':list(bpw.shape),'ee_shape':list(ee.shape)}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--mode',choices=['stock','patched'],required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--mmap-dir'); a=ap.parse_args()
 out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True); md=Path(a.mmap_dir) if a.mmap_dir else None
 v=importlib.metadata.version('pymaster'); assert v=='2.7' or v.startswith('2.7.')
 if a.mode=='patched':
  assert os.environ.get('DSIR_NMT_FILEBACKED_MCM')=='1' and md is not None; md.mkdir(parents=True,exist_ok=True); assert Path(os.environ['DSIR_NMT_MMAP_DIR']).resolve()==md.resolve(); assert cleanup(md)
 else: assert os.environ.get('DSIR_NMT_FILEBACKED_MCM')!='1'
 s0,s1=masks(); assert not np.array_equal(s0,s1)
 f0=nmt.NmtField(s0,None,spin=2,lmax=47,lmax_mask=47); f1=nmt.NmtField(s1,None,spin=2,lmax=47,lmax_mask=47); b=nmt.NmtBin.from_edges(EDGES[:-1],EDGES[1:])
 w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f1,b)
 p_construct=proof(md) if md else {'valid':False,'files':[],'maps':[],'expected_bytes':EXPECTED}
 if a.mode=='patched' and not p_construct['valid']: raise RuntimeError('construction mmap proof failed: '+repr(p_construct))
 mcm=canon(w.get_coupling_matrix()); bpw=canon(w.get_bandpower_windows()); ee=canon(bpw[0,:,0,:]); assert mcm.shape==(192,192) and bpw.shape==(4,8,4,48) and ee.shape==(8,48); assert all(np.all(np.isfinite(x)) for x in (mcm,bpw,ee))
 construction=save(out,'construction',mcm,bpw,ee); fp=out/'workspace.fits'; w.write_to(str(fp))
 del w,mcm,bpw,ee,f0,f1,s0,s1; gc.collect(); construct_cleanup=cleanup(md)
 if a.mode=='patched' and not construct_cleanup: raise RuntimeError('construction mmap cleanup failed')
 wr=nmt.NmtWorkspace(); wr.read_from(str(fp),read_unbinned_MCM=True)
 p_read=proof(md) if md else {'valid':False,'files':[],'maps':[],'expected_bytes':EXPECTED}
 if a.mode=='patched' and not p_read['valid']: raise RuntimeError('read mmap proof failed: '+repr(p_read))
 rmcm=canon(wr.get_coupling_matrix()); rbpw=canon(wr.get_bandpower_windows()); ree=canon(rbpw[0,:,0,:]); assert rmcm.shape==(192,192) and rbpw.shape==(4,8,4,48) and ree.shape==(8,48); assert all(np.all(np.isfinite(x)) for x in (rmcm,rbpw,ree))
 reload=save(out,'reload',rmcm,rbpw,ree)
 del wr,rmcm,rbpw,ree; gc.collect(); read_cleanup=cleanup(md)
 if a.mode=='patched' and not read_cleanup: raise RuntimeError('read mmap cleanup failed')
 rec={'experiment':'Exp073EW','mode':a.mode,'pymaster_version':v,'distinct_masks':True,'expected_mcm_bytes':EXPECTED,'construction':construction,'reload':reload,'construction_mmap_proof':p_construct,'read_mmap_proof':p_read,'construction_cleanup_complete':construct_cleanup,'read_cleanup_complete':read_cleanup,'er_expected_reload_full':ER_FULL,'er_expected_reload_ee':ER_EE,'no_tolerance_rescue':True}
 (out/'route_receipt.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(json.dumps(rec,indent=2,sort_keys=True))
if __name__=='__main__': main()
