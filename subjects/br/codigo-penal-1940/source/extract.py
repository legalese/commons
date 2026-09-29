#!/usr/bin/env python3
"""Extract plain UTF-8 text from Planalto's compiled Código Penal HTML.

Usage: python3 extract.py del2848compilado.htm > codigo-penal-1940.txt

One source paragraph per output line. The page is ISO-8859-1. Text Planalto
struck through (<strike>, six occurrences, all revoked matter) is kept but
wrapped as ⟦STRUCK: …⟧ so it can never be read as current law. Nothing else is
rewritten: amendment notes such as "(Redação dada pela Lei nº …)" and
"(Incluído pela Lei nº …)" stay inline, because they are the annotation
inventory P2 disposes of.
"""
import html, re, sys

raw = open(sys.argv[1], "rb").read().decode("iso-8859-1")
s = re.sub(r"(?is)<strike>(.*?)</strike>", lambda m: "⟦STRUCK: " + m.group(1) + "⟧", raw)
s = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", "", s)
s = re.sub(r"(?i)<br\s*/?>", "\n", s)
s = re.sub(r"(?i)</?(p|div|tr|h\d|table|center)[^>]*>", "\n", s)
s = re.sub(r"<[^>]+>", "", s)
s = html.unescape(s).replace("\r", "").replace("\xa0", " ")
lines = [re.sub(r"[ \t]+", " ", l).strip() for l in s.split("\n")]
paras = [re.sub(r"\s*\n\s*", " ", p).strip() for p in re.split(r"\n\s*\n", "\n".join(lines))]
sys.stdout.write("\n".join(p for p in paras if p) + "\n")
