#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import healpy as hp
import numpy as np
NROWS=136_930_995; NSIDE=4096; NPIX=hp.nside2npix(NSIDE)
PASS='PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1'
P2='PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2'
EXPECTED_SOURCE='491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd'; EXPECTED_METACAL='39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8'
def sha(p):
 h=hashlib.sha256();
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''): h.update(b)
 return h.hexdigest()
def mask_from_record(record,scratch,out):
 c=np.memmap(scratch,mode='w+',dtype=np.uint32,shape=(NPIX,)); c[:]=0; selected=0
 with record.open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''):
   if len(b)%4: raise AssertionError('unaligned record')
   p=np.frombuffer(b,dtype='<u4').astype(np.int64,copy=False)
   if p.size:
    if int(p.max())>=NPIX: raise AssertionError('pixel range')
    u,n=np.unique(p,return_counts=True); c[u]+=n.astype(np.uint32); selected+=int(p.size)
 c.flush(); h=hashlib.sha256(); unique=0; nbytes=0; out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('wb') as f:
  for lo in range(0,NPIX,8_388_608):
   bits=np.asarray(c[lo:min(NPIX,lo+8_388_608)]>0,dtype=np.uint8); unique+=int(bits.sum()); q=np.packbits(bits,bitorder='little').tobytes(); f.write(q); h.update(q); nbytes+=len(q)
 del c; scratch.unlink(missing_ok=True); return selected,unique,nbytes,h.hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); ap.add_argument('--checksum-record',required=True); a=ap.parse_args(); root=Path(a.root); out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True)
 txt=Path(a.checksum_record).read_text(); assert P2 in txt and EXPECTED_SOURCE in txt and EXPECTED_METACAL in txt
 dirs=sorted([p for p in root.iterdir() if p.is_dir() and (p/'shard.json').exists()],key=lambda p:json.loads((p/'shard.json').read_text())['shard']); assert len(dirs)==8
 rs=[json.loads((p/'shard.json').read_text()) for p in dirs]; assert [r['shard'] for r in rs]==list(range(8)); assert all(r['nshards']==8 and r['science_gate_scored'] is False and r['f_invalid_computed'] is False and r['covariance_read'] is False and r['G8_read'] is False for r in rs)
 assert rs[0]['row_lo']==0 and rs[-1]['row_hi_exclusive']==NROWS
 for x,y in zip(rs,rs[1:]): assert x['row_hi_exclusive']==y['row_lo']
 assert sum(r['rows'] for r in rs)==NROWS and all(r['rows']==r['row_hi_exclusive']-r['row_lo'] for r in rs)
 recdir=out.parent/'exp073r1_records'; maskdir=out.parent/'exp073r1_masks'; recdir.mkdir(exist_ok=True); maskdir.mkdir(exist_ok=True)
 records={}; masks={}; repeat={}
 for b in range(4):
  dst=recdir/f'exp073r1_bin{b}_pixel_indices_le_u32.bin'; h=hashlib.sha256(); total=0
  with dst.open('wb') as w:
   for d,r in zip(dirs,rs):
    src=d/r['records'][str(b)]['file']; assert src.stat().st_size==r['records'][str(b)]['bytes'] and sha(src)==r['records'][str(b)]['sha256']
    with src.open('rb') as f:
     for q in iter(lambda:f.read(8<<20),b''): w.write(q); h.update(q); total+=len(q)
  selected=sum(r['selected_rows_per_bin'][str(b)] for r in rs); assert total==selected*4
  mp=maskdir/f'exp073r1_desy1_source_bin{b}_mask_ring_nside4096_bitpack_little.bin'; s,u,n,dig=mask_from_record(dst,out.parent/f'.count{b}.u32',mp); assert s==selected
  records[str(b)]={'path':str(dst),'serialization':'little-endian uint32 HEALPix RING pixel index sequence in selected row order','selected_rows':selected,'file_bytes':total,'sha256':h.hexdigest()}; masks[str(b)]={'path':str(mp),'nside':NSIDE,'ordering':'RING','selected_rows':selected,'unique_pixels':u,'file_bytes':n,'sha256':dig}
  rp=out.parent/f'.repeat{b}.bin'; s2,u2,n2,d2=mask_from_record(dst,out.parent/f'.repeatcount{b}.u32',rp); rp.unlink(missing_ok=True); repeat[str(b)]={'matches_selected_rows':s2==s,'matches_unique_pixels':u2==u,'matches_mask_sha256':d2==dig}
 assert all(all(v.values()) for v in repeat.values())
 result={'experiment':'Exp073R1','implementation':'v0.2 sharded transport/merge equivalent to frozen v0.1 mapper','status':PASS,'rows_read_source':NROWS,'rows_read_metacal':NROWS,'input_identity_binding':{'checksum_record':a.checksum_record,'source_sha256':EXPECTED_SOURCE,'metacal_sha256':EXPECTED_METACAL,'checksum_status':P2},'shard_coverage':[{'shard':r['shard'],'row_lo':r['row_lo'],'row_hi_exclusive':r['row_hi_exclusive'],'source_data_range_sha256':r['source_data_range_sha256'],'metacal_data_range_sha256':r['metacal_data_range_sha256']} for r in rs],'selection':rs[0]['selection'],'mapper':rs[0]['mapper'],'selected_rows_per_bin':{str(b):records[str(b)]['selected_rows'] for b in range(4)},'pixel_records':records,'masks':masks,'repeatability_from_merged_records':repeat,'science_gate_scored':False,'f_invalid_computed':False,'covariance_read':False,'G8_read':False,'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}}
 out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':PASS,'selected':result['selected_rows_per_bin'],'unique':{b:masks[b]['unique_pixels'] for b in masks}},sort_keys=True))
if __name__=='__main__': main()
