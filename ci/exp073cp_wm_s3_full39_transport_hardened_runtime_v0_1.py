#!/usr/bin/env python3
"""Exp073CP bound runtime entrypoint.

Adds exact workflow/binding lineage to the immutable checkpoint contract without
changing the numerical implementation in the separately committed driver.
"""
from __future__ import annotations

import os
import exp073cp_wm_s3_full39_transport_hardened_resource_v0_1 as cp

IMPLEMENTATION_COMMIT = 'ce5e871c3824a8970f05672d03ab3c984e3813b7'
_base_contract = cp.contract


def bound_contract(source_head: str, driver_commit: str):
    d = _base_contract(source_head, driver_commit)
    d.pop('fingerprint', None)
    workflow_commit = os.environ.get('DSIR_WORKFLOW_COMMIT', '').lower()
    binding_commit = os.environ.get('DSIR_BINDING_COMMIT', '').lower()
    if len(workflow_commit) != 40 or len(binding_commit) != 40:
        raise RuntimeError('workflow/binding commit environment is not exact; fail closed')
    d['implementation_commit'] = IMPLEMENTATION_COMMIT
    d['workflow_commit'] = workflow_commit
    d['binding_commit'] = binding_commit
    d['fingerprint'] = cp.jhash(d)
    return d


cp.contract = bound_contract

if __name__ == '__main__':
    cp.main()
