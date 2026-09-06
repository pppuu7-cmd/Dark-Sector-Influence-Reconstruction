#!/usr/bin/env python3
from __future__ import annotations
import importlib.util
from pathlib import Path

BASE = Path(__file__).with_name('exp073eo_ww_s0_s0_provenance_admission_v0_1.py')
spec = importlib.util.spec_from_file_location('exp073eo_v01', BASE)
if spec is None or spec.loader is None:
    raise RuntimeError('cannot load frozen Exp073EO v0.1 auditor')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

# Prospective v0.2 erratum: canonicalize only the frozen hosted Exp073EM artifact
# identifier representation. The authoritative value remains exactly 9977333691.
mod.EM_ID = '9977333691'
mod.PASS_EO = 'PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_2'
mod.BLOCK_EO = 'BLOCKED_EXP073EO_PROVENANCE_ADMISSION_V0_2'
mod.main()
