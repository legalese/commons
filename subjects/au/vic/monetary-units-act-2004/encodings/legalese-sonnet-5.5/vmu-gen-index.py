#!/usr/bin/env python3
"""Generate vmu-provisions.l4, vmu-xrefs.l4 and vmu-tests-xrefs.l4 from the text file.

Usage, from this folder:   python3 -I vmu-gen-index.py [--out DIR] [--report] [--units]
Reads ../../registers/source-bundle/monetary-units-act-2004.txt, lines 22 to 135, and writes the three files into DIR
(default: this folder).
With --report it prints every reference the script found, with the heading of its target, and writes nothing.
With --units it prints the units the text was split into and writes nothing.

How it reads the text.
Lines 22 to 135 are split into units: a section heading, a section's opening words or undivided body, a subsection, a paragraph,
a subparagraph or a definition, each with the identifier as printed ("s 9(2)(a)(ii)", "s 3 'fee'").
A side note belongs to the unit its own label names.
References are found by pattern in each unit's own text: "section N" and "sections N, M and K" (with a pinpoint such as 5(3) when printed),
"subsection (n)" and "subsections (n) and (m)" with a following paragraph path such as (1)(c), "this section" (also when capitalised at the start of a sentence), and "section N of the X Act" or "Part N of the X Act" for another Act.
A pinpoint is resolved against the unit that holds it: a bare "subsection (4)" in section 5 means s 5(4).
A mention of "this Act" and a citation inside a side note are not rows.
"""
import re, sys, json, os


HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, '..', '..', 'registers', 'source-bundle', 'monetary-units-act-2004.txt')
FIRST, LAST = 22, 135


def load():
    with open(RAW, encoding='utf-8') as f:
        data = f.read().split('\n')
    return data  # data[i-1] is line i


def parse():
    data = load()
    units = []
    sidenotes = []  # (line, label, text)
    cur_sec = None
    cur_heading = None
    cur_sub = None
    cur_para = None
    cur_subpara = None

    def add(uid, kind, line, text, sec=None, extra=None):
        u = dict(id=uid, kind=kind, section=sec if sec is not None else cur_sec,
                 heading=cur_heading, line=line, lines=[line], text=text)
        if extra:
            u.update(extra)
        units.append(u)
        return u

    for n in range(FIRST, LAST + 1):
        raw = data[n - 1]
        if not raw.strip():
            continue
        m = re.match(r'^\[Side note: (.*)\]$', raw)
        if m:
            sidenotes.append(dict(line=n, text=m.group(1)))
            continue
        m = re.match(r'^(\d+) (.+)$', raw)
        if m and not raw.startswith(' '):
            cur_sec = m.group(1)
            cur_heading = m.group(2)
            cur_sub = cur_para = cur_subpara = None
            add('s %s heading' % cur_sec, 'section heading', n, raw, extra=dict(num=cur_sec))
            continue
        if raw.startswith('* * * * *'):
            add('end-marker-%d' % n, 'blank marker', n, raw, sec='')
            continue
        if raw.startswith('═'):
            add('divider', 'divider', n, raw, sec='')
            continue
        m = re.match(r'^      \(([ivx]+)\) (.*)$', raw)
        if m:
            cur_subpara = m.group(1)
            base = 's %s' % cur_sec
            if cur_sub:
                base += '(%s)' % cur_sub
            base += '(%s)(%s)' % (cur_para, cur_subpara)
            add(base, 'subparagraph', n, raw.strip())
            continue
        m = re.match(r'^    \(([a-z])\) (.*)$', raw)
        if m:
            cur_para = m.group(1)
            cur_subpara = None
            base = 's %s' % cur_sec
            if cur_sub:
                base += '(%s)' % cur_sub
            base += '(%s)' % cur_para
            add(base, 'paragraph', n, raw.strip())
            continue
        m = re.match(r'^  \((\d+[A-Z]?)\) (.*)$', raw)
        if m:
            cur_sub = m.group(1)
            cur_para = cur_subpara = None
            add('s %s(%s)' % (cur_sec, cur_sub), 'subsection', n, raw.strip())
            continue
        m = re.match(r'^  (.*)$', raw)
        if m:
            body = m.group(1)
            if cur_sec == '3' and not body.startswith('In this Act'):
                term = re.match(r'^(.+?) (includes|means|has) ', body).group(1)
                add("s 3 '%s'" % term, 'definition', n, body, extra=dict(term=term))
            else:
                # opening words or undivided body of a section
                cur_sub = cur_para = cur_subpara = None
                add('s %s body' % cur_sec, 'section body', n, body)
            continue
        raise SystemExit('unparsed line %d: %r' % (n, raw))

    # attach side notes by their own label
    for sn in sidenotes:
        t = sn['text']
        label = None
        m = re.match(r'^S\. (\d+[A-Z]?)(\((\d+[A-Z]?)\))? ?(def\. of ([a-z ]+?) )?(inserted|amended|substituted)', t)
        if m:
            sec, _, sub, _, term, _ = m.groups()
            if term:
                label = "s %s '%s'" % (sec, term)
            elif sub:
                label = 's %s(%s)' % (sec, sub)
            else:
                label = 's %s' % sec
        elif t.startswith('Ss 13'):
            label = 'end-marker-131'
        elif t.startswith('Schs 1, 2'):
            label = 'end-marker-133'
        sn['label'] = label
    return units, sidenotes


