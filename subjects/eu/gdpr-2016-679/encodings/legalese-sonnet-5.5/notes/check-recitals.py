#!/usr/bin/env python3
# notes/check-recitals.py -- the word-for-word check of recitals/gdpr-recitals.l4 against the deposited source.
#
# Run:   L4=/path/to/an/unstable/l4 python3 -I notes/check-recitals.py [--l4 FILE] [--source FILE] [--corrigendum FILE]
#                                                                     [--l4-bin PATH | --no-run] [--self-test]
# Exit status: 0 every check passed; 1 a check failed (the line names the recital); 2 a step could not run (no l4 binary, a missing file).
#
# It does NOT import or call notes/gen-recitals.py, and it parses the source and the module by its own code, so that a
# fault in the generator's reading cannot be repeated here.  What it checks:
#   1. The inputs are the deposited ones: sha256 of the source and of the corrigendum equal the text_sha256 of their .meta.json.
#   2. The source region (from "Whereas:" to "HAVE ADOPTED") is exactly 173 rows `| (n) | text |`, n = 1..173 in order, and
#      rebuilding "| (n) | " + text + " |" gives back the source line byte for byte, so removing the frame drops nothing.
#      Its characters: no double quote, no backslash, no control character (so no escape is in play), and the census of
#      the non-ASCII ones is printed.
#   3. The module has, and only has, the lines the generator writes: the heading and 6 citation items, the heading and 173 recital
#      items, in source order, each recital's `-- (n)` comment equal to its position and to its source number.
#   4. NO NORMALISATION: each item's string, decoded by this script's own string scanner, equals the source text byte for byte,
#      except recital 71, which equals the as-published text with the corrigendum's two changes made (stated here by hand, as
#      two small replacements, not read from the corrigendum).  The corrigendum file is read as a cross-check, by a different
#      route: its 'read' passage is in the module's recital 71, its 'for' passage is not, and putting the 'for' passage back
#      gives the as-published recital byte for byte.  Exactly one correction of the corrigendum names a recital.
#   5. What the compiler read: `l4 run` is run on the module, with JL4_LIBRARY_PATH unset; there is no error; every #ASSERT is satisfied;
#      the two #EVAL results are decoded and compared, line by line, with the source: the heading, then "<n>\t<text>" for
#      n = 1..173 (and "•\t<text>" for the citations).  This is the step that reads the numbers the renderer gave.
# --self-test mutates the module in memory, in sixteen ways, and requires step 3 and 4 to fail, naming the recital; it prints the table.
import argparse
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

ENC = Path(__file__).resolve().parent.parent
BUNDLE = ENC.parent.parent / "registers" / "source-bundle"
DEFAULT_L4 = ENC / "recitals" / "gdpr-recitals.l4"

HEAD = "THE EUROPEAN PARLIAMENT AND THE COUNCIL OF THE EUROPEAN UNION,"

# The two changes the 2018 corrigendum makes to recital 71, written out by hand from its 'for' and 'read' passages.
R71_EDITS = [
    ("of the data subject and that prevents, inter alia, discriminatory",
     "of the data subject, and prevent, inter alia, discriminatory"),
    ("sexual orientation, or that result in measures having such an effect.",
     "sexual orientation, or processing that results in measures having such an effect."),
]


class Fail(Exception):
    pass


# ---------------------------------------------------------------------------------------------------- the source

def read_text_checked(path, meta):
    raw = Path(path).read_bytes()
    want = json.loads(Path(meta).read_text(encoding="utf-8"))["text_sha256"]
    got = hashlib.sha256(raw).hexdigest()
    if got != want:
        raise Fail("input %s: sha256 %s is not the text_sha256 %s that %s records" % (Path(path).name, got, want, Path(meta).name))
    return raw.decode("utf-8").split("\n")


