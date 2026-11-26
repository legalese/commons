#!/usr/bin/env python3
# notes/add-tests.py -- P2's helper: inserts the text on stdin into notes/gen-tests-p2.py before its main guard.
import sys
p = "notes/gen-tests-p2.py"
s = open(p, encoding="utf-8").read()
new = sys.stdin.read().rstrip("\n") + "\n\n"
g = 'if __name__ == "__main__":'
i = s.index(g)
open(p, "w", encoding="utf-8").write(s[:i] + new + s[i:])
