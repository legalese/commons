#!/usr/bin/env bash
# Written for row il-43 (2026-11-10), adapted for rows il-48 and il-50. hebcheck.py takes one deposit; this row quotes four Hebrew Wikisource EXCERPTS (the Companies Law s 367, the Companies (Fees) Regulations,
# the Companies (Motion for Compromise or Arrangement) Regulations and the Companies Ordinance), so the four are joined in a temporary file and every run of Hebrew in the given files must occur in the joined text.
# Only the excerpts and the text layer of the KT 7639 page extract are joined, never a whole page of a consolidation: a Hebrew phrase the excerpts do not hold fails here, which keeps the row's Hebrew inside what the excerpts deposit.
# A `ext:[tag] N |` or `ext:[SH ... p.N...] |` or `ext:[KT ... p.N...] |` line is skipped by hebcheck.py.
# Usage (from the row folder): tools/hebcheck-all.sh *.l4 NOTES.md
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SB="$HERE/../../../registers/source-bundle"
T="$(mktemp "${TMPDIR:-/tmp}/hebcheck-all.XXXXXX")" || exit 2
trap 'rm -f "$T"' EXIT
cat "$SB/companies-law-5759-1999-s367.excerpt.he.wiki.txt" "$SB/companies-fees-regulations-5761-2001.excerpt.he.wiki.txt" \
    "$SB/companies-compromise-regulations-5762-2002.excerpt.he.wiki.txt" "$SB/companies-ordinance-new-version-5743-1983.excerpt.he.wiki.txt" > "$T"
# The Kovetz HaTakanot 7639 page extract has a text layer, and it is the source of the Hebrew of the signature lines of that issue; its words are in garbled order, which is enough for a check of words.
pdftotext -layout "$SB/official/kt7639-5776-pp946-949-page-extract.pdf" - >> "$T"
python3 -I "$HERE/hebcheck.py" "$T" "$@"
