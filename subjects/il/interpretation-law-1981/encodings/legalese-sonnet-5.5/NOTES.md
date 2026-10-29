# NOTES: Israel's Interpretation Law 5741-1981 and Interpretation Ordinance [New Version], in L4

Row `legalese-sonnet-5.5`: Claude Sonnet 5.5 agents working alone from written briefs, with no ontology agent, fleet, integrator or independent test author.
Pass 1 (2026-10-13) encoded the time rules.
Pass 2 (2026-10-29) is the completion pass: it brings every unit of both texts to one disposition, and added modules, tests and this audit.
Version `0.2.0`.
Status: **draft**.
No domain expert has read any of it against the statute.

**Both source texts are unofficial.**
They are Hebrew Wikisource consolidations (section 0).
Nothing here is "verified against the official text"; the one comparison with an official PDF is in section 7.

## Re-disposition audit

Written before any pass-2 L4 and kept current as the work landed.
Pass 1 worked to a narrower standard of what to skip; this section re-derives every disposition from the text.
The tools are `inventory.py` (counts the units of the two wikitext files and gives each an id), `coverage-data.py` (the disposition of every unit) and `gen-coverage.py` (joins them, checks them, and writes the table in section 2).

### Counts

`python3 -I inventory.py` reads `../../source/law.wiki` and `ordinance.wiki`, and counts a unit for each of: the title; the publication history; a chapter heading; a section (its heading and lead-in text); a lettered or numbered subsection; a defined-term entry of the interpretation section; a numbered limb of such an entry; an editorial note (`{{ח:הערה}}`) on a line of its own; the editorial note at the head of the Ordinance; the signature block.
The text's own table of contents repeats the chapter headings and is not counted.

| | Law | Ordinance | both |
| --- | --- | --- | --- |
| title | 1 | 1 | 2 |
| publication history | 1 | 2 | 3 |
| chapter headings | 5 | 7 | 12 |
| sections | 33 | 43 | 76 |
| subsections | 10 | 5 | 15 |
| defined-term entries | 26 | 66 | 92 |
| limbs of a defined-term entry | 4 | 6 | 10 |
| editorial notes (the head note, the note before the entries of s 1, and the notes under them) | 2 | 12 | 14 |
| signature blocks | 1 | 1 | 2 |
| **units** | **83** | **143** | **226** |

Pass 1's coverage table had **76 rows**, one per section (33 of the Law, 43 of the Ordinance).
Its rows for s 3 of the Law and s 1 of the Ordinance named the defined terms in prose, and its carried-text module quoted them, but no defined term, subsection or limb had a row of its own.
The coverage table in section 2 now has **226 rows**, one per unit, and `gen-coverage.py --check` refuses to pass unless each unit has exactly one disposition, each `encoded` or `fork` row names a rule that a module defines and that at least one assertion calls, and every fork it cites is a heading in section 3.

Final dispositions (from `gen-coverage.py`): **encoded 123, fork 31, inert 15, repealed or blank in this text 57**.
By side: Law 83 units (encoded 49, fork 19, inert 11, repealed or blank 4); Ordinance 143 units (encoded 74, fork 12, inert 4, repealed or blank 53).
There is no `out-of-scope` and no `deferred` row.

### Units that had no row in pass 1's table

All 150 units that are not a section: in the Law, the title (`Ltitle`), the history (`Lhist`), five chapter headings (`Lch1` to `Lch5`), the 26 entries of s 3 (`L3d01` to `L3d26`) and their four limbs (`L3d02.1`, `.2`, `.3a`, `.3b`), the two notes in s 3 (`L3n1`, `L3n2`), ten subsections (`L10a` to `c`, `L13a`, `b`, `L17a`, `b`, `L22.1` to `.3`) and the signature block (`Lsig`); in the Ordinance, the title, two histories, the head note (`Ohead`), seven chapter headings (`Och1` to `Och7`), the 66 entries of s 1 (`O1d01` to `O1d66`) and their six limbs (`O1d10.1` to `.4`, `O1d48.1`, `.2`), the note before the entries (`O1n1`) and the ten notes under them (`O1n2` to `O1n11`), the five subsections of s 16 (`O16.1` to `.5`) and the signature (`Osig`).
Pass 1 had no row for the `(1)`, `(3)` and `(5)` of Ordinance s 16 either, only the sentence that they read `(בוטלה)`.

### Verdict on every pass-1 row that was not `encoded`

Pass 1 used two dispositions the standard no longer allows (`out-of-scope`), and one reason for `inert` that is not among the three (a canon, an open standard, "no input would change the answer").

**Law, 16 rows `inert`: all moved to `encoded`.**
ss 2, 4, 5, 6, 7, 9 (canons of construction: each is now a function over a small typed representation of what it operates on, with a test on each side of each limb; module `il-interpretation-reading.l4`), ss 11 to 19 (the scope of a grant of power; s 11 takes "the proper speed" as a plain input; module `il-interpretation-powers.l4`), and s 25 (references: the version in force when the reference is resorted to; `il-interpretation-reading.l4`).
Two of them then became `fork` rows, because the reading taken has a rejected alternative with a different answer: s 16 (F30) and s 25 (F31).
Pass 1's s 20 (already `fork`, F17) gained F30 as well.
Pass 1's reasons ("a canon of construction", "open-textured", "the answer is constant", "no input changes the answer") are listed in the brief as reasons that no longer stand.

**Law, 4 rows `out-of-scope` (ss 27 to 30): moved to `repealed or blank in this text`.**
The text under each number is only a note that the section's text was incorporated into another enactment (the Evidence Ordinance, the State Property Law, the Contracts (General Part) Law, the Law and Administration Ordinance).
The row says what the text shows; there is nothing to encode, and the other enactments are not among the sources.

**Law, 2 rows "part encoded, rest inert" (ss 3 and 22): the rest moved to `encoded`.**
s 3: the 23 entries pass 1 left as text became rules in `il-interpretation-definitions-law.l4` (`L3d01` to `L3d26` each have a row; the entries pass 1 had encoded keep their rules); 20 of them are `encoded` and three are `fork`: "coastal waters" `L3d12` (F29), "immovables" `L3d13` (F27) and "possession" `L3d24` (F28). The opening words are the dispatcher `s 3 — section 3 governs`.
s 22: limbs (1) and (3) became rules in `il-interpretation-repeal.l4`; limb (1) `L22.1` is a `fork` (F31, the boundary at the hour of the repeal) and limb (3) `L22.3` is `encoded`; limb (2) keeps pass 1's rule (`fork` F18).

**Law, 11 rows `encoded` in pass 1: 7 moved to `fork`, because the fork register already records two readings with different answers.**
s 1 (F14), s 20 (F17), s 21 (F12, F26), s 23 (F19), s 31 (F15), s 33 (F21), and, by their subsections, s 10(a) (F6, F7), (b) (F1, F24, F25) and (c) (F2, F3, F11).
s 8 stays `encoded`: F4 records that the Law settles the case.
s 24, s 26 and s 32 stay `encoded`.

