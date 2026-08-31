# Exp073BY — remote checkpoint failover Miniforge successor v0.1 — preregistration

**Project:** DSIR only. **Classification:** NONCLASSIFYING infrastructure/durability QA. **Accounting:** `+0/+0`.

Frozen after Exp073BX run `33441722203` stopped on the home runner before checkpoint generation solely because system `python3` lacked NumPy (`ModuleNotFoundError: numpy`). BX produced no checkpoint evidence.

## Sole BX -> BY change

Reuse the already proven self-hosted Wigner benchmark environment at `$HOME/.cache/dsir-nmt27/bin/python`. If absent, bootstrap it using the previously successful Miniforge recipe from commit `a53c4cfdd813f3963ea6d551b37cc3401e7800cf`: local Miniforge plus conda-forge `python=3.11 namaster=2.7 healpy astropy numpy`.

On the GitHub-hosted restore job, create a temporary Python venv and install NumPy before running the unchanged checkpoint driver.

Everything else is frozen unchanged from BX:
- checkpoint utility commit `0b0324afb69acb16cbea97bb924b9be48f303dde`;
- remote sync helper commit `96886916b41dce7f0a40807622928c841ef5fc58`;
- BX driver commit `15809928dbeea082c0bb6921d581085a89ea6e45`;
- dedicated branch `checkpoints/exp073bx-v0-1`;
- three canonical `<f8` deterministic bands;
- exact contract/SHA/final-matrix validation;
- progress `% / elapsed / ETA / threads`;
- Q1/Q2/Q3/Q4 definitions and `+0/+0` accounting.

No scientific result, Wm_S2 authority, mixed-host floating-point equivalence, Layer A/B or G7/G8 authorization follows from BY.
