#!/usr/bin/env python3
"""Render the audited DSIR-I JCAP markdown candidate to LaTeX.

This is intentionally a narrow, fail-closed Markdown renderer for the syntax
actually used by DSIR-I. It is not a general Markdown implementation. The
scientific source remains manuscript_v0_2/manuscript_jcap_candidate; the TeX
file is a deterministic submission rendering.
"""

from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "manuscript_jcap_candidate.md"
FRONT = HERE / "JCAP_FRONT_MATTER_DRAFT.md"
CAPTIONS = HERE / "FIGURE_CAPTIONS.md"
OUTDIR = HERE / "jcap"
OUT = OUTDIR / "dsir1_jcap.tex"

FIGURES = {
    1: ("fig:operator", "../figures/generated/fig01_operator_architecture.pdf"),
    2: ("fig:additive", "../figures/generated/fig02_additive_core_failure.pdf"),
    3: ("fig:hierarchy", "../figures/generated/fig03_chiI_hierarchy.pdf"),
    4: ("fig:channel", "../figures/generated/fig04_channel_conditional_degeneracy.pdf"),
    5: ("fig:curvature", "../figures/generated/fig05_curvature_and_localization.pdf"),
    6: ("fig:failure", "../figures/generated/fig06_failure_resistant_science.pdf"),
    7: ("fig:support", "../figures/generated/fig07_observation_space_support_closure.pdf"),
}

# Frozen Paper-I main-table policy: only the conceptual evidence-graded map and
# exact finite-amplitude hierarchy remain in the journal narrative. Detailed
# family/tangent/angle/turning/localization/route tables are supplementary.
TABLE_META = {
    1: (
        "tab:mechanism-response",
        "Evidence-graded mechanism-to-response map. Equation-level cues identify which response blocks are informative; the mapping is many-to-many and is not a unique inversion to microphysics.",
    ),
    2: (
        "tab:chiI-envelopes",
        "Finite-amplitude sampled interaction-fraction envelopes on the frozen response families. The ordering is descriptive for the tested domains and survives all twelve deterministic single-node deletions.",
    ),
}


def require(cond: bool, message: str) -> None:
    if not cond:
        raise RuntimeError(message)


def extract_between(text: str, start: str, end: str) -> str:
    require(start in text and end in text, f"missing section boundary: {start} -> {end}")
    return text.split(start, 1)[1].split(end, 1)[0].strip()


def escape_plain(s: str) -> str:
    repl = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(repl.get(ch, ch) for ch in s)


def cite_tex(raw: str) -> str:
    keys = [x.strip().lstrip("@") for x in raw.split(";")]
    require(all(re.fullmatch(r"[A-Za-z0-9_.:-]+", k) for k in keys), f"invalid citation token: {raw}")
    return r"\cite{" + ",".join(keys) + "}"


def inline_tex(text: str) -> str:
    """Convert the restricted DSIR-I inline Markdown/LaTeX syntax."""
    pattern = re.compile(
        r"(\\\(.*?\\\)|`[^`]+`|\[@[^\]]+\]|\*\*[^*]+\*\*|Figure [1-7])"
    )
    out: list[str] = []
    pos = 0
    for m in pattern.finditer(text):
        plain = text[pos:m.start()]
        require("\\" not in plain, f"unparsed backslash in prose: {plain!r}")
        out.append(escape_plain(plain))
        token = m.group(0)
        if token.startswith(r"\("):
            out.append(token)
        elif token.startswith("`"):
            payload = token[1:-1]
            require("{" not in payload and "}" not in payload, f"unsupported braces in inline code: {payload}")
            out.append(r"\texttt{\detokenize{" + payload + "}}")
        elif token.startswith("[@"):
            out.append(cite_tex(token[1:-1]))
        elif token.startswith("**"):
            out.append(r"\textbf{" + inline_tex(token[2:-2]) + "}")
        elif token.startswith("Figure "):
            n = int(token.split()[1])
            label, _ = FIGURES[n]
            out.append(r"Figure~\ref{" + label + "}")
        else:
            raise AssertionError(token)
        pos = m.end()
    tail = text[pos:]
    require("\\" not in tail, f"unparsed backslash in prose tail: {tail!r}")
    out.append(escape_plain(tail))
    return "".join(out)


def captions_by_old_number() -> dict[int, str]:
    text = CAPTIONS.read_text(encoding="utf-8")
    result: dict[int, str] = {}
    for n in range(1, 8):
        marker = f"## Figure {n} "
        require(marker in text, f"caption heading missing for Figure {n}")
        block = text.split(marker, 1)[1]
        next_heading = re.search(r"\n## Figure \d+ |\n## Supplementary", block)
        if next_heading:
            block = block[: next_heading.start()]
        block = block.strip()
        paras = [p.strip() for p in block.split("\n\n") if p.strip()]
        require(paras, f"caption body missing for Figure {n}")
        caption = paras[0]
        caption = re.sub(rf"^\*\*Figure {n}\.[^*]*\*\*\s*", "", caption)
        if caption.startswith(f"**Figure {n}."):
            end = caption.find("**", 2)
            require(end > 0, f"malformed bold caption lead for Figure {n}")
            caption = caption[end + 2 :].strip()
        require(caption, f"empty stripped caption for Figure {n}")
        result[n] = caption
    return result


