# NOTES: Israel's rules for counting time, in L4

Row `legalese-sonnet-5.5`: one Sonnet 5.5 agent working alone from a written brief, with no ontology agent, fleet, integrator or independent test author.
Status: **draft**.
No domain expert has read any of it against the statute.

## 0. Provenance, and what to know before trusting anything here

**Both sources are unofficial.**
`../../source/law.wiki` (the Interpretation Law 5741-1981) and `../../source/ordinance.wiki` (the Interpretation Ordinance [New Version]) are consolidations from Hebrew Wikisource ("ספר החוקים הפתוח", a volunteer project run by a bot, OpenLawBot, from the Knesset's law database), fetched 2026-10-13: revisions 2883979 (2024-09-23) and 2966850 (2025-12-08).
The official Knesset PDFs could not be fetched (`fs.knesset.gov.il` answered every request with an HTML "Unavailable" page), so nothing here is verified against the gazette, and every claim about either text rests on one unofficial copy.
`../../source/SOURCES.md` records the hashes and the official links.
Wikisource's own notes (the `{{ח:הערה|…}}` template) are part of the text as fetched; where this encoding leans on one, it says so.

**The L4 was run with the `l4` built 2026-10-13 16:13 from l4-ide `unstable`** (`~/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-41dd7a67/bin/l4`, `JL4_LIBRARY_PATH` unset).
`l4` has no `--version` and I was given no commit id, so that timestamp is all the provenance the binary has.
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

**Encoded as executable functions with tests** (module `il-interpretation-time.l4`, which imports only `prelude` and `daydate`, and is the module other encodings should import):

- Law s. 10(a), (b) and (c), each as its own named function, plus composed forms: the last day of N days or weeks from a day, of N months or years after an event, and of a period whose nominal last day falls on days of rest, recess or holiday; whether a date falls inside a period (for days, weeks, months and years).
  The "from a day" and "after the day" spellings are aliases that say which subsection governs.
- Law s. 8 ("עד" includes the day it names), for dates, numbers (the citation sense) and moments.
- Law s. 3: "יום" (a day is midnight to the midnight after it), "שנה" and "חודש" (which calendar; a period counted by the Hebrew calendar is a named refusal), "שנת כספים" (first day, last day, whether a date is in it).
- Law s. 21 (a statute binds from 00:01 on its commencement day), with the case where the statute fixes a moment of its own.
- The Ordinance's s. 17 (regulations of legislative effect come into force on the day of publication, unless another provision fixes the day), alone and with Law s. 21.

**Encoded as executable functions with tests** (module `il-interpretation-law.l4`): Law s. 1 (the gate, "given before the Law commenced", which of s. 3 and Ordinance s. 1 defines a word, the calendar of year and month by vintage), s. 20, s. 22(2), s. 23, s. 24, s. 26, s. 31, s. 32, s. 33; Ordinance s. 16(4), s. 19, s. 42.

**Carried as quoted text and not computed** (module `il-interpretation-carried-text.l4`, generated from the source): the canons of construction and scope-of-power sections of the Law (ss. 2, 4 to 7, 9, 11 to 19, 25), the 23 definitions of s. 3 not encoded, limbs (1) and (3) of s. 22, the notes in the blank ss. 27 to 30, and the Ordinance's s. 1 notes and 65 definitions.
The reason each is not computed is in the coverage table.

**Not encoded at all:** the content of ss. 27 to 30 of the Law (the text says only that it was incorporated into four other enactments); the Hebrew calendar; any calendar of holidays; periods that s. 10 does not speak of (counted backwards, "within", mixed units: F8).
The 38 blank sections of the Ordinance have a row in the table and no L4.

**Files** (all under `encodings/legalese-sonnet-5.5/`):

| file | what it is |
| --- | --- |
| `il-interpretation-time.l4` | the reusable time module |
| `il-interpretation-law.l4` | the other computable provisions |
| `il-interpretation-carried-text.l4` | quoted text, generated by `gen-carried.py` |
| `tests-time.l4`, `tests-law.l4`, `tests-worked-cases.l4`, `tests-sweep.l4` | tests (the sweep is generated by `oracle-s10.py`) |
| `tests-red.l4` | twelve expectations that are meant to fail (section 5) |
| `check.sh`, `srcrefs.py` | the self-check; the quotation and locator gate |
| `quote-hebrew.py`, `gen-carried.py`, `oracle-s10.py` | how the Hebrew was quoted, the carried module generated, and the sweep generated |
| `encoding.json`, `SOURCE-LICENSE.md` | descriptors |

**A limit on reuse.**
The functions that take days of rest take a `FUNCTION FROM DATE TO BOOLEAN`, and, per the `writing-l4-rules` skill (R-X4), a rule with a function-typed input cannot be `@export`ed, because an API request carries values and not rules.
I did not test that here.
A caller who wants an API wraps one of these functions in a rule that takes a `LIST OF DATE` and passes `days of rest, recess or holiday listed in` that list; no such wrapper is provided.

**How the Hebrew got into the L4.**
Every Hebrew quotation is a `-- src:N | …` comment produced by `quote-hebrew.py` reading `../../source/*.wiki`, and `check.sh` runs `srcrefs.py check --refs` over every module to confirm each is a verbatim slice of the source and each `@ref` locator lies inside a quotation.
The operative modules cite their lines with `@ref … (src:N)`.
Where an `@ref` cites a line quoted in the other operative module it says so in words and carries no locator, because the gate checks a locator against quotations in the same file.
English paraphrases beside the quotations are mine and say so.

## 2. Coverage table

<!-- COVERAGE:BEGIN (generated by a script from the wikitext and dispositions.json; do not edit by hand) -->

#### Part A: the Interpretation Law 5741-1981 (33 sections; encoded 11, inert 16, out-of-scope 4, part encoded, rest inert 2)

| § | heading (Hebrew, from the text) | raw lines | the text shows | disposition | where, and why |
| --- | --- | --- | --- | --- | --- |
| 1 | תחולת החוק וסייגיה | 21-23 | content | encoded | il-interpretation-law.l4: the gate `s 1 — the Law governs` (two judgements the caller makes: another provision, an inconsistent context); whether an enactment was given before the Law commenced (by day, and by moment because the Law binds from 00:01 on 1981-10-01); whether s 3 reaches a word (it does not, for an earlier enactment, except חטא, עוון, פשע, fiscal year and, by a note, coastal waters); which definition governs; the calendar of year and month by vintage. Not encoded: whether s 21 re-times a statute that commenced before 1981-10-01 (fork F14). |
| 2 | תחולת הגדרות שבחיקוק | 24-26 | content | inert | Text carried in il-interpretation-carried-text.l4. A defined term means as defined; the definition reaches regulations made under the enactment and grammatical forms of the term; all subject to the s 1 gate. No input changes the answer except the gate's two judgements, which `s 1 — the Law governs` already takes, so a function here would be the constant TRUE. |
| 3 | משמעותם של מלים וביטויים | 29-63 | content | part encoded, rest inert | Encoded in il-interpretation-time.l4: יום (the midnight that begins and ends a day, whether a moment is within it), שנה and חודש (which calendar), שנת כספים (first and last day, whether a date is in it). Carried as text in il-interpretation-carried-text.l4: the opening words and 23 other definitions (writing, law, administrative direction, breach, statute, sin/chet, enactment, final, district, movables, coastal waters, immovables, representative of the Attorney General, determined, misdemeanour, ordinance, felony, consul, local authority, corporation, possession, affidavit, regulation; glosses mine). Each names a kind of thing or status; whether a thing falls under it is a judgement of the case, and no figure or date follows from it. Forks F5, F22, F24. |
| 4 | אדם | 64-66 | content | inert | Text carried in il-interpretation-carried-text.l4. A reference to a person includes a body of persons, corporate or not. A canon that widens a class named in some other enactment; applying it means reading that enactment, and no input to a function would change the answer. |
| 5 | יחיד ורבים | 67-69 | content | inert | Text carried in il-interpretation-carried-text.l4. The singular includes the plural and the reverse. A canon of construction for the words of another enactment; the brief names it as a canon that need not be forced into code. |
| 6 | זכר ונקבה | 70-72 | content | inert | Text carried in il-interpretation-carried-text.l4. The masculine includes the feminine and the reverse. A canon of construction, as s 5. |
| 7 | הכלל אינו מעין הפרט דוקא | 73-75 | content | inert | Text carried in il-interpretation-carried-text.l4. 'Or', 'other' or a like expression distinguishes from the list before it and does not infer from it, unless 'similar' or 'like' or another expression of analogy accompanies it. A canon on how to read a list in another enactment; whether an analogy word is present is a reading of that enactment's words, not a fact a caller can supply. |
| 8 | ”עד...“ | 76-78 | content | encoded | il-interpretation-time.l4: `s 8 — the date/number/moment … is up to and including` a limit. Settles that a date bound written 'until D' includes D; also reaches s 3's own 'until the following midnight' (F5) and fiscal year's 'until 31 December'. Forks F4, F5. |
| 9 | ”לפי“ | 79-81 | content | inert | Text carried in il-interpretation-carried-text.l4. 'According to' an enactment includes according to regulations made under it. A canon with a constant answer (yes). |
| 10 | תקופות | 82-86 | content | encoded | il-interpretation-time.l4: (a) days and weeks, (b) months and years, (c) days of rest, recess or holiday, composed forms, 'from'/'after' aliases, and 'inside a period' for each unit. Forks F1 to F3, F6 to F11. |
| 11 | מקום שלא נקבע זמן | 89-91 | content | inert | Text carried in il-interpretation-carried-text.l4. Where no time is fixed for a power or duty, it means with the proper speed and again from time to time as the circumstances require. The standard is open-textured and fixes no number; encoding one would invent a period (a duty with no WITHIN is the faithful shape), and no function here needs it. |
| 12 | סמכות לפטור | 92-94 | content | inert | Text carried in il-interpretation-carried-text.l4. A power to grant exemption, relief, discount and the like includes granting it in part or on conditions. One of the scope-of-power canons (ss 12 to 18). Each says what a grant of power includes by implication; a table of grant-and-included-power pairs could be written, but it would restate the text and no input varies. |
| 13 | מינוי והסמכה – כיצד | 95-98 | content | inert | Text carried in il-interpretation-carried-text.l4. A power to appoint, authorise or impose a duty may be exercised by naming the person or the office; an appointment by office means whoever fills the office from time to time. Computing the second limb needs the history of the office's holders, which only the caller has. |
| 14 | סמכות מינוי | 99-101 | content | inert | Text carried in il-interpretation-carried-text.l4. A power to make an appointment includes power to suspend its validity, cancel it, dismiss the appointee or suspend them from the post. Scope-of-power canon, as s 12. |
| 15 | סמכות התקנה | 102-104 | content | inert | Text carried in il-interpretation-carried-text.l4. A power to make regulations or give an administrative direction includes power to amend, change, suspend or cancel them in the way they were made. Scope-of-power canon, as s 12. |
| 16 | סמכות מינוי גוף | 105-107 | content | inert | Text carried in il-interpretation-carried-text.l4. A power to appoint a body of several members includes power to appoint a chairman and an alternate for each member. Scope-of-power canon, as s 12. |
| 17 | סמכויות עזר | 108-111 | content | inert | Text carried in il-interpretation-carried-text.l4. A power to do a thing or to hear a matter includes fixing procedure where an enactment has not (a), and the ancillary powers reasonably needed (b). Scope-of-power canon; (b) is an open standard ('to a reasonable extent'). |
| 18 | סמכות בהשגה ובערר | 112-114 | content | inert | Text carried in il-interpretation-carried-text.l4. A power to hear an appeal or objection includes confirming the decision with or without changes, cancelling it and deciding otherwise, or returning the matter with instructions. Scope-of-power canon, as s 12. |
| 19 | שמירת סמכויות וחובות | 115-117 | content | inert | Text carried in il-interpretation-carried-text.l4. A grant of power or imposition of a duty under one enactment does not by itself detract from a power or duty under another. A rule of non-derogation: it prevents an inference and computes nothing. |
| 20 | פעולת מספר בני אדם | 118-120 | content | encoded | il-interpretation-law.l4: `s 20 — an act imposed on N persons was validly done when K of them did it` (strictly more than half; fork F17). |
| 21 | שעת תחילה | 123-125 | content | encoded | il-interpretation-time.l4: the moment a statute begins to bind (00:01 on its commencement day), whether a moment is one at which it binds, and the same with a moment the statute fixes for itself. Self-applied to the Law in il-interpretation-law.l4 (s 32). Forks F12, F13. |
| 22 | סייגים לכוחו של ביטול | 126-131 | content | part encoded, rest inert | Limb (2) encoded in il-interpretation-law.l4: a repeal commencing on D cannot reach an act done before it binds (00:01 on D, by s 21). Limbs (1) (nothing without validity at the repeal is revived) and (3) (rights and obligations under the repealed law are unaffected) carried as text in il-interpretation-carried-text.l4: each is a proposition about the substance of the repealed law, with no date or number to compute. Fork F18. |
| 23 | תקנות ומינויים לפי חיקוק שבוטל | 132-134 | content | encoded | il-interpretation-law.l4: regulations and appointments lapse with the repealed enactment, unless the repealing enactment provides provisions in their place, when they stand until cancelled under it. One boolean input (F19). |
| 24 | הנוסח המחייב | 135-137 | content | encoded | il-interpretation-law.l4: the binding text is the text in the language in which the enactment was given, except for an enactment given in English before the State for which a new text was fixed under s 16 of the Law and Administration Ordinance (F20). |
| 25 | פירושם של אזכורים | 138-140 | content | inert | Text carried in il-interpretation-carried-text.l4. A reference to an enactment is to it as worded when it is resorted to, including added provisions and those that took its place. In L4 this is the rule-version axis (`EVAL UNDER RULES EFFECTIVE AT`), a property of how a caller evaluates, not a function of facts; the sources hold no version history to evaluate against. |
| 26 | סטיה מטופס | 141-143 | content | encoded | il-interpretation-law.l4: a deviation from a prescribed form disqualifies what was done unless it is slight and neither harms the essential nor misleads (three judgement inputs; F20). |
| 27 | (none) | 146-148 | blank: a note that the text was incorporated into another enactment | out-of-scope | Blank in the text. The text under the number is a note that the section's text was incorporated into the Evidence Ordinance [New Version], 5731-1971 (note carried in il-interpretation-carried-text.l4). It does not say what the text was, and that enactment is not among the sources, so what s 27 said is not known here and nothing is encoded. |
| 28 | (none) | 149-151 | blank: a note that the text was incorporated into another enactment | out-of-scope | Blank in the text. The text under the number is a note that the section's text was incorporated into the State Property Law, 5711-1951 (note carried in il-interpretation-carried-text.l4). It does not say what the text was, and that enactment is not among the sources, so what s 28 said is not known here and nothing is encoded. |
| 29 | (none) | 152-154 | blank: a note that the text was incorporated into another enactment | out-of-scope | Blank in the text. The text under the number is a note that the section's text was incorporated into the Contracts (General Part) Law, 5733-1973 (note carried in il-interpretation-carried-text.l4). It does not say what the text was, and that enactment is not among the sources, so what s 29 said is not known here and nothing is encoded. |
| 30 | (none) | 155-157 | blank: a note that the text was incorporated into another enactment | out-of-scope | Blank in the text. The text under the number is a note that the section's text was incorporated into the Law and Administration Ordinance, 5708-1948 (note carried in il-interpretation-carried-text.l4). It does not say what the text was, and that enactment is not among the sources, so what s 30 said is not known here and nothing is encoded. |
| 31 | ביטול | 158-160 | content | encoded | il-interpretation-law.l4: `s 31 — the Ordinance's section N, subsection M, survives the Law`: 16(2), 16(4), 17, 19 and 42 survive; the rest of the Ordinance is repealed; a question about section 16 as a whole is a named refusal. The Ordinance text marks 16(2) 'deleted' (F15). |
| 32 | תחילה | 161-163 | content | encoded | il-interpretation-law.l4: the Law commenced on 1981-10-01 (the text states the Hebrew date 3 Tishrei 5742 and the Gregorian date together; the Gregorian one is used). With s 21 it binds from 00:01 that day. |
| 33 | פרסום | 164-166 | content | encoded | il-interpretation-law.l4: the Law is to be published within thirty days from the day of its adoption; by s 10(a) the last day is 1981-06-19 for the adoption on 1981-05-20 that the text records. Fork F21. |

#### Part B: the Interpretation Ordinance [New Version] (43 sections; encoded 3, inert 38, part encoded, rest inert 2)

| § | heading (Hebrew, from the text) | raw lines | the text shows | disposition | where, and why |
| --- | --- | --- | --- | --- | --- |
| 1 | פירושם של מונחים רווחים | 30-115 | content | part encoded, rest inert | Not in the saving list of Law s 31 and so repealed, yet the text still carries it, with a note that its definitions continue to apply to enactments given before the Law (Law s 1). Encoded in il-interpretation-law.l4: שנה and חודש (Gregorian, no Hebrew clause) in the vintage functions. Carried as text in il-interpretation-carried-text.l4: the notes, the opening words and 65 other definitions. The Ordinance has no definition of יום. |
| 2 | (none) | 116-118 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 3 | (none) | 119-121 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 4 | (none) | 122-124 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 5 | (none) | 125-127 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 6 | (none) | 128-130 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 7 | (none) | 131-133 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 8 | (none) | 134-136 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 9 | (none) | 137-139 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 10 | (none) | 142-144 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 11 | (none) | 145-147 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 12 | (none) | 150-152 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 13 | (none) | 153-155 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 14 | (none) | 156-158 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 15 | (none) | 159-161 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 16 | התקנת תקנות | 164-171 | content | part encoded, rest inert | Encoded in il-interpretation-law.l4: (4), a regulation may not contradict a law (where the power was conferred by a law and no other intention is implied). Subsections (1), (3), (5) read `(בוטלה)` (repealed) and (2) reads `(נמחקה)` (deleted); carried as text in il-interpretation-carried-text.l4. Law s 31 says (2) survives, which the text contradicts (F15). |
| 17 | תחילת תקפן של תקנות בנות־פעל תחיקתי | 172-174 | content | encoded | il-interpretation-time.l4: regulations of legislative effect come into force on the day of their publication unless another provision fixes the day; with Law s 21, from 00:01 that day. |
| 18 | (none) | 175-177 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 19 | שימוש בסמכות בין נתינת חוק לתחילת תקפו | 180-182 | content | encoded | il-interpretation-law.l4: when s 19 permits using a power before the enactment commences, and the earliest day a regulation made under it may be valid. Fork F16. |
| 20 | (none) | 183-185 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 21 | (none) | 186-188 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 22 | (none) | 189-191 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 23 | (none) | 192-194 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 24 | (none) | 195-197 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 25 | (none) | 198-200 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 26 | (none) | 201-203 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 27 | (none) | 204-206 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 28 | (none) | 209-211 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 29 | (none) | 212-214 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 30 | (none) | 215-217 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 31 | (none) | 218-220 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 32 | (none) | 223-225 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 33 | (none) | 226-228 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 34 | (none) | 229-231 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 35 | (none) | 232-234 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 36 | (none) | 235-237 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 37 | (none) | 238-240 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 38 | (none) | 241-243 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 39 | (none) | 244-246 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 40 | (none) | 247-249 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 41 | (none) | 250-252 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |
| 42 | זכויות המדינה שמורות | 253-255 | content | encoded | il-interpretation-law.l4: an enactment derogates from a right of the State or imposes a duty on it only if it says so expressly. |
| 43 | (none) | 256-258 | blank: `(בוטל)` (repealed) | inert | Blank: `(בוטל)`, repealed. The Law's s 31 repeals the Ordinance except 16(2), 16(4), 17, 19 and 42, and this section is not among them. Nothing to encode. |

<!-- COVERAGE:END -->

## 3. Fork register

Each entry gives the readings seen, the one taken, the text that licenses each, and whether it changes an answer.
Entries marked *assumed, not ruled* are this encoding's choices where the text says nothing; they are meant to be reverted alone.
The rejected readings that have a computable answer are asserted, and fail, in `tests-red.l4`.

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

### F16. Ordinance s. 19: using a power before the enactment commences

- **Text.** Line 181. A power conferred by an enactment whose commencement is not with its giving may be used, "if no other intention is implied, at any hour after the giving of the enactment, to the extent it appears necessary or proper to operate the enactment on its commencement day"; what was done under it has "no validity **until** the day of commencement" unless another intention is implied or it was needed to operate the enactment.
- **Reading taken, "until".** Validity begins **on** the commencement day. Read with s. 8 ("until" includes the day), nothing done under the power would be valid on the day the enactment first binds, which defeats the section's own purpose of operating the enactment on that day; Law s. 1's context exception is taken to switch s. 8 off here. The literal reading's answer (valid from the day after) is asserted, and fails, in `tests-red.l4`.
- **"At any hour after its giving."** The functions work in days, so the day of giving is included (the use is taken to follow the giving within the day). The permission is modelled as the window from the day of giving up to, not including, the commencement day; from the commencement day the power is the ordinary power and s. 19 gives no permission and no prohibition, so `s 19 permits …` answers FALSE there. FALSE means "s. 19 does not itself permit it", not "forbidden".

### F17. Law s. 20: "רובם"

- A majority is more than half: 3 of 5, 3 of 4 and 2 of 3 are, 2 of 4 is not. Two of four as "their majority" is asserted, and fails, in `tests-red.l4`. Numbers that cannot describe an act done by some of the people it was imposed on (more actors than persons, none imposed, fractions) are a named refusal.

### F18. Law s. 22(2): "a previous act"

- Measured against the moment the repeal binds (00:01 on its commencement day, by s. 21): an act at 00:00:30 on that day is earlier, an act at 00:01:00 is not. Limbs (1) and (3) are propositions about the substance of the repealed law and are carried as text.

### F19. Law s. 23: replacement provisions

- Modelled as one boolean the caller supplies: whether the repealing enactment "provides provisions in place of the repealed ones". Whether it does is a reading of that enactment. The result is two named outcomes (lapse, or stand until cancelled under the repealing enactment).

### F20. Law ss. 24 and 26: judgement inputs

- s. 24 (the binding text): two booleans, whether the enactment was given in English before the State and whether a new text was fixed under s. 16 of the Law and Administration Ordinance (a statute outside the sources). s. 26 (deviation from a form): three judgements, "slight", "harms the essential", "misleads", read as a conjunction (slight and neither of the others) because the relative clause "שאין בה כדי לפגוע בעיקר או להטעות" restricts the slight deviation. The encoding states the test and takes the judgements as inputs.

### F21. Law s. 33

- "Within thirty days **from** the day of its adoption": s. 10(a), days, so the last day is the day thirty days on (1981-06-19 for the adoption on 1981-05-20 that the text records). s. 10(c) is not applied: whether a duty to publish is a "period" whose last day can move is not said; a caller can compose it.

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

### Where I looked and found nothing further

- Ss. 2, 4, 5, 6, 7, 9: read for any input that could change the answer other than the s. 1 gate; none. Ss. 11 to 19: read for a number or a date; s. 11 has an open standard ("the proper speed") and no number; ss. 12 to 18 only list what a grant of power includes. s. 25 (references): the text points at the version in force when the reference is resorted to, which is a way of evaluating, not a function.
- s. 10: read for the forks the brief names, for the position of "from" and "after", for any treatment of weeks, backward counting, "within", and time of day; found F1 to F3, F6, F7, F8 and F25 and nothing else.
- Ordinance ss. 2 to 15, 18, 20 to 41, 43: each reads "(בוטל)" and nothing more.

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

`check.sh` is the skill's script plus three checks of its own: every module starts with `@lang en` and has an ASCII filename, `l4 check` prints no stray-`@ref` warning, and `srcrefs.py check --refs` finds no problem in any quotation or locator.
It reads the diagnostics, not the exit code: `l4 run` exits 0 when an `#ASSERT` fails.
The run recorded here, with the binary named in section 0:

```text
module                                    errors satisfied  failed  refused  expected
il-interpretation-carried-text.l4              0         0       0        0         0
il-interpretation-law.l4                       0         0       0        0         0
il-interpretation-time.l4                      0         0       0        0         0
tests-law.l4                                   0       113       0        0         0
tests-red.l4                                  12         0      12        0        12
tests-sweep.l4                                 0       314       0        0         0
tests-time.l4                                  0       182       0        0         0
tests-worked-cases.l4                          0        21       0        0         0
TOTAL (8 modules)                             12       630      12        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)

extra checks
  all modules start with '@lang en' and have ASCII filenames
  l4 check: no stray @ref warnings
  srcrefs: srcrefs check: 232 src: lines, 137 runs, 193 locators, 0 problems
```

**The 12 failed assertions in `tests-red.l4` are expected.**
Each asserts the answer of a reading that section 3 considered and rejected: F1 (R3, two), F25 (two), F3 (readings B and C, two), F2, F5, F12, F4, F16 and F17 (one each).
So each must fail while the encoding takes the other reading.
`check.sh` lists the count (`expected_failed`), and `encoding.json` names the file (`expected_red`).
The file doubles as proof that this harness can fail.
Separately, deliberate mutations were each caught by the tests in a scratch copy of the modules: counting the start day in s. 10(a) (56 failures), walking the end of (c) backwards (21), making s. 8 exclusive for dates (10), binding from midnight in s. 21 (9), ending a short month on the 28th in (b) (14), ignoring another provision in Ordinance s. 17 (2); and, in the law module, the s. 20 threshold (2), the s. 31 list (1), the s. 1 gate (2) and the s. 22(2) comparison (1).
No assertion refused, and none was left unevaluated.

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

