#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import socket
import time
import urllib.error
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


class TransportError(RuntimeError):
    pass


class SchemaError(RuntimeError):
    pass


def _parse_content_range(value: str | None):
    if not value:
        return None
    m = re.fullmatch(r"bytes\s+(\d+)-(\d+)/(\d+)", value.strip())
    return tuple(map(int, m.groups())) if m else None


def fetch_prefix(url: str, expected_total: int, prefix_bytes: int, attempts: int = 5):
    last = None
    for attempt in range(1, attempts + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={
                    "Range": f"bytes=0-{prefix_bytes-1}",
                    "Accept-Encoding": "identity",
                    "User-Agent": "DSIR-Exp073Q2-FITS-prefix/0.2",
                },
            )
            with urllib.request.urlopen(req, timeout=180) as r:
                status = getattr(r, "status", None)
                headers = dict(r.headers.items())
                if status == 206:
                    cr = _parse_content_range(headers.get("Content-Range"))
                    if cr is None:
                        raise TransportError("HTTP 206 without valid Content-Range")
                    start, end, total = cr
                    if start != 0 or total != expected_total:
                        raise TransportError(
                            f"unexpected Content-Range {cr}, expected total {expected_total}"
                        )
                    data = r.read(prefix_bytes)
                    mode = "HTTP_206_RANGE"
                elif status == 200:
                    cl = headers.get("Content-Length")
                    if cl is not None and int(cl) != expected_total:
                        raise TransportError(
                            f"HTTP 200 Content-Length {cl} != expected {expected_total}"
                        )
                    data = r.read(prefix_bytes)
                    mode = "HTTP_200_PREFIX_ONLY"
                else:
                    raise TransportError(f"unexpected HTTP status {status}")
            if len(data) < BLOCK:
                raise TransportError(f"prefix too short: {len(data)} bytes")
            return data, {
                "attempt": attempt,
                "http_status": status,
                "transport_mode": mode,
                "received_prefix_bytes": len(data),
                "content_length": headers.get("Content-Length"),
                "content_range": headers.get("Content-Range"),
                "etag": headers.get("ETag"),
                "last_modified": headers.get("Last-Modified"),
            }
        except (TimeoutError, socket.timeout, urllib.error.URLError, TransportError) as exc:
            last = exc
            if attempt < attempts:
                time.sleep(min(5 * attempt, 20))
    raise TransportError(f"all {attempts} prefix attempts failed: {type(last).__name__}: {last}")


def _value_text(card: str):
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


def _parse_scalar(text):
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


def parse_header(buf: bytes, offset: int):
    if offset < 0 or offset >= len(buf):
        raise SchemaError(f"header offset {offset} outside prefix {len(buf)}")
    cards = []
    pos = offset
    for _ in range(256):
        if pos + BLOCK > len(buf):
            raise SchemaError("FITS header extends beyond fetched prefix")
        block = buf[pos : pos + BLOCK]
        block_cards = [
            block[i : i + CARD].decode("ascii", errors="strict")
            for i in range(0, BLOCK, CARD)
        ]
        cards.extend(block_cards)
        if any(c[:8].strip() == "END" for c in block_cards):
            hsz = pos + BLOCK - offset
            break
        pos += BLOCK
    else:
        raise SchemaError("FITS header exceeds 256 blocks")

    h = {}
    for c in cards:
        key = c[:8].strip()
        if key == "END":
            break
        if key and c[8:10] == "= ":
            h[key] = _parse_scalar(_value_text(c))
    return h, hsz


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


def table_columns(h: dict):
    out = []
    for i in range(1, int(h.get("TFIELDS", 0) or 0) + 1):
        name = h.get(f"TTYPE{i}")
        form = h.get(f"TFORM{i}")
        if name is not None and form is not None:
            out.append({"index": i, "name": str(name).strip(), "tform": str(form).strip()})
    return out


def tform_row_storage(tform: str):
    m = re.fullmatch(r"\s*(\d*)([LXBIJKAEDCMPQ])(?:\([^)]*\))?\s*", tform.upper())
    if not m:
        raise SchemaError(f"unsupported TFORM {tform!r}")
    rep = int(m.group(1) or "1")
    code = m.group(2)
    if code == "X":
        return math.ceil(rep / 8), False
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
        "P": 8,
        "Q": 16,
    }[code]
    return rep * unit, code in ("P", "Q")


