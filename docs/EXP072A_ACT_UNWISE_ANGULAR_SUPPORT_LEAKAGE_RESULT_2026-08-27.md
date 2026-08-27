# Exp072A — ACT×unWISE angular support/leakage result — 2026-08-27

## Classification

**Scientific classification: `FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1`.**

This is a scientific FAIL under the prospectively frozen Exp072A contract. It is not an infrastructure failure and it must not be rescued by relaxing the 5% leakage threshold, widening `V0` without a new provider certification, dropping samples/channels, changing absolute operator weights, or lowering the preregistered retained-dimension requirement.

## Provenance

- implementation PR: #104;
- implementation head: `553f6867f1cf71d4661a9f7b1f739a970648d05d`;
- implementation merge: `f7888f60a916537d4ffd69e179471a26f1ed2655`;
- workflow run: `33029362485`;
- workflow job: `98378044465`;
- immutable artifact: `9629763833`;
- artifact digest: `sha256:9ecf7d61b4db5e091392a23f508cd5dd3d04dafe32a4a66d1256a70d9947701d`;
- extracted JSON SHA256: `56b96c096830bf8399ef18df41251a14ded00101a1f206b4419ccb6b5730abe3`.

The run completed all scientific evaluation and artifact-upload steps successfully. Therefore the FAIL below is a frozen scientific outcome.

## Frozen gate result

The candidate observation space contained exactly 26 coordinates. With the frozen nominal support envelope

- `0.295 <= z <= 2.33`,
- `0.000704833374744468 <= k <= 0.06664762008318016 Mpc^-1`,
- all three provider blocks `mm/Wm/WW`,

and the preregistered invalid-support threshold

`L_j(V0) <= 0.05`,

**zero of 26 coordinates survived**.

Nominal retained counts:

- Blue `Clgg`: 0/6;
- Blue `Clkg`: 0/7;
- Green `Clgg`: 0/6;
- Green `Clkg`: 0/7;
- total: 0/26.

The one-layer-tightened `V1` robustness mask also retained 0/26.

The smallest nominal aggregate leakage among all 26 coordinates was

`0.6151682900038838`

for Green `Clkg` at released midpoint `ell=76.5`, still more than an order of magnitude above the frozen 0.05 ceiling. The next-lowest low-ell examples were Blue `Clkg(76.5)=0.7642825952218016` and Green `Clgg(126.5)=0.8989342451263727`.

## A1–A9

Passed:

- A1 exact upstream/CAMB/archive provenance and pinned source contract;
- A2 exact immutable Exp071A support binding;
- A3 exact released operator and 26-coordinate binding;
- A4 finite positive denominators and finite leakage fractions;
- A5 exact nominal mask construction at the frozen 5% threshold;
- A8 tightened-support monotonicity/subset controls;
- A9 proof that covariance, Cholesky/whitening, nuisance SVD/rank, G7 relation/null, G8 responses and article-selection quantities were not read.

Failed:

- A6 per-sample/per-channel retained coverage, because every channel retained zero coordinates;
- A7 retained dimension >=15, because the nominal retained dimension is zero.

No downstream covariance restriction is authorized.

## Post-output blockwise robustness diagnostic

The preregistered aggregate statistic sums positive support weights over physical blocks. After the scientific classification was fixed, a diagnostic was made using the already-recorded per-block leakages to check that the negative result is not an artifact of relative block weighting.

Minimum nominal `V0` leakage over all coordinates in each applicable block was:

- `gg/mm`: `0.08425052286761503`;
- `gg/Wm`: `0.6832935480972744`;
- `gg/WW`: `0.8989342679620471`;
- `kg/Wm`: `0.1364788719151473`;
- `kg/WW`: `0.615168379027028`.

Every blockwise minimum is itself above 0.05. Thus even a convention-invariant rule requiring every applicable block separately to satisfy the same 5% support ceiling would retain no coordinate. This is explicitly a post-output robustness statement, **not** a replacement acceptance rule and not a reclassification of Exp072A.

## Scientific meaning

Exp071A remains a valid provider-space PASS: C3 and C5 share a certified finite physical grid. Exp072A shows that this shared grid is far too narrow, under the frozen released ACT×unWISE operator-support criterion, to support any of the 26 selected angular observables at <=5% invalid-support leakage.

This is a boundary result about the present physical-provider support, not evidence against GDM, designer f(R), dark matter, modified gravity, or a dark sector. It also provides no evidence for new physics.

The present ACT×unWISE G7 route is therefore blocked **before covariance whitening and nuisance quotienting**. The next admissible experiment must diagnose which physical support boundary (`k`, `z`, or both) dominates the leakage and then, if justified, certify a genuinely wider physical provider domain under a new prospective contract. Exp072A itself remains a permanent scientific FAIL.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