def assign_sidenotes(units, sidenotes):
    byid = {}
    for u in units:
        byid.setdefault(u['id'], []).append(u)
    for sn in sidenotes:
        lab = sn['label']
        if lab is None:
            raise SystemExit('side note without label: %r' % sn)
        # a section label such as "s 4" attaches to the section heading unit; "s 10" likewise
        tgt = None
        if lab in byid:
            cands = byid[lab]
            tgt = cands[0]
        elif lab + ' heading' in byid:
            tgt = byid[lab + ' heading'][0]
        else:
            raise SystemExit('side note label not found: %r' % lab)
        tgt['lines'].append(sn['line'])
        tgt.setdefault('sidenotes', []).append(sn)
    for u in units:
        u['lines'].sort()
    return units


def units_all():
    units, sidenotes = parse()
    units = assign_sidenotes(units, sidenotes)
    return units, sidenotes


if '--units' in sys.argv:
    units, sidenotes = units_all()
    covered = set()
    for u in units:
        covered.update(u['lines'])
    data = load()
    missing = [n for n in range(FIRST, LAST + 1) if data[n - 1].strip() and n not in covered]
    for u in units:
        print('%-22s %-16s lines %s  [%s]' % (u['id'], u['kind'], u['lines'], u['text'][:50]))
    print('units:', len(units), 'sidenotes:', len(sidenotes), 'uncovered non-blank lines:', missing)
    sys.exit(0)


import re, os, sys, json

OUT = HERE if '--out' not in sys.argv else sys.argv[sys.argv.index('--out') + 1]

units, sidenotes = units_all()

# ---------------------------------------------------------------- the index
headings = {}
for u in units:
    if u['kind'] == 'section heading':
        headings[u['num']] = re.match(r'^\d+ (.+)$', u['text']).group(1)

index = []  # dicts: id, kind, heading, line
for u in units:
    if u['kind'] == 'section heading':
        index.append(dict(id='s %s' % u['num'], kind='section', heading=headings[u['num']], line=u['line']))
    elif u['kind'] in ('subsection', 'paragraph', 'subparagraph', 'definition'):
        index.append(dict(id=u['id'], kind=u['kind'], heading=headings[u['section']], line=u['line']))
ids = {e['id']: e for e in index}
assert len(ids) == len(index), 'duplicate ids'

# ---------------------------------------------------------------- the references
PATH = r'\(\w+\)(?:\(\w+\))*'
other_acts = [
    (r'section (\d+) of the (Sentencing Act 1991)', 'section'),
    (r'Part (\d+) of the (Subordinate Legislation Act 1994)', 'Part'),
]
act_titles = ['Subordinate Legislation Act 1994', 'Sentencing Act 1991', 'Petroleum (Submerged Lands) Act 1982']

other_rows = []
int_rows = []


def rel_ids(cites, sec, sub_first=None):
    """cites: list of path strings like '(2)(a)' or '(b)' ; resolve relative to section sec"""
    out = []
    prev_parent = None
    for c in cites:
        parts = re.findall(r'\((\w+)\)', c)
        if len(parts) == 1 and prev_parent is not None and not parts[0][0].isdigit():
            parts = prev_parent + parts
        prev_parent = parts[:-1] if len(parts) > 1 else prev_parent
        out.append('s %s' % sec + ''.join('(%s)' % p for p in parts))
    return out