def figure_env(old_n: int, caption: str) -> str:
    label, path = FIGURES[old_n]
    return "\n".join(
        [
            r"\begin{figure}[t]",
            r"\centering",
            rf"\includegraphics[width=0.98\textwidth]{{{path}}}",
            r"\caption{" + inline_tex(caption) + "}",
            r"\label{" + label + "}",
            r"\end{figure}",
        ]
    )


def parse_table_row(line: str) -> list[str]:
    require(line.startswith("|") and line.endswith("|"), f"malformed Markdown table row: {line}")
    return [cell.strip() for cell in line[1:-1].split("|")]


def is_table_separator(line: str) -> bool:
    if not (line.startswith("|") and line.endswith("|")):
        return False
    cells = parse_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c) for c in cells)


def table_env(index: int, header: list[str], rows: list[list[str]]) -> str:
    require(index in TABLE_META, f"unexpected extra main-manuscript table #{index}")
    ncols = len(header)
    require(ncols in (2, 3), f"unsupported table width {ncols} in table #{index}")
    require(rows, f"table #{index} has no data rows")
    require(all(len(r) == ncols for r in rows), f"inconsistent column count in table #{index}")

    if ncols == 3:
        colspec = r"p{0.17\textwidth} p{0.34\textwidth} p{0.41\textwidth}"
    else:
        colspec = r"p{0.42\textwidth} p{0.46\textwidth}"

    label, caption = TABLE_META[index]
    tex: list[str] = [
        r"\begin{table}[t]",
        r"\centering",
        r"\small",
        r"\begin{tabular}{" + colspec + "}",
        r"\toprule",
        " & ".join(r"\textbf{" + inline_tex(c) + "}" for c in header) + r" \\",
        r"\midrule",
    ]
    for row in rows:
        tex.append(" & ".join(inline_tex(c) for c in row) + r" \\")
    tex += [
        r"\bottomrule",
        r"\end{tabular}",
        r"\caption{" + inline_tex(caption) + "}",
        r"\label{" + label + "}",
        r"\end{table}",
    ]
    return "\n".join(tex)


