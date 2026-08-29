# Recovery checkpoint — Exp073R1 v0.6 repeated remote EOF -> v0.7 transport-stabilized launch

Date: 2026-08-29

## Authority status

Exp073R1 reproduction remains INCOMPLETE. No scientific FAIL has occurred. G7/G8/G9 remain OPEN and no downstream support-validity, covariance/whitening, nuisance SVD/rank, quotient/relation/null or withheld-family quantity has been computed.

## v0.6 attempt 2 terminal observation

Canonical workflow run: `33222848695`
Latest job attempt ID: `99062223326`
Conclusion: failure

All preflight integrity stages passed:

- frozen evaluator blob exact;
- immutable Stage-A metadata binding PASS;
- immutable Exp073R0 metadata binding PASS;
- Stage-A and R0 artifacts downloaded and internally re-bound PASS;
- runtime installed successfully with numpy 2.5.2 and healpy 1.20.0.

The unchanged mapper then failed after about 12 minutes inside `read_exact` with:

`EOFError: whole stream ended after 10839192 of requested 40239104 bytes`

The terminal genuine-R1 assertion was skipped. This is the second independent premature-EOF failure of the direct remote whole-object stream. The earlier attempt had also terminated in the same code path with a different partial-byte position. Therefore the repeated event is classified as:

`INFRASTRUCTURE_TRANSPORT_FAILURE_REMOTE_WHOLE_OBJECT_EOF_REPEATED`

It is explicitly NOT a scientific FAIL and NOT evidence against the frozen Exp073R1 mapping result.

## Recovery decision

A third unchanged direct-stream retry was not launched because the same upstream transport failure mode is now replicated twice. Instead, an infrastructure-only v0.7 route was preregistered before execution.

Preregistration commit: `401b6bc6f28fcef369d83dd0bc893bb35f9c722e`
Acquisition guard commit: `50ce6d2f430dbbeff973358f75348adbb768885a`
Workflow commit: `17aea62e7addb6d5c12326afaeab7a2065b58585`
Trigger commit: `9a4606fb37d5aaa071aa57322ebb7c05eca905d7`

## v0.7 frozen recovery architecture

1. acquire the authoritative 84,075,649,920-byte metacal object using independent whole-object GET attempts only;
2. every retry starts at byte zero; no Range/resume/sparse assembly is allowed;
3. reject any HTTP non-200, Content-Range, wrong Content-Length, premature EOF, wrong byte count, or wrong SHA;
4. authorize the local object only at exact SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
5. serve that exact byte object over loopback HTTP;
6. execute the unchanged frozen v0.5 evaluator blob against the loopback whole-object endpoint;
7. require the same terminal `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` assertions and downstream firewall as before.

This separates unreliable remote transport from the scientific evaluator boundary without changing the data bytes, selection, HEALPix mapper, frozen acceptance criteria, or parent authority.

## Active authoritative candidate

v0.7 workflow run: `33240490287`
Head: `9a4606fb37d5aaa071aa57322ebb7c05eca905d7`
Status at checkpoint creation: `in_progress`

No duplicate heavy run was launched.

## Required downstream order after genuine R1 PASS

validated physical forward/power-input bridges -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> only then fresh G8 withheld family.
