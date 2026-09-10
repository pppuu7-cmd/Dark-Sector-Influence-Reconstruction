#!/usr/bin/env python3
from pathlib import Path
import sys

root=Path(sys.argv[1]) if len(sys.argv)>1 else Path('external/class_iv')
p=root/'source/perturbations.c'
s=p.read_text()

source_anchor='''      if (ppt->has_density_transfers == _TRUE_) {\n        ppt->has_lss = _TRUE_;\n        ppt->has_source_delta_tot = _TRUE_;\n'''
source_repl='''      if (ppt->has_density_transfers == _TRUE_) {\n        ppt->has_lss = _TRUE_;\n        ppt->has_source_delta_m = _TRUE_;\n        ppt->has_source_delta_tot = _TRUE_;\n'''
title_anchor='''      class_store_columntitle(titles,"d_scf",pba->has_scf);\n      class_store_columntitle(titles,"d_tot",_TRUE_);\n'''
title_repl='''      class_store_columntitle(titles,"d_scf",pba->has_scf);\n      class_store_columntitle(titles,"d_m",ppt->has_source_delta_m);\n      class_store_columntitle(titles,"d_tot",_TRUE_);\n'''
data_anchor='''          class_store_double(dataptr,tk[ppt->index_tp_delta_scf],ppt->has_source_delta_scf,storeidx);\n          class_store_double(dataptr,tk[ppt->index_tp_delta_tot],ppt->has_source_delta_tot,storeidx);\n'''
data_repl='''          class_store_double(dataptr,tk[ppt->index_tp_delta_scf],ppt->has_source_delta_scf,storeidx);\n          class_store_double(dataptr,tk[ppt->index_tp_delta_m],ppt->has_source_delta_m,storeidx);\n          class_store_double(dataptr,tk[ppt->index_tp_delta_tot],ppt->has_source_delta_tot,storeidx);\n'''
for name,a,b in [('source',source_anchor,source_repl),('title',title_anchor,title_repl),('data',data_anchor,data_repl)]:
    if s.count(a)!=1:
        raise SystemExit(f'FAIL_{name.upper()}_ANCHOR_COUNT={s.count(a)}')
    if b in s:
        raise SystemExit(f'FAIL_{name.upper()}_ALREADY_PATCHED')
    s=s.replace(a,b,1)

required='_set_source_(ppt->index_tp_delta_m) = ppw->delta_m;'
if s.count(required)!=1:
    raise SystemExit(f'FAIL_DM_INTERNAL_SOURCE_COUNT={s.count(required)}')
if s.count('class_store_columntitle(titles,"d_m",ppt->has_source_delta_m);')!=1:
    raise SystemExit('FAIL_DM_TITLE_COUNT')
if s.count('class_store_double(dataptr,tk[ppt->index_tp_delta_m],ppt->has_source_delta_m,storeidx);')!=1:
    raise SystemExit('FAIL_DM_DATA_COUNT')
if s.count('class_store_columntitle(titles,"d_tot",_TRUE_);')!=1:
    raise SystemExit('FAIL_DTOT_TITLE_PRESERVATION')
if s.count('class_store_double(dataptr,tk[ppt->index_tp_delta_tot],ppt->has_source_delta_tot,storeidx);')!=1:
    raise SystemExit('FAIL_DTOT_DATA_PRESERVATION')
p.write_text(s)
print('EXP073IU_DM_PUBLIC_EXPOSURE_PATCH_APPLIED_EXACTLY_ONCE')
