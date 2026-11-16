#!/usr/bin/env node
/**
 * build-index.mjs — turn a checkout of legalese/commons into a SQL file
 * that loads the D1 search index the L4 Commons MCP server queries
 * (https://commons.utility.workers.dev/mcp). Run by .github/workflows/mcp-index.yml.
 * Nothing under subjects/ depends on it.
 *
 *   node .github/mcp-index/build-index.mjs . index.sql
 *
 * What gets indexed:
 *   laws        one row per subject (a directory holding subject.json)
 *   encodings   one row per encoding of a subject (encoding.json, seat, scope, NOTES.md)
 *   decisions   one row per `@export`ed L4 function: the question it answers,
 *               its parameters (with their @desc), what it returns, where it lives
 *   provisions  one row per `§` / `§§` heading in a non-test .l4 file, with the
 *               comment text under it (usually the quoted statutory text)
 *
 * Laws, decisions and provisions each get an FTS5 table (porter stemming)
 * for ranked search; a law's row also carries its encodings' seats, scopes
 * and NOTES.md, so one law-level hit covers "is this encoded, and how".
 * File contents themselves are not stored: the worker reads them from
 * raw.githubusercontent.com at the commit recorded in `meta`.
 *
 * No dependencies; Node >= 18.
 */

import { readFileSync, readdirSync, statSync, writeFileSync, existsSync } from 'node:fs'
import { join, relative, dirname, basename, sep } from 'node:path'
import { execFileSync } from 'node:child_process'

const root = process.argv[2]
const out = process.argv[3] ?? 'build/index.sql'
if (!root || !existsSync(join(root, 'subjects'))) {
  console.error('usage: node .github/mcp-index/build-index.mjs <commons-checkout> [out.sql]')
  process.exit(2)
}

const SUBJECTS = join(root, 'subjects')
const NOTES_MAX = 6000 // chars of NOTES.md kept per encoding
const CONTEXT_MAX = 1200 // chars of comment kept above an @export
const PROVISION_MAX = 1500 // chars of comment text kept under a § heading
const DECISION_MAX_LINES = 250

// ── walk ─────────────────────────────────────────────────────────────

const repoPath = (abs) => relative(root, abs).split(sep).join('/')

/** All files under `dir`, skipping dot-directories. */
function walk(dir, acc = []) {
  for (const name of readdirSync(dir)) {
    if (name.startsWith('.')) continue
    const p = join(dir, name)
    const st = statSync(p)
    if (st.isDirectory()) walk(p, acc)
    else acc.push(p)
  }
  return acc
}

const files = walk(SUBJECTS)
const fileSet = new Set(files)

// A subject is the *shallowest* directory holding a subject.json (a couple of
// encodings carry their own pipeline subject.json; those are not subjects).
const subjectDirs = files
  .filter((f) => basename(f) === 'subject.json')
  .map(dirname)
  .sort((a, b) => a.length - b.length)
const subjectSet = new Set()
for (const d of subjectDirs) {
  if (![...ancestors(d)].some((a) => subjectSet.has(a))) subjectSet.add(d)
}

function* ancestors(dir) {
  let d = dirname(dir)
  while (d.startsWith(SUBJECTS) && d !== SUBJECTS) {
    yield d
    d = dirname(d)
  }
}

function subjectOf(file) {
  let d = dirname(file)
  let found = null
  while (d.startsWith(SUBJECTS) && d !== SUBJECTS) {
    if (subjectSet.has(d)) found = d
    d = dirname(d)
  }
  if (found || !file.endsWith('.l4')) return found
  // An encoding filed without a subject.json: the subject is the directory
  // holding `encodings/`, or failing that the .l4 file's own directory.
  const rel = relative(SUBJECTS, file).split(sep)
  const i = rel.indexOf('encodings')
  found = i > 0 ? join(SUBJECTS, ...rel.slice(0, i)) : dirname(file)
  subjectSet.add(found)
  return found
}

/** The encoding directory a file belongs to. */
function encodingDirOf(file, subjectDir) {
  const rel = relative(subjectDir, file).split(sep)
  const i = rel.indexOf('encodings')
  if (i === 0 && rel.length > 2) return join(subjectDir, 'encodings', rel[1])
  if (i === 0) return join(subjectDir, 'encodings')
  return dirname(file)
}

