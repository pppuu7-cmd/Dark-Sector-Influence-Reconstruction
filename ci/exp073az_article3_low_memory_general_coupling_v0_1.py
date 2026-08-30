#!/usr/bin/env python3
from __future__ import annotations
import argparse, gc, hashlib, importlib.metadata, json
from pathlib import Path
import numpy as np
import healpy as hp
import pymaster as nmt

NSIDE=4096
NPIX=12*NSIDE*NSIDE
L=3*NSIDE
EDGES=np.array([0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288],dtype=np.int64)
R1_ARTIFACT_DIGEST='sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd'
R1_SUMMARY_SHA='100458e046088b24cba671db1852112676e487331d5c1f5c5cb55f8a9e011df4'
R1_PASS='PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1'
METACAL_BYTES=84_075_649_920
METACAL_SHA='39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8'
LENS_BYTES=104_595_840
LENS_SHA='a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55'
SOURCE={
0:{'selected':7_705_486,'bytes':30_821_944,'record_sha':'5b507215ca961c09b82786e61e681a0178c29e9b593c17b588e366722a021f15','unique':4_305_774,'occupancy_sha':'b6ed74f31540d4041267f94e2f7cdb70b7040d943ba22a4aa7eab62418f8cb32'},
1:{'selected':7_851_711,'bytes':31_406_844,'record_sha':'752f585125e413c7bd40cc5174cf7ef98e95f970022a351c5d91206f371d2241','unique':4_339_193,'occupancy_sha':'fed1ffdf2ef7a7ae88e42615bd08e207e039239c44fa20b7994258f147a739f1'},
2:{'selected':8_238_547,'bytes':32_954_188,'record_sha':'259295a1f5a23ad9e5c6b46842bcf612b0eb13dc701ab6d54eb15f0d7bb0105f','unique':4_401_919,'occupancy_sha':'9e2bfb92289ca4a3abb11efabf7ac8d59bb7c68eb63a7104c2b247267733b24d'},
3:{'selected':4_196_641,'bytes':16_786_564,'record_sha':'3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec','unique':2_943_132,'occupancy_sha':'21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094'}}
ALL=['Wm_S0','Wm_S1','Wm_S2','Wm_S3','WW_S0_S0','WW_S0_S1','WW_S0_S2','WW_S0_S3','WW_S1_S1','WW_S1_S2','WW_S1_S3','WW_S2_S2','WW_S2_S3','WW_S3_S3']

def sha_file(p:Path,chunk=8<<20):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(chunk),b''): h.update(b)
 return h.hexdigest()
def chash(a):
 x=np.ascontiguousarray(a,dtype='<f8'); return hashlib.sha256(x.tobytes()).hexdigest()
def one(root:Path,name:str):
 hits=list(root.rglob(name))
 if len(hits)!=1: raise AssertionError((name,len(hits)))
 return hits[0]
def parse_task(task):
 if task not in ALL: raise AssertionError(task)
 p=task.split('_')
 if p[0]=='Wm': return 'Wm',[int(p[1][1:])]
 return 'WW',[int(p[1][1:]),int(p[2][1:])]
def occ_sha(counts):
 h=hashlib.sha256(); block=8_388_608
 for lo in range(0,counts.size,block):
  bits=(counts[lo:min(counts.size,lo+block)]>0).astype(np.uint8,copy=False)
  h.update(np.packbits(bits,bitorder='little').tobytes())
 return h.hexdigest()
def validate_r1(root:Path,digest):
 if digest!=R1_ARTIFACT_DIGEST: raise AssertionError('digest')
 s=one(root,'exp073r1_desy1_hosted_wholestream_v0_8_summary.json')
 if sha_file(s)!=R1_SUMMARY_SHA: raise AssertionError('summary sha')
 d=json.loads(s.read_text())
 if d.get('status')!=R1_PASS or d.get('observed_bytes_metacal')!=METACAL_BYTES or d.get('metacal_sha256')!=METACAL_SHA: raise AssertionError('r1 summary')
