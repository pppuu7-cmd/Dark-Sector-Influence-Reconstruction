# Exp073BZ — remote checkpoint failover Python-path successor v0.1 — preregistration

NONCLASSIFYING DSIR infrastructure/durability QA; every outcome `+0/+0`.

Exp073BY run `33441871911` successfully reused the proven home Miniforge environment and imported NumPy 2.4.6, but stopped before checkpoint logic because invoking `ci/exp073bx_remote_checkpoint_failover_qa_v0_1.py` did not place the repository root on Python's module search path (`ModuleNotFoundError: ci`).

Sole BY->BZ change: execute the unchanged driver with `PYTHONPATH="$GITHUB_WORKSPACE"` on both home and hosted jobs. No checkpoint code, sync code, deterministic row, branch, SHA criterion, progress format, environment lineage or outcome interpretation changes.

Frozen implementation commits remain checkpoint `0b0324afb69acb16cbea97bb924b9be48f303dde`, sync `96886916b41dce7f0a40807622928c841ef5fc58`, driver `15809928dbeea082c0bb6921d581085a89ea6e45`. No scientific authority follows from BZ.
