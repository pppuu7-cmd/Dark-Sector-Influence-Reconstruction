# Exp073HZ — C2 tangent raw-set provenance admission v0.1

Status: PROSPECTIVELY FROZEN BEFORE ADMISSION EXECUTION.

## Purpose
Admit, and only admit, the nine complete raw tangent model-point artifacts produced by Exp073HY run `34243515299` at head `ca3b6a1de8ff96dfc0525ef8485f1ad57e2976b8`. This gate performs no ABI decode, no `Delta_m` mapping, no tangent derivative, no prediction, and creates no scientific model authority.

## Frozen producer lineage
- producer run: `34243515299`
- producer head: `ca3b6a1de8ff96dfc0525ef8485f1ad57e2976b8`
- solver: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`
- post-HS `perturbations.c` SHA256: `483b481b48e50a6afb396b15b85258ac6c5a7a39b38fb1c6192e7e4a95c139ae`
- post-HS `evolver_ndf15.c` SHA256: `3f12121ce2de319453e1ff5fadae9391fd96747731c0df3fa05fae1cd2608aa9`
- baseline SHA256: `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`
- precision SHA256: `463a3960d6a955c1e2a561e988562a1fc5486b0b79f120eb634ccca6f86002f9`

## Frozen nine-artifact manifest
Each artifact must contain exactly 28 packet files named `packets/z00k00.bin` through `packets/z06k03.bin`, each exactly 64 bytes, and `aggregate.bin` exactly equal to their z-major/k-minor concatenation and exactly 1792 bytes. `RECEIPT.txt` must bind the same model point, run/head/job/source fingerprints and must state `complete_model_unit=true`, `tangent_raw_set_admitted=false`, `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`.

| model | alpha | beta | job | artifact id | GitHub ZIP SHA256 | aggregate SHA256 |
|---|---:|---:|---:|---:|---|---|
| alpha_m1e4 | -1e-4 | 0 | 102119471802 | 10064603451 | 009217562eab68c85a701b1a4b7de4dbe4f0f2d933a129e496336748aa01219b | 1aa24586b57116ac126d314c389e13f8d3159826cc20edea1c8220b1ef69e6ba |
| alpha_m1e3 | -1e-3 | 0 | 102119471057 | 10063499422 | c74365587ec13b581e79f0cfb124d90db643a0cc6e3998d076ca9164b7dc1c7c | b4258528fffa8f115fa98ad9dedb29b8dc6ac8bd7b1710790dfde60776101797 |
| alpha_m1e2 | -1e-2 | 0 | 102119471655 | 10063491863 | 93df49f78bff19844d841008291284d82c3c77855a28be70333a6aa494ddc7f5 | 383b4afbf91d8caa30ed546e562da79a5ddaa35e6725627901b6bd2ff5b9f1c2 |
| beta_p1e4 | 0 | 1e-4 | 102119471486 | 10063489526 | 146d7d9470f89367624030524108f4a5fe0a9ff6890d6b00cfb46732bcf355d0 | d3f852986d23e3c527ca6da389af2e1b63f51c4af19588d33be31bcdd2a01c4e |
| beta_m1e4 | 0 | -1e-4 | 102119471483 | 10063472739 | dc470dce5f802ec57c1a8801cfc634d56fe597c1eb172cc32bf8ab6b40ace36c | 13b80ab8f1d5c7d6a4402768c7a66a50376a7245b745cc76d55f7f63ecd2fe64 |
| beta_p1e3 | 0 | 1e-3 | 102119471369 | 10063484506 | d6b1064ef0ec1fd45a51a77ca1f919a071badda790aebd41b9a2373a2e0b47bb | 77ef62e3d4e0670334245112612af043f38e0cd38262b14fd923e3446d94bc21 |
| beta_m1e3 | 0 | -1e-3 | 102119471373 | 10063583778 | d78f45ab1d7405f969ea825cfaa670ff2b91e28f2d324e9639ce30a3ff79c607 | 0a06a4395e0050185790cecb6ee1091bb8249052b74125778bba1c0384fc284c |
| beta_p1e2 | 0 | 1e-2 | 102119471600 | 10063508302 | 176a2b209fef406f1dee72352ed8f6ac0331c5e81164cf015c627d7208210081 | cc21ed6c8989b1e05db1184de400b25e866285790ba8089658eb211c79f52c44 |
| beta_m1e2 | 0 | -1e-2 | 102119471334 | 10063482583 | 18695bc1ab4e429d55723e44862b118e67ad2aa1ab7b6b3dbec266c976dbe873 | cb9c076b54f8bc48a55f5a49a921e66021a9a59bba43be57aea07efc32d43954 |

## Exact gate
PASS only if all nine GitHub artifact ZIP SHA256 digests match the frozen manifest, each receipt matches its frozen lineage/model/job fields, each has exactly 28 distinct 64-byte packets in the exact `z00k00..z06k03` coordinate set, exact z-major/k-minor reassembly equals `aggregate.bin`, each aggregate is exactly 1792 bytes and matches its frozen SHA256, and no extra or duplicate model point is admitted.

PASS token: `PASS_EXP073HZ_C2_TANGENT_RAW_SET_PROVENANCE_ADMISSION_V0_1`

On PASS only:
- `classification=TANGENT_RAW_SET_ADMITTED_PLUS_0_PLUS_0`
- `tangent_raw_set_admitted=true`
- `decoded=false`
- `mapped=false`
- `tangent_response_ready=false`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

Any mismatch is fail-closed. No tolerance, rounding, smoothing, averaging, effective coordinate, replacement payload, or post-hoc rescue is permitted.