for u in units:
    if u['kind'] in ('divider', 'blank marker', 'section heading'):
        continue
    text = u['text']
    sec = u['section']
    citing = u['id'] if u['kind'] != 'section body' else 's %s' % sec
    line = u['line']
    consumed = []  # spans consumed by other-act patterns

    def free(span):
        return not any(a < span[1] and span[0] < b for a, b in consumed)

    # other instruments: provision-level
    for pat, kindword in other_acts:
        for m in re.finditer(pat, text):
            consumed.append(m.span())
            other_rows.append(dict(citing=citing, line=line, words=m.group(0), instrument=m.group(2),
                                   provision='%s %s' % (kindword, m.group(1))))
    for t in act_titles:
        for m in re.finditer(re.escape(t), text):
            if free(m.span()):
                consumed.append(m.span())
                other_rows.append(dict(citing=citing, line=line, words='the ' + t if text[max(0, m.start() - 4):m.start()] == 'the ' else t,
                                       instrument=t, provision=''))
    # internal: sections
    for m in re.finditer(r'\bsections? (\d+[A-Z]?(?:\([^)]*\))*(?:(?:, | and | or )\d+[A-Z]?(?:\([^)]*\))*)*)', text):
        if not free(m.span()):
            continue
        words = m.group(0)
        items = re.split(r', | and | or ', m.group(1))
        for it in items:
            mm = re.match(r'(\d+[A-Z]?)((?:\([^)]*\))*)$', it)
            cid = 's %s%s' % (mm.group(1), mm.group(2))
            int_rows.append(dict(citing=citing, line=line, words=words, cited=cid, pos=m.start()))
    # internal: subsections / paragraphs
    for m in re.finditer(r'\bsubsections? (%s(?:(?:, | and | or )%s)*)' % (PATH, PATH), text):
        words = m.group(0)
        items = re.split(r', | and | or ', m.group(1))
        for cid in rel_ids(items, sec):
            int_rows.append(dict(citing=citing, line=line, words=words, cited=cid, pos=m.start()))
    # internal: this section
    for m in re.finditer(r'\b[Tt]his section\b', text):
        int_rows.append(dict(citing=citing, line=line, words=m.group(0), cited='s %s' % sec, pos=m.start()))

int_rows.sort(key=lambda r: (r['line'], r['pos']))
other_rows.sort(key=lambda r: r['line'])
for i, r in enumerate(int_rows, 1):
    r['n'] = i
    e = ids.get(r['cited'])
    r['heading'] = e['heading'] if e else None
    r['in_index'] = e is not None
for i, r in enumerate(other_rows, 1):
    r['n'] = i

# ---------------------------------------------------------------- reports
REPORT = []

class _Sink:
    def write(self, t):
        REPORT.append(t)


if True:
    f = _Sink()
    f.write('INTERNAL ROWS: %d\n' % len(int_rows))
    for r in int_rows:
        f.write('%03d  line %3d  %-14s %-34s -> %-12s %s %s\n' % (r['n'], r['line'], r['citing'], '"%s"' % r['words'], r['cited'],
                                                                     'OK ' if r['in_index'] else 'MISSING', r['heading']))
    f.write('\nOTHER-INSTRUMENT ROWS: %d\n' % len(other_rows))
    for r in other_rows:
        f.write('%03d  line %3d  %-14s %-50s %s | %s\n' % (r['n'], r['line'], r['citing'], '"%s"' % r['words'], r['instrument'], r['provision']))

if '--report' in sys.argv:
    print(''.join(REPORT))
    sys.exit(0)


def s(x):
    assert '"' not in x
    return '"%s"' % x


