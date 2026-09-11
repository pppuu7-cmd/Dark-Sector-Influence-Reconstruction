# Layer-B post-16385 numerical plateau/root-cause stage V0.1

Status: prospectively frozen diagnostic plan after independently validated 8193->16385 NOT_CONVERGED. Scope: DSIR Article III only.

This stage is diagnostic/support-only and cannot authorize covariance restriction, Wm_S3, a 32769 rung, altered tolerance, altered h, altered interpolation, altered masks/domain, or any scientific PASS. It exists only to identify whether the persistent adjacent-grid discrepancy is more consistent with deterministic grid/solver structure, finite-difference cancellation sensitivity, or another reproducible numerical mechanism.

Frozen inputs: JM 4097->8193 authority; independently verified 8193->16385 terminal authority; canonical 8193 and 16385 lattices; validated 16385 cross-VM/intra-VM/noise diagnostics; pinned CAMB/CLASS-IV identities and history-suppression execution patch. No partial downstream science may be inspected to tune probes.

Permitted independent lanes, all +0/+0:
1. Fixed-node raw-operand localization: use a deterministic response-blind node selection defined only by canonical index quantiles and fixed z/domain anchors, not by observed discrepancy magnitude. Compare raw transfer operands from canonical 8193 and 16385 at identical physical requests under the frozen solver stack. No 107-row classifier is evaluated.
2. Fixed-node finite-difference cancellation audit: at the same deterministic requests, evaluate the already frozen four roles and report numerator scale, denominator scale, and conditioning indicators at h=1e-4. No alternative h values are allowed.
3. Canonical interpolation identity/control audit: independently confirm exact shared-node nesting, centered-cubic stencil identity where defined, and deterministic interpolation residual controls without changing interpolation or science.

Decision boundary: results may rank numerical mechanisms and determine what further diagnostic is justified. They may not by themselves authorize a denser scientific rung. Any future 32769 execution requires a separate prospective scientific/resource justification frozen before that execution.

Anti-duplication: do not rerun the full 8193->16385 science merely for diagnostics. Prefer small fixed-request controls. All runs must record exact commit/run/job/artifact hashes and remain +0/+0.
