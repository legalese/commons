#!/usr/bin/env python3
"""Check nodes.tsv and edges.tsv against the deposited source texts.

Run as:  python3 -I check-graph.py

The worktree root is found from this file's location (graph/ sits five levels
below it).  Nothing is fetched and nothing is written.  Exit status is 0 only
when no problem is found.

What is checked (every item is a problem if it fails):

Nodes
  * header columns exactly as specified; every row has the same number of
    tab-separated fields; ids unique; kind in the allowed set;
    short_label has at most 6 words.
  * `source` is `path:line` or `path:first-last`; the file exists (UTF-8,
    strict) and the lines exist.  Line numbers count newline characters only
    (form feeds inside the text do not start a line).
  * every date column parses as YYYY-MM-DD (`published` may carry ` HH:MM SGT`).
  * `made`, `published`, `in_force`, `deemed_from` must be found in the text
    of the lines cited by `source` and by any `file.txt:line` tokens in `note`
    (a bare file name in a note stands for the one file of that name under
    subjects/sg/*/registers/source-bundle/).  The search accepts "30th day of
    October 2012", "1st January 2011", "[19th August 1994]", "1 October 1994"
    and "29.2.2004" forms, and, for a time, "5:00 pm" / "5.00 pm" / "5 pm".
    `revoked` is not searched for in the node's own lines: it must equal the
    `effective` date of a `revokes` edge into the node.
  * `added_for_arrow` is empty or names an edge that starts or ends at the node.
Edges
  * header columns exact; ids unique; `from` and `to` are node ids; `kind` is in
    the allowed set.
  * `source` as above; the quote is non-empty, has at most 25 words, and is a
    substring of the cited lines after every run of whitespace is collapsed to
    one space (both sides).
  * dates parse; deemed_from is not later than effective.
  * when `from` is an instrument node with a made or published date, published /
    effective / deemed_from must equal that node's published / in_force /
    deemed_from; when `from` is a section, a schedule, or an instrument known
    only from a Revised Edition (no made or published date), they must be empty.
Text
  * short_label, note and gloss must not contain the words listed in
    FORBIDDEN (the graph states no conclusion about the question).
  * `basis` is `named` or `by-description`.  When the target is a numbered
    section, a `named` quote must contain that section's number (its 2020 number
    or the 2000 number given by renumbering.tsv) as a whole token, and a
    `by-description` quote must not.  For any other target the label is the
    extractor's judgement and is not checked.
Uncited file
  * header exact; every row has the same number of fields; every file named in
    `looked_in` exists.
tv-path.tsv
  * one row for every node, with the same `on_tv_path` as nodes.tsv, which is
    `yes`, `not-decided` or `no`.  A `yes` row has a source and a quotation of at
    most 25 words that is a substring of the cited lines and contains one of the
    words receiver, television, broadcasting apparatus or TVRO; a row that is not
    `yes` has neither.  Every row has a `why`, which may not contain a
    conclusion word, and every file.txt:line token in it must exist.
renumbering.tsv
  * each row cites one line of the printed 2020 Revised Edition's Comparative
    Table; the whole line, whitespace collapsed, must be `<new> <old>`.  Every
    TA section node (except section 2, which the table does not list) must have a
    row, every row must be used, and every "then section N", "numbered N in the
    2000 Revised Edition" or "section N of the 2000 Revised Edition" in a note or
    gloss must name an old number that has a row.
"""
import datetime
import glob
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
if not (ROOT / 'subjects').is_dir():
    sys.exit('cannot find the worktree root above %s' % HERE)

NODE_COLS = ['id', 'short_label', 'full_citation', 'kind', 'made', 'published',
             'in_force', 'deemed_from', 'revoked', 'source', 'added_for_arrow',
             'note', 'on_tv_path']
EDGE_COLS = ['edge_id', 'from', 'to', 'kind', 'published', 'effective',
             'deemed_from', 'source', 'quote', 'gloss', 'basis']