const readJson = (p) => {
  try {
    return JSON.parse(readFileSync(p, 'utf8'))
  } catch {
    return null
  }
}
const readText = (p) => (fileSet.has(p) ? readFileSync(p, 'utf8') : null)
const clip = (s, n) => (s == null ? null : s.length > n ? s.slice(0, n) + ' …' : s)
const str = (v) => (v == null ? null : typeof v === 'string' ? v : JSON.stringify(v))

// ── laws ─────────────────────────────────────────────────────────────

const laws = new Map() // law id → row
function lawFor(dir) {
  const id = relative(SUBJECTS, dir).split(sep).join('/')
  if (laws.has(id)) return laws.get(id)
  const sj = readJson(join(dir, 'subject.json')) ?? {}
  const segs = id.split('/')
  const slug = segs[segs.length - 1]
  // `_jurisdiction/library` and the like are shared code, not a jurisdiction level
  const juris = segs.slice(0, -1).filter((s) => !s.startsWith('_'))
  const row = {
    id,
    jurisdiction: juris.length ? juris.join('/') : segs[0],
    name:
      sj.display_name ??
      sj.title ??
      sj.name ??
      (segs.some((s) => s.startsWith('_'))
        ? `Shared L4 library (${id})`
        : slug.charAt(0).toUpperCase() + slug.slice(1).replace(/-/g, ' ')),
    citation: str(sj.citation),
    jurisdiction_label: str(sj.jurisdiction),
    source_url: sj.source?.url ?? sj.sources?.[0]?.url ?? null,
    status: str(sj.status) ?? 'draft',
    files: [],
    encodings: 0,
    decisions: 0,
  }
  laws.set(id, row)
  return row
}

for (const d of subjectSet) lawFor(d)

// ── encodings, decisions, provisions ────────────────────────────────

const encodings = new Map() // encoding id → row
const decisions = []
const provisions = []

const isTestFile = (f) => /(^|[-_.])(tests?|cases?|checks?)([-_.]|$)/i.test(basename(f, '.l4'))

