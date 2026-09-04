#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import exp073bu_wm_s3_fresh_ab_production_v0_4 as prior

SCHEMA = 'dsir.exp073bu.wm_s3.fresh_ab_production.v0.5'
EXPECTED_CUMULATIVE = {'lens': 1, 'source': 1}
ZERO_INVOCATION = {'lens': 0, 'source': 0}


def _exact_counts(value, expected):
    return (
        isinstance(value, dict)
        and set(value) == {'lens', 'source'}
        and type(value.get('lens')) is int
        and type(value.get('source')) is int
        and value == expected
    )


def _verify_restored_mask_lineage(root: Path, replica: str, source_head: str, contract_fingerprint: str):
    st = prior.base.load_manifest(root, 'fresh_masks_complete', replica, source_head, contract_fingerprint)
    if st is None:
        raise RuntimeError('fail-closed missing masks checkpoint for workspace lineage resume')
    payloads = st.get('payloads')
    if not isinstance(payloads, dict) or not _exact_counts(payloads.get('reconstruction_counts'), EXPECTED_CUMULATIVE):
        raise RuntimeError('fail-closed masks cumulative reconstruction lineage mismatch')
    lp = root / 'lens_mask.npy'
    sp = root / 's3_mask.npy'
    if not lp.is_file() or not sp.is_file():
        raise RuntimeError('fail-closed restored mask payload missing')
    lm = payloads.get('lens_mask') or {}
    sm = payloads.get('s3_mask') or {}
    lens = prior.np.load(lp, mmap_mode='r', allow_pickle=False)
    source = prior.np.load(sp, mmap_mode='r', allow_pickle=False)
    try:
        if prior.base.canonical_f8_sha(lens) != lm.get('canonical_sha256'):
            raise RuntimeError('fail-closed restored lens mask SHA mismatch')
        if prior.base.canonical_f8_sha(source) != sm.get('canonical_sha256'):
            raise RuntimeError('fail-closed restored S3 mask SHA mismatch')
    finally:
        del lens, source
    return dict(EXPECTED_CUMULATIVE)


def _preserving_stage_manifest(root: Path, stage: str, replica: str, source_head: str, contract_fingerprint: str, payloads: dict):
    existing = prior.base.load_manifest(root, stage, replica, source_head, contract_fingerprint)
    if existing is not None:
        return existing
    out = dict(payloads)
    if stage == 'fresh_workspace_mcm_complete':
        counts = out.get('reconstruction_counts')
        if _exact_counts(counts, ZERO_INVOCATION):
            _verify_restored_mask_lineage(root, replica, source_head, contract_fingerprint)
            out['reconstruction_counts'] = dict(EXPECTED_CUMULATIVE)
        elif not _exact_counts(counts, EXPECTED_CUMULATIVE):
            raise RuntimeError('fail-closed new workspace reconstruction lineage mismatch')
    return prior._ORIGINAL_STAGE_MANIFEST(root, stage, replica, source_head, contract_fingerprint, out)


# Replace only the prospective manifest writer used by the already audited
# boundary-safe v0.4 resume logic. Existing valid manifests remain read-only.
prior._preserving_stage_manifest = _preserving_stage_manifest
prior.SCHEMA = SCHEMA


def main():
    prior.main()


if __name__ == '__main__':
    main()
