#!/usr/bin/env python3
"""Coverage table for Terrorism Act 2000, Part III, built from the deposited text by script.

  python3 -I coverage.py RAW [--map coverage-map.tsv] [--rows] [--audit] [--table] [--notes NOTES.md]

RAW is inputs/ukpga-2000-11-part-3.txt (it is not copied into this folder).

One row for every heading, section, subsection, paragraph, sub-paragraph, defined term and list item.
Every non-blank line of RAW belongs to exactly one row (its own line, plus any unlabelled
continuation lines that follow it); --audit proves it.

The map (coverage-map.tsv) has one line per row that is not simply the same as its parent:
    label TAB disposition TAB pointer TAB note
disposition is encoded | inert | fork | repealed.  A row with no map line takes its parent's
disposition and pointer.  A row with no map line and no mapped ancestor is `deferred`.
pointer:  encoded -> the L4 rule names (separated by ` ;; `) that implement the row;
          inert   -> the reason number 1, 2 or 3 (see the brief);
          fork    -> F<n>, then ` ;; `, then the rule names (or `not covered`);
          repealed-> what the text shows.

--audit also checks every `encoded` pointer: each rule name must be DEFINED in a ta-*.l4 file here
and must appear in at least one #ASSERT or #EVAL of a ta-cases-*.l4 or ta-tests-*.l4 file.
"""
import re, sys, os, glob, argparse, collections

ROMAN = {"i", "ii", "iii", "iv", "v", "vi", "vii", "viii"}


def parse(raw_path):
    lines = open(raw_path, encoding="utf-8").read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    rows = []          # dicts
    stack = {}         # level name -> row
    cur_sec = None

    def add(label, kind, start, parent, text):
        r = dict(label=label, kind=kind, start=start, end=start, parent=parent, text=text)
        rows.append(r)
        return r

    sec = sub = para = subp = None
    item_mode = False
    defn = None
    prev_para_label = None
    for i, line in enumerate(lines, 1):
        if line.strip() == "":
            continue
        m_head = re.match(r"^\t(.+)$", line)
        m_sec = re.match(r"^(\d+[A-Z]*)\t(.*)$", line)
        m_sub = re.match(r"^\((\d+[A-Z]*)\)\s(.*)$", line)
        m_par = re.match(r"^\(([a-z]+)\)\s(.*)$", line)
        if m_head:
            add("heading: " + m_head.group(1).strip(), "heading", i, None, m_head.group(1).strip())
            sec = sub = para = subp = defn = None
            item_mode = False
            continue
        if m_sec:
            num, title = m_sec.group(1), m_sec.group(2)
            kind = "repealed" if re.fullmatch(r"[ .]+", title) else "section"
            sec = add("s " + num, kind, i, None, title if kind == "section" else "(repealed: dots only)")
            sub = para = subp = defn = None
            item_mode = False
            prev_para_label = None
            continue
        if m_sub:
            sub = add(sec["label"] + "(" + m_sub.group(1) + ")", "subsection", i, sec, m_sub.group(2))
            para = subp = defn = None
            item_mode = False
            prev_para_label = None
            continue
        if m_par:
            lab = m_par.group(1)
            is_roman = lab in ROMAN and not (lab == "i" and prev_para_label == "h") and para is not None
            if is_roman:
                parent = para
                subp = add(para["label"] + "(" + lab + ")", "sub-paragraph", i, parent, m_par.group(2))
            else:
                parent = sub if sub is not None else sec
                para = add(parent["label"] + "(" + lab + ")", "paragraph", i, parent, m_par.group(2))
                subp = None
                prev_para_label = lab
            defn = None
            item_mode = line.rstrip().endswith("—")
            continue
        # unlabelled line
        st = line.strip()
        if st.startswith("“") or st.startswith('"'):
            parent = sub if sub is not None else sec
            term = re.match(r"^[“\"]\s*([^”\"]+?)\s*[”\"]", st)
            name = term.group(1) if term else st[:20]
            defn = add(parent["label"] + " “" + name + "”", "definition", i, parent, st)
            item_mode = st.endswith("—")
            continue
        if item_mode:
            owner = defn if defn is not None else (subp or para or sub or sec)
            n = sum(1 for r in rows if r["kind"] == "item" and r["parent"] is owner) + 1
            add(owner["label"] + " item " + str(n), "item", i, owner, st)
            if not (st.endswith(";") or st.endswith(",") or st.endswith(", or") or st.endswith("or")):
                # a final item ends the list when it ends the sentence
                if st.endswith("."):
                    item_mode = False
            continue
        # continuation (tail) line: belongs to the row that is open
        owner = rows[-1]
        owner["end"] = i
    # Defined terms and labels that sit inside a row's own text become rows of their own (kind "term").
    # They own no lines (the row that holds the sentence owns them), so the line audit ignores them.
    terms = []
    for r in rows:
        if r["kind"] in ("heading", "repealed", "definition", "item"):
            continue
        body = " ".join(lines[r["start"] - 1:r["end"]])
        seen = set()
        for m in re.finditer(r"[\u201c\"]\s*([^\u201d\"]{2,60}?)\s*[\u201d\"]", body):
            t = m.group(1).strip()
            if t in seen:
                continue
            seen.add(t)
            terms.append(dict(label=r["label"] + " term \u201c" + t + "\u201d", kind="term", start=r["start"], end=r["end"],
                              parent=r, text=t, virtual=True))
    rows.extend(terms)
    rows.sort(key=lambda r: (r["start"], 0 if not r.get("virtual") else 1))
    return lines, rows


