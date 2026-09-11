#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

CLASS_COMMIT = "ac627d54e9ce196a08878d1ba33999819925d19c"
OLD = "perhaps_print_variables = perturb_print_variables;"
NEW = "perhaps_print_variables = NULL;"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    if len(sys.argv) not in (2, 3):
        raise SystemExit("usage: classiv_k_output_history_suppression_patch_v0_1.py CLASS_ROOT [receipt.json]")
    root = Path(sys.argv[1])
    p = root / "source" / "perturbations.c"
    raw = p.read_bytes()
    text = raw.decode()
    if text.count(OLD) != 1:
        raise SystemExit(f"expected exactly one history callback assignment, found {text.count(OLD)}")
    # Fail closed on the two invariants that must remain present in the pinned source.
    if "tmp_k_list[index_newk] = ppt->k_output_values[index_k_output];" not in text:
        raise SystemExit("k_output_values insertion invariant missing")
    if "ppt->index_k_output_values[index_mode*ppt->k_output_values_num+index_k_output]=index_newk;" not in text:
        raise SystemExit("k_output_values index invariant missing")
    pre = sha(raw)
    patched = text.replace(OLD, NEW, 1)
    p.write_text(patched)
    post_raw = p.read_bytes()
    if post_raw.decode().count(OLD) != 0 or post_raw.decode().count(NEW) < 2:
        # One NULL assignment already exists as initialization; after patch there must be at least two.
        raise SystemExit("history callback suppression postcondition failed")
    receipt = {
        "schema": "CLASSIV_K_OUTPUT_HISTORY_SUPPRESSION_PATCH_RECEIPT_V0_1",
        "source_commit": CLASS_COMMIT,
        "path": "source/perturbations.c",
        "old_assignment": OLD,
        "new_assignment": NEW,
        "replacement_count": 1,
        "pre_sha256": pre,
        "post_sha256": sha(post_raw),
        "k_output_values_still_inserted_into_solver_grid": True,
        "perturbation_history_callback_suppressed": True,
        "scientific_parameters_changed": False,
        "token": "CLASSIV_K_OUTPUT_HISTORY_SUPPRESSION_PATCH_APPLIED_EXACTLY_ONCE",
    }
    if len(sys.argv) == 3:
        out = Path(sys.argv[2]); out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(receipt["token"])
    print(json.dumps(receipt, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
