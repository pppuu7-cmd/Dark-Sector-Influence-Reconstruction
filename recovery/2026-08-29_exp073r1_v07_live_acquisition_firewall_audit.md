# Exp073R1 v0.7 live acquisition firewall audit — 2026-08-29

## Authority/status

- Canonical run: GitHub Actions run `33240490287`, job `99068879596`.
- At this checkpoint steps 1–9 are successful and step 10, `Acquire authoritative object by full-from-zero no-Range retries`, is in progress.
- Steps 11–15 are pending; therefore no mapper result and no genuine Exp073R1 reproduction PASS exists yet.
- Classification remains `REPRODUCTION_INCOMPLETE`; there is no scientific FAIL at this checkpoint.

## Independent transport-firewall audit

Audited `.github/workflows/exp073r1-desy1-transport-stabilized-replay-v0-7.yml` and `ci/exp073r1_v0_7_whole_object_acquire.py` without modifying the active run or any frozen scientific acceptance criterion.

The acquisition path is fail-closed on the identity conditions required by the preregistered transport recovery:

1. each retry deletes any prior destination and starts a new GET from byte zero;
2. the request sends no `Range` header and requests `Accept-Encoding: identity`;
3. HTTP status must be 200 and `Content-Range` must be absent;
4. if supplied, `Content-Length` must equal exactly `84,075,649,920` bytes;
5. the complete stream is hashed while writing;
6. replay authorization remains false until both exact byte count and frozen SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8` pass;
7. interrupted/incomplete attempts are deleted and recorded as infrastructure transport failures;
8. the loopback replay step independently rechecks exact size and SHA256 before serving the object;
9. terminal R1 assertion independently checks acquisition provenance, exact object identity, source/R0 parent bindings, row counts, frozen selection/mapper, repeatability and explicit non-use of downstream science quantities.

No evidence was found in this audit that v0.7 weakens the frozen scientific evaluator. v0.7 changes the transport staging only; the mapper remains the frozen v0.5 implementation identified by Git blob SHA1 `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`.

## Classification note

The acquisition helper currently labels a *complete-length but wrong-SHA256* object as `REPRODUCTION_IDENTITY_FAIL`. This label is an identity/reproducibility failure, **not a scientific G7 FAIL**. Do not reinterpret it as a negative physical result. No code change is made during the active authoritative run; this note freezes the semantic distinction for later provenance/recovery handling.

## Downstream firewall

Until a genuine terminal Exp073R1 PASS exists, do not execute the real Exp073P support-validity mask, covariance restriction/whitening, nuisance tangent SVD/rank, quotient/relation/null control, or any fresh G8 withheld-family computation.

Frozen sequence remains:

`validated physical forward/power-input bridges -> genuine Exp073R1 reproduction PASS -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`.
