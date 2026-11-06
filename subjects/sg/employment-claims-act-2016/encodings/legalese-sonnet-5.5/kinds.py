#!/usr/bin/env python3
"""Lint and list the FALSE and NOTHING branches of the layer-1 modules.

usage:  python3 -I kinds.py lint       every JUST FALSE or NOTHING result has a FALSE-kind or NOTHING-kind comment on it on its line, the next line or the two lines above it
        python3 -I kinds.py marginal   print the "Marginal readings for a lawyer" table rows
        python3 -I kinds.py ruled      print the table of the sites decided by the rulings of 2026-11-05 (I(a), I(b), I(c), II(c), II(d))
        python3 -I kinds.py sites W    print one line per branch of class W (w: the "when" assumption; o: the open questions), for the fork register
        python3 -I kinds.py counts     counts of branches by kind

A branch is a line that ends a result with `JUST FALSE` or is a result `NOTHING`
(not an `EQUALS NOTHING` inside a test, and not the word in a comment).
The table of marginal readings follows the brief: reading (a) is a failed "if"-type condition or a flat negative counted as the text's no.
Reading (b), a limited grant or prohibition whose case falls outside the limit, was ruled on 2026-11-05 (Meng): (a) a period the text fixes in its own words, outside it JUST FALSE;
(b) a "where" condition not met, JUST FALSE; (c) a scope limit with no "only", NOTHING outside the scope.
A NOTHING that says `limited by its own wording` therefore carries one of three tags, which this script reads:
`[scope limit, ruled I(c)]`, `[no yes-or-no]` (the function returns a value, so there is no JUST FALSE to give) or `[open question...]` (a scope limit the review expected to be JUST FALSE).
A JUST FALSE that rests on the ruling or on the assumption below carries `[ruled I(a)]`, `[ruled I(b)]` or `[assumed: when]`.
Assumed, not ruled: "when", "upon", "after an event", "on the application of" and "whenever" are read as "where".
A "means" definition or a list closed with "only" is the text's own no and is not marginal.
"""
import re, sys, glob, os, collections

WHYS = ["silent", "list not closed", "includes", "undefined term", "points outside the text", "limited by its own wording"]
COND = re.compile(r"\b(if|only if|as long as|so long as|while|until|unless|except|save|provided that|provided)\b", re.I)
FLAT = re.compile(r"\b(does not|do not|shall not|may not|cannot|must not|is not entitled|is not|are not|need not|no liability)\b", re.I)
CLOSED = re.compile(r"\b(means|only|nothing but)\b", re.I)

def layer1_files(folder):
    out = []
    for f in sorted(glob.glob(os.path.join(folder, "eca-*.l4"))):
        b = os.path.basename(f)
        if re.match(r"eca-(tests|cases|seat)", b) or b == "eca-nouns.l4":
            continue
        out.append(f)
    return out

def strip_comment(line):
    i = line.find("--")
    return line if i < 0 else line[:i]

RESULT = re.compile(r"(THEN|ELSE|OTHERWISE)\s+(JUST\b|NOTHING\b|TRUE\b|FALSE\b|`)")

def find_comment(L, k, want):
    """The comment that belongs to the branch on line k: on the line itself, or in the comment lines directly above it.
    The search climbs past lines of code that are not themselves a result (the IF line of a three-line branch) and past
    a result of the same kind (consecutive branches under one comment, the idiom of a CONSIDER whose arms share a reason);
    a result of the other kind ends it.  Only as a last resort is the line below looked at."""
    if want in L[k]:
        return L[k][L[k].index(want) - 3:].strip() if "--" in L[k] else None
    for j in range(k - 1, max(k - 5, -1), -1):
        if want in L[j]:
            return L[j].strip()
        if L[j].strip().startswith("--"):
            continue
        code = strip_comment(L[j])
        if RESULT.search(code):
            same = ("FALSE" in want and re.search(r"\bJUST FALSE\b", code)) or ("NOTHING" in want and re.search(r"(THEN|ELSE|OTHERWISE)\s+NOTHING\b", code))
            if not same:
                break
    if k + 1 < len(L) and want in L[k + 1] and not RESULT.search(strip_comment(L[k + 1])):
        return L[k + 1].strip()
    return None

def scan(folder):
    """yield (file, lineno, fname, kind('F' or 'N'), comment-or-None, text)"""
    rows = []
    for f in layer1_files(folder):
        L = open(f, encoding="utf-8").read().split("\n")
        fname = None
        for k, line in enumerate(L):
            m = re.match(r"^`([^`]+)` MEANS", line)
            if m:
                fname = m.group(1)
            code = strip_comment(line)
            code = re.sub(r"EQUALS\s+(JUST\s+(TRUE|FALSE)|NOTHING)", "", code)
            kinds = []
            if re.search(r"\bJUST FALSE\b", code):
                kinds.append("F")
            if re.search(r"(THEN|ELSE|->|MEANS|\bIS|OTHERWISE)\s+NOTHING\b", code) or re.fullmatch(r"\s*NOTHING\s*", code):
                kinds.append("N")
            for kind in kinds:
                want = "FALSE-kind" if kind == "F" else "NOTHING-kind"
                cm = find_comment(L, k, want)
                rows.append((os.path.basename(f), k + 1, fname, kind, cm, line.strip()))
    return rows

