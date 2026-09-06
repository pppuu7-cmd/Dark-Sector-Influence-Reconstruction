# Exp073FV — WW_S1_S3 provenance admission v0.1

Date frozen: 2026-09-06. Hosted-only authority gate after Exp073FU terminal heavy science.

Admit `WW_S1_S3` only if the Exp073FU home job completed success, raw logs contain both replica full-chain PASS tokens and `PASS_EXP073FU_WW_S1_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`, and the uploaded artifact independently verifies the six-stage/prune chains, ordered `[1,3]` / `S1->S3`, one S1 plus one S3 reconstruction, exactly two distinct field identities, public file-backed NaMaster route, exact `19,327,352,832`-byte MCM backing proof, canonical `<f8 [39,12288]` EE arrays, exact SHA equality, `numpy.array_equal`, finiteness and no tolerance/rescue path.

Only complete success emits `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, classification `SCIENTIFIC_AUTHORITY_ADMITTED`, `ww_s1_s3_authority_created=true`. Any failure stops the autonomous heavy queue. Exact numerical mismatch is scientific FAIL; infrastructure/resource failures remain separate and create no authority.
