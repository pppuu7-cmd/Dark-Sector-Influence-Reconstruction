# Method — Exp073P split-provenance prerequisite join v0.1

**Preregistered:** 2026-08-28  
**Stage:** G7, before physical-support evaluation  
**Scientific score at this stage:** forbidden

## Purpose

Exp073P has several independently valid provenance/reproduction parents. No single existing job currently constitutes the aggregate authorization boundary for the physical-support calculation. This document freezes the semantics of that missing join before the final Exp073R1 result is known.

The join is bookkeeping/provenance only. It must not evaluate `f_invalid`, retained dimension, covariance, nuisance SVD, relation/null quantities, or any withheld G8/G9 family.

## Newly identified closure gap

The legacy public-input preflight `ci/exp073p_des_public_input_checksum_preflight_v0_1.py` uses

`MAX_DOWNLOAD_BYTES = 200 * 1024 * 1024`

and sets its local `support_evaluation_authorized` only if **all six** DES objects have `checksum_bound=true` in that same run.

Two frozen inputs alone already exceed that cap:

- `y1_source_redshift_binning_v1.fits`: `2,738,626,560` bytes;
- `mcal-y1a1-combined-riz-unblind-v4-matched.fits`: `84,075,649,920` bytes.

For an object above the cap, that implementation never enters the download/hash branch and leaves `checksum_bound=false`. Therefore the old preflight's `READY_FOR_EXP073P_SUPPORT_IMPLEMENTATION` state is structurally unreachable for the actual six-object input set. This is a provenance-architecture defect, not a physical/support failure.

The defect does **not** invalidate the independent exact bindings. Large-object checksum evidence, remaining-release checksum evidence, S0 map/n(z) reproduction, and R1 mask reproduction are intentionally produced by separate gates. What is missing is an explicit immutable join of those pieces.

## Frozen aggregate evidence set

A future aggregate join may emit a prerequisite PASS only if it binds all of the following without substitution:

1. **Cosmotheka/public-input provenance**
   - exact Cosmotheka pin `7bde066626f66cd7bbe79cc46224d2342840e463`;
   - exact public DES object names/config bindings from the Exp073P preflight;
   - parent Exp073O status `PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O`.
2. **Large DES whole-object identity**
   - source bytes `2,738,626,560`, SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
   - metacal bytes `84,075,649,920`, SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
   - provenance status `PASS_LARGE_DES_STREAMING_SHA256_BINDING_EXP073P` or a later explicitly superseding byte-equivalent gate.
3. **Remaining DES Y1 release objects**
   - exact P2 checksum-binding evidence with status `PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2`.
4. **redMaGiC mask and n(z) reproduction**
   - exact S0 status `PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0` and its immutable artifact provenance.
5. **weak-lensing mask reproduction**
   - exact final R1 status `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`;
   - all `136930995` parent rows covered exactly once by the canonical 32-shard partition;
   - exact frozen source/metacal SHA256 identities;
   - `nside=4096`, RING, celestial coordinates, `lonlat=True`;
   - four tomographic bins and deterministic independent mask reconstruction;
   - all R1 non-science flags false.
6. **BOSS fixed upstream support operator**
   - frozen Exp073J result `54/240`, cap `27/120`, with `9/40` in each P0/P2/P4 block.
7. **Frozen support-contract self-test**
   - exact physical-support constants and ordering preserved.

Canonical source/metacal range manifests are necessary parents of R1 but are **not** substitutes for final R1 PASS.

## Join output semantics

The prospective aggregate join may emit only a status such as

`PASS_EXP073P_PREREQUISITE_BINDING_V0_1`

when every required immutable parent is present and exact. Its receipt must explicitly contain:

- `support_fraction_evaluated=false`;
- `f_invalid_computed=false`;
- `retained_dimension_evaluated=false`;
- `covariance_read=false`;
- `nuisance_svd_read=false`;
- `relation_null_read=false`;
- `heldout_read=false`;
- `G8_read=false`.

Only that aggregate prerequisite PASS may make the **physical-support executor** eligible to start. Eligibility is not itself physical-support PASS.

## Frozen Exp073P physical-support contract

No criterion is changed by this architecture repair:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05`;
- minimum retained full-coordinate dimension `15`;
- classifying DES maps at `nside=4096`;
- exact Limber map `k=(ell+1/2)/chi(z)` under the pinned background;
- support uses the positive absolute final-response envelope;
- signed Wm production response remains signed;
- full radial tails outside the z rectangle remain invalid;
- no crop-before-normalization;
- no effective ell;
- no fiducial-P/model weighting;
- no post-hoc k/ell cuts;
- no covariance/SVD/relation/held-out leakage into support selection.

## Scientific interpretation

The split-provenance finding is neither evidence for nor against dark-sector physics. It is an architectural/provenance result: the previous local READY flag cannot represent the aggregate gate, so a separate immutable join is required. This prevents both false authorization and accidental loss of independently validated evidence.
