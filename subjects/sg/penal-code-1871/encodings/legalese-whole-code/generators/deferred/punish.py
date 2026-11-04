"""The `Punishment` records of the provisions completed on 2026-11-04, as data.

Each entry gives the provision's label (for the name `punishment prescribed by s <label>`), the raw lines
the punishing words are in, the words verbatim (checked by expand.py against those lines, with the
enumerators "(a)" "(b)" taken out of the raw text), and the shape.  The shapes are the Code's own verbs:

  IMP_FINE_BOTH        "imprisonment ..., or with fine, or with both"
  IMP_ALSO_FINE_CANE   "imprisonment ..., and shall also be liable to fine or to caning"
  IMP_FINE_CANE_COMB   "imprisonment ..., or with fine, or with caning, or with any combination of such punishments"
  IMP_ONLY             "imprisonment for a term which may extend to N years"
  (special)            written out in the entry
"""

NP, PW, OR, SAL = "`not prescribed`", "`shall be punished with`", "`or with`", "`shall also be liable to`"


def months(y):
    return int(y * 12)


def shape(kind, term, maxfine=None):
    base = dict(death=NP, life=NP, imp=PW, mx=term, mn=None, forf=NP, fine=NP, maxfine=maxfine, minfine=None,
                cane=NP, minstr=None, maxstr=None, both=False)
    if kind == "IMP_FINE_BOTH":
        base.update(imp=OR, fine=OR, both=True)
    elif kind == "IMP_ALSO_FINE_CANE":
        base.update(imp=PW, fine=SAL, cane=SAL, both=False)
    elif kind == "IMP_FINE_CANE_COMB":
        base.update(imp=OR, fine=OR, cane=OR, both=True)
    elif kind == "IMP_ONLY":
        base.update(imp=PW, both=False)
    else:
        raise ValueError(kind)
    return base


def P(label, lines, words, kind, years, maxfine=None):
    d = shape(kind, months(years), maxfine)
    d.update(label=label, lines=lines, words=words)
    return d


PUNISH = {}


def add(label, lines, words, kind, years, maxfine=None):
    PUNISH[label] = P(label, lines, words, kind, years, maxfine)


# ------------------------------------------------------------------ body-a
# two alternatives the text does not choose between (304B(1)(a)/(b), 304C(4)(a)/(b)): both are recorded in
# the one record, as `punishment prescribed by s 304(a)` records its (i)/(ii)
for lab, ln in (("304B(1)", (6862, 6868)), ("304C(4)", (6953, 6959))):
    d = shape("IMP_ALSO_FINE_CANE", months(30))
    d.update(label=lab, lines=ln, life=OR, imp=OR,
             words="imprisonment for life and shall also be liable to caning; or imprisonment for a term which may extend to 30 years, and shall also be liable to fine or to caning")
    PUNISH[lab] = d
d = shape("IMP_ALSO_FINE_CANE", months(20))
d.update(label="308A(2)", lines=(7139, 7141), life=OR, imp=OR, fine=NP,
         words="imprisonment for life or imprisonment for a term which may extend to 20 years, and shall also be liable to caning")
PUNISH["308A(2)"] = d
d = shape("IMP_ALSO_FINE_CANE", months(10))
d.update(label="311", lines=(7193, 7196), life=OR, imp=OR, cane=NP,
         words="imprisonment for life, or with imprisonment for a term which may extend to 10 years, and shall, if she is not sentenced to imprisonment for life, also be liable to fine")
PUNISH["311"] = d
add("314", (7233, 7238), "imprisonment for a term which may extend to 10 years, and shall also be liable to fine", "IMP_ALSO_FINE_CANE", 10)
PUNISH["314"].update(cane=NP)
d = shape("IMP_ALSO_FINE_CANE", months(10))
d.update(label="314, without consent", lines=(7233, 7238), life=OR, imp=OR, fine=SAL, cane=NP,
         words="imprisonment for life, or with the punishment above-mentioned")
