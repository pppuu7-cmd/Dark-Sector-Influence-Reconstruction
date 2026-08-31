# DSIR recovery checkpoint — Exp073BE provenance PASS, Exp073BA harness-only rerun, Exp073BD active

**Date:** 2026-08-31  
**Authority scope:** Article 3 / G7 pre-support angular production  
**Scientific authority readiness:** **52.0% — unchanged**  
**Draft/data readiness:** **53.7% — unchanged by this checkpoint**

Repository/hosted authority outranks chat wording. This checkpoint does not authorize covariance/whitening, G7 closure, or G8.

## 1. Exp073BC binding is no longer future work

The AZ-to-BA binding receipt was frozen in commit:

`60e16d8a6266a32feb17073c1947c28dce23c944` — `freeze Exp073BC AZ-to-BA binding receipt`.

The exact Exp073AZ PCL authority had already been bound to the frozen BA route in commit:

`994c1ee765a26e1f30794edf86ce06acb2734a25`.

Therefore the older `docs/RECOVERY_LATEST.md` wording that places BC receipt creation as the next future action is historical and is superseded by this checkpoint.

## 2. Exp073BE exact artifact-binding diagnostic — PASS, provenance only

Hosted diagnostic run:

- run `33344976594`;
- trigger/head commit `e511136c147298ad3e35b814377f9b4f8ffb45e9`;
- diagnostic workflow commit `0c5d3304b58e391f17bcb888f440519926e1d1c3`;
- canonical Exp073AZ PCL shape: `[12288]`;
- canonical dtype under the frozen contract: `<f8`;
- full payload SHA-256: `2a990b28ac490f96228b4131303db746a31668029220366f6c81e90b86da5888`;
- A/B diagnostic copies agree with the frozen receipt;
- classification: provenance/harness PASS only;
- scientific readiness increment: `+0`.

This confirms that the downloaded canonical `.npy` payload is the intended frozen Exp073AZ authority object. It does not establish Wm_S1 scientific repeatability and does not repair the permanent Exp073AQ exact-repeatability FAIL.

## 3. Exp073BA first production attempt — infrastructure failure before matrix computation

First BA production run:

- run `33342137113`;
- trigger/head commit `089d81eb6716b83a93910fc3f546523da122f38e`;
- both replica jobs failed at `Bind exact admitted AZ PCL`;
- failure occurred before `Compute low-memory compact Wm_S1 replica`;
- therefore this run supplies no scientific Wm_S1 classification and must not be recorded as scientific FAIL.

The frozen provenance receipt and the Exp073BE diagnostic agree on the PCL payload and hashes. Inspection of the BA workflow isolated a harness defect: the binding step imported NumPy through plain `python` even though NumPy/NaMaster are installed in the dedicated frozen environment and exposed as `NMT_PY` immediately before the binding step.

## 4. Harness-only correction — no scientific contract change

Workflow correction commit:

`1c3c279317f5e178ce168b967834725ae31ecad3` — `fix Exp073BA AZ bind interpreter`.

Only the binding interpreter was changed:

- before: `python - <<'PY'`;
- after: `"${NMT_PY}" - <<'PY'`.

Unchanged:

- Exp073AZ run/head binding;
- PCL payload/hash;
- Wm_S1 task definition;
- geometry and banding;
- low-memory scientific implementation;
- exact A/B comparator;
- seeds/deterministic policy;
- thresholds and PASS criteria;
- no tolerance, rounding, ULP, preferred-replica, or majority-vote rescue.

This is therefore an infrastructure/harness repair, not a post-hoc scientific rule change.

## 5. Exp073BA clean rerun launched

Trigger commit:

`e921f556885b4432efd0556b661711d7835fd4c0` — `rerun Exp073BA after provenance bind interpreter fix`.

New hosted run:

`33345968620` — `Exp073BA Article3 low-memory Wm_S1 production v0.1`.

At checkpoint creation the rerun is queued. No PASS/FAIL classification may be assigned until both independent compact replicas, exact compact comparator, finalizers, and exact final comparator complete under the frozen workflow.

## 6. Exp073BD provisional Wm_S2 twin production remains active

Hosted run:

`33342265114` — Exp073BD provisional Wm_S2 twin data production.

At the latest inspection both independent branches A and B were still `in_progress` in `Compute independent Wm_S2 provisional branch` after passing setup, frozen Track-P enforcement, exact NaMaster installation, artifact download, and DES Y1 mask download.

Exp073BD is Track P/provisional only. Its completion may improve draft/data handling only under the frozen dual-readiness ledger; it cannot create Track-A scientific authority, cannot substitute for BA exact PASS, and cannot authorize covariance/whitening.

## 7. Exact next operating order

1. Inspect run `33345968620` first. If it fails before scientific computation, diagnose infrastructure without weakening frozen criteria. If it reaches scientific outputs, consume every required A/B/comparator authority artifact exactly.
2. Inspect run `33342265114` without duplicating the heavy computation. Preserve both provisional branches; never choose a preferred branch.
3. If and only if Exp073BA earns the frozen exact Track-A PASS, update the authority/recovery ledger and admit Wm_S1 under the low-memory authority class.
4. Continue the prospective Track-A angular sequence in order. Do not use the provisional BD run as retroactive Track-A authority unless a separately frozen authority protocol explicitly permits that exact provenance.
5. Only after the real 14-window aggregate and support-validity prerequisites are satisfied may Layer A / Layer B proceed.
6. Covariance restriction/whitening remains blocked until its prerequisites are actually passed.
7. Nuisance tangent rank/SVD -> quotient/relation/null control follows whitening.
8. **Fresh G8 withheld-family testing remains forbidden until the complete G7 chain authorizes it.**

## 8. Current status shorthand

- ✅ Exp073AZ exact PCL predecessor authority: PASS.
- ✅ Exp073BC AZ-to-BA binding receipt: frozen.
- ✅ Exp073BE artifact/provenance diagnostic: PASS, `+0` scientific readiness.
- ✅ BA harness defect: isolated and repaired without scientific-contract change.
- 🟡 Exp073BA clean rerun `33345968620`: launched/queued at checkpoint.
- 🟡 Exp073BD provisional Wm_S2 run `33342265114`: active at checkpoint.
- ❌ Exp073AQ historical exact Wm_S1 repeatability result remains permanent scientific FAIL under its original implementation/class.
- ❌ covariance/whitening: not authorized yet.
- ❌ G7: open.
- ❌ G8: open and must not be jumped.
- ❌ G9: open.

`Verified: 52.0% | Draft/data: 53.7%`
