"""sync-check: are the copies in g7-interpretation-laws.l4 still identical to their sources?

For every `-- COPY of the (noun|function) `NAME` from SUBJECT (row ROW), module MODULE, ...` comment in the copy module, this finds the block (the blank-line-separated paragraph that defines NAME)
in the copy and in SUBJECT/encodings/ROW/MODULE, drops the comment lines and reduces every @ref line to a bare @ref (the one thing a copy changes is the text of the @ref), and diffs the two.
It also checks that the copy module holds no code that a COPY comment does not claim, and that it imports only prelude and daydate.

Usage: sync-check.sh [COPY-MODULE]           (default: the copy module in the Charities row)
Environment: JE_SUBJECTS   the directory holding the subjects (default: the commons worktree je-interp)
             JE_CHAR       the directory of the Charities row
Exit status: 0 if every block is identical and nothing is unclaimed; 1 otherwise; 2 on a usage or reading error.
A block that is found nowhere, or has no code lines, is an error: a diff of two empty blocks says nothing.
"""
import difflib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blocks as B  # noqa: E402  (only for SUBJECTS, CHAR, MINE and the paragraph helpers; the list of blocks is read from the copy module itself)

COPY = re.compile(r"^-- COPY of the (noun|function) `(.+?)` from (je/[A-Za-z0-9-]+) \(row ([A-Za-z0-9-]+)\), module ([A-Za-z0-9._-]+),")


def main():
    mine_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(B.CHAR, B.MINE)
    try:
        mine = B.read_lines(mine_path)
    except OSError as e:
        print(f"sync-check: cannot read {mine_path}: {e}", file=sys.stderr)
        return 2

    claims = []
    for line in mine:
        m = COPY.match(line)
        if m:
            claims.append((("noun" if m.group(1) == "noun" else "fn"), m.group(2), m.group(3), m.group(4), m.group(5)))
    if not claims:
        print("sync-check: no COPY comment found in the copy module", file=sys.stderr)
        return 2

    status = 0
    claimed_starts = set()
    seen = set()
    for kind, name, subject, row, module in claims:
        if (kind, name) in seen:
            print(f"DUP   {kind} `{name}` is claimed twice")
            status = 1
            continue
        seen.add((kind, name))
        src_path = os.path.join(B.SUBJECTS, subject.split("/", 1)[1], "encodings", row, module)
        try:
            src_lines = B.read_lines(src_path)
        except OSError as e:
            print(f"ERROR {kind} `{name}`: cannot read the source {src_path}: {e}")
            status = 1
            continue
        try:
            start_mine, par_mine = B.find_block(mine, kind, name)
        except SystemExit as e:
            print(f"ERROR in the copy module: {e}")
            status = 1
            continue
        claimed_starts.add(start_mine)
        try:
            _, par_src = B.find_block(src_lines, kind, name)
        except SystemExit as e:
            print(f"ERROR in the source {module}: {e}")
            status = 1
            continue
        a, b = B.code_of(par_src), B.code_of(par_mine)
        if not a or not b:
            print(f"ERROR {kind} `{name}`: no code lines to compare (source {len(a)}, copy {len(b)})")
            status = 1
            continue
        if a == b:
            print(f"SAME  {kind:4} `{name}`  ({len(a)} code lines; source {module})")
        else:
            status = 1
            print(f"DIFF  {kind:4} `{name}`  (source {module})")
            for d in difflib.unified_diff(a, b, "source", "copy", lineterm="", n=1):
                print("      " + d)

    # Code in the copy module that no COPY comment claims.
    imports = []
    for start, par in B.paragraphs(mine):
        code = [ln for ln in par if not B.is_comment(ln)]
        if not code:
            continue
        for ln in code:
            if ln.startswith("IMPORT "):
                imports.append(ln[len("IMPORT "):].strip())
        rest = [ln for ln in code if not ln.startswith("IMPORT ") and not ln.startswith("§")]
        if rest and start not in claimed_starts:
            status = 1
            print(f"EXTRA code at line {start} of the copy module that no COPY comment claims: {rest[0][:100]}")
    if sorted(imports) != ["daydate", "prelude"]:
        status = 1
        print(f"IMPORTS of the copy module are {imports}, not [prelude, daydate]")

    n = len(claims)
    print(f"sync-check: {n} copied blocks checked against their sources; " + ("all identical, nothing unclaimed." if status == 0 else "PROBLEMS above."))
    return status


sys.exit(main())
