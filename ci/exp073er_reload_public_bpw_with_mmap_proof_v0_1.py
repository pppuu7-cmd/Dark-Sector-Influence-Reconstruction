#!/usr/bin/env python3
from __future__ import annotations
import argparse,gc,hashlib,importlib.metadata,json,os,stat
from pathlib import Path
import numpy as np
import pymaster as nmt
EXPECTED=294912

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def sha(x): return hashlib.sha256(memoryview(canon(x)).cast('B')).hexdigest()
def proof(d:Path):
 rp=str(d.resolve()); files=[]
 for p in sorted(d.glob('dsir-nmt-mcm-*')):
  s=p.stat(); files.append({'path':str(p.resolve()),'size':int(s.st_size),'regular':stat.S_ISREG(s.st_mode)})
 maps=[]
 try:
  maps=[x for x in Path('/proc/self/maps').read_text(errors='replace').splitlines() if 'dsir-nmt-mcm-' in x and rp in x]
 except OSError: pass
 return {'valid':len(files)==1 and files[0]['regular'] and files[0]['size']==EXPECTED and len(maps)>=1,'files':files,'maps':maps,'expected_bytes':EXPECTED}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--workspace',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--mode',choices=['stock','patched'],required=True); ap.add_argument('--mmap-dir'); ap.add_argument('--label',required=True); a=ap.parse_args()
 out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True); v=importlib.metadata.version('pymaster'); assert v=='2.7' or v.startswith('2.7.')
 md=Path(a.mmap_dir) if a.mmap_dir else None
 if a.mode=='patched':
  assert os.environ.get('DSIR_NMT_FILEBACKED_MCM')=='1' and md is not None; md.mkdir(parents=True,exist_ok=True)
  assert Path(os.environ['DSIR_NMT_MMAP_DIR']).resolve()==md.resolve()
 else:
  assert os.environ.get('DSIR_NMT_FILEBACKED_MCM')!='1'
 w=nmt.NmtWorkspace(); w.read_from(a.workspace,read_unbinned_MCM=True)
 pf=proof(md) if md else {'valid':False,'files':[],'maps':[],'expected_bytes':EXPECTED}
 if a.mode=='patched' and not pf['valid']: raise RuntimeError('patched FITS-read mmap proof failed: '+repr(pf))
 bpw=canon(w.get_bandpower_windows()); ee=canon(bpw[0,:,0,:]); assert bpw.shape==(4,8,4,48) and ee.shape==(8,48); assert np.all(np.isfinite(bpw)) and np.all(np.isfinite(ee))
 np.save(out/'reload_bpw.npy',bpw,allow_pickle=False); np.save(out/'reload_ee.npy',ee,allow_pickle=False)
 rec={'label':a.label,'mode':a.mode,'pymaster_version':v,'operation':'NmtWorkspace.read_from(read_unbinned_MCM=True) -> get_bandpower_windows','full_sha256':sha(bpw),'selected_sha256':sha(ee),'full_shape':list(bpw.shape),'selected_shape':list(ee.shape),'mmap_proof':pf,'no_tolerance_rescue':True}
 del w,bpw,ee; gc.collect(); survivors=[] if md is None else [str(p) for p in md.glob('dsir-nmt-mcm-*')]; rec['mmap_cleanup_complete']=(len(survivors)==0); rec['mmap_survivors']=survivors
 if a.mode=='patched' and not rec['mmap_cleanup_complete']: raise RuntimeError('mmap survived: '+repr(survivors))
 (out/'reload_meta.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(json.dumps(rec,indent=2,sort_keys=True))
if __name__=='__main__': main()