PUNISH["314, without consent"] = d
add("315(1)", (7245, 7250), "imprisonment for a term not exceeding 10 years, or with fine, or with both", "IMP_FINE_BOTH", 10)
add("316", (7260, 7263), "imprisonment for a term which may extend to 10 years, and shall also be liable to fine", "IMP_ALSO_FINE_CANE", 10)
PUNISH["316"].update(cane=NP)
add("335A(5)(a)", (7598, 7600), "imprisonment for a term which may extend to 7 years, or with fine which may extend to $20,000, or with both", "IMP_FINE_BOTH", 7, 20000)
add("335A(5)(b)", (7603, 7604), "imprisonment for a term which may extend to 4 years, or with fine which may extend to $4,000, or with both", "IMP_FINE_BOTH", 4, 4000)

# ------------------------------------------------------------------ body-b
add("372", (8073, 8078), "imprisonment for a term which may extend to 10 years, and shall also be liable to fine", "IMP_ALSO_FINE_CANE", 10)
PUNISH["372"].update(cane=NP)
add("373", (8087, 8092), "imprisonment for a term which may extend to 10 years, and shall also be liable to fine", "IMP_ALSO_FINE_CANE", 10)
PUNISH["373"].update(cane=NP)
add("373A", (8112, 8113), "imprisonment for a term not exceeding 10 years, and shall also be liable to fine", "IMP_ALSO_FINE_CANE", 10)
PUNISH["373A"].update(cane=NP)
add("376B(1)", (8361, 8363), "imprisonment for a term which may extend to 7 years, or with fine, or with both", "IMP_FINE_BOTH", 7)
add("376B(2)", (8365, 8368), "imprisonment for a term which may extend to 2 years, or with fine, or with both", "IMP_FINE_BOTH", 2)
add("376D(3)", (8437, 8438), "imprisonment for a term which may extend to 10 years, or with fine, or with both", "IMP_FINE_BOTH", 10)
add("376E(4)(a)", (8507, 8512), "imprisonment for a term which may extend to 7 years, or with fine, or with both", "IMP_FINE_BOTH", 7)
add("376E(4)(b)", (8516, 8518), "imprisonment for a term which may extend to 5 years, or with fine, or with both", "IMP_FINE_BOTH", 5)
add("376EA(4)", (8598, 8599), "imprisonment for a term which may extend to 5 years, or with fine, or with both", "IMP_FINE_BOTH", 5)
add("376EB(3)(a)", (8631, 8636), "imprisonment for a term which may extend to 3 years, or with fine, or with both", "IMP_FINE_BOTH", 3)
add("376EB(3)(b)", (8638, 8639), "imprisonment for a term which may extend to 2 years, or with fine, or with both", "IMP_FINE_BOTH", 2)
add("376EC(3)", (8680, 8681), "imprisonment for a term which may extend to 2 years, or with fine, or with both", "IMP_FINE_BOTH", 2)
add("376ED(3)(a)", (8727, 8732), "imprisonment for a term which may extend to 3 years, or with fine, or with both", "IMP_FINE_BOTH", 3)
add("376ED(3)(b)", (8734, 8736), "imprisonment for a term which may extend to 2 years, or with fine, or with both", "IMP_FINE_BOTH", 2)
add("376EE(3)", (8793, 8795), "imprisonment for a term which may extend to 2 years, or with fine, or with both", "IMP_FINE_BOTH", 2)
add("376F(2)", (8822, 8824), "imprisonment for a term which may extend to 5 years, or with fine, or with caning, or with any combination of such punishments", "IMP_FINE_CANE_COMB", 5)
add("376F(3)", (8835, 8837), "imprisonment for a term which may extend to 20 years, and shall also be liable to a fine or to caning", "IMP_ALSO_FINE_CANE", 20)
add("376G(3)", (8882, 8883), "imprisonment for a term which may extend to 5 years", "IMP_ONLY", 5)
add("376H(2)(a)", (8942, 8953), "imprisonment for a term which may extend to 10 years, or with fine, or with caning, or any combination of such punishments", "IMP_FINE_CANE_COMB", 10)
add("376H(2)(b)", (8955, 8956), "imprisonment for a term which may extend to 2 years, or with fine, or with both", "IMP_FINE_BOTH", 2)
add("377(2)", (9010, 9012), "imprisonment for a term that may extend to 5 years, or with fine, or with both", "IMP_FINE_BOTH", 5)
add("377(3)", (9014, 9018), "imprisonment for a term that may extend to 20 years, and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 20)
add("377B(2)", (9035, 9036), "imprisonment for a term which may extend to 2 years, or with fine, or with both", "IMP_FINE_BOTH", 2)
add("377B(4)", (9048, 9050), "imprisonment for a term which may extend to 20 years, and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 20)
add("377BB(7)", (9133, 9135), "imprisonment for a term which may extend to 2 years, or with fine, or with caning, or with any combination of such punishments", "IMP_FINE_CANE_COMB", 2)
add("377BB(8)", (9139, 9141), "imprisonment for a term which may extend to 2 years and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 2)
add("377BC(3)", (9181, 9186), "imprisonment for a term which may extend to 5 years, or with fine, or with caning, or any combination of such punishments", "IMP_FINE_CANE_COMB", 5)
add("377BC(4)", (9190, 9193), "imprisonment for a term which may extend to 5 years, and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 5)
add("377BD(2)", (9220, 9222), "imprisonment for a term which may extend to 2 years, or with fine, or with both", "IMP_FINE_BOTH", 2)
add("377BD(3)", (9227, 9230), "imprisonment for a term which may extend to 2 years, and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 2)
add("377BD(6)", (9263, 9265), "imprisonment for a term which may extend to 2 years, or with fine, or with both", "IMP_FINE_BOTH", 2)
add("377BD(7)", (9269, 9272), "imprisonment for a term which may extend to 2 years, and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 2)
add("377BE(3)", (9316, 9319), "imprisonment for a term which may extend to 5 years, or with fine, or with caning, or with any combination of such punishments", "IMP_FINE_CANE_COMB", 5)
add("377BE(4)", (9323, 9325), "imprisonment for a term which may extend to 5 years and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 5)
add("377BF(3)", (9397, 9399), "imprisonment for a term which may extend to one year, or with fine, or with both", "IMP_FINE_BOTH", 1)
add("377BF(4)", (9403, 9405), "imprisonment for a term which may extend to 2 years, and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 2)
add("377BG(2)", (9423, 9425), "imprisonment for a term which may extend to 10 years, and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 10)
add("377BH(2)", (9457, 9459), "imprisonment for a term which may extend to 10 years, and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 10)
add("377BI(2)", (9487, 9489), "imprisonment for a term which may extend to 7 years, and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 7)
add("377BJ(3)", (9513, 9515), "imprisonment for a term which may extend to 5 years, and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 5)
add("377BK(2)", (9541, 9543), "imprisonment for a term which may extend to 5 years, and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 5)
add("377BL(2)", (9578, 9580), "imprisonment for a term which may extend to 10 years, and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 10)
add("377BL(3)", (9584, 9586), "imprisonment for a term which may extend to 10 years, and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 10)
add("377BL(4)", (9590, 9594), "imprisonment for a term which may extend to 7 years, and shall also be liable to fine or to caning", "IMP_ALSO_FINE_CANE", 7)


def opt(v):
    return "NOTHING" if v is None else "JUST %d" % v


def render(label, d):
    a, b = d["lines"]
    out = []
    out.append("@ref Penal Code 1871 s %s (src:%d-%d)" % (d["label"], a, b))
    out.append("`punishment prescribed by s %s` MEANS Punishment WITH" % d["label"])
    out.append('    section                  IS "%s"' % d["label"])
    out.append('    words                    IS "%s"' % d["words"])
    out.append("    death                    IS %s" % d["death"])
    out.append("    `imprisonment for life`  IS %s" % d["life"])
    out.append("    imprisonment             IS %s" % d["imp"])
    out.append("    `maximum term in months` IS %s" % opt(d["mx"]))
    out.append("    `minimum term in months` IS %s" % opt(d["mn"]))
    out.append("    `forfeiture of property` IS %s" % d["forf"])
    out.append("    fine                     IS %s" % d["fine"])
    out.append("    `maximum fine`           IS %s" % opt(d["maxfine"]))
    out.append("    `minimum fine`           IS %s" % opt(d["minfine"]))
    out.append("    caning                   IS %s" % d["cane"])
    out.append("    `minimum strokes`        IS %s" % opt(d["minstr"]))
    out.append("    `maximum strokes`        IS %s" % opt(d["maxstr"]))
    out.append("    `or with both`           IS %s" % ("TRUE" if d["both"] else "FALSE"))
    out.append("")
    return out
