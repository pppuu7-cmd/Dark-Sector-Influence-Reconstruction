#!/usr/bin/env python3
from pathlib import Path
import hashlib,re,subprocess,types

BASE=Path('ci/exp073fs_verify_and_prune_replica_v0_1.py')
BASE_BLOB='92bf5eaa047d97adeddad240784dcc5176c9459e'
PASS='PASS_EXP073FU_PRUNER_NAMESPACE_REPAIR_STATIC_AUDIT_V0_1'

def transformed(include_namespace_fix: bool):
    src=BASE.read_text(encoding='utf-8')
    repl=[
        ('exp073fs','exp073fu'),('EXP073FS','EXP073FU'),
        ('S1S2','S1S3'),('S1->S2','S1->S3'),('[1,2]','[1,3]'),
        ('s2_count_map','s3_count_map')]
    if include_namespace_fix:
        repl.append(('ww-s1-s2','ww-s1-s3'))
    for old,new in repl:
        if old not in src: raise RuntimeError(f'missing base token {old!r}')
        src=src.replace(old,new)
    for old,new in [('p2','p3'),('h2','h3')]: src=re.sub(rf'\b{old}\b',new,src)
    src=src.replace("'s2':1","'s3':1")
    return src

got=subprocess.check_output(['git','rev-parse','HEAD:ci/exp073fs_verify_and_prune_replica_v0_1.py'],text=True).strip()
if got!=BASE_BLOB: raise RuntimeError(f'base blob drift {got}')
old=transformed(False); new=transformed(True)
# Prove the historical v0.1 bug exactly.
for rep in ('a','b'):
    bad=f'checkpoints/exp073fu-ww-s1-s2-{rep}-v0-1'
    good=f'checkpoints/exp073fu-ww-s1-s3-{rep}-v0-1'
    if bad not in old or good in old: raise RuntimeError('historical namespace defect not reproduced')
    if good not in new or bad in new: raise RuntimeError('namespace repair not exact')
# Prove v0.2 differs from the old transformed program only by the hyphenated namespace token.
if new != old.replace('ww-s1-s2','ww-s1-s3'):
    raise RuntimeError('repair scope exceeded namespace transform')
for token in [
    "'source_pair':'S1->S3'","'ordered_source_indices':[1,3]","field_construction_count':2",
    'historical_ww_numerical_import','other_replica_output_read','mcm_backing_bytes',
    '19327352832','no_tolerance_rescue','PASS_EXP073FU_REPLICA_']:
    if token not in new: raise RuntimeError(f'frozen pruner invariant missing {token!r}')
for forbidden in ['np.allclose','np.isclose','rounding_rescue','smoothing_rescue','averaging_rescue']:
    if forbidden in new: raise RuntimeError(f'forbidden rescue token {forbidden}')
# Ensure committed v0.2 itself carries the exact additional transform and no stale namespace.
v02=Path('ci/exp073fu_verify_and_prune_replica_v0_2.py').read_text(encoding='utf-8')
for token in ["('ww-s1-s2','ww-s1-s3')",'checkpoints/exp073fu-ww-s1-s3-a-v0-1','checkpoints/exp073fu-ww-s1-s3-b-v0-1']:
    if token not in v02: raise RuntimeError(f'v0.2 repair token missing {token!r}')
print('classification=INFRASTRUCTURE_REPAIR_SUPPORT_PLUS_0_PLUS_0')
print('historical_v01_first_causal_defect=checkpoint_namespace_transform_omission')
print('repair_scope=hyphenated_checkpoint_namespace_transform_only')
print('scientific_arithmetic_changed=false')
print('acceptance_criteria_changed=false')
print('source_domain_changed=false')
print('scientific_model_authority_created=false')
print('old_transformed_sha256='+hashlib.sha256(old.encode()).hexdigest())
print('new_transformed_sha256='+hashlib.sha256(new.encode()).hexdigest())
print(PASS)