def source_map(root:Path,i:int):
 m=SOURCE[i]; p=one(root,f'exp073r1_v05_bin{i}_pixel_indices_le_u32.bin')
 if p.stat().st_size!=m['bytes'] or sha_file(p)!=m['record_sha']: raise AssertionError('record')
 pix=np.memmap(p,mode='r',dtype='<u4',shape=(m['selected'],)); x=np.zeros(NPIX,dtype=np.float64)
 for lo in range(0,m['selected'],1_000_000): np.add.at(x,np.asarray(pix[lo:min(m['selected'],lo+1_000_000)],dtype=np.int64),1.0)
 del pix
 if int(np.count_nonzero(x))!=m['unique'] or occ_sha(x)!=m['occupancy_sha']: raise AssertionError('occupancy')
 return x
def lens_map(path:Path):
 if path.stat().st_size!=LENS_BYTES or sha_file(path)!=LENS_SHA: raise AssertionError('lens authority')
 x=np.asarray(hp.read_map(path,field=0,dtype=np.float64,nest=False),dtype=np.float64); x[x==hp.UNSEEN]=0; x[x<=0.5]=0
 return x

def task_pcl(task,root,lens=None):
 kind,bins=parse_task(task); validate_r1(root,R1_ARTIFACT_DIGEST)
 if kind=='Wm':
  a=lens_map(Path(lens)); b=source_map(root,bins[0]); fa=nmt.NmtField(a,None,spin=0); fb=nmt.NmtField(b,None,spin=2)
  aa=fa.get_mask_alms(); ab=fb.get_mask_alms(); pcl=hp.alm2cl(aa,ab,lmax=fa.ainfo_mask.lmax)
 else:
  a=source_map(root,bins[0]); fa=nmt.NmtField(a,None,spin=2)
  if bins[1]==bins[0]:
   aa=fa.get_mask_alms(); pcl=hp.alm2cl(aa,aa,lmax=fa.ainfo_mask.lmax)-fa.Nw
  else:
   b=source_map(root,bins[1]); fb=nmt.NmtField(b,None,spin=2); aa=fa.get_mask_alms(); ab=fb.get_mask_alms(); pcl=hp.alm2cl(aa,ab,lmax=fa.ainfo_mask.lmax)
 pcl=np.ascontiguousarray(pcl,dtype='<f8')
 if pcl.shape!=(L,) or not np.all(np.isfinite(pcl)): raise AssertionError('pcl')
 return pcl

def compress_general(G,edges=EDGES):
 l=G.shape[1]; A=np.empty((len(edges)-1,l),dtype=np.float64)
 for ib,(lo,hi) in enumerate(zip(edges[:-1],edges[1:])):
  acc=np.zeros(l,dtype=np.float64)
  for ell in range(int(lo),int(hi)): acc += G[ell]
  A[ib]=acc/float(hi-lo)
 return np.ascontiguousarray(A,dtype='<f8')
def compact_from_pcl(task,pcl):
 kind,_=parse_task(task)
 if kind=='Wm':
  G=nmt.get_general_coupling_matrix(pcl,0,2,0,2); A=compress_general(G); del G; gc.collect(); return {'A':A}
 G=nmt.get_general_coupling_matrix(pcl,2,2,2,2); As=compress_general(G); del G; gc.collect()
 G=nmt.get_general_coupling_matrix(pcl,2,-2,2,-2); Af=compress_general(G); del G; gc.collect(); return {'Asame':As,'Aflip':Af}
def k_from_a(A,edges=EDGES):
 nb=len(edges)-1; K=np.empty((nb,nb),dtype=np.float64)
 for ib,(lo,hi) in enumerate(zip(edges[:-1],edges[1:])):
  acc=np.zeros(nb,dtype=np.float64)
  for ell in range(int(lo),int(hi)): acc += A[:,ell]
  K[:,ib]=acc
 return K
def finalize(task,d):
 kind,_=parse_task(task)
 if kind=='Wm':
  A=np.asarray(d['A'],dtype=np.float64); W=np.linalg.solve(k_from_a(A),A); return np.ascontiguousarray(W,dtype='<f8')
 As=np.asarray(d['Asame'],dtype=np.float64); Af=np.asarray(d['Aflip'],dtype=np.float64)
 Ap=0.5*(As+Af); Am=0.5*(As-Af); Kp=k_from_a(Ap); Km=k_from_a(Am)
 A2=np.block([[Ap,Am],[Am,Ap]]); K2=np.block([[Kp,Km],[Km,Kp]])
 W=np.linalg.solve(K2,A2)[:39,:L]; return np.ascontiguousarray(W,dtype='<f8')

