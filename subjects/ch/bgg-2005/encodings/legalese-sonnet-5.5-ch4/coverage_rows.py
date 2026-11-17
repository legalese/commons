"""Build the coverage rows from the text, by script: one row per heading, paragraph, list item and sentence-level split.
Imported by coverage.py."""
import re, unicodedata
SPLIT = {  # line -> list of (row suffix, text-start marker): the line is cut before each later marker
 111: [('first sentence', None), ('second sentence', 'Auf dem Gebiet der internationalen Rechtshilfe in Strafsachen ist es nicht')],
 125: [('first sentence', None), ('second sentence', 'Artikel 58 Absatz 1 Buchstabe b findet')],
 129: [('first sentence', None), ('second sentence', 'Es kann ganz oder teilweise')],
 139: [('first sentence', None), ('second sentence', '…')],
 147: [('first sentence', None), ('second sentence', 'Die Parteien können in diesem Fall'), ('third sentence', 'Der Entscheid ist nicht vollstreckbar')],
}
def load(text_path):
    raw = open(text_path, encoding='utf-8').read().split('\n')
    while raw and raw[-1] == '': raw.pop()   # the file ends with a newline: 166 lines, not 167
    return raw
def rows(raw):
    R = []
    art = None; para = None
    def add(rid, a, b, text, kind):
        R.append(dict(id=rid, a=a, b=b, text=text, kind=kind, art=art))
    # header: lines 1-5
    add('File header', 1, 5, raw[0], 'header')
    for n in range(6, len(raw) + 1):
        line = raw[n - 1]
        if line.strip() == '': continue
        if n >= 151:
            continue  # footnotes: one row below
        if re.match(r'^\d+\. Kapitel', line):
            add('Chapter 4 heading', n, n, line, 'heading'); continue
        m = re.match(r'^(\d+)\. Abschnitt', line)
        if m:
            add(f'Section {m.group(1)} heading', n, n, line, 'heading'); continue
        m = re.match(r'^Art\. (\d+[a-z]*)\b ?(.*)$', line)
        if m:
            art = m.group(1); para = None
            add(f'Art {art} heading', n, n, line, 'heading'); continue
        m = re.match(r'^  ([a-z])\.(?:\[\^\d+\])? (.*)$', line)
        if m:
            add(f'Art {art}({para})({m.group(1)})' if para else f'Art {art}({m.group(1)})', n, n, line, 'item'); continue
        m = re.match(r'^(\d+) (.*)$', line)
        if m:
            para = m.group(1)
            rid = f'Art {art}({para})'
            if n in SPLIT:
                for suffix, marker in SPLIT[n]:
                    add(f'{rid} {suffix}', n, n, line, 'sentence')
            else:
                add(rid, n, n, line, 'para')
            continue
        # an article with an unnumbered body line
        para = None
        has_items = n + 1 <= len(raw) and re.match(r'^  [a-z]\.', raw[n])
        add(f'Art {art} (intro)' if has_items else f'Art {art}', n, n, line, 'para')
    add('Footnotes (amendment history)', 151, len(raw), raw[150], 'footnotes')
    return R
def sentence_text(raw, n, rid):
    line = raw[n - 1]
    if n not in SPLIT: return line
    marks = SPLIT[n]
    idx = [i for i, (s, m) in enumerate(marks) if rid.endswith(s)][0]
    start = 0 if marks[idx][1] is None else line.index(marks[idx][1])
    end = len(line) if idx + 1 >= len(marks) else line.index(marks[idx + 1][1])
    return line[start:end].strip()