def inherit(rows, mp):
    out = {}
    for r in rows:
        lab = r["label"]
        node = r
        got = None
        while node is not None:
            if node["label"] in mp:
                got = mp[node["label"]]
                break
            node = node["parent"]
        if r["kind"] == "heading" and got is None:
            got = ("inert", "1", "heading")
        if r["kind"] == "repealed" and got is None:
            got = ("repealed", "blank in this text", "section number with nothing under it")
        out[lab] = got if got else ("deferred", "", "")
    return out


def load_map(path):
    mp = {}
    if not path or not os.path.exists(path):
        return mp
    for ln, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            sys.exit("%s:%d: need label TAB disposition TAB pointer" % (path, ln))
        lab, disp, ptr = parts[0], parts[1], parts[2]
        note = parts[3] if len(parts) > 3 else ""
        if disp not in ("encoded", "inert", "fork", "repealed"):
            sys.exit("%s:%d: bad disposition %r" % (path, ln, disp))
        mp[lab] = (disp, ptr, note)
    return mp


def defined_names(l4dir):
    names = {}
    for f in sorted(glob.glob(os.path.join(l4dir, "ta-*.l4"))):
        if os.path.basename(f).startswith(("ta-tests-", "ta-cases-")):
            continue
        txt = open(f, encoding="utf-8").read()
        for m in re.finditer(r"^(?:DECIDE\s+)?(`[^`]+`)(?=\s+(?:MEANS|IS|IF)\b|\s+[A-Za-z`])", txt, re.M):
            names.setdefault(m.group(1).strip("`"), os.path.basename(f))
        for m in re.finditer(r"^(?:DECIDE\s+)?`([^`]+)`", txt, re.M):
            names.setdefault(m.group(1), os.path.basename(f))
    return names


def resolve(ptr_item, names):
    """A pointer item is a rule name or a prefix: `s 14(1)` stands for every rule named `s 14(1) ...`."""
    it = ptr_item.strip()
    if it in names:
        return [it]
    return sorted(n for n in names if n.startswith(it + " "))


def test_text(l4dir):
    t = []
    for f in sorted(glob.glob(os.path.join(l4dir, "ta-cases-*.l4")) + glob.glob(os.path.join(l4dir, "ta-tests-*.l4"))):
        t.append(open(f, encoding="utf-8").read())
    return "\n".join(t)


