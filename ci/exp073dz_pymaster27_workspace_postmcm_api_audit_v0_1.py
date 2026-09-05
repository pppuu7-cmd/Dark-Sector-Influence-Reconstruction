#!/usr/bin/env python3
from __future__ import annotations
import importlib.metadata, json, tempfile
from pathlib import Path
import numpy as np
import pymaster as nmt

TOKEN='COMPLETE_EXP073DZ_PYMASTER27_WORKSPACE_POSTMCM_API_AUDIT_V0_1'

def masks(nside):
    p=np.arange(12*nside*nside,dtype=np.int64)
    a=(((p*17+3)%101)<61).astype(float); a*=1+(((p*13+5)%7)/7.0)
    b=(((p*29+11)%103)<57).astype(float); b*=1+(((p*19+2)%11)/11.0)
    return a,b

def desc(obj,name):
    if not hasattr(obj,name): return {'present':False}
    v=getattr(obj,name)
    r={'present':True,'type':type(v).__name__}
    try: r['shape']=list(np.asarray(v).shape)
    except Exception: pass
    return r

def main():
    ver=importlib.metadata.version('pymaster')
    if not (ver=='2.7' or ver.startswith('2.7.')): raise RuntimeError('PyMaster 2.7 required')
    nside=16
    edges=np.asarray([0,6,12,18,24,30,36,42,48],dtype=np.int32)
    s0,s1=masks(nside)
    f0=nmt.NmtField(s0,None,spin=2); f1=nmt.NmtField(s1,None,spin=2)
    bins=nmt.NmtBin.from_edges(edges[:-1],edges[1:])
    w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f1,bins)
    with tempfile.TemporaryDirectory() as td:
        fp=Path(td)/'w01.fits'; w.write_to(str(fp))
        wr=nmt.NmtWorkspace(); wr.read_from(str(fp))
        bpw=wr.get_bandpower_windows(); mcm=wr.get_coupling_matrix()
        candidates=['mcm_binned','mcm','norm_type','wawb','beam1','beam2','ncls','lmax','lmax_fields','bin']
        out={
          'experiment':'Exp073DZ','classification':'DIAGNOSTIC_COMPLETE +0/+0','science_gate_scored':False,'ww_authority_created':False,
          'pymaster_version':ver,
          'public':{'bandpower_windows_shape':list(np.asarray(bpw).shape),'coupling_matrix_shape':list(np.asarray(mcm).shape),'workspace_has_bpws':hasattr(wr,'bpws'),'bin_has__bin_mcm':hasattr(bins,'_bin_mcm')},
          'workspace_attrs':{k:desc(wr,k) for k in candidates},
          'wsp_attrs':{k:desc(wr.wsp,k) for k in candidates},
          'no_tolerance_rescue':True
        }
        Path('exp073dz_api_audit.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
        print(TOKEN); print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()
