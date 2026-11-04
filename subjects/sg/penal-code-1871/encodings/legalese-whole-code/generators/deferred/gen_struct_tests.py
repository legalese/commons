#!/usr/bin/env python3
"""Write the structural tests of the generated offences and definitions, as a gen_tests.py template.

Usage (from the encoding folder):
    python3 -I generators/deferred/gen_struct_tests.py OFFENCE_SPEC.py [DEFS_SPEC.py] > TEMPLATE.tests.in

For every flat offence in the offence spec (no record-typed leaf), and for each of its elements (a conjunct of
its definition, written from the Code's text in the spec), the template asserts:

  - a minimal set of facts that satisfies every element makes the offence made out, the charge `made out`,
    with the section, the offence's name and the punishment the Code states;
  - with any one element made not true the offence is not made out, and the charge refuses (no text, a refusal);
  - with every leaf FALSE the offence is not made out.

For every definition in the definitions spec, by its shape (means / if / includes / limited / flat):
  JUST TRUE where the condition holds, JUST FALSE or NOTHING where it does not, as the shape says.

What this does and does not do: the expectations come from the elements as the spec states them, which were written
from the Code's text, not from any output of the compiler.  It tests that the generated L4 says what the spec says
(wiring, punishment choice, refusal); it cannot find a spec that misreads the text.  The tests of that kind are the
hand-written ones (Illustrations, boundary cases, readings) in the extra files.
"""
import importlib.util
import itertools
import re
import sys

HERE = __file__.rsplit("/", 1)[0]
sys.path.insert(0, HERE)
from punish import PUNISH  # noqa: E402


def load(path):
    sp = importlib.util.spec_from_file_location("m" + str(abs(hash(path))), path)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


# ------------------------------------------------------------------ a tiny boolean formula over [leaf] atoms
TOK = re.compile(r"\[[^\]]+\]|\(|\)|\bAND\b|\bOR\b|\bNOT\b")


def parse(s):
    toks = TOK.findall(s)
    pos = [0]

    def peek():
        return toks[pos[0]] if pos[0] < len(toks) else None

    def eat():
        t = toks[pos[0]]
        pos[0] += 1
        return t

    def p_or():
        xs = [p_and()]
        while peek() == "OR":
            eat()
            xs.append(p_and())
        return xs[0] if len(xs) == 1 else ("or", xs)

    def p_and():
        xs = [p_not()]
        while peek() == "AND":
            eat()
            xs.append(p_not())
        return xs[0] if len(xs) == 1 else ("and", xs)

    def p_not():
        if peek() == "NOT":
            eat()
            return ("not", p_not())
        return p_atom()

    def p_atom():
        t = eat()
        if t == "(":
            n = p_or()
            assert eat() == ")"
            return n
        assert t.startswith("["), (t, s)
        return ("leaf", t[1:-1])

    n = p_or()
    assert peek() is None, ("trailing tokens in", s)
    return n


CAP = 12


def merge(a, b):
    out = dict(a)
    for k, v in b.items():
        if k in out and out[k] != v:
            return None
        out[k] = v
    return out


def sols(node, want=True):
    """Partial assignments {leaf: bool} under which node evaluates to want."""
    kind = node[0]
    if kind == "leaf":
        return [{node[1]: want}]
    if kind == "not":
        return sols(node[1], not want)
    kids = node[1]
    conj = (kind == "and") == want  # and/true  or  or/false  need every child
    if conj:
        acc = [{}]
        for k in kids:
            ks = sols(k, want)
            nxt = []
            for a in acc:
                for b in ks:
                    m = merge(a, b)
                    if m is not None:
                        nxt.append(m)
            acc = nxt[:CAP]
        return acc
    out = []
    for k in kids:
        out.extend(sols(k, want))
    return out[:CAP]


def leaves_of(node):
    if node[0] == "leaf":
        return [node[1]]
    if node[0] == "not":
        return leaves_of(node[1])
    return [x for k in node[1] for x in leaves_of(k)]


def children_and(node):
    return node[1] if node[0] == "and" else [node]


# ------------------------------------------------------------------ output
out = []
W = out.append
seen = {}


def qn(s):
    return "`%s`" % s


def fixture(rec, tag, assign, all_leaves, extra=None):
    key = (rec, tag.split(" ")[0], frozenset(k for k, v in assign.items() if v), frozenset((extra or {}).items()))
    if key in seen:
        return seen[key]
    name = "%s %s" % (rec_short(rec), tag)
    seen[key] = name
    W("-- @fixture %s OF %s" % (qn(name), qn(rec)))
    W('-- S victim = "Lim Mei Ling"')
    W('-- S the manner = "by the act charged"')
    for lf in all_leaves:
        if assign.get(lf):
            W("-- T %s" % lf)
    for k, v in (extra or {}).items():
        W("-- T %s" % k)
    W("-- @end")
    return name


def rec_short(rec):
    return rec.replace(" Facts", "")


def words(pid):
    return PUNISH[pid]["words"]


def esc(s):
    return s.replace('"', '\\"')