def audit(lines, rows, disp, l4dir, strict_names):
    problems = []
    owner = {}
    for r in rows:
        if r.get("virtual"):
            continue
        for ln in range(r["start"], r["end"] + 1):
            if ln in owner:
                problems.append("line %d owned twice: %s and %s" % (ln, owner[ln], r["label"]))
            owner[ln] = r["label"]
    nonblank = [i for i, l in enumerate(lines, 1) if l.strip()]
    missing = [i for i in nonblank if i not in owner]
    for i in missing:
        problems.append("line %d has no row" % i)
    deferred = [r["label"] for r in rows if disp[r["label"]][0] == "deferred"]
    for d in deferred:
        problems.append("row still deferred: " + d)
    names = defined_names(l4dir) if l4dir else {}
    tt = test_text(l4dir) if l4dir else ""
    checked = set()
    if strict_names:
        for r in rows:
            d, ptr, _ = disp[r["label"]]
            if d not in ("encoded", "fork"):
                continue
            rules = ptr.split(" ;; ")
            if d == "fork":
                rules = rules[1:]
            for item in rules:
                item = item.strip()
                if not item or item == "not covered":
                    continue
                got = resolve(item, names)
                if not got:
                    problems.append("%s: no rule named or prefixed `%s` in any ta-*.l4" % (r["label"], item))
                for nm in got:
                    if nm in checked:
                        continue
                    checked.add(nm)
                    if ("`" + nm + "`") not in tt:
                        problems.append("%s: rule defined but never used in a ta-cases-/ta-tests- file: `%s`" % (r["label"], nm))
    return nonblank, owner, problems, checked


def ledgers(l4dir):
    """Scan the layer-1 and layer-2 modules for FALSE-kind and NOTHING-kind tags; return (marginal table, reason counts)."""
    rows = []
    for f in sorted(glob.glob(os.path.join(l4dir, "ta-*.l4"))):
        base = os.path.basename(f)
        if base.startswith(("ta-tests-", "ta-cases-")):
            continue
        cur = ""
        for ln, line in enumerate(open(f, encoding="utf-8"), 1):
            m = re.match(r"^(?:DECIDE\s+)?`([^`]+)`", line)
            if m and not line.startswith("--"):
                cur = m.group(1)
            m = re.search(r"--\s*(FALSE|NOTHING)-kind\s*\(([^)]*)\)\s*:?\s*(.*)$", line)
            if m:
                kind, why, quote = m.group(1), m.group(2), m.group(3).strip()
                rows.append((base, ln, cur, kind, why, quote))
    out = ["| rule | where | tag | the text's words | other reading |", "|---|---|---|---|---|"]
    counts = collections.Counter()
    for base, ln, cur, kind, why, quote in rows:
        if kind == "FALSE":
            ql = quote.lower()
            if re.search(r"\b(means|is a reference to|has the meaning|has the same meaning)\b", ql) and not re.search(r"\bif\b", ql):
                reading = "a definition that says it means (not marginal)"
                other = "-"
            else:
                reading = "M1: a failed \u201cif\u201d, \u201cwhere\u201d, \u201cis that\u201d or \u201cmust\u2014\u201d condition, or a flat negative, counts as the text\u2019s no"
                other = "the text is silent on the case that fails the condition: NOTHING-kind (silent)"
            counts["FALSE " + reading.split(":")[0]] += 1
        else:
            if "limited by its own wording" in why:
                reading = "M2: a grant or prohibition limited by its own wording does not give a no"
                other = "the case outside the limit is the text\u2019s no: JUST FALSE"
            else:
                reading = "NOTHING (" + why + ")"
                other = "-"
            counts["NOTHING " + reading.split(":")[0].split(" (")[0] + (" " + why if reading.startswith("NOTHING") else "")] += 1
        out.append("| `%s` | %s:%d | %s | %s | %s |" % (cur.replace("|", "/"), base, ln, reading, quote.replace("|", "/"), other))
    return "\n".join(out), counts, len(rows)


def jural(path):
    if not os.path.exists(path):
        return "(no rows yet)"
    out = ["| provision | holder of the right, privilege, power or immunity | kind | bearer of the correlative duty, no-right, liability or disability | correlative | L4 rule |", "|---|---|---|---|---|---|"]
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        parts = (line.split("\t") + [""] * 6)[:6]
        out.append("| " + " | ".join(x.replace("|", "/") for x in parts) + " |")
    return "\n".join(out)


