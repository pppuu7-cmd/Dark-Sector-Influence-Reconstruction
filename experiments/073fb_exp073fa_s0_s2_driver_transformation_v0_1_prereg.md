# Exp073FB — Exp073FA S0_S2 driver transformation audit v0.1

Date: 2026-09-06. DSIR only.

Purpose: before any Exp073FA self-hosted science execution, prove fail-closed that the already validated Exp073EY durable A/B architecture can be transformed prospectively to the frozen ordered `(S0,S2)` pair without changing arithmetic, geometry, public BPW extraction, checkpoint order, exactness policy, or storage semantics.

Frozen inputs:
- Exp073FA science prereg blob `edc044792be8ac7b796c8469943924942ae91932`;
- Exp073EY durable base driver blob `1db1eabbdba492c476cc61d3c4d71147aa688384`;
- Exp073EY file-backed public-read wrapper blob `066847006b2ed9d712d2c22d3576a0d8887fa7bf`;
- task-runner blob `050ed7dd3387c4fb031f877825e6b3f4d4ce3ef2`;
- qualified read-patch blob `d534b698f9131688d263eedcef27260386c58641`.

Allowed semantic substitutions in the durable base driver are only:
1. experiment identity `exp073ey` -> `exp073fa` and `EXP073EY` -> `EXP073FA`;
2. checkpoint/cache pair label `ww-s0-s1` -> `ww-s0-s2` where present;
3. source-1 local semantic labels `s1`/`S1` -> `s2`/`S2` only in the source-pair provenance context;
4. the second authoritative source reconstruction call index `1` -> `2`;
5. ordered provenance indices `[0,1]` -> `[0,2]`;
6. candidate PASS/FAIL token pair identity `WW_S0_S1` -> `WW_S0_S2`.

No numerical constants for NSIDE, ell, band edges, shapes, dtype, public BPW indexing, MCM byte count, source head, contract fingerprint, SHA algorithm, exact equality, checkpoint order, finiteness, or tolerance policy may change. No S0_S1 numerical artifact is an input.

The public-read wrapper may change only experiment/base-driver identity so it imports the generated Exp073FA base driver; its storage/mmap/public-BPW logic must otherwise be byte-equivalent after normalizing that identity.

Hosted audit must generate candidate driver files, parse/compile them, assert authoritative source indices exactly `{0,2}`, ordered pair `[0,2]`, source pair `S0->S2`, dedicated Exp073FA namespaces, exact token, unchanged shapes and checkpoint stage order, absence of tolerance-rescue calls, and normalized equivalence of all non-pair scientific logic to the frozen Exp073EY inputs.

PASS token: `PASS_EXP073FB_EXP073FA_S0_S2_DRIVER_TRANSFORMATION_STATIC_AUDIT_V0_1`.
Classification: support/governance `+0/+0`; no WW authority is created and no self-hosted science may start merely from this PASS.