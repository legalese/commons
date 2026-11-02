"""Fetch he.wikisource pages through the MediaWiki parse API and write plain text.

Usage: python3 -I fetch_wikisource.py OUTDIR TITLE [TITLE ...]
Writes OUTDIR/<n>.json (raw API answer) and prints, per page, title, revid and the
rendered text's sha256. Rendering: <br>, </p>, </div>, </li>, headings -> newline;
tags stripped; entities unescaped; blank runs collapsed. One line of the page is one
line of output. Sleeps 3 s between requests (Wikimedia etiquette).
"""
import hashlib
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request

UA = "legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)"


def render(t: str) -> str:
    t = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", "", t)
    t = re.sub(r"(?s)<sup[^>]*class=\"reference\"[^>]*>.*?</sup>", "", t)
    t = re.sub(r"<br\s*/?>|</p>|</div>|</h\d>|</li>|</dd>|</dt>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    lines = [re.sub(r"[ \t ]+", " ", ln).strip() for ln in t.split("\n")]
    return "\n".join(ln for ln in lines if ln) + "\n"


def main() -> None:
    outdir, titles = sys.argv[1], sys.argv[2:]
    for i, title in enumerate(titles):
        url = ("https://he.wikisource.org/w/api.php?action=parse&prop=text|revid"
               "&disableeditsection=1&format=json&page=" + urllib.parse.quote(title))
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
        d = json.loads(raw)["parse"]
        text = render(d["text"]["*"])
        stem = f"{outdir}/page-{i:02d}"
        with open(stem + ".json", "wb") as f:
            f.write(raw)
        with open(stem + ".txt", "w", encoding="utf-8") as f:
            f.write(text)
        print(json.dumps({"i": i, "title": d["title"], "revid": d["revid"],
                          "fetched": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                          "sha256": hashlib.sha256(text.encode()).hexdigest(),
                          "lines": text.count("\n")}, ensure_ascii=False))
        time.sleep(3)


if __name__ == "__main__":
    main()
