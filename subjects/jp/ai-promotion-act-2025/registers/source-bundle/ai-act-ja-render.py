"""Render the e-Gov law XML of Act No. 53 of 2025 as plain text, one sentence per line.

Usage:  python3 -I ai-act-ja-render.py ai-act-ja.xml > ai-act-ja.txt

Why: the encoding quotes the Japanese with `-- src:ai-act-ja:N | text` lines, which need
a plain-text file with stable line numbers. The XML is the deposited original; this file
is a rendering of it and adds no words. What it does, element by element:

  LawTitle, LawNum           one line each
  TOC                        "目次", then one line per chapter (title + article range),
                             then the supplementary-provisions label
  ChapterTitle               one line
  ArticleCaption             one line (the article heading, e.g. （目的）)
  Paragraph                  each Sentence on its own line; the first Sentence of the
                             paragraph is prefixed with the ArticleTitle (first
                             paragraph) or the ParagraphNum (later paragraphs), joined
                             by an ideographic space U+3000
  Item                       each Sentence on its own line, the first prefixed with the
                             ItemTitle and U+3000
  SupplProvisionLabel        one line

Nothing else is emitted. Attributes (such as Extract="true" on the supplementary
provisions) are not rendered; the .meta.json beside the text records them.
"""

import sys
import xml.etree.ElementTree as ET

IDEOGRAPHIC_SPACE = "　"


def text_of(el):
    return "".join(el.itertext()).strip() if el is not None else ""


def sentences(container):
    return [text_of(s) for s in container.iter("Sentence")]


def emit_paragraph(out, para, lead):
    sents = []
    ps = para.find("ParagraphSentence")
    if ps is not None:
        sents = sentences(ps)
    for i, s in enumerate(sents):
        out.append((lead + IDEOGRAPHIC_SPACE + s) if (i == 0 and lead) else s)
    for item in para.findall("Item"):
        isents = sentences(item.find("ItemSentence"))
        title = text_of(item.find("ItemTitle"))
        for i, s in enumerate(isents):
            out.append((title + IDEOGRAPHIC_SPACE + s) if i == 0 else s)


def emit_article(out, art):
    cap = art.find("ArticleCaption")
    if cap is not None:
        out.append(text_of(cap))
    title = text_of(art.find("ArticleTitle"))
    for n, para in enumerate(art.findall("Paragraph")):
        lead = title if n == 0 else text_of(para.find("ParagraphNum"))
        emit_paragraph(out, para, lead)


def main(path):
    root = ET.parse(path).getroot()
    out = []
    body = root.find("LawBody")
    out.append(text_of(body.find("LawTitle")))
    out.append(text_of(root.find("LawNum")))
    toc = body.find("TOC")
    if toc is not None:
        out.append(text_of(toc.find("TOCLabel")))
        for ch in toc.findall("TOCChapter"):
            out.append(text_of(ch.find("ChapterTitle")) + text_of(ch.find("ArticleRange")))
        sp = toc.find("TOCSupplProvision")
        if sp is not None:
            out.append(text_of(sp.find("SupplProvisionLabel")))
    for ch in body.find("MainProvision").findall("Chapter"):
        out.append(text_of(ch.find("ChapterTitle")))
        for art in ch.findall("Article"):
            emit_article(out, art)
    for sp in body.findall("SupplProvision"):
        out.append(text_of(sp.find("SupplProvisionLabel")))
        for art in sp.findall("Article"):
            emit_article(out, art)
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main(sys.argv[1])