def source_view(lines):
    """(citations, recital texts by number 1..173, census of the region's characters)."""
    where = [i for i, l in enumerate(lines) if l == "Whereas:"]
    ends = [i for i, l in enumerate(lines) if l.startswith("HAVE ADOPTED")]
    heads = [i for i, l in enumerate(lines) if l.startswith("THE EUROPEAN PARLIAMENT AND THE COUNCIL")]
    if len(where) != 1 or len(ends) != 1 or len(heads) != 1:
        raise Fail("source: the anchors 'Whereas:', 'HAVE ADOPTED' and the heading are not each found once")
    h, w, e = heads[0], where[0], ends[0]
    if lines[h] != HEAD:
        raise Fail("source: the heading line is %r" % lines[h])
    cites = lines[h + 1:w]
    texts = {}
    region = []
    for line in lines[w + 1:e]:
        region.append(line)
        if not line.startswith("| ("):
            raise Fail("source: a line between 'Whereas:' and 'HAVE ADOPTED' is not a row: %r" % line[:70])
        close = line.index(") | ")
        n = int(line[3:close])
        body = line[close + 4:]
        if not body.endswith(" |"):
            raise Fail("source: row (%d) does not end with ' |'" % n)
        body = body[:-2]
        if "| (%d) | %s |" % (n, body) != line:
            raise Fail("source: recital %d: the frame removed is not the frame put back" % n)
        if n in texts:
            raise Fail("source: recital %d occurs twice" % n)
        texts[n] = body
    if sorted(texts) != list(range(1, 174)) or [int(l[3:l.index(")")]) for l in region] != list(range(1, 174)):
        raise Fail("source: the rows are not exactly (1) to (173), once each, in order (found %d rows)" % len(texts))
    census = Counter(ch for t in texts.values() for ch in t if ord(ch) > 126)
    for t in list(texts.values()) + cites:
        if '"' in t or "\\" in t or any(ord(ch) < 0x20 for ch in t):
            raise Fail("source: a double quote, a backslash or a control character occurs in the region (this check assumes none)")
    return cites, texts, census


def expected_texts(texts):
    """The text each recital must have: as published, but recital 71 with the corrigendum's two changes."""
    out = dict(texts)
    r = texts[71]
    for a, b in R71_EDITS:
        if r.count(a) != 1:
            raise Fail("source: the passage %r is not found exactly once in the as-published recital 71" % a)
        r = r.replace(a, b)
    out[71] = r
    return out


def corrigendum_crosscheck(cor_lines, published71, l4_71):
    """A second route to recital 71: read its 'for' and 'read' passages from the corrigendum file itself."""
    hits = [i for i, l in enumerate(cor_lines) if l.startswith("On page") and "recital" in l]
    if len(hits) != 1 or "recital 71," not in cor_lines[hits[0]]:
        raise Fail("corrigendum: exactly one correction should name a recital (71); found %d" % len(hits))
    i = hits[0]
    if cor_lines[i + 1] != "for:" or cor_lines[i + 3] != "read:":
        raise Fail("corrigendum: the recital 71 entry does not have for:/read: where expected")

    def passage(line):
        # `| ‘(71) | … PASSAGE’, |` for the 'for', `| ‘(71) | … PASSAGE’. |` for the 'read'
        after = line.partition("… ")[2]
        return after[:after.rindex("’")]

    f, r = passage(cor_lines[i + 2]), passage(cor_lines[i + 4])
    if f not in published71:
        raise Fail("corrigendum: its 'for' passage is not in the as-published recital 71")
    if r not in l4_71:
        raise Fail("recital 71: the corrigendum's 'read' passage is not in the module's recital")
    if f in l4_71:
        raise Fail("recital 71: the module still carries the corrigendum's 'for' passage (the as-published wording)")
    if l4_71.replace(r, f) != published71:
        raise Fail("recital 71: putting the corrigendum's 'for' passage back does not give the as-published recital byte for byte")
    return len(f.split()), len(r.split())


# ------------------------------------------------------------------------------------------------ the module

def scan_literal(s, i):
    """The L4 string literal starting at s[i] == '"': (decoded value, index after the closing quote).  Only \\" and \\\\ are escapes."""
    if s[i] != '"':
        raise Fail("a string literal is expected at column %d" % (i + 1))
    out = []
    i += 1
    while True:
        if i >= len(s):
            raise Fail("a string literal is not closed")
        c = s[i]
        if c == '"':
            return "".join(out), i + 1
        if c == "\\":
            d = s[i + 1:i + 2]
            if d not in ('"', "\\"):
                raise Fail("an escape other than \\\" and \\\\ in a string literal")
            out.append(d)
            i += 2
        else:
            out.append(c)
            i += 1