def offence_tests(S):
    rec = S["record"]
    simple = all(len(lf) < 3 or lf[2] in ("BOOLEAN", "STRING", "NUMBER") for lf in S["leaves"])
    if not simple:
        W("-- (%s has a record-typed leaf: tested by hand below)" % S["sec"])
        return
    all_leaves = [lf[0] for lf in S["leaves"]]
    defs = {d["name"]: d for d in S["defs"]}
    for O in S["offences"]:
        lab = O["label"]
        m = re.match(r"^`([^`]+)` f(.*)$", O["defn"].strip())
        dn, rest = m.group(1), m.group(2)
        conjs = [parse(c[1]) for c in defs[dn]["conj"]]
        for part in [p for p in rest.split(" AND ") if p.strip()]:
            conjs.append(parse(part.strip()))
        W("")
        W("-- s %s: %s" % (lab, O["charge_name"]))
        # positives: one fixture per alternative of the widest "or" among the elements, so that every limb is met
        cs_list = [sols(c, True) for c in conjs]
        n = max(len(cs) for cs in cs_list)
        acc = []
        for i in range(n):
            a = {}
            for cs in cs_list:
                pick = None
                for off in range(len(cs)):
                    m2 = merge(a, cs[(i + off) % len(cs)])
                    if m2 is not None:
                        pick = m2
                        break
                assert pick is not None, ("unsatisfiable", lab)
                a = pick
            if not any(frozenset(k for k, v in a.items() if v) == frozenset(k for k, v in b.items() if v) for b in acc):
                acc.append(a)
        assert acc, ("unsatisfiable", lab)
        # a punishment choice, if the charge picks between two records on one leaf
        pc = re.match(r"^IF (.+?) THEN `punishment prescribed by s (.+?)`'s words ELSE `punishment prescribed by s (.+?)`'s words$", O["punish_expr"])
        pcond = parse(pc.group(1)) if pc else None
        pids = O["punish"]
        for k, base in enumerate(acc[:10]):
            variants = [("", {}, pids[0] if len(pids) == 1 else None)]
            if pc:
                va = [x for x in (merge(base, y) for y in sols(pcond, True)) if x is not None]
                vb = [x for x in (merge(base, y) for y in sols(pcond, False)) if x is not None]
                assert va and vb, ("punishment condition not independent of the elements", lab)
                variants = [(" a", va[0], pc.group(2)), (" b", vb[0], pc.group(3))]
            for (suf, ov, pid) in variants:
                a = dict(ov) if ov else dict(base)
                tag = "%s via %d%s" % (lab, k + 1, suf)
                f = fixture(rec, tag, a, all_leaves)
                W("#ASSERT %s %s" % (qn("offence under s " + lab), qn(f)))
                ch = "(%s %s)" % (qn("charge under s " + lab), qn(f))
                W("#ASSERT %s's `made out`" % ch)
                W('#ASSERT %s\'s section EQUALS "%s"' % (ch, lab))
                W('#ASSERT %s\'s offence EQUALS "%s"' % (ch, esc(O["charge_name"])))
                if pid:
                    W('#ASSERT %s\'s punishment EQUALS "%s"' % (ch, esc(words(pid))))
                W('#ASSERT NOT (%s\'s text EQUALS "")' % ch)
                W('#ASSERT %s\'s refusal EQUALS ""' % ch)
        base = acc[0]
        # negatives: each element made false
        for i, c in enumerate(conjs):
            fs = sols(c, False)
            # the way of making this element untrue that disturbs the other elements least
            best = min(fs, key=lambda x: sum(1 for k, v in x.items() if base.get(k) and not v))
            a = dict(base)
            a.update(best)
            f = fixture(rec, "%s without element %d" % (lab, i + 1), a, all_leaves)
            W("#ASSERT NOT (%s %s)" % (qn("offence under s " + lab), qn(f)))
            ch = "(%s %s)" % (qn("charge under s " + lab), qn(f))
            W("#ASSERT NOT (%s's `made out`)" % ch)
            W('#ASSERT %s\'s text EQUALS ""' % ch)
            W('#ASSERT NOT (%s\'s refusal EQUALS "")' % ch)
        f = fixture(rec, "%s nothing established" % lab, {}, all_leaves)
        W("#ASSERT NOT (%s %s)" % (qn("offence under s " + lab), qn(f)))
        ch = "(%s %s)" % (qn("charge under s " + lab), qn(f))
        W("#ASSERT NOT (%s's `made out`)" % ch)


def def_tests(D):
    names = [p[0] for p in D["params"]]
    fn = qn(D["name"])

    def call(assign):
        return "%s %s" % (fn, " ".join("TRUE" if assign.get(n) else "FALSE" for n in names))

    W("")
    W("-- %s" % D["name"])
    shape = D["shape"]
    if shape == "flat":
        W("#ASSERT %s EQUALS JUST FALSE" % call({}))
        W("#ASSERT %s EQUALS JUST FALSE" % call({n: True for n in names}))
        return
    f = parse(D["expr"])
    pos = sols(f, True)
    for a in pos[:3]:
        W("#ASSERT %s EQUALS JUST TRUE" % call(a))
    neg_val = "JUST FALSE" if shape in ("means", "if") else "NOTHING"
    W("#ASSERT %s EQUALS %s" % (call({}), neg_val))
    base = pos[0]
    for c in children_and(f):
        fs = sols(c, False)
        best = min(fs, key=lambda x: sum(1 for k, v in x.items() if base.get(k) and not v))
        a = dict(base)
        a.update(best)
        W("#ASSERT %s EQUALS %s" % (call(a), neg_val))


def main():
    offs = load(sys.argv[1])
    for S in offs.SECTIONS:
        if "record" in S:
            W("")
            W("§§ `s %s`" % S["sec"])
            offence_tests(S)
    if len(sys.argv) > 2:
        defs = load(sys.argv[2])
        cur = None
        for D in defs.DEFS:
            if D["sec"] != cur:
                cur = D["sec"]
                W("")
                W("§§ `definitions and rules of reading under s %s`" % cur)
            def_tests(D)
    print("\n".join(out))


main()