function encodingFor(encDir, law, subjectDir) {
  const id = relative(SUBJECTS, encDir).split(sep).join('/')
  if (encodings.has(id)) return encodings.get(id)
  const ej = readJson(join(encDir, 'encoding.json')) ?? {}
  const notes = readText(join(encDir, 'NOTES.md')) ?? readText(join(subjectDir, 'NOTES.md'))
  const relDir = relative(subjectDir, encDir).split(sep).join('/')
  const row = {
    id,
    law_id: law.id,
    row: relDir === 'encodings' ? '(encodings)' : relDir.replace(/^encodings\//, '') || '(subject)',
    dir: repoPath(encDir),
    seat: str(ej.seat),
    scope: str(ej.scope),
    status: str(ej.status),
    version: str(ej.version),
    edition: str(ej.edition_encoded),
    method: str(ej.method),
    modules: JSON.stringify(ej.modules ?? []),
    cases: JSON.stringify(ej.cases ?? []),
    notes: clip(notes, NOTES_MAX),
    decisions: 0,
  }
  encodings.set(id, row)
  law.encodings++
  return row
}

const IDENT = String.raw`(\`[^\`]+\`|[A-Za-z_][\w']*)`
const RE_PARAM = new RegExp(
  String.raw`^\s*(?:GIVEN\s+)?${IDENT}\s+IS\s+(?:AN?\s+)?(.+?)(?:\s+@desc\s+(.*))?\s*$`
)
const RE_DECIDE = new RegExp(String.raw`^\s*DECIDE\s+${IDENT}`)
const RE_MEANS = new RegExp(String.raw`^${IDENT}.*\b(MEANS|IS|IF)\s*$|^${IDENT}.*\bMEANS\b`)
const unquote = (s) => s.replace(/^`|`$/g, '')

function indexL4(file, law, enc) {
  const text = readFileSync(file, 'utf8')
  const lines = text.split(/\r?\n/)
  const path = repoPath(file)
  const test = isTestFile(file)

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i]

    // ── provisions: § / §§ headings and the comment text under them
    const sec = !test && line.match(/^\s*(§+)\s*(.*)$/)
    if (sec) {
      const heading = unquote(sec[2].trim())
      const buf = []
      let j = i + 1
      for (; j < lines.length; j++) {
        const l = lines[j]
        if (/^\s*§/.test(l)) break
        const c = l.match(/^\s*--\s?(.*)$/)
        if (c) buf.push(c[1].replace(/^src:\d+\s*\|\s*/, ''))
        else if (l.trim()) break // the comment block ends at the first line of code
        if (buf.join(' ').length > PROVISION_MAX) break
      }
      let end = j - 1
      while (end > i && !lines[end].trim()) end--
      if (heading) {
        provisions.push({
          law_id: law.id,
          encoding_id: enc.id,
          file: path,
          line: i + 1,
          end_line: Math.max(i + 1, end + 1),
          level: sec[1].length,
          heading,
          text: clip(buf.join(' ').replace(/\s+/g, ' ').trim(), PROVISION_MAX) || null,
        })
      }
    }

    // ── decisions: @export annotations
    const ex = line.match(/^\s*@export\b\s*(.*)$/)
    if (!ex) continue

    let question = ex[1].trim()
    let isDefault = 0
    if (/^default\b/i.test(question)) {
      isDefault = 1
      question = question.replace(/^default\b\s*/i, '')
    }

    // annotations + comment block directly above
    let start = i
    const refs = []
    const ctx = []
    for (let k = i - 1; k >= 0 && k > i - 60; k--) {
      const l = lines[k]
      const ref = l.match(/^\s*@ref\s+(.*)$/)
      const desc = l.match(/^\s*@desc\s+(.*)$/)
      const c = l.match(/^\s*--\s?(.*)$/)
      if (ref) refs.unshift(ref[1].trim())
      else if (desc && !question) question = desc[1].trim()
      else if (c) ctx.unshift(c[1])
      else if (!desc) break
      start = k
    }

    // annotations, GIVEN, GIVETH, then the definition line
    const params = []
    let returns = null
    let name = null
    let defLine = null
    let inGiven = false
    for (let k = i + 1; k < lines.length && k < i + 400; k++) {
      const l = lines[k]
      if (!l.trim() || /^\s*--/.test(l)) continue
      const ref = l.match(/^\s*@ref\s+(.*)$/)
      if (ref) {
        refs.push(ref[1].trim())
        continue
      }
      const desc = l.match(/^\s*@desc\s+(.*)$/)
      if (desc) {
        if (!question) question = desc[1].trim()
        continue
      }
      if (/^\s*GIVEN\b/.test(l)) inGiven = true
      const giveth = l.match(/^\s*GIVETH\s+(?:AN?\s+)?(.*?)\s*$/)
      if (giveth) {
        returns = giveth[1]
        inGiven = false
        continue
      }
      const decide = l.match(RE_DECIDE)
      if (decide) {
        name = unquote(decide[1])
        defLine = k
        break
      }
      if (inGiven && /\bIS\b/.test(l) && !/\bMEANS\b/.test(l)) {
        const p = l.match(RE_PARAM)
        if (p) params.push([unquote(p[1]), p[2].trim(), p[3]?.trim() ?? null])
        continue
      }
      const m = !/^\s/.test(l) && l.match(RE_MEANS)
      if (m) {
        name = unquote(m[1] ?? m[3])
        defLine = k
        break
      }
      // after GIVETH, the first top-level identifier starts the definition
      // even when its MEANS is on the next line
      const head = returns != null && !/^\s/.test(l) && l.match(new RegExp(`^${IDENT}`))
      if (head && !/^(GIVEN|GIVETH|DECIDE|DECLARE|ASSUME|IMPORT)$/.test(head[1])) {
        name = unquote(head[1])
        defLine = k
        break
      }
    }
    if (!name) continue

    // body: until the next line at column 0 (a new top-level item)
    let end = defLine
    for (let k = defLine + 1; k < lines.length && k < defLine + DECISION_MAX_LINES; k++) {
      const l = lines[k]
      if (l.trim() && !/^\s/.test(l)) break
      if (l.trim()) end = k
    }

    decisions.push({
      law_id: law.id,
      encoding_id: enc.id,
      file: path,
      line: i + 1,
      start_line: start + 1,
      end_line: end + 1,
      name,
      question: question || name,
      ref: refs.join('; ') || null,
      params: JSON.stringify(params),
      param_text: params.map((p) => `${p[0]} ${p[2] ?? ''}`).join(' | '),
      returns,
      is_default: isDefault,
      is_test: test ? 1 : 0,
      context: clip(ctx.join(' ').replace(/\s+/g, ' ').trim(), CONTEXT_MAX) || null,
    })
    enc.decisions++
    law.decisions++
  }
}

