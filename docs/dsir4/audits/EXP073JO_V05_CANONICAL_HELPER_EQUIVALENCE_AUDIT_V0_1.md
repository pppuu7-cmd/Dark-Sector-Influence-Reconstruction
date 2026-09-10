# Exp073JO v0.5 canonical helper equivalence audit v0.1

Date: 2026-09-10. Scope: DSIR Article III process/support only. Effect: `+0/+0`.

Status: completed while canonical response run `34530745922` was still in progress. No v0.5 response output or shard artifact was read for this audit.

Compared:
- v0.4 helper blob `9afb076a0744dd30d4e45d4090d16ef23cc501fa`;
- v0.5 helper blob `26da8da97c91ad4adac324ebf3e40dab48524975`;
- canonical authority blob `b70ede7f8ecdf0cc67a9f20d33cafc1708eee8e8`.

Unchanged execution/science semantics:
- `H=1e-4`, `REL_TOL=1e-3`, native kpd `20`, base N4096, expected requested count 4097, capacity 4608, parser 131072, pinned CLASS-IV commit;
- model roles exactly reference `(0,0)`, alpha-minus `(-h,0)`, beta-plus `(0,+h)`, beta-minus `(0,-h)`;
- exact `pre_z=0x1.3851eb851eb85p-1`, `tail_z=0x1.1c28f5c28f5c3p+0`;
- pre targets `[0.0013,0.0047,0.013,0.041]`, tail targets `[0.0019,0.0073,0.021,0.057]` as binary64 arrays;
- exact public CLASS `d_m` extraction and physical-k unit conversion logic;
- `jj.requested_values` recovery, unchanged `jj.cubic_centered` interpolation and frozen target support;
- after-history phase evaluates pre_z then tail_z on the same CLASS instance; fresh-tail evaluates tail_z only;
- exact contiguous little-endian float64 four-value tail serialization.

The intentional execution/provenance repair is solely the node source. V0.4 called `jj.guarded_lattice(4096)` independently on every hosted runner. V0.5 instead reads the committed exact canonical `.f64` and `.hex` payloads, requires SHA256 `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb` / `98cd360d0764a884471cb09b4504b79583e2ffaea4423389ec473e98b8656c2a`, verifies bitwise hex roundtrip and monotonic/support guards, and then supplies those unchanged node bytes to the same CLASS/interpolation machinery.

No v0.4 response is reused. No response value informed canonical selection. This audit creates no scientific PASS, no covariance authority and does not open Wm_S3.
