# Exp073CQ precompute diagnostic durability addendum

Date: 2026-09-03
Status: LIVE GOVERNANCE / CONTROL AUDIT FINDING; +0/+0

Companion to `recovery/2026-09-03_exp073cq_diagnostic_coverage_static_audit_gap.md`. Frozen Exp073CQ run `33742582807` is not modified.

## Additional finding

The Exp073CQ Python driver catches non-compute command exceptions in `main()` and calls:

`diagnostic(root, a.cmd, e)`

without `branch` or `sync_script`. The diagnostic writer therefore creates local `diagnostics/first_failure.json` and prints the JSON, but does not attempt successor-namespace durability for these precompute Python failures.

Affected Python-command paths include `init`, `import-parent`, and `validate` (and a Python finalization exception before the separate workflow push).

The workflow's `actions/upload-artifact@v4` step runs with `if: always()`, but its path is only `data/derived/g7/exp073cq_*.json`. A diagnostic is copied into that directory only inside the `Frozen final classification` step. If an earlier import/validate/helper step fails, final classification is skipped and the local checkpoint diagnostic is not copied into the always-uploaded artifact path.

Therefore a precompute Python exception may be visible only in the transient runner filesystem and console log. Historical `BlobNotFound` experience means console log availability must not be treated as durable diagnostic authority.

## Distinction from compute-path behavior

The numerical `compute` exception handler is stronger:

`diagnostic(root, 'compute', e, branch, sync_script, admitted)`

so it attempts a best-effort durable successor checkpoint push labelled `diagnostic-first-failure`. This addendum does not criticize that compute-path mechanism.

## Successor repair requirement

Any future version should make diagnostic durability uniform across ALL stages:

- diagnostic writer receives successor branch/sync binding for `init/import/validate/materialization/finalize` failures whenever a valid successor contract exists;
- shell-level failures are trapped and routed into the same canonical schema;
- `actions/upload-artifact@v4 if: always()` directly includes the checkpoint diagnostic path or a dedicated copied diagnostic staging path independent of final classification;
- static audit simulates or proves every failure route rather than checking only for diagnostic-related strings.

If current CQ completes through these precompute steps successfully, this latent durability gap was not exercised; the finding remains governance QA `+0/+0`. If a vulnerable path fails, absence of a durable canonical diagnostic must be classified as control/infrastructure incompleteness, not filled by inference.