def replace_block(body, tag, text):
    b, e = "<!-- %s:BEGIN -->" % tag, "<!-- %s:END -->" % tag
    if b not in body or e not in body:
        sys.exit("NOTES.md has no %s markers" % tag)
    return body.split(b)[0] + b + "\n\n" + text + "\n\n" + e + body.split(e)[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("raw")
    ap.add_argument("--map", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "coverage-map.tsv"))
    ap.add_argument("--rows", action="store_true", help="print the parsed rows")
    ap.add_argument("--audit", action="store_true")
    ap.add_argument("--names", action="store_true", help="with --audit: also check encoded rule names")
    ap.add_argument("--table", action="store_true", help="print the markdown coverage table")
    ap.add_argument("--notes", help="rewrite the block between the COVERAGE markers in this NOTES.md")
    a = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    lines, rows = parse(a.raw)
    mp = load_map(a.map)
    disp = inherit(rows, mp)
    if a.rows:
        for r in rows:
            print("%4d-%-4d %-14s %-34s %s" % (r["start"], r["end"], r["kind"], r["label"], r["text"][:60]))
    counts = collections.Counter(disp[r["label"]][0] for r in rows)
    if a.audit or a.table or a.notes:
        nonblank, owner, problems, checked = audit(lines, rows, disp, here, a.names)
        summary = ("text lines: %d (non-blank %d); rows: %d; lines owned by exactly one row: %d; "
                   "encoded %d, inert %d, fork %d, repealed %d, deferred %d"
                   % (len(lines), len(nonblank), len(rows), len(owner), counts["encoded"], counts["inert"],
                      counts["fork"], counts["repealed"], counts["deferred"]))
        inert_by = collections.Counter(disp[r["label"]][1] for r in rows if disp[r["label"]][0] == "inert")
        summary += "; inert by reason " + ", ".join("%s: %d" % (k, v) for k, v in sorted(inert_by.items()))
        if a.audit:
            print(summary)
            print("encoded rule names checked: %d" % len(checked))
            for p in problems:
                print("PROBLEM:", p)
            print("audit problems: %d" % len(problems))
    if a.table or a.notes:
        names_all = defined_names(here)
        out = []
        out.append("| text lines | row | kind | disposition | where |")
        out.append("|---|---|---|---|---|")
        for r in rows:
            d, ptr, note = disp[r["label"]]
            if d == "inert":
                where = "reason " + ptr + (": " + note if note else "")
            elif d == "fork":
                where = ptr.replace(" ;; ", " ; ")
            elif d == "repealed":
                where = ptr
            else:
                where = ptr.replace(" ;; ", " ; ")
            if d in ("encoded", "fork") and names_all:
                items = ptr.split(" ;; ")
                if d == "fork":
                    where = items[0] + " ; "
                    items = items[1:]
                else:
                    where = ""
                full = []
                for it in items:
                    got = resolve(it, names_all)
                    full.extend(("`" + g + "`") for g in got) if got else full.append(it.strip())
                where += " ; ".join(full)
            if note and d in ("encoded", "fork"):
                where += " ; " + note
            where = where.replace("|", "/")
            rng = str(r["start"]) if r["end"] == r["start"] else "%d-%d" % (r["start"], r["end"])
            out.append("| %s | %s | %s | %s | %s |" % (rng, r["label"], r["kind"], d, where))
        table = "\n".join(out)
        if a.table:
            print(table)
        if a.notes:
            body = open(a.notes, encoding="utf-8").read()
            b, e = "<!-- COVERAGE:BEGIN -->", "<!-- COVERAGE:END -->"
            if b not in body or e not in body:
                sys.exit("%s has no COVERAGE markers" % a.notes)
            pre = body.split(b)[0]
            post = body.split(e)[1]
            new = pre + b + "\n\n" + "Counts, from `coverage.py --audit`: " + summary + ".\n\n" + table + "\n\n" + e + post
            open(a.notes, "w", encoding="utf-8").write(new)
            print("wrote coverage table to", a.notes)
            tbl, cnt, n = ledgers(here)
            body = open(a.notes, encoding="utf-8").read()
            sumry = "Generated by `coverage.py` from the `-- FALSE-kind` and `-- NOTHING-kind` comments in the modules (%d tagged branches): " % n + "; ".join("%s: %d" % (k, v) for k, v in sorted(cnt.items())) + "."
            body = replace_block(body, "MARGINAL", sumry + "\n\n" + tbl)
            body = replace_block(body, "JURAL", jural(os.path.join(here, "jural.tsv")))
            open(a.notes, "w", encoding="utf-8").write(body)
            print("wrote marginal readings (%d branches) and jural relations" % n)


if __name__ == "__main__":
    main()
