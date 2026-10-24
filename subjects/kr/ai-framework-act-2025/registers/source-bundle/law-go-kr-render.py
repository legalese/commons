"""Render a law.go.kr statute body (the HTML that lsInfoR.do serves) as plain text.

Usage: python3 -I law-go-kr-render.py IN.html OUT.txt

One paragraph, item or sub-item of the statute per line, as the page lays them out.
Whitespace inside a line is squeezed to single spaces; empty lines are dropped.
The site's own navigation before the statute's title line (the line carrying
"( 약칭:") is dropped, and so is everything from the first annex-download line
("[별표 ") onward, which is the page's list of annex files, not statute text.
Nothing else is changed: no character of the statute text is added, removed
or reordered.
"""

import re
import sys
from html.parser import HTMLParser

BLOCK = {"br", "p", "div", "tr", "li", "h1", "h2", "h3", "h4", "table"}


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in BLOCK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        if tag in BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def main(src, dst):
    p = Text()
    with open(src, encoding="utf-8") as f:
        p.feed(f.read())
    lines = []
    for raw in "".join(p.out).split("\n"):
        line = re.sub(r"[ \t ]+", " ", raw).strip()
        if line:
            lines.append(line)
    start = next(i for i, l in enumerate(lines) if "( 약칭:" in l)
    end = next((i for i, l in enumerate(lines) if l.startswith("[별표 ")), len(lines))
    with open(dst, "w", encoding="utf-8") as f:
        f.write("\n".join(lines[start:end]) + "\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
