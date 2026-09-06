# Exp073FT — WW_S1_S2 provenance admission v0.1

Date frozen: 2026-09-06. This is a hosted-only gate executed after Exp073FS heavy science and before any successor heavy target.

Admit `WW_S1_S2` only if the Exp073FS home job completed success, raw logs contain both `PASS_EXP073FS_REPLICA_{A,B}_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1` and `PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`, and the uploaded artifact independently verifies the complete six-stage/prune chains, ordered `[1,2]` / `S1->S2`, exactly two distinct field identities, one S1 and one S2 reconstruction, exact public file-backed 19,327,352,832-byte MCM route, canonical `<f8 [39,12288]` EE arrays, exact SHA equality, `numpy.array_equal`, finiteness, and no tolerance/rescue path.

The candidate run/head, artifact id/size/digest are bound from the executing frozen Exp073FS workflow and must be self-consistent. Artifact ZIP SHA-256 must equal GitHub metadata digest. Candidate PASS alone is not authority.

Only complete success emits `PASS_EXP073FT_WW_S1_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, classification `SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s1_s2_authority_created=true`. Any failure stops the autonomous queue. A successor may be dispatched only after this exact admission PASS.