# ---------------------------------------------------------------- vmu-provisions.l4
def write_provisions(path, with_header=True):
    L = []
    L.append('IMPORT prelude')
    L.append('')
    L.append('-- The provision index of Monetary Units Act 2004 (Victoria), sections 1 to 12, as the text file prints it.')
    L.append('-- Generated by a script that reads the text file (lines 22 to 135): one entry per section, subsection,')
    L.append('-- paragraph, subparagraph and defined term, with its identifier as printed and the heading of its section.')
    L.append('-- A subsection, paragraph or subparagraph has no heading of its own, so it carries the heading of its section.')
    L.append('')
    L.append('DECLARE Provision HAS')
    L.append('    `identifier as printed` IS A STRING')
    L.append('    `kind` IS A STRING')
    L.append('    `heading as printed` IS A STRING')
    L.append('    `first line in the text file` IS A NUMBER')
    L.append('')
    L.append('-- Ruler: identifier, kind, heading, first line in the text file.')
    L.append('`the provision index` MEANS')
    first = True
    for e in index:
        tmpl = '    LIST (Provision OF %s, %s, %s, %d)' if first else '       , (Provision OF %s, %s, %s, %d)'
        L.append(tmpl % (s(e['id']), s(e['kind']), s(e['heading']), e['line']))
        first = False
    L.append('')
    L.append('GIVEN identifier IS A STRING')
    L.append('GIVETH A MAYBE Provision')
    L.append('`the provision with the identifier` MEANS')
    L.append('    CONSIDER filter `has the identifier` `the provision index`')
    L.append('    WHEN EMPTY THEN NOTHING')
    L.append('    WHEN first FOLLOWED BY rest THEN JUST first')
    L.append('    WHERE')
    L.append('        `has the identifier` p MEANS p\'s `identifier as printed` EQUALS identifier')
    L.append('')
    L.append('GIVEN identifier IS A STRING')
    L.append('GIVETH A BOOLEAN')
    L.append('`the identifier is in the index` MEANS')
    L.append('    CONSIDER `the provision with the identifier` identifier')
    L.append('    WHEN NOTHING THEN FALSE')
    L.append('    WHEN JUST p THEN TRUE')
    L.append('')
    L.append('GIVEN identifier IS A STRING')
    L.append('GIVETH A MAYBE STRING')
    L.append('`the heading of the provision with the identifier` MEANS')
    L.append('    CONSIDER `the provision with the identifier` identifier')
    L.append('    WHEN NOTHING THEN NOTHING')
    L.append("    WHEN JUST p THEN JUST (p's `heading as printed`)")
    L.append('')
    open(path, 'w', encoding='utf-8').write('\n'.join(L))


def write_xrefs(path):
    L = []
    L.append('IMPORT prelude')
    L.append('IMPORT `vmu-provisions`')
    L.append('')
    L.append('-- Every reference in sections 1 to 12 of the text from one provision to another provision of the same text,')
    L.append('-- one row per cited provision, found by a script that reads the text file (lines 22 to 135).')
    L.append('-- A citation of several provisions ("sections 5 and 6") gives one row for each, with the words as printed.')
    L.append('-- A subsection, paragraph or subparagraph has no heading of its own, so its row carries the heading of its section.')
    L.append('-- A reference to another Act is a row of its own kind further down; it is not resolved here.')
    L.append('')
    L.append('DECLARE `Cross-reference` HAS')
    L.append('    `citing provision` IS A STRING')
    L.append('    `line of the citation in the text file` IS A NUMBER')
    L.append('    `words as printed` IS A STRING')
    L.append('    `cited identifier` IS A STRING')
    L.append('    `heading of the cited provision` IS A STRING')
    L.append('')
    L.append('DECLARE `Reference to another instrument` HAS')
    L.append('    `citing provision` IS A STRING')
    L.append('    `line of the citation in the text file` IS A NUMBER')
    L.append('    `words as printed` IS A STRING')
    L.append('    `instrument as printed` IS A STRING')
    L.append('    `provision as printed` IS A STRING')
    L.append('')
    L.append('-- Ruler: citing provision, line in the text file, words as printed, cited identifier, heading of the cited provision.')
    for r in int_rows:
        L.append('`xref %03d` MEANS `Cross-reference` OF %s, %d, %s, %s, %s' % (r['n'], s(r['citing']), r['line'], s(r['words']), s(r['cited']), s(r['heading'])))
    L.append('')
    L.append('`the cross-references in the text` MEANS')
    for i, r in enumerate(int_rows):
        L.append('    LIST `xref %03d`' % r['n'] if i == 0 else '       , `xref %03d`' % r['n'])
    L.append('')
    L.append('-- Ruler: citing provision, line in the text file, words as printed, instrument as printed, provision as printed.')
    for r in other_rows:
        L.append('`other-instrument reference %03d` MEANS `Reference to another instrument` OF %s, %d, %s, %s, %s' % (r['n'], s(r['citing']), r['line'], s(r['words']), s(r['instrument']), s(r['provision'])))
    L.append('')
    L.append('`the references to other instruments in the text` MEANS')
    for i, r in enumerate(other_rows):
        L.append('    LIST `other-instrument reference %03d`' % r['n'] if i == 0 else '       , `other-instrument reference %03d`' % r['n'])
    L.append('')
    L.append('-- A row resolves when the cited identifier is in the index and the row\'s heading is the index\'s heading for it.')
    L.append('GIVEN row IS A `Cross-reference`')
    L.append('GIVETH A BOOLEAN')
    L.append('`the cross-reference resolves` MEANS')
    L.append('    CONSIDER `the provision with the identifier` (row\'s `cited identifier`)')
    L.append('    WHEN NOTHING THEN FALSE')
    L.append('    WHEN JUST p THEN p\'s `heading as printed` EQUALS row\'s `heading of the cited provision`')
    L.append('')
    open(path, 'w', encoding='utf-8').write('\n'.join(L))


