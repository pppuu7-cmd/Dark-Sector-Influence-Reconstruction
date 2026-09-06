# Exp073FR — WW_S1_S1 file-backed checkpoint provenance admission v0.1

Status: **PROSPECTIVELY FROZEN; NOT YET RUN**

Scope: DSIR only. Never mix RTK or RQIR.

## Purpose

Exp073FR is the authority-writing admission gate that may be executed only after Exp073FM reaches a terminal state and its compact artifact has first been independently consumed and classified under the already-frozen Exp073FM contract. Exp073FR must not inspect or depend on partial Exp073FM numerical output while Exp073FM is running.

A workflow/job SUCCESS is not sufficient. Authority may be created only if every requirement below is verified against the terminal Exp073FM evidence.

## Frozen predecessor and science identity

Predecessor science gate: Exp073FM `WW_S1_S1`.

Frozen target semantics:
- authoritative source pair `[1,1]`;
- reconstruct S1 exactly once per replica;
- construct exactly one spin-2 field per replica;
- pass the **same Python field object** to both sides of the coupling matrix;
- equal-but-distinct second field is forbidden;
- DES NSIDE = 4096;
- ell = `0..12287`;
- 39 bands;
- WW selection `EE<-EE`;
- canonical selected array dtype/shape `<f8 [39,12288]`;
- public file-backed NaMaster 2.7 BPW route;
- exact MCM backing size `19,327,352,832` bytes with `/proc/self/maps` proof;
- exact A/B SHA equality plus `numpy.array_equal` and all-finite requirement;
- no `allclose`, `isclose`, tolerance, rounding, smoothing, averaging, manual reconstruction, effective-coordinate shortcut, fiducial-P shortcut, or post-hoc rescue.

Frozen implementation blobs inherited from Exp073FM:
- driver v0.1 `477647c5164264665cc16e20d1577fb25cd245f4`;
- file-backed adapter v0.2 `8e3edff39aae95d3abc3196806802c5f0ae59832`;
- complete-chain verify/prune `8e04e99084aed582f9586e3f316c023650ce6c63`;
- terminal comparator `02d69d5d517c676b3ec0963380f93d13f2b9874e`;
- fail-closed home envelope `873232cc96f9a97afefeff1ff0a433fd5b49a5a2`.

Exp073FM prereg creation commit: `391af1d14ca61f20ef42cccde348453ca84a1aaa`; prereg blob: `da64cbb6d0f7553387b5b635812cfa25ec7fb8fa`.

## Mandatory terminal evidence checks

Before any authority write, Exp073FR must fail-closed unless all of the following hold:

1. The exact terminal Exp073FM workflow/run, job, head SHA, artifact ID, GitHub artifact digest and independently recomputed ZIP SHA256 are recorded and mutually consistent.
2. Both A and B checkpoint namespaces are the prospectively frozen Exp073FM namespaces and show complete, internally consistent six-stage chains with canonical payload SHA256/provenance/contract identity verified before pruning.
3. Any restored completed stage is accepted only after exact payload and receipt revalidation; no stale, cross-namespace or historical payload is admitted.
4. Source identity is S1/S1 exactly, with one S1 reconstruction and one field object per replica, reused on both coupling sides.
5. Public file-backed BPW provenance and exact `19,327,352,832`-byte mmap backing proof are present and valid.
6. Frozen source/contract/driver/adapter/verify-prune/comparator/home-envelope identities match the prospectively frozen values above.
7. Both canonical selected A/B arrays are `<f8 [39,12288]`, finite, have identical SHA256 and satisfy exact `numpy.array_equal`.
8. The terminal Exp073FM candidate token, if PASS, is exactly `PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.
9. No tolerance/rescue path was used anywhere in scoring or admission.
10. Historical support gates (Exp073FO/FP/FQ and hosted launch audit) remain support `+0/+0` and are not promoted to science authority.

## Classification

- If every mandatory check passes and the independently consumed Exp073FM candidate is a valid exact PASS, emit exactly:
  `PASS_EXP073FR_WW_S1_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`
  with classification `SCIENTIFIC_AUTHORITY_ADMITTED` and `ww_s1_s1_authority_created=true`.
- Exact numerical A/B mismatch under the frozen Exp073FM contract is a genuine `SCIENTIFIC_FAIL`; Exp073FR must not repair or rescue it.
- Provenance, artifact, checkpoint, identity, transport, malformed-evidence, runner or software defects are classified separately as infrastructure/support/resource outcomes as appropriate and create no authority.
- Ambiguity at an exact threshold is `numerically_unresolved`, never tolerance-rescued.

## Nonduplication / execution rule

Do not launch Exp073FR while Exp073FM is in progress. First consume and classify the terminal Exp073FM artifact. Only then may one nonduplicating hosted admission workflow be generated and run against the frozen evidence. Exp073FR performs no self-hosted heavy science and must not acquire `DSIR-HOME-PC`.