BULLET = re.compile(r"^    • item ")
COMMENT_N = re.compile(r"^\s*-- \((\d+)\)\s*$")


def module_view(text):
    """(heading1, citations, heading2, recitals-with-comment-number) read from the module; any other code line is a failure."""
    section = None
    h1 = h2 = None
    cites, recs = [], []
    seen = Counter()
    for no, line in enumerate(text.split("\n"), 1):
        if line == "" or line.startswith("--"):
            continue
        if line in ("IMPORT hierarchy", "`GDPR citations scheme` MEANS LIST Bulleted", "`GDPR recitals scheme` MEANS LIST Decimal"):
            seen[line] += 1
            continue
        if line == "`GDPR preamble citations` MEANS":
            section = 1
            continue
        if line == "`GDPR recitals` MEANS":
            section = 2
            continue
        if line.startswith("#ASSERT ") or line.startswith("#EVAL "):
            section = None
            seen["directive"] += 1
            continue
        if line.startswith("  item ") and section in (1, 2):
            v, j = scan_literal(line, len("  item "))
            if line[j:] != "":
                raise Fail("line %d: text after a heading literal" % no)
            if section == 1 and h1 is None:
                h1 = v
            elif section == 2 and h2 is None:
                h2 = v
            else:
                raise Fail("line %d: a second heading in a section" % no)
            continue
        if BULLET.match(line) and section in (1, 2):
            v, j = scan_literal(line, len("    • item "))
            rest = line[j:]
            if section == 1:
                if rest != "":
                    raise Fail("line %d: text after a citation literal" % no)
                cites.append(v)
            else:
                m = COMMENT_N.match(rest)
                if not m:
                    raise Fail("line %d: a recital item without its '-- (n)' comment" % no)
                recs.append((v, int(m.group(1)), no))
            continue
        raise Fail("line %d: a line the generator does not write: %r" % (no, line[:80]))
    if seen["IMPORT hierarchy"] != 1 or seen["`GDPR citations scheme` MEANS LIST Bulleted"] != 1 or seen["`GDPR recitals scheme` MEANS LIST Decimal"] != 1:
        raise Fail("module: the IMPORT or one of the two scheme lines is missing or repeated")
    return h1, cites, h2, recs


def words_diff(a, b):
    """A short description of how the word lists a (source) and b (module) differ."""
    wa, wb = a.split(), b.split()
    sm = difflib.SequenceMatcher(a=wa, b=wb, autojunk=False)
    parts = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        parts.append("%s at word %d: source %r, module %r" % (tag, i1 + 1, " ".join(wa[i1:i2])[:60], " ".join(wb[j1:j2])[:60]))
        if len(parts) == 2:
            break
    return "; ".join(parts) + " (source %d words, module %d)" % (len(wa), len(wb))


