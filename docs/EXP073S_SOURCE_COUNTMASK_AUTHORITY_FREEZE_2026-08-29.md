# Exp073S source count-mask authority freeze — 2026-08-29

This commit freezes the exact implementation that may be launched by the immediately following trigger-only child commit.

## Protected blobs

- preregistration `experiments/073s_desy1_source_countmask_reconstruction_v0_1_prereg.md`: git blob `61809ee4430321d4533523ef7834d7155ac9dcc3`;
- evaluator `ci/exp073s_desy1_source_countmask_reconstruction_v0_1.py`: git blob `4d22d596b39f07f0bcb3af390e99ead607c517f5`;
- workflow `.github/workflows/exp073s-desy1-source-countmask-reconstruction-v0-1.yml`: git blob `844a76dbbaf70a033ab4e0ad843e06c21e1465fd`.

## R1 input authority

- run `33270843577` / job `99148916507`;
- head `ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- artifact ID `9743987175`;
- artifact digest `sha256:702151cb02abd291e96060887a0da3ce86b908d352997515d48897022b0387ba`.

## Launch rule

The only authorized automatic launch is a direct child commit of this authority-freeze commit whose sole changed path is:

`ci/exp073s_desy1_source_countmask_reconstruction_v0_1.trigger`

and whose trigger file records this authority commit SHA exactly. The workflow checks this relation before any reconstruction.

The four matrix jobs are independent bin-wise reconstruction tests. Their outputs are representation/provenance QA only and cannot score physical support, covariance or G7/G8/G9.
