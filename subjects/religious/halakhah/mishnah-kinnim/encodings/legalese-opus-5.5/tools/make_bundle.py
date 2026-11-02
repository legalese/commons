"""Slice the fetched he.wikisource renderings into the commons source bundle.

Usage: python3 -I make_bundle.py RAW_DIR BUNDLE_DIR
RAW_DIR holds page-NN.txt and manifest.jsonl from fetch_wikisource.py.
Each deposited file is a contiguous run of lines of one page, copied byte for byte;
the slice boundaries are recorded in the .meta.json as `verified_how`.
"""
import hashlib
import json
import sys

raw, out = sys.argv[1], sys.argv[2]
manifest = [json.loads(l) for l in open(f"{raw}/manifest.jsonl", encoding="utf-8")]


def lines(i):
    return open(f"{raw}/page-{i:02d}.txt", encoding="utf-8").read().split("\n")


def between(ls, start, stop):
    a = ls.index(start)
    b = ls.index(stop, a + 1) if stop else len(ls)
    while b > a and not ls[b - 1].strip():
        b -= 1
    return a, b


CH = {0: "1", 1: "2", 2: "3"}
HEB = {0: "א", 1: "ב", 2: "ג"}
specs = []
for i in (0, 1, 2):
    specs.append(dict(page=i, sid=f"mishnah-kinnim-{CH[i]}", start="משנה א", stop="משנה מנוקדת", skip_start=False,
                      title=f"Mishnah Kinnim, chapter {CH[i]} (משנה קינים פרק {HEB[i]}), the printed text (נוסח הדפוסים), standard numbering",
                      kind="primary-text", authoritative=True,
                      notes="The Mishnah's text, unvocalised, as he.wikisource prints it under each chapter's first heading. Standard numbering: 4, 5 and 6 units in chapters 1 to 3. Square brackets in a line are the page's own (a variant reading)."))
for i in (0, 1, 2):
    specs.append(dict(page=i, sid=f"mishnah-kinnim-{CH[i]}-rambam-recension", start='נוסח הרמב"ם', stop="הערות", skip_start=True,
                      title=f"Mishnah Kinnim, chapter {CH[i]}, in Maimonides' recension (נוסח הרמב\"ם)",
                      kind="textual-witness", authoritative=False,
                      notes="A second witness to the same text, used only where a word differs. Parenthesised numbers are the standard division; bracketed numbers are Maimonides' division (5, 6 and 5 units), as the page's own note says."))
for i, c in ((3, "1"), (4, "2"), (5, "3")):
    specs.append(dict(page=i, sid=f"bartenura-kinnim-{c}", start="(א)", stop=None, skip_start=False,
                      title=f"R. Ovadiah of Bertinoro (d. c. 1515) on Mishnah Kinnim, chapter {c}",
                      kind="commentary", authoritative=False,
                      notes="An aid: the standard printed commentary. Its unit numbers in parentheses follow the standard division."))
specs.append(dict(page=6, sid="tiferet-yisrael-kinnim-3", start="יכין", stop=None, skip_start=False,
                  title="R. Israel Lipschutz (1782-1860), Tiferet Yisrael (Yakhin and Boaz) on Mishnah Kinnim, chapter 3",
                  kind="commentary", authoritative=False,
                  notes="An aid. The page says it was made by automatic OCR and needs full proofreading ('דף זה נוצר מתוך המרת סריקת קבצים אוטומטית בתוכנת OCR. דרושה הגהה מלאה'); quote it with that caution."))
specs.append(dict(page=7, sid="rambam-pesulei-hamukdashin-8", start="הלכה א", stop="הגהה", skip_start=False,
                  title="Maimonides, Mishneh Torah, Hilkhot Pesulei ha-Mukdashin, chapter 8 (Vilna-Warsaw print)",
                  kind="code", authoritative=False,
                  notes="An aid: Maimonides' code, which rules on the same mixtures and reads Kinnim 3:2 differently (halakhot 6 and 7)."))

for s in specs:
    m = manifest[s["page"]]
    ls = lines(s["page"])
    a, b = between(ls, s["start"], s["stop"])
    if s["skip_start"]:
        a += 1
    text = "\n".join(ls[a:b]) + "\n"
    sha = hashlib.sha256(text.encode()).hexdigest()
    with open(f"{out}/{s['sid']}.txt", "w", encoding="utf-8") as f:
        f.write(text)
    page_url = "https://he.wikisource.org/w/index.php?oldid=" + str(m["revid"])
    meta = {
        "title": s["title"],
        "source_id": s["sid"],
        "landing_url": "https://he.wikisource.org/wiki/" + m["title"].replace(" ", "_"),
        "revision_url": page_url,
        "revision_id": m["revid"],
        "indexed_date": m["fetched"][:10],
        "text_deposited": True,
        "in_force": "no: Temple offerings have not been brought since 70 CE; the text is law as the Mishnah states it",
        "kind": s["kind"],
        "language": "he",
        "text_sha256": sha,
        "lines": text.count("\n"),
        "verified_how": (f"Fetched page '{m['title']}' (revision {m['revid']}) through the MediaWiki parse API on {m['fetched']} "
                         "with the commons source-fetcher User-Agent (robots.txt allows the API to all user agents). "
                         "The rendered HTML was converted to one line per paragraph or line break by a script (tags stripped, entities unescaped, "
                         "blank lines dropped). This file is lines " + str(a + 1) + " to " + str(b) + " of that rendering, copied unchanged."),
        "authoritative": s["authoritative"],
        "licence": "Text: public domain (the Mishnah c. 200 CE; the commentaries before 1900). Wikisource page: CC BY-SA 4.0, he.wikisource contributors.",
        "notes": s["notes"],
    }
    with open(f"{out}/{s['sid']}.meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(s["sid"], meta["lines"], sha[:12])