def lint(folder):
    rows = scan(folder)
    bad = [r for r in rows if r[4] is None]
    for r in bad:
        print(f"MISSING {r[3]}-kind comment: {r[0]}:{r[1]} in `{r[2]}`: {r[5][:100]}")
    badwhy = [r for r in rows if r[3] == "N" and r[4] and not any(w in r[4] for w in WHYS)]
    for r in badwhy:
        print(f"NOTHING-kind comment names no allowed reason: {r[0]}:{r[1]} in `{r[2]}`: {r[4][:120]}")
    badq = [r for r in rows if r[3] == "F" and r[4] and '"' not in r[4]]
    for r in badq:
        print(f"FALSE-kind comment quotes nothing: {r[0]}:{r[1]} in `{r[2]}`: {r[4][:120]}")
    notag = [r for r in rows if r[3] == "N" and r[4] and "limited by its own wording" in r[4] and not any(w in r[4] for w in ("[scope limit, ruled I(c)]", "[no yes-or-no]", "[open question"))]
    for r in notag:
        print(f"NOTHING-kind (limited by its own wording) carries none of [scope limit, ruled I(c)], [no yes-or-no], [open question...]: {r[0]}:{r[1]} in `{r[2]}`")
    print(f"{len(rows)} branches ({sum(1 for r in rows if r[3]=='F')} JUST FALSE, {sum(1 for r in rows if r[3]=='N')} NOTHING); {len(bad)} without a comment; {len(badwhy)} NOTHING comments with no allowed reason; {len(badq)} FALSE comments with no quotation; {len(notag)} scope-limit NOTHING branches with no ruling tag")
    return 1 if (bad or badwhy or badq or notag) else 0

def quote_of(cm):
    m = re.search(r'"([^"]*)"', cm or "")
    return m.group(1) if m else ""

def classify(r):
    """Return (class, comment).  Classes:
       '-'       not marginal: the text's own no ("means", "has the meaning given by", a list closed with "only"), or a NOTHING that is not a limit on a grant
       'a-if'    reading (a): a failed "if"-type condition counted as the text's no
       'a-flat'  reading (a), flat-negative half: a flat negative counted as the text's no (ruled N2, 2026-11-04)
       'a-must'  reading (a) extended: a requirement worded "must" that is not met counted as the text's no, like "only if"
       'r-a'     JUST FALSE outside a period the text fixes in its own words (ruled 2026-11-05, (a))
       'r-b'     JUST FALSE where a "where" condition is not met (ruled 2026-11-05, (b))
       'r2c'     JUST FALSE where a "when", "upon" or "whenever" condition is not met (second ruling of 2026-11-05, (c))
       'r2d'     the two questions of an "until" bar (second ruling of 2026-11-05, (d)): the bar is JUST FALSE after Y, "has it ended" is JUST FALSE while the bar stands and NOTHING after
       'w'       JUST FALSE where "in adopting", "after" an event, "on the application of" or "on the recommendation of" is not met (assumed, not ruled: read as "where", fork F9)
       'c'       NOTHING outside a scope limit with no "only" (ruled 2026-11-05, (c))
       'o'       NOTHING outside a scope limit that the review expected to be JUST FALSE: open question
       'v'       NOTHING because the function returns a value, so there is no JUST FALSE to give
       '?'       none of the above matched; read by hand"""
    cm = r[4] or ""
    q = quote_of(cm)
    if "[ruled II(c)]" in cm:
        return "r2c", cm
    if "[ruled II(d)]" in cm:
        return "r2d", cm
    if r[3] == "N":
        if "limited by its own wording" in cm:
            if "[open question" in cm:
                return "o", cm
            if "[no yes-or-no]" in cm:
                return "v", cm
            if "[scope limit, ruled I(c)]" in cm:
                return "c", cm
            return "?", cm
        return "-", cm
    if "[ruled I(a)]" in cm:
        return "r-a", cm
    if "[ruled I(b)]" in cm:
        return "r-b", cm
    if "[assumed: when]" in cm:
        return "w", cm
    low = q.lower()
    if "has the meaning" in low:
        return "-", cm
    if re.search(r"\bmeans\b", low) and not COND.search(low):
        return "-", cm
    if re.search(r"\bonly\b", re.sub(r"\b(only if|if the only|where the only)\b", "", low)):
        return "-", cm
    if COND.search(low):
        return "a-if", cm
    if FLAT.search(low):
        return "a-flat", cm
    if re.search(r"\bmust\b", low) or "the conditions are as follows" in low or "requirements" in low:
        return "a-must", cm
    if re.match(r"s 12\(2\)", r[2]):   # the chapeau of s 12(2) is "The claim must be made -", and each limb names who may make it
        return "a-must", cm
    return "?", cm

