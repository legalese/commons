#!/usr/bin/env python3
"""Expand quotation macros in an .l4 file, in place, so that quotations are copied from the deposited text and never typed.

  @@Q N-M <label>          part 7, lines N-M: the `-- src:` quote lines, then `@ref <label> (src:N-M)`
  @@Q s9 N-M <label>       schedule 9, lines N-M: the same, with the `src:ukpga-2002-29-schedule-9:` form
  @@R N-M <label>          only the `@ref <label> (src:N-M)` line (a narrower citation of lines already quoted above)
  @@R s9 N-M <label>       the same for schedule 9

Run:  python3 -I mkrefs.py FILE.l4 [RAW_DIR]     (RAW_DIR defaults to $RAW_DIR)
Quote lines are produced by `srcrefs.py quote` / `quoteid`, so the squeezing and NFC normalisation are the script's.
"""
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
raw_dir = sys.argv[2] if len(sys.argv) > 2 else os.environ["RAW_DIR"]
P7 = os.path.join(raw_dir, "ukpga-2002-29-part-7.txt")
S9 = os.path.join(raw_dir, "ukpga-2002-29-schedule-9.txt")
S9ID = "ukpga-2002-29-schedule-9"


def quote(sch, a, b):
    raw = S9 if sch else P7
    cmd = ["python3", "-I", os.path.join(HERE, "srcrefs.py"), "quoteid" if sch else "quote", raw, str(a)] + ([str(b)] if b != a else [])
    text = subprocess.run(cmd, check=True, capture_output=True, text=True).stdout.rstrip("\n")
    # a raw line that is only dots is a repealed or blank line: it has no text to quote (srcrefs.py R1), so leave it out
    keep = [ln for ln in text.split("\n") if re.sub(r"[\s.…]", "", ln.split(" | ", 1)[-1])]
    return "\n".join(keep)


def loc(sch, a, b):
    rng = f"{a}-{b}" if a != b else f"{a}"
    return f"src:{S9ID}:{rng}" if sch else f"src:{rng}"


out = []
for line in open(sys.argv[1], encoding="utf-8").read().split("\n"):
    m = re.match(r"^@@([QR])\s+(?:(s9)\s+)?(\d+)(?:-(\d+))?\s+(.+)$", line)
    if not m:
        out.append(line)
        continue
    kind, sch, a, b, label = m.group(1), bool(m.group(2)), int(m.group(3)), int(m.group(4) or m.group(3)), m.group(5).strip()
    if kind == "Q":
        out.append(quote(sch, a, b))
    out.append(f"@ref {label} ({loc(sch, a, b)})")
open(sys.argv[1], "w", encoding="utf-8").write("\n".join(out))
