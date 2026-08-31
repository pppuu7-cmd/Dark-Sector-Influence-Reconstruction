# DSIR recovery — Exp073BV Q1 exact source lineage terminal

**Date:** 2026-08-31  
**Scope:** DSIR only.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

## Preserved authority

- Exp073BJ run `33379013167` remains terminal Track-A exact Wm_S1 authority PASS; final authority artifact `9758841785` remains authoritative.
- Exp073AQ remains the permanent hosted exact-repeatability scientific FAIL.
- Exp073BD remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`; it cannot be preferred or used downstream.
- Exp073BV is provenance/source-lineage only and carries `+0/+0`.

## Exp073BV immutable result

Hosted run: `33420824723`  
Job: `99582473539`  
Head: `6010f094782a277017cbf0bb2a9af63331bb3282`  
Artifact: `9768866582`  
Artifact digest: `sha256:33f013a8c7c06ce2f5f68e62a324b80f2b1911ff2a3cd3ff89a6af4add179cc5`

Preregistered terminal label:

`BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED`

The immutable receipt established all Q1 predicates:

- installed `pymaster` version is exactly `2.7`;
- top-level `_nmtlib` imports and resolves to `/home/runner/work/_temp/nmt27/lib/python3.11/site-packages/_nmtlib.cpython-311-x86_64-linux-gnu.so`;
- `pymaster.nmtlib` imports successfully;
- `pymaster.nmtlib._nmtlib` is the same loaded extension object;
- official upstream source HEAD is exactly `24365fa59a38c15732f4f37e8b29265b75c442d5` (NaMaster v2.7);
- all preregistered source-topology predicates pass;
- installed `pymaster/nmtlib.py` and exact upstream-v2.7 `pymaster/nmtlib.py` are byte-for-byte identical;
- both wrapper SHA256 values are `3c82b229231debf224b1e2206e6e7490d1e274b1d7df3803a17f2ce3fb3a4c6d`;
- runtime symbol-table probes find `drc3jj` in the loaded `_nmtlib` binary, including a global function symbol.

This does not itself validate any extracted/streaming implementation and cannot authorize Wm_S2/WW.

## Exact upstream general-coupling algorithm identified

At exact upstream v2.7 commit `24365fa59a38c15732f4f37e8b29265b75c442d5`:

`pymaster.get_general_coupling_matrix(...)` calls SWIG `comp_general_coupling_matrix(...)`, which zeroes the output and calls `nmt_compute_general_coupling_matrix(...)`.

The exact C implementation in `src/nmt_master.c`:

1. sets `nls=lmax+1` and `lstart=max(s1,s2)`;
2. computes each thread-local `wl_mask[l] = pcl_mask[l]*(2*l+1)/(4*M_PI)`;
3. for each `(ll2,ll3)` from `lstart..lmax`, calls runtime `drc3jj(ll2,ll3,n1,-s1,...)` and, unless `(s1,n1)==(s2,n2)`, a second `drc3jj(ll2,ll3,n2,-s2,...)`;
4. accumulates in increasing `l1` exactly `xi += wl_mask[l1]*wsn1*wsn2` for `abs(ll2-ll3) <= l1 <= min(ll2+ll3,lmax)`;
5. multiplies the completed element by `(2*ll3+1.0)`.

The DSIR low-memory AZ path then row-compresses a full general matrix in increasing `ell` order using `compress_general` and, for Wm, calls `(s1,s2,n1,n2)=(0,2,0,2)`; WW uses `(2,2,2,2)` and `(2,-2,2,-2)`.

Therefore a prospectively frozen C streaming helper can preserve the exact stock element operation order while avoiding materialization of the full `[12288,12288]` matrix by accumulating completed rows directly into the same band-compression order. This must still pass a separate exact numerical-equivalence QA before any Track-A use.

## Exact next gate

Prospectively preregister a small/medium numerical-equivalence QA covering all three scientific spin signatures. It must compare:

1. full helper matrix vs stock `pymaster.get_general_coupling_matrix` with `numpy.array_equal` and canonical `<f8` SHA equality;
2. streaming-compressed helper output vs stock full-matrix output passed through the frozen DSIR `compress_general`, again exact array/SHA equality;
3. one-thread vs two-thread helper outputs exactly.

No tolerance or result-driven rescue is allowed. Any mismatch is preserved under a preregistered mismatch label. This QA is `+0/+0` and cannot itself authorize Wm_S2/WW.

Required G7 order and all Article-3 support boundaries remain unchanged. **No G8 jump.**
