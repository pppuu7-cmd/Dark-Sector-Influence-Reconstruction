#!/usr/bin/env python3
from pathlib import Path
import re, sys

INCLUDE_ANCHOR = '#include "perturbations.h"\n'
INCLUDE_BLOCK = (
    '#ifdef DSIR_C2_PRETRANSFORM_HOOK\n'
    '#include "dsir_c2_pretransform_hook.h"\n'
    '#endif\n'
)
CALL_BLOCK = (
    '#ifdef DSIR_C2_PRETRANSFORM_HOOK\n'
    '  dsir_c2_pretransform_observe(\n'
    '      tau,\n'
    '      k,\n'
    '      a,\n'
    '      ppw->pvecback[pba->index_bg_H],\n'
    '      ppw->delta_m,\n'
    '      ppw->theta_m,\n'
    '      ppw->pvecback[pba->index_bg_rho_idm_iv],\n'
    '      ppw->pvecback[pba->index_bg_rho_iv]);\n'
    '#endif\n'
)
CALL_RE = re.compile(
    r'(?P<stmt>class_call\(\s*perturb_total_stress_energy\s*\(\s*ppr\s*,\s*pba\s*,\s*pth\s*,\s*ppt\s*,\s*index_md\s*,\s*k\s*,\s*y\s*,\s*ppw\s*\)\s*,.*?\);)',
    re.S,
)


def transform(text: str) -> str:
    if text.count(INCLUDE_ANCHOR) != 1:
        raise SystemExit('FAIL include anchor multiplicity')
    matches = list(CALL_RE.finditer(text))
    if len(matches) != 1:
        raise SystemExit(f'FAIL helper class_call multiplicity {len(matches)}')
    if 'DSIR_C2_PRETRANSFORM_HOOK' in text or 'dsir_c2_pretransform_observe' in text:
        raise SystemExit('FAIL source already contains DSIR hook identity')
    text = text.replace(INCLUDE_ANCHOR, INCLUDE_ANCHOR + INCLUDE_BLOCK, 1)
    matches = list(CALL_RE.finditer(text))
    m = matches[0]
    text = text[:m.end()] + '\n' + CALL_BLOCK + text[m.end():]
    return text


def main():
    if len(sys.argv) != 3:
        raise SystemExit('usage: apply_exp073gm_c2_pretransform_hook.py <input perturbations.c> <output perturbations.c>')
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    dst.write_text(transform(src.read_text(encoding='utf-8')), encoding='utf-8')

if __name__ == '__main__':
    main()
