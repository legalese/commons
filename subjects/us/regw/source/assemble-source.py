#!/usr/bin/env python3
"""Render part223.txt from part223.govinfo-2025.xml, the Part 223 slice of the
govinfo annual CFR volume named in part223.source.json.

    python3 -I assemble-source.py

Nothing here reaches the network. Inline markup is dropped, italics become _x_,
each <P> becomes one line, and each section is headed by its <SECTNO>/<SUBJECT>.
"""
import html
import os
import re

D = os.path.dirname(os.path.abspath(__file__))


def inline(s):
    s = re.sub(r"<I>(.*?)</I>", lambda m: "_" + m.group(1) + "_", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"[ \t\n]+", " ", html.unescape(s)).strip()


x = open(os.path.join(D, "part223.govinfo-2025.xml"), encoding="utf-8").read()
out = []
for sec in re.finditer(r"<SECTION>(.*?)</SECTION>", x, re.S):
    body = sec.group(1)
    no = re.search(r"<SECTNO>(.*?)</SECTNO>", body, re.S)
    sub = re.search(r"<SUBJECT>(.*?)</SUBJECT>", body, re.S)
    out.append("-" * 78)
    out.append(inline(no.group(1)) + "  " + inline(sub.group(1)))
    out.append("-" * 78)
    for pm in re.finditer(r"<(P|FP|CITA|EXTRACT|HD)\b[^>]*>(.*?)</\1>", body, re.S):
        kind, inner = pm.group(1), pm.group(2)
        if kind in ("P", "FP", "HD"):
            out.append(inline(inner))
        elif kind == "CITA":
            out.append(inline(inner))
        else:
            out.append("    " + inline(inner))
    out.append("")
open(os.path.join(D, "part223.txt"), "w", encoding="utf-8").write("\n".join(out))
