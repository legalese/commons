#!/usr/bin/env python3
"""Write definition, presumption and defence functions of completion pass 2026-11-04 as MAYBE BOOLEAN functions.

Usage (from the encoding folder):
    python3 -I generators/deferred/gen_defs.py SPEC.py > OUT.l4

SPEC.py defines DEFS, a list of dicts.  The text is written into the after-file format gen_offences.py reads
(`-- @@section SEC` markers), so a definition lands after the quotation of its section.

Keys of a def:
    sec      the section it belongs to (the marker)
    name     the function's name, which carries the section: "s 377C(1) the material is child abuse material"
    ref      "s 377C(1) \"child abuse material\"" and lines (lo, hi)
    whole    True on the first definition of a section: an extra `@ref ... (src:@@)` citing the whole quoted run above it
    export   the @export text
    params   [(name, desc)] BOOLEAN parameters
    expr     an L4 condition over the parameters, written [param]
    shape    one of
        means    JUST TRUE if expr, else JUST FALSE   ("means", a closed definition)
        includes JUST TRUE if expr, else NOTHING      ("includes", "may include": the list is not closed)
        if       JUST TRUE if expr, else JUST FALSE   (an "if" / "unless" condition read as the text's own no: marginal reading a)
        flat     JUST FALSE whatever the parameters   ("it is not necessary", "it is not a defence": a flat negative)
        limited  JUST TRUE if expr, else NOTHING      (a grant or rule limited by its own wording: marginal reading b)
    quote    the words that carry the shape, quoted into the comment on the FALSE or NOTHING branch
    why      for NOTHING: one of  list not closed / includes / limited by its own wording / silent / undefined term / points outside the text
"""
import importlib.util
import re
import sys

sp = importlib.util.spec_from_file_location("spec", sys.argv[1])
mod = importlib.util.module_from_spec(sp)
sp.loader.exec_module(mod)

BY = {}
for D in mod.DEFS:
    out = BY.setdefault(D["sec"], [])
    W = out.append
    lo, hi = D["lines"]
    W("")
    if D.get("whole"):  # the first definition of a section quoted once above: its block's @refs reach the whole run (srcrefs --strict)
        W("@ref Penal Code 1871 s %s (src:@@)" % D["sec"])
    W("@ref Penal Code 1871 %s (src:%d-%d)" % (D["ref"], lo, hi))
    W("@export %s" % D["export"])
    first = True
    for (n, d) in D["params"]:
        W("%s`%s` IS A BOOLEAN @desc %s" % ("GIVEN " if first else "      ", n, d))
        first = False
    W("GIVETH A MAYBE BOOLEAN")
    W("`%s` MEANS" % D["name"])
    cond = re.sub(r"\[([^\]]+)\]", lambda m: "`%s`" % m.group(1), D.get("expr", "FALSE"))
    cond = re.sub(r"\bNOT (`[^`]+`)", r"NOT (\1)", cond)  # every NOT is parenthesised (the brief)
    shape = D["shape"]
    q = D["quote"].replace('"', '\\"')
    if shape == "flat":
        W("    JUST FALSE")
        W("        -- FALSE-kind (the text says no in its own words): \"%s\"" % q)
    else:
        W("    IF %s" % cond)
        W("    THEN JUST TRUE")
        if shape in ("means", "if"):
            W("    ELSE JUST FALSE")
            W("        -- FALSE-kind (the text says no in its own words): \"%s\"%s" % (q, " (an \"if\" read as closed: marginal reading a)" if shape == "if" else ""))
        else:
            W("    ELSE NOTHING")
            W("        -- NOTHING-kind (%s): %s" % (D.get("why", "includes"), D.get("note", "\"%s\"" % q)))

for sec, lines in BY.items():
    print("-- @@section %s" % sec)
    print("\n".join(lines).lstrip("\n"))
    print("")
