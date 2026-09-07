# DSIR immutable recovery — Exp073FV S1S3 authority / Exp073FW active

Date: 2026-09-07. Scope: DSIR only.

## Newly admitted WW authority

Exp073FU run `34120000242` reached a frozen exact candidate PASS from preserved post-prune durable checkpoints without recomputing the expensive MCM stages. Home job `101735669327` on `DSIR-HOME-PC-2` emitted `PASS_EXP073FU_A_POST_PRUNE_TERMINAL_RESUME_CANDIDATE_V0_1`, `PASS_EXP073FU_B_POST_PRUNE_TERMINAL_RESUME_CANDIDATE_V0_1`, `PASS_EXP073FU_LIVE_EXCLUSIVITY`, and `PASS_EXP073FU_WW_S1_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

Artifact `10017795904`, GitHub ZIP digest `sha256:91c881a132e5a85c7a18cacb6890e42f4bd66ae7dbdd402c72cd9a317e8d68c2`; independent download hash matched exactly. The preserved canonical A/B selected payload SHA256 is `aee5a7b28b60b522a885a121c44544b0360fd9736b955fa5024641db63c2429b`, shape `[39,12288]`, dtype `<f8`, semantics `EE<-EE`; bytes are exact-equal and finite. Frozen provenance remains ordered `[1,3] = S1->S3`, one S1 and one S3 reconstruction, distinct field identities, same-field handoff false, source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, and exact file-backed MCM proof `19,327,352,832` bytes.

Exp073FV hosted provenance admission job `101735763144` raw-log emitted:

- `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`
- `classification=SCIENTIFIC_AUTHORITY_ADMITTED`
- `ww_s1_s3_authority_created=true`

Therefore `WW_S1_S3` is now admitted authority. Historical FU implementation/infrastructure failures remain immutable `+0/+0`; they are not scientific failures.

## Repairs preserved prospectively

Comparator literal/schema repairs culminated in comparator blob `08e91910da2b510ef92ab705dbbe360f57506a31`. Terminal-resume wrapper blob `a32eb3c47b4e6c557d43a572a0af356c91134e1b` reuses only post-prune compact checkpoints and lets the comparator re-verify the complete manifest/payload chain. FV verifier blob `0c17dae9172316563a0b09d1da07cceb152acb7a` accepts either original full-chain markers or explicit post-prune resume markers while still independently hashing the preserved stage manifests and canonical payload. No frozen scientific arithmetic, domain, threshold, field semantics or tolerance policy was changed.

## Current heavy process

FV admission deterministically dispatched `exp073fw-ww-s2-s2-home-science-v0-1.yml`.

- workflow/run: Exp073FW / `34120059297`
- head SHA: `d45bf07026956e0bbd95da4f0bfb5840393390e1`
- hosted audit job `101735824056`: SUCCESS
- home job `101735874893`: IN_PROGRESS at this note
- runner owner: `DSIR-HOME-PC-2`
- expected gate: frozen `WW_S2_S2` A/B exact file-backed gate
- no competing DSIR heavy run was launched

Exact next action: terminal-consume Exp073FW, verify raw artifact/provenance against its preregistered gate, classify scientifically, then admit/chain only if the frozen contract permits.

C2 runtime sampling/provenance contract remains frozen support-only; do not start competing C2 cosmological heavy extraction while Exp073FW owns the home runner.