def selftest():
 nside=16; l=3*nside; edges=np.array([0,4,8,16,24,32,48]); npix=12*nside*nside; th,ph=hp.pix2ang(nside,np.arange(npix)); m=((th<2.2)&(ph>0.25)&(ph<5.7)).astype(float)
 f=nmt.NmtField(m,None,spin=2,lmax=l-1,lmax_mask=l-1); b=nmt.NmtBin.from_edges(edges[:-1],edges[1:]); w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f,f,b); ref=w.get_bandpower_windows()[0,:,0,:]
 pcl=hp.alm2cl(f.get_mask_alms(),f.get_mask_alms(),lmax=l-1)-f.Nw
 G=nmt.get_general_coupling_matrix(pcl,2,2,2,2); As=compress_general(G,edges); del G
 G=nmt.get_general_coupling_matrix(pcl,2,-2,2,-2); Af=compress_general(G,edges); del G
 def K(A): return k_from_a(A,edges)
 Ap=.5*(As+Af); Am=.5*(As-Af); W=np.linalg.solve(np.block([[K(Ap),K(Am)],[K(Am),K(Ap)]]),np.block([[Ap,Am],[Am,Ap]]))[:len(edges)-1,:l]
 maxd=float(np.max(np.abs(W-ref)))
 G1=nmt.get_general_coupling_matrix(pcl,2,2,2,2); G2=nmt.get_general_coupling_matrix(pcl,2,2,2,2)
 exact=bool(np.array_equal(G1,G2))
 return {'status':'PASS_EXP073AZ_SELFTEST_V0_1' if (maxd<1e-12 and exact) else 'FAIL_EXP073AZ_SELFTEST_V0_1','stock_reference_max_abs':maxd,'same_input_general_matrix_exact_repeat':exact}

def main():
 ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True); sp.add_parser('selftest')
 p=sp.add_parser('pcl'); p.add_argument('--task',required=True); p.add_argument('--r1-root',required=True); p.add_argument('--lens-mask'); p.add_argument('--out-npy',required=True); p.add_argument('--out-json',required=True)
 p=sp.add_parser('compact'); p.add_argument('--task',required=True); p.add_argument('--pcl-npy',required=True); p.add_argument('--out-npz',required=True); p.add_argument('--out-json',required=True)
 p=sp.add_parser('finalize'); p.add_argument('--task',required=True); p.add_argument('--compact-npz',required=True); p.add_argument('--out-npz',required=True); p.add_argument('--out-json',required=True)
 a=ap.parse_args(); ver=importlib.metadata.version('pymaster')
 if not (ver=='2.7' or ver.startswith('2.7.')): raise AssertionError(ver)
 if a.cmd=='selftest': print(json.dumps(selftest(),indent=2,sort_keys=True)); return
 if a.cmd=='pcl':
  x=task_pcl(a.task,Path(a.r1_root),a.lens_mask); np.save(a.out_npy,x,allow_pickle=False); meta={'experiment':'Exp073AZ','stage':'mask_pcl','task':a.task,'shape':list(x.shape),'sha256':chash(x),'authority_class_candidate':'low_memory_general_coupling_deterministic_v1','readiness':52,'science_gate_scored':False}; Path(a.out_json).write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n'); return
 if a.cmd=='compact':
  pcl=np.load(a.pcl_npy,allow_pickle=False); d=compact_from_pcl(a.task,pcl); np.savez(a.out_npz,**d); meta={'experiment':'Exp073AZ','stage':'compact_general_coupling','task':a.task,'arrays':{k:{'shape':list(v.shape),'sha256':chash(v)} for k,v in d.items()},'authority_class_candidate':'low_memory_general_coupling_deterministic_v1','readiness':52,'science_gate_scored':False}; Path(a.out_json).write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n'); return
 d=dict(np.load(a.compact_npz,allow_pickle=False)); w=finalize(a.task,d); np.savez(a.out_npz,window=w); meta={'experiment':'Exp073AZ','stage':'finalize','task':a.task,'window':{'shape':list(w.shape),'sha256':chash(w)},'norm_min':float(np.min(np.sum(np.abs(w),axis=1))),'authority_class_candidate':'low_memory_general_coupling_deterministic_v1','readiness':52,'science_gate_scored':False}; Path(a.out_json).write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