for (const f of files) {
  const subjectDir = subjectOf(f)
  if (!subjectDir) continue
  const law = lawFor(subjectDir)
  law.files.push(relative(subjectDir, f).split(sep).join('/'))
  if (!f.endsWith('.l4')) continue
  const enc = encodingFor(encodingDirOf(f, subjectDir), law, subjectDir)
  indexL4(f, law, enc)
}
// encodings that hold an encoding.json but (oddly) no .l4 still count
for (const f of files) {
  if (basename(f) !== 'encoding.json') continue
  const subjectDir = subjectOf(f)
  if (!subjectDir) continue
  const law = lawFor(subjectDir)
  encodingFor(encodingDirOf(f, subjectDir), law, subjectDir)
}

// ── emit SQL ─────────────────────────────────────────────────────────

const q = (v) =>
  v == null ? 'NULL' : typeof v === 'number' ? String(v) : `'${String(v).replace(/'/g, "''").replace(/\u0000/g, '')}'`

const sql = []
const emitRows = (table, cols, rows) => {
  // D1 caps a statement at 100 KB; stay well under it.
  let batch = []
  let size = 0
  const flush = () => {
    if (!batch.length) return
    sql.push(`INSERT INTO ${table} (${cols.join(', ')}) VALUES\n${batch.join(',\n')};`)
    batch = []
    size = 0
  }
  for (const r of rows) {
    const tuple = `(${cols.map((c) => q(r[c])).join(', ')})`
    if (size + tuple.length > 60_000) flush()
    batch.push(tuple)
    size += tuple.length
  }
  flush()
}

