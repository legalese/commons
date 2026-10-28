# Encoding brief: the Interpretation (Jersey) Law 1954, every deposited version, in L4

You are producing an L4 encoding of the Interpretation (Jersey) Law 1954 from its sources.
This brief is the whole specification.
Read it fully before opening any source, then read the two skills it names.

## The subject

**Interpretation (Jersey) Law 1954** (L.17/1954), "A LAW for promoting brevity and uniformity in enactments".
It tells the reader of any Jersey enactment, whenever passed or made, what standard words mean and how standard situations are construed: what an "enactment" is, how a day of commencement is read, what "month" and "midnight" mean, when service by post is deemed made, how penalties are read, which references go where.
Its rules nearly all say "unless the contrary intention appears" or "unless the context otherwise requires".
It is read together with the **Legislation (Jersey) Law 2021** (L.8/2021), which on 28 September 2021 took over and deleted several of its provisions (Article 1(2), (5), (6); Articles 6, 16, 17; paragraphs 11(3), 11(4)); that Law is encoded separately, by someone else, as its own commons subject, and you do not encode it.
Wherever a provision of the 1954 Law now says "see the Legislation (Jersey) Law 2021", you cite it and take what you need from it as an input.

## Vintages: seven deposited versions, each its own answer

All under `SOURCES` = `subjects/je/interpretation-1954/source/`, one `.txt` per version (one paragraph per line, indented by level; `src:N` is line N) and the `.html` it came from.
`RAW` for your quotations is the current text, `l_17_1954.current.txt`; quote every other version as `src:<stem>:N`.

| version | stem | the text shown | what changed from the previous one (verified by comparing the seven texts paragraph by paragraph on 2026-10-28) |
| --- | --- | --- | --- |
| V1 | `l_17_1954_20210927` | 1 Jan 2019 to 27 Sep 2021 | the first consolidated version. Has Art 1(2), 1(5), 1(6); Art 6 (effect of repeal, (1) to (3)); Art 9(3) "as amended from time to time"; Art 11(3), 11(4); Art 16 (exercise of statutory powers before commencement); Art 17 (effect of repeal and re-enactment, and expiry). Art 8 has limbs (a) (b) (ba) (c) (d) (e). |
| V2a | `l_17_1954_20220130` | 28 Sep 2021 to 30 Jan 2022 | 1(2), 1(5), 1(6), 6, 11(3), 11(4), 16, 17 deleted (placeholders remain); 9(3) now "as amended, revised or otherwise consolidated (within the meaning of the Legislation (Jersey) Law 2021) from time to time"; Art 11A (power to appoint to an office) added. |
| V2b | `l_17_1954_20220831` | 31 Jan 2022 to 31 Aug 2022 | Art 8: new limb (f) for a bank winding up order. |
| V2c | `l_17_1954_20240110` | 1 Sep 2022 to 10 Jan 2024 | Art 8: new limb (f) for a limited liability company; the bank limb becomes (g). |
| V2d | `l_17_1954_20251123` | 11 Jan 2024 to 23 Nov 2025 | Art 1(1) editorial ("confirmed by Her Majesty in Council" becomes "confirmed by Order in Council"); "Schedule" capitalisation. |
| V2e | `l_17_1954_20260618` | 24 Nov 2025 to 18 Jun 2026 | Schedule Part 1: definitions of "child" and "parent" added. |
| V2f | `l_17_1954.current` | 19 Jun 2026 to current | Art 8: new limb (ea) for an administration order. |

The first line of each `.txt` after the title and the `.meta.json` beside it give the retrieval details; each `.html` banner reads "Showing the law from … to …".
**Before 1 January 2019 no text is deposited.** The site offers none.
The endnotes of V1 say that Art 1(5) was amended and Art 1(6) was inserted by the Interpretation (Amendment) (Jersey) Law 2003 (L.16/2003, in force 28 March 2003), and that the Schedule was inserted by the same Law and later amended by L.8/2005, L.6/2010, L.4/2012, L.17/2015, R&O.115/2016 and L.19/2018.
So, for a date from 28 March 2003 to 31 December 2018, you may answer **only** these four, each labelled "inferred from the endnotes of the 2019 consolidation, not verified against L.16/2003": Art 1(5), Art 1(6), the Schedule definition of "month", the Schedule definition of "midnight" (for the last two, the amending Laws named in the endnote are, by their titles, about other subjects; that is an inference, say so).
**Everything else, for a date before 1 January 2019, refuses** with `before the first consolidated version (1 January 2019)`; for a date before 28 March 2003 even those four refuse.
Model the version as a function of a date input (`the text of the Law in force on` d), with the table above as data; do not make the caller name V2c.