def convert_body(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    in_math = False
    in_itemize = False
    in_enumerate = False
    inserted_figures: set[int] = set()
    captions = captions_by_old_number()
    table_count = 0

    def close_lists() -> None:
        nonlocal in_itemize, in_enumerate
        if in_itemize:
            out.append(r"\end{itemize}")
            in_itemize = False
        if in_enumerate:
            out.append(r"\end{enumerate}")
            in_enumerate = False

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        if line.strip() == r"\[":
            close_lists()
            require(not in_math, "nested display math start")
            in_math = True
            out.append(r"\[")
            i += 1
            continue
        if line.strip() == r"\]":
            require(in_math, "display math end without start")
            in_math = False
            out.append(r"\]")
            i += 1
            continue
        if in_math:
            out.append(line)
            i += 1
            continue

        if not line.strip():
            close_lists()
            out.append("")
            i += 1
            continue

        if line.startswith("|"):
            close_lists()
            require(
                i + 1 < len(lines) and is_table_separator(lines[i + 1].rstrip()),
                f"table header lacks valid separator at source line {i + 1}",
            )
            header = parse_table_row(line)
            sep = parse_table_row(lines[i + 1].rstrip())
            require(len(sep) == len(header), "table separator width differs from header")
            rows: list[list[str]] = []
            j = i + 2
            while j < len(lines) and lines[j].rstrip().startswith("|"):
                row_line = lines[j].rstrip()
                require(not is_table_separator(row_line), "unexpected second table separator")
                rows.append(parse_table_row(row_line))
                j += 1
            table_count += 1
            out.append(table_env(table_count, header, rows))
            i = j
            continue

        if line.startswith("### "):
            close_lists()
            title = re.sub(r"^\d+(?:\.\d+)*\s+", "", line[4:])
            out.append(r"\subsubsection{" + inline_tex(title) + "}")
            i += 1
            continue
        if line.startswith("## "):
            close_lists()
            title = re.sub(r"^\d+(?:\.\d+)*\s+", "", line[3:])
            out.append(r"\subsection{" + inline_tex(title) + "}")
            i += 1
            continue
        if line.startswith("# "):
            close_lists()
            title = re.sub(r"^\d+\.\s+", "", line[2:])
            require(title != "Abstract", "Abstract leaked into LaTeX body")
            out.append(r"\section{" + inline_tex(title) + "}")
            i += 1
            continue

        if line.startswith("- "):
            if in_enumerate:
                out.append(r"\end{enumerate}")
                in_enumerate = False
            if not in_itemize:
                out.append(r"\begin{itemize}")
                in_itemize = True
            out.append(r"\item " + inline_tex(line[2:]))
            i += 1
            continue

        mnum = re.match(r"^\d+\.\s+(.*)$", line)
        if mnum:
            if in_itemize:
                out.append(r"\end{itemize}")
                in_itemize = False
            if not in_enumerate:
                out.append(r"\begin{enumerate}")
                in_enumerate = True
            out.append(r"\item " + inline_tex(mnum.group(1)))
            i += 1
            continue

        close_lists()
        require(not line.startswith(">"), "Markdown blockquotes are unsupported in manuscript body")
        require("```" not in line, "fenced code blocks are unsupported in manuscript body")

        old_refs = [int(x) for x in re.findall(r"Figure ([1-7])", line)]
        out.append(inline_tex(line))
        for old_n in old_refs:
            if old_n not in inserted_figures:
                out.append(figure_env(old_n, captions[old_n]))
                inserted_figures.add(old_n)
        i += 1

    close_lists()
    require(not in_math, "unclosed display math block")
    require(inserted_figures == set(range(1, 8)), f"not all seven figures inserted: {sorted(inserted_figures)}")
    require(table_count == 2, f"expected exactly two main-manuscript Markdown tables, found {table_count}")
    return "\n".join(out).strip()


def main() -> None:
    src = SOURCE.read_text(encoding="utf-8")
    front = FRONT.read_text(encoding="utf-8")

    if src.startswith("---\n"):
        parts = src.split("---\n", 2)
        require(len(parts) == 3, "malformed YAML front matter")
        src = parts[2].lstrip()

    require("# 1. Introduction" in src, "Introduction missing from JCAP candidate")
    body = src.split("# 1. Introduction", 1)[1]
    body = "# 1. Introduction\n" + body

    abstract = extract_between(front, "## JCAP-ready abstract candidate", "## Candidate JCAP keywords")

    title = "Dark-Sector Influence Reconstruction I: Observable-response geometry, channel-conditional equivalence, and failure-resistant model comparison"
    keywords = "dark energy theory, dark matter theory, modified gravity, Cosmological perturbation theory in GR and beyond"

    tex_body = convert_body(body)

    tex = rf"""\documentclass[11pt,a4paper]{{article}}
\pdfoutput=1
\usepackage{{jcappub}}
\usepackage{{booktabs}}

\title{{{title}}}
\author[a]{{Aleksey Buyanov}}
\affiliation[a]{{Independent Researcher, Moscow, Russia}}
\emailAdd{{pppuu7@gmail.com}}
\note{{ORCID: 0009-0001-2621-9305}}
\abstract{{{inline_tex(abstract)}}}
\keywords{{{keywords}}}
% \arxivnumber{{TO-BE-ASSIGNED}}

\begin{{document}}
\maketitle

{tex_body}

\bibliographystyle{{JHEP}}
\bibliography{{../references}}

\end{{document}}
"""

    for token in (
        r"\documentclass[11pt,a4paper]{article}",
        r"\pdfoutput=1",
        r"\usepackage{jcappub}",
        r"\usepackage{booktabs}",
        r"\author[a]{Aleksey Buyanov}",
        "Independent Researcher",
        r"\bibliographystyle{JHEP}",
        r"\bibliography{../references}",
        r"\label{fig:operator}",
        r"\label{fig:channel}",
        r"\label{fig:additive}",
        r"\label{fig:hierarchy}",
        r"\label{fig:curvature}",
        r"\label{fig:failure}",
        r"\label{fig:support}",
        r"\label{tab:mechanism-response}",
        r"\label{tab:chiI-envelopes}",
    ):
        require(token in tex, f"required JCAP LaTeX token missing: {token}")

    for forbidden_label in (r"\label{tab:atlas}", r"\label{tab:chiI}"):
        require(forbidden_label not in tex, f"supplement-only table leaked into JCAP main TeX: {forbidden_label}")

    require("[@" not in tex, "unconverted Pandoc citation remains in TeX")
    require("**" not in tex, "unconverted Markdown bold remains in TeX")
    require("```" not in tex, "unconverted Markdown fence remains in TeX")
    require("# 1." not in tex, "raw Markdown heading remains in TeX")
    require("|---" not in tex, "raw Markdown table separator remains in TeX")

    OUTDIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(tex, encoding="utf-8")
    print(f"wrote {OUT}")
    print("PASS: JCAP LaTeX main-table count = 2")


if __name__ == "__main__":
    main()
