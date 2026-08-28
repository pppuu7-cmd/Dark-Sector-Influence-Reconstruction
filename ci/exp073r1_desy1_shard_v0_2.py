#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess, tempfile, time
from pathlib import Path
import healpy as hp
import numpy as np

NROWS=136_930_995; NSIDE=4096; NPIX=hp.nside2npix(NSIDE); CHUNK=262_144
SOURCE={'total_bytes':2738626560,'data_start':5760,'row_bytes':20,'sha256':'491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd'}
METACAL={'total_bytes':84075649920,'data_start':17280,'row_bytes':614,'sha256':'39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8'}

def fetch(url,start,size,total):
    end=start+size-1; expected=f'bytes {start}-{end}/{total}'; last=None
    for a in range(5):
        try:
            with tempfile.TemporaryDirectory() as td:
                b=Path(td)/'b'; h=Path(td)/'h'
                subprocess.run(['curl','--fail','--silent','--show-error','--location','--http1.1','--retry','4','--retry-all-errors','--connect-timeout','30','--max-time','600','--header','Accept-Encoding: identity','--header','User-Agent: DSIR-Exp073R1-shard/0.2','--range',f'{start}-{end}','--dump-header',str(h),'--output',str(b),url],check=True,timeout=630)
                raw=b.read_bytes(); cr=[x.split(':',1)[1].strip() for x in h.read_text(errors='replace').splitlines() if x.lower().startswith('content-range:')]
                if not cr or cr[-1]!=expected or len(raw)!=size: raise RuntimeError((cr[-1] if cr else None,len(raw),expected,size))
                return raw
        except Exception as e:
            last=e
            if a<4: time.sleep(min(5*(a+1),20))
    raise RuntimeError(f'range transport exhausted: {last}')

def sdecode(raw):
    return np.frombuffer(raw,dtype=np.dtype({'names':['z'],'formats':['>i2'],'offsets':[10],'itemsize':20}))
def mdecode(raw):
    return np.frombuffer(raw,dtype=np.dtype({'names':['ra','dec','flags'],'formats':['>f8','>f8','>i4'],'offsets':[566,574,594],'itemsize':614}))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-url',required=True); ap.add_argument('--metacal-url',required=True); ap.add_argument('--shard',type=int,required=True); ap.add_argument('--nshards',type=int,default=8); ap.add_argument('--outdir',required=True); a=ap.parse_args()
    assert 0<=a.shard<a.nshards
    lo=(NROWS*a.shard)//a.nshards; hi=(NROWS*(a.shard+1))//a.nshards
    out=Path(a.outdir); out.mkdir(parents=True,exist_ok=True)
    files=[out/f'bin{b}.u32' for b in range(4)]; fh=[p.open('wb') for p in files]; hh=[hashlib.sha256() for _ in range(4)]
    hs=hashlib.sha256(); hm=hashlib.sha256(); sel=[0]*4; finite=nonfinite=badpix=0; rows=0
    try:
        row=lo
        while row<hi:
            nr=min(CHUNK,hi-row)
            sb=fetch(a.source_url,SOURCE['data_start']+row*SOURCE['row_bytes'],nr*SOURCE['row_bytes'],SOURCE['total_bytes'])
            mb=fetch(a.metacal_url,METACAL['data_start']+row*METACAL['row_bytes'],nr*METACAL['row_bytes'],METACAL['total_bytes'])
            hs.update(sb); hm.update(mb); s=sdecode(sb); m=mdecode(mb); assert len(s)==nr==len(m)
            z=np.asarray(s['z']); ra=np.asarray(m['ra']); dec=np.asarray(m['dec']); flags=np.asarray(m['flags'])
            fin=np.isfinite(ra)&np.isfinite(dec); finite+=int(fin.sum()); nonfinite+=int((~fin).sum()); base=(dec>=-90)&(dec<=-35)&(flags==0)
            for b in range(4):
                q=base&(z==b)
                if np.any(q&~fin): raise AssertionError(f'nonfinite selected coords bin {b}')
                if not np.any(q): continue
                pix=hp.ang2pix(NSIDE,ra[q],dec[q],lonlat=True).astype(np.int64,copy=False); bad=(pix<0)|(pix>=NPIX); badpix+=int(bad.sum())
                if np.any(bad): raise AssertionError('out-of-range HEALPix index')
                raw=np.asarray(pix,dtype='<u4').tobytes(); fh[b].write(raw); hh[b].update(raw); sel[b]+=int(pix.size)
            row+=nr; rows+=nr
            if rows%(CHUNK*16)==0 or row==hi: print(json.dumps({'shard':a.shard,'row':row,'hi':hi,'selected':sel}),flush=True)
    finally:
        for f in fh: f.close()
    rec={'experiment':'Exp073R1S','implementation':'deterministic disjoint transport shard; NON-SCIENCE','shard':a.shard,'nshards':a.nshards,'row_lo':lo,'row_hi_exclusive':hi,'rows':rows,'selection':'zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0','mapper':{'nside':NSIDE,'ordering':'RING','coords':'C','lonlat':True},'selected_rows_per_bin':{str(i):sel[i] for i in range(4)},'finite_ra_dec_rows':finite,'nonfinite_ra_dec_rows':nonfinite,'out_of_range_pixel_count':badpix,'source_data_range_sha256':hs.hexdigest(),'metacal_data_range_sha256':hm.hexdigest(),'records':{str(i):{'file':files[i].name,'bytes':files[i].stat().st_size,'sha256':hh[i].hexdigest()} for i in range(4)},'science_gate_scored':False,'f_invalid_computed':False,'covariance_read':False,'G8_read':False,'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}}
    assert rows==hi-lo and badpix==0
    (out/'shard.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
