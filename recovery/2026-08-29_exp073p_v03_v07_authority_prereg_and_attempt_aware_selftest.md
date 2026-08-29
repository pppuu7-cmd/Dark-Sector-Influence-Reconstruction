# DSIR recovery checkpoint — Exp073P v0.3 authority for Exp073R1 v0.7

Date: 2026-08-29

## Live upstream state at checkpoint

- Exp073R1 v0.7 authoritative run: `33240490287`.
- Exact rerun attempt: `2`.
- Attempt-2 job: `99080934021` (`transport-stabilized-replay`).
- Execution head: `9a4606fb37d5aaa071aa57322ebb7c05eca905d7`.
- Workflow: `.github/workflows/exp073r1-desy1-transport-stabilized-replay-v0-7.yml`.
- At the start of this iteration attempt 2 remained queued for the self-hosted Linux runner. No duplicate heavy run was launched.
- Exp073R1 reproduction therefore remains INCOMPLETE unless later live Actions metadata proves a genuine terminal PASS.

## Authority gap found

The existing Exp073P production aggregate prerequisite join v0.2 is prospectively frozen to Exp073R1 v0.6 run `33222848695`, attempt 1, job `99020389131`. It cannot legally be repointed to v0.7 after observing a v0.7 result. Reusing it for v0.7 would violate the non-retroactive authority contract even if the scientific evaluator itself were unchanged.

A second, more subtle reproducibility issue is that GitHub Actions reruns share a run ID. Authority keyed only to run ID/name can therefore confuse attempt-1 and attempt-2 executions. Future v0.3 collection must explicitly bind `run_attempt=2` and the attempt-2 job identity.

These are provenance/reproducibility issues, not scientific FAILs.

## Prospective repair frozen before attempt-2 result

Created `experiments/073p_aggregate_prerequisite_join_v07_r1_authority_prereg_v0_3.md` while run `33240490287`, attempt 2, was still queued. It freezes the sole admitted v0.7 authority to:

- run `33240490287`, attempt `2`;
- job `99080934021`;
- head `9a4606fb37d5aaa071aa57322ebb7c05eca905d7`;
- workflow ID `345172058` and exact workflow path/name;
- workflow Git blob `99ce26540f15620c9c6a7acd9198b9d5fe81ecb6`;
- unchanged evaluator Git blob `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`;
- expected v0.7 artifact and required summary/acquisition/runtime members.

Historical v0.1/v0.2 authority files remain immutable and fail-closed.

## Independent synthetic validation

Added `ci/exp073p_v03_v07_authority_contract_selftest.py` and hosted workflow `.github/workflows/exp073p-v03-v07-authority-contract-selftest.yml`.

Hosted Actions run `33250019007`, job `99093989267`, completed `success`. It verified the preregistration/script byte identities and rejected 15 synthetic fail-open mutations, including:

- wrong run attempt;
- wrong job ID;
- wrong job attempt;
- wrong head/workflow;
- artifact ID/digest mismatch;
- missing or unauthorized acquisition provenance;
- nonzero Range count;
- wrong final byte count/SHA256;
- resumed acquisition attempt;
- non-PASS R1 summary;
- downstream science leakage.

The immutable synthetic receipt artifact is `9714057464`, digest `sha256:df2742602a2039817a04d537d86dd884490484be40e7135b7aa2a1a1dae26f26`. Synthetic evidence explicitly keeps `support_executor_authorized=false` and does not evaluate physical support.

## Next scientifically admissible work

1. Do not duplicate Exp073R1 v0.7 while attempt 2 is queued/running.
2. If attempt 2 reaches genuine terminal Exp073R1 PASS, collect immutable artifact ID/digest and implement/run the new v0.3 aggregate prerequisite join under the frozen attempt-aware authority contract.
3. If attempt 2 ends in infrastructure failure, record it as infrastructure failure; do not call it a G7 scientific FAIL and do not authorize support execution.
4. Only after genuine real v0.3 prerequisite PASS may the already-preregistered physical support-validity mask execute.
5. Preserve strict order thereafter: covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> only then fresh G8 withheld family.

No `f_invalid`, covariance, whitening, nuisance SVD/rank, relation/null, held-out or G8 quantity was computed in this iteration.