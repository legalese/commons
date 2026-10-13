#!/usr/bin/env python3
"""check-traces.py: check every #TRACE of an L4 module against the outcome its author said it must have.

Why this exists.  A DEONTIC value (a MUST, MAY or SHANT rule run against a list of events) has no equality, so no
#ASSERT can state its outcome, and `l4 run` prints a trace's result and exits 0 whatever it printed.  Without this
script the traces of the encoding guard nothing.  The eight group encoders each wrote their own checker for their
own comment format; this one reads all of them.

Where an expectation comes from, per #TRACE, in this order:
  1. an EXPECT comment in the module itself.  Four spellings are accepted, all meaning the same:
         -- EXPECT: FULFILLED                       (groups 1 and 5, and the int- modules)
         -- EXPECT: BREACH BY `the Registrar`       (the words after the kind must occur in the printed result)
         -- EXPECT FULFILLED | BREACH text | STANDING text     (group 4: no colon; the text must occur)
         -- TRACE-EXPECT: BREACHED | text           (group 3: BREACHED is BREACH)
     The comment sits in the comment lines right ABOVE the #TRACE statement (groups 3, 4, 5, int-) or right BELOW its
     WITH body (group 1).  Which one a file uses is decided once per file: if any EXPECT comment comes before the first
     #TRACE the file is "above", otherwise "below".  Every EXPECT comment must be claimed by exactly one trace.
  2. the sidecar file (--sidecar, default int-trace-expect.tsv next to this script), for modules whose authors wrote
     the expectation in prose and not in a comment (groups 2, 6, 7, 8) and which this encoding may not edit.
     A sidecar row names the file and a key: the first 12 hex digits of the sha1 of the trace's statement (the #TRACE line and
     the indented lines under it, stripped).  A row is matched by content (a second identical statement in one file gets the suffix +2, +3, ...), so an edit that adds or
     moves a trace cannot make a row attach itself to a different trace; a row whose statement is no longer in the file is reported as stale.
  3. nothing: the trace is reported as UNGUARDED.  With --require-all that is a failure.

Outcomes.  FULFILLED: the printed result is exactly FULFILLED.  BREACH: it begins `DEONTIC BREACHED` and contains the
text, if any.  STANDING: it is neither of those (the obligation, permission or prohibition is printed back, still
open) and contains the text, if any.

A run that fails to start, is killed by a signal, or prints no result for a #TRACE is a failure, never a pass: the
check cannot tell "all as expected" from "nothing ran" unless it counts what it saw.

Usage: check-traces.py [--l4 PATH] [--sidecar FILE] [--require-all] [--quiet] FILE.l4 ...
Exit status 0 only if every guarded trace matched and (with --require-all) none was unguarded.
"""
import argparse, hashlib, json, os, pathlib, re, subprocess, sys

KIND_RE = re.compile(r"^--\s*(?:TRACE-)?EXPECT:?\s+(FULFILLED|BREACHED|BREACH|STANDING)\b\s*(.*)$")


def norm_kind(k):
    return "BREACH" if k in ("BREACH", "BREACHED") else k


def clean_text(rest):
    rest = rest.strip()
    if rest.startswith("|"):
        rest = rest[1:].strip()
    return rest


def parse_module(path):
    """Return (traces, tags, problems).  traces: list of dicts {ordinal, line, head}; tags: list of (line, kind, text)."""
    lines = pathlib.Path(path).read_text(encoding="utf-8").split("\n")
    traces, tags, seen = [], [], {}
    for i, l in enumerate(lines):
        if l.startswith("#TRACE"):
            k = i + 1
            stmt = [l.strip()]
            while k < len(lines) and (lines[k].startswith(" ") or lines[k].startswith("\t")):
                stmt.append(lines[k].strip())
                k += 1
            key = hashlib.sha1("\n".join(stmt).encode("utf-8")).hexdigest()[:12]
            seen[key] = seen.get(key, 0) + 1
            if seen[key] > 1:  # two identical statements in one file: the second is told apart by its occurrence number
                key = "%s+%d" % (key, seen[key])
            traces.append({"ordinal": len(traces) + 1, "line": i + 1, "head": l[:80], "index": i, "key": key})
        m = KIND_RE.match(l)
        if m:
            tags.append({"line": i + 1, "index": i, "kind": norm_kind(m.group(1)), "text": clean_text(m.group(2))})
    return lines, traces, tags


def is_comment_or_blank(s):
    return (not s.strip()) or s.startswith("--")


def assign_tags(base, lines, traces, tags):
    """Attach each tag to one trace.  Returns (expect: ordinal -> (kind, text, tagline), problems)."""
    problems, expect = [], {}
    if not tags:
        return expect, problems
    first_trace = traces[0]["index"] if traces else None
    above = first_trace is not None and any(t["index"] < first_trace for t in tags)
    claimed = set()
    for tr in traces:
        i = tr["index"]
        if above:
            j = i - 1
            while j >= 0 and is_comment_or_blank(lines[j]):
                j -= 1
            lo = j + 1
            cand = [t for t in tags if lo <= t["index"] < i]
        else:
            j = i + 1
            while j < len(lines) and (lines[j].startswith(" ") or lines[j].startswith("\t") or not lines[j].strip()):
                j += 1
            hi = j
            while hi < len(lines) and is_comment_or_blank(lines[hi]):
                hi += 1
            cand = [t for t in tags if j <= t["index"] < hi]
        if len(cand) > 1:
            problems.append("%s:%d: %d EXPECT comments claim this #TRACE" % (base, tr["line"], len(cand)))
        if cand:
            t = cand[-1] if above else cand[0]
            expect[tr["ordinal"]] = (t["kind"], t["text"], "line %d" % t["line"])
            claimed.add(t["index"])
    for t in tags:
        if t["index"] not in claimed:
            problems.append("%s:%d: EXPECT comment that no #TRACE claims" % (base, t["line"]))
    return expect, problems


def load_sidecar(path):
    rows = {}
    if not path or not os.path.exists(path):
        return rows
    for n, raw in enumerate(pathlib.Path(path).read_text(encoding="utf-8").split("\n"), 1):
        if not raw.strip() or raw.startswith("#"):
            continue
        c = raw.split("\t")
        if len(c) < 5:
            print("sidecar line %d: expected at least 5 tab-separated columns" % n)
            sys.exit(2)
        file, key, head, kind, text = c[0], c[1], c[2], norm_kind(c[3].strip()), c[4].strip()
        rows[(file, key)] = (kind, text, head, "sidecar line %d" % n)
    return rows


def run_l4(l4, path, tries=3):
    for attempt in range(tries):
        r = subprocess.run(["nice", "-n", "15", l4, "run", os.path.abspath(path), "--json"], capture_output=True, text=True,
                           cwd=os.path.dirname(os.path.abspath(path)))
        if r.returncode < 0:
            print("  (l4 was killed by signal %d on %s; that run is INVALID, rerunning)" % (-r.returncode, os.path.basename(path)))
            continue
        try:
            d = json.loads(r.stdout)
        except Exception as e:  # not JSON: the run did not complete
            print("  (l4 printed no JSON for %s: %s)" % (os.path.basename(path), e))
            continue
        return d
    return None


def check_file(l4, path, sidecar, require_all, quiet):
    base = os.path.basename(path)
    lines, traces, tags = parse_module(path)
    if not traces:
        return dict(file=base, n=0, ok=0, bad=0, unguarded=0, tagged=0, side=0, problems=[])
    expect, problems = assign_tags(base, lines, traces, tags)
    d = run_l4(l4, path)
    bad = ok = unguarded = tagged = side = 0
    if d is None:
        print("%s: NO VALID RUN: %d traces unchecked" % (base, len(traces)))
        return dict(file=base, n=len(traces), ok=0, bad=len(traces), unguarded=0, tagged=0, side=0, problems=problems)
    by_line = {}
    for r in d.get("results", []):
        m = re.match(r".*?:(\d+):\d+", r.get("range", ""))
        if m:
            by_line[int(m.group(1))] = r.get("value")
    for tr in traces:
        val = by_line.get(tr["line"])
        e = expect.get(tr["ordinal"])
        src = None
        if e:
            tagged += 1
            src = "comment " + e[2]
        else:
            s = sidecar.get((base, tr["key"]))
            if s:
                kind, text, head, where = s
                e = (kind, text, where)
                side += 1
                src = where
        if e is None:
            unguarded += 1
            print("%s:%d: UNGUARDED: #TRACE with no EXPECT comment and no sidecar row" % (base, tr["line"]))
            continue
        kind, text = e[0], e[1]
        if not isinstance(val, str):
            print("%s:%d: no result printed for this #TRACE (expected %s)" % (base, tr["line"], kind))
            bad += 1
            continue
        if kind == "FULFILLED":
            good = val.strip() == "FULFILLED"
        elif kind == "BREACH":
            good = val.startswith("DEONTIC BREACHED") and text in val
        else:
            good = (not val.startswith("DEONTIC BREACHED")) and val.strip() != "FULFILLED" and bool(val.strip()) and text in val
        if good:
            ok += 1
        else:
            bad += 1
            print("%s:%d: expected %s%s (%s), got: %s" % (base, tr["line"], kind, (" containing %r" % text) if text else "", src,
                                                       val.replace("\n", " / ")[:240]))
    keys = set(tr["key"] for tr in traces)
    for (f, key), (kind, text, head, where) in sorted(sidecar.items()):
        if f == base and key not in keys:
            problems.append("%s: STALE sidecar row (%s): no #TRACE of this file has the statement it was written for: %s" % (base, where, head))
    for p in problems:
        print(p)
    return dict(file=base, n=len(traces), ok=ok, bad=bad, unguarded=unguarded, tagged=tagged, side=side, problems=problems)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--l4", default=os.environ.get("L4", "l4"))
    ap.add_argument("--sidecar", default=str(pathlib.Path(__file__).resolve().parent / "int-trace-expect.tsv"))
    ap.add_argument("--require-all", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="accepted and ignored: every problem is always printed")
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    sidecar = load_sidecar(a.sidecar)
    tot = dict(n=0, ok=0, bad=0, unguarded=0, tagged=0, side=0)
    probs = 0
    print("%-44s %7s %9s %9s %6s %5s %10s" % ("module", "traces", "in-module", "sidecar", "ok", "bad", "unguarded"))
    for f in a.files:
        r = check_file(a.l4, f, sidecar, a.require_all, a.quiet)
        if r["n"] == 0:
            continue
        print("%-44s %7d %9d %9d %6d %5d %10d" % (r["file"], r["n"], r["tagged"], r["side"], r["ok"], r["bad"], r["unguarded"]))
        for k in tot:
            tot[k] += r[k]
        probs += len(r["problems"])
    print("%-44s %7d %9d %9d %6d %5d %10d" % ("TOTAL", tot["n"], tot["tagged"], tot["side"], tot["ok"], tot["bad"], tot["unguarded"]))
    if tot["n"] != tot["ok"] + tot["bad"] + tot["unguarded"]:
        print("check-traces: the counts do not add up: a trace went unaccounted for")
        sys.exit(1)
    if tot["bad"] or probs:
        print("check-traces: FAILED, %d trace(s) did not behave as expected, %d problem(s) with the expectations themselves (stale sidecar rows, EXPECT comments that no trace claims)" % (tot["bad"], probs))
        sys.exit(1)
    if tot["unguarded"]:
        print("check-traces: %d trace(s) have no expectation" % tot["unguarded"])
        if a.require_all:
            sys.exit(1)
    print("check-traces: all %d guarded trace(s) behaved as expected" % tot["ok"])


if __name__ == "__main__":
    main()
