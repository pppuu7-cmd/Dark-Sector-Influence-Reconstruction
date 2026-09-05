#!/usr/bin/env python3
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit('usage: exp073dl_evidence_guard_static_test_v0_1.py WORKFLOW')
s = Path(sys.argv[1]).read_text()
job_marker = '\n  export-terminal-canonical-payloads:\n'
job = s.find(job_marker)
if job < 0:
    raise SystemExit('FAIL_EXP073DL_EXPORT_JOB_MISSING')
bind_marker = '      - name: Bind prospective evidence-only contract'
step_marker = '      - name: Lock, live noncompetition, and immutable payload export'
bind_start = s.find(bind_marker, job)
step = s.find(step_marker, job)
if bind_start < 0 or step < 0 or bind_start >= step:
    raise SystemExit('FAIL_EXP073DL_EXPORT_OR_BIND_STEP_MISSING')

markers = [
    'exec 9>"$lock"',
    'flock -n 9',
    'root="$CHECKPOINT_ROOT"',
    'test -d "$root"',
    '"$NMT_PY" - <<\'PY\'',
    "root=Path(os.environ['CHECKPOINT_ROOT'])",
]
pos = []
for marker in markers:
    i = s.find(marker, step)
    if i < 0:
        raise SystemExit('FAIL_EXP073DL_STATIC_MARKER_MISSING:' + marker)
    pos.append(i)
if pos != sorted(pos) or len(set(pos)) != len(pos):
    raise SystemExit('FAIL_EXP073DL_LOCK_SCOPE_ORDER')

bind = s[bind_start:step]
required_bind = (
    'NMT_PY=$HOME/.cache/dsir-nmt27/bin/python',
    'test -x "$HOME/.cache/dsir-nmt27/bin/python"',
)
if not all(x in bind for x in required_bind):
    raise SystemExit('FAIL_EXP073DL_FROZEN_PYTHON_BINDING_MISSING')
forbidden_prelock = (
    'test -d "$CHECKPOINT_ROOT"',
    "Path(os.environ['CHECKPOINT_ROOT'])",
    'selected_te.bin',
    'terminal_science_receipt_resume_v0_1.json',
)
if any(x in bind for x in forbidden_prelock):
    raise SystemExit('FAIL_EXP073DL_PRELOCK_ROOT_ACCESS')

body = s[step:]
forbidden_science = (
    'import pymaster',
    'compute_coupling_matrix(',
    'get_bandpower_windows(',
    'couple_cell(',
    'decouple_cell(',
    'conda install',
    'pip install',
)
if any(x in body for x in forbidden_science):
    raise SystemExit('FAIL_EXP073DL_SCIENCE_OR_DEPENDENCY_RECOMPUTE_PRESENT')

print('PASS_EXP073DL_HOSTED_STATIC_AUDIT_V0_1')
