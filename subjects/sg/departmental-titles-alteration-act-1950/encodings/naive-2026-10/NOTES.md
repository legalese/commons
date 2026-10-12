# Departmental Titles (Alteration) Act 1950 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (footer: "version in
force from 1/10/2026"). The cover says it incorporates amendments up to 1 December
2021; the Schedule is annotated with later notifications, the latest S 704/2026
with effect from 1 October 2026. The Schedule is column-shifted in the `.txt`
deposit on its pages 7 and 8, so those entries were matched by order of appearance
(see finding 6).

**Checks:** one case file, 48 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0262** in `subjects/sg/requirements.jsonl`: Tier 4 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet. What it decides is how to read an office named in an old law,
licence, deed or form. The Act has three sections and a Schedule of 116 entries.
This row encodes s 2, s 3 and 27 of the entries (44 titles), picked where the
Schedule chains, splits or nearly matches itself, or where a member of the public
deals with the office (prisons, customs, the registries, the Shariah Court,
ministries). The rest of the Schedule is the same one-step substitution repeated.

## What the Act turns out to say

### 1. Old titles chain, and s 2 does not say whether to follow the chain

Many new titles are themselves old titles in a later row. Sub-warder becomes Warder
(item 7), Warder becomes Principal Officer (item 5), and Principal Officer becomes
Principal Rehabilitation Officer (item 19). Revenue Officer becomes Customs Officer
(25), which becomes Assistant Superintendent of Customs and Excise (22). s 2 says only
that the old title "is to be substituted" by the one "opposite it". It does not say
whether you substitute once or keep going. The encoding has both readings: one pass
(Sub-warder reads as Warder) and repeated substitution (Sub-warder reads as Principal
Rehabilitation Officer, three steps). Which one is right is an interpretive fork the
text leaves open. Asserted.

### 2. One old title has two new titles

Items 27 and 28 both list "Registrar of Births, Deaths and Marriages", one opposite
"Registrar of Births and Deaths" and the other opposite "Registrar of Marriages".
s 2 speaks of "the" title opposite, in the singular, and gives no rule for choosing.
The encoding records both as substitutes and leaves the single-pass function
unchanged for that title. Asserted.

### 3. A near-miss spelling breaks a chain

Item 87 turns the Head of Support and Services Division into "Assistant Director CID
(Support and Services)". A later entry (by order, item 93) renames "Assistant Director
CID (Support **&** Services)". Matched literally, the first result is not the second
old title, so the chain stops at item 87. Whether "and" and "&" are the same title is
not answered by the text. Asserted (literal reading).

### 4. Chief Kathi becomes Registrar of Muslim Marriages, which is not item 44

Item 45 turns the Chief Kathi into "Registrar of Muslim Marriages". Item 44 renames a
different, combined office, "Registrar of Muslim Marriages and President, Shariah
Court", to "President, Shariah Court". So the Chief Kathi does not go on to become
President of the Shariah Court. Asserted.

### 5. It reaches "any other document", not only laws

s 2 applies "in any written law or in any other document". Read literally, that takes
in a private contract or letter that names an old office. Whether a court would read
it more narrowly is not in the text; the encoding takes the literal reading. s 3
lets the Minister responsible for the department the title relates to add to or amend
the Schedule by Gazette notification, at any time. Asserted.

### 6. The deposit's last two Schedule pages are out of line

On page 7 the item numbers 89 to 101 are printed in a column above the entries, and
on page 8 the new titles sit up to two lines above their old titles. There are 13 old
and 13 new titles on page 7, and 12 and 12 (with 107A) on page 8, so they were paired
by order. On that pairing, Parliamentary Counsel becomes Chief Legislative Counsel
(104), and the Deputy Chief Executive of Judiciary Administration becomes Deputy Chief
Executive of the Supreme Court (106), which then becomes Deputy Chief Executive,
Office of the Chief Justice (107A). The item numbers for page-7 entries are an
inference. Asserted on that pairing.

## What would need doing before this is worth anything

- The other 89 Schedule entries are not encoded.
- The pairing on pages 7 and 8 should be checked against the SSO web text or the
  amending notifications (S 704/2026 and the earlier S numbers), which were not read.
- Whether substitution is single or repeated, and whether "&" matches "and", needs an
  answer from outside the text before either reading is relied on.
- No case law on s 2 or "any other document" was searched.
