#!/usr/bin/env python3
"""Expand the fixtures of a tests template of completion pass 2026-11-04.

Usage (from the encoding folder):
    python3 -I generators/deferred/gen_tests.py TEMPLATE.tests.in OUT.l4 MODULE.l4 [MODULE.l4 ...]

A fixture is a record with a dozen to fifty fields, nearly all FALSE.  The template names only the
fields that are not.  The expected values in the assertions are written by hand, from the Code's text,
in the template; the generator writes no assertion.

    -- @fixture `name` OF `Record Facts`
    -- T the field that is TRUE
    -- S a string field = "its value"
    -- E a field of another type = an L4 expression
    -- @end

Every field the record declares and the fixture does not name gets its default: FALSE, "", 0, `the
particulars` for a Particulars, `the victim` for a Person; any other type must be named with E.
A field named in the fixture that the record does not declare is an error, so is a misspelt one.
The records are read from the MODULE files.  Every other line of the template is copied as it is.
"""
import re
import sys

tpl, out = sys.argv[1], sys.argv[2]
mods = sys.argv[3:]

records = {}  # name -> [(field, type)]


def parse_records(text):
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"^DECLARE\s+(`[^`]+`|\S+)\s+HAS\s*$", lines[i])
        if not m:
            i += 1
            continue
        name = m.group(1).strip("`")
        j = i + 1
        body = []
        while j < len(lines) and (lines[j].startswith(" ") or not lines[j].strip()):
            l = lines[j]
            if l.strip() and not l.strip().startswith("--"):
                l = re.split(r"\s@desc\b", l)[0]
                body.append(l.strip())
            j += 1
        joined = " ".join(body)
        fields = []
        for fm in re.finditer(r"(`[^`]+`|[A-Za-z_][\w]*)\s+IS\s+(?:A|AN)\s+(`[^`]+`|[A-Za-z][\w]*)", joined):
            fields.append((fm.group(1).strip("`"), fm.group(2).strip("`")))
        records[name] = fields
        i = j


for mp in mods:
    parse_records(open(mp, encoding="utf-8").read())

DEFAULT = {"BOOLEAN": "FALSE", "STRING": '""', "NUMBER": "0", "Particulars": "`the particulars`", "Person": "`the victim`"}


def q(n):
    return "`%s`" % n if re.search(r"[^A-Za-z0-9_]", n) or True else n


lines = open(tpl, encoding="utf-8").read().split("\n")
res = []
i = 0
count = 0
while i < len(lines):
    ln = lines[i]
    m = re.match(r"^-- @fixture (`[^`]+`) OF (`[^`]+`|\S+)\s*$", ln)
    if not m:
        res.append(ln)
        i += 1
        continue
    fname, rname = m.group(1), m.group(2).strip("`")
    if rname not in records:
        sys.exit("unknown record %r (known: %s)" % (rname, ", ".join(sorted(records))))
    fields = records[rname]
    names = [f for f, _ in fields]
    setv = {}
    i += 1
    comments = []
    while not lines[i].startswith("-- @end"):
        l = lines[i]
        mt = re.match(r"^-- T (.+?)\s*$", l)
        ms = re.match(r"^-- S (.+?) = (\".*\")\s*$", l)
        me = re.match(r"^-- E (.+?) = (.+?)\s*$", l)
        mc = re.match(r"^-- C (.*)$", l)
        if mt:
            f = mt.group(1)
            if f not in names:
                sys.exit("%s: record %s has no field %r" % (fname, rname, f))
            ftype = dict(fields)[f]
            if ftype != "BOOLEAN":
                sys.exit("%s: field %r is %s, not BOOLEAN" % (fname, f, ftype))
            setv[f] = "TRUE"
        elif ms:
            f = ms.group(1)
            if f not in names:
                sys.exit("%s: record %s has no field %r" % (fname, rname, f))
            setv[f] = ms.group(2)
        elif me:
            f = me.group(1)
            if f not in names:
                sys.exit("%s: record %s has no field %r" % (fname, rname, f))
            setv[f] = me.group(2)
        elif mc:
            comments.append("-- " + mc.group(1))
        else:
            sys.exit("%s: cannot read fixture line %r" % (fname, l))
        i += 1
    i += 1  # the @end
    res.extend(comments)
    res.append("%s MEANS `%s` WITH" % (fname, rname))
    for f, t in fields:
        if f in setv:
            v = setv[f]
        elif t in DEFAULT:
            v = DEFAULT[t]
        else:
            sys.exit("%s: field %r has type %s; name it with E" % (fname, f, t))
        res.append("    `%s` IS %s" % (f, v))
    res.append("")
    count += 1

open(out, "w", encoding="utf-8").write("\n".join(res))
print("wrote %s: %d fixtures" % (out, count))
