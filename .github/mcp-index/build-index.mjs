#!/usr/bin/env node
/**
 * build-index.mjs — turn a checkout of legalese/commons into SQL for the D1
 * search index behind the L4 Commons MCP server (https://commons.utility.workers.dev/mcp).
 *
 * The same file lives at .github/mcp-index/build-index.mjs in legalese/commons
 * (run by .github/workflows/mcp-index.yml) and at scripts/build-index.mjs in the
 * worker's project. Keep the two identical. Nothing under subjects/ depends on it.
 *
 *   node build-index.mjs <commons> <out.sql> --full
 *       The whole schema and every row, for an empty database. Costs about
 *       170,000 D1 rows written, more than the free plan's 100,000 a day.
 *
 *   node build-index.mjs <commons> <out.sql> --sync <state.json> [--budget 50000]
 *       Only what changed. state.json is the output of
 *         wrangler d1 execute <db> --remote --json --command \
 *           "SELECT id, hash, commit_sha, writes FROM law_state; SELECT key, value FROM meta"
 *       Each law carries a hash of its rows; a law whose hash changed is deleted
 *       and re-inserted, with its full-text entries, and nothing else is touched.
 *       Writes are counted per UTC day in meta (`writes:YYYY-MM-DD`). Changes that
 *       would take today's count past --budget wait for a later run; the laws
 *       they belong to keep their old rows and the commit those rows came from,
 *       so line numbers stay right in the meantime.
 *
 *   node build-index.mjs <commons> <out.sql> --adopt
 *       Declare that the database already holds exactly this checkout: write
 *       law_state from it and nothing else. For a database loaded before
 *       law_state existed, or to recover one whose law_state was lost.
 *
 * What gets indexed:
 *   laws        one row per subject (a directory holding subject.json), with its
 *               encodings' seats, scopes and NOTES.md folded in for search
 *   encodings   one row per encoding of a subject (encoding.json, seat, scope, NOTES.md)
 *   decisions   one row per `@export`ed L4 function: the question it answers,
 *               its parameters (with their @desc), what it returns, where it lives
 *   provisions  one row per `§` / `§§` heading in a non-test .l4 file, with the
 *               comment text under it (usually the quoted statutory text)
 *   law_state   per law: the hash of its rows, the commit they were built from,
 *               and what writing them costs
 * Laws, decisions and provisions each have an FTS5 table (porter stemming).
 * File contents are not stored: the worker reads them from GitHub at the
 * law's commit.
 *
 * When the step runs inside GitHub Actions it also writes `load=true|false`
 * to $GITHUB_OUTPUT and a summary to $GITHUB_STEP_SUMMARY.
 *
 * No dependencies; Node >= 18.
 */

import { readFileSync, readdirSync, statSync, writeFileSync, existsSync, appendFileSync } from 'node:fs'
import { join, relative, dirname, basename, sep } from 'node:path'
import { execFileSync } from 'node:child_process'
import { createHash } from 'node:crypto'

// ── arguments ────────────────────────────────────────────────────────

const argv = process.argv.slice(2)
const flag = (name) => {
  const i = argv.indexOf(name)
  if (i < 0) return undefined
  const v = argv[i + 1]
  argv.splice(i, v === undefined || v.startsWith('--') ? 1 : 2)
  return v === undefined || v.startsWith('--') ? true : v
}
const MODE_FULL = flag('--full')
const MODE_ADOPT = flag('--adopt')
const SYNC_STATE = flag('--sync')
const BUDGET = Number(flag('--budget') ?? 50_000)
const TODAY = String(flag('--today') ?? new Date().toISOString().slice(0, 10)) // for tests
const [root, out] = argv