let commit = null
let committed = null
try {
  commit = execFileSync('git', ['-C', root, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim()
  committed = execFileSync('git', ['-C', root, 'log', '-1', '--format=%cI'], { encoding: 'utf8' }).trim()
} catch {
  console.warn('warning: not a git checkout; file reads will use the branch, not a pinned commit')
}

sql.push(`-- generated by build-index.mjs from legalese/commons ${commit ?? '(unknown commit)'}`)
sql.push(`
DROP TABLE IF EXISTS laws_fts;
DROP TABLE IF EXISTS decisions_fts;
DROP TABLE IF EXISTS provisions_fts;
DROP TABLE IF EXISTS provisions;
DROP TABLE IF EXISTS decisions;
DROP TABLE IF EXISTS encodings;
DROP TABLE IF EXISTS laws;
DROP TABLE IF EXISTS meta;

CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);

CREATE TABLE laws (
  rid INTEGER PRIMARY KEY,
  id TEXT NOT NULL UNIQUE,
  jurisdiction TEXT NOT NULL,
  jurisdiction_label TEXT,
  name TEXT NOT NULL,
  citation TEXT,
  source_url TEXT,
  status TEXT,
  encodings INTEGER NOT NULL,
  decisions INTEGER NOT NULL,
  files TEXT NOT NULL,
  summary TEXT,
  notes TEXT
);
CREATE INDEX laws_jurisdiction ON laws (jurisdiction);

CREATE TABLE encodings (
  rid INTEGER PRIMARY KEY,
  id TEXT NOT NULL UNIQUE,
  law_id TEXT NOT NULL,
  row TEXT NOT NULL,
  dir TEXT NOT NULL,
  seat TEXT, scope TEXT, status TEXT, version TEXT, edition TEXT, method TEXT,
  modules TEXT, cases TEXT, notes TEXT,
  decisions INTEGER NOT NULL
);
CREATE INDEX encodings_law ON encodings (law_id);

CREATE TABLE decisions (
  id INTEGER PRIMARY KEY,
  law_id TEXT NOT NULL,
  encoding_id TEXT NOT NULL,
  file TEXT NOT NULL,
  line INTEGER NOT NULL,
  start_line INTEGER NOT NULL,
  end_line INTEGER NOT NULL,
  name TEXT NOT NULL,
  question TEXT NOT NULL,
  ref TEXT,
  params TEXT NOT NULL,
  param_text TEXT,
  returns TEXT,
  is_default INTEGER NOT NULL,
  is_test INTEGER NOT NULL,
  context TEXT
);
CREATE INDEX decisions_law ON decisions (law_id);
CREATE INDEX decisions_encoding ON decisions (encoding_id);

CREATE TABLE provisions (
  id INTEGER PRIMARY KEY,
  law_id TEXT NOT NULL,
  encoding_id TEXT NOT NULL,
  file TEXT NOT NULL,
  line INTEGER NOT NULL,
  end_line INTEGER NOT NULL,
  level INTEGER NOT NULL,
  heading TEXT NOT NULL,
  text TEXT
);
CREATE INDEX provisions_law ON provisions (law_id);
`)

sql.push(
  `INSERT INTO meta (key, value) VALUES ('commit', ${q(commit)}), ('committed_at', ${q(committed)}), ('indexed_at', ${q(new Date().toISOString())});`
)

// Each law also carries its encodings' seats, scopes and notes, so one FTS
// row answers "is this law encoded, and does the encoding cover X?".
const encodingsByLaw = new Map()
for (const e of encodings.values()) {
  if (!encodingsByLaw.has(e.law_id)) encodingsByLaw.set(e.law_id, [])
  encodingsByLaw.get(e.law_id).push(e)
}
const lawRows = [...laws.values()].map((l) => {
  const encs = encodingsByLaw.get(l.id) ?? []
  return {
    ...l,
    files: JSON.stringify(l.files.sort()),
    summary: clip(encs.map((e) => [e.seat && `Seat: ${e.seat}.`, e.scope].filter(Boolean).join(' ')).filter(Boolean).join(' | '), 4000),
    notes: clip(encs.map((e) => e.notes).filter(Boolean).join('\n\n'), 8000),
  }
})
emitRows(
  'laws',
  ['id', 'jurisdiction', 'jurisdiction_label', 'name', 'citation', 'source_url', 'status', 'encodings', 'decisions', 'files', 'summary', 'notes'],
  lawRows
)
emitRows(
  'encodings',
  ['id', 'law_id', 'row', 'dir', 'seat', 'scope', 'status', 'version', 'edition', 'method', 'modules', 'cases', 'notes', 'decisions'],
  [...encodings.values()]
)
emitRows(
  'decisions',
  ['law_id', 'encoding_id', 'file', 'line', 'start_line', 'end_line', 'name', 'question', 'ref', 'params', 'param_text', 'returns', 'is_default', 'is_test', 'context'],
  decisions
)
emitRows('provisions', ['law_id', 'encoding_id', 'file', 'line', 'end_line', 'level', 'heading', 'text'], provisions)

// Full-text indexes. External-content tables keep the text once, in the base
// tables, and let snippet() highlight matches.
sql.push(`
CREATE VIRTUAL TABLE laws_fts USING fts5(
  name, citation, summary, notes, content='laws', content_rowid='rid', tokenize='porter unicode61 remove_diacritics 2'
);
INSERT INTO laws_fts (laws_fts) VALUES ('rebuild');

CREATE VIRTUAL TABLE decisions_fts USING fts5(
  question, name, ref, param_text, context, content='decisions', content_rowid='id', tokenize='porter unicode61 remove_diacritics 2'
);
INSERT INTO decisions_fts (decisions_fts) VALUES ('rebuild');

CREATE VIRTUAL TABLE provisions_fts USING fts5(
  heading, text, content='provisions', content_rowid='id', tokenize='porter unicode61 remove_diacritics 2'
);
INSERT INTO provisions_fts (provisions_fts) VALUES ('rebuild');
`)

writeFileSync(out, sql.join('\n') + '\n')
const mb = (statSync(out).size / 1e6).toFixed(1)
console.log(
  `commons ${commit?.slice(0, 12) ?? '?'}: ${laws.size} laws, ${encodings.size} encodings, ` +
    `${decisions.length} decisions, ${provisions.length} provisions` +
    ` → ${out} (${mb} MB)`
)
