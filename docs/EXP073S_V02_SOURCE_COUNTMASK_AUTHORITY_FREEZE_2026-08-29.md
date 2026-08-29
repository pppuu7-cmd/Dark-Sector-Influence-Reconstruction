# Exp073S v0.2 source count-mask authority freeze — 2026-08-29

This commit is the direct-parent authority freeze for the corrected artifact-delivery lineage.

Protected inputs:

- v0.1 representation prereg blob `61809ee4430321d4533523ef7834d7155ac9dcc3`;
- v0.2 artifact-correction prereg blob `c17a4d1dbdba3d674b0d76281a84a4bc0df992cd`;
- unchanged evaluator blob `4d22d596b39f07f0bcb3af390e99ead607c517f5`;
- v0.2 workflow blob `1d46c5a45580a49df7eed1fb6fe244983e63f25b`.

Corrected R1 Actions artifact identity:

- run `33270843577` / job `99148916507`;
- artifact ID `9720335366`;
- size `66138507`;
- digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- expected name `exp073r1-v08-hosted-wholestream-ef783ca941fb9b9b5f5eae537986c56ff06e6536`.

The immediate child may change only `ci/exp073s_desy1_source_countmask_reconstruction_v0_2.trigger`. The workflow enforces that relation before any artifact download.

No physical-support, covariance, nuisance or G7/G8/G9 criterion changes are authorized here.