def static_check(src_lines, cor_lines, l4_text):
    """Steps 2 to 4.  Returns (failures, facts); failures is a list of strings, each naming its recital."""
    fails = []
    cites, texts, census = source_view(src_lines)
    want = expected_texts(texts)
    h1, got_cites, h2, recs = module_view(l4_text)
    if h1 != HEAD:
        fails.append("preamble heading: %r" % (h1,))
    if h2 != "Whereas:":
        fails.append("recitals heading: %r" % (h2,))
    if got_cites != cites:
        if len(got_cites) != len(cites):
            fails.append("preamble: %d citation formulae in the module, %d in the source" % (len(got_cites), len(cites)))
        for k, (s, m) in enumerate(zip(cites, got_cites), 1):
            if s != m:
                fails.append("preamble citation %d: %s" % (k, words_diff(s, m)))
    if len(recs) != 173:
        fails.append("recitals: %d items in the module, 173 in the source" % len(recs))
    for k, (v, c, no) in enumerate(recs, 1):
        if c != k:
            fails.append("recital %d: the comment on line %d says (%d); the position is %d" % (k, no, c, k))
        if k in want and v != want[k]:
            if v.split() == want[k].split():
                fails.append("recital %d: the words are equal but the characters differ (whitespace) at line %d" % (k, no))
            else:
                fails.append("recital %d: %s" % (k, words_diff(want[k], v)))
    # a recital that appears elsewhere in the module (a merge, a duplicate, a swap) is caught above by position; say so by name too
    by_text = Counter(v for v, _, _ in recs)
    for v, n in by_text.items():
        if n > 1:
            k = [i for i, (x, _, _) in enumerate(recs, 1) if x == v][0]
            fails.append("recital %d: the same text occurs %d times in the module" % (k, n))
    facts = {"citations": len(got_cites), "recitals": len(recs),
             "source_words": sum(len(want[n].split()) for n in want) + sum(len(c.split()) for c in cites),
             "census": census}
    # the corrigendum, by a second route
    if len(recs) >= 71:
        try:
            facts["corrigendum_words"] = corrigendum_crosscheck(cor_lines, texts[71], recs[70][0])
        except Fail as e:
            fails.append(str(e))
    return fails, facts


# ----------------------------------------------------------------------------------------- what the compiler read

def run_l4(l4_bin, module):
    env = {k: v for k, v in os.environ.items() if k != "JL4_LIBRARY_PATH"}
    p = subprocess.run([l4_bin, "run", Path(module).name], cwd=str(Path(module).resolve().parent), env=env,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="replace")
    return p.returncode, p.stdout


def decode_list(s):
    """`LIST "a", "b", ...` -> [a, b, ...]; refuses anything else."""
    if not s.startswith("LIST "):
        raise Fail("an #EVAL result is not a LIST: %r" % s[:60])
    i = len("LIST ")
    out = []
    while True:
        v, i = scan_literal(s, i)
        out.append(v)
        if i == len(s):
            return out
        if s[i:i + 2] != ", ":
            raise Fail("a LIST result is not a comma-separated list of strings at column %d" % (i + 1))
        i += 2


def results_of(out):
    """The text of every `Result:` block of the run, in order (the line after `Result:`)."""
    lines = out.split("\n")
    res = []
    for i, l in enumerate(lines):
        if l.startswith("Evaluation["):
            j = i + 1
            while j < len(lines) and lines[j] != "Result:":
                j += 1
            res.append(lines[j + 1].strip() if j + 1 < len(lines) else "")
    return res


def compiler_check(l4_bin, module, src_lines):
    fails = []
    cites, texts, _ = source_view(src_lines)
    want = expected_texts(texts)
    rc, out = run_l4(l4_bin, module)
    n_err = out.count("DiagnosticSeverity_Error")
    n_assert = len(re.findall(r"(?m)^#ASSERT ", Path(module).read_text(encoding="utf-8")))
    res = results_of(out)
    n_ok = sum(1 for r in res if r == "assertion satisfied")
    if n_err:
        fails.append("l4 run: %d error diagnostics" % n_err)
    if n_ok != n_assert:
        fails.append("l4 run: %d assertions satisfied, %d written" % (n_ok, n_assert))
    lists = [r for r in res if r.startswith("LIST ")]
    if len(lists) != 2:
        fails.append("l4 run: expected two LIST results, found %d" % len(lists))
        return fails, {"rc": rc, "errors": n_err, "assertions": n_ok}
    c, r = decode_list(lists[0]), decode_list(lists[1])
    if c != [HEAD] + ["•\t" + x for x in cites]:
        fails.append("l4 run: the rendered preamble does not equal the heading and the six citations")
    if len(r) != 174:
        fails.append("l4 run: the rendered recitals have %d lines, not 174" % len(r))
    if r and r[0] != "Whereas:":
        fails.append("l4 run: the first rendered line is %r" % r[0][:40])
    for n in range(1, min(len(r), 174)):
        num, sep, text = r[n].partition("\t")
        if not sep or num != str(n):
            fails.append("recital %d: the rendered number is %r" % (n, num))
        elif text != want[n]:
            fails.append("recital %d (as rendered by l4): %s" % (n, words_diff(want[n], text)))
    return fails, {"rc": rc, "errors": n_err, "assertions": n_ok, "rendered": r}


