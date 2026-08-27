# DSIR recovery checkpoint — Exp069F/Exp069H C5 provider certification

Date: 2026-08-27

## Immutable evidence

Exp069F GitHub Actions run `33023027901` completed successfully at the infrastructure level and uploaded artifact `exp069f-c5-general-accuracy-30706773a0069b6bbe3144443debeeffa6fba328` (artifact id `9627458877`, digest `sha256:d8e1a42bf813d5ae105ea33e723868d454ff7584424373ecfe4594a2dfe49358`). The frozen ladder was q=[1,2,3,4] with hard GR-limit 5e-6.

Scientific Exp069F diagnostics:

- M_q = [5.302921926164412e-6, 2.904403568550871e-6, 1.7011186858522977e-6, 1.3107890273503598e-6].
- R_q = [9.938162077359033e-6, 5.400555774622087e-6, 2.8421302380756537e-6, 1.5177816179258466e-6].
- M_q and R_q are monotone non-increasing across the frozen ladder.
- First q satisfying the frozen target closure M_q <= 5e-6 is q=2.
- Classification: `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`.
- Exp069F by construction does not certify C5.

Exp069H GitHub Actions run `33024638764` completed successfully at the infrastructure level and uploaded artifact `exp069h-c5-q3-provider-26162b0f2472dc1862eeb60b564a3563eaae12f9` (artifact id `9628053962`, digest `sha256:fa61b504d31edeba2afcbed0f4b14bda688df82a96d2cba55eac034682b5382f`). It prospectively bound the already-frozen Exp069G contract and froze q=3 before executing the provider certification.

Scientific Exp069H hard checks, all PASS:

- C1 exact-zero closure: M0_target = 1.7011186858522977e-6 <= 5e-6 and R0_raw = 2.8421302380756537e-6 <= 5e-6.
- C2 tiny-positive continuity: PASS at B0={1e-12,1e-10,1e-8} under the unchanged 5e-6 limit.
- C3 nontrivial production signal: S_prod = 0.013249122882007408 > 0.001.
- C4 signed P_Wm/accessor semantics: PASS.
- C5 repeatability/state integrity: D_repeat_target=0 and D_repeat_raw=0, threshold 1e-12.
- C6 no retrospective correction: PASS.
- C7 literal public zero provider: PASS.
- Solver SHA remained pinned at `16d9c4e9f85751e30efd0a53b177941713078904` before/after; upstream source was not modified; no floor subtraction or renormalization was used.

Scientific classification: `PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1`.

## Gate transition

This is a scientific provider certification, not merely a workflow success. Therefore the provider ledger advances prospectively:

- C3/GDM physical provider: **ELIGIBLE** (Exp070C).
- C5/designer-f(R) physical provider: **ELIGIBLE** (Exp069H).
- Exp069B remains a permanent scientific FAIL for its original q=1 bridge and is not overwritten.
- The prior q=1 failure and exact-A=0 analytic boundary remain part of provenance.

The G7 ordering constraint now authorizes only the next stage: **prospectively preregister the common physical support-validity mask**. Covariance restriction/whitening, nuisance tangent SVD, quotient/relation/null controls and G8 remain blocked until their preceding stage is frozen and completed.

## Recovery state

`C3 provider = ELIGIBLE`

`C5 provider = ELIGIBLE`

`support mask preregistration = AUTHORIZED`

`support mask application = NOT YET RUN`

`covariance/whitening = BLOCKED`

`nuisance SVD = BLOCKED`

`quotient/relation/null = BLOCKED`

`G7 = OPEN`

`G8 = OPEN`

`G9 = OPEN`