**Which date selects the text (changed 2026-10-28 after the first brief, on GM's point that Article 3(6) keys on whether the legislation had COMMENCED before 28 September 2021, not on the day it was made).** Fork `I1`. DEFAULT: for an enactment made before 28 September 2021, evaluate its commencement under V1 Art 1(5)/(6) to get a candidate day; if the candidate is before 28 September 2021, V1 governs; if it is on or after it, V1 no longer exists (deleted that day) and the 2021 Law's Article 3 governs, so the function returns the candidate day with a marker `governed by the 2021 Law, Article 3(2)` (for a named day both rules give the start of that day); for an enactment made on or after 28 September 2021 the function refuses naming the 2021 Law, Article 3. Not circular: the candidate is computed under V1 and then compared with 28 September 2021. CALLABLE ALTERNATIVES: (b) the text in force on the day the enactment was made; (c) the text in force on the day the question is asked. All three are 'assumed, not ruled'. Hand-written tests: made 20 Sep 2021, named day 1 Oct 2021: candidate 1 Oct 2021, marker 2021 Art 3; made 20 Sep 2021, named day 21 Sep 2021: V1; made 27 Sep 2021, silent: V1, candidate 27 Sep 2021 (start of that day, by 1(5) with 1(6)); made 28 Sep 2021: refuses naming the 2021 Law Art 3; and show that on (a) and (b) the day is the same in each case and only the governing provision differs. For Art 8 the selecting date is the day of the event (item 6 below); for every other Article, the day the question is asked about (the day the fact occurred) unless the Article says otherwise; say which in a comment on each function.

## Scope — the whole Law, in every version, pinned

Every paragraph of Articles 1 to 18 and of the Schedule (Part 1 and Part 2) in each of the seven versions, including the paragraphs that exist in some versions only.
The placeholders of deleted provisions ("(2) [2]") get a row, disposition `inert`.
The endnotes (Table of Legislation History, Table of Renumbered Provisions, Table of Endnote References) are not provisions; use them as evidence for the vintage table and the pre-2019 rule, and say so in `NOTES.md`.
Out of scope: the other enactments the Law mentions (Companies Law, Children Law, Civil Partnership Law and the rest; their contents are inputs where needed); the Legislation (Jersey) Law 2021 (encoded elsewhere).

## Claims to verify against the text (they come from a first reading; check each, correct the brief if wrong)

1. V1 Art 1(5): an enactment "expressed or construed as being expressed to come into operation on a particular day" is "construed as coming into operation immediately on the expiration of the previous day" (so: at the start of that day). V1 Art 1(6): an enactment "expressed to come into operation forthwith or … silent as to the time at which it is to come into operation" is "construed as being expressed to come into operation on the day on which it was passed or made". Read together, 1(5) applies to what 1(6) construes ("or construed as being expressed"), so a silent enactment made on day D comes into operation at the start of D, before it was made. Encode what the words say, test it, and register it as a finding. V2 has neither paragraph; the commencement rule is then in the 2021 Law (not yours), so for a date from 28 September 2021 your commencement function refuses with a message that names the 2021 Law, Article 3. (Do NOT copy the 2021 Law's rule into your row.)
2. Art 1(7) (all versions): where the time at which an enactment is to come into operation is expressed or calculated by reference to its promulgation and the date of promulgation is unknown, that date is deemed to be the day the enactment was passed or made. V1 Art 1(2): a Law is not deemed passed until confirmed by Her Majesty in Council and registered by the Royal Court.
3. Art 7 (all versions): service by post is dealt with only "where an enactment … authorizes or requires any document to be served by post"; then, unless the contrary intention appears, service is deemed effected by properly addressing, prepaying and posting a letter containing the document, and, unless the contrary is proved, to have been effected at the time at which the letter would be delivered in the ordinary course of post. It is a presumption about the time, rebuttable; neither the day of posting nor the day of actual receipt as such. Model it as such (the ordinary-course delivery time is an input; proof of another time is an input). It does not apply to other modes of service. It does not say how many days post takes.
4. Schedule Part 1: "month" shall mean a calendar month; "midnight", in relation to a day, shall mean the last moment of that day. Neither says how a month is added to a date at a month end, or in which time zone a day is read. A function for "done by midnight on D" compares the instant's calendar day with D (an instant on the following day at 00:00:00 is after the midnight of D); say in `NOTES.md` that the time zone is an input you assumed (Jersey local time), not something the Law says.
5. Schedule: some definitions say "shall mean" (exhaustive) and some "includes"/"shall include" (not exhaustive): model the difference and test it (a thing outside a "includes" list may still be within the word; outside a "means" list it is not). Part 2 is "only … an index of definitions in other enactments which are of extended application" (Art 4(2)): it never supplies a meaning; test that. Art 4(1): the Part 1 definitions apply "unless the contrary intention appears" to every enactment, whenever passed or made. Part 1 changes only for "child" and "parent" (V2e); every other definition is the same in all seven versions (verify with a diff).
6. Art 8: a "person becoming bankrupt" in any enactment means any of the listed events, which vary by version (limbs above); the limb for a company is "the winding up … by means of a creditors' winding up". A question about a person's bankruptcy needs the event, its date, and which text governs: register as a fork whether the text in force on the day of the event or on the day the question is asked governs, default the day of the event (assumed, not ruled), with the other callable.
7. Art 13: (1) a penalty specified for an offence means the offence is punishable by a penalty not exceeding it; (2) a fine with no amount or level on the standard scale specified is a fine of unlimited amount; (3) where more than one penalty is specified, "and" means the penalties may be imposed alternatively or cumulatively; (4) applies to all enactments, whenever passed or made. All versions, same text.
8. Art 12: an act or omission that is an offence under two or more enactments, or under an enactment and the customary law of Jersey, may be prosecuted and punished under either or any, but not punished twice for the same offence. (It says nothing about two offences in the same enactment.)
9. Art 3 with the Schedule: in an enactment relating to a punishable offence "person" includes a body corporate unless the contrary intention appears; the Schedule says "person" shall include any body of persons corporate or unincorporated; the proviso protects a body corporate from liability for anything done before the date of the commencement of the Law (21 August 1954, from the Table of Legislation History in the endnotes) if it would not then have been liable.
10. Art 9: references by number only (9(1), 9(2)); a reference to an enactment is to it as amended (V1: "from time to time"; V2: "amended, revised or otherwise consolidated … from time to time" and "includes … as extended or applied under another enactment") unless the context otherwise requires (9(3)); applies to subordinate enactments with the necessary changes (9(4)); to all enactments including this Law (9(5)); "subordinate enactment" (9(6)).
11. Art 11 (V1: paragraphs (1) to (4); V2: (1), (2)); 11(4) of V1 applies only to an enactment passed after 28 March 2003 and is a long list of ways a power may be exercised. Art 11A (V2 only): a power to appoint to an office includes the four related powers, the last only in the four circumstances of 11A(2). Art 14: a deviation from a prescribed or specified form "not materially affecting the substance nor likely to mislead" does not invalidate the form used (both conditions are judgement inputs). Art 15: a distance is measured in a straight line on a horizontal plane. Do NOT build geometry: the Law gives a method, not a formula. Encode the method as a noun (the way the distance was measured: along a straight line on a horizontal plane, or another way) with the measured distance as an input, and a rule that says whether the method is the Law's default or a contrary intention is relied on. Arts 5, 10: inputs and tests as the text allows.
12. V1 Arts 6, 16, 17: effect of repeal; exercise of statutory powers before commencement; effect of repeal and re-enactment and of expiry. Encode them as the rules they state (inputs: what was repealed, what was done, what the contrary intention is).
13. The Law's own commencement date, 21 August 1954 (Table of Legislation History).
14. **"Comes into operation" and "comes into force".** The 1954 Law says "commencement … the time at which the enactment comes into operation" (Art 1(4)); the 2021 Law and the Charities (Jersey) Law 2014 say "comes into force". Treat them as the same event (assumed, not ruled, and say so in `NOTES.md`), put "comes into force" in the names and descriptions of your exported questions, and cite Art 1(4) in a comment.

## Worked cases from outside the Law (cross-checks, labelled as such in the tests)

The Charities (Jersey) Law 2014 text, `subjects/je/charities-2014/source/charities-jersey-law-2014-2026-10-02.txt`, lines about 870 to 900 (the Table of Legislation History, in the endnotes) gives commencement dates: Law in force 21 November 2014; 1 May 2018 and 1 January 2019 under R&O.17/2018 ("come into force on 1st May 2018" / "1st January 2019"); R&O.10/2024 Article 5 "comes into force at 9.30 a.m. on 27th February 2024" (that one is after 28 September 2021).
Your commencement function should answer, for an enactment commenced on a named day on or before 27 September 2021: in force from the start of that day, by V1 Art 1(5).
Use those dates as cross-check cases in a clearly separate test module (`je54-tests-crosschecks.l4`), with comments saying they apply the Law to instruments it does not contain.
You may read those few lines of that file and nothing else of the Charities Law.

## What the Law does not say — each a refusal or an input, listed in NOTES.md section 7

(Also list there, with the reason, that Articles 2, 3, 7, 10, 12, 13, 14, 15 and the other provisions outside the four pre-2019 items refuse for a date before 1 January 2019 although their endnotes show no amendment after 2003: this is a deliberate choice, consistent with the Charities (Jersey) Law 2014 row, because no text of those years is deposited. Art 7 in particular was the original Article 12 and was renumbered; a question about service before 1 January 2019 refuses.)

How a period of days, weeks or years is counted; what a "year", "week" or "day" is; how a calendar month is added at a month end; the time zone of a day; how long post takes; what is "the ordinary course of post"; which of two times governs a bankruptcy question; any rule for the commencement of an enactment after 27 September 2021 (the 2021 Law's); the time of day at which a silent enactment commences under V1 other than what 1(5)+1(6) produce.

## Naming and layout

Module prefix `je54-`: `je54-nouns.l4` (nouns only), then for example `je54-vintage.l4` (the text in force on a date), `je54-art01-commencement.l4`, `je54-schedule-definitions.l4`, `je54-art07-service-by-post.l4`, `je54-art08-bankruptcy.l4`, `je54-art09-references.l4`, `je54-art11-powers.l4`, `je54-art12-15-penalties-forms.l4`, `je54-v1-arts-6-16-17.l4`, and `je54-tests-*.l4` (one tests module per rule module, plus the cross-checks).
Name the exported questions in the reader's words; a short `§ Seat questions` module `je54-seat.l4` that imports the rule modules and holds the `@export`ed questions is welcome (a layer that asks the reader's questions of the rule modules).

## Where you work (fixed paths; do not use any other)

| name | path |
| --- | --- |
| `DEPOSIT` (your row; write only here) | `subjects/je/interpretation-1954/encodings/legalese-2026-10/` |
| `SOURCES` (read only; never edit) | `subjects/je/interpretation-1954/source/` |
| `SCRATCH` (temporary files, logs; nothing goes to `/tmp`) | `<scratch directory, not deposited>` |
| `L4_BIN` | `<path to the pinned l4 binary>` |
| skills (read them first) | `skills/encoding-a-subject/` and `skills/writing-l4-rules/` in the legalese/l4-ide repository (open `SKILL.md`, then the `references/` and `assets/` they point at) |
| the Charities (Jersey) Law 2014 row, for style and tools only | `subjects/je/charities-2014/encodings/legalese-full-2026-10/` (read `g7-commencement.l4`, `g7-tests-commencement.l4`, `domain.l4` for house style; `check.sh`, `srcrefs.py`, `check-traces.py` as models; do not edit anything there) |

`DEPOSIT` already holds `tools/extract_law.py` (how the `.txt` sources were made), `srcrefs.py` (the quotation and locator checker), `check.sh.template` (the skill's `check.sh`, to adapt) and `SOURCE-LICENSE.md`.
Do not run git. Do not edit anything outside `DEPOSIT` and `SCRATCH`.
Do not use the network.
Run `l4` under `nice -n 15`, at most two `l4` processes at a time, and kill a stuck process only by its PID (`kill <pid>`), never with `pkill -f` or a pattern.
Never print or write the environment (`env`, `printenv`).
If you wait for a process, wait on its PID (`kill -0`), never with `pgrep -f` on a name.

## Toolchain and target

You run `L4_BIN`, the prerelease `unstable-20261026-6325439` (`L4_BIN --version` prints it; sha256 of the binary `18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475`).
**The target is `unstable`** (ruled for this job by the owner, Meng, 2026-10-28: nobody will run this on a `main` build).
So `REFUSE "…"`, `#ASSERT REFUSED … BECAUSE "…"` and everything else `writing-l4-rules` documents for `unstable` are allowed, and you do not need `fetch-main-l4.sh` or a main-build comparison.
Say in `NOTES.md` that no `main` build has read the deposit.
Leave `JL4_LIBRARY_PATH` unset.
`L4_BIN check FILE` typechecks, `L4_BIN run FILE` also evaluates every `#EVAL`/`#ASSERT`.
Never write a bare `#EVAL` of an expression that refuses: it prints a Warning. Test a refusal with `#ASSERT REFUSED … BECAUSE "…"`.
Warnings are not acceptable in the deposit: every module must run with no `DiagnosticSeverity_Warning` and no error other than a failed assertion that `NOTES.md` records as meant to fail.

## Rules that matter (all of them apply)

- **Seat.** Every encoding in commons is written from the seat of the individual to whom the law is applied.
  Here that individual is the *reader of an enactment*: someone who has to know what an enactment means for them, when it bound them, what it lets be done to them, whether a notice reached them in time.
  Phrase each exported question as that person would ask it ("Was this regulation already in force on 1 June 2018?", "On what day am I treated as having been served?", "Does `person` in this offence reach my company?", "What is the most I can be punished?").
  Facts are ones that person could state.
  A provision that addresses only an official is encoded for what it means to the person (what may be done, what they must be given).
  Put `@export` and `@desc` on every question, `@desc` on every input.
  Record the seat in `NOTES.md` and `encoding.json`.
- **Encode isomorphically and cite.** One source provision, one recognisable place in the L4, with the source's numbering and an `@ref` on every rule.
  Quote the source on `-- src:N | text` lines made by `python3 -I srcrefs.py quote RAW N [M]` (never retyped) and put locators on the `@ref` as `references/source-locators.md` in `encoding-a-subject` describes; `python3 -I srcrefs.py check --refs RAW FILE…` must report 0 problems.
  `RAW` is the `.txt` named below; a quotation from another deposited version is `-- src:<stem>:N | text` with that version's stem (`<stem>.txt` beside `RAW`).
- **Vintages are inputs, never merged.** Every deposited version is in scope as its own answer.
  Where two versions differ, the date (or the version) is an input and each version answers by its own text.
  A version that is silent answers with silence (`REFUSE`), never with a rule borrowed from another version.
- **Where the sources do not answer: `REFUSE "…"`**, never `FALSE`, `0` or a plausible default.
  A call that depends on "unless a contrary intention appears", "unless the context otherwise requires" or "unless provision is made to the contrary" takes that fact as an input (a `BOOLEAN` with a `@desc`); never decide it yourself.
- **Never claim a rule the text does not contain.** Neither Law has a general rule for counting a period of days, weeks or years, and neither defines "day", "week" or "year" (verified by search on 2026-10-28 in every deposited version: the only day/period words are those you will meet in the commencement provisions and in the 2021 Law's definition of "relevant period" in Article 8(2), which is that Article's own).
  No function of yours may count days, add years, or add calendar months to a date.
  Where a question needs that, it takes the computed day as an input or refuses; say so in `NOTES.md`.
- **A failing assertion is a finding.** Never edit an expected value to match what the code computed.
  Expected values are written by hand from the source text before you look at the code's answer.
  Some tests may be meant to fail (in their own file, with the count named in `check.sh`'s `expected_failed` table and in `NOTES.md`); each is then a finding.
- **Read the diagnostics, not the exit code.** `check.sh` (below) does this for you; report the numbers it prints.
- **Nouns first.** One module of nouns only (`DECLARE`, nothing else), imported by the others, then rules module by module along the Law's own structure, then tests.
  Several modules, not one: nothing over about 600 lines.
- **Keep what another encoding will copy small and self-contained.** The commencement functions and the definitions that other encodings need will be COPIED, by hand, into other encodings (L4 cannot import across folders yet).
  So put them in modules that import only `prelude`, `daydate` and your own nouns module, give every function a name that is unique in your row, and say in a comment above each what it answers and which Article it comes from.
- **Use the house style of the Charities row**: backtick names that read as prose, `GIVEN … GIVETH … MEANS/DECIDE`, `§` sections in the Law's order, `BRANCH IF … OTHERWISE` rather than chains of `ELSE IF`, `YMD y m d` for dates (`IMPORT daydate`), no `ASSUME`.
- **Inputs are values.** An `@export`ed rule's inputs are never functions.
- **Register every fork**: a place where the words allow more than one reading and you take one.
  Each fork gets an id (`I1`, `I2`, … for the 1954 Law; `L1`, `L2`, … for the 2021 Law), the readings with the text that licenses each, the reading taken and why, a discriminating case, and — unless the alternative cannot be expressed — a callable alternative with a test (an enum input on the function, with the default stated).
  A fork the Law's words do not create is not a fork.
  "No ambiguities found" is not an answer; say where you looked.

## Deliverables, all under `DEPOSIT`

1. `.l4` modules with ASCII file names (prefix given below). Nouns first. No module over about 600 lines.
2. Tests modules, with expected values hand-written from the source: both sides of every threshold and every date edge, one case per branch of each rule, the same scenario asserted against each version where the versions differ, and `#ASSERT REFUSED … BECAUSE "…"` for every refusal you wrote.
3. `check.sh`: adapt `check.sh.template` (delete the template when done).
   It must: run every `.l4` module with `L4` (default `L4_BIN` above), `L4_TARGET=unstable` as its default, count per module errors / satisfied / failed / refused / warnings reading the line after every `Message:`; take an `expected_failed` and an `expected_refused` table (zero unless listed); run `srcrefs.py check --refs` over every module against `RAW` and fail on any problem; check that no module starts with `@lang en`; exit 0 only when everything passed.
   It prints the numbers; paste its output into `NOTES.md`.
4. `NOTES.md`, which a reviewer reads first, with these numbered sections:
   (1) what is encoded and what is not, in a paragraph; (2) the seat; (3) the target and the build (no main build has read it); (4) the **coverage table**: one row for EVERY paragraph of every deposited version in scope, keyed by the Article/paragraph number as the source writes it, the vintages in which it exists, its disposition (`encoded` / `inert` — quoted, no operative content, say why / `out-of-scope` with a reason of real length / `refused`), and the module and rule names that carry it; no row may be left `deferred`; (5) the **vintage table** (which text governs on which date, with the amendment that made each change, from the endnotes); (6) the **fork register**; (7) **what the Law does not say** (the list of questions a reader will ask and the Law does not answer, each with its refusal); (8) an **answer table** for the headline questions with the source cited per cell; (9) **what `check.sh` prints**; (10) open questions for a domain expert; (11) **provenance**: your model and effort, what you read, anything you ran that was not in this brief.
5. `encoding.json` (see `references/canon-deposit.md` in `encoding-a-subject` for the fields, and `subjects/je/charities-2014/encodings/legalese-full-2026-10/encoding.json` for an example): status `draft`, `not_reviewed` saying no domain expert has read it against the source, the seat, the scope, the sources and their versions, the target `unstable` and the binary, the checks and their numbers, `expected_red`.
6. `SOURCE-LICENSE.md` (already there).
7. A short `README.md` (what this row is, how to run `check.sh`, the module list in dependency order).

## When you finish

Reply with: the final `check.sh` totals (modules, satisfied, failed with the expected number, refused, warnings, srcrefs lines/runs/locators/problems); the fork register as a list of ids and one-line questions; every place where the text did NOT say what this brief said it says (the brief's claims are claims to verify against the text, not facts: if you find one wrong, say so first, with the line numbers); anything you assumed; anything you ran or read that the brief did not list.
Do not report green for a run whose output you did not read.
