# DSIR recovery checkpoint — Exp072A hard FAIL — 2026-08-27

## Immutable classifications

- Exp066B: permanent hard FAIL.
- Exp067B: permanent hard FAIL.
- Exp068A: permanent scientific FAIL.
- Exp068B: scientific PASS for literal upstream PCA physical forward reproduction only.
- Exp069B: permanent scientific FAIL.
- Exp069H: certified C5 q=3 provider PASS.
- Exp069I: raw-k provenance PASS; does not rewrite prior C5 classifications.
- Exp070A: permanent scientific FAIL.
- Exp070B: interpolation-dominated C3 mechanism diagnosis.
- Exp070C: certified native-grid C3 provider PASS.
- Exp071A: `PASS_COMMON_PHYSICAL_SUPPORT_MASK_V0_1`, 495/495 provider cells retained.
- Exp072A: **permanent scientific FAIL** `FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1`.

## Exp072A immutable provenance

- preregistration merged before first leakage evaluation: PR #102, merge `a22dad1396ff31fe2ab889b5a5d5cfb9170d5f68`;
- execution binding merged before first leakage evaluation: PR #103, merge `d91df1fd04f2db1676d548f9788689b2ff15eb02`;
- implementation PR #104;
- implementation head `553f6867f1cf71d4661a9f7b1f739a970648d05d`;
- implementation merge `f7888f60a916537d4ffd69e179471a26f1ed2655`;
- workflow run `33029362485`;
- workflow job `98378044465`;
- artifact `9629763833`;
- artifact digest `sha256:9ecf7d61b4db5e091392a23f508cd5dd3d04dafe32a4a66d1256a70d9947701d`;
- extracted result JSON SHA256 `56b96c096830bf8399ef18df41251a14ded00101a1f206b4419ccb6b5730abe3`.

## Frozen result

Threshold: invalid positive operator support leakage `<=0.05`.

Candidate observation coordinates: 26.

Nominal retained dimension: **0**.

Tightened-support retained dimension: **0**.

Per sample/channel nominal retention:

- Blue gg 0/6;
- Blue kg 0/7;
- Green gg 0/6;
- Green kg 0/7.

A1–A5, A8, A9 PASS. A6 and A7 FAIL.

Lowest aggregate nominal leakage: `0.6151682900038838`, Green kg at ell midpoint 76.5. Therefore this is not a near-threshold outcome.

Post-output diagnostic only: minimum per-block nominal leakages are `gg/mm=0.08425052286761503`, `gg/Wm=0.6832935480972744`, `gg/WW=0.8989342679620471`, `kg/Wm=0.1364788719151473`, `kg/WW=0.615168379027028`; every one exceeds 0.05. This diagnostic cannot alter the frozen classification.

## Forbidden next actions

Do not:

- lower or relax 0.05;
- widen Exp072A V0 post hoc;
- drop Blue, Green, gg or kg to manufacture a mask;
- proceed to covariance restriction/Cholesky using an empty or hand-selected mask;
- inspect nuisance SVD/rank, G7 residual or G8 response as a workaround;
- reinterpret Exp071A provider-space PASS as observational support.

## Next admissible scientific front

Preregister a causal support-boundary decomposition before evaluating it. Use the same positive released ACT×unWISE operator weights and decompose invalid V0 support into disjoint categories:

1. z-outside only;
2. k-outside only;
3. both z and k outside;
4. valid in both.

The decomposition must not change Exp072A. Its purpose is only to decide whether a corrective provider-certification program should extend k, z, or both. Any later support extension must be independently certified for both C3 and C5 before another angular leakage gate is preregistered.

G7/G8/G9 remain OPEN.
