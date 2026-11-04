#!/usr/bin/env python3
"""Write the repetitive parts of the offence modules of completion pass 2026-11-04.

Usage (from the encoding folder):
    python3 -I generators/deferred/gen_offences.py SPEC.py >> MODULE.l4
    python3 -I generators/deferred/expand.py MODULE.l4

SPEC.py defines SECTIONS, a list of dicts; each dict is one section.  For the section the generator writes,
in the form pc-body-a-deferred.l4 uses by hand for ss 304B and 304C:

  - the `-- @quote` placeholder over the section's raw lines (expand.py then writes the quotation lines);
  - the facts record (particulars, victim, `victim described as`, `the manner`, then the leaves given);
  - one defining predicate per entry of `defs`, written as the Code's words (a quotation) joined by `...`
    to the leaves that carry them;
  - one `-- @punish` placeholder per punishment record named;
  - per entry of `offences`: `offence under s N`, the list of what is not made out, and `charge under s N`.

A section's hand-written parts (definitions as functions, defences, Illustrations) go in a separate file or are
appended by hand; the generator does not touch them.

Mini-syntax in every expression string:
    [leaf name]   becomes   f's `leaf name`
    {v}           becomes   (`one` (f's victim) (f's `victim described as`))
    {m}           becomes   f's `the manner`
An expression with AND, OR or NOT in it is wrapped in parentheses where it stands alone.

Keys of a section dict:
    sec        the heading label, e.g. "372"
    title      the §§ heading text
    quote      (lo, hi) raw lines
    notes      comment lines written above the first @ref (list of str), optional
    record     the facts record's name
    victim     @desc of the `victim` field
    manner     @desc of the `the manner` field
    leaves     list of (name, desc) or (name, desc, type)
    defs       list of dicts: name, lines (lo, hi), export (str), conj [(quote|None, expr, missing|None)]
    offences   list of dicts: label, lines, export_offence, export_charge, offence_quote, defn (an L4 expression
               over the defs, e.g. "`x within section 372` f"), punish (list of ids to render),
               punish_expr (L4 expression for the punishment words in the charge),
               charge_name, charge_body (an L4 expression of type STRING), miss [(expr, text)] (what to list
               as not made out; the last entry, the definition taken together, is added by the generator)
"""
import importlib.util
import re
import sys

spec_path = sys.argv[1]
AFTER = {}
if len(sys.argv) > 2:
    cur = None
    for ln in open(sys.argv[2], encoding="utf-8").read().split("\n"):
        m = re.match(r"^-- @@section (\S+)\s*$", ln)
        if m:
            cur = m.group(1)
            AFTER.setdefault(cur, [])
        elif cur:
            AFTER[cur].append(ln)

sp = importlib.util.spec_from_file_location("spec", spec_path)
mod = importlib.util.module_from_spec(sp)
sp.loader.exec_module(mod)


def sub(expr, rec):
    expr = re.sub(r"\[([^\]]+)\]", lambda m: "f's `%s`" % m.group(1), expr)
    expr = re.sub(r"\bNOT (f's `[^`]+`)", r"NOT (\1)", expr)  # every NOT is parenthesised (the brief)
    expr = expr.replace("{v}", "(`one` (f's victim) (f's `victim described as`))")
    expr = expr.replace("{m}", "f's `the manner`")
    return expr


def top_ops(e):
    """The set of AND / OR / NOT found at parenthesis depth 0, outside backticks and strings."""
    ops, d, i = set(), 0, 0
    while i < len(e):
        c = e[i]
        if c == "`":
            i = e.index("`", i + 1) + 1
            continue
        if c == '"':
            i = e.index('"', i + 1) + 1
            continue
        if c == "(":
            d += 1
        elif c == ")":
            d -= 1
        elif d == 0:
            for op in ("AND", "OR", "NOT"):
                if e.startswith(op, i) and (i == 0 or e[i - 1] == " ") and (i + len(op) == len(e) or e[i + len(op)] == " "):
                    ops.add(op)
        i += 1
    return ops


def paren(expr):
    e = expr.strip()
    return "(" + e + ")" if top_ops(e) else e


def top_or(e):
    """True if the expression has OR at depth 0 (the linter wants such groups at another column)."""
    return "OR" in top_ops(e)


def q(s):
    return '"' + s.replace('"', '\\"') + '"'


