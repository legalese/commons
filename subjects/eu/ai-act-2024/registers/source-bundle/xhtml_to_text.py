#!/usr/bin/env python3
"""xhtml_to_text.py IN.xhtml OUT.txt : plain-text rendering of an EU Publications Office XHTML text (Official Journal act or consolidated version).
Deterministic, standard library only.  Run it as `python3 -I xhtml_to_text.py IN OUT` (the input is untrusted data).
What it does (and every thing it does that the older mechanical extraction in the AI Act subject did not):
  - one block (heading, paragraph, list item, table row) per line; a list label such as "(a)" or "1." is joined to its text, so a quote line is a whole sentence;
  - an amendment marker of a consolidated version (anchors in p.arrow / p.modref, titled e.g. "32026R1744: REPLACED") becomes its own line "▼M1 REPLACED" / "▼B";
  - a footnote reference (a superscript inside a link) becomes "[^N]" and the footnote itself "[^N] text";
  - any other superscript (an exponent) becomes "^N", so 10<sup>25</sup> reads "10^25" and not "1025" (the older extraction flattened it);
  - table rows read "| cell | cell |".
It does not drop or reorder text.  Writes the sha256 of IN and OUT to stdout."""
import hashlib, html, re, sys
from html.parser import HTMLParser

BLOCK = {"p", "div", "tr", "table", "li", "h1", "h2", "h3", "h4", "ul", "ol", "br", "hr", "tbody", "thead", "body", "head", "title"}
SKIP = {"script", "style", "head", "title"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []          # finished lines
        self.cur = []          # pieces of the current line
        self.skip = 0
        self.stack = []        # (tag, classes)
        self.in_a = 0
        self.row = None        # list of cell strings while inside a tr
        self.cell = None

    # ---- helpers
    def flush(self):
        s = "".join(self.cur)
        s = re.sub(r"[ \t   ]+", " ", s).strip()
        self.cur = []
        if s:
            self.out.append(s)

    def add(self, s):
        if self.cell is not None:
            self.cell.append(s)
        else:
            self.cur.append(s)

    # ---- parser callbacks
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get("class") or "").split()
        self.stack.append((tag, cls))
        if tag in SKIP:
            self.skip += 1
            return
        if tag == "tr":
            self.flush()
            self.row = []
            return
        if tag in ("td", "th"):
            self.cell = []
            return
        if tag == "a":
            self.in_a += 1
            t = a.get("title") or ""
            m = re.match(r"^\d{5}[A-Z]\d{4}: ([A-Z]+)", t)
            if m and ("modref" in self._parent_classes() or "arrow" in self._parent_classes()):
                self._marker = m.group(1)
            return
        if tag == "span" and "superscript" in cls:
            self._sup = True
            self.add("")  # position marker
            return
        if tag in BLOCK and self.cell is None:
            self.flush()

    def _parent_classes(self):
        return self.stack[-2][1] if len(self.stack) >= 2 else []

    def handle_endtag(self, tag):
        if tag in SKIP:
            self.skip -= 1
        if tag == "a":
            self.in_a -= 1
        if tag in ("td", "th") and self.cell is not None:
            c = re.sub(r"\s+", " ", " ".join(self.cell)).strip()
            if self.row is not None:
                self.row.append(c)
            self.cell = None
        elif tag == "tr" and self.row is not None:
            if any(self.row):
                self.out.append("| " + " | ".join(self.row) + " |")
            self.row = None
        elif tag in BLOCK and self.cell is None:
            self.flush()
        # pop to the matching tag (the markup is XHTML, but be tolerant)
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if self.skip:
            return
        top = self.stack[-1] if self.stack else ("", [])
        if top[0] == "a" and getattr(self, "_marker", None) and re.fullmatch(r"\s*[▼►]\s*(B|M\d+)\s*", data):
            kind = self._marker
            self._marker = None
            m = re.search(r"(B|M\d+)", data)
            tag = m.group(1)
            self.flush()
            self.out.append("▼" + tag + ("" if tag == "B" else " " + kind))
            return
        if top[0] == "a" and re.fullmatch(r"\s*[▼►]\s*(B|M\d+)\s*", data):
            m = re.search(r"(B|M\d+)", data)
            self.flush()
            self.out.append("▼" + m.group(1))
            return
        if top[0] == "span" and "superscript" in top[1]:
            d = data.strip()
            if not d:
                return
            if self.in_a:                      # a footnote reference
                self.add("[^" + d.lstrip("*") + "]" if not d.startswith("*") else "[^*" + d.lstrip("*") + "]")
            else:                              # an exponent
                self.add("^" + d)
            return
        self.add(data)


def render(src):
    p = P()
    p._marker = None
    p._sup = False
    p.feed(src)
    p.flush()
    lines = p.out
    # join a bare list label to the text that follows it
    lab = re.compile(r"^(\(\d+[a-z]?\)|\([a-z]{1,4}\)|\(?[ivxl]+\)|\d+[a-z]?\.|—|–|-|•|[a-z]\))$")
    res, i = [], 0
    while i < len(lines):
        l = lines[i]
        if lab.match(l) and i + 1 < len(lines) and not lines[i + 1].startswith(("▼", "|")):
            res.append(l + " " + lines[i + 1])
            i += 2
            continue
        res.append(l)
        i += 1
    # a footnote body line starts "(^1) ..." or "([^1]) ..."; normalise it to "[^1] ..."
    out = []
    for l in res:
        l = re.sub(r"^\(\s*\[\^(\*?\d+)\]\s*\)\s*", r"[^\1] ", l)
        out.append(l)
    return "\n".join(out) + "\n"


def main():
    src = open(sys.argv[1], encoding="utf-8").read()
    txt = render(src)
    open(sys.argv[2], "w", encoding="utf-8").write(txt)
    sha = lambda b: hashlib.sha256(b).hexdigest()
    print("in  sha256", sha(open(sys.argv[1], "rb").read()))
    print("out sha256", sha(txt.encode("utf-8")), len(txt.splitlines()), "lines", len(txt), "chars")


if __name__ == "__main__":
    main()