TV_COLS = ['id', 'on_tv_path', 'source', 'quote', 'why']
RENUM_COLS = ['new_2020', 'old_2000', 'source', 'quote', 'used_for']
TV_VALUES = {'yes', 'not-decided', 'no'}
BASIS_VALUES = {'named', 'by-description'}
TV_WORDS = ['receiver', 'television', 'broadcasting apparatus', 'tvro']
NO_RENUMBERING_ROW = {'2'}   # section 2 is not listed in the Comparative Table
UNCITED_COLS = ['uncited_id', 'from', 'to', 'kind', 'reason', 'looked_in',
                'missing']
NODE_KINDS = {'Act', 'section', 'regulations', 'schedule', 'order',
              'notification', 'technical-specification'}
EDGE_KINDS = {'made-under', 'amends', 'revokes', 'replaces', 'saves',
              'carves-out', 'defines-by-list', 'cites'}
INSTRUMENT_KINDS = {'Act', 'regulations', 'order', 'notification',
                    'technical-specification'}
FORBIDDEN = ['offence', 'offender', 'guilty', 'liable', 'illegal', 'unlawful',
             'lawful', 'prohibited', 'must hold', 'must have', 'need a licence',
             'needs a licence', 'no licence is required', 'does not need',
             'not required to', 'is required to']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

problems = []


def problem(where, msg):
    problems.append('%s: %s' % (where, msg))


_file_cache = {}


def file_lines(rel):
    """Return the list of lines of rel (path relative to ROOT), or None."""
    if rel in _file_cache:
        return _file_cache[rel]
    p = ROOT / rel
    lines = None
    if p.is_file():
        data = p.read_bytes().decode('utf-8')  # strict
        lines = data.split('\n')
        if lines and lines[-1] == '':
            lines.pop()
    _file_cache[rel] = lines
    return lines


def collapse(s):
    return re.sub(r'\s+', ' ', s).strip()


def parse_tsv(path, cols, where):
    p = HERE / path
    if not p.is_file():
        problem(where, 'missing file %s' % path)
        return []
    raw = p.read_bytes().decode('utf-8')
    rows = raw.split('\n')
    if rows and rows[-1] == '':
        rows.pop()
    if not rows:
        problem(where, 'empty file')
        return []
    header = rows[0].split('\t')
    if header != cols:
        problem(where, 'header is %r, expected %r' % (header, cols))
        return []
    out = []
    for i, line in enumerate(rows[1:], start=2):
        f = line.split('\t')
        if len(f) != len(cols):
            problem('%s line %d' % (where, i),
                    '%d fields, expected %d' % (len(f), len(cols)))
            continue
        d = dict(zip(cols, f))
        d['_line'] = i
        out.append(d)
    return out


SRC_RE = re.compile(r'^(?P<path>[^:\s]+):(?P<a>\d+)(?:-(?P<b>\d+))?$')


def resolve_source(src, where):
    """Return (rel, a, b, text) for a path:line[-line] string, or None."""
    m = SRC_RE.match(src.strip())
    if not m:
        problem(where, 'source %r is not path:line or path:first-last' % src)
        return None
    rel = m.group('path')
    a = int(m.group('a'))
    b = int(m.group('b')) if m.group('b') else a
    lines = file_lines(rel)
    if lines is None:
        problem(where, 'source file %s does not exist' % rel)
        return None
    if not (1 <= a <= b <= len(lines)):
        problem(where, 'lines %d-%d outside %s (%d lines)' % (a, b, rel, len(lines)))
        return None
    return rel, a, b, ' '.join(lines[a - 1:b])


# index of bare file names for the tokens in notes
BASENAMES = {}
for f in glob.glob(str(ROOT / 'subjects/sg/*/registers/source-bundle/*.txt')):
    BASENAMES.setdefault(Path(f).name, []).append(str(Path(f).relative_to(ROOT)))

TOKEN_RE = re.compile(r'([A-Za-z0-9][A-Za-z0-9_.\-]*\.txt):(\d+)(?:-(\d+))?')