def enrich_offsets(cols: list[dict], row_bytes: int):
    out = []
    off = 0
    for c in cols:
        width, variable_payload = tform_row_storage(c["tform"])
        d = dict(c)
        d["row_offset_bytes"] = off
        d["row_storage_bytes"] = width
        d["variable_length_payload"] = variable_payload
        out.append(d)
        off += width
    if off != row_bytes:
        raise SchemaError(f"TFORM row-storage sum {off} != NAXIS1 {row_bytes}")
    return out


def first_bintable(buf: bytes, required: list[str]):
    offset = 0
    hdus = []
    for hdu_index in range(8):
        h, hsz = parse_header(buf, offset)
        xt = str(h.get("XTENSION", "PRIMARY")).strip().upper()
        data_bytes = hdu_data_bytes(h)
        info = {
            "hdu_index": hdu_index,
            "header_offset": offset,
            "header_bytes": hsz,
            "xtension": xt,
            "data_bytes": data_bytes,
        }
        hdus.append(info)
        if xt == "BINTABLE":
            row_bytes = int(h["NAXIS1"])
            nrows = int(h["NAXIS2"])
            cols = enrich_offsets(table_columns(h), row_bytes)
            by_name = {c["name"].lower(): c for c in cols}
            missing = [name for name in required if name.lower() not in by_name]
            if missing:
                raise SchemaError(f"first BINTABLE missing required columns: {missing}")
            req_info = []
            for name in required:
                c = by_name[name.lower()]
                if c["variable_length_payload"]:
                    raise SchemaError(f"required column {name} is variable-length payload")
                req_info.append(c)
            return {
                "matching_table": {
                    "hdu_index": hdu_index,
                    "header_offset": offset,
                    "header_bytes": hsz,
                    "naxis1": row_bytes,
                    "naxis2": nrows,
                    "tfields": int(h.get("TFIELDS", 0) or 0),
                },
                "required_columns": req_info,
                "all_columns": cols,
                "hdu_summary": hdus,
            }
        offset += hsz + padded(data_bytes)
        if offset >= len(buf):
            raise SchemaError("first BINTABLE not reachable inside fetched prefix")
    raise SchemaError("no BINTABLE found in first 8 HDUs")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-url", required=True)
    ap.add_argument("--source-bytes", required=True, type=int)
    ap.add_argument("--metacal-url", required=True)
    ap.add_argument("--metacal-bytes", required=True, type=int)
    ap.add_argument("--output", required=True)
    ap.add_argument("--prefix-mib", type=int, default=8)
    args = ap.parse_args()

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    prefix_bytes = args.prefix_mib * 1024 * 1024
    rec = {
        "experiment": "Exp073Q2",
        "date": "2026-08-27",
        "contract": "transport-resilient first-BINTABLE prefix schema and positional row-layout audit",
        "prefix_bytes_requested": prefix_bytes,
        "full_object_redownloaded": False,
        "science_gate_scored": False,
        "coordinate_provenance": {"nside": 4096, "coords": "C", "status": "RESOLVED"},
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "source": {"url": args.source_url, "expected_bytes": args.source_bytes},
        "metacal": {"url": args.metacal_url, "expected_bytes": args.metacal_bytes},
    }
    try:
        src_buf, src_transport = fetch_prefix(args.source_url, args.source_bytes, prefix_bytes)
        rec["source"]["transport"] = src_transport
        rec["source"]["fits"] = first_bintable(src_buf, SOURCE_REQUIRED)
        out.write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")

        mc_buf, mc_transport = fetch_prefix(args.metacal_url, args.metacal_bytes, prefix_bytes)
        rec["metacal"]["transport"] = mc_transport
        rec["metacal"]["fits"] = first_bintable(mc_buf, METACAL_REQUIRED)

        ns = int(rec["source"]["fits"]["matching_table"]["naxis2"])
        nm = int(rec["metacal"]["fits"]["matching_table"]["naxis2"])
        rec["source_rows"] = ns
        rec["metacal_rows"] = nm
        rec["row_count_equal"] = ns == nm
        if ns != nm:
            raise SchemaError(f"row-count mismatch source={ns} metacal={nm}")
        rec["status"] = "SCHEMA_ROW_LAYOUT_PASS_EXP073Q2"
    except TransportError as exc:
        rec["status"] = "INCOMPLETE_EXP073Q2_TRANSPORT"
        rec["error"] = f"{type(exc).__name__}: {exc}"
        rec["completed_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
        out.write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")
        raise
    except (SchemaError, UnicodeDecodeError, KeyError, ValueError) as exc:
        rec["status"] = "FAIL_EXP073Q2_SCHEMA_OR_ROW_ALIGNMENT"
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
        "coords": rec["coordinate_provenance"]["coords"],
        "nside": rec["coordinate_provenance"]["nside"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
