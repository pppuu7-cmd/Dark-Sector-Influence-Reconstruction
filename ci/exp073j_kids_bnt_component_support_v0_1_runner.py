#!/usr/bin/env python3
"""Execution shim for the prospectively frozen Exp073J KiDS-BNT evaluator.

The first implementation commit had a purely array-orientation bug in the
chunked Hankel multiplication.  No support output had been evaluated.  Keep
the frozen evaluator and replace only that numerical helper here so the
scientific contract remains immutable and the implementation correction is
explicitly auditable.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import numpy as np
from scipy.special import jv

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "ci" / "exp073j_kids_bnt_component_support_v0_1.py"
spec = importlib.util.spec_from_file_location("exp073j_base", SRC)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)

if not hasattr(np, "trapz"):
    np.trapz = np.trapezoid


def response_on_grid(ell: np.ndarray, th, tp, tm, tn, chunk=512):
    rg = np.empty((8, ell.size)); rs = np.empty((8, ell.size))
    for a in range(0, ell.size, chunk):
        e = ell[a:a+chunk]
        x = e[:, None] * th[None, :]
        pref = e[:, None] / (2 * np.pi)
        rg[:, a:a+len(e)] = (((pref * jv(2, x)) @ tn.T).T)
        rs[:, a:a+len(e)] = ((((pref * jv(0, x)) @ tp.T) + ((pref * jv(4, x)) @ tm.T)).T)
    return rg, rs

base.response_on_grid = response_on_grid
base.main()