# ------------------------------------------------------------------------------------------------- self-test

def mutations(l4_text):
    """(name, mutated text, a string the failure list must contain)."""
    lines = l4_text.split("\n")

    def idx(k):  # the line of recital k
        return [i for i, l in enumerate(lines) if l.endswith("-- (%d)" % k)][0]

    def with_line(k, f):
        ls = list(lines)
        ls[idx(k)] = f(ls[idx(k)])
        return "\n".join(ls)

    def delete_word(line):
        a = line.index("• item \"") + 8
        sp = [m.start() for m in re.finditer(" ", line[a:])]
        p = a + sp[len(sp) // 2]
        q = line.index(" ", p + 1)
        return line[:p] + line[q:]

    m = []
    m.append(("delete one word from recital 100", with_line(100, delete_word), "recital 100"))
    m.append(("delete one word from recital 1", with_line(1, delete_word), "recital 1:"))
    m.append(("delete one word from recital 173", with_line(173, delete_word), "recital 173"))
    m.append(("drop the footnote marker '( 4 )' from recital 3", with_line(3, lambda l: l.replace(" ( 4 )", "", 1)), "recital 3"))
    m.append(("curly quote to a straight quote in recital 1", with_line(1, lambda l: l.replace("‘", "'", 1)), "recital 1:"))
    m.append(("a double space in recital 12", with_line(12, lambda l: (lambda i: l[:i] + " " + l[i:])(l.index(" ", l.index("• item \"") + 8))), "recital 12"))
    m.append(("truncate recital 50 by its last character", with_line(50, lambda l: (lambda i: l[:i - 1] + l[i:])(l.rindex("\"  -- ("))), "recital 50"))
    m.append(("revert recital 71 to the as-published (uncorrected) wording",
              with_line(71, lambda l: l.replace(R71_EDITS[0][1], R71_EDITS[0][0]).replace(R71_EDITS[1][1], R71_EDITS[1][0])), "recital 71"))
    m.append(("revert only the first change in recital 71", with_line(71, lambda l: l.replace(R71_EDITS[0][1], R71_EDITS[0][0])), "recital 71"))
    # a swap of two recitals' texts
    ls = list(lines)
    a, b = idx(20), idx(21)
    ta, tb = ls[a][:ls[a].rindex("  -- (")], ls[b][:ls[b].rindex("  -- (")]
    ls[a], ls[b] = tb + "  -- (20)", ta + "  -- (21)"
    m.append(("swap the texts of recitals 20 and 21", "\n".join(ls), "recital 20"))
    # a merge: recital 30 absorbs recital 31 (one item fewer)
    ls = list(lines)
    a, b = idx(30), idx(31)
    ta = ls[a][:ls[a].rindex("\"  -- (")]
    tb = ls[b][ls[b].index("• item \"") + 8:ls[b].rindex("\"  -- (")]
    ls[a] = ta + " " + tb + "\"  -- (30)"
    del ls[b]
    m.append(("merge recitals 30 and 31 into one item", "\n".join(ls), "recital 30"))
    # a dropped recital
    ls = list(lines)
    del ls[idx(173)]
    m.append(("drop recital 173", "\n".join(ls), "recitals: 172 items"))
    # a duplicated recital
    ls = list(lines)
    ls.insert(idx(88) + 1, ls[idx(88)])
    m.append(("duplicate recital 88", "\n".join(ls), "recital 88"))
    # a wrong position comment
    m.append(("change the comment of recital 9 to (10)", with_line(9, lambda l: l.replace("-- (9)", "-- (10)")), "recital 9:"))
    # a citation changed
    m.append(("delete a word from the third citation", l4_text.replace("legislative act to the", "legislative to the", 1), "preamble citation"))
    # an invented recital text appended
    ls = list(lines)
    ls.insert(idx(173) + 1, "    • item \"An invented recital.\"  -- (174)")
    m.append(("invent a recital 174", "\n".join(ls), "recitals: 174 items"))
    return m


def self_test(src_lines, cor_lines, l4_text):
    base, _ = static_check(src_lines, cor_lines, l4_text)
    if base:
        print("self-test: the unmutated module already fails: %s" % base[0])
        return 1
    print("%-62s %s" % ("mutation (in memory)", "result"))
    bad = 0
    for name, text, must in mutations(l4_text):
        if text == l4_text:
            print("%-62s NOT APPLIED (the mutation changed nothing)" % name)
            bad += 1
            continue
        try:
            fails, _ = static_check(src_lines, cor_lines, text)
        except Fail as e:
            fails = [str(e)]
        hit = [f for f in fails if must in f]
        if hit:
            print("%-62s caught: %s" % (name, hit[0][:110]))
        else:
            print("%-62s MISSED (failures: %s)" % (name, "; ".join(f[:60] for f in fails) or "none"))
            bad += 1
    print("self-test: %s" % ("all mutations caught" if not bad else "%d mutation(s) not caught" % bad))
    return 1 if bad else 0


# ------------------------------------------------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser(description="word-for-word check of recitals/gdpr-recitals.l4 against the deposited source")
    ap.add_argument("--l4", default=str(DEFAULT_L4), help="the module to check")
    ap.add_argument("--source", default=str(BUNDLE / "eu-gdpr-2016-679.txt"))
    ap.add_argument("--corrigendum", default=str(BUNDLE / "eu-gdpr-2016-679-corrigendum-20180523.txt"))
    ap.add_argument("--l4-bin", default=os.environ.get("L4", ""), help="an unstable-build l4 (default: $L4)")
    ap.add_argument("--no-run", action="store_true", help="skip step 5 (the compiler); the exit status is then not a full check")
    ap.add_argument("--self-test", action="store_true", help="mutate the module in memory and require every mutation to be caught")
    a = ap.parse_args()
    try:
        src_lines = read_text_checked(a.source, BUNDLE / "eu-gdpr-2016-679.meta.json")
        cor_lines = read_text_checked(a.corrigendum, BUNDLE / "eu-gdpr-2016-679-corrigendum-20180523.meta.json")
        l4_text = Path(a.l4).read_text(encoding="utf-8")
    except (Fail, OSError) as e:
        print("check-recitals: %s" % e)
        return 2 if isinstance(e, OSError) else 1
    if a.self_test:
        return self_test(src_lines, cor_lines, l4_text)
    try:
        fails, facts = static_check(src_lines, cor_lines, l4_text)
    except Fail as e:
        fails, facts = [str(e)], {}
    for f in fails:
        print("FAIL " + f)
    if facts:
        print("static: %d citations, %d recitals, %d words in all; non-ASCII characters in the recitals: %s" % (
            facts["citations"], facts["recitals"], facts["source_words"],
            ", ".join("%s U+%04X x%d" % (c, ord(c), n) for c, n in sorted(facts["census"].items()))))
        if "corrigendum_words" in facts:
            print("corrigendum, recital 71: 'for' passage %d words, 'read' passage %d words; the module has the 'read' one" % facts["corrigendum_words"])
    status = 1 if fails else 0
    if a.no_run:
        print("compiler step skipped (--no-run): this is not a full check")
        return status
    if not a.l4_bin or not (Path(a.l4_bin).exists() or shutil.which(a.l4_bin)):
        print("check-recitals: no l4 binary (set L4 or --l4-bin, or pass --no-run): the compiler step could not run")
        return 2
    cfails, cfacts = compiler_check(a.l4_bin, a.l4, src_lines)
    for f in cfails:
        print("FAIL " + f)
    print("compiler: l4 exit %d, %d error diagnostics, %d assertions satisfied, %d lines rendered" % (
        cfacts.get("rc", -1), cfacts.get("errors", -1), cfacts.get("assertions", -1), len(cfacts.get("rendered", []))))
    status = 1 if (fails or cfails) else 0
    print("check-recitals: %s" % ("PASS" if not status else "FAIL"))
    return status


if __name__ == "__main__":
    sys.exit(main())
