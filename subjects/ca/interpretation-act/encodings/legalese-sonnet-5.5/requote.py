#!/usr/bin/env python3
"""Refresh the quotation lines above every `@ref` that carries `src:` locators.

  python3 -I requote.py RAW FILE...

For each FILE this script (1) deletes every `-- src:N | text` quote line, then (2) for each `@ref` line
containing locators `src:N` or `src:N-M`, writes the quote lines for exactly those raw lines directly
above that `@ref`, by running `srcrefs.py quote RAW N M` (so the text is copied by a script that reads
RAW, never retyped). Run it after editing a locator; it is idempotent.
It then leaves the checking to `python3 -I srcrefs.py check --strict RAW FILE...`.
"""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOC = re.compile(r"\bsrc:(\d+)(?:-(\d+))?")
REF = re.compile(r"^@ref(?!-src|-map)")


def quote(raw: str, n: int, m: int) -> list[str]:
    out = subprocess.run(
        ["python3", "-I", str(HERE / "srcrefs.py"), "quote", raw, str(n), str(m)],
        check=True, capture_output=True, text=True,
    ).stdout
    return out.splitlines()


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    raw = sys.argv[1]
    for name in sys.argv[2:]:
        p = Path(name)
        lines = p.read_text(encoding="utf-8").split("\n")
        lines = [l for l in lines if not l.startswith("-- src:")]
        out: list[str] = []
        for l in lines:
            if REF.match(l):
                for mt in LOC.finditer(l):
                    n = int(mt.group(1))
                    m = int(mt.group(2) or mt.group(1))
                    out.extend(quote(raw, n, m))
            out.append(l)
        p.write_text("\n".join(out), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
