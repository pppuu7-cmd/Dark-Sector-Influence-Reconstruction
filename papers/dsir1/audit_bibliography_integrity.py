#!/usr/bin/env python3
"""Audit DSIR-I citation-key integrity without changing bibliography content."""

from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BIB = HERE / "references.bib"
SOURCES = [HERE / "manuscript.md"] + sorted((HERE / "sections").glob("*.md"))


def require(cond: bool, message: str) -> None:
    if not cond:
        raise AssertionError(message)


def main() -> None:
    bib = BIB.read_text(encoding="utf-8")
    bib_keys = re.findall(r"(?m)^@\w+\s*\{\s*([^,\s]+)\s*,", bib)
    require(bib_keys, "no BibTeX entries found")
    duplicates = sorted({k for k in bib_keys if bib_keys.count(k) > 1})
    require(not duplicates, f"duplicate BibTeX keys: {duplicates}")
    keyset = set(bib_keys)

    cited: set[str] = set()
    citation_occurrences = 0
    for path in SOURCES:
        text = path.read_text(encoding="utf-8")
        for group in re.findall(r"\[(@[^\]]+)\]", text):
            keys = [x.strip().lstrip("@") for x in group.split(";")]
            for key in keys:
                require(re.fullmatch(r"[A-Za-z0-9_.:-]+", key) is not None,
                        f"malformed citation key {key!r} in {path.name}")
                cited.add(key)
                citation_occurrences += 1

    require(cited, "no manuscript citation keys found")
    missing = sorted(cited - keyset)
    require(not missing, f"citation keys missing from references.bib: {missing}")

    unused = sorted(keyset - cited)
    print(f"PASS: {len(cited)} unique cited keys / {citation_occurrences} citation-key occurrences")
    print(f"PASS: {len(keyset)} unique BibTeX entries; no duplicate keys")
    print("PASS: every manuscript citation key exists in references.bib")
    print(f"INFO: {len(unused)} currently uncited bibliography entries")
    if unused:
        print("INFO: uncited keys: " + ", ".join(unused))


if __name__ == "__main__":
    main()