def note_tokens(note, where):
    """Yield texts of the lines cited by file.txt:line tokens in a note."""
    texts = []
    for m in TOKEN_RE.finditer(note):
        name = m.group(1)
        paths = BASENAMES.get(name)
        if not paths:
            problem(where, 'note cites %s, which is not a deposited text' % name)
            continue
        if len(paths) > 1:
            problem(where, 'note cites %s, which is ambiguous' % name)
            continue
        a = int(m.group(2))
        b = int(m.group(3)) if m.group(3) else a
        res = resolve_source('%s:%d-%d' % (paths[0], a, b), where + ' (note token)')
        if res:
            texts.append(res[3])
    return texts


def parse_date(s, with_time=False):
    pat = r'^(\d{4}-\d{2}-\d{2})( \d{2}:\d{2} SGT)?$' if with_time else r'^(\d{4}-\d{2}-\d{2})$'
    m = re.match(pat, s)
    if not m:
        return None, None
    try:
        d = datetime.date.fromisoformat(m.group(1))
    except ValueError:
        return None, None
    tm = (m.group(2) or '').strip() if with_time else ''
    return d, tm


def date_in_text(d, text):
    t = collapse(text)
    mon = MONTHS[d.month - 1]
    dd = d.day
    pats = [
        r'(?<!\d)0?%d(?:st|nd|rd|th)?(?!\d)[^0-9]{0,15}%s\s+%d(?!\d)' % (dd, mon, d.year),
        r'(?<!\d)0?%d\.0?%d\.%d(?!\d)' % (dd, d.month, d.year),
    ]
    return any(re.search(p, t, re.I) for p in pats)


def time_in_text(hhmm, text):
    h, m = int(hhmm[:2]), int(hhmm[3:5])
    h12 = h % 12 or 12
    suffix = 'pm' if h >= 12 else 'am'
    t = collapse(text)
    if m == 0:
        p = r'(?<![\d:.])%d(?:[:.]00)?\s*%s\b' % (h12, suffix)
    else:
        p = r'(?<![\d:.])%d[:.]%02d\s*%s\b' % (h12, m, suffix)
    return re.search(p, t, re.I) is not None


def forbidden(where, text):
    low = text.lower()
    for w in FORBIDDEN:
        if w in low:
            problem(where, 'contains the word/phrase %r (the graph states no conclusion)' % w)


