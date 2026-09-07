# DSIR research log — FV authority and FW chaining

Date: 2026-09-07. DSIR only.

Exp073FU historical terminal failures were consumed as implementation/infrastructure `+0/+0`. The first causal defects were successively isolated to comparator literal transforms and resume/admission log semantics; all repairs were prospective and left frozen science unchanged.

Successful Exp073FU run `34120000242`: home job `101735669327` reused verified post-prune compact checkpoints A/B and emitted the exact frozen S1->S3 repeatability PASS. Artifact `10017795904`, ZIP SHA256 `91c881a132e5a85c7a18cacb6890e42f4bd66ae7dbdd402c72cd9a317e8d68c2` independently matched; A/B canonical payload SHA256 `aee5a7b28b60b522a885a121c44544b0360fd9736b955fa5024641db63c2429b`, exact-equal and finite.

Exp073FV hosted job `101735763144` independently verified the artifact/manifests and emitted `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `ww_s1_s3_authority_created=true`. `WW_S1_S3` is therefore admitted.

FV then deterministically dispatched Exp073FW run `34120059297` for frozen `WW_S2_S2`. Hosted launch audit `101735824056` passed; home job `101735874893` is the sole active heavy owner on `DSIR-HOME-PC-2`. No competing heavy run was launched. Next action is terminal consumption of FW under its preregistered contract.
