# Exp073CV v0.3 — corrected freeze-binding preregistration

Status: PROSPECTIVE / support-integration only / +0/+0.

Exp073CV v0.1 run 33843210949 / job 100929554219 is historical I4 infrastructure failure before numerics because the whole-file forbidden-pattern verifier self-matched its own literal. Exp073CV v0.2 run 33847035743 / job 100941100858 / head 41fe6e521b69856ab6c4fd0569690b8b4dda4f09 is historical I4 infrastructure/source-binding failure before numerics because the workflow froze prereg blob `22e2b1de27fb11b48352e2ddc68248dfc5fad68d` while the committed v0.2 prereg blob is `a3635da105aed6b7e69f590577bd5e12523b142a`. No numerical stage ran and no artifact/receipt was produced.

The sole v0.3 change relative to the prospectively defined v0.2 repair is correcting the freeze binding to the actual committed prereg blob. The scoped verifier helper remains blob `640205ab9f21fd3b3ada6cb0b3a3e7c5e461f704`; frozen v0.1 production adapter remains blob `dafe86086a470c852106f0d4ecccbda1d389e397`; component identities and exact NaMaster 2.7/GSL arithmetic remain unchanged.

The scoped verifier MUST fail closed if `get_coupling_matrix` occurs inside production functions `stream_fits_to_canonical_input`, `run_downstream`, or `execute`, and then replace exactly one historical whole-file verifier defect site in a runtime copy. The hosted reference calculation is otherwise byte-for-byte inherited from v0.1.

Frozen hosted gate: the same three deterministic synthetic masks, nside=16, nl=48, edges [0,4,8,12,16,24,32,40,48], ncls=2. Every full `<f8` tensor and TE<-TE slice must satisfy SHA256 equality, `numpy.array_equal == True`, and maximum absolute difference exactly 0.0 against stock NaMaster 2.7; inherited mmap/FITS `/proc/self/maps` proof must pass.

PASS token `I1_PRODUCTION_INTERFACE_EXACT_INTEGRATION_PASS`; arithmetic mismatch I2; mmap/memory mismatch I3; infrastructure/source/verifier failure I4; malformed/missing receipt I5. Only I1 is support PASS +0/+0. It does not activate Exp073BU and creates no Wm_S3 authority. Frozen science boundaries and no-tolerance-rescue rules are unchanged.