def main():
    nodes = parse_tsv('nodes.tsv', NODE_COLS, 'nodes.tsv')
    edges = parse_tsv('edges.tsv', EDGE_COLS, 'edges.tsv')
    uncited = parse_tsv('edges-uncited.tsv', UNCITED_COLS, 'edges-uncited.tsv')
    tvrows = parse_tsv('tv-path.tsv', TV_COLS, 'tv-path.tsv')
    renum = parse_tsv('renumbering.tsv', RENUM_COLS, 'renumbering.tsv')

    by_id = {}
    for n in nodes:
        w = 'nodes.tsv line %d (%s)' % (n['_line'], n['id'])
        if not n['id'] or n['id'] in by_id:
            problem(w, 'id empty or repeated')
        by_id[n['id']] = n
        if n['kind'] not in NODE_KINDS:
            problem(w, 'kind %r not allowed' % n['kind'])
        if len(n['short_label'].split()) > 6 or not n['short_label'].strip():
            problem(w, 'short_label must be 1-6 words: %r' % n['short_label'])
        for col in ('short_label', 'note'):
            forbidden(w + ' ' + col, n[col])
        if n['on_tv_path'] not in TV_VALUES:
            problem(w, 'on_tv_path %r is not one of %s' % (n['on_tv_path'], sorted(TV_VALUES)))

    edge_ids = {}
    for e in edges:
        w = 'edges.tsv line %d (%s)' % (e['_line'], e['edge_id'])
        if not e['edge_id'] or e['edge_id'] in edge_ids:
            problem(w, 'edge_id empty or repeated')
        edge_ids[e['edge_id']] = e

    # ---- nodes: sources and dates
    for n in nodes:
        w = 'nodes.tsv line %d (%s)' % (n['_line'], n['id'])
        res = resolve_source(n['source'], w) if n['source'] else None
        if not n['source']:
            problem(w, 'source is empty')
        texts = [res[3]] if res else []
        texts += note_tokens(n['note'], w)
        union = ' '.join(texts)
        for col in ('made', 'in_force', 'deemed_from', 'revoked'):
            v = n[col]
            if not v:
                continue
            d, _ = parse_date(v)
            if d is None:
                problem(w, '%s=%r is not YYYY-MM-DD' % (col, v))
                continue
            if col != 'revoked' and not date_in_text(d, union):
                problem(w, '%s=%s is not found in the cited lines' % (col, v))
        if n['published']:
            d, tm = parse_date(n['published'], with_time=True)
            if d is None:
                problem(w, 'published=%r is not YYYY-MM-DD[ HH:MM SGT]' % n['published'])
            else:
                if not date_in_text(d, union):
                    problem(w, 'published=%s is not found in the cited lines' % n['published'])
                if tm and not time_in_text(tm[:5], union):
                    problem(w, 'published time %s is not found in the cited lines' % tm)
        if n['deemed_from'] and n['in_force']:
            d1, _ = parse_date(n['deemed_from'])
            d2, _ = parse_date(n['in_force'])
            if d1 and d2 and d1 > d2:
                problem(w, 'deemed_from is later than in_force')
        if n['revoked']:
            ok = any(e['kind'] == 'revokes' and e['to'] == n['id'] and e['effective'] == n['revoked']
                     for e in edges)
            if not ok:
                problem(w, 'revoked=%s matches the effective date of no revokes edge into this node'
                        % n['revoked'])
        a = n['added_for_arrow']
        if a:
            e = edge_ids.get(a)
            if e is None:
                problem(w, 'added_for_arrow %r is not an edge id' % a)
            elif n['id'] not in (e['from'], e['to']):
                problem(w, 'added_for_arrow %s does not start or end at this node' % a)

    # ---- edges
    kinds = {}
    for e in edges:
        w = 'edges.tsv line %d (%s)' % (e['_line'], e['edge_id'])
        if e['from'] not in by_id:
            problem(w, 'from %r is not a node id' % e['from'])
        if e['to'] not in by_id:
            problem(w, 'to %r is not a node id' % e['to'])
        if e['kind'] not in EDGE_KINDS:
            problem(w, 'kind %r not allowed' % e['kind'])
        kinds[e['kind']] = kinds.get(e['kind'], 0) + 1
        res = resolve_source(e['source'], w)
        q = e['quote']
        if not q.strip():
            problem(w, 'quote is empty')
        elif len(q.split()) > 25:
            problem(w, 'quote has %d words (limit 25)' % len(q.split()))
        if res and q.strip():
            if collapse(q) not in collapse(res[3]):
                problem(w, 'quote is not a substring of %s:%d-%d' % (res[0], res[1], res[2]))
        forbidden(w + ' gloss', e['gloss'])
        if not e['gloss'].strip():
            problem(w, 'gloss is empty')
        if e['basis'] not in BASIS_VALUES:
            problem(w, 'basis %r is not one of %s' % (e['basis'], sorted(BASIS_VALUES)))
        dates = {}
        for col in ('published', 'effective', 'deemed_from'):
            v = e[col]
            if not v:
                dates[col] = None
                continue
            d, tm = parse_date(v, with_time=(col == 'published'))
            if d is None:
                problem(w, '%s=%r does not parse' % (col, v))
            dates[col] = d
        if dates.get('deemed_from') and dates.get('effective') and dates['deemed_from'] > dates['effective']:
            problem(w, 'deemed_from is later than effective')
        src = by_id.get(e['from'])
        if src:
            if src['kind'] in INSTRUMENT_KINDS and (src['made'] or src['published']):
                if e['published'] != src['published']:
                    problem(w, 'published %r differs from node %s published %r'
                            % (e['published'], src['id'], src['published']))
                # An edge repeats its instrument's deemed_from, or leaves it empty
                # when the instrument has a split commencement (in_force differs
                # from deemed_from); a wholly retrospective instrument's edges
                # must carry it.  effective is the deemed day when there is one.
                if e['deemed_from'] not in ('', src['deemed_from']):
                    problem(w, 'deemed_from %r differs from node %s deemed_from %r'
                            % (e['deemed_from'], src['id'], src['deemed_from']))
                if src['deemed_from'] and src['deemed_from'] == src['in_force'] \
                        and e['deemed_from'] != src['deemed_from']:
                    problem(w, 'node %s is wholly retrospective, so the edge must carry deemed_from %s'
                            % (src['id'], src['deemed_from']))
                want = e['deemed_from'] or src['in_force']
                if e['effective'] != want:
                    problem(w, 'effective %r should be %r (node %s)' % (e['effective'], want, src['id']))
            else:
                # sections, schedules, and instruments known only from a Revised
                # Edition (no made or published date) carry no edge dates
                for col in ('published', 'effective', 'deemed_from'):
                    if e[col]:
                        problem(w, '%s must be empty when from is a %s node with no made/published date'
                                % (col, src['kind']))

    # ---- uncited file
    for u in uncited:
        w = 'edges-uncited.tsv line %d (%s)' % (u['_line'], u['uncited_id'])
        for part in [p.strip() for p in u['looked_in'].split(';') if p.strip()]:
            if file_lines(part) is None:
                problem(w, 'looked_in file %s does not exist' % part)
        for col in ('reason', 'missing'):
            if not u[col].strip():
                problem(w, '%s is empty' % col)
        forbidden(w + ' reason', u['reason'])

    # ---- renumbering.tsv
    old_numbers = set()
    new_numbers = set()
    used = {}
    for r in renum:
        w = 'renumbering.tsv line %d (%s/%s)' % (r['_line'], r['new_2020'], r['old_2000'])
        res = resolve_source(r['source'], w)
        old_numbers.add(r['old_2000'])
        new_numbers.add(r['new_2020'])
        if not r['used_for'].strip():
            problem(w, 'used_for is empty')
        if res:
            line = collapse(res[3])
            if res[1] != res[2]:
                problem(w, 'source must be a single line')
            if collapse(r['quote']) != line:
                problem(w, 'quote %r is not the whole cited line %r' % (r['quote'], line))
            if line != '%s %s' % (r['new_2020'], r['old_2000']):
                problem(w, 'the cited line %r is not "<new> <old>" = "%s %s"'
                        % (line, r['new_2020'], r['old_2000']))
    for n in nodes:
        m = re.match(r'^TA_s(\d+[A-Z]?)(?:_\d+)?$', n['id'])
        if m and m.group(1) not in new_numbers and m.group(1) not in NO_RENUMBERING_ROW:
            problem('nodes.tsv (%s)' % n['id'], 'no renumbering row for section %s' % m.group(1))
    num_res = [re.compile(r'then section (\d+[A-Z]?)'),
               re.compile(r'numbered (\d+[A-Z]?)(?:\(\d+\))? in the 2000 Revised Edition'),
               re.compile(r'section (\d+[A-Z]?)(?:\(\d+\))?(?:\([a-z]\))? of the 2000 Revised Edition')]
    new_res = re.compile(r'section (\d+[A-Z]?)(?:\(\d+\))?(?:\([a-z]\))? of the 2020 Revised Edition')
    for who, text in [('nodes.tsv (%s) note' % n['id'], n['note']) for n in nodes] + \
                     [('edges.tsv (%s) gloss' % e['edge_id'], e['gloss']) for e in edges]:
        for rx in num_res:
            for m in rx.finditer(text):
                if m.group(1) not in old_numbers:
                    problem(who, 'names old section %s, which has no row in renumbering.tsv' % m.group(1))
        for m in new_res.finditer(text):
            if m.group(1) not in new_numbers:
                problem(who, 'names 2020 section %s, which has no row in renumbering.tsv' % m.group(1))

    # ---- edge basis against the target's section number
    for e in edges:
        w = 'edges.tsv line %d (%s)' % (e['_line'], e['edge_id'])
        to = by_id.get(e['to'])
        if not to or e['basis'] not in BASIS_VALUES:
            continue
        m = re.match(r'^(?:BA|TA|TAS)_s(\d+[A-Z]?)(?:_\d+)?$', to['id'])
        if not m:
            continue
        nums = {m.group(1)}
        for r in renum:
            if r['new_2020'] == m.group(1) and to['id'].startswith('TA_'):
                nums.add(r['old_2000'])
        has = any(re.search(r'(?<![\w.])%s(?![\w])' % re.escape(x), e['quote']) for x in nums)
        if e['basis'] == 'named' and not has:
            problem(w, 'basis is named but the quote has none of the section numbers %s of %s'
                    % (sorted(nums), to['id']))
        if e['basis'] == 'by-description' and has:
            problem(w, 'basis is by-description but the quote contains a section number %s of %s'
                    % (sorted(nums), to['id']))

    # ---- tv-path.tsv
    tv_ids = {}
    for t in tvrows:
        w = 'tv-path.tsv line %d (%s)' % (t['_line'], t['id'])
        if t['id'] in tv_ids:
            problem(w, 'id repeated')
        tv_ids[t['id']] = t
        n = by_id.get(t['id'])
        if n is None:
            problem(w, 'id is not a node id')
            continue
        if t['on_tv_path'] != n['on_tv_path']:
            problem(w, 'on_tv_path %r differs from nodes.tsv %r' % (t['on_tv_path'], n['on_tv_path']))
        if not t['why'].strip():
            problem(w, 'why is empty')
        forbidden(w + ' why', t['why'])
        note_tokens(t['why'], w + ' why')
        if t['on_tv_path'] == 'yes':
            res = resolve_source(t['source'], w) if t['source'] else None
            q = t['quote']
            if not t['source']:
                problem(w, 'a yes row needs a source')
            if not q.strip():
                problem(w, 'a yes row needs a quotation')
            elif len(q.split()) > 25:
                problem(w, 'quote has %d words (limit 25)' % len(q.split()))
            if res and q.strip():
                if collapse(q) not in collapse(res[3]):
                    problem(w, 'quote is not a substring of %s:%d-%d' % (res[0], res[1], res[2]))
            if q.strip() and not any(x in q.lower() for x in TV_WORDS):
                problem(w, 'a yes quotation must name a receiver, television, broadcasting apparatus or TVRO')
        elif t['source'] or t['quote']:
            problem(w, 'a row that is not yes has no source or quote')
    for n in nodes:
        if n['id'] not in tv_ids:
            problem('tv-path.tsv', 'no row for node %s' % n['id'])

    # ---- report
    touched = set()
    for e in edges:
        touched.add(e['from'])
        touched.add(e['to'])
    isolated = [n['id'] for n in nodes if n['id'] not in touched]
    added = [n['id'] for n in nodes if n['added_for_arrow']]
    print('worktree root: %s' % ROOT)
    print('nodes: %d' % len(nodes))
    print('edges: %d' % len(edges))
    print('edges per kind: ' + ', '.join('%s=%d' % (k, kinds.get(k, 0)) for k in sorted(EDGE_KINDS)))
    print('nodes added for an arrow: %d' % len(added))
    tvc = {}
    for n in nodes:
        tvc[n['on_tv_path']] = tvc.get(n['on_tv_path'], 0) + 1
    print('nodes by on_tv_path: ' + ', '.join('%s=%d' % (k, tvc.get(k, 0)) for k in sorted(TV_VALUES)))
    bc = {}
    for e in edges:
        bc[e['basis']] = bc.get(e['basis'], 0) + 1
    print('edges by basis: ' + ', '.join('%s=%d' % (k, bc.get(k, 0)) for k in sorted(BASIS_VALUES)))
    print('renumbering rows: %d' % len(renum))
    print('nodes with no edge: %d %s' % (len(isolated), isolated))
    print('uncited rows: %d' % len(uncited))
    print('problems: %d' % len(problems))
    for p in problems:
        print('  PROBLEM ' + p)
    return 0 if not problems else 1


if __name__ == '__main__':
    sys.exit(main())
