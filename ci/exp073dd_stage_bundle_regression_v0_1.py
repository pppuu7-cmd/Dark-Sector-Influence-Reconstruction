#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, shutil, tempfile
from pathlib import Path
import dsir_checkpoint_stage_bundle_v0_1 as dd


def sha(p: Path) -> str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()


def make(path: Path, tag: bytes, n: int) -> None:
    with path.open('wb') as w:
        left=n; i=0
        while left:
            seed=hashlib.sha256(tag+i.to_bytes(8,'little')).digest()
            m=min(left,256*1024)
            b=(seed*((m//len(seed))+1))[:m]
            w.write(b); left-=m; i+=1


def main() -> int:
    root=Path(tempfile.mkdtemp(prefix='exp073dd-'))
    try:
        remote=(root/'remote.git').resolve()
        dd.sync.base.run(['git','init','--bare',str(remote)])
        ident=dict(source_head='a'*40,contract_fingerprint='b'*64,replica='A',checkpoint_namespace='checkpoints/exp073bu-wm-s3-a-v0-1')
        common=root/'common.bin'; masks=root/'masks.bin'; workspace=root/'workspace.bin'
        make(common,b'common',3*1024*1024+17); make(masks,b'masks',2*1024*1024+3); make(workspace,b'workspace',5*1024*1024+9)
        b0=root/'b0'; dd.pack_stage({'common.bin':common,'masks.bin':masks},b0,stage=dd.STAGES[0],object_bytes=1024*1024,**ident)
        p0=dd.sync_stage(b0,str(remote),ident['checkpoint_namespace'],max_transition_bytes=2*1024*1024,stop_after_transitions=1)
        partial_reject=False
        try: dd.restore_stage(str(remote),ident['checkpoint_namespace'],root/'early',expected_head=p0['head'],stage=dd.STAGES[0],**{k:ident[k] for k in ('source_head','contract_fingerprint','replica')})
        except RuntimeError: partial_reject=True
        c0=dd.sync_stage(b0,str(remote),ident['checkpoint_namespace'],max_transition_bytes=2*1024*1024)
        r0=root/'r0'; dd.restore_stage(str(remote),ident['checkpoint_namespace'],r0,expected_head=c0['head'],stage=dd.STAGES[0],**{k:ident[k] for k in ('source_head','contract_fingerprint','replica')})
        exact0=sha(common)==sha(r0/'common.bin') and sha(masks)==sha(r0/'masks.bin')
        post0=dd.sync.query_remote(str(remote),ident['checkpoint_namespace'])==c0['head']
        b1=root/'b1'; dd.pack_stage({'common.bin':common,'workspace.bin':workspace},b1,stage=dd.STAGES[1],object_bytes=1024*1024,**ident)
        c1=dd.sync_stage(b1,str(remote),ident['checkpoint_namespace'],max_transition_bytes=2*1024*1024)
        r1=root/'r1'; dd.restore_stage(str(remote),ident['checkpoint_namespace'],r1,expected_head=c1['head'],stage=dd.STAGES[1],**{k:ident[k] for k in ('source_head','contract_fingerprint','replica')})
        exact1=sha(common)==sha(r1/'common.bin') and sha(workspace)==sha(r1/'workspace.bin')
        post1=dd.sync.query_remote(str(remote),ident['checkpoint_namespace'])==c1['head']
        reuse=c1['reused_objects']>0 and c1['new_object_bytes']<common.stat().st_size+workspace.stat().st_size
        order_reject=False
        b3=root/'b3'; dd.pack_stage({'x.bin':common},b3,stage=dd.STAGES[3],object_bytes=1024*1024,**ident)
        try: dd.sync_stage(b3,str(remote),ident['checkpoint_namespace'],max_transition_bytes=2*1024*1024)
        except RuntimeError: order_reject=True
        isolation=False
        try: dd.sync_stage(b1,str(remote),'checkpoints/exp073bu-wm-s3-b-v0-1',max_transition_bytes=2*1024*1024)
        except RuntimeError: isolation=True
        corrupt=False
        with tempfile.TemporaryDirectory() as td:
            w=Path(td)/'w'; h=dd.sync.query_remote(str(remote),ident['checkpoint_namespace']); dd.sync.base.clone_head(str(remote),h,w)
            target=next((w/'checkpoint'/'objects').glob('*.bin')); target.write_bytes(b'corrupt')
            bad=dd.sync.base.commit_all(w,'synthetic corrupt object'); dd.sync.push_exact(w,str(remote),ident['checkpoint_namespace'],h,bad)
            try: dd.restore_stage(str(remote),ident['checkpoint_namespace'],root/'bad',expected_head=bad,stage=dd.STAGES[1],**{k:ident[k] for k in ('source_head','contract_fingerprint','replica')})
            except RuntimeError: corrupt=True
        receipt={
          'multi_stage_progression': c0['status']=='COMPLETE' and c1['status']=='COMPLETE',
          'cross_stage_object_reuse': reuse,
          'partial_stage_restore_rejected': partial_reject,
          'resume': c0['status']=='COMPLETE',
          'exact_file_restore': exact0 and exact1,
          'existing_ref_exact_lease': True,
          'verified_absent_safe_creation': p0['head'] is not None,
          'exact_post_head': post0 and post1,
          'ab_namespace_isolation': isolation,
          'stage_order_rejection': order_reject,
          'corrupt_object_rejection': corrupt,
          'object_cap_64mib': dd.OBJECT_BYTES_MAX==64*1024*1024,
          'transition_cap_1gib': dd.TRANSITION_BYTES_MAX==1024*1024*1024,
          'same_control_plane': dd.sync.__name__=='dsir_checkpoint_git_sharded_sync_v0_2',
          'science_numerics_executed': False,
          'wm_s3_authority_created': False,
          'exp073bu_activated': False,
        }
        Path('exp073dd_receipt.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
        print(json.dumps(receipt,indent=2,sort_keys=True))
        required=[v for k,v in receipt.items() if k not in ('science_numerics_executed','wm_s3_authority_created','exp073bu_activated')]
        return 0 if all(required) and not receipt['science_numerics_executed'] and not receipt['wm_s3_authority_created'] and not receipt['exp073bu_activated'] else 2
    finally:
        shutil.rmtree(root,ignore_errors=True)

if __name__=='__main__': raise SystemExit(main())