out = []
W = out.append

for S in mod.SECTIONS:
    rec = S.get("record")
    W("")
    W("")
    W("§§ `s %s - %s`" % (S["sec"], S["title"]))
    W("")
    lo, hi = S["quote"]
    W("-- @quote %d %d" % (lo, hi))
    for n in S.get("notes", []):
        W("-- " + n)
    if "record" in S:
        W("@ref Penal Code 1871 s %s (src:@@)" % S["sec"])
        W("DECLARE `%s` HAS" % rec)
        W("    particulars IS A Particulars @desc Who is charged, and when and where the offence was committed")
        W("    victim IS A STRING @desc %s" % S["victim"])
        W("    `victim described as` IS A STRING @desc How the charge describes that person, after the name; leave blank if not needed")
        W("    `the manner` IS A STRING @desc %s" % S["manner"])
        for lf in S["leaves"]:
            name, desc = lf[0], lf[1]
            typ = lf[2] if len(lf) > 2 else "BOOLEAN"
            if typ not in ("BOOLEAN", "STRING", "NUMBER"):
                typ = "`%s`" % typ
            W("    `%s` IS A %s @desc %s" % (name, typ, desc))
        for D in S["defs"]:
            a, b = D["lines"]
            W("")
            W("@ref Penal Code 1871 s %s (src:%d-%d)" % (S["sec"], a, b))
            W("@export %s" % D["export"])
            W("GIVEN f IS A `%s` @desc %s" % (rec, D.get("given", "The facts of the case")))
            W("GIVETH A BOOLEAN")
            W("DECIDE `%s` f IF" % D["name"])
            first = True
            for cj in D["conj"]:
                quote, expr = cj[0], cj[1]
                if quote:
                    W(("        " if first else "   ...  ") + q(quote))
                    first = False
                ex = sub(expr, rec)
                pre = "        " if first else ("   ...    " if top_or(ex) else "   ...  ")
                W(pre + paren(ex))
                first = False
                if len(cj) > 3 and cj[3]:
                    W("        -- " + cj[3])
        for O in S["offences"]:
            lab = O["label"]
            a, b = O["lines"]
            for pid in O.get("punish", []):
                W("")
                W("-- @punish %s" % pid)
            W("")
            W("@ref Penal Code 1871 s %s (src:%d-%d)" % (lab, a, b))
            W("@export %s" % O["export_offence"])
            W("GIVEN f IS A `%s` @desc %s" % (rec, O.get("given", "The facts of the case")))
            W("GIVETH A BOOLEAN")
            W("DECIDE `offence under s %s` f IF" % lab)
            W("        " + q(O["offence_quote"]))
            W("   ...  " + sub(O["defn"], rec))
            W("")
            key = O.get("key", lab)
            W("GIVEN f IS A `%s`" % rec)
            W("GIVETH A LIST OF STRING")
            W("`elements of %s not made out` f MEANS" % O["charge_name"])
            W("    concat (LIST")
            miss = O.get("miss")
            if miss is None:
                miss = []
                for dn in O["miss_from"]:
                    dd = next(d for d in S["defs"] if d["name"] == dn)
                    miss += [(c[1], c[2] or c[1]) for c in dd["conj"]]
                miss += O.get("miss_extra", [])
            for (expr, text) in miss:
                W("        (`missing unless` (%s) %s)," % (sub(expr, rec), q(text)))
            W("        (`missing unless` (`offence under s %s` f) %s))" % (lab, q("the elements of section %s taken together" % lab)))
            W("")
            W("@ref Penal Code 1871 s %s (src:%d-%d)" % (lab, a, b))
            W("@export %s" % O["export_charge"])
            W("GIVEN f IS A `%s` @desc %s" % (rec, O.get("given_charge", "The facts of the case and the particulars of the charge")))
            W("GIVETH A Charge")
            W("`charge under s %s` f MEANS" % lab)
            W("    `frame the charge` (f's particulars) %s %s" % (q(lab), q(O["charge_name"])))
            W("        (%s)" % sub(O["punish_expr"], rec))
            W("        (`offence under s %s` f)" % lab)
            W("        (%s)" % sub(O["charge_body"], rec))
            W("        (`elements of %s not made out` f)" % O["charge_name"])
    if S["sec"] in AFTER:
        W("")
        out.extend(AFTER[S["sec"]])

print("\n".join(out))
