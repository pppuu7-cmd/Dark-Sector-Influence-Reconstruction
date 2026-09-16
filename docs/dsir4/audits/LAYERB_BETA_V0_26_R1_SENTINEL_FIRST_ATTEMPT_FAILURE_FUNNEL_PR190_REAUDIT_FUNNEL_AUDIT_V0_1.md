# DSIR Funnel Auditor review — hardened PR190 static re-audit V0.1

Date: 2026-09-16. Role: independent DSIR Funnel Auditor / Critic. Scope is DSIR only. Repository and Actions state are authoritative; chat is not authority.

## Result reviewed
The reviewed object is the independent response-blind static re-audit of the prospectively hardened PR #190 first-attempt failure-funnel candidate. Main at review start was `0377c6f435ff94682f95708072c8e58c2c5be2cd`. The hardened PR190 target is exact head `5731b605afdc35bd85d3a2014a9e135719a07697`, auditor blob `f7eff337e511baa25d51e5b0c333a97534e1bbc3`, contract blob `3369e5cdd2086ca22dca6bfa575054286fd1dcd7`. The governing prior qualification authority is blob `74b10d5d326ec6984edec986fe1bbc368a73b4f6` and authorizes hardening plus fresh static re-audit only.

The independent re-audit is exact head `ece06ed801c65aa336a06ee8b421e9812b8e1e58`, re-auditor blob `4bf1b3867a953b61e62225735883628869218ded`, workflow blob `5db1a2580c22ca2c65d9b0f0d87aa42940f402bd`.

## Authorization and preregistration
The re-audit is within the prior terminal qualification authority: no failure-funnel execution and no science execution were authorized. V0.26 R1 scientific preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9` remain unchanged. Frozen scientific thresholds and denominator were not modified: 107 rows = DES 53 + BOSS 54; alpha `3e-10`; beta exact-target `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay 738 CLASS constructions. Since the consumed first sentinel attempt failed before science and this gate is static-only, no response-dependent threshold tuning is possible here.

## Code and target identity
Independent comparison from target base `52662ca7a21b3a32377f9b3afe6cfe9d290d6cca` to hardened target head `5731b605...` shows exactly two changed non-runtime files: the failure-funnel auditor and its machine contract. No hosted failure-funnel workflow is present on the target.

The re-audit branch itself adds only the independent re-auditor and its static workflow. The workflow checks out full history (`fetch-depth: 0`), explicitly fetches and binds the exact PR190 target head, verifies the independent re-auditor blob, executes the static auditor, asserts the exact target auditor/contract blobs and fail-closed properties, and uploads only the static receipt plus its SHA256 manifest.

The independent re-auditor checks the governing qualification authority, exact target head/blobs, exact two-file non-runtime diff, absence of a failure-funnel workflow, frozen forensic artifact identity, required live exact-head science-run enumeration, duplicate/rerun rejection, recursive exact ZIP and extracted-tree path checks, exact `safe/...` manifest names/cardinality, and absence of the previously identified basename-normalization/nonrecursive patterns. It also executes adversarial fixtures for nested ZIP extras, nested extracted-tree extras, basename-collision manifests, and duplicate/rerun selection semantics.

## Hosted execution and provenance
Authoritative hosted run `35036894735` is now terminal `completed/success`, workflow id `359177543`, exact head `ece06ed801c65aa336a06ee8b421e9812b8e1e58`, event `push`, run #1 / attempt #1. Exact-head Actions history contains exactly one run, so there is no rerun/selection contamination for this audit object.

There is exactly one job, `104607902297` (`pr190-hardened-static-reaudit`), terminal success. Every substantive step completed successfully: full-history checkout; exact-target fetch/binding; response-blind static re-audit; immutable evidence upload.

There is exactly one artifact, id `10425156161`, name `dsir-v026-r1-first-attempt-failure-funnel-pr190-reaudit-v0-1`. Actions reports ZIP digest `sha256:760f3093f1482461412c433358843c86b477b9d42eae88c7a7be48c04323b9d1`. Independent download and hashing produced the same SHA256.

The ZIP contains exactly two files and no extras:
- `pr190_failure_funnel_reaudit.json`, 1633 bytes, SHA256 `a3426a0dd1a6e5392450c38df3bab1b7c9fd6534f47a6c56dc5a3131ca129ce0`;
- `pr190_failure_funnel_reaudit.sha256`, 105 bytes, SHA256 `84f29443de7f45c278c25640052144965509009b0d1538d72709d3c2a6b76d5d`.

The manifest binds `safe/pr190_failure_funnel_reaudit.json` to SHA256 `a3426a0dd1a6e5392450c38df3bab1b7c9fd6534f47a6c56dc5a3131ca129ce0` and independently verifies.

The producer receipt verdict is `QUALIFIED`; classification is exactly `PR190_HARDENED_FAILURE_FUNNEL_CANDIDATE_STATICALLY_QUALIFIED_FOR_SEPARATE_HOSTED_WORKFLOW_AUTHORING_ONLY`. It records all four adversarial hardening checks true and explicitly records `hosted_failure_funnel_execution_authorized=false`, `terminal_result_authority_authorized=false`, `rerun_authorized=false`, `same_nonce_second_attempt_authorized=false`, `successor_sentinel_science_authorized=false`, and `full_107_row_execution_authorized=false`.

## Counterexample review
The prior two concrete counterexamples were addressed at the frozen hardened head. A post-forensic duplicate/rerun is now a fail-closed condition through required live exact-workflow/head enumeration. Seven correct top-level files plus a nested extra are rejected by recursive ZIP and extracted-tree validation. Basename-collision manifest substitution is rejected by exact relative-name/cardinality parsing. Full-history/exact-SHA availability is prospectively required for any future hosted failure-funnel workflow.

No new counterexample was found that invalidates this static re-audit. This does not prove the future hosted failure-funnel workflow correct: that workflow does not yet exist and must itself be prospectively frozen and independently audited before execution.

## Numerical and interpretation ceiling
No CLASS solve, scientific response, interpolation/grid comparison, solver-tolerance comparison, numerical nondeterminism measurement, covariance read, nuisance analysis, statistical/model inference or physical dark-sector inference occurred in this re-audit. The consumed science attempt `35033268924` remains historical pre-science failure and must never be rerun. The forensic producer remains evidence, not by itself terminal scientific authority.

Green hosted static CI is infrastructure/governance evidence only. It does not convert V0.26 R1 into a sentinel scientific PASS, does not open full 107-row replay, and does not raise readiness or scientific frontier. Effect remains `+0/+0`; readiness remains `68%`; scientific frontier remains `67%`.

## Verdict
`CONFIRMED_SCOPED`.

Confirmed scope: the exact hardened PR190 candidate at head `5731b605...` survived the separately frozen response-blind static re-audit at head `ece06ed...` with independently verified hosted provenance. The only newly admissible stage is prospective authoring of a separate frozen hosted failure-funnel workflow candidate followed by an independent response-blind audit before execution.

Not authorized: execution of the failure funnel; terminal first-attempt result authority; rerun of `35033268924`; same-nonce second attempt; modification/removal/recreation of final L; successor sentinel science; full 107-row replay; covariance; whitening; nuisance marginalization; relation-null; `Wm_S3`; global 65537; downstream statistical/model or physical dark-sector inference.
