"""Render .l4.in templates: replace `{{Q ID N M}}` with the quote lines srcrefs.py prints.

Usage: python3 -I render.py SRCREFS BUNDLE_DIR OUT_DIR TEMPLATE...
`{{Q mishnah-kinnim-3 8 11}}` becomes the `-- src:mishnah-kinnim-3:N | ...` lines for raw lines 8 to 11
of BUNDLE_DIR/mishnah-kinnim-3.txt, exactly as `srcrefs.py quoteid` prints them, at the
placeholder's indentation. Nothing else in the template is touched.
"""
import os
import re
import subprocess
import sys

srcrefs, bundle, outdir, templates = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
pat = re.compile(r"^(\s*)\{\{Q ([A-Za-z][\w.-]*) (\d+) (\d+)\}\}\s*$")


def quote(sid: str, n: str, m: str) -> list[str]:
    out = subprocess.run([sys.executable, "-I", srcrefs, "quoteid", f"{bundle}/{sid}.txt", n, m],
                         check=True, capture_output=True, text=True).stdout
    return [l for l in out.split("\n") if l.strip()]


for t in templates:
    lines = []
    for line in open(t, encoding="utf-8").read().split("\n"):
        mm = pat.match(line)
        if mm:
            ind = mm.group(1)
            lines.extend(ind + q for q in quote(mm.group(2), mm.group(3), mm.group(4)))
        else:
            if "{{Q" in line:
                sys.exit(f"{t}: malformed placeholder: {line!r}")
            lines.append(line)
    name = os.path.basename(t)[:-3]
    with open(f"{outdir}/{name}", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(name)