const modes = [MODE_FULL, MODE_ADOPT, SYNC_STATE].filter(Boolean).length
if (!root || !out || !existsSync(join(root, 'subjects')) || modes !== 1 || !Number.isFinite(BUDGET)) {
  console.error(
    'usage: build-index.mjs <commons> <out.sql> --full\n' +
      '       build-index.mjs <commons> <out.sql> --sync <state.json> [--budget N]\n' +
      '       build-index.mjs <commons> <out.sql> --adopt'
  )
  process.exit(2)
}

const SUBJECTS = join(root, 'subjects')
const NOTES_MAX = 6000 // chars of NOTES.md kept per encoding
const CONTEXT_MAX = 1200 // chars of comment kept above an @export
const PROVISION_MAX = 1500 // chars of comment text kept under a § heading
const DECISION_MAX_LINES = 250

// D1 counts a row written for every table row and every index entry a
// statement touches, and one per row inserted into or deleted from an FTS5
// table. A law row: laws (row, id, jurisdiction) + law_state + laws_fts.
const COST = { law: 5, encoding: 3, decision: 3, provision: 3 }

// ── walk ─────────────────────────────────────────────────────────────

const repoPath = (abs) => relative(root, abs).split(sep).join('/')

/** All files under `dir` in a stable order, skipping dot-directories. */
function walk(dir, acc = []) {
  for (const name of readdirSync(dir).sort()) {
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
  .sort((a, b) => a.length - b.length || (a < b ? -1 : 1))
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
  encodingFor(encodingDirOf(f, subjectDir), lawFor(subjectDir), subjectDir)
}

// ── per-law rows, hash and cost ─────────────────────────────────────

const COLS = {
  laws: ['id', 'jurisdiction', 'jurisdiction_label', 'name', 'citation', 'source_url', 'status', 'encodings', 'decisions', 'files', 'summary', 'notes'],
  encodings: ['id', 'law_id', 'row', 'dir', 'seat', 'scope', 'status', 'version', 'edition', 'method', 'modules', 'cases', 'notes', 'decisions'],
  decisions: ['law_id', 'encoding_id', 'file', 'line', 'start_line', 'end_line', 'name', 'question', 'ref', 'params', 'param_text', 'returns', 'is_default', 'is_test', 'context'],
  provisions: ['law_id', 'encoding_id', 'file', 'line', 'end_line', 'level', 'heading', 'text'],
}

const byLaw = new Map()
for (const l of laws.values()) byLaw.set(l.id, { law: l, encodings: [], decisions: [], provisions: [] })
for (const e of encodings.values()) byLaw.get(e.law_id).encodings.push(e)
for (const d of decisions) byLaw.get(d.law_id).decisions.push(d)
for (const p of provisions) byLaw.get(p.law_id).provisions.push(p)

const byPos = (a, b) => (a.file < b.file ? -1 : a.file > b.file ? 1 : a.line - b.line)
for (const g of byLaw.values()) {
  g.encodings.sort((a, b) => (a.id < b.id ? -1 : 1))
  g.decisions.sort(byPos)
  g.provisions.sort(byPos)
  // Each law also carries its encodings' seats, scopes and notes, so one FTS
  // row answers "is this law encoded, and does the encoding cover X?".
  const l = g.law
  g.law = {
    ...l,
    files: JSON.stringify([...l.files].sort()),
    summary: clip(g.encodings.map((e) => [e.seat && `Seat: ${e.seat}.`, e.scope].filter(Boolean).join(' ')).filter(Boolean).join(' | '), 4000),
    notes: clip(g.encodings.map((e) => e.notes).filter(Boolean).join('\n\n'), 8000),
  }
  const pick = (cols, r) => cols.map((c) => r[c] ?? null)
  g.hash = createHash('sha256')
    .update(
      JSON.stringify([
        pick(COLS.laws, g.law),
        g.encodings.map((r) => pick(COLS.encodings, r)),
        g.decisions.map((r) => pick(COLS.decisions, r)),
        g.provisions.map((r) => pick(COLS.provisions, r)),
      ])
    )
    .digest('hex')
    .slice(0, 32)
  g.writes = COST.law + COST.encoding * g.encodings.length + COST.decision * g.decisions.length + COST.provision * g.provisions.length
}

let commit = null
let committed = null
try {
  commit = execFileSync('git', ['-C', root, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim()
  committed = execFileSync('git', ['-C', root, 'log', '-1', '--format=%cI'], { encoding: 'utf8' }).trim()
} catch {
  if (!MODE_FULL) {
    console.error('error: <commons> must be a git checkout, so each law can record the commit it was built from')
    process.exit(2)
  }
  console.warn('warning: not a git checkout; file reads will use the branch, not a pinned commit')
}

// ── SQL ──────────────────────────────────────────────────────────────

const q = (v) =>
  v == null ? 'NULL' : typeof v === 'number' ? String(v) : `'${String(v).replace(/'/g, "''").replace(/\u0000/g, '')}'`

const sql = []
/** Multi-row INSERTs, each well under D1's 100 KB statement limit. */
function emitRows(table, cols, rows) {
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
/** One statement per chunk of law ids: `make(list)` gets "('a', 'b', …)". */
function emitForLaws(ids, make) {
  for (let i = 0; i < ids.length; i += 200) sql.push(make(`(${ids.slice(i, i + 200).map(q).join(', ')})`))
}

const FTS = {
  laws: { cols: 'name, citation, summary, notes', key: 'rid', where: 'id' },
  decisions: { cols: 'question, name, ref, param_text, context', key: 'id', where: 'law_id' },
  provisions: { cols: 'heading, text', key: 'id', where: 'law_id' },
}

const LAW_STATE_DDL = `CREATE TABLE IF NOT EXISTS law_state (
  id TEXT PRIMARY KEY,
  hash TEXT NOT NULL,
  commit_sha TEXT,
  writes INTEGER NOT NULL
) WITHOUT ROWID;`

function emitLawRows(groups) {
  emitRows('laws', COLS.laws, groups.map((g) => g.law))
  emitRows('encodings', COLS.encodings, groups.flatMap((g) => g.encodings))
  emitRows('decisions', COLS.decisions, groups.flatMap((g) => g.decisions))
  emitRows('provisions', COLS.provisions, groups.flatMap((g) => g.provisions))
  emitRows('law_state', ['id', 'hash', 'commit_sha', 'writes'], groups.map((g) => ({ id: g.law.id, hash: g.hash, commit_sha: commit, writes: g.writes })))
}

function emitMeta(writes, pending) {
  const rows = { commit, committed_at: committed, indexed_at: new Date().toISOString(), pending: String(pending) }
  sql.push(
    `INSERT INTO meta (key, value) VALUES ${Object.entries(rows)
      .map(([k, v]) => `(${q(k)}, ${q(v)})`)
      .join(', ')}\n  ON CONFLICT (key) DO UPDATE SET value = excluded.value;`
  )
  sql.push(
    `INSERT INTO meta (key, value) VALUES (${q(`writes:${TODAY}`)}, ${q(String(writes))})\n` +
      `  ON CONFLICT (key) DO UPDATE SET value = CAST(CAST(value AS INTEGER) + CAST(excluded.value AS INTEGER) AS TEXT);`
  )
  const weekAgo = new Date(Date.parse(TODAY) - 7 * 864e5).toISOString().slice(0, 10)
  sql.push(`DELETE FROM meta WHERE key LIKE 'writes:%' AND key < ${q(`writes:${weekAgo}`)};`)
}

const groups = [...byLaw.values()]
const fmt = (n) => n.toLocaleString('en-US')
let summary
let load = true

if (MODE_FULL) {
  sql.push(`-- full index of legalese/commons ${commit ?? '(unknown commit)'}`)
  sql.push(`
DROP TABLE IF EXISTS laws_fts;
DROP TABLE IF EXISTS decisions_fts;
DROP TABLE IF EXISTS provisions_fts;
DROP TABLE IF EXISTS encodings_fts;
DROP TABLE IF EXISTS provisions;
DROP TABLE IF EXISTS decisions;
DROP TABLE IF EXISTS encodings;
DROP TABLE IF EXISTS laws;
DROP TABLE IF EXISTS law_state;
DROP TABLE IF EXISTS meta;

CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);
${LAW_STATE_DDL}

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
  emitLawRows(groups)
  // External-content FTS tables: the text lives once, in the base tables.
  for (const [t, f] of Object.entries(FTS)) {
    sql.push(
      `CREATE VIRTUAL TABLE ${t}_fts USING fts5(${f.cols}, content='${t}', content_rowid='${f.key}', tokenize='porter unicode61 remove_diacritics 2');\n` +
        `INSERT INTO ${t}_fts (${t}_fts) VALUES ('rebuild');`
    )
  }
  // A bulk load fills the FTS tables with one 'rebuild' each, which D1 counts
  // as a handful of rows, so only table rows and index entries count here.
  const writes = groups.reduce(
    (n, g) => n + 4 + 3 * g.encodings.length + 2 * g.decisions.length + 2 * g.provisions.length,
    100
  )
  emitMeta(writes, 0)
  summary = `full index: ${fmt(groups.length)} laws, about ${fmt(writes)} rows written`
} else if (MODE_ADOPT) {
  sql.push(`-- adopt legalese/commons ${commit}: the database already holds these rows`)
  sql.push(LAW_STATE_DDL)
  sql.push(`DROP INDEX IF EXISTS decisions_encoding;`) // no query uses it; it cost a write per decision
  sql.push(`DELETE FROM law_state;`)
  emitRows('law_state', ['id', 'hash', 'commit_sha', 'writes'], groups.map((g) => ({ id: g.law.id, hash: g.hash, commit_sha: commit, writes: g.writes })))
  const writes = groups.length + 20
  emitMeta(writes, 0)
  summary = `adopted ${fmt(groups.length)} laws at ${commit.slice(0, 12)}: about ${fmt(writes)} rows written`
} else {
  // ── sync: only what changed, within today's budget
  let state
  try {
    state = JSON.parse(readFileSync(SYNC_STATE, 'utf8'))
  } catch (err) {
    console.error(`error: cannot read ${SYNC_STATE}: ${err.message}`)
    process.exit(2)
  }
  const sets = Array.isArray(state) ? state.map((s) => s.results ?? s) : [state]
  const old = new Map((sets[0] ?? []).map((r) => [r.id, r]))
  const meta = Object.fromEntries((sets[1] ?? []).map((r) => [r.key, r.value]))
  if (!old.size && !meta.commit) {
    console.error('error: the database has no law_state and no meta: load it with --full first')
    process.exit(2)
  }
  if (!old.size) {
    console.error('error: the database has no law_state. If it holds an index built before law_state existed, run --adopt once with the commit it was built from.')
    process.exit(2)
  }

  const now = new Map(groups.map((g) => [g.law.id, g]))
  const changes = []
  for (const [id, o] of old) if (!now.has(id)) changes.push({ id, kind: 'removed', cost: o.writes })
  for (const [id, g] of now) {
    const o = old.get(id)
    if (!o) changes.push({ id, kind: 'added', cost: g.writes, g })
    else if (o.hash !== g.hash) changes.push({ id, kind: 'changed', cost: o.writes + g.writes, g })
  }
  // Removals first, then cheapest first, so one huge law cannot hold up the rest.
  changes.sort((a, b) => (b.kind === 'removed') - (a.kind === 'removed') || a.cost - b.cost)

  const OVERHEAD = 40 // meta upserts, the writes counter, schema no-ops
  const used = Number(meta[`writes:${TODAY}`] ?? 0)
  let room = BUDGET - used - OVERHEAD
  const apply = []
  const deferred = []
  for (const c of changes) {
    if (c.cost <= room) {
      apply.push(c)
      room -= c.cost
    } else deferred.push(c)
  }

  const writes = apply.reduce((n, c) => n + c.cost, 0) + (apply.length ? OVERHEAD : 0)
  const lines = [
    `commons ${commit.slice(0, 12)}: ${fmt(changes.length)} of ${fmt(now.size)} laws differ from the index` +
      (changes.length ? ` (${['added', 'changed', 'removed'].map((k) => `${changes.filter((c) => c.kind === k).length} ${k}`).join(', ')})` : ''),
    `budget ${fmt(BUDGET)} rows written a day; ${fmt(used)} already used today (${TODAY} UTC)`,
    apply.length ? `applying ${fmt(apply.length)}: about ${fmt(writes)} rows written` : 'nothing to write',
  ]
  for (const c of apply.slice(0, 40)) lines.push(`  ${c.kind.padEnd(7)} ${c.id} (${fmt(c.cost)})`)
  if (apply.length > 40) lines.push(`  … and ${apply.length - 40} more`)
  if (deferred.length) {
    lines.push(`deferred to a later run (over today's budget): ${fmt(deferred.length)}, about ${fmt(deferred.reduce((n, c) => n + c.cost, 0))} rows`)
    for (const c of deferred.slice(0, 40)) lines.push(`  ${c.kind.padEnd(7)} ${c.id} (${fmt(c.cost)})`)
    const never = deferred.filter((c) => c.cost > BUDGET - OVERHEAD)
    if (never.length) {
      lines.push(
        `::warning::${never.map((c) => c.id).join(', ')} need${never.length === 1 ? 's' : ''} more than the whole daily budget; ` +
          'run the workflow by hand with a larger budget once, on a day with room.'
      )
    }
  }
  summary = lines.join('\n')

  if (!apply.length) {
    load = false
  } else {
    sql.push(`-- sync to legalese/commons ${commit}`)
    sql.push(LAW_STATE_DDL)
    const gone = apply.filter((c) => c.kind !== 'added').map((c) => c.id)
    const fresh = apply.filter((c) => c.kind !== 'removed')
    // FTS entries go first, while the rows they index still exist.
    for (const [t, f] of Object.entries(FTS)) {
      emitForLaws(gone, (ids) => `INSERT INTO ${t}_fts (${t}_fts, rowid, ${f.cols}) SELECT 'delete', ${f.key}, ${f.cols} FROM ${t} WHERE ${f.where} IN ${ids};`)
    }
    for (const t of ['decisions', 'provisions', 'encodings']) emitForLaws(gone, (ids) => `DELETE FROM ${t} WHERE law_id IN ${ids};`)
    emitForLaws(gone, (ids) => `DELETE FROM laws WHERE id IN ${ids};`)
    emitForLaws(gone, (ids) => `DELETE FROM law_state WHERE id IN ${ids};`)
    emitLawRows(fresh.map((c) => c.g))
    const freshIds = fresh.map((c) => c.id)
    for (const [t, f] of Object.entries(FTS)) {
      emitForLaws(freshIds, (ids) => `INSERT INTO ${t}_fts (rowid, ${f.cols}) SELECT ${f.key}, ${f.cols} FROM ${t} WHERE ${f.where} IN ${ids};`)
    }
    emitMeta(writes, deferred.length)
  }
}

if (load) writeFileSync(out, sql.join('\n') + '\n')
else writeFileSync(out, '')
console.log(summary + (load ? `\n→ ${out} (${(statSync(out).size / 1e6).toFixed(1)} MB)` : ''))

if (process.env.GITHUB_OUTPUT) appendFileSync(process.env.GITHUB_OUTPUT, `load=${load}\n`)
if (process.env.GITHUB_STEP_SUMMARY) {
  appendFileSync(process.env.GITHUB_STEP_SUMMARY, '### MCP index\n\n```\n' + summary.replace(/^::warning::/gm, 'warning: ') + '\n```\n')
}
