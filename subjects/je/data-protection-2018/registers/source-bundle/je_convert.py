#!/usr/bin/python3 -I
"""je_convert.py IN.html OUT.txt TITLE CITATION URL RETRIEVED_UTC : plain-text conversion of a jerseylaw.je "current laws" page.
Deterministic, standard library only; run as `python3 -I je_convert.py ...` (the input is untrusted data).
Body = the HTML between the page's 'Page Content' marker and 'Back to top'.
Dropped: contents-list paragraphs (class MsoToc*), display:none elements, script and style, the coat-of-arms images.
Block elements become lines, whitespace is collapsed, and the iLAWS paragraph, sub-paragraph, clause and sub-clause classes are
indented by 2, 4, 6 and 8 spaces.  Table rows read "| a | b |".  Endnote markers [n] and the endnotes are kept.
A formula the source sets as an image is marked "[image in source not converted: <file>]".  Prints the sha256 and size of IN and OUT.
Written for legalese/commons, 2026-11-26; the converter that made the earlier subjects/je deposits was not kept in the repository."""
import hashlib, re, sys
from html.parser import HTMLParser

BLOCK = {"p", "div", "tr", "li", "h1", "h2", "h3", "h4", "h5", "h6", "br", "hr", "table", "ul", "ol", "tbody", "thead"}
VOID = {"br", "hr", "img", "meta", "link", "input"}
CREST = ("iLAWS101", "iLAWS115")


def indent_for(cls):
    for c in cls:
        m = re.match(r"iLAWS(\d{3})", c)
        if not m:
            continue
        n = int(m.group(1))
        if n in (301, 310, 311, 410, 411): return 2
        if n in (320, 321): return 4
        if n in (330, 331): return 6
        if n in (340, 341): return 8
    return 0


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lines, self.cur = [], []
        self.skip_tag, self.skip_depth = None, 0   # inside a dropped element
        self.indent = 0
        self.row = None
        self.cell = None
        self.crest = 0
        self.images = []

    def flush(self):
        s = re.sub(r"\s+", " ", "".join(self.cur)).strip()
        self.cur = []
        if s:
            self.lines.append(" " * self.indent + s)

    def put(self, s):
        (self.cell if self.cell is not None else self.cur).append(s)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get("class") or "").split()
        style = (a.get("style") or "").replace(" ", "").lower()
        if self.skip_tag is not None:
            if tag == self.skip_tag and tag not in VOID: self.skip_depth += 1
            return
        if tag in ("script", "style") or "display:none" in style or any(c.startswith("MsoToc") for c in cls):
            if tag not in VOID:
                self.skip_tag, self.skip_depth = tag, 1
            return
        if tag == "img":
            if self.crest: return
            src = (a.get("src") or "")
            self.put("[image in source not converted: %s]" % src.rsplit("/", 1)[-1]); self.images.append(src)
            return
        if tag == "tr":
            self.flush(); self.row = []; return
        if tag in ("td", "th"):
            self.cell = []; return
        if tag in BLOCK and self.cell is None:
            self.flush()
        if tag == "p":
            self.indent = indent_for(cls)
            if any(c.startswith(CREST) for c in cls): self.crest += 1

    def handle_endtag(self, tag):
        if self.skip_tag is not None:
            if tag == self.skip_tag:
                self.skip_depth -= 1
                if self.skip_depth == 0: self.skip_tag = None
            return
        if tag in ("td", "th") and self.cell is not None:
            c = re.sub(r"\s+", " ", re.sub(r"[ ]", " ", " ".join(self.cell))).strip()
            if self.row is not None: self.row.append(c)
            self.cell = None
        elif tag == "tr" and self.row is not None:
            if any(self.row): self.lines.append("| " + " | ".join(self.row) + " |")
            self.row = None
        elif tag in BLOCK and self.cell is None:
            self.flush()
            if tag == "p": self.crest = 0; self.indent = 0

    def handle_data(self, data):
        if self.skip_tag is None:
            self.put(data)


def main():
    src_path, out_path, title, citation, url, retrieved = sys.argv[1:7]
    raw = open(src_path, "rb").read()
    html = raw.decode("utf-8")
    i = html.find("Page Content"); j = html.find("Back to top")
    assert 0 <= i < j, "markers not found"
    p = P(); p.feed(html[i + len("Page Content"):j]); p.flush()
    m = re.search(r"Showing the law from\s*([^<]{3,60}?)\s*(?:<|$)", html)
    showing = re.sub(r"\s+", " ", m.group(1)).strip() if m else "?"
    head = f"""{title}
Citation: {citation}
Source: {url} (jerseylaw.je, Jersey Legal Information Board), Official Consolidated Version
Currency: the page showed "Showing the law from {showing}" when retrieved
Retrieved: {retrieved} (UTC)

UNOFFICIAL VERSION. This is a plain-text conversion made by Legalese Commons from the HTML of the
official consolidated version on jerseylaw.je. It is not an official text and may contain conversion
errors. The jerseylaw.je Disclaimer says: "Nothing within this site should be relied upon as
constituting verified or official text." Check the source before relying on anything here.

Licence: Contains States Assembly information licensed under the Open States Assembly Licence – Jersey v1.0.

Conversion: the contents list is dropped; Part, Article, paragraph and Schedule headings and numbers
are kept, with sub-levels indented by two spaces; tables are rows "| a | b |"; endnote markers [n]
and the endnotes (legislative history) are kept; formulae that the source sets as images are marked
"[image in source not converted: <file>]".
==============================================================================
"""
    txt = head + "\n".join(p.lines) + "\n"
    open(out_path, "w", encoding="utf-8").write(txt)
    sha = lambda b: hashlib.sha256(b).hexdigest()
    print("in  sha256", sha(raw), len(raw), "bytes")
    print("out sha256", sha(txt.encode("utf-8")), len(txt), "chars", len(txt.splitlines()), "lines", "| images not converted:", len(p.images), "| showing:", showing)


if __name__ == "__main__":
    main()
