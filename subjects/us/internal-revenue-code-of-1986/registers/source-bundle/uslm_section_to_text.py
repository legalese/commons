#!/usr/bin/env python3
"""uslm_section_to_text.py SECTION_ID IN.xml OUT.txt  (standard library only; run as python3 -I)
Renders one section of an OLRC USLM XML title (for example SECTION_ID /us/usc/t26/s121) as plain text:
the section number and heading, then every level (subsection, paragraph, subparagraph, clause, subclause, item, subitem)
indented two spaces per level with its number, its heading and its text, tables one row per line with cells separated by ' | ',
and the section's source credit last.  The editorial, statutory and amendment notes that follow the section are not rendered
(the section's <notes> element is skipped), and the tables of contents are not part of a section.
The converter does not edit the wording of a section: it joins the text nodes of each paragraph with single spaces collapsed."""
import re, sys, xml.etree.ElementTree as ET

LEVELS = ("subsection", "paragraph", "subparagraph", "clause", "subclause", "item", "subitem", "subsubitem")


def tag(e):
    return e.tag.split("}")[-1] if isinstance(e.tag, str) else ""


FOOTNOTES = []


def walk(e, buf):
    """text of e: a footnote reference reads [^N] and its note is collected into FOOTNOTES; other tags are dropped"""
    t = tag(e)
    if t == "note" and e.get("type") == "footnote":
        nid = e.get("id")
        if nid not in [n[0] for n in FOOTNOTES]:
            FOOTNOTES.append((nid, re.sub(r"\s+", " ", "".join(e.itertext())).strip()))
        return
    if t == "ref" and e.get("class") == "footnoteRef":
        buf.append("[^" + "".join(e.itertext()).strip() + "]")
        if e.tail: buf.append(e.tail)
        return
    if e.text: buf.append(e.text)
    for c in e:
        walk(c, buf)
        if c.tail and not (tag(c) == "ref" and c.get("class") == "footnoteRef"): buf.append(c.tail)   # walk() already appended a footnote reference's own tail


def text_of(e):
    """all text under e, tags removed, whitespace collapsed; a table is rendered one row per line."""
    if tag(e) == "table":
        rows = []
        for tr in e.iter():
            if tag(tr) == "tr":
                cells = [text_of(c) for c in tr if tag(c) in ("td", "th")]
                rows.append(" | ".join(cells))
        return "\n".join(rows)
    buf = []
    walk(e, buf)
    return re.sub(r"\s+", " ", "".join(buf)).strip()


def render(e, depth, out):
    t = tag(e)
    pad = "  " * depth
    if t in LEVELS:
        num = ""; head = ""
        for c in e:
            if tag(c) == "num": num = text_of(c)
            elif tag(c) == "heading": head = text_of(c)
        first = len(out); out.append((pad + (num + " " if num else "") + (head if head else "")).rstrip()); nohead = not head
        for c in e:
            ct = tag(c)
            if ct in ("num", "heading"): continue
            if ct in LEVELS: render(c, depth + 1, out)
            elif ct in ("chapeau", "content", "continuation"):
                # a content/chapeau may hold paragraphs or a table
                kids = [k for k in c if tag(k) in ("p", "table")]
                if kids:
                    for k in kids:
                        for ln in text_of(k).split("\n"): out.append(pad + "  " + ln)
                else:
                    tx = text_of(c)
                    if tx and nohead and len(out) == first + 1: out[first] += " " + tx
                    elif tx: out.append(pad + "  " + tx)
            elif ct in ("notes", "sourceCredit"): pass
            else:
                tx = text_of(c)
                if tx: out.append(pad + "  " + tx)
    return


def main():
    sid, src, dst = sys.argv[1:4]
    notes_dst = sys.argv[4] if len(sys.argv) > 4 else None   # optional: a second file with the section's own editorial, statutory and amendment notes
    want = None
    for ev, e in ET.iterparse(src, events=("end",)):
        if tag(e) == "section" and e.get("identifier") == sid:
            want = e; break
    if want is None: sys.exit("section %s not found" % sid)
    out = []
    num = head = ""; credit = ""
    for c in want:
        if tag(c) == "num": num = text_of(c)
        elif tag(c) == "heading": head = text_of(c)
        elif tag(c) == "sourceCredit": credit = text_of(c)
    out.append((num + " " + head).strip())
    for c in want:
        ct = tag(c)
        if ct in LEVELS: render(c, 0, out)
        elif ct in ("chapeau", "content", "continuation"):
            tx = text_of(c)
            if tx: out.append("  " + tx)
    if credit: out.append(credit)
    for nid, tx in FOOTNOTES: out.append("[^" + tx.split(" ", 1)[0] + "] " + (tx.split(" ", 1)[1] if " " in tx else ""))
    if notes_dst:
        nl = ["Notes that follow " + (num + " " + head).strip() + " in the OLRC edition (editorial, statutory and amendment notes; they are not part of the section's text)", ""]
        for nt in want:
            if tag(nt) != "notes": continue
            for n in nt:
                if tag(n) != "note": continue
                hd = [text_of(h) for h in n if tag(h) == "heading"]
                nl.append(hd[0] if hd else "Note")
                for k in n:
                    if tag(k) == "heading": continue
                    tx = text_of(k)
                    if tx: nl.append("  " + tx)
                nl.append("")
        open(notes_dst, "w", encoding="utf-8").write("\n".join(nl))
        print("wrote %s: %d lines" % (notes_dst, len(nl)))
    open(dst, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("wrote %s: %d lines, %d chars, %d words" % (dst, len(out), sum(len(l) + 1 for l in out), sum(len(l.split()) for l in out)))


if __name__ == "__main__":
    main()
