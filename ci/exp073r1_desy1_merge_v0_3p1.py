#!/usr/bin/env python3
"""Provenance correction wrapper for Exp073R1 merge v0.3.

The mapper/merge semantics are unchanged. This wrapper replaces the obsolete
transcription-only source-object SHA256 constant with the authoritative value
recorded by Exp073P2 after its 2026-08-28 provenance correction.
"""
from __future__ import annotations

import exp073r1_desy1_merge_v0_3 as impl

OBSOLETE_TRANSCRIPTION = '491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd'
AUTHORITATIVE_SOURCE = '491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5'


def main() -> None:
    assert impl.EXPECTED_SOURCE == OBSOLETE_TRANSCRIPTION, (
        'base implementation changed; audit provenance patch before reuse',
        impl.EXPECTED_SOURCE,
    )
    impl.EXPECTED_SOURCE = AUTHORITATIVE_SOURCE
    impl.main()


if __name__ == '__main__':
    main()
