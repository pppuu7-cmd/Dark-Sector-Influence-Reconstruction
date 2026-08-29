# DSIR checkpoint — Exp073R1 v0.6 attempt 1 PEP 668 incomplete

**Date:** 2026-08-29 07:15 EEST  
**Scope:** exact audit of the first execution on `DSIR-HOME-PC`; no science
classification.

## Terminal execution identity

The sole canonical v0.6 run left the queue and executed on the intended
repository-level Linux runner:

- run `33212521957`, attempt `1`;
- job `98988824629`, `metacal-map-longrun`;
- head `79abf2a9694e57e7a2ba1fbb563a0f6413e891f9`;
- workflow
  `.github/workflows/exp073r1-desy1-selfhosted-longrun-stageb-v0-6.yml`;
- runner `DSIR-HOME-PC`, group `Default`, machine `win-ws338`;
- runner version `2.336.0`;
- job interval `2026-08-29T00:07:25Z` through
  `2026-08-29T00:07:43Z`;
- terminal Actions state `completed/failure`.

This confirms that the DSIR runner registration, repository binding and
`[self-hosted, linux]` label matching are correct.  The separate RTK runner and
repository were not used.

## Exact failure boundary

The following controls passed before failure:

1. checkout of the frozen workflow head;
2. exact evaluator Git blob
   `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`;
3. evaluator Python compilation and v0.6 preregistration presence;
4. live binding of the immutable Stage-A run/artifact metadata;
5. live binding of the immutable Exp073R0 run/artifact metadata;
6. internal marker `V06_IMMUTABLE_PARENT_METADATA_PASS`.

Step 5, `Install frozen mapper runtime on long-lived runner`, failed on

`python3 -m pip install --user numpy healpy`

with pip's `externally-managed-environment` error.  The host Python follows
PEP 668 and refuses an unqualified user install unless the caller explicitly
acknowledges the distribution boundary.

Both parent-artifact downloads were skipped.  The ordinary no-Range 84 GB GET
was never opened, zero metacal rows were read, no pixel record or mask was
constructed, the terminal R1 interlock was not reached, and no artifact was
created.  The upload step itself succeeded only with a no-files warning.

## Classification

The only valid classification is

`INCOMPLETE_EXP073R1`.

It is not `FAIL_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`, not an Exp073P
support result, and not evidence for or against a dark-sector relation.  No
partial output is authoritative.  `support_executor_authorized=false`; G7,
G8 and G9 remain OPEN.

Machine-readable incident record:
`data/derived/g7/exp073r1_v06_attempt1_pep668_incomplete_v0_1.json`.

## Admissible recovery boundary

Do not edit or rerun v0.6 post hoc as if job `98988824629` had passed.  The
already-frozen aggregate join evaluator v0.1 admits that exact failed job and
therefore must remain fail-closed.

The next route must be prospectively preregistered before any replacement
output is inspected.  It may change only the execution substrate needed to
acknowledge PEP 668 for the dependency-install command.  It must retain:

- the unchanged v0.5 evaluator blob;
- the same Stage-A and Exp073R0 parents;
- the same 84 GB URL, byte count and SHA256;
- one ordinary HTTP 200 whole-object GET, with no Range/resume;
- the same rows, field offsets/types, selection and parent order;
- `nside=4096`, RING, celestial `lonlat=True` mapping;
- exact record/mask serialization and independent repeatability checks;
- every no-support/no-covariance/no-G8 firewall;
- all frozen Exp073P thresholds and downstream ordering.

## Implemented recovery update

The earlier candidate plan to use a PEP 668 override was not executed.  Commit
`5f773b3600defd5c5a2e94b8ef9489bb9ba32787` instead introduced the cleaner
isolated-venv repair, avoiding both the externally managed interpreter and any
persistent user-wide configuration that could affect the separate RTK runner.

Replacement run `33222848695`, job `99020389131`, uses the unchanged evaluator
and had entered the 84 GB whole-object mapper at the next audit.  Its exact
downstream authority was prospectively frozen in aggregate join v0.2 before a
terminal result or artifact existed.  If replacement execution is interrupted,
retain only infrastructure `INCOMPLETE`.