**Ordinance, 38 rows `inert` (the sections that read `(בוטל)`): they keep their place and change name.**
They were `inert` for a reason that is right (text shown repealed: reason 3), and the standard has a disposition for exactly this, `repealed or blank in this text`.
There are 38 such sections (ss 2 to 15, 18, 20 to 41, 43), and Law s 31 is the text that repeals them (it saves only 16(2), 16(4), 17, 19, 42).
Each is checked by a test: `tests-ordinance-sweep.l4` asserts that `s 31 — the Ordinance's section N ... survives the Law` is false for each (49 assertions with s 16's subsections, s 1 and the three survivors).

**Ordinance, 2 rows "part encoded, rest inert" (ss 1 and 16): the rest moved to `encoded`, `repealed` or `fork`.**
s 1: the 66 entries each have a row.
61 are live entries; 5 read `(בוטלה)` and are `repealed or blank in this text` (`חטא`, `מימי חופין`, `עוון`, `פשע`, `שנת כספים`).
Of the 61, 56 are `encoded` and 5 are `fork` (F27 "immovables", F28 "possession", F32 "master", F34 "in writing" and "seaman").
Their module is `il-interpretation-definitions-ordinance.l4`.
The note before the entries (`O1n1`) and the head note (`Ohead`) are `fork` (F14, F33), because they say which enactments the definitions reach and the text does not reconcile that with Law s 31.
Of the ten notes under the entries, nine are `encoded` (what the word meant in an earlier enactment, or that the Law's definition governs earlier enactments) and `O1n5` (coastal waters, in miles) is a `fork` (F23, F29).
s 16: (4) keeps pass 1's rule; (1), (3), (5) read `(בוטלה)` (`repealed or blank`); (2) reads `(נמחקה)` while Law s 31 saves it (`fork` F15, pointing at the explicit "not covered" value `s 31 saves subsections (2) and (4) of section 16 ...`).

**Ordinance, 3 rows `encoded` (ss 17, 19, 42): s 17 and s 19 moved to `fork` (F13, F16); s 42 stays `encoded`.**

### Rows that stay `inert`, with the reason

All 15 are reason **1** (not operative); none is reason 2 or 3.
`Ltitle`, `Otitle` (titles); `Lhist`, `Ohist-old`, `Ohist-new` (publication histories); `Lch1` to `Lch5` (chapter headings); `L10`, `L13`, `L17` (the heading of a section whose rules are all in its subsections); `L3n1` (an editorial note that the Government published a notice dividing the State into districts; it creates no rule); `Osig` (the date of the new text and the signatory).
The seven chapter headings of the Ordinance read `(בוטל)` and are `repealed or blank`.
No row is left `inert` for being a canon, an open standard, a reference to an instrument outside the sources, or a rule with one answer.
The editorial notes in the Ordinance that restate Law ss 1 and 3, and the note under "coastal waters" in the Law, are not inert: the encoding relies on them (F14), so they are `encoded` or `fork`.
`Osig` stays inert although it carries a date (1 January 1954, "26 Tevet 5714"): it is the Minister's date of signing the new text, not the date the new text was published, and the provisos of Ordinance s 1 turn on dates the sources do not give (finding 4).

### What this audit does not do

It does not decide any fork.
The new forks it found (F27 to F34) are in section 3, each marked as this encoding's reading and not a ruling.
The fix pass after the independent test pass registered four more (F35 to F38), marked the same way.

## 0. Provenance, and what to know before trusting anything here

**Both sources are unofficial.**
`../../source/law.wiki` (the Interpretation Law 5741-1981) and `../../source/ordinance.wiki` (the Interpretation Ordinance [New Version]) are consolidations from Hebrew Wikisource ("ספר החוקים הפתוח", a volunteer project run by a bot, OpenLawBot, from the Knesset's law database), fetched 2026-10-13: revisions 2883979 (2024-09-23) and 2966850 (2025-12-08).
The official Knesset PDFs could not be fetched (`fs.knesset.gov.il` answered every request with an HTML "Unavailable" page), so nothing here is verified against the gazette, and every claim about either text rests on one unofficial copy.
`../../source/SOURCES.md` records the hashes and the official links.
Wikisource's own notes (the `{{ח:הערה|…}}` template) are part of the text as fetched; where this encoding leans on one, it says so.

**Pass 1 ran the L4 with the `l4` built 2026-10-13 16:13 from l4-ide `unstable`** (`~/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-41dd7a67/bin/l4`, `JL4_LIBRARY_PATH` unset).
`l4` has no `--version` and pass 1 was given no commit id, so that timestamp is all the provenance that binary had.

**Pass 2 ran the L4 with `unstable-20261028-5e95b5a (unstable, 5e95b5a, 2026-10-28)`**, sha256 `0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d`, `JL4_LIBRARY_PATH` unset, as `L4=<that binary> L4_TARGET=unstable ./check.sh`.
The pass-1 files gave the same numbers on this binary (630 assertions satisfied, 12 expected failures; the baseline in `PROGRESS.md`) as pass 1 recorded on its own.

**The fix pass ran with the same binary** (the same version string and sha256), as `L4=<that binary> L4_TARGET=unstable ./check.sh`.
Canon has no CI: the numbers in section 5 are a point-in-time record from that binary.

### 0.1 Expected answers, decided from the statute text before any module was run

These were written down first, from the words of s. 10 and s. 8 of the Law, and the tests were written from them.
One probe was run before they were written: `add months` and `add years` from `daydate` on twelve hard cases, to see what the library does on a 31st and on 29 February.
Every expected value below was derived from the words of s. 10 without looking at that output, and the output then agreed with it.
Where a value is a weekday, it was checked on a calendar (Python's `datetime`), not computed by the L4.

Reading used (Law s. 10, `law.wiki` lines 83-85):

- (a) "a fixed period in a number of days or weeks **from** a certain day: that day shall not be counted." The first counted day is the day after D, and the last day is D + N days (D + 7N for weeks).
- (b) "a fixed period in a number of months or years **after** a certain event ends in the last month on the day whose number in the month is as the number of the day of the event, and if the month lacks that day, on the last day of the month." The month of the end is the month of D plus N months (12N for years).
- (c) "days of rest, recess or holiday under an enactment are counted, **unless they are the last days of the period**." Taken to mean that the period does not end on such a day: it ends on the first day, from the nominal end on, that is not one.

| case | section | expected last day | weekday |
| --- | --- | --- | --- |
| three years from the day 2025-07-16 | 10(b) | 2028-07-16 | Sunday |
| five years from the day 2025-01-15 | 10(b) | 2030-01-15 | Tuesday |
| five years from the day 2025-09-01 | 10(b) | 2030-09-01 | Sunday |
| thirty days from the day 2026-01-01 | 10(a): 2026-01-01 not counted, days 2026-01-02 to 2026-01-31 | 2026-01-31 | Saturday |
| two years from the day 2024-02-28 | 10(b) | 2026-02-28 | Saturday |
| one year from the day 2024-02-29 | 10(b): February 2025 lacks the 29th | 2025-02-28 | Friday |
| one month from the day 2025-01-31 | 10(b): February 2025 lacks the 31st | 2025-02-28 | Friday |

With rest days chosen by the tests (illustrations, not a calendar of any country): 30 days from 2026-01-01 with 2026-01-31 a rest day ends on 2026-02-01; with 2026-01-31 and 2026-02-01 both, on 2026-02-02; with 2026-01-30 and 2026-01-31 both, on 2026-02-01.
The last case is the one that separates the readings of fork F3.
A rest day in the middle of a period does not move the end; a rest day just before an unaffected last day does not; a one-day period whose only day is a rest day ends on the next day that is not.
s. 8 makes "until D" include D.
s. 21 makes a statute bind from 00:01 on its commencement day, so 00:00 on that day is not yet bound; the Law binds from 00:01 on 1981-10-01 (s. 32 with s. 21); s. 33's thirty days from the adoption on 1981-05-20 end on 1981-06-19.

The large sweep in `tests-sweep.l4` (314 assertions) takes its expected values from `oracle-s10.py`, a second reading of s. 10 written in Python from the words.
It is the same reading in another language, so it catches slips in the L4 (a month-arithmetic off-by-one, a wrong leap rule) and not errors of reading.

## 1. What is encoded and what is not

**Every unit of both texts has a row in section 2 and one disposition.**
What follows names the modules; the coverage table says which rule encodes which unit and which assertions call it.

**Pass 1: the time rules** (module `il-interpretation-time.l4`, which imports only `prelude` and `daydate`, and is the module other encodings should import):

- Law s. 10(a), (b) and (c), each as its own named function, plus composed forms: the last day of N days or weeks from a day, of N months or years after an event, and of a period whose nominal last day falls on days of rest, recess or holiday; whether a date falls inside a period (for days, weeks, months and years).
  The "from a day" and "after the day" spellings are aliases that say which subsection governs.
- Law s. 8 ("עד" includes the day it names), for dates, numbers (the citation sense) and moments.
- Law s. 3: "יום" (a day is midnight to the midnight after it), "שנה" and "חודש" (which calendar; a period counted by the Hebrew calendar is a named refusal), "שנת כספים" (first day, last day, whether a date is in it).
- Law s. 21 (a statute binds from 00:01 on its commencement day), with the case where the statute fixes a moment of its own.
- The Ordinance's s. 17 (regulations of legislative effect come into force on the day of publication, unless another provision fixes the day), alone and with Law s. 21.

**Pass 1: the other computable provisions** (module `il-interpretation-law.l4`): Law s. 1 (the gate, "given before the Law commenced", which of s. 3 and Ordinance s. 1 defines a word, the calendar of year and month by vintage), s. 20, s. 22(2), s. 23, s. 24, s. 26, s. 31, s. 32, s. 33; Ordinance s. 16(4), s. 19, s. 42.

**Pass 2: the rest, in six new modules.** Each takes the facts it needs as a small typed record or a closed list, and answers whether a thing is within the term or the power.

**What `FALSE` and a refusal mean in every module (stated once, here).**
`FALSE` means the thing is outside the term, or the section does not extend to it; it does not mean "the Act says no".
A question about a private contract that asks whether the Law's rules of reading reach it answers FALSE because s. 1 names enactments and administrative directions and no contract, not because the Law forbids reading a contract.
A question the text does not answer is a named refusal (`REFUSE`, asserted with `#ASSERT REFUSED ... BECAUSE`).
An open entry (`לרבות`, "includes") never answers for a thing that is neither listed nor settled by the caller: an entry held as a record takes the word's ordinary or defined core as a field the caller must give, and an entry held as an enumeration refuses for a thing it does not list (F36).
A closed entry (a plain dash, or the Law's "each of these", `כל אחד מאלה`) answers FALSE for a thing it does not list.
**The carried-text constants** in `il-interpretation-carried-text.l4` (among them 23 definitions of Law s. 3 and 65 entries of Ordinance s. 1) are strings that nothing reads; they are kept so that the carried text is a faithful quotation, and the computed rules are in the pass-2 modules.

| module | what it encodes |
| --- | --- |
| `il-interpretation-gate.l4` | Law s. 1's gate as a helper: `under s 1, the Law's answer for` a matter `is` an answer. The Law is displaced when another provision deals with the matter or its context is inconsistent, and the rules of reading then REFUSE rather than answer FALSE. |
| `il-interpretation-reading.l4` | Law s. 2 (a defined term bears its definition), s. 4 (a person includes a body of persons), s. 5 (singular and plural), s. 6 (masculine and feminine), s. 7 ("or" and "other" do not infer from the list), s. 9 ("according to" an enactment includes according to its regulations), s. 25 (a reference to an enactment: the wording in force when it is resorted to, and provisions that took its place). |
| `il-interpretation-powers.l4` | Law ss. 11 to 19, the scope of a grant of power: no time fixed (proper speed, again as required), exemption in part or on conditions, appointment by name or by office, power to suspend and dismiss, power over regulations and directions, a body of members with a chairman and alternates, procedure and ancillary powers, appeals, and no derogation from another enactment. |
| `il-interpretation-repeal.l4` | Law s. 22(1) (a repeal cannot revive what had no validity at the hour it took effect) and s. 22(3) (it cannot affect a right or obligation under the repealed law). |
| `il-interpretation-definitions-law.l4` | The 23 entries of Law s. 3 that pass 1 had left as text, each as a function over the facts the entry names (what it includes, excludes or points at), and the opening words as a dispatcher over all 27 words of the entries (`s 3 — section 3 governs`), which gives pass 1's vintage rule an entry to ask about. Entries that point at the Penal Law ("sin", "misdemeanour", "felony") ask the pointed-at fact as an input. |
| `il-interpretation-definitions-ordinance.l4` | The 61 live entries of Ordinance s. 1, the earlier meanings that its notes state, a selector for which meaning of the six words with provisos governs an enactment of a given age, and a dispatcher over all 66 entries (`Ordinance s 1 — the Ordinance's definitions govern`), which says that the Ordinance's definitions govern the words of an enactment given before the Law and not those of a later one (F33). Entries with the same words as the Law's call the Law's function. |

**What the fix pass added to those modules** (the independent test pass is described in `## Changes to existing modules` and in findings 15 to 19).
`-gate`: `s 1 — section` n `of the Law reaches an instrument of the kind` k `given on` d (sections 2 and 4 to 26 reach every enactment and administrative direction whatever its date; section 3 refuses for an earlier enactment, because its reach turns on the word; a private contract and any other document are not reached) (F37).
`-reading`: `s 25 — a reference to an enactment made in an instrument of the kind` (F37); the members of s. 7's "or", "other" and signs of analogy as fields of their own.
`-powers`: `s 13(b) — the person bound on` d `by a designation that names` (a name alone, the office alone, or both: the third refuses) and `s 13(b) — the rule that the office-holder from time to time is bound applies to a designation that names`; `s 20 — where the enactment's requirement that all act is` and `s 20 — the rule of the majority applies ...` (an enactment that requires all to act is another provision, s. 1).
`-repeal`: `Ordinance consolidation — what the text shows for section` and `s 31 and the consolidation of the Ordinance agree on section` (F15); Ordinance s. 17 as publication in Reshumot and the day validity has begun (`Ordinance s 17 — the regulation must be published in Reshumot:` and `Ordinance s 17 — the validity of the regulation has begun by`).
`-definitions-law`: `s 3 — where the meaning of the entry is found:` (sin, misdemeanour and felony are found in the Penal Law, 5737-1977; the other entries in s. 3 itself); the members of the lists of the entries "law", "in writing", "possession", "final" and "administrative direction".
`-definitions-ordinance`: the open entries refuse for an unlisted thing (F36); `Ordinance s 1 — the Ordinance's definitions govern` e `in an instrument of the kind` k `given on` d (F37); "determined" refuses for a regulation that itself uses the word; "judge" knows the office of president of a magistrates' court (outside the extension); the members of the lists set out below as fields or constructors of their own.

**Lists inside entries: the phrase as printed and each member are both askable.**
Where an entry names alternatives, the function takes the phrase as the entry prints it and each member as a field or constructor of its own, so a caller can ask about the phrase, about one member, or about a thing the entry does not name (which is not named: every member field is FALSE, or the constructor is `anything else`).
A script (run again at the end of the fix pass) swept every field and constructor name in the six pass-2 `.l4.in` files for a comma, "or" or "and", and each hit was decided against the Hebrew line.
*Extended* (fields are appended at the end of the record; constructors are added beside the phrase's):

- Ordinance "person" (line 33): company, association, body of persons (3 fields).
  "Representative of the Attorney General" (35): the State Attorney's deputy, an assistant of the State Attorney, a district attorney, a deputy of a district attorney (4 constructors).
  "House" (37): building, other structure (2 fields).
  "In writing" (41): print, lithography, typewriting, photography (4 fields).
  "Law" (42 to 46): Act of the British Parliament, Order in Council, and order, regulation, rule, by-law, manifesto, direction, notice, other document given by virtue of them, oral and written religious law, the common law of England, the principles of equity (14 constructors).
  "Seaman" (55): works on a ship, is employed on it (2 fields).
  "Import" and "export" (54, 56): by sea, by land, by air (3 fields).
  "Street" (99): highway, avenue, lane, bridle path, footpath, square, courtyard, promenade, alley, passage (10 fields).
  "Local authority" (101): municipality, local council, an authority like them (3 fields).
  "Possession" (111): use, residence, possession, enjoyment (4 fields).
  "Regulation" (112): regulation, rule, by-law, manifesto, proclamation, order, direction, notice, announcement, other document (10 fields).
  Three notes and an entry: "immovables" (note, 76: 9 constructors), "ordinance" (note, 88: regulations made under an ordinance and orders made under one; 2 constructors), and "contravene" (79: a requirement or condition set in a permit, a licence or another authorisation; 3 constructors).
- Law "in writing" (line 31): letters, numerals, signs (3 fields).
  "Law" (32 to 36): Act of the British Parliament or part of it, Order in Council or part of it, regulations under them, oral and written religious law, the common law, the principles of equity (7 constructors).
  "Administrative direction" (37): direction, appointment, notice, announcement, licence, permit, something like them (7 fields).
  "Final" (42): appeal, appeal by petition (`ערר`), objection, a like remedy (4 fields).
  "Possession" (60): use, possession, enjoyment (3 fields).
  Law s. 7: the words "or" and "other", an expression like them; "similar", "of like kind", another expression of analogy (6 fields).

*Checked and left, with the reason* (every hit of the sweep that is neither above nor here is a rule's own name, or a phrase that names one thing):

- Members that are already a constructor of their own: Law "consul" (55), "local authority" (56) and s. 12's exemption, relief and discount (`A consular post`, `A local body`, `What a power to give relief grants`); Ordinance "sale" (69), "will" (91) and "lease" (106) (`A transaction or offer`, `A testamentary document`, `A letting`).
- Ordinance "Inspector General of Police" and "Commissioner of Prisons": the first constructor is the post itself and the extension adds the deputy; `anyone else` is outside, not unlisted.
- Alternatives of one test, where whichever member holds the test is met and no answer depends on which:
  "ship" ("oars or paddles", 34); "house" ("dwell in or occupy"; "by right or otherwise, by day or night"; "wholly or partly below the surface"); "in writing" ("presents words or numerals, or copies them", 41); "repeal" ("by or under which", 36);
  "regulation" ("by virtue of an Act of the British Parliament or an Order in Council"; "by an authority in Palestine or in Israel"; "a regulation, rule or by-law of that kind", 112);
  "import" ("brought or caused to be brought"); "street" (the two pairs in the open-place limb: "uses it or customarily passes through it", "enters it or may enter it", 99);
  "Government Printer" ("an enactment or a State document"; "the Government Printer or a printer so authorised"; "generally or specially", 61); "public notice" ("of the Government or on its behalf");
  "possession" ("employee or official"; "supervision or guarding", F28); "representative or agent" (a synonym pair in the entry's own heading); "balloon, tethered or not"; "regulations or orders" (114);
  Law s. 9 ("according to" or an expression like it, 80), whose test is the same for either member and whose answer is the same.
- Conjunctions, one test of facts joined by "and", where the flag is the caller's judgement of both: the apprentice "bound by a contract and properly registered" in "seaman" (55); the Mandate "approved and its terms defined" by the Council of the League of Nations (70); Law s. 11 ("with proper speed, and again from time to time as required", 90); "rules of procedure" ("practice and procedure", 114).
- A gloss and a threshold, neither a list: "an engineer or mechanic" is one Hebrew word (`מכונאי`, "crew", 92); "senior police officer" is "assistant district commander or higher" (103).
- Law "determined" (51, `בחיקוק`): unchanged; it already has its own place for "in regulations made under that enactment".

**Tests.** `tests-reading.l4` (130), `tests-powers.l4` (116), `tests-repeal.l4` (139), `tests-definitions-law.l4` (235), `tests-definitions-ordinance.l4` (801) and `tests-ordinance-sweep.l4` (49) are satisfied.
`tests-red-completion.l4` has 14 expectations that are meant to fail (section 5).
Expected values were decided from the words of each provision, before the module was run; each group of assertions carries a comment naming the units it tests, and the expected answer is the `NOT` or its absence on the assertion.
`tests-definitions-ordinance.l4` is generated by `gen-tests-ordinance.py`, where the facts of each case (a string of T and F per record field) sit beside the expected answer; running the script rewrites the test file byte for byte (checked), so the script is the record of how the 801 cases were chosen and the `.l4` file is the record of what was run.

**What the text does not answer, and the encoding says so (explicit "not covered" values, each asserted).**

- A period counted by the Hebrew calendar (pass 1; named refusal).
- A day-level date on 1981-10-01, which cannot say whether an enactment came before 00:01 (named refusal; the moment-level function settles it).
- The earlier meaning of "enactment" (`חיקוק`) in an enactment given before the Ordinance: the entry says only that it means what it would have meant without the Ordinance, and no note or other text of the sources says what that was.
- Any question about the whole of Ordinance s. 16 (it is saved by subsection, not as a whole).
- A question that Law s. 1's gate turns away (another provision deals with the matter, or the context is inconsistent): the rules of reading and powers REFUSE.
- Law s. 7 asked of a word that is not "or", "other" or like them; Law s. 11 asked of an authorisation that fixes a time; Law s. 19 asked of something other than the grant by itself; Law s. 22(1) asked of a thing that was valid at the hour; Law s. 22(3) asked of a right that does not arise under the repealed law.
- Which days are days of rest, recess or holiday (an input; pass 1).

**Not encoded at all:** nothing in the text is left without a row.
The content of Law ss. 27 to 30 is blank in the text (a note says each was incorporated into another enactment, which is not among the sources), and has a `repealed or blank in this text` row.
The Hebrew calendar and a calendar of holidays are not computed (named refusal and input).
Periods that s. 10 does not speak of (counted backwards, "within", mixed units: F8) are not computed.

**Files** (all under `encodings/legalese-sonnet-5.5/`):

| file | what it is |
| --- | --- |
| `il-interpretation-time.l4` | the reusable time module (pass 1) |
| `il-interpretation-law.l4` | the other computable provisions (pass 1) |
| `il-interpretation-carried-text.l4` | quoted text, generated by `gen-carried.py` (pass 1); see `## Changes to existing modules` for what in it is stale |
| `il-interpretation-gate.l4`, `-reading.l4`, `-powers.l4`, `-repeal.l4`, `-definitions-law.l4`, `-definitions-ordinance.l4` | pass 2 modules; each is expanded from a `.l4.in` file by `expand-quotes.py` |
| `tests-time.l4`, `tests-law.l4`, `tests-worked-cases.l4`, `tests-sweep.l4` | tests (pass 1; the sweep is generated by `oracle-s10.py`) |
| `tests-reading.l4`, `tests-powers.l4`, `tests-repeal.l4`, `tests-definitions-law.l4`, `tests-definitions-ordinance.l4`, `tests-ordinance-sweep.l4` | tests (pass 2) |
| `tests-red.l4`, `tests-red-completion.l4` | expectations that are meant to fail: 12 (F1 to F25) and 14 (F27 to F34) |
| `check.sh`, `srcrefs.py` | the self-check; the quotation and locator gate |
| `inventory.py`, `coverage-data.py`, `gen-coverage.py` | the unit count, the dispositions and the table generator |
| `gen-tests-ordinance.py` | generates `tests-definitions-ordinance.l4` (801 assertions) from the facts and expected answers it holds |
| `quote-hebrew.py`, `expand-quotes.py`, `gen-carried.py`, `oracle-s10.py` | how the Hebrew was quoted (a script reads the file; none is typed by hand), the `.l4.in` files expanded, the carried module generated, and the sweep generated |
| `encoding.json`, `SOURCE-LICENSE.md` | descriptors |

**A limit on reuse.**
The functions that take days of rest take a `FUNCTION FROM DATE TO BOOLEAN`, and, per the `writing-l4-rules` skill (R-X4), a rule with a function-typed input cannot be `@export`ed, because an API request carries values and not rules.
I did not test that here.
A caller who wants an API wraps one of these functions in a rule that takes a `LIST OF DATE` and passes `days of rest, recess or holiday listed in` that list; no such wrapper is provided.

**How the Hebrew got into the L4.**
Every Hebrew quotation is a `-- src:N | …` comment produced by `quote-hebrew.py` reading `../../source/*.wiki` (pass-2 modules: `expand-quotes.py` expanding a `--@@` directive in a `.l4.in` file with `quote-hebrew.py`), and `check.sh` runs `srcrefs.py check --refs` over every module to confirm each is a verbatim slice of the source and each `@ref` locator lies inside a quotation.
The operative modules cite their lines with `@ref … (src:N)` for the Law and `(src:ordinance:N)` for the Ordinance.
English paraphrases and glosses beside the quotations are mine and say so.
`srcrefs.py` does not check that a locator names the right provision, so the line of each entry was taken from `inventory.py`'s listing and not typed from memory.

**Reading the pass-2 rule names.**
A rule name that begins `Ordinance s 1 "gloss"` encodes the entry of Ordinance s. 1 whose headword the gloss translates; `s 3 "gloss"` is the entry of Law s. 3.
The gloss is mine and the Hebrew governs.
A rule that begins `s 1 —`, `s 2 —` and so on encodes that section of the Law.

## 2. Coverage table

One row per unit of the two texts (226), generated by `gen-coverage.py` from the wikitext (`inventory.py`) and the dispositions (`coverage-data.py`); do not edit it by hand, run `python3 -I gen-coverage.py --write`.
Columns: the unit's id (L = the Law, O = the Ordinance; `L3d07` the 7th entry of Law s. 3, `O1d33` the 33rd entry of Ordinance s. 1, `O1n5` the 5th editorial note in Ordinance s. 1), what it is, its kind, its raw line(s) in the wikitext file (the same numbers as the `src:` locators), what the text shows, its disposition, and the module and the number of assertions per test file that call the rule that encodes it.
Dispositions: `encoded`; `fork` (with the fork ids of section 3); `inert 1` (reason 1: not operative; no row is inert for reason 2 or 3); `repealed` (repealed or blank in this text).
The "where" column counts the assertions in each test file whose text contains the rule's name, so `tests-red 1` means one expected failure in `tests-red.l4` calls it.

<!-- COVERAGE:BEGIN (generated by gen-coverage.py from inventory.py and coverage-data.py; do not edit by hand) -->

#### Part A: the Interpretation Law 5741-1981 (83 units: encoded 49, fork 19, inert 1 11, repealed 4)

| id | unit | kind | raw lines | the text shows | disposition | where (module; assertions that call it), and why |
| --- | --- | --- | --- | --- | --- | --- |
| Ltitle | חוק הפרשנות, התשמ״א–1981 | title | 2 | content | inert 1 | the title |
| Lhist | publication history | history | 5 | content | inert 1 | the gazette citations of the Law and of its three amendments; publication history, no rule |
| Lch1 | פרק א׳: תחולה}} | chapter | 19 | content | inert 1 | a chapter heading |
| L1 | תחולת החוק וסייגיה | section | 21-22 | content | fork (F14, F37) | il-interpretation-gate, il-interpretation-law; tests: tests-law 34; tests-reading 69. the gate, the vintage of the words of s 3, and 'given before the commencement' |
| L2 | תחולת הגדרות שבחיקוק | section | 24-25 | content | encoded | il-interpretation-reading; tests: tests-reading 10. a defined term bears its definition, in regulations under the enactment, in its grammatical forms |
| Lch2 | פרק ב׳: פירוש מלים וביטויים}} | chapter | 27 | content | inert 1 | a chapter heading |
| L3d01 | ”בכתב“ | definition | 31 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 9. in writing |
| L3d02 | ”דין“ | definition | 32 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 26. law: the stem and its limbs |
| L3d02.1 | (1) of ”דין“ | paragraph | 33 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 26. a limb of 'law' |
| L3d02.2 | (2) of ”דין“ | paragraph | 34 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 26. a limb of 'law' |
| L3d02.3a | (3)(א) of ”דין“ | paragraph | 35 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 26. a limb of 'law' |
| L3d02.3b | (3)(ב) of ”דין“ | paragraph | 36 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 26. a limb of 'law' |
| L3d03 | ”הוראת מינהל“ | definition | 37 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 14. administrative direction |
| L3d04 | ”הפרה“, לענין דרישה או הוראה | definition | 38 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 4. breach |
| L3d05 | ”חוק“ | definition | 39 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 4. statute |
| L3d06 | ”חטא“ | definition | 40 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 29. sin: points at the Penal Law, which is not among the sources; asked as a fact, and the source of the meaning named |
| L3d07 | ”חיקוק“ | definition | 41 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 4. enactment |
| L3d08 | ”חלוט“, לענין פסק דין או החלטה של בית משפט | definition | 42 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 7. final |
| L3d09 | ”יום“ | definition | 43 | content | fork (F5) | il-interpretation-time; tests: tests-red 1; tests-time 13. day (existing module) |
| L3d10 | ”מחוז“ | definition | 44 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 5. district |
| L3n1 | editorial note: הממשלה פרסמה הודעה על חלוקת שטח המדינה למחוזות ולנ | note | 45 | content | inert 1 | an editorial note that the Government published a notice dividing the State into districts; it creates no rule |
| L3d11 | ”מיטלטלין“ או ”טובין“ | definition | 46 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 6. movables |
| L3d12 | ”מימי חופין“ | definition | 47 | content | fork (F29) | il-interpretation-definitions-law; tests: tests-definitions-law 6; tests-red-completion 1. coastal waters: a strip of twelve nautical miles; whether the outer edge is inside |
| L3n2 | editorial note: לפי סעיף 1(ב) לחוק מימי חופין, תשי״ז–1956 ההגדרה ” | note | 48 | content | fork (F14) | il-interpretation-law; tests: tests-law 13. an editorial note: by s 1(b) of the Coastal Waters Law the definition applies to earlier enactments |
| L3d13 | ”מקרקעין“ | definition | 49 | content | fork (F27) | il-interpretation-definitions-law; tests: tests-definitions-law 11; tests-red-completion 1. immovables: the exception 'except detachable fixtures' reaches the last limb or all |
| L3d14 | ”נציג היועץ המשפטי לממשלה“ או ”בא כוח היועץ המשפטי לממשלה“ | definition | 50 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 3. representative of the Attorney General |
| L3d15 | ”נקבע“ | definition | 51 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 3. determined |
| L3d16 | ”עוון“ | definition | 52 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 29. misdemeanour: points at the Penal Law; asked as a fact, and the source of the meaning named |
| L3d17 | ”פשע“ | definition | 53 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 29. felony: points at the Penal Law; asked as a fact, and the source of the meaning named |
| L3d18 | ”פקודה“ | definition | 54 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 4. ordinance |
| L3d19 | ”קונסול“ או ”נציג קונסולרי“ | definition | 55 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 6. consul |
| L3d20 | ”רשות מקומית“ | definition | 56 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 5. local authority |
| L3d21 | ”שנה“ ו”חודש“ | definition | 57 | content | fork (F22, F24) | il-interpretation-time; tests: tests-time 4. year and month (existing module) |
| L3d22 | ”שנת כספים“ | definition | 58 | content | encoded | il-interpretation-time; tests: tests-time 6. fiscal year (existing module) |
| L3d23 | ”תאגיד“ | definition | 59 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 5. corporation |
| L3d24 | ”תפישה“, לענין מקרקעין | definition | 60 | content | fork (F28) | il-interpretation-definitions-law; tests: tests-definitions-law 13; tests-red-completion 1. possession: 'not merely as an employee ... or merely for supervision' read as neither nor |
| L3d25 | ”תצהיר“ | definition | 61 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 4. affidavit |
| L3d26 | ”תקנה“ | definition | 62 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 5. regulation |
| L3 | משמעותם של מלים וביטויים | section | 29-62 | content | encoded | il-interpretation-definitions-law; tests: tests-definitions-law 58; tests-definitions-ordinance 5. the opening words: the listed words mean what is explained beside them (the dispatcher over all 26 entries) |
| L4 | אדם | section | 64-65 | content | encoded | il-interpretation-reading; tests: tests-reading 5. a reference to a person reaches a body of persons, corporate or not |
| L5 | יחיד ורבים | section | 67-68 | content | encoded | il-interpretation-reading; tests: tests-reading 6. singular and plural |
| L6 | זכר ונקבה | section | 70-71 | content | encoded | il-interpretation-reading; tests: tests-reading 5. masculine and feminine |
| L7 | הכלל אינו מעין הפרט דוקא | section | 73-74 | content | encoded | il-interpretation-reading; tests: tests-reading 12. 'or' and 'other' distinguish from the list before them unless an analogy word accompanies |
| L8 | ”עד...“ | section | 76-77 | content | encoded | il-interpretation-time; tests: tests-red 1; tests-time 6. 'until' includes the day it names (existing module) |
| L9 | ”לפי“ | section | 79-80 | content | encoded | il-interpretation-reading; tests: tests-reading 5. 'according to' an enactment includes according to regulations made under it |
| L10a | (א) מקום שנקבעה תקופה קצובה במספר ימים או שב | subsection | 83 | content | fork (F6, F7) | il-interpretation-time; tests: tests-red 1; tests-sweep 28; tests-time 16; tests-worked-cases 1. days and weeks from a day (existing module) |
| L10b | (ב) תקופה קצובה במספר חדשים או שנים לאחר איר | subsection | 84 | content | fork (F1, F24, F25) | il-interpretation-time; tests: tests-red 2; tests-sweep 143; tests-time 40. months and years after an event (existing module) |
| L10c | (ג) במנין ימי תקופה יבואו גם ימי מנוחה, פגרה | subsection | 85 | content | fork (F2, F3, F11) | il-interpretation-time; tests: tests-time 3. days of rest, recess or holiday (existing module) |
| L10 | תקופות | section | 82-85 | heading only; the rules are in its subse | inert 1 | the heading 'Periods'; the rules are in (a), (b) and (c) |
| Lch3 | פרק ג׳: פירוש הסמָכוֹת}} | chapter | 87 | content | inert 1 | a chapter heading |
| L11 | מקום שלא נקבע זמן | section | 89-90 | content | encoded | il-interpretation-powers; tests: tests-powers 13. no time fixed: power or duty to act with proper speed and again as circumstances require |
| L12 | סמכות לפטור | section | 92-93 | content | encoded | il-interpretation-powers; tests: tests-powers 9. a power to grant an exemption, relief or discount includes granting it in part or on conditions |
| L13a | (א) מקום שניתנה סמכות למנות אדם, להסמיכו או  | subsection | 96 | content | encoded | il-interpretation-powers; tests: tests-powers 7. appointing, authorising or charging a person by name or by the name of the office |
| L13b | (ב) מינוי אדם, הסמכתו או הטלת חובה עליו בנקי | subsection | 97 | content | encoded | il-interpretation-powers; tests: tests-powers 22. an appointment by the name of the office alone is of whoever fills the office from time to time |
| L13 | מינוי והסמכה – כיצד | section | 95-97 | heading only; the rules are in its subse | inert 1 | the heading 'Appointment and authorisation: how'; the rules are in (a) and (b) |
| L14 | סמכות מינוי | section | 99-100 | content | encoded | il-interpretation-powers; tests: tests-powers 7. a power of appointment includes suspending, cancelling, dismissing and suspending the appointee |
| L15 | סמכות התקנה | section | 102-103 | content | encoded | il-interpretation-powers; tests: tests-powers 9. a power to make regulations or give a direction includes amending, changing, suspending and cancelling them in the way they were made |
| L16 | סמכות מינוי גוף | section | 105-106 | content | fork (F30) | il-interpretation-powers; tests: tests-powers 8; tests-red-completion 1. a power to appoint a body of several members includes appointing a chairman and an alternate for each member; 'several' read as at least two |
| L17a | (א) הסמכה לעשות דבר או לדון בענין פלוני או ל | subsection | 109 | content | encoded | il-interpretation-powers; tests: tests-powers 7. a power to do, hear or decide includes fixing procedure where an enactment has not |
| L17b | (ב) הסמכה לעשות דבר או לכפות עשייתו – משמעה  | subsection | 110 | content | encoded | il-interpretation-powers; tests: tests-powers 6. a power to do a thing or compel it includes the ancillary powers needed, to a reasonable extent |
| L17 | סמכויות עזר | section | 108-110 | heading only; the rules are in its subse | inert 1 | the heading 'Ancillary powers'; the rules are in (a) and (b) |
| L18 | סמכות בהשגה ובערר | section | 112-113 | content | encoded | il-interpretation-powers; tests: tests-powers 9. a power to hear an appeal or objection includes confirming, cancelling and deciding otherwise, or returning the matter |
| L19 | שמירת סמכויות וחובות | section | 115-116 | content | encoded | il-interpretation-law, il-interpretation-powers; tests: tests-law 11; tests-powers 3; tests-red 1. a grant of power or imposition of duty under one enactment does not by itself derogate from a power or duty under another |
| L20 | פעולת מספר בני אדם | section | 118-119 | content | fork (F17, F30) | il-interpretation-law, il-interpretation-powers; tests: tests-law 11; tests-powers 16; tests-red-completion 1; tests-red 1. an act imposed on several persons is valid if done by most of them (existing module); where the enactment requires all to act, s 1's gate makes the module refuse |
| Lch4 | פרק ד׳: דין חיקוקים}} | chapter | 121 | content | inert 1 | a chapter heading |
| L21 | שעת תחילה | section | 123-124 | content | fork (F12, F26, F35) | il-interpretation-time; tests: tests-time 4. the hour a statute begins to bind (existing module) |
| L22.1 | (1) להחיות דבר שלא היה לו תוקף בשעה שהביטול  | subsection | 128 | content | fork (F31) | il-interpretation-repeal; tests: tests-red-completion 1; tests-repeal 12. a repeal cannot revive what had no validity when it took effect; the boundary at the hour of the repeal |
| L22.2 | (2) להשפיע על פעולה קודמת של הדין המבוטל או  | subsection | 129 | content | fork (F18) | il-interpretation-law; tests: tests-law 5. a repeal cannot affect an earlier act (existing module) |
| L22.3 | (3) להשפיע על זכות או חיוב שלפי הדין המבוטל. | subsection | 130 | content | encoded | il-interpretation-repeal; tests: tests-repeal 4. a repeal cannot affect a right or obligation under the repealed law |
| L22 | סייגים לכוחו של ביטול | section | 126-130 | content | encoded | il-interpretation-law, il-interpretation-repeal; tests: tests-law 5; tests-red-completion 1; tests-repeal 16. the stem 'the repeal of a law has no force ...' is completed by each limb; see (1), (2) and (3) |
| L23 | תקנות ומינויים לפי חיקוק שבוטל | section | 132-133 | content | fork (F19) | il-interpretation-law; tests: tests-law 2. regulations and appointments under a repealed enactment (existing module) |
| L24 | הנוסח המחייב | section | 135-136 | content | encoded | il-interpretation-law; tests: tests-law 4. the binding text of a law (existing module) |
| L25 | פירושם של אזכורים | section | 138-139 | content | fork (F31, F37) | il-interpretation-reading; tests: tests-reading 18; tests-red-completion 1. a reference to an enactment is to it as worded when it is resorted to, with added provisions and those that took its place; the day a version takes over |
| L26 | סטיה מטופס | section | 141-142 | content | encoded (F38) | il-interpretation-law; tests: tests-law 8. a slight deviation from a form (existing module) |
| Lch5 | פרק ה׳: שונות}} | chapter | 144 | content | inert 1 | a chapter heading |
| L27 | (none) | section | 146-147 | blank: only a note (the text was incorpo | repealed | blank: the only text is a note that the section's text was incorporated into another enactment |
| L28 | (none) | section | 149-150 | blank: only a note (the text was incorpo | repealed | blank: the only text is a note that the section's text was incorporated into another enactment |
| L29 | (none) | section | 152-153 | blank: only a note (the text was incorpo | repealed | blank: the only text is a note that the section's text was incorporated into another enactment |
| L30 | (none) | section | 155-156 | blank: only a note (the text was incorpo | repealed | blank: the only text is a note that the section's text was incorporated into another enactment |
| L31 | ביטול | section | 158-159 | content | fork (F15) | il-interpretation-law; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 1. the Ordinance is repealed except 16(2), 16(4), 17, 19, 42 (existing module) |
| L32 | תחילה | section | 161-162 | content | encoded (F35) | il-interpretation-law; tests: tests-law 3. the Law commenced on 1981-10-01 (existing module) |
| L33 | פרסום | section | 164-165 | content | fork (F21) | il-interpretation-law; tests: tests-law 5. the Law is to be published within thirty days of its adoption (existing module) |
| Lsig | נתקבל בכנסת ביום ט״ז באייר התשמ״א (20 במאי 1981). | signature | 167-169 | content | encoded | il-interpretation-law; tests: tests-law 2. the day of adoption, which s 33's thirty days count from (existing module); the signatories' names are not operative |

#### Part B: the Interpretation Ordinance [New Version] (143 units: encoded 74, fork 12, inert 1 4, repealed 53)

| id | unit | kind | raw lines | the text shows | disposition | where (module; assertions that call it), and why |
| --- | --- | --- | --- | --- | --- | --- |
| Otitle | פקודת הפרשנות | title | 2 | content | inert 1 | the title |
| Ohist-old | publication history of the old text (נוסח ישן) | history | 5 | content | inert 1 | publication history; no rule |
| Ohist-new | publication history of the new text (נוסח חדש) | history | 7 | content | inert 1 | publication history; no rule |
| Ohead | editorial note at the head of the text | note | 12 | content | fork (F14, F33, F37) | il-interpretation-definitions-ordinance, il-interpretation-law; tests: tests-definitions-ordinance 232; tests-law 13; tests-red-completion 1. an editorial note: the Ordinance was largely replaced by the Law; which words keep the Ordinance's definitions |
| Och1 | פרק ראשון: עקרונות כלליים | chapter | 28 | content | repealed | a chapter heading that the text marks `(בוטל)` |
| O1n1 | editorial note: בהתאם לסעיפים 1 ו־3 לחוק הפרשנות וסעיף 1(ב) לחוק מ | note | 31 | content | fork (F14, F33, F37) | il-interpretation-definitions-ordinance, il-interpretation-law; tests: tests-definitions-ordinance 232; tests-law 13; tests-red-completion 1. an editorial note restating Law ss 1 and 3: the definitions apply to earlier enactments, except five words |
| O1d01 | ”אדם“ | definition | 33 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 9. "person" |
| O1d02 | ”אניה“ או ”ספינה“ | definition | 34 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 4. "ship" |
| O1d03 | ”בא כוח, או נציג, של היועץ המשפטי לממשלה“ | definition | 35 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 10. "representative of the Attorney General" |
| O1d04 | ”ביטול“, של דין | definition | 36 | content | encoded (F36) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 6. "repeal" |
| O1d05 | ”בית“ | definition | 37 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 15. "house" |
| O1d06 | ”בית משפט“ | definition | 38 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 3. "court" |
| O1d07 | ”בית משפט לערעורים אזרחיים“ | definition | 39 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 5. "court of civil appeals" |
| O1d08 | ”בית משפט לערעורים פליליים“ | definition | 40 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 5. "court of criminal appeals" |
| O1d09 | ”בכתב“ | definition | 41 | content | fork (F34) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 11; tests-red-completion 1. "in writing" |
| O1d10 | ”דין“ | definition | 42 | content | encoded (F36) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 44. "law" |
| O1d10.1 | (1) of ”דין“ | paragraph | 43 | content | encoded (F36) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 44. a limb of "law" |
| O1d10.2 | (2) of ”דין“ | paragraph | 44 | content | encoded (F36) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 44. a limb of "law" |
| O1d10.3 | (3) of ”דין“ | paragraph | 45 | content | encoded (F36) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 44. a limb of "law" |
| O1d10.4 | (4) of ”דין“ | paragraph | 46 | content | encoded (F36) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 44. a limb of "law" |
| O1d11 | ”הצהרה בשבועה“ | definition | 47 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 5. "declaration on oath" |
| O1d12 | ”חוק“ | definition | 48 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 12. "statute" |
| O1n2 | editorial note: ההגדרה החלה על חיקוק שניתן לפני פרסום הנוסח החדש ל | note | 49 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 12. note under "statute": what the word meant in an enactment given before the new text |
| O1d13 | ”חטא“ | definition | 50 | blank: `(בוטלה)` (repealed) | repealed | "sin": the entry reads `(בוטלה)`; the note under it gives the Law's definition, which governs earlier enactments |
| O1n3 | editorial note: לפי סעיף 1 לחוק הפרשנות, ההגדרה שלהלן תחול גם על ח | note | 51 | content | encoded | il-interpretation-definitions-law, il-interpretation-law; tests: tests-definitions-law 2; tests-law 13. note under "sin": the Law's definition applies to earlier enactments too |
| O1d14 | ”חיקוק“ | definition | 52 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 15. "enactment" |
| O1d15 | ”חתימה“, באדם שאינו יכול לכתוב שמו | definition | 53 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 5. "signature" |
| O1d16 | ”ייבוא“ | definition | 54 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 10. "import" |
| O1d17 | ”יורד ים“ | definition | 55 | content | fork (F34) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 12; tests-red-completion 1. "seaman" |
| O1d18 | ”ייצוא“ | definition | 56 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 10. "export" |
| O1d19 | ”ישראל“ או ”המדינה“ | definition | 57 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 7. "Israel" |
| O1d20 | ”כלי טיס“ | definition | 58 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 5. "aircraft" |
| O1d21 | ”כלי שיט“ | definition | 59 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 6. "vessel" |
| O1d22 | ”לירה“ | definition | 60 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 2. "pound" |
| O1d23 | ”מדפיס ממשלתי“ | definition | 61 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 9. "Government Printer" |
| O1d24 | ”מזכיר הממשלה“ | definition | 62 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 2. "Secretary to the Government" |
| O1d25 | ”מודעה לרבים“ | definition | 63 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 4. "public notice" |
| O1d26 | ”מחוז“ | definition | 64 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 4. "district" |
| O1d27 | ”מיטלטלין“ או ”טובין“ | definition | 65 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 10. "movables" |
| O1n4 | editorial note: ההגדרה החלה על חיקוק שניתן לפני תחילת חוק המיטלטלי | note | 66 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 10. note under "movables": what the word meant in an enactment given before the Movables Law |
| O1d28 | ”מימי חופין“ | definition | 67 | blank: `(בוטלה)` (repealed) | repealed | "coastal waters": the entry reads `(בוטלה)`; the note under it gives the Law's definition, which governs earlier enactments |
| O1n5 | editorial note: לפי סעיף 1(ב) לחוק מימי חופין, תשי״ז–1956, ההגדרה  | note | 68 | content | fork (F23, F29) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 19; tests-red-completion 1. note under "coastal waters": the definition, in miles; the Law says nautical miles |
| O1d29 | ”מֶכֶר“ | definition | 69 | content | encoded (F36) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 7. "sale" |
| O1d30 | ”מנדט“ | definition | 70 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 5. "Mandate" |
| O1d31 | ”מנשר“ או ”אכרזה“ | definition | 71 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 4. "proclamation" |
| O1d32 | ”מסירה לדין“ | definition | 72 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 3. "committal for trial" |
| O1d33 | ”מפקד“, בכלי טיס | definition | 73 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 4. "commander of an aircraft" |
| O1d34 | ”מפקח כללי של המשטרה“ | definition | 74 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 3. "Inspector General of Police" |
| O1d35 | ”מקרקעין“ | definition | 75 | content | fork (F27) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 27; tests-red-completion 1. "immovables" |
| O1n6 | editorial note: ההגדרה החלה על חיקוק שניתן לפני תחילת חוק המקרקעין | note | 76 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 27; tests-red-completion 1. note under "immovables": what the word meant in an enactment given before the Land Law |
| O1d36 | ”נציב בתי הסוהר“ | definition | 77 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 3. "Commissioner of Prisons" |
| O1d37 | ”נקבע“ | definition | 78 | content | encoded (F36) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 4. "determined" |
| O1d38 | ”עבור“ או ”הפר“, לענין דרישה או תנאי שנקבעו בחיקוק, או בכל היתר, רשיון | definition | 79 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 14. "contravene" |
| O1d39 | ”עבירה“ | definition | 80 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 6. "offence" |
| O1d40 | ”עובד ציבורי“ או ”משרד ציבורי“ | definition | 81 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 7. "public servant" |
| O1d41 | עוון | definition | 82 | blank: `(בוטלה)` (repealed) | repealed | "misdemeanour": the entry reads `(בוטלה)`; the note under it gives the Law's definition, which governs earlier enactments |
| O1n7 | editorial note: לפי סעיף 1 לחוק הפרשנות, ההגדרה שלהלן תחול גם על ח | note | 83 | content | encoded | il-interpretation-definitions-law, il-interpretation-law; tests: tests-definitions-law 2; tests-law 13. note under "misdemeanour": the Law's definition applies to earlier enactments too |
| O1d42 | ”עונש“, לענין עבירה | definition | 84 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 4. "penalty" |
| O1d43 | ”פרק“ | definition | 85 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 11. "chapter" |
| O1d44 | ”סעיף קטן“ | definition | 86 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 3. "subsection" |
| O1d45 | ”פקודה“ | definition | 87 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 18. "ordinance" |
| O1n8 | editorial note: ההגדרה החלה על חיקוק שניתן לפני תחילת תקפה של פקוד | note | 88 | content | encoded (F36) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 18. note under "ordinance": what the word meant in an enactment given before the Ordinance |
| O1d46 | פשע | definition | 89 | blank: `(בוטלה)` (repealed) | repealed | "felony": the entry reads `(בוטלה)`; the note under it gives the Law's definition, which governs earlier enactments |
| O1n9 | editorial note: לפי סעיף 1 לחוק הפרשנות, ההגדרה שלהלן תחול גם על ח | note | 90 | content | encoded | il-interpretation-definitions-law, il-interpretation-law; tests: tests-definitions-law 2; tests-law 13. note under "felony": the Law's definition applies to earlier enactments too |
| O1d47 | ”צוואה“ | definition | 91 | content | encoded (F36) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 4. "will" |
| O1d48 | ”צוות“ | definition | 92 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 24. "crew" |
| O1d48.1 | (1) of ”צוות“ | paragraph | 93 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 24. a limb of "crew" |
| O1d48.2 | (2) of ”צוות“ | paragraph | 94 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 24. a limb of "crew" |
| O1d49 | ”קונסול“ או ”נציג קונסולרי“ | definition | 95 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 6. "consul" |
| O1d50 | ”קברניט“ | definition | 96 | content | fork (F32) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 16; tests-red-completion 1. "master" |
| O1d51 | ”רופא ממשלתי“ | definition | 97 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 4. "Government doctor" |
| O1d52 | ”רופא מוסמך“ | definition | 98 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 4. "qualified doctor" |
| O1d53 | ”רחוב“ או ”דרך“ | definition | 99 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 19. "street" |
| O1d54 | ”רשום“, לענין מסמך | definition | 100 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 3. "registered" |
| O1d55 | ”רשות מקומית“ | definition | 101 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 9. "local authority" |
| O1d56 | ”שבועה“ | definition | 102 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 5. "oath" |
| O1d57 | ”שוטר“ | definition | 103 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 8. "policeman" |
| O1d58 | ”שופט“, לענין שופטי בית המשפט העליון | definition | 104 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 16. "judge" |
| O1d59 | ”שופט של בית משפט שלום“ | definition | 105 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 2. "magistrates' court judge" |
| O1d60 | ”שכירות“ | definition | 106 | content | encoded (F36) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 4. "lease" |
| O1d61 | ”שנה“ ו”חודש“ | definition | 107 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 3. "year" |
| O1d62 | ”שנת כספים“ | definition | 108 | blank: `(בוטלה)` (repealed) | repealed | "fiscal year": the entry reads `(בוטלה)`; the note under it gives the Law's definition, which governs earlier enactments |
| O1n10 | editorial note: לפי סעיף 3 לחוק הפרשנות, ההגדרה שלהלן תחול גם על ח | note | 109 | content | encoded | il-interpretation-law, il-interpretation-time; tests: tests-law 13; tests-time 1. note under "fiscal year": the Law's definition applies to earlier enactments too |
| O1d63 | ”תחילה“, לענין חיקוק | definition | 110 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 5. "commencement" |
| O1d64 | ”תפישה“, לענין מקרקעין | definition | 111 | content | fork (F28) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 14; tests-red-completion 1. "possession" |
| O1d65 | ”תקנה“ | definition | 112 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 25. "regulation" |
| O1n11 | editorial note: ההגדרה החלה על חיקוק שניתן לפני תחילת תקפה של פקוד | note | 113 | content | encoded (F36) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 25. note under "regulation": what the word meant in an enactment given before the Ordinance |
| O1d66 | ”תקנות סדרי הדין“, לענין כל בית משפט | definition | 114 | content | encoded | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 3. "rules of procedure" |
| O1 | פירושם של מונחים רווחים | section | 30-114 | content | fork (F14, F33, F37) | il-interpretation-definitions-ordinance; tests: tests-definitions-ordinance 232; tests-red-completion 1. the opening words and their reach: the Ordinance's definitions now govern enactments given before the Law |
| O2 | (none) | section | 116-117 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O3 | (none) | section | 119-120 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O4 | (none) | section | 122-123 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O5 | (none) | section | 125-126 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O6 | (none) | section | 128-129 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O7 | (none) | section | 131-132 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O8 | (none) | section | 134-135 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O9 | (none) | section | 137-138 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| Och2 | פרק שני: שמם ותחילת תקפם של חיקוקים | chapter | 140 | content | repealed | a chapter heading that the text marks `(בוטל)` |
| O10 | (none) | section | 142-143 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O11 | (none) | section | 145-146 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| Och3 | פרק שלישי: ביטולים | chapter | 148 | content | repealed | a chapter heading that the text marks `(בוטל)` |
| O12 | (none) | section | 150-151 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O13 | (none) | section | 153-154 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O14 | (none) | section | 156-157 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O15 | (none) | section | 159-160 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| Och4 | פרק רביעי: תקנות | chapter | 162 | content | repealed | a chapter heading that the text marks `(בוטל)` |
| O16.1 | (1) (בוטלה); | subsection | 166 | blank: `(בוטלה)`/`(נמחקה)` (repealed or  | repealed | the subsection reads `(בוטלה)` |
| O16.2 | (2) (נמחקה); | subsection | 167 | blank: `(בוטלה)`/`(נמחקה)` (repealed or  | fork (F15) | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the subsection reads `(נמחקה)` (deleted), but Law s 31 saves it; the consolidation function shows it struck |
| O16.3 | (3) (בוטלה); | subsection | 168 | blank: `(בוטלה)`/`(נמחקה)` (repealed or  | repealed | the subsection reads `(בוטלה)` |
| O16.4 | (4) לא תהא תקנה סותרת הוראותיו של כל חוק; | subsection | 169 | content | encoded | il-interpretation-law; tests: tests-law 4. a regulation may not contradict a law (existing module) |
| O16.5 | (5) (בוטלה). | subsection | 170 | blank: `(בוטלה)`/`(נמחקה)` (repealed or  | repealed | the subsection reads `(בוטלה)` |
| O16 | התקנת תקנות | section | 164-170 | content | encoded | il-interpretation-law; tests: tests-law 4. the stem: where a law gives an authority the power to make regulations, these provisions apply unless another intention is implied |
| O17 | תחילת תקפן של תקנות בנות־<wbr>פעל תחיקתי | section | 172-173 | content | fork (F13) | il-interpretation-repeal, il-interpretation-time; tests: tests-repeal 21; tests-time 2. regulations of legislative effect come into force on the day of publication (existing module) |
| O18 | (none) | section | 175-176 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| Och5 | פרק חמישי: סמכויות | chapter | 178 | content | repealed | a chapter heading that the text marks `(בוטל)` |
| O19 | שימוש בסמכות בין נתינת חוק לתחילת תקפו | section | 180-181 | content | fork (F16) | il-interpretation-law; tests: tests-law 11; tests-red 1. using a power between the giving of an enactment and its commencement (existing module) |
| O20 | (none) | section | 183-184 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O21 | (none) | section | 186-187 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O22 | (none) | section | 189-190 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O23 | (none) | section | 192-193 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O24 | (none) | section | 195-196 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O25 | (none) | section | 198-199 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O26 | (none) | section | 201-202 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O27 | (none) | section | 204-205 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| Och6 | פרק ששי: עבירות ועונשין | chapter | 207 | content | repealed | a chapter heading that the text marks `(בוטל)` |
| O28 | (none) | section | 209-210 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O29 | (none) | section | 212-213 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O30 | (none) | section | 215-216 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O31 | (none) | section | 218-219 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| Och7 | פרק שביעי: שונות | chapter | 221 | content | repealed | a chapter heading that the text marks `(בוטל)` |
| O32 | (none) | section | 223-224 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O33 | (none) | section | 226-227 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O34 | (none) | section | 229-230 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O35 | (none) | section | 232-233 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O36 | (none) | section | 235-236 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O37 | (none) | section | 238-239 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O38 | (none) | section | 241-242 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O39 | (none) | section | 244-245 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O40 | (none) | section | 247-248 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O41 | (none) | section | 250-251 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| O42 | זכויות המדינה שמורות | section | 253-254 | content | encoded | il-interpretation-law; tests: tests-law 4. an enactment derogates from a right of the State or imposes a duty on it only if it says so expressly (existing module) |
| O43 | (none) | section | 256-257 | blank: `(בוטל)` (repealed) | repealed | il-interpretation-law, il-interpretation-repeal; tests: tests-law 12; tests-ordinance-sweep 49; tests-repeal 102. the section reads `(בוטל)`; Law s 31 repeals it (it is not among 16(2), 16(4), 17, 19, 42) |
| Osig | כ״ו בטבת תשי״ד (1 בינואר 1954) | signature | 259-260 | content | inert 1 | the date of the new text and the signatory |

Totals: 226 units: encoded 123, fork 31, inert 1 15, repealed 57.

<!-- COVERAGE:END -->

## 3. Fork register

Each entry gives the readings seen, the one taken, the text that licenses each, and whether it changes an answer.
Entries marked *assumed, not ruled* are this encoding's choices where the text says nothing; they are meant to be reverted alone.
The rejected readings that have a computable answer are asserted, and fail, in `tests-red.l4` (F1 to F25, pass 1) and `tests-red-completion.l4` (F27 to F34, pass 2).
F35 to F38, found in the fix pass, have no assertion in a red file (the number of expected failures stays 26); the answer of F36's rejected reading is the one that mutation 1 of section 5 produces.
F1 to F26 are pass 1's; F27 to F34 were found in pass 2; F35 to F38 in the fix pass.

### F1. Which of s. 10(a) and (b) governs a period of months or years written "from" a day; does it matter?

- **Text.** (a), line 83: "תקופה קצובה במספר **ימים או שבועות** מיום פלוני". (b), line 84: "תקופה קצובה במספר **חדשים או שנים** לאחר אירוע פלוני". Each subsection restricts the unit. The anchor phrases ("from a day", "after an event") differ, but the end rule of (b) is stated by "יום האירוע" (the day of the event), so a day is a fit anchor for (b).
- **Reading taken (R1).** (b) governs every period of months or years, whichever anchor phrase the enactment uses, with the day as the day of the event. The unit decides, so "N days after the day" is (a) in the same way. `s 10 — … months from the day` and `… years from the day` are named aliases of (b), and `… days after the day` and `… weeks after the day` of (a).
- **R2, rejected.** Carry (a)'s exclusion of the start day over to months and years: the period begins the day after D and runs whole months or years. (a)'s words stop at days and weeks, and the reading needs a convention for month-end starts that only (b) supplies.
- **R3, rejected.** "From" includes the day, so three years from 2025-07-16 end on 2028-07-15. Nothing in s. 10 supports it: (a) excludes the start day and (b) puts the end on the day with the event's number. Its answer is asserted, and fails, in `tests-red.l4`.
- **R4, rejected.** Neither governs, so a named refusal. It would leave "three years from the grant", the commonest drafting, without a rule, when (b) reaches months and years by its words.
- **Does it matter?** R1 against R3: yes, by one day in every case.
  R1 against R2: measured with `python3 oracle-s10.py --fork1` over every start day of 2024 and 2025 and N of 1, 2, 6, 12 and 24 months (3,655 cases), under two conventions for an anniversary that does not exist.
  Where the period ends the day before the clamped anniversary, R2 differs from R1 in 63 cases (26 of them where the event is on the last day of a month, such as one month from 2025-02-28: 2025-03-28 under R1, 2025-03-31 under R2).
  Where it ends on the clamped month-end itself, R2 differs in 26 cases, all of that last-day-of-the-month kind.
  Of the brief's six rows in months or years, R2 agrees with R1 on five under either convention; on two years from 2024-02-28 it gives 2026-02-27 under the first convention and 2026-02-28 under the second.
  So the dates on the brief's list do not depend on the choice, except one under one convention; a small, predictable class (month-end starts) does if (a) were imported by analogy.

### F2. Whether s. 10(c) applies to periods in months and years or only to periods in days

- **Text.** (c), line 85: "במנין **ימי תקופה** יבואו גם ימי מנוחה…, זולת אם הם הימים האחרונים שבתקופה". (a) and (b) each name the kind of period they govern ("תקופה קצובה במספר ימים או שבועות", "… חדשים או שנים"); (c) says only "תקופה" and is a subsection of its own.
- **Reading taken.** (c) applies to every period, months and years included: its words are not limited, and every period has last days.
- **Rejected.** (c) applies only to periods in days and weeks, because "במנין ימי" speaks of counting days and a period of months is not counted by days. The words do not say so; they say "the days of a period".
- **Does it matter?** Yes whenever the nominal end of a months or years period falls on a rest day. One month from 2025-01-31, nominal end Friday 2025-02-28, with 28 February, 1 and 2 March as rest days: 2025-03-03 under the reading taken, 2025-02-28 under the other (asserted, and fails, in `tests-red.l4`).
- **Both readings are available.** `s 10(b) — …` alone is the reading without (c) for months and years; `s 10(b), (c) — …` is the reading taken.

### F3. What s. 10(c) does when several days at the end of a period are rest days in a row

- **Text.** "הימים האחרונים" is plural: the last days of the period. The text says what is not counted, not what to do about it, so it does not settle this fork.
- **Reading A, taken: extension.** The period does not end on a rest day. It ends on the first day, from the nominal last day on, that is not one. Rest days inside the period are counted as days of it, as (c) says.
  A is the earliest day on which at least N days have been counted, every rest day inside the period being counted, and on which the period's last day is not a rest day.
  A does not keep the number N exactly: 30 days from 2026-01-01 with Fri 30 and Sat 31 January rest spans 2026-01-02 to 2026-02-01, which is 31 days.
- **Reading B, rejected: replacement.** Each of the nominal last days that is a rest day is "not counted" and is made up by one more day, so two trailing rest days push the end by two. It is coherent as an algorithm (measure "the last days" on the nominal span, skip that trailing run, keep counting). On the same case it ends on 2026-02-02, a 32-day span, so it overshoots further than A, and it needs a step the text does not have (measuring "the last days" on a span that has stopped being the period). That is my reason for preferring A, and it is a preference: the text does not rule B out. (`tests-red.l4`)
- **Reading C, rejected: contraction.** The trailing rest days fall out of the period and it ends on the last day before them (2026-01-30 when 2026-01-31 is a rest day). Also coherent as an algorithm, but it makes a deadline *earlier* because of a rest day and the period shorter than the number fixed, which the text gives no sign of intending. (`tests-red.l4`)
- **Cases that discriminate**, all in `tests-time.l4`: two rest days both inside the nominal period and in a row at its end (A gives 2026-02-01, B 2026-02-02); a one-day period whose only day is a rest day; a two-day period whose two days are both rest days; three in a row; a rest day in the middle; a rest day just before an unaffected last day.
  A and B agree whenever only the nominal last day is a rest day and the next day is not.

### F4. Whether "עד" in s. 8 settles a case a convention would otherwise settle

- **Text.** s. 8, line 77: "הביטוי ”עד...“ לענין זמן או לענין מובאה – משמעו עד ועד בכלל" ("until" in relation to time or a quotation means until and including).
- **Answer.** Yes. The case is whether the closing date of a bound written "until D" is inside it; the Law answers yes, so no convention is needed. `s 8 — the date … is up to and including` is a plain `AT MOST`. It is used by "inside a period", by the fiscal year ("until the thirty-first of December") and by the s. 3 day. The opposite (an exclusive "until") is asserted, and fails, in `tests-red.l4`.
- **What it does not settle.** The start of a bound ("from D"): s. 8 is silent, and s. 10(a) deals with that for periods. And s. 10(a) and (b) do not need it: they say the period "ends" (תסתיים) on a day, so that day is the last day.
- **The quotation sense** ("לענין מובאה"): "sections 3 until 5" includes section 5. Encoded for numbers.

### F5. The closing midnight of a day (s. 3 "יום" read with s. 8)

- **Text.** s. 3, line 43: a day is "תקופה מחצות הלילה **עד** חצות הלילה שלאחריו".
- **Reading taken.** Taken literally with s. 8, the following midnight is inside the day as well as the first moment of the next day, so the instant 00:00:00 belongs to two days. `s 3 — the moment … is within the day` implements this. `s 3 — the day of the moment` still gives every moment one day (the day it is stamped with).
- **Alternative, offered and tested.** The half-open reading, where the closing midnight belongs only to the next day (`… , not counting the closing midnight`). Its assertion against the literal reading is in `tests-red.l4`.
- **Why it hardly matters.** It decides only the single instant of midnight. s. 21's 00:01 for the start of a statute avoids the question for statutes.

### F6. When a period after an event starts (s. 10(b) is silent)

- **Text.** (a) says the day is not counted; (b) says only where the period ends.
- **Reading taken.** The first day of every period is the day after D. (b)'s end rule forces it: a month after an event on 15 January ends on 15 February, so the period is 16 January to 15 February and the event's own day is outside. (If the event's day counted, the period would be a day longer than a month.)
- **Used by** "whether a date falls inside a period".

### F7. A week is seven days *(assumed, not ruled)*

- **Text.** s. 10(a) says "שבועות" (weeks). Neither text defines a week (the only occurrence of the word in either is s. 10(a); "שבועה" is an oath).
- **Reading taken.** N weeks are 7N days: the ordinary meaning. A calendar-week reading (Sunday to Saturday) would need a definition the texts do not have.

### F8. Periods s. 10 does not speak of

- s. 10 deals with periods **from** a day or **after** an event. It says nothing about a period counted **backwards** ("at least 14 days **before**"), "within" a period, or periods in mixed units ("one year and three months"). No function is offered for them; a caller who needs one has no answer from this module, and none is invented.

### F9. A period fixed in a number that is not a positive whole number *(assumed, not ruled)*

- s. 10 speaks of "a fixed period in a number of days, weeks, months or years". The functions refuse (a named refusal, message asserted in the tests) for 0, a negative number or a fraction, instead of computing a date nobody could defend.
- The alternative is to leave the number unchecked. An `EITHER` with a named problem would be the other house-style option; a refusal was taken to keep the functions' types simple.

### F10. The walk of s. 10(c) is bounded at 366 days *(assumed, not ruled)*

- The statute sets no bound. If the supplied calendar names every day in a year a rest day, the answer is a named refusal and not a loop. A real calendar never reaches it (a court recess is about 45 days).

### F11. Days of rest, recess or holiday are one input

- **Text.** "ימי מנוחה, פגרה או שבתון שעל פי חיקוק" (days of rest, recess or holiday under an enactment).
- **Reading taken.** The three kinds are one predicate from DATE to BOOLEAN, supplied by the caller (a function, or a list through `days of rest, recess or holiday listed in`). Which enactment makes a day one (the weekly rest, a court recess, a holiday statute) can differ by context; this encoding cannot know it. The tests use illustrative calendars and say so. The Hebrew calendar is not computed.

### F12. s. 21: "00.01" and the minute before it

- **Text.** s. 21, line 124: "שעת תחילת תקפו של חיקוק היא בשעה 00.01 של יום תחילתו".
- **Reading taken.** 00.01 is one minute past midnight, 00:01:00. A statute binds from 00:01:00 on its commencement day, inclusive. From 00:00:00 to 00:00:59 on that day it does not yet bind, so there is a one-minute gap at the start of its commencement day. The opposite (binding from midnight) is asserted, and fails, in `tests-red.l4`.
- **Another provision.** If the statute fixes a moment of its own, s. 1's gate ("if there is no other provision on the matter") lets it displace the default; the function takes that as a `MAYBE`.

### F13. Ordinance s. 17 read with Law s. 21

- **Text.** Ordinance s. 17, line 173: regulations of legislative effect are published in Reshumot and "their validity begins on the day of their publication, if there is no other provision". Law s. 21: the validity of an enactment begins at 00.01 on its commencement day, and "חיקוק" is a law or a regulation (s. 3).
- **Consequence taken.** Regulations bind from 00:01 on the day of publication, which can be before the moment they were published on that day. The text does not say otherwise. *The encoding states the consequence; whether it is intended is an open question (section 6).*
- **"Another provision"** is a `MAYBE DATE`: the day it fixes. Where another provision exists but fixes no day (for example, on approval by a committee), nothing can be computed until the caller has that day.

### F14. Law s. 1: the gate, and enactments given before the Law

- **Gate.** "If there is no other provision on the matter and if there is nothing in the matter or its context inconsistent with this Law." Both are judgements. They are two inputs of `s 1 — the Law governs`, which a caller consults before relying on any function here; the time functions do not repeat it.
- **Vintage.** s. 3 does not apply to the words of an enactment given before the Law, except חטא, עוון, פשע (named in s. 1), "fiscal year" (s. 3's own text) and, by a note, "coastal waters". For the rest, the definitions of Ordinance s. 1 continue. The Ordinance text defines year and month as Gregorian with **no Hebrew-calendar clause**, and defines **no "day" at all**. So for an enactment given before 1981-10-01, the calendar of year and month is Gregorian whatever the enactment specified, and "the definition that governs the word day" is a named refusal (the text has none to give).
- **The commencement day.** "Given before the commencement" depends on the moment (the Law binds from 00:01 on 1981-10-01 by s. 32 with s. 21). A day-level date settles every day except 1981-10-01, where it is a named refusal; the moment-level function settles that day.
- **Not decided.** Law s. 1 also says the Law applies "even if [the enactments were] given before its commencement". Whether that re-times the commencement of a statute that bound before 1981-10-01 (s. 21's 00:01 for a statute that commenced in 1960) the text does not say. The module computes s. 21 for any commencement day; whether it should is for the caller.

### F15. The Ordinance after s. 31 of the Law

- **Text.** Law s. 31, line 159: the Ordinance, "except ss. 16(2) and (4), 17, 19 and 42", is repealed. The Ordinance text, line 167, shows s. 16(2) as "(נמחקה)" (deleted), and (1), (3), (5) as "(בוטלה)" (repealed); only (4) has content.
- **A possible explanation, not in the text.** s. 16's heading lists amendments up to 5754 (`ordinance.wiki` line 164), after the Law, so 16(2) may have been deleted later and Wikisource's s. 31 not updated. `s 31 — … survives the Law` follows s. 31's words (16(2) survives); the coverage row for Ordinance s. 16 records that the text shows it deleted.
- **Ordinance s. 1** is not in s. 31's list and so is repealed, yet the text carries it with a note that its definitions continue for enactments given before the Law (Law s. 1). It is the one repealed section that still has operative life, and only for those enactments.
- **Fix pass: both readings are now answerable.** Reading A (taken, unchanged): s. 31 lists 16(2), so `s 31 — the Ordinance's section` 16 `, subsection` (JUST 2) is TRUE. Reading B: the consolidation shows 16(2) struck (`(נמחקה)`, `ordinance.wiki` line 167), the amendments in the heading of s. 16 (line 164) run to 5754, and so there is no text to save. `Ordinance consolidation — what the text shows for section` n `, subsection` m says what the consolidation shows (operative text, marked repealed, marked deleted, no such provision), and `s 31 and the consolidation of the Ordinance agree on section` n `, subsection` m is FALSE at 16(2) (saved, shown struck) and at s. 1 (not saved, shown with text), TRUE elsewhere; a question about the whole of s. 16 still refuses. The TRUE at 16(2) was not changed.

### F16. Ordinance s. 19: using a power before the enactment commences

- **Text.** Line 181. A power conferred by an enactment whose commencement is not with its giving may be used, "if no other intention is implied, at any hour after the giving of the enactment, to the extent it appears necessary or proper to operate the enactment on its commencement day"; what was done under it has "no validity **until** the day of commencement" unless another intention is implied or it was needed to operate the enactment.
- **Reading taken, "until".** Validity begins **on** the commencement day. Read with s. 8 ("until" includes the day), nothing done under the power would be valid on the day the enactment first binds, which defeats the section's own purpose of operating the enactment on that day; Law s. 1's context exception is taken to switch s. 8 off here. The literal reading's answer (valid from the day after) is asserted, and fails, in `tests-red.l4`.
- **"At any hour after its giving."** The functions work in days, so the day of giving is included (the use is taken to follow the giving within the day). The permission is modelled as the window from the day of giving up to, not including, the commencement day; from the commencement day the power is the ordinary power and s. 19 gives no permission and no prohibition, so `s 19 permits …` answers FALSE there. FALSE means "s. 19 does not itself permit it", not "forbidden".

### F17. Law s. 20: "רובם"

- A majority is more than half: 3 of 5, 3 of 4 and 2 of 3 are, 2 of 4 is not. Two of four as "their majority" is asserted, and fails, in `tests-red.l4`. Numbers that cannot describe an act done by some of the people it was imposed on (more actors than persons, none imposed, fractions) are a named refusal.

### F18. Law s. 22(2): "a previous act"

- Measured against the moment the repeal binds (00:01 on its commencement day, by s. 21): an act at 00:00:30 on that day is earlier, an act at 00:01:00 is not. Limbs (1) and (3) are propositions about the substance of the repealed law; pass 1 carried them as text and pass 2 encodes them in `il-interpretation-repeal.l4` (F31 for the boundary of limb (1)).

### F19. Law s. 23: replacement provisions

- Modelled as one boolean the caller supplies: whether the repealing enactment "provides provisions in place of the repealed ones". Whether it does is a reading of that enactment. The result is two named outcomes (lapse, or stand until cancelled under the repealing enactment).

### F20. Law ss. 24 and 26: judgement inputs

- s. 24 (the binding text): two booleans, whether the enactment was given in English before the State and whether a new text was fixed under s. 16 of the Law and Administration Ordinance (a statute outside the sources). s. 26 (deviation from a form): three judgements, "slight", "harms the essential", "misleads", read as a conjunction (slight and neither of the others) because the relative clause "שאין בה כדי לפגוע בעיקר או להטעות" restricts the slight deviation. The encoding states the test and takes the judgements as inputs.

### F21. Law s. 33

- "Within thirty days **from** the day of its adoption": s. 10(a), days, so the last day is the day thirty days on (1981-06-19 for the adoption on 1981-05-20 that the text records). s. 10(c) is not applied: whether a duty to publish is a "period" whose last day can move is not said; a caller can compose it.
- **Stated limit (S163).** `s 33 — the last day for publishing a law adopted by the Knesset on` takes no calendar of rest days, so it answers 1981-06-19 (a Friday) whatever the calendar is.
  If s. 10(c) applies to the duty and Friday and Saturday are rest days, the last day is 1981-06-21 (a Sunday); the module does not compute that, and F11 makes the calendar an input of s. 10(c) itself.
  Whether s. 10(c) applies to the duty is the open question above, so the limit and the fork are the same one.

### F22. Law s. 3: two ends, two calendars

- "If the beginning of their period **or** its end was specified by the Hebrew calendar only, by the Hebrew calendar." Either end triggers it, so a period whose beginning is Hebrew-only and whose end is Gregorian-only is Hebrew by the words. The text does not consider that mixed case.

### F23. Oddities in the unofficial text

- Line 84 reads "בחדשה האחרון", where "בחדש האחרון" (in the last month) is meant; the stray ה is in the Wikisource text and does not change the meaning. Only the official text can say.
- The note under the "coastal waters" definition in the Ordinance (`ordinance.wiki` lines 67-68) gives the width as "twelve miles" where the Law's s. 3 (line 47) says "twelve nautical miles". The two texts disagree; not a time question, recorded because it was found.
- The adoption date used for s. 33 is from the signature line after s. 33 (`law.wiki` line 167), which is not part of the section.

### F24. A year is twelve months

- s. 10(b) names years and months in one rule. N years are taken as 12N months from the event, which gives the same day number in the year N later (and the last day of February where the month lacks the 29th). The Law does not define the length of a year in months.

### F25. What (b) does when the month lacks the day

- **Text.** (b), line 84: "ואם היה החודש חסר אותו יום – ביום האחרון של החודש" ("if the month lacks that day, on the last day of the month").
- **Reading taken.** The last day of the month, as written: one month from 2025-01-31 ends 2025-02-28; one year from 2024-02-29 ends 2025-02-28.
- **Rejected, and a hazard rather than a reading.** Rolling forward into the next month (3 March, 1 March), which is what the lenient `Date` constructor of `daydate` does. The text says otherwise, so the encoding computes (b) from its words and does not use `Date`; both rolled answers are asserted, and fail, in `tests-red.l4`.
- **`daydate`'s own `add months` and `add years`** clamp to the last day of the month. They were measured against the statute on 143 cases (118 month cases: every 29th, 30th and 31st start of 2024 and 2025, for 1 and 12 months; and 25 year cases: five start days, 29 February 2024 among them, for 1 to 5 years): they agree in every one. The statute governs; the agreement is asserted in `tests-sweep.l4`, so a library change that broke it would show.

### F26. A statute that fixes no commencement day

- **Text.** s. 21 gives the hour (00.01) of "the day of its commencement" and nothing about which day that is. Chapter 2 of the Ordinance, "the name and commencement of enactments" (ss. 10 and 11), reads "(בוטל)" (`ordinance.wiki` lines 140 to 147). Ordinance s. 17 gives a day for regulations of legislative effect only.
- **Reading taken.** The sources give **no default commencement day for a law that fixes none**. "The day from which a statute binds" is therefore an input to `s 21 — …`, and nothing here supplies it; the encoding does not invent a default (a day of publication, for instance, which is what s. 17 says for regulations only).

### F27. "Immovables" (Law s. 3; Ordinance s. 1): what "except detachable fixtures" qualifies

- **Text.** Law s. 3 "מקרקעין", `law.wiki` line 49: land, everything built on it and planted in it, and anything else attached to it permanently, except detachable fixtures. Ordinance s. 1 "מקרקעין", `ordinance.wiki` line 75, has the same list in the same order.
- **Reading taken (A).** The exception qualifies the last limb only ("anything else attached to it permanently"). A building or a tree is immovable whether or not it could be detached. This is where the exception stands in the text: it follows the last limb with nothing between.
- **Reading rejected (B).** The exception reaches every limb, so a detachable thing built on or planted in the ground is not immovable.
- **Where it matters.** A detachable cabin standing on the ground: immovable under A, movable under B (and then "movables" says the opposite as well).
- **Rules.** `s 3 "immovables" — the thing is immovable:` (A) and `... if the exception for detachable fixtures reaches every limb:` (B); the Ordinance's two rules call them. The rejected reading's answer is asserted, and fails, twice in `tests-red-completion.l4`.

### F28. "Possession" (Law s. 3; Ordinance s. 1): what the two exclusions exclude

- **Text.** Law s. 3 "תפישה" in relation to immovables, `law.wiki` line 60: includes use, possession or enjoyment *not merely as an employee or official, or merely for supervision or guarding*. Ordinance s. 1, `ordinance.wiki` line 111: the same, with "residence" added to the list and the exclusions joined with "and" where the Law has "or".
- **Reading taken (A).** Neither exclusion may hold: use only as an employee or official is not possession, and use only for supervision or guarding is not possession.
- **Reading rejected (B).** "Or merely for supervision or guarding" is a further limb of what is included: guarding alone is possession.
- **Where it matters.** A holding that is use for guarding only.
- **Rules.** `s 3 "possession" — the holding of land is possession:` (A), with (B) as `... if supervision or guarding is a limb of what is included:`; `Ordinance s 1 "possession" — the holding of land is possession:` (A). Two failing assertions in `tests-red-completion.l4`.
- **The Ordinance's "and" makes (A) the plainer reading there, and the Law's "or" is the harder text.** The Ordinance has no (B) rule of its own.

### F29. "Coastal waters" (Law s. 3; Ordinance s. 1, note): miles, and the outer edge

- **Text.** Law s. 3 "מימי חופין", `law.wiki` line 47: a strip of open sea along the State's coast, twelve **nautical** miles wide from the low-water point on the shore. The Ordinance's note under its repealed entry, `ordinance.wiki` line 68: the same strip, twelve **miles** wide.
- **(a) Which miles. Reading taken (A):** both texts name one strip, and the Ordinance's note is read as the Law's, in nautical miles; the Law's note (line 48) says the Law's definition reaches earlier enactments (by s. 1(b) of the Coastal Waters Law). **Reading rejected (B):** the note's "miles" are statute miles (1,609.344 m against 1,852 m), which needs a conversion that is not in the sources. The two differ for points between 10.43 and 12 nautical miles out.
- **(b) The edge. Reading taken (A):** a point exactly twelve nautical miles out is inside ("at most 12"). **Reading rejected (B):** a strip "of a width of twelve miles" stops short of the edge.
- **Rules.** `s 3 "coastal waters" — the point is within the coastal waters:`; `Ordinance s 1 "coastal waters" — the note's strip, read as the Law's twelve nautical miles:` (A) and `... read literally as twelve statute miles:` (B). Two failing assertions in `tests-red-completion.l4`.
- **See also** F23 (the oddity is recorded there as found in pass 1).

### F30. "A number of" (מספר): Law s. 16 and s. 20

- **Text.** s. 16, `law.wiki` line 106: a power to appoint "a body of a number of members" includes appointing a chairman and an alternate for each member. s. 20, line 119: "an act imposed on a number of persons" is valid if done by most of them. The same word in both.
- **Reading taken for s. 16 (A).** At least two members. A body of one is not "a body of a number of members".
- **Reading taken for s. 20 in pass 1 (not edited).** At least one: `tests-law.l4` asserts that an act imposed on one person and done by that one is valid.
- **The two passes disagree about one word.** I did not edit pass 1 (the brief allows an edit only to fix a defect shown against the text, and this is a choice of reading). The rejected reading for s. 16 (one member) and the pass-2 reading for s. 20 (one person is not within the section: a refusal) are asserted, and fail, in `tests-red-completion.l4`. A domain expert should choose one reading for both.
- **A second input in s. 16.** Whether the chairman is one of the members decides whether "an alternate for the chairman" is covered ("an alternate for each member"); it is a plain input, `the chairman is one of the members`.

### F31. Day-level boundaries of ss. 22(1) and 25

- **Text.** s. 25, line 139: a reference to an enactment is to it as worded "when it is resorted to", with provisions added and, if replaced, the provisions that took its place. s. 22(1), line 127: a repeal cannot revive what had no validity "at the hour the repeal took effect".
- **Reading taken (A).** A version "in force from" a day applies on that day itself; provisions that took the enactment's place apply from their day. A thing valid until the very moment of the repeal still had validity at that hour (s. 8: "until" includes its end).
- **Reading rejected (B).** The day a version takes over belongs to the old one; a thing whose validity ended at the repeal's moment did not have validity at it.
- **Where it matters.** On 2010-01-01 with versions in force from 2000 and from 2010 (the 2010 wording under A); a rule that stopped at 00:01:00 on the commencement day (valid at the hour under A).
- **Rules.** `s 25 — the wording in force on` day `among` versions; `s 22(1) — the thing had validity at the hour a repeal commencing on` d `took effect:` thing. Two failing assertions in `tests-red-completion.l4`.

### F32. "Master" (קברניט): how far the exclusion reaches

- **Text.** Ordinance s. 1, `ordinance.wiki` line 96: whoever has control of a ship or vessel, or whoever is appointed over it at that time, "to take out" (`להוציא`, here "excluding", as in "excluding a pilot and a harbour master") a navigator and a harbour master.
- **Reading taken (A).** The exclusion closes the whole sentence: a navigator or harbour master is not the master even if in control.
- **Reading rejected (B).** The exclusion belongs to the second limb only: whoever has control is the master.
- **Where it matters.** A navigator who has control of the ship at that time.
- **Rules.** `Ordinance s 1 "master" — the person is the master:` (A) and `... if the exclusion belongs to the second limb only:` (B). One failing assertion in `tests-red-completion.l4`.
- **The gloss is mine.** The reading of `להוציא` as "excluding" rests on the sense of the clause; the word is not defined in the sources.

### F33. Which enactments Ordinance s. 1 reaches, and whether Law s. 1's gate applies to it

- **Text.** Ordinance s. 1, line 32: the entries bear their meanings in this Ordinance, in every enactment in force today and in every enactment given "hereafter". Law s. 31 repeals the Ordinance except ss. 16(2), 16(4), 17, 19 and 42 (s. 1 is not saved). The note before the entries (line 31) and the note at the head of the Ordinance (line 12) say that, by Law ss. 1 and 3 and s. 1(b) of the Coastal Waters Law, the Ordinance's definitions apply to words in enactments given **before the Law**, except five (`חטא`, `עוון`, `פשע`, `שנת כספים`, `מימי חופין`), and Law s. 1 (line 22) says the same.
- **Reading taken (A).** The Ordinance's definitions govern the words of an enactment given before the Law (before 00:01 on 1981-10-01), except the five; they govern no word of a later enactment. For a later enactment the sources give no definition of "person", "ship", "house" and the rest: `FALSE` from the dispatcher means "this section does not govern", not "the thing is not a person".
- **Reading rejected (B).** The opening words' "hereafter" still reaches later enactments for words that Law s. 3 does not define.
- **The Law's gate is not applied to the Ordinance's definitions.** Ordinance s. 1 has no "unless the context otherwise requires", and Law s. 1's second limb says the Ordinance's definitions *continue* to apply. A caller who wants the gate composes it: `under s 1, the Law's answer for` ...
- **Rules.** `Ordinance s 1 — the Ordinance's definitions govern` entry `in an enactment given on` d (and `... given at` moment). One failing assertion in `tests-red-completion.l4`.

### F34. Qualifiers inside entries: "seaman" and "in writing"

- **(a) "Seaman" (יורד ים), `ordinance.wiki` line 55.** "Includes any person working on a ship or employed on it in any capacity, except the master, a navigator, and an apprentice bound by a contract and properly registered." **Taken (A):** the exceptions limit what the word is extended to; a person who is a seaman in the ordinary sense stays one. **Rejected (B):** they remove even that person.
- **(b) "In writing" (בכתב), line 41.** "Includes print, lithography, typewriting, photography and every other way of presenting words or numerals, or copying them, in a form visible to the eye." **Taken (A):** "in a form visible to the eye" governs the whole list. **Rejected (B):** it qualifies only the last item ("every other way"), so print that is not visible is still in writing.
- **Rules.** `Ordinance s 1 "seaman" — the person is a seaman:`; `Ordinance s 1 "in writing" — the presentation counts as writing:`. Two failing assertions in `tests-red-completion.l4`.

### F35. Law s. 21 and the Law's own commencement (s. 32)

- **Text.** s. 32, line 162: "תחילתו של חוק זה ביום ג׳ בתשרי התשמ״ב (1 באוקטובר 1981)". s. 21, line 124: "שעת תחילת תקפו של חיקוק היא בשעה 00.01 של יום תחילתו". s. 1, line 22: the Law applies to every enactment "even if given before its commencement".
- **Taken (A).** s. 21 applies to the Law itself, so the Law binds from 00:01:00 on 1981-10-01 (`s 32, s 21 — the moment the Interpretation Law began to bind`); `s 1 — it was before the Law commenced that an enactment was given at` m rests on it. The reading is pass 1's; the fix pass registered it as a fork.
- **Rejected (B).** s. 21 does not reach the Law's own commencement (the Law cannot give itself an hour before it binds, and s. 32 gives the day alone). The text would then fix no hour for the Law's own commencement, and a moment-level question on 1981-10-01 would have no answer from the text.
- *Assumed, not ruled.* Not asserted in a red file.

### F36. An open ("includes") entry and a thing it does not list

- **Text.** Ordinance entries that say `לרבות` or `כוללות` and that the module holds as an enumeration with a catch-all constructor: "repeal" (line 36), "law" (42), "sale" (69), "will" (91), "lease" (106), and the notes under "ordinance" (88) and "regulation" (113). The other open entries ("person", "house", "in writing", "declaration on oath" and "oath", "signature", "seaman", "Israel", "public servant", "street", "possession", and "statute" and "regulation", which have a defined core) are held as records, each with a field for the ordinary or defined core that the caller must give (`a person in the ordinary sense`; for "statute", `a legislative act of the Knesset`; for "regulation", the flags of `An instrument under the Ordinance`), so they never answered for a thing nobody had settled.
  Checked by a census of every line with `לרבות` or `כוללות` in the staged texts: Ordinance lines 33, 36, 37, 41, 42, 47, 48, 53, 55, 57, 69, 74, 77, 81, 88, 91, 99, 102, 106, 111, 112 and 113, and Law lines 31, 37, 60 and 139.
  Each is in one of the two groups above, or is "Inspector General of Police" or "Commissioner of Prisons" (74, 77; below), or is Law s. 25 (139), which is a rule of reading and not an entry and is held as a record of the two things a reference reaches. The Law's entry for "law" (line 32) says `כל אחד מאלה` ("each of these") and not `לרבות`: it is closed.
- **Taken (A).** An open entry puts its listed members in and keeps nothing out, so a thing it does not list is neither in nor out: the rule refuses, and the caller settles it by choosing the constructor for a thing that is within the ordinary meaning (`anything that is law in its ordinary sense`) or for one that is not (`something that is not law in its ordinary sense`). The closed Law entry answers FALSE for `any other source`.
- **Rejected (B).** An unlisted thing in an open entry is FALSE (the module's first reading), which answered FALSE for an Israeli Supreme Court precedent as a source of law. Mutation 1 of section 5 reinstates it.
- **"Determined" (line 78).** "נקבע בחוק שבו מצויה מלה זו או בתקנות שניתנו לפיו": a regulation that itself uses the word is neither the law in which the word appears nor regulations made under it, so `in the regulation in which the word appears` refuses; `somewhere else` stays FALSE. The Law's entry (line 51, `בחיקוק`) is unchanged.
- **Left as FALSE.** "Inspector General of Police" and "Commissioner of Prisons": the first constructor is the post and `anyone else` is outside it.
- *Assumed, not ruled.*

### F37. Which instruments the Law and the Ordinance reach, and s. 25 for an administrative direction

- **Text.** Law s. 1, line 22: the Law applies "לגבי כל חיקוק והוראת מינהל, אף אם ניתנו לפני תחילתו". Ordinance line 31 (its note): the definitions apply to words in enactments and administrative directions given before the Law; line 32 (the opening words) speaks of enactments. Law s. 25, line 139: "אזכור של חיקוק בחיקוק אחר".
- **Taken.** Sections 2 and 4 to 26 reach every enactment and administrative direction whatever its date (`s 1 — section` n `of the Law reaches ...`); section 3 refuses for an earlier enactment, because its reach turns on the word (pass 1's `s 1 — section 3 applies to`); a private contract and any other document are not named, so FALSE. The Ordinance's definitions follow the same kinds, and the date as before (F33). s. 25: a reference made in an enactment is within it, one made in a private contract or other document is not, and one made in an administrative direction refuses, because s. 25 says "in another enactment" and s. 1 applies the Law to directions without saying whether that enlarges s. 25.
- **Rejected.** For the administrative direction in s. 25: TRUE (s. 1 applies the Law wholesale) or FALSE (s. 25's own words).
- *Assumed, not ruled.*

### F38. Law s. 26: a deviation that is not saved

- **Text.** Line 142: "טופס שנקבע בחיקוק – סטיה קלה ממנו, שאין בה כדי לפגוע בעיקר או להטעות, אינה פוסלת את הנעשה לפיו".
- **Taken (A).** The text says that a slight deviation that neither harms the essential nor misleads does not disqualify what was done under the form (the rule answers FALSE); for a deviation that is not slight, or harms the essential, or misleads, it says nothing, so the rule refuses.
- **Rejected (B).** Any other deviation disqualifies (TRUE). Pass 1 took B; the independent test pass found that the rule's name went a step beyond the text. The edit is logged in `## Changes to existing modules`.
- *Assumed, not ruled.*

### Scenario codes from the independent test pass: where each lands

| code | what it asked | where it lands |
| --- | --- | --- |
| S013 | an enactment given on the Law's commencement day | F14: the day-level functions refuse; the moment-level ones settle it. Kept. |
| S163 | whether Friday is a statutory rest day, and s. 10(c) at `s 33` | F11 and F2. `s 33 — the last day for publishing a law adopted by the Knesset on` applies s. 10(a) alone and has no rest-day calendar (F21); this is a stated limit, and a caller who has a calendar composes s. 10(c). |
| S187, S201, S202 | s. 10(c) for periods in months or years; "months from a day" as s. 10(b) "after an event" | F2 (c reaches months and years) and F1 (a or b). Both functions exist: `s 10(b) — …` alone, and `s 10(b), (c) — …`. |
| S211 | whether s. 21 applies to the Law's own commencement | F35 |
| S291, S292 | s. 26 for a deviation that is not slight | F38 |
| S303 | Ordinance s. 16(2): saved by Law s. 31, shown struck by the consolidation | F15 (both readings answerable now) |
| S373, S485 | an unlisted source in the open "law"; a regulation that uses "determined" | F36 |
| no code | exceptions inside the `לרבות` definitions: "seaman" (55), "master" (96), "possession" (Law 60, Ordinance 111), "immovables" | F34 (seaman), F32 (master), F28 (possession), F27 (immovables) |
| no code | whether Ordinance s. 1 reaches an enactment given after the Law | F33 |
| no code | the unit of the coastal strip | F29 |
| no code | using a power before the enactment commences (Ordinance s. 19) | F16 |
| no code | how long a week is | F7 (seven days) |
| no code | the meaning of `רובם` in Law s. 20 | F17 (more than half) |
| S014, S015, S021, S016, S017, S018, S289, S643 | the Law's reach by date and by kind of instrument; s. 25 for a contract or a direction | implemented: F37 |
| S065, S066, S067 | the source of the meaning of חטא, עוון, פשע | implemented: `s 3 — where the meaning of the entry is found:` (the Penal Law, 5737-1977) |
| S231, S232 | s. 13(b) for a designation by name alone, or by name and office | implemented: `s 13(b) — the person bound on` d `by a designation that names` ... |
| S269 | s. 20 where the enactment requires all to act | implemented: `s 20 — where the enactment's requirement that all act is` ... |
| S591, S599, S600, S601 | Ordinance s. 17: the duty to publish in Reshumot; an administrative instruction; a regulation never published; publication in a newspaper only | implemented: `Ordinance s 17 — the regulation must be published in Reshumot:` and `Ordinance s 17 — the validity of the regulation has begun by` |
| S554 | a president of a magistrates' court and "judge" | implemented: outside the extension (FALSE) |
| S188 | one month after 1 Nisan 5780 | declined: no Hebrew-date type; Hebrew-calendar arithmetic is a named refusal by design (section 1) |
| S218 | the number of days "due speed" means | declined: the text states no number, and "due speed" is a judgement input |
| S635 | which days are statutory rest days | declined: an input by design (F11) |
| S321 | the Ordinance text is dated 1954-01-01 | declined: not a value; the signature date is not the date of publication (finding 4) |
| S638 | schedule or table rows | declined: the texts have none |
| S631, S632, S633, S634, S636 | deemed service, registered mail, a period counted backwards, hours, business days | declined: the texts are silent, and a function with no text behind it would invent a rule (F8 for backwards) |
| S637 | a foreign State as an "אדם" | declined: Law s. 4 names no such case, and the subject type has none |
| S639 | the text of the definition of "פשע" | declined: not a value; the Penal Law is not among the sources |
| S641 | a quorum for an act done by a majority | declined: s. 20 states none |

### Where I looked and found nothing further

- Ss. 2, 4, 5, 6, 7, 9: read for any input that could change the answer other than the s. 1 gate; none. Ss. 11 to 19: read for a number or a date; s. 11 has an open standard ("the proper speed") and no number; ss. 12 to 18 only list what a grant of power includes. s. 25 (references): the text points at the version in force when the reference is resorted to, which is a way of evaluating, not a function.
- s. 10: read for the forks the brief names, for the position of "from" and "after", for any treatment of weeks, backward counting, "within", and time of day; found F1 to F3, F6, F7, F8 and F25 and nothing else.
- Ordinance ss. 2 to 15, 18, 20 to 41, 43: each reads "(בוטל)" and nothing more.
- Pass 2, Ordinance s. 1: each of the 66 entries read for a proviso that points at an earlier meaning, a pointer to another Act, an "includes" (which needs an ordinary-meaning input), an exclusion, a number or a date; found F27, F28, F29, F32, F33, F34, the provisos (finding 3) and the missing dates (finding 4).
- Pass 2, Law ss. 2, 4 to 7, 9, 11 to 19, 22, 25 and the 23 entries of s. 3: read for the same; found F27 to F31.
- Fix pass: every field and constructor name in the six pass-2 modules swept by script for a list of alternatives, each hit decided against the Hebrew (section 1); the open entries of both texts read for an unlisted thing (F36); the sections s. 31 saves read against the consolidation (F15). Found F35 to F38.

## 4. Answer table for the worked cases

Each row was run as `s 10 — … from the day` (or `s 10(a) — …`) and as the composed `s 10(…), (c) — …` with three calendars of rest days supplied by `tests-worked-cases.l4`: none, Saturdays, and Fridays and Saturdays.
The two calendars are illustrations and not a statement of any country's calendar.
The "no rest days" column is the answer of the statute with no rest-day input, and is what an encoding that has no calendar should use.

| period | counted from | section | no rest days | Saturdays rest | Fridays and Saturdays rest |
| --- | --- | --- | --- | --- | --- |
| three years | the day 2025-07-16 | s. 10(b) | 2028-07-16 (Sun) | 2028-07-16 | 2028-07-16 |
| five years | the day 2025-01-15 | s. 10(b) | 2030-01-15 (Tue) | 2030-01-15 | 2030-01-15 |
| five years | the day 2025-09-01 | s. 10(b) | 2030-09-01 (Sun) | 2030-09-01 | 2030-09-01 |
| thirty days | the day 2026-01-01 | s. 10(a), (c) | 2026-01-31 (Sat) | 2026-02-01 | 2026-02-01 |
| two years | the day 2024-02-28 | s. 10(b), (c) | 2026-02-28 (Sat) | 2026-03-01 | 2026-03-01 |
| one year | the day 2024-02-29 | s. 10(b), (c): February 2025 lacks the 29th | 2025-02-28 (Fri) | 2025-02-28 | 2025-03-02 |
| one month | the day 2025-01-31 | s. 10(b), (c): February 2025 lacks the 31st | 2025-02-28 (Fri) | 2025-02-28 | 2025-03-02 |

All 21 expectations in this table pass in `tests-worked-cases.l4`, and its seven `#EVAL`s print the "no rest days" column.
The last two rows in the final column are the two-in-a-row case: Friday 28 February and Saturday 1 March are both rest days, so the period ends on Sunday 2 March.

Other results the tests pin (section citation in the test file): the Law binds from 00:01 on 1981-10-01 (s. 32, s. 21); the last day for publishing the Law was 1981-06-19 (s. 33, s. 10(a)); regulations published on 2026-05-14 come into force on 2026-05-14, from 00:01 (Ordinance s. 17, Law s. 21); fiscal year 2026 runs 2026-01-01 to 2026-12-31 (s. 3).

## 5. What `check.sh` prints, and which failures are expected

`check.sh` is the skill's script plus three checks of its own: every module has an ASCII filename, `l4 check` prints no stray-`@ref` warning, and `srcrefs.py check --refs` finds no problem in any quotation or locator.
It reads the diagnostics, not the exit code: `l4 run` exits 0 when an `#ASSERT` fails.
The run recorded here is the fix pass's, with the binary named in section 0, run as `L4=<binary> L4_TARGET=unstable ./check.sh`; it exits 0.

```text
module                                    errors satisfied  failed  refused  expected
il-interpretation-carried-text.l4              0         0       0        0         0
il-interpretation-definitions-law.l4           0         0       0        0         0
il-interpretation-definitions-ordinance.l4       0         0       0        0         0
il-interpretation-gate.l4                      0         0       0        0         0
il-interpretation-law.l4                       0         0       0        0         0
il-interpretation-powers.l4                    0         0       0        0         0
il-interpretation-reading.l4                   0         0       0        0         0
il-interpretation-repeal.l4                    0         0       0        0         0
il-interpretation-time.l4                      0         0       0        0         0
tests-definitions-law.l4                       0       235       0        0         0
tests-definitions-ordinance.l4                 0       801       0        0         0
tests-law.l4                                   0       116       0        0         0
tests-ordinance-sweep.l4                       0        49       0        0         0
tests-powers.l4                                0       116       0        0         0
tests-reading.l4                               0       130       0        0         0
tests-red-completion.l4                       14         0      14        0        14
tests-red.l4                                  12         0      12        0        12
tests-repeal.l4                                0       139       0        0         0
tests-sweep.l4                                 0       314       0        0         0
tests-time.l4                                  0       182       0        0         0
tests-worked-cases.l4                          0        21       0        0         0
TOTAL (21 modules)                            26      2103      26        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)

extra checks
  all modules have ASCII filenames
  l4 check: no stray @ref warnings
  srcrefs: srcrefs check: 502 src: lines, 260 runs, 354 locators, 0 problems
```

**The baseline it replaced** (pass 1, before any change in pass 2, recorded in `PROGRESS.md`): 8 modules, 630 assertions satisfied (113 in `tests-law.l4`, 314 in `tests-sweep.l4`, 182 in `tests-time.l4`, 21 in `tests-worked-cases.l4`), 12 failed and expected in `tests-red.l4`, 0 refused, srcrefs 232 `src:` lines, 137 runs, 193 locators, 0 problems.
Every one of those numbers still holds except one that moved on purpose: `tests-law.l4` now gives 116, not 113 (the four s. 26 assertions that said TRUE now assert the refusal, and three combinations were added), so the old test files give 116 + 314 + 182 + 21 = 633 satisfied and 12 expected failures.
Pass 2 added 13 files (6 modules and 7 test files) and 14 expected failures; the fix pass brought the six pass-2 test files from 1,024 satisfied to 1,470 (130 + 116 + 139 + 235 + 801 + 49); together with the 633, the 2,103 above.
There are no warnings on any file (checked by counting `DiagnosticSeverity_Warning` per file), no refused assertion, and no assertion left unevaluated.

**The 26 failed assertions are expected.**
`tests-red.l4` (12, pass 1): F1 (R3, two), F25 (two), F3 (readings B and C, two), F2, F5, F12, F4, F16 and F17 (one each).
`tests-red-completion.l4` (14, pass 2): F27 (two), F28 (two), F29 (two), F30 (two), F31 (two), F32, F33, and F34 (two).
Each asserts the answer of a reading that section 3 considered and rejected, so each must fail while the encoding takes the other reading; 13 fail with `assertion failed` and one (F30, s. 20) with `assertion failed: expected a refusal, but the expression produced a value`.
`check.sh` lists the counts (`expected_failed`), and `encoding.json` names the files (`expected_red`).
The files double as proof that this harness can fail.

**Mutations (pass 1, recorded as found).**
Deliberate mutations were each caught by the tests in a scratch copy of the modules: counting the start day in s. 10(a) (56 failures), walking the end of (c) backwards (21), making s. 8 exclusive for dates (10), binding from midnight in s. 21 (9), ending a short month on the 28th in (b) (14), ignoring another provision in Ordinance s. 17 (2); and, in the law module, the s. 20 threshold (2), the s. 31 list (1), the s. 1 gate (2) and the s. 22(2) comparison (1).
**Mutations (pass 2).**
Six deliberate mutations of `il-interpretation-definitions-ordinance.l4`, each in a scratch copy of the folder (since removed), were each caught by `tests-definitions-ordinance.l4`, which gave 650 satisfied and 0 failed on the unmutated copy (at the end of pass 2; 801 satisfied now): dropping the exclusion of a navigator in "master" (3 failures), making the dispatcher govern the repealed entry "sin" (3), dropping the master from the exceptions to "seaman" (1), accepting any day for the Mandate (1), requiring that a house be dwelt in even if only intended for dwelling (2), and letting "enactment" answer in an earlier enactment instead of refusing (2).
The other pass-2 modules (`-gate`, `-reading`, `-powers`, `-repeal`, `-definitions-law`) were not mutated in pass 2: their 325 assertions then (49 + 87 + 16 + 173) were tested for the ability to fail only through the 14 expected failures, which fail on 14 rules (one for each rejected reading).

**Mutations (fix pass).**
Ten deliberate mutations of the code added in the fix pass, each in a scratch copy of the folder (since removed), each run with `L4_BIN` against the test file for that module, were each caught; the number of failing assertions is in brackets.
1. The open "law" answers FALSE for `any other source` again (2).
2. "Street" without "a promenade" (1).
3. Law s. 26 answers TRUE for a deviation that is not saved (7).
4. The consolidation shows 16(2) as operative text (3).
5. "Administrative direction" without "a permit" (1).
6. s. 13(b) answers a designation by name and office as if it named a person (1).
7. The reach of section 3 for an earlier enactment answers TRUE (1).
8. Ordinance s. 17 begins validity the day after publication (2).
9. "Determined" answers TRUE for a regulation that uses the word (1).
10. s. 20 ignores the requirement that all act (5).
The unmutated copy gave 801 satisfied in `tests-definitions-ordinance.l4` and nothing failed.
The rest of the code added in the fix pass (the other list members, the fields of the extended records, `s 3 — where the meaning of the entry is found:`, the `in an instrument of the kind` rules of the Ordinance and of s. 25, the field for publication some other way) has not been mutated.

**Run these too.**
`python3 -I gen-coverage.py --check` (every unit has one disposition; every `encoded` or `fork` row names a rule a module defines and an assertion that calls it; every fork a row cites is a heading in section 3) must print `226 units, 0 problems`.
`python3 -I inventory.py` prints the unit count and its ids from the wikitext.

## 6. Open questions for a domain expert

1. **Is F3's reading A (extension) right, and does (c) reach months and years (F2)?** These are the two answers a lawyer will notice first. The text does not settle F3 (it separates A from B only when two or more rest days end the nominal period), and the preference for A is mine; the brief asked for the reading from the text alone, and case law may differ.
2. **Which enactment makes a day a day of rest, recess or holiday** for a given period (F11)? The module takes it as an input and cannot choose.
3. **Ordinance s. 17 with Law s. 21 (F13):** do regulations bind from 00:01 on the day of publication, before they were published? Is there anything that says otherwise?
4. **Ordinance s. 19 and s. 8 (F16):** does "until the day of commencement" include that day? The encoding takes validity from the commencement day.
5. **Pre-1981 enactments (F14):** the Ordinance defines no "day", and s. 1 of the Law switches off s. 3 for those enactments; what defines a day for them? Does s. 21's 00:01 apply to a statute that commenced before the Law?
6. **Ordinance s. 16(2) (F15):** the Law's s. 31 saves it and the text shows it deleted; which is current?
7. **Midnight (F5):** does the closing midnight of a day belong to both days under s. 8, or only to the next?
8. **The official texts.** Everything here rests on unofficial Wikisource copies: the typo in s. 10(b) (F23) and the Wikisource notes the encoding leans on ("coastal waters" in s. 3; the Ordinance's s. 1 note) need checking against the gazette.
9. **A week (F7), "their majority" (F17), "provisions in their place" (F19):** are the ordinary meanings what the courts apply?
10. **Periods s. 10 does not speak of (F8):** what governs a period counted backwards, or "within N days of"? Is s. 10(a)'s exclusion of the start day applied to them in practice?
11. **Which day does a law bind from when it fixes none (F26)?** s. 21 fixes only the hour, the Ordinance's chapter on commencement is repealed, and Ordinance s. 17 covers regulations only. Nothing in the sources supplies the day, so it is an input.
12. **F27, F28, F34 (qualifiers):** does "except detachable fixtures" reach every limb of "immovables"; is guarding alone "possession"; does "visible to the eye" govern every way of presenting words; do the exceptions in "seaman" remove an ordinary seaman?
13. **F29:** are the note's "miles" nautical miles, and is the outer edge of the strip inside?
14. **F30:** is "a number of" (מספר) at least two, or at least one, and is it the same in ss. 16 and 20?
15. **F32:** does the exclusion of a navigator and a harbour master in "master" reach whoever has control?
16. **F33:** do the Ordinance's definitions govern anything given after 1981-10-01, and does Law s. 1's gate apply to them?
17. **The dates (finding 4):** when did the Ordinance take effect, when was its new text published, and when did the Movables Law and the Land Law take effect? The provisos of six entries turn on them.
18. **The earlier meaning of "enactment" (finding 3):** what did `חיקוק` mean in an enactment given before the Ordinance?
19. **Is the Ordinance's s. 1 still operative for earlier enactments at all (finding 1)?** Law s. 31 repeals it; Law s. 1 and the notes keep its definitions alive. A court's practice would settle which.
20. **F36:** does an open ("includes") entry refuse for a thing it does not list, or is a listed-members-only reading what courts apply? Is `נקבע` in the Ordinance (line 78) read to reach a regulation that itself uses the word?
21. **F37:** does Law s. 25 reach a reference made in an administrative direction? Do the Ordinance's definitions reach a direction given before the Law as they reach an enactment?
22. **F38:** what follows from a deviation from a form that is not slight, harms the essential or misleads?
23. **F35:** does s. 21's 00.01 govern the Law's own commencement?

## Findings

Numbered; each says what the text shows or what the run showed.
The mutation results and the expected failures are in section 5.

1. **The Ordinance's s. 1 is repealed and still operative.** Law s. 31 repeals the Ordinance except ss. 16(2), 16(4), 17, 19 and 42, so s. 1 is not saved; the text nonetheless carries it in full, with a note and Law s. 1 saying its definitions continue for words in enactments given before the Law. It is the one repealed section with operative life, and only for those enactments (F15, F33). Test: `s 31 — the Ordinance's section` 1 is not a survivor (`tests-ordinance-sweep.l4`), while the dispatcher says its definitions govern a 1960 enactment (`tests-definitions-ordinance.l4`).
2. **Five entries of Ordinance s. 1 read "(בוטלה)" and are replaced by the Law's.** `חטא`, `עוון`, `פשע`, `שנת כספים` and `מימי חופין`: each has a note giving the Law's definition and saying it governs earlier enactments. The dispatcher answers FALSE for them for every date (the Ordinance does not govern them) and `s 3 — section 3 governs` answers TRUE for them for a 1960 enactment (`tests-definitions-law.l4`, `tests-definitions-ordinance.l4`).
3. **Six entries carry a proviso that points at an earlier meaning, and the sources state five of them.** "Statute" (חוק), "enactment" (חיקוק), "ordinance" (פקודה), "regulation" (תקנה), "movables" (מיטלטלין) and "immovables" (מקרקעין) say that in an earlier enactment the word has the meaning it would have had without this Ordinance (or without the Movables Law, or the Land Law). The notes under "statute", "ordinance", "regulation", "movables" and "immovables" state that earlier meaning; no note or text states it for "enactment". The earlier meaning of "statute" is "law" (דין), which includes religious and Ottoman law and so is wider than the current definition. The encoding has one function per stated earlier meaning and a named refusal for "enactment" (asserted with `#ASSERT REFUSED ... BECAUSE`).
4. **The dates the provisos turn on are not in the sources.** The Ordinance's commencement (its ss. 10 and 11 are repealed), the publication of the new text (the signature line gives only the Minister's date, 1954-01-01, which is when the text was signed and not when it was published), the commencement of the Movables Law and of the Land Law (neither is among the sources). Each is therefore a plain fact the caller supplies (`The age of the enactment a word stands in`), and `Osig` stays `inert`.
5. **Miles and nautical miles (F23, F29).** The Law says nautical miles and the Ordinance's note says miles for what both treat as one strip. The two readings give different answers between 10.43 and 12 nautical miles; both are encoded and the rejected one is asserted to fail.
6. **One word, two readings across the passes (F30).** "מספר" is read as at least two in s. 16 and at least one in s. 20. Unedited.
7. **The Ordinance and the Law define the same word differently.** "Law" (דין): the Ordinance's covers a British Act or Order in Council "as in force in Palestine before the State was established or as in force in the State", the Law's only "as in force in the State". "Determined" (נקבע): the Ordinance says "in the law in which the word appears", the Law "in the enactment". "District" (מחוז): the Ordinance "by virtue of an enactment", the Law "by the Government by law". "Local authority" (רשות מקומית): the Ordinance has a municipality, a local council or a like authority, constituted by a law in force at that time that provides for local government; the Law has four named bodies. "Possession" (F28), "in writing" and "statute" also differ. Which governs depends on the age of the enactment, and the two dispatchers say so. "Consul", "movables" and "immovables" have the same list in both (the order of "built" and "planted" in "immovables" differs), and the Ordinance's rule calls the Law's.
8. **"Master" has a trailing exclusion whose reach the text does not fix (F32).** The Hebrew `להוציא` ("to take out") is read as "excluding".
9. **Two terms in one row.** The entry for "policeman" (שוטר) defines a second term, "senior police officer" (קצין משטרה גבוה), after a semicolon. The Ordinance's rule for it is a second function under the same row.
10. **A gloss that is uncertain.** `מַיִר` (in "sale", with exchange) is glossed "mayir (an exchange of goods)"; the sources do not define it, and it makes no difference to any answer (every listed form is a sale). `משוטי־דחף` is glossed "paddles"; the entry says a thing "not propelled by oars or paddles only" is a ship.
11. **A headword without quotation marks.** The repealed entries for `עוון` and `פשע` (lines 82 and 89) have no quotation marks around the headword, unlike the live entries. Unofficial-text formatting; the note under each uses the marks.
12. **One expected value was first written wrong, and corrected before any other change.** In `tests-definitions-ordinance.l4`, for the alternate reading of "master" (F32, B) the first draft of the expected-values list gave FALSE for a navigator who has control and is also appointed over the ship. Reading B is defined as "control alone is enough", so TRUE is what the reading says; the draft was a slip in the list and not a statement about the text. The run flagged it (1 failed of 650), and nothing else was changed to make an assertion pass.
13. **Pass 2 found no defect in pass 1 that a test shows.** No existing module or test was edited in pass 2. F30 records the one place where the two passes read a word differently.
    *The fix pass changed this:* the independent test pass showed that pass 1's s. 26 said TRUE where the text is silent (F38); the rule and its tests were edited and the edit is logged under `## Changes to existing modules`.
14. **Expected failures are now 26.** 12 in `tests-red.l4` (F1 to F25) and 14 in `tests-red-completion.l4` (F27 to F34); each asserts the answer of a considered and rejected reading, so each must fail while the encoding takes the other reading.
15. **Open entries lumped "not listed" with "not within the term" (F36).** The first reading of Ordinance "law" (line 42) answered FALSE for any source it did not list, including an Israeli Supreme Court precedent; the same shape was in "repeal", "sale", "will", "lease" and the notes under "ordinance" and "regulation". The independent test pass found the first; the rest were found by reading the other open entries.
16. **Lists collapsed into one flag or constructor.** Entries that name alternatives had the module take them only as one phrase (the ten kinds of street in one flag, the ten kinds of document in "regulation" in one flag, and so on). Each member is now askable beside the phrase: 27 declared types changed, of which 14 records gained fields (their signatures changed) and 13 enumerations gained constructors (`## Changes to existing modules`).
17. **Gaps the first two passes left.** The Law's reach by date and by kind of instrument, the source of the meaning of sin, misdemeanour and felony, s. 13(b) for a name alone, s. 20 where all must act, Ordinance s. 17 as publication and a day, and the office of president of a magistrates' court had no function; the scenario table in section 3 lists each.
18. **A struck subsection that the Law saves (F15).** Law s. 31 saves Ordinance s. 16(2), and the consolidation shows it deleted; both facts are now answerable, and the TRUE of pass 1 stands.
19. **One srcrefs `--strict` problem was in a file of pass 2 and is fixed.** In `il-interpretation-repeal.l4` a quotation and the locators below it did not cover the same lines; separate quote-only and locator-only directives now do. The 11 that remain are in the two pass-1 files and are listed under `## Changes to existing modules`.

## Jural relations

An interpretation Act mostly says what words and powers mean, and so creates few relations.
Where a rule extends a power or an immunity that another enactment gives, the relation is stated once, as between the two parties, and the L4 rule is named neutrally (it says what the power "covers", not whose it is).
The parties are those the text implies: the sections do not name them, because they apply to whatever enactment is being read.

| section | right / privilege / power / immunity held by | correlative duty / no-right / liability / disability borne by | kind | L4 rule |
| --- | --- | --- | --- | --- |
| Law s. 11 | the person for whose benefit an authorisation or duty with no time fixed exists (not named) | the holder of the authorisation or duty: to act with proper speed, and again as required | claim / duty | `s 11 — the thing was done in time:`, `s 11 — it is to be done again:` |
| Law s. 12 | the authority empowered to grant an exemption, relief or discount | the person who may be exempted: liable to a partial or conditional grant | power / liability | `s 12 — a power to grant exemption, relief or a discount covers granting` |
| Law s. 13(a), (b) | the authority empowered to appoint, authorise or charge | the person appointed, authorised or charged, by name or by the name of the office; whoever fills the office from time to time | power / liability | `s 13(a) — ...`, `s 13(b) — ...` |
| Law s. 14 | the authority empowered to appoint | the appointee: liable to be suspended, cancelled, dismissed or removed from duty | power / liability | `s 14 — a power to make an appointment covers` |
| Law s. 15 | the authority empowered to make regulations or give a direction | those the regulations or direction bind: liable to their amendment, change, suspension or cancellation | power / liability | `s 15 — a power to make regulations or give a direction covers` |
| Law s. 16 | the authority empowered to appoint a body of members | the members and the body: liable to a chairman and an alternate for each member | power / liability | `s 16 — a power to appoint a body of ... members covers` |
| Law s. 17(a), (b) | the authority empowered to do, hear or decide, or to compel | those who appear before it or are compelled: liable to its working procedure and to ancillary powers to a reasonable extent | power / liability | `s 17(a) — ...`, `s 17(b) — ...` |
| Law s. 18 | the authority empowered to decide an appeal or objection | the authority whose decision is reviewed, and the appellant: liable to confirmation, cancellation, a fresh decision or return | power / liability | `s 18 — the power to hear and decide an appeal or objection ...` |
| Law s. 19 | the holder of a power or duty under an earlier enactment | a later grant of power or imposition of duty: disabled, by itself, from taking away from the earlier | immunity / disability | `s 19 — a grant of power or an imposition of duty, by itself, takes away from ...` |
| Law s. 20 | most of the persons on whom an act is imposed | the rest of them, and those the act affects: liable to the act as done by most | power / liability | `s 20 — an act imposed on ... persons was validly done when ... of them did it` |
| Law s. 22(1), (2), (3) | anyone with validity, an earlier act or a right or obligation under the repealed law | the repealing enactment: disabled from reviving, affecting an earlier act, or affecting a right or obligation | immunity / disability | `s 22(1) — ...`, `s 22(2) — ...`, `s 22(3) — ...` |
| Law s. 23 | anyone with a regulation or appointment under a repealed enactment, where provisions replace it | the repeal: disabled from ending them until they are cancelled under the repealing enactment | immunity / disability | `s 23 — the regulations and appointments made under a repealed enactment ...` |
| Law s. 26 | the person who used a form with a slight deviation that neither harms the essential nor misleads | whoever would disqualify what was done under the form: disabled | immunity / disability | `s 26 — the deviation disqualifies what was done under the form:` |
| Law s. 33 | none named in the text | the person who publishes the Law: duty to publish within thirty days of adoption | duty (claimant not named) | `s 33 — the last day for publishing a law adopted by the Knesset on` |
| Ordinance s. 16(4) | the law with which a regulation would conflict | the authority making the regulation: disabled from contradicting a law | immunity / disability | `Ordinance s 16(4) — s 16(4) forbids the regulation:` |
| Ordinance s. 19 | the holder of a power conferred by an enactment not yet in force | everyone the early use of the power affects: liable to its exercise before commencement, valid from the commencement day | privilege or power / liability | `Ordinance s 19 — s 19 permits using the power of ...` |
| Ordinance s. 42 | the State | an enactment, and its makers: disabled from derogating from a right of the State or imposing a duty on it unless the enactment says so expressly | immunity / disability | `Ordinance s 42 — the enactment derogates from a right of the State or imposes a duty on it:` |
| **none** | | | | Law ss. 1 (the gate and the vintage rules), 2, 3 (all 26 entries and the opening words), 4 to 10, 21, 24, 25, 27 to 30, 31, 32; Ordinance s. 1 (all 66 entries, the notes and the opening words), ss. 16(1), 16(2), 16(3), 16(5), 17, and the repealed sections; the titles, headings, histories and signature blocks. These define a word, fix a date, count a period, choose a text, repeal or commence; none holds a party out as having a claim, liberty, power or immunity against another. |

Law ss. 11 and 33 are the only duties; the others extend or protect a power. s. 11's claimant, and s. 33's, are not named in the text, so they are listed as such and not guessed.

## Changes to existing modules

**Pass 1 files edited in the fix pass: two.**
Checked: `il-interpretation-time.l4` and `il-interpretation-carried-text.l4` are byte-identical (`cmp`) to the copies the independent test author was given, and that copy of `il-interpretation-law.l4` differs from this one only by item 1 below.
The other pass-1 tests and scripts (`tests-time.l4`, `tests-worked-cases.l4`, `tests-sweep.l4`, `tests-red.l4`, `gen-carried.py`, `oracle-s10.py`, `quote-hebrew.py`, `srcrefs.py`) were not compared byte for byte; their modification times are before the fix pass began.

1. `il-interpretation-law.l4`, Law s. 26: the rule `s 26 — the deviation disqualifies what was done under the form:` kept its name and signature, and now answers FALSE for a slight deviation that neither harms the essential nor misleads, and REFUSES for any other (F38). A named refusal was added to the file's `Named refusals` section. Before, it answered TRUE for any other deviation.
2. `tests-law.l4`, Law s. 26: the four assertions that expected TRUE for a deviation that is slight and harms the essential, slight and misleads, not slight and not harmful, and not slight and harmful and misleading, now assert the refusal; three combinations were added (all three true; not slight and harms the essential only; not slight and misleads only). 113 satisfied before, 116 now.

**Pass 2 records that gained fields.** A record built with `WITH` must now give every field, so a caller who built one of these must add the new fields. **Every new field is appended at the end.**
In the four fixtures of `tests-red-completion.l4` that build these records, `FALSE` for every new field kept the old answer (the 14 expected failures are unchanged); other callers should check theirs.

| record | fields added at the end |
| --- | --- |
| `A candidate person` | `a company`, `an association`, `a body of persons` |
| `A building or place` | `a building`, `another structure` |
| `A presentation of words or numerals` | `by printing`, `by lithography`, `by typewriting`, `by photography` |
| `An instrument under the Ordinance` | `a regulation`, `a rule`, `a by-law`, `a manifesto`, `a proclamation`, `an order`, `a direction`, `a notice`, `an announcement`, `another document` |
| `A person aboard a ship` | `works on a ship`, `is employed on a ship in any capacity` |
| `A way or place` | `a highway`, `an avenue`, `a lane`, `a bridle path`, `a footpath`, `a square`, `a courtyard`, `a promenade`, `an alley`, `a passage` |
| `A local body under the Ordinance` | `a municipality`, `a local council`, `an authority like them` |
| `A holding of land under the Ordinance` | `use`, `residence`, `possession`, `enjoyment` |
| `A movement across Israel's border` | `by sea`, `by land`, `by air` |
| `Instrument` (Law s. 3) | `a direction`, `an appointment`, `a notice`, `an announcement`, `a licence`, `a permit`, `something like them` |
| `A presentation of letters, numerals or signs` | `it presents letters`, `it presents numerals`, `it presents signs` |
| `A holding of land` (Law s. 3) | `it is use`, `it is possession`, `it is enjoyment` |
| `A judgment or decision` | `an appeal still lies against it`, `an appeal by petition still lies against it`, `an objection still lies against it`, `a like remedy still lies against it` |
| `A general word that follows a list` (Law s. 7) | `it is "or"`, `it is "other"`, `it is an expression like them`, `it is accompanied by "similar"`, `it is accompanied by "of like kind"`, `it is accompanied by another expression of analogy` |
| `A regulation measured against s 17 of the Ordinance for publication` (new) | (new record: `of legislative effect`, `published in Reshumot on`, `published in some other way on`) |

**Answers that changed on purpose** (a caller that relied on the old answer gets the new one):

- `anything else` in "repeal", "sale", "will", "lease" and the notes under "ordinance" and "regulation", and `any other source` in the Ordinance's "law", now REFUSE (F36); the new constructors `something that is not law in its ordinary sense`, `something that is not a sale in its ordinary sense` and the like answer FALSE. The Law's closed "law" still answers FALSE for `any other source`.
- Constructors were added to `A source that may be law under the Ordinance` (15: the 14 members and the one for what is not law in its ordinary sense), `A source that may be law` (Law; 7), `A post under the Attorney General` (4), `A way a law ceased to be valid` (2), `Where something was determined under the Ordinance` (1: it refuses), `A judicial office` (1), `A candidate for the earlier meaning of immovables` (9) and of `ordinance` (3), `A requirement or condition` (3), `A transaction or offer`, `A testamentary document`, `A letting` and `A candidate for the earlier meaning of regulation` (1 each). Adding a constructor breaks no existing call.
- `tests-red-completion.l4` and the pass-2 test files had their fixtures extended as above; the 14 expected failures still fail for the same rules.

**Two comments in pass-1 files are stale and were left as they were**, because they are neither a failing assertion nor a wrong citation:

- the header of `il-interpretation-carried-text.l4` (generated by `gen-carried.py`) says its provisions are "carried as quoted text and not computed"; the provisions of Law ss. 2, 4 to 7, 9, 11 to 19, 25, 22(1) and (3), the 23 entries of s. 3 and the Ordinance's s. 1 are now computed by the pass-2 modules, and the carried constants are still correct quotations that nothing reads;
- `il-interpretation-law.l4` line 11 says the canons are "carried as quoted text in il-interpretation-carried-text.l4 and listed in NOTES.md", and line 216 (now line 221, after the edit above) says limbs (1) and (3) of s. 22 are carried as text.

**srcrefs `--strict` problems in the two pass-1 files, not touched (11):** `il-interpretation-law.l4` lines 128, 139, 154 and 180 (a locator for `src:162` or `src:22` that no quote line above it covers), 151 (the run quotes `src:47-48`, its locators reach `src:22-48`), 217 (the run quotes `src:127-130`, its locators reach `src:129-129`); `il-interpretation-time.l4` lines 182 and 397 (`src:77`), 301 and 311 (`src:57`), 494 (`src:124`), each a locator that no quote line above it covers.
The six in `il-interpretation-law.l4` stood at lines 123, 134, 146, 149, 175 and 212 before item 1 above added five lines in front of them; they are the same six.
`--strict` is stricter than the gate `check.sh` runs (`--refs`, 0 problems).

Section 1 and the coverage table are the record of what is encoded.

## What would need doing before this encoding is worth relying on

1. **A domain expert reads it against the official text.** The official Knesset PDFs are linked in `../../source/SOURCES.md` (section 7 says they were fetched afterwards); only s. 10 of the Law has been compared with one (section 7). Everything else, and the whole Ordinance, rests on the Wikisource copy and on its editorial notes, which the encoding leans on in several places (the notes under the Ordinance's entries; the notes in Law s. 3; the head note).
2. **Fork choices are decided.** 38 forks, none ruled. The expensive ones: F3 and F2 (the end of a period), F14/F33 (what the Ordinance still governs), F30 (a number of), F29 (nautical or statute miles).
3. **The proviso dates are supplied** (finding 4): the Ordinance's commencement, the publication of the new text, the Movables Law and Land Law commencements.
4. **The earlier meaning of "enactment" is found** (finding 3).
5. **An independent test author** writes tests from the text without reading the modules, and does it again on this deposit.
   One such pass has run (607 assertions: 590 satisfied, 13 failed, 4 refused, 37 gaps); what it found is in findings 15 to 19 and the scenario table in section 3, and its assertions are not among these.
   All 2,103 satisfied assertions here were written by the agent that wrote the modules and share its one reading.
6. **A wrapper for an API.** The pass-2 functions take typed records, not the plain fields an API request carries, and the rest-days functions take a function. A caller builds the record from facts or wraps the function.
7. **Port to stable**, if wanted: the folder uses `REFUSE`, `#ASSERT REFUSED ... BECAUSE` and `YMD`, which the stable binary rejects. Not done and not part of this job.

## 7. Provenance of this run (added by the launching session, not by the encoder)

Everything above this heading was written by the encoder.
This section was added afterwards by the Claude Code session that launched and checked the run, on 2026-10-13.

**How the row was made.**
One Claude Sonnet 5.5 agent (Agent tool, `model: sonnet`, default effort), working alone from `BRIEF.md` in this directory; no ontology agent, fleet, integrator or independent test author.
Its transcript runs 2026-10-13 10:20Z to 11:10Z (18:20 to 19:10 +08), about 50 minutes.
It records 178 requests, all on `claude-sonnet-5-5`, 31,290 output tokens (a lower bound: the figure sums per-request usage), 1,671,862 cache-write and 77,889,842 cache-read tokens, with a peak context of 658,980 tokens.
Dollar cost is not computed here.

**The binary.**
`/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-41dd7a67/bin/l4`, built 2026-10-13 16:13 from l4-ide `unstable`, sha256 `2e3d6bd3a154e6b4080a445af6cc189dbc4ac087d8221682d09509212f1ce187`; `JL4_LIBRARY_PATH` unset.

**What the launching session re-ran, rather than taking from the encoder's report.**
`check.sh` printed the table the encoder reported: 8 modules, 630 assertions satisfied (113 in `tests-law.l4`, 314 in `tests-sweep.l4`, 182 in `tests-time.l4`, 21 in `tests-worked-cases.l4`), 0 refused, and 12 failed, all in `tests-red.l4` and all expected.
The `#ASSERT` directive counts in those five files are 113, 314, 182, 21 and 12, so none is double-counted or missing, and no module emits a warning.

**Checked independently.**
A separate Python implementation of s. 10(a), (b) and (c), reading A of fork F3 (the end moves to the first day that is not a rest day), reproduces all 21 cells of section 4's answer table, three rest-day calendars by seven cases, and the weekdays named in it.
That oracle was written by the launching session and shares reading A with the encoder; it does not test F3.
s. 10 of the Law as enacted (`source/official/9_lsr_209361.pdf`, text layer) matches the Wikisource text this row quotes, word for word, including the enacted spelling "בחדשה האחרון" in (b).

**Correction to statements above.**
Where this row's `README.md`, `subject.json`, `SOURCE-LICENSE.md` and section 0 of this file say that the official PDFs could not be fetched and that nothing is verified against the gazette, that was true when the encoder ran.
The PDFs were fetched afterwards and are in `source/official/`.
The only comparison made since is s. 10 of the Law, above; every other section of both texts, and the Ordinance in particular, is still read from Wikisource alone.

**Independence, and one departure from the brief.**
The encoder's transcript was audited: its Read, Glob and Grep calls touch only its own `inputs/` and deposit directories and the `encoding-a-subject` and `writing-l4-rules` skills, and no tool call names `commons`, `commonswt`, `canon` or `il`.
It did write scratch outside `DEPOSIT` and outside its working directory, in `scratchpad/interp-probes/` and `scratchpad/interp-tools/`; neither holds a deliverable and neither is filed here.

**Not done, and open for a domain expert.**
No independent test pass; the 630 assertions share the encoder's one reading, and `oracle-s10.py` covers s. 10 arithmetic only.
Fork F3 (several rest days at the end of a period: extension, or replacement by one day each) is not settled by the text; section 6 of this file has the discriminating case.
No domain expert has read this row; gate HG1 is not sought.

## Generators and checkers used and not shipped

Some files this document names were used while the encoding was written and are not in this folder: `coverage-data.py`, `expand-quotes.py`, `gen-coverage.py`, `gen-tests-ordinance.py`, `il-interpretation-definitions-law.l4.in`, `il-interpretation-definitions-ordinance.l4.in`, `il-interpretation-gate.l4.in`, `il-interpretation-powers.l4.in`, `il-interpretation-reading.l4.in`, `il-interpretation-repeal.l4.in`, `inventory.py`.
They were scripts and tables written for one run and are not part of the encoding.
The counts and tables they produced are copied into this file, and the `.l4` modules, not the scripts, are the source of truth.
Where a script generated a module, the module in this folder is the file to edit, and its template is not shipped.
The lead keeps them outside this repository.

## Independent test pass

A separate agent that had not seen this encoding, its NOTES.md or its brief, and that reads Hebrew, wrote `ANSWERS.md` from the two Hebrew texts alone before it opened any `.l4` file: 643 numbered scenarios over the Interpretation Law, 5741-1981, and the Interpretation Ordinance [New Version].
It then wrote `tests-independent.l4`, one `#ASSERT` per scenario that the encoding has a function for (607 assertions), and ran it against the pass-2 encoding with the pinned unstable binary.
Both texts are Hebrew Wikisource renderings, not the official text; nothing here was checked against the official text.
`ANSWERS.md` is not kept in this folder; the scenario numbers `S<n>` in `tests-independent.l4` refer to it, and each assertion carries its provision.

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run against the pass-2 encoding | 607 | 590 | 13 | 4 |
| after the fix pass, its API change and the reconciliation below | 607 | 607 | 0 | 0 |

The 37 scenarios the encoding had no function for when the file was run are the `-- GAP` lines at the end of the test file (21 lines naming 37 scenarios), with the test author's reason at that time; the fix pass later gave several of them a function, and NOTES.md, "Scenario codes from the independent test pass: where each lands", says where each of those went.

**What the 17 first-run disagreements turned out to be.**

- **Three led to a repair (S373, S485, S303).**
  S373: an open ("לרבות", "includes") entry answered `FALSE` for a thing it does not list; the Ordinance entries for "law", "repeal", "sale", "will", "lease" and the notes under "ordinance" and "regulation" now refuse for `any other source` or `anything else` (F36).
  S485: the Ordinance entry for "determined" had no way to ask about a word that appears in a regulation, where the matter is fixed in that regulation; the option `in the regulation in which the word appears` was added, and it refuses.
  S303 is a genuine fork (F15): the Law, s 31, names sections 16(2) and (4) of the Ordinance as surviving, and the consolidated Ordinance shows s 16(2) struck; the encoding follows the Law's operative words, and a sibling function states what the consolidation shows.
- **Eight were the convention, not the encoding (S009, S052, S223, S237, S259, S387, S589, S640).**
  The author expected a refusal where the module answers `FALSE`, which in this encoding means "outside the term / the section does not extend to it", not "the Act says no"; NOTES states the convention once, in section 1.
- **Two were the author's own errors (S384, S469).**
- **Four were refusals the module gives by design where the author wrote a value (S013, S135, S217, S623).**

**Four passed in the first run and refuse now because of the fix pass:** S291 and S292 (Law s 26 saves only a slight deviation that neither harms the essential nor misleads; for any other deviation the text does not say whether what was done under the form is disqualified, so the rule now refuses (F38); the author had noted that the old name "disqualifies" went a step beyond the text), and S475 and S514 (the "sale" and "will" entries are open, so `anything else` is neither in nor out (F36)).

Twenty assertions are rewritten in place (`#ASSERT REFUSED`, `#ASSERT`, or the encoding's value), each with a `-- RECONCILED S<n>` comment above it that quotes the author's original and gives the reason; none is deleted.

**The fix pass changed a public shape.**
Fourteen record types gained fields, appended at the end, so a caller that builds one with `WITH` must now give every field (the list is in "Changes to existing modules").
The author's file builds all fourteen, in 19 places; the lead added each new field with the value `FALSE` there so that the file would type-check, and no expected value was changed by it.
The fix pass also made the lists the Ordinance and the Law print askable by member, answered the author's gaps where the text states a rule (S231, S232, S269, S014 to S018, S021, S065 to S067, S289, S554, S591, S599 to S601, S643), and registered F35 to F38 (38 forks in all; the four new ones are marked "assumed, not ruled").
It edited two pass-1 files, the Law's s 26 rule and its test file, and logged both.

**Independence caveat.** No file of the lead's session was delivered into the test author's session.
The encoder's session received, after a context summary, the paths only of four other rows' triage files (AU, BC, CA, SG); a search of its tool calls finds no read of them.
It did read the test author's report for this row (its scenario texts and verdicts) to build its table of scenario codes, and compared three files with the copies the author was given; it did not open `tests-independent.l4`.

**Check.** `check.sh` with `tests-independent.l4` in the folder, run with `L4_TARGET=unstable` (so not compared with a main build) and the pinned binary `l4-unstable-0528`: 22 modules, 2710 satisfied, 26 failed (the expected 26: 12 in `tests-red.l4` and 14 in `tests-red-completion.l4`), 0 refused, run on 2026-10-29.
