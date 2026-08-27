#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import urllib.request
from pathlib import Path

BLOCK = 2880
CARD = 80

SOURCE_REQUIRED = [
    "zbin_mcal",
    "zbin_mcal_1p",
    "zbin_mcal_1m",
    "zbin_mcal_2p",
    "zbin_mcal_2m",
]
METACAL_REQUIRED = ["ra", "dec", "flags_select"]


def _parse_content_range(value: str | None) -> tuple[int, int, int] | None:
    if not value:
        return None
    m = re.fullmatch(r"bytes\s+(\d+)-(\d+)/(\d+)", value.strip())
    if not m:
        return None
    return tuple(map(int, m.groups()))


def fetch_range(url: str, start: int, size: int, expected_total: int) -> bytes:
    end = start + size - 1
    req = urllib.request.Request(
        url,
        headers={
            "Range": f"bytes={start}-{end}",
            "User-Agent": "DSIR-Exp073Q-FITS-schema/0.1",
            "Accept-Encoding": "identity",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        status = getattr(r, "status", None)
        if status != 206:
            raise RuntimeError(f"server did not honor Range: HTTP {status}")
        cr = _parse_content_range(r.headers.get("Content-Range"))
        if cr is None:
            raise RuntimeError("missing or malformed Content-Range")
        got_start, got_end, total = cr
        if (got_start, got_end) != (start, end):
            raise RuntimeError(
                f"Content-Range interval {(got_start, got_end)} != {(start, end)}"
            )
        if total != expected_total:
            raise RuntimeError(f"remote total {total} != expected {expected_total}")
        data = r.read(size + 1)
    if len(data) != size:
        raise RuntimeError(f"range returned {len(data)} bytes, expected {size}")
    return data


def _value_text(card: str) -> str | None:
    if len(card) < 10 or card[8] != "=":
        return None
    s = card[10:]
    in_quote = False
    out = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "'":
            if in_quote and i + 1 < len(s) and s[i + 1] == "'":
                out.extend(["'", "'"])
                i += 2
                continue
            in_quote = not in_quote
        if ch == "/" and not in_quote:
            break
        out.append(ch)
        i += 1
    return "".join(out).strip()


def _parse_scalar(text: str | None):
    if text is None:
        return None
    if text.startswith("'") and text.endswith("'"):
        return text[1:-1].replace("''", "'").strip()
    if text in ("T", "F"):
        return text == "T"
    try:
        return int(text)
    except ValueError:
        try:
            return float(text.replace("D", "E"))
        except ValueError:
            return text


def read_header(url: str, offset: int, expected_total: int) -> tuple[dict, int]:
    cards: list[str] = []
    pos = offset
    for _ in range(256):
        block = fetch_range(url, pos, BLOCK, expected_total)
        block_cards = [
            block[i : i + CARD].decode("ascii", errors="strict")
            for i in range(0, BLOCK, CARD)
        ]
        cards.extend(block_cards)
        if any(c[:8].strip() == "END" for c in block_cards):
            header_size = pos + BLOCK - offset
            break
        pos += BLOCK
    else:
        raise RuntimeError("FITS header exceeded 256 blocks")

    header: dict[str, object] = {}
    for c in cards:
        key = c[:8].strip()
        if key == "END":
            break
        if key and c[8:10] == "= ":
            header[key] = _parse_scalar(_value_text(c))
    return header, header_size


def hdu_data_bytes(h: dict) -> int:
    xt = str(h.get("XTENSION", "PRIMARY")).strip().upper()
    naxis = int(h.get("NAXIS", 0) or 0)
    pcount = int(h.get("PCOUNT", 0) or 0)
    gcount = int(h.get("GCOUNT", 1) or 1)
    if xt == "BINTABLE":
        return (int(h["NAXIS1"]) * int(h["NAXIS2"]) + pcount) * gcount
    if naxis == 0:
        return 0
    bitpix = abs(int(h["BITPIX"]))
    n = 1
    for i in range(1, naxis + 1):
        n *= int(h[f"NAXIS{i}"])
    return ((bitpix * n + 7) // 8 + pcount) * gcount


def padded(n: int) -> int:
    return ((n + BLOCK - 1) // BLOCK) * BLOCK


def table_columns(h: dict) -> list[dict]:
    n = int(h.get("TFIELDS", 0) or 0)
    cols = []
    for i in range(1, n + 1):
        name = h.get(f"TTYPE{i}")
        form = h.get(f"TFORM{i}")
        if name is not None and form is not None:
            cols.append({"index": i, "name": str(name).strip(), "tform": str(form).strip()})
    return cols


def tform_fixed_width(tform: str) -> int | None:
    # FITS binary-table fixed row descriptor width. P/Q are descriptors; values
    # themselves are variable-length and are rejected for required geometry fields.
    m = re.fullmatch(r"\s*(\d*)([LXBIJKAEDCMPQ])(?:\([^)]*\))?\s*", tform.upper())
    if not m:
        return None
    rep = int(m.group(1) or "1")
    code = m.group(2)
    if code in ("P", "Q"):
        return None
    if code == "X":
        return math.ceil(rep / 8)
    unit = {
        "L": 1,
        "B": 1,
        "A": 1,
        "I": 2,
        "J": 4,
        "K": 8,
        "E": 4,
        "D": 8,
        "C": 8,
        "M": 16,
    }[code]
    return rep * unit


def enrich_offsets(cols: list[dict], row_bytes: int) -> list[dict]:
    out = []
    off = 0
    for c in cols:
        width = tform_fixed_width(c["tform"])
        d = dict(c)
        d["row_offset_bytes"] = off if width is not None else None
        d["fixed_width_bytes"] = width
        out.append(d)
        if width is None:
            # We cannot safely infer offsets beyond an unsupported layout.
            off = -1
        elif off >= 0:
            off += width
    if off >= 0 and off != row_bytes:
        raise RuntimeError(f"parsed TFORM widths sum to {off}, NAXIS1={row_bytes}")
    return out


def scan_for_table(url: str, expected_total: int, required: list[str]) -> dict:
    offset = 0
    candidates = []
    hdus = []
    required_lower = {x.lower() for x in required}
    for hdu_index in range(32):
        if offset >= expected_total:
            break
        h, hsz = read_header(url, offset, expected_total)
        xt = str(h.get("XTENSION", "PRIMARY")).strip().upper()
        data_bytes = hdu_data_bytes(h)
        info = {
            "hdu_index": hdu_index,
            "header_offset": offset,
            "header_bytes": hsz,
            "xtension": xt,
            "data_bytes": data_bytes,
        }
        if xt == "BINTABLE":
            row_bytes = int(h["NAXIS1"])
            nrows = int(h["NAXIS2"])
            cols = enrich_offsets(table_columns(h), row_bytes)
            names = {c["name"].lower() for c in cols}
            info.update(
                {
                    "naxis1": row_bytes,
                    "naxis2": nrows,
                    "tfields": int(h.get("TFIELDS", 0) or 0),
                    "columns": cols,
                }
            )
            if required_lower.issubset(names):
                candidates.append(info)
        hdus.append(info)
        offset += hsz + padded(data_bytes)

    if len(candidates) != 1:
        raise RuntimeError(f"expected exactly one matching BINTABLE, found {len(candidates)}")
    chosen = candidates[0]
    by_name = {c["name"].lower(): c for c in chosen["columns"]}
    required_info = []
    for name in required:
        c = by_name[name.lower()]
        if c["fixed_width_bytes"] is None or c["row_offset_bytes"] is None:
            raise RuntimeError(f"required column {name} is not fixed-width: {c['tform']}")
        required_info.append(c)
    return {
        "matching_table": {
            k: chosen[k]
            for k in ("hdu_index", "header_offset", "header_bytes", "naxis1", "naxis2", "tfields")
        },
        "required_columns": required_info,
        "all_columns": chosen["columns"],
        "hdu_summary": [
            {k: v for k, v in h.items() if k != "columns"} for h in hdus
        ],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-url", required=True)
    ap.add_argument("--source-bytes", required=True, type=int)
    ap.add_argument("--metacal-url", required=True)
    ap.add_argument("--metacal-bytes", required=True, type=int)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    rec = {
        "experiment": "Exp073Q",
        "date": "2026-08-27",
        "contract": "range-only FITS schema and positional-row-layout audit",
        "full_object_redownloaded": False,
        "science_gate_scored": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "source": {"url": args.source_url, "expected_bytes": args.source_bytes},
        "metacal": {"url": args.metacal_url, "expected_bytes": args.metacal_bytes},
    }
    try:
        source = scan_for_table(args.source_url, args.source_bytes, SOURCE_REQUIRED)
        metacal = scan_for_table(args.metacal_url, args.metacal_bytes, METACAL_REQUIRED)
        rec["source"]["fits"] = source
        rec["metacal"]["fits"] = metacal
        ns = int(source["matching_table"]["naxis2"])
        nm = int(metacal["matching_table"]["naxis2"])
        rec["source_rows"] = ns
        rec["metacal_rows"] = nm
        rec["row_count_equal"] = ns == nm
        if ns != nm:
            raise RuntimeError(f"row-count mismatch source={ns} metacal={nm}")
        rec["status"] = "SCHEMA_ROW_LAYOUT_PASS_EXP073Q"
    except Exception as exc:
        rec["status"] = "FAIL_EXP073Q_SCHEMA_OR_ROW_ALIGNMENT"
        rec["error"] = f"{type(exc).__name__}: {exc}"
        rec["completed_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
        out.write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")
        raise

    rec["completed_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
    out.write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": rec["status"],
        "source_rows": rec["source_rows"],
        "metacal_rows": rec["metacal_rows"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
