#!/usr/bin/env python3
"""Extract plain UTF-8 text from Planalto's compiled Código Penal HTML.

Usage: python3 extract.py del2848compilado.htm > codigo-penal-1940.txt

One source paragraph per output line. The page declares no charset and is
Windows-1252 (cp1252), not ISO-8859-1: decoded as ISO-8859-1, byte 0x96 (an en
dash in "Pena – reclusão") became the C1 control U+0096 on 80 lines, and 0x94
became U+0094 on one. That was the first extraction, corrected 2026-09-29. Text Planalto
struck through (<strike>, six occurrences, all revoked matter) is kept but
wrapped as ⟦STRUCK: …⟧ so it can never be read as current law. Nothing else is
rewritten: amendment notes such as "(Redação dada pela Lei nº …)" and
"(Incluído pela Lei nº …)" stay inline, because they are the annotation
inventory P2 disposes of.
"""
import html, re, sys, unicodedata

raw = open(sys.argv[1], "rb").read().decode("cp1252")
s = re.sub(r"(?is)<strike>(.*?)</strike>", lambda m: "⟦STRUCK: " + m.group(1) + "⟧", raw)
s = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", "", s)
s = re.sub(r"(?i)<br\s*/?>", "\n", s)
s = re.sub(r"(?i)</?(p|div|tr|h\d|table|center)[^>]*>", "\n", s)
s = re.sub(r"<[^>]+>", "", s)
s = html.unescape(s).replace("\r", "").replace("\xa0", " ")
lines = [re.sub(r"[ \t]+", " ", l).strip() for l in s.split("\n")]
paras = [re.sub(r"\s*\n\s*", " ", p).strip() for p in re.split(r"\n\s*\n", "\n".join(lines))]
# Two lines (art. 121-A § 2º and art. 339) arrive in decomposed form (NFD:
# "a" + U+0300 for "à"). Normalise to NFC so a quotation typed or copied in the
# ordinary composed form matches the text byte for byte.
sys.stdout.write(unicodedata.normalize("NFC", "\n".join(p for p in paras if p)) + "\n")