LABEL = {
    "a-if": ("(a) a failed condition", "JUST FALSE", "NOTHING: \"if A then B\" does not itself say \"if not A then not B\""),
    "a-flat": ("(a) a flat negative", "JUST FALSE", "NOTHING: a flat negative is not a no for a case it does not reach (ruled N2, 2026-11-04: it counts as the no)"),
    "a-must": ("(a) a requirement worded \"must\", not met", "JUST FALSE", "NOTHING: \"must\" is not one of the words that make a no (\"if\", \"only if\", \"unless\", a flat negative)"),
    "w": ("assumed, not ruled: \"in adopting\", \"after\" an event, \"on the application of\" or \"on the recommendation of\" read as \"where\"", "JUST FALSE", "NOTHING: the words fix the scope of the rule and are not a condition on it (fork F9)"),
    "r2c": ("II(c) a \"when\", \"upon\" or \"whenever\" condition not met", "JUST FALSE", "NOTHING (the reading the second ruling rejects)"),
    "r2d": ("II(d) an \"until\" bar: the bar after Y, or has the stay ended", "bar: JUST FALSE after Y; ended: JUST FALSE while the bar stands, NOTHING after", "ended: JUST TRUE after Y on the strength of the bar alone (the reading the second ruling rejects)"),
    "o": ("open question: a scope limit with no \"only\" (ruled I(c)); the review expected JUST FALSE", "NOTHING", "JUST FALSE: the limit is itself the text's no for any case outside it"),
    "r-a": ("I(a) outside a period the text fixes in its own words", "JUST FALSE", "NOTHING (the reading the first ruling of 2026-11-05 rejects)"),
    "r-b": ("I(b) a \"where\" condition not met", "JUST FALSE", "NOTHING (the reading the first ruling of 2026-11-05 rejects)"),
    "c": ("I(c) outside a scope limit with no \"only\"", "NOTHING", "JUST FALSE (the reading the first ruling of 2026-11-05 rejects)"),
    "v": ("outside a scope limit, in a function that returns a value (a person, a date, an amount), so there is no yes-or-no to refuse", "NOTHING", "none: a value cannot be JUST FALSE"),
}

MARGINAL = ("a-if", "a-flat", "a-must", "w", "o")
RULED = ("r-a", "r-b", "c", "v", "r2c", "r2d")

def table(folder, classes, prefix):
    rows = scan(folder)
    groups = collections.OrderedDict()
    unknown = []
    for r in rows:
        k, cm = classify(r)
        if k == "?":
            unknown.append(r)
            continue
        if k not in classes:
            continue
        groups.setdefault((r[2], k), []).append(r)
    print("| # | Function | Module:line | Rests on | The words | Answer given | The other reading |")
    print("| --- | --- | --- | --- | --- | --- | --- |")
    n = 0
    for (fname, k), rs in groups.items():
        n += 1
        r = rs[0]
        q = quote_of(r[4])
        if not q:
            q = re.sub(r"^--\s*NOTHING-kind\s*", "", r[4] or "")
        q = q.replace("|", "\\|")
        if len(q) > 130:
            q = q[:127] + "..."
        what, ans, other = LABEL[k]
        more = (f" (and {len(rs) - 1} more branch{'es' if len(rs) > 2 else ''} of the same kind)") if len(rs) > 1 else ""
        print(f"| {prefix}{n} | `{fname}`{more} | {r[0][4:-3]}:{r[1]} | {what} | {q} | {ans} | {other} |")
    if unknown:
        for r in unknown:
            print("UNCLASSIFIED", r[0], r[1], r[2], r[4], file=sys.stderr)

def marginal(folder):
    table(folder, MARGINAL, "M")

def ruled(folder):
    table(folder, RULED, "R")

def sites(folder, cls):
    """One line per branch of the class: function, module:line, the words."""
    for r in scan(folder):
        k, cm = classify(r)
        if k == cls:
            q = quote_of(r[4]) or re.sub(r"^--\s*NOTHING-kind[^:]*:\s*", "", r[4] or "")
            print(f"`{r[2]}` ({r[0][4:-3]}:{r[1]}): {q[:160]}")

def counts(folder):
    rows = scan(folder)
    c = collections.Counter()
    fn = collections.defaultdict(set)
    for r in rows:
        k, cm = classify(r)
        c[(r[3], k)] += 1
        fn[k].add(r[2])
    print("branches by (kind, class):", dict(c))
    print("distinct functions by class:", {k: len(v) for k, v in fn.items()})

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    cmd = sys.argv[1] if len(sys.argv) > 1 else "lint"
    if cmd == "lint":
        sys.exit(lint(here))
    elif cmd == "marginal":
        marginal(here)
    elif cmd == "ruled":
        ruled(here)
    elif cmd == "sites":
        sites(here, sys.argv[2])
    else:
        counts(here)
