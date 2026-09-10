# Recovered Exp073JL — corrected resource-layout audit v0.2

Date: 2026-09-11. Scope: DSIR Article III implementation/resource preparation only. Effect `+0/+0`. This supersedes the historical-construction-count statement in v0.1; no scientific gate changes.

## Correction: original full traversal constructed 16 CLASS instances, not 12

Post-JW full source audit of `ci/exp073ir_article3_real_layerb_common_response_v0_1.py` shows four separate `ResponseSuite` lifetimes in the inherited traversal:

1. production/coarse DES-2001 suite, then close;
2. production/coarse BOSS GL64 suite, then close;
3. dense/fine DES-2001 plus BOSS GL64 suite, then close;
4. dense/fine BOSS GL128 suite, then close.

The inherited common-grid `ResolutionSuite.__init__` constructs four CLASS objects and retains all four simultaneously until `close()`. Therefore the historical Exp073JL v0.1 execution shape was **4 suite lifetimes × 4 CLASS = 16 CLASS constructions total, with up to 4 simultaneously live**.

The earlier v0.1 audit incorrectly merged the first two production/coarse suite lifetimes when counting constructions and stated 12. That statement is superseded by this v0.2 correction. The scientific traversal semantics described there remain unchanged.

## Recovered execution remains exactly 8 constructions / max one live

The independently verified response-blind request plan proves that the four inherited suite call streams can be merged without changing call identity:

- coarse: 377 DES calls + 64 BOSS GL64 calls = 441 calls per role;
- fine: 377 DES calls + 64 BOSS GL64 + 128 BOSS GL128 = 569 calls per role;
- four roles on each lattice -> exactly 8 CLASS constructions and 4040 transfer calls total;
- fine GL128 remains fine-only and is used solely for the inherited dense-z status control.

Exp073JW independently demonstrated the exact eight-build/max-one-live lifecycle using the canonical grids. The recovered Exp073JL v0.2 helper may therefore merge request phases **inside each role lifetime** while replaying the original four-suite call boundaries back through Exp073IR for identical row accounting.

## Correct compact storage bound from audited response-blind plan

The verified flattened request plan is much smaller than the conservative rectangular estimate in v0.1:

- coarse raw scalar count per role: 83,666; four `<f8` role buffers = 2,677,312 bytes;
- fine raw scalar count per role: 121,682; four `<f8` role buffers = 3,893,824 bytes.

Thus process-local raw finite-difference operand storage is only a few MiB when stored on the exact union-target plan. No compression, quantization, averaging, downsampling, changed precision, changed masks or altered arithmetic is needed.

The inherited Exp073IR replay may still create its historical coarse-response memmap for accounting/comparison; that is execution scratch, not additional live CLASS state and does not change scientific atoms.

## Authority boundary

This correction is process-history/resource authority only. It does not change `REL_TOL=1e-3`, `h=1e-4`, native kpd20, canonical 2049/4097 grids, centered-cubic interpolation, physical domain, 107-row traversal, GL64/GL128 semantics, Layer-B accounting, covariance status or Wm_S3 status. Article III repository readiness remains 68% and funnel-freeze readiness remains 67% until recovered JL returns an independently verified terminal scientific-support classification.