def write_tests(path):
    L = []
    L.append('IMPORT prelude')
    L.append('IMPORT `vmu-provisions`')
    L.append('IMPORT `vmu-xrefs`')
    L.append('')
    L.append('-- One assertion per row: the cited identifier is in the index and the row\'s heading is the index\'s heading for it.')
    for r in int_rows:
        L.append('#ASSERT `the cross-reference resolves` `xref %03d`' % r['n'])
    L.append('')
    L.append('-- The counts, read from the report of the script that found the rows.')
    L.append('#ASSERT count `the cross-references in the text` EQUALS %d' % len(int_rows))
    L.append('#ASSERT count `the references to other instruments in the text` EQUALS %d' % len(other_rows))
    L.append('#ASSERT count `the provision index` EQUALS %d' % len(index))
    L.append('')
    L.append('-- Spot checks of the index, each expected value read by hand from the text file.')
    L.append('-- Line 55: the heading printed for section 5.')
    L.append('#ASSERT `the heading of the provision with the identifier` "s 5" EQUALS JUST "Calculation of value of fee and penalty units"')
    L.append('-- A subsection carries the heading of its section: line 58 is section 5(3).')
    L.append('#ASSERT `the heading of the provision with the identifier` "s 5(3)" EQUALS JUST "Calculation of value of fee and penalty units"')
    L.append('-- Line 82: section 8(1A) is printed under the heading of section 8 (line 78).')
    L.append('#ASSERT `the heading of the provision with the identifier` "s 8(1A)" EQUALS JUST "Certain monetary amounts to be construed in fee units or penalty units"')
    L.append('-- Line 97: a subparagraph of section 9(2)(a).')
    L.append('#ASSERT `the heading of the provision with the identifier` "s 9(2)(a)(ii)" EQUALS JUST "Regulations"')
    L.append('-- Line 118: the heading of section 11 as printed, with its en dash.')
    L.append('#ASSERT `the heading of the provision with the identifier` "s 11" EQUALS JUST "Provisions for 2012\u20132013"')
    L.append('-- A defined term of section 3 (line 47).')
    L.append('#ASSERT `the identifier is in the index` "s 3 \'penalty\'"')
    L.append('-- The text has no section 13 in this range and no section 5(9).')
    L.append('#ASSERT NOT `the identifier is in the index` "s 13"')
    L.append('#ASSERT NOT `the identifier is in the index` "s 5(9)"')
    L.append('')
    open(path, 'w', encoding='utf-8').write('\n'.join(L))


if __name__ == '__main__':
    write_provisions(os.path.join(OUT, 'vmu-provisions.l4'))
    write_xrefs(os.path.join(OUT, 'vmu-xrefs.l4'))
    write_tests(os.path.join(OUT, 'vmu-tests-xrefs.l4'))
    print('index entries', len(index), 'internal rows', len(int_rows), 'other rows', len(other_rows))
