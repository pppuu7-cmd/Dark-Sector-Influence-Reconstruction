# DSIR recovery checkpoint — Exp073B implementation — 2026-08-27

Exp073B preregistration is already merged to `main` at `df88524b6de81f7e4a50147dfe1749427056a7a1` before this implementation branch.

The frozen preregistration names the C3/GDM source target as

`lesgourg/class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

The already-certified Exp070C workflow, however, records its actual C3 source as

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

Because Exp073B section 7 explicitly classifies a source/provenance reproduction failure as `FAIL_EXP073B_REPRODUCTION_OR_PROVENANCE`, the implementation is provenance-first. It will bind the exact Exp073A artifact, query the frozen source/SHA and the certified workflow source/SHA, and only allow capability claims if the frozen provenance itself reproduces.

No Exp073B scientific classification is claimed in this checkpoint. The workflow must execute on merged `main` first.

If the frozen C3 repository/SHA does not reproduce while the certified workflow repository/SHA does, Exp073B must remain a permanent provenance FAIL. F1–F6 capability claims must then remain unevaluated, rather than being filled post hoc from a different repository.

A corrective audit would require a new prospective experiment identifier and preregistration that changes only the erroneous repository identity while retaining the Exp073B capability criteria and forbidden shortcuts.

No nonlinear cosmology output, covariance, whitening, nuisance SVD/rank, G7 relation/null or G8 result is used by this implementation.

G7/G8/G9 remain OPEN.
