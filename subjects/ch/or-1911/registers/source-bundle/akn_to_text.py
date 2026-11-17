#!/usr/bin/env python3
"""akn_to_text.py IN.xml OUT.txt SELECTOR [SELECTOR ...]   (standard library only; run as python3 -I; use /usr/bin/python3 where the Homebrew Python lacks expat)
Renders parts of a Fedlex Akoma Ntoso XML file (the official consolidated text of a Swiss federal act) as plain text.
A SELECTOR is an eId of an article, a range of articles, or a chapter / section:
    art_336            one article
    art_336..art_336_b  the articles from the first to the second in document order
    chap_3             a chapter (every section and article in it)
    all                the whole body
Each selected article is printed under the headings that contain it (title, chapter, section: number and heading), then as
"Art. 336 <heading>", every paragraph on its own line led by its number, list items on indented lines led by their letter,
tables not occurring in the selections used so far.  A footnote (authorialNote) is printed as [^N] at its place and as "[^N] text" after the text.
Nothing is reworded: the text nodes are joined with whitespace collapsed."""
import re, sys, xml.etree.ElementTree as ET


def tag(e):
    return e.tag.split("}")[-1] if isinstance(e.tag, str) else ""


NOTES = []


def walk(e, buf):
    t = tag(e)
    if t == "authorialNote":
        txt = re.sub(r"\s+", " ", "".join(e.itertext())).strip()
        NOTES.append(txt); buf.append("[^%d]" % len(NOTES)); return
    if e.text: buf.append(e.text)
    for c in e:
        walk(c, buf)
        if c.tail: buf.append(c.tail)


def text_of(e):
    buf = []; walk(e, buf)
    return re.sub(r"\s+", " ", "".join(buf)).strip()


def label(e):
    for c in e:
        if tag(c) == "num": return text_of(c)
    return ""


def heading(e):
    for c in e:
        if tag(c) == "heading": return text_of(c)
    return ""


def render_block(e, depth, out, lead=""):
    """e is a paragraph, item, content, blockList or p; lead is the label to put before the first line"""
    pad = "  " * depth
    t = tag(e)
    if t in ("paragraph", "item", "point", "indent"):
        lab = label(e); first = True
        for c in e:
            if tag(c) in ("num", "heading"): continue
            if tag(c) == "p":
                tx = text_of(c)
                out.append(pad + (lab + " " if lab and first else "") + tx); first = False
            elif tag(c) in ("content", "blockList"):
                n0 = len(out); render_block(c, depth, out)
                if first and lab and len(out) > n0:
                    out[n0] = pad + lab + " " + out[n0].lstrip(); first = False
            else:
                out.append(pad + text_of(c)); first = False
        if first and lab: out.append(pad + lab)
        return
    if t == "content":
        for c in e: render_block(c, depth, out)
        return
    if t == "blockList":
        for c in e:
            if tag(c) == "listIntroduction": out.append(pad + text_of(c))
            elif tag(c) == "listWrapUp": out.append(pad + text_of(c))
            elif tag(c) == "item": render_block(c, depth + 1, out)
            else: out.append(pad + text_of(c))
        return
    if t == "p":
        out.append(pad + text_of(e)); return
    tx = text_of(e)
    if tx: out.append(pad + tx)


def render_article(a, out):
    out.append((label(a) + " " + heading(a)).strip())
    for c in a:
        if tag(c) in ("num", "heading"): continue
        if tag(c) in ("paragraph", "content", "blockList", "p"): render_block(c, 0, out)
        else:
            tx = text_of(c)
            if tx: out.append(tx)
    out.append("")


def main():
    src, dst = sys.argv[1:3]; sels = sys.argv[3:]
    root = ET.parse(src).getroot()
    parent = {c: p for p in root.iter() for c in p}
    body = [e for e in root.iter() if tag(e) == "body"][0]
    arts = [a for a in root.iter() if tag(a) == "article"]
    ids = [a.get("eId") for a in arts]
    chosen = []
    for s in sels:
        if s == "all": chosen += arts
        elif ".." in s:
            a, b = s.split(".."); chosen += arts[ids.index(a): ids.index(b) + 1]
        elif s.startswith("art_"): chosen.append(arts[ids.index(s)])
        else:
            el = [e for e in root.iter() if e.get("eId") == s][0]
            chosen += [a for a in el.iter() if tag(a) == "article"]
    seen = set(); chosen = [a for a in chosen if not (id(a) in seen or seen.add(id(a)))]
    out = []; last = None
    for a in chosen:
        chain = []; p = parent.get(a)
        while p is not None and p is not body:
            if tag(p) in ("chapter", "section", "title", "part", "level", "subdivision", "book"):
                lab = (label(p) + " " + heading(p)).strip()
                if not lab:
                    # fedlex puts the number and heading of a subdivision in its first child
                    lab = text_of(p[0]) if len(p) else ""
                    lab = lab[:100]
                chain.append(lab)
            p = parent.get(p)
        chain.reverse()
        if chain != last:
            if out and out[-1] != "": out.append("")
            for i, c in enumerate(chain):
                if last is None or i >= len(last) or last[i] != c: out.append(c)
            last = chain; out.append("")
        render_article(a, out)
    for i, n in enumerate(NOTES, 1): out.append("[^%d] %s" % (i, n))
    open(dst, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("wrote %s: %d articles, %d lines, %d words, %d footnotes" % (dst, len(chosen), len(out), sum(len(l.split()) for l in out), len(NOTES)))


if __name__ == "__main__":
    main()
