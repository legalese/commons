# Interpretation Act 1965 (Singapore): an L4 encoding with a seat layer

Row `legalese-sonnet-5.5` of the subject `sg/interpretation-act-1965`.
Status: **draft**.
Not reviewed: no domain expert has read this encoding against the text.
Written by Claude Sonnet 5.5 in one run, from the single input text and the files named under "Inputs" below.
Nothing in this folder was copied from, or compared with, any other encoding of this Act or of any other Act.

## The text, and what it is not

The only source is `../../registers/source-bundle/IA1965.txt`, a **plain-text rendering made by a converter script**.
It is **not the official text**, and nothing here is "verified against the official text".
The rendering is of the *informal consolidation, version in force from 5/12/2025* (its page footers say so), taken from Singapore Statutes Online on 2026-09-22 (`../../registers/source-bundle/IA1965.meta.json`).
Its cover says "2020 Revised Edition", but the body is the consolidation as amended since, including Act 19 of 2025 (see the `[Act 19 of 2025 wef 05/12/2025]` notes at ss 41A, 41D and 41E); it is not the 2020 edition as first printed.
Provenance caveat: `../../registers/source-bundle/IA1965.meta.json` and the meta file record `text_sha256 539898ff...`, but `sha256sum ../../registers/source-bundle/IA1965.txt` gives `f7a60e18...`.
The recorded character count (112,979) and word count (15,987) do match the file, so the recorded hash was taken over something other than these exact bytes.
The cause is unknown.
Every quotation in the L4 files is copied out of that file by script (`qx.py`), and `srcrefs.py` re-checks each one against it; neither tool can say whether the converter dropped or changed a word.
The licence terms of the quoted text are in `../../SOURCE-LICENSE.md`; `SOURCE-LICENSE.md` here points at it and does not repeat it.

## Seat

The seat is **a person who has a time limit to meet under a written law (to apply, object, appeal, reply or pay), or who needs to know when something takes effect, asking on which day their period ends and which of their days count.**
Why this seat: the Interpretation Act addresses nobody directly.
It tells everyone who reads any Singapore written law how to read it, and for the people holding a deadline its answer is a date.
Section 50 (computation of time) is the heart of the Act for them, and ss 10, 23, 51, 52, 53 and 2(5) answer the neighbouring questions (when does a law start to bind me, which clock, how soon, may I still ask for more time, when is my posted document treated as served).
The other sections are asked only where they change what that person may do, owe or rely on: a repeal that spares an accrued right (s 16), the maximum penalty (s 41), the process for a Court application (s 41A), the ways to serve a document (s 48A), whether the office may wait for the fee (s 45), and so on.
`sgia-seat.l4` has **31 questions**, each with `@export` and an `@desc` on every input, in section order.
Every input is plain: yes/no, a number, a date, a choice written out in words, or a list of dates.
No question asks the person which reading of a fork to take.
**Deployment note**: the public holidays that bear on a period are a *list of dates* input, so the Interact form must accept a list of dates for that field.
`sgia-seat.l4` restates no rule; it only words the answer.
In round 1 no layer-1 module was changed for it.
The question added in round 2 (the Gazette, s 48(6) and (7)) words the answer of a round-2 rule; see "Changes to existing modules".
Where the Act does not say, the answer is the sentence **"The Interpretation Act does not say."**, which is the explicit not-covered value (a `NOTHING` in layer 1) turned into words, and `sgia-cases-seat.l4` asserts it.

## Inputs

`../../registers/source-bundle/IA1965.txt`, `SOURCES.md`, `STUB-SOURCE-LICENSE.md`, `ENCODING-GUIDE.md`, `COMMONS-CLAUDE.md`, `EXAMPLE-sg-employment-act-seat/ea-seat.l4` (read for its shape only), and the two skills `encoding-a-subject` and `writing-l4-rules`.
The encoder read no other encoding.

## What is encoded, and in which file

Layer 1 follows the text's own structure.
All `.l4` files are flat in this folder and named `sgia-*.l4`.

| file | text | what it holds |
| --- | --- | --- |
| `sgia-interpretation-time.l4` | ss 10, 50, 51, 52, 53, 2(5), and the units that s 2(1) defines | every time rule, in one module that imports only the prelude and `daydate` |
| `sgia-p1-definitions.l4` | s 2(1), the 92 defined terms | generated from a hand-read table by `gen-defs.py`; one `Definition` per entry, with the members the Act names (where the Act prints a list, the phrase as printed and each constituent: see "List members in the s 2(1) table") and what it points at |
| `sgia-p1-other.l4` | s 2(1) chapeau and rules of reading; ss 2(2), 2(2A), 2(3), 2(4), 2(6), 2A | including the twelve construction rows of s 2(3) (row (l) pairs each old expression with its own replacement, as its word "respectively" says) and the criteria for determining death |
| `sgia-p2-written-law.l4` | ss 3 to 9B, 11 to 18 | s 10 is in the time module |
| `sgia-p3-subsidiary.l4` | ss 19 to 26A | |
| `sgia-p4-powers.l4` | ss 27 to 37 | powers, appointments, boards, delegation |
| `sgia-p5-penal-court.l4` | ss 38 to 41E | including the tables of ss 41B, 41D and 41E |
| `sgia-p6-misc.l4` | ss 42 to 49, 54, 55 | ss 50 to 53 are in the time module |
| `sgia-seat.l4`, `sgia-cases-seat.l4` | layer 2 | 31 questions; 161 cases |
| `sgia-tests-*.l4` | tests for each layer-1 module | expected values hand-written from the text |

Scripts and records in this folder (none is part of the law):
`check.sh` and `fetch-main-l4.sh` (the self-check, from the skill);
`srcrefs.py` (checks every `-- src:` quotation and `@ref` locator against the text);
`qx.py` (expands a `--@Q` macro into quotation lines copied from the text plus the `@ref`; each macro was expanded once);
`gen-defs.py` (writes `sgia-p1-definitions.l4` and `sgia-tests-definitions.l4` from a hand-read table of the 92 entries, and with `--verify` ties the table to the text);
`gen-units.py`, `gen-coverage.py` and `coverage-dispositions.py` (the coverage table);
`BRIEF.md` (a copy of the brief) and `PROGRESS.md` (the encoder's working notes).

Not encoded, and why (each is a row in the coverage table):
the title page, contents list, long title and legislative history (inert, reason 1); every marginal heading and Part heading (inert, reason 1); the short title, s 1 (inert, reason 2); the regulation-making power of s 2A(7), the order-making power of s 41A(7) and the regulation-making power of s 48(8) (inert, reason 2), whose products enter as plain inputs; and the three deleted subsections, ss 2(4), 2(6) and 41D(3) (repealed or blank in this text).
Everything else is encoded, including every provision that addresses an official, which is encoded for what it decides.

Borrowed facts, asked as inputs and never guessed: which days are public holidays (s 2(1) "public holiday" points at other written laws); the standard-time offset if the President has notified another (s 51(2)); the day a letter would be delivered in the ordinary course of post (s 2(5)); the "appointed date" of the Electronic Gazette and Legislation Act 2025 (s 48); the prescribed criteria and postgraduate qualifications (s 2A); the classes of application and the courts prescribed under s 41A(7).

## List members in the s 2(1) table

Added in round 2.
In the team lead's triage of the independent test pass, 36 of its 68 gaps were negative or instance-membership questions about the s 2(1) table.
The rule now: where the Act prints a list of alternatives or items in an entry of s 2(1), `what the Act names` holds BOTH the phrase exactly as the Act prints it AND each constituent, and a thing the Act does not list is still not named.
A limb is split out only when it is itself something the term covers or names (a State, a mode of carriage, a kind of writing, a document, a kind of instrument, an office).
A printed item is left whole when its coordination is a title or fixed name, an exception, a restatement of what the context refers to, a qualifier that says where a single thing comes from, a qualifier whose scope the text does not fix, two verbs that say how one kind of thing comes to be, or limbs that share a head so that the second cannot be quoted as a phrase of its own.
The sweep is a script, not a reading: `gen-defs.py` fails, and prints the entry, when a printed item contains a comma, "and", "or", ";" or "/" and is in neither its `EXTEND` table (split) nor its `LEFT` table (left whole, with the reason below).
It also fails when a constituent is not in the entry's own text, when a left item is not one of the entry's printed items, when an extended entry has no unlisted thing to test, or when that unlisted thing is in fact named.
Each extended entry carries, in `sgia-tests-definitions.l4`, one assertion for the printed phrase, one for each constituent, and one `NOT (elem ...)` for a thing the Act does not list: 143 assertions for 21 entries.
"Not named" is not "excluded": the table records what the Act names in defining a term, so `handwriting` not being named under "writing" does not say that handwriting is not writing.

**Entries extended (21).**
A constituent is a phrase that occurs in the entry's own text; the printed phrase is kept as the item before its constituents.

| entry | printed items split | constituents now named | one thing tested as not named |
| --- | --- | --- | --- |
| "animal" | 1 | every kind of vertebrate animal; the young thereof | a plant |
| "common law" | 1 | custom; usage | statute |
| "Commonwealth" | 1 | any colony; protectorate; protected state; any other territory administered by any Commonwealth country | France |
| "Commonwealth country" | 1 | any Commonwealth country; any colony; protectorate; protected state; any other territory administered by the government of any Commonwealth country | France |
| "consular officer" | 1 | consul-general; consul; vice-consul; consular agent | ambassador |
| "export" | 1 | land; sea; air | rail |
| "Government Printer" | 1 | written laws; Bills; the Gazette; documents of the Government; other official documents | newspapers |
| "import" | 1 | land; sea; air | rail |
| "Judge" | 2 | a Supreme Court Judge; a Judicial Commissioner; a Senior Judge; the General Division of the High Court; Appellate Division of the High Court; the Court of Appeal; an International Judge; the Singapore International Commercial Court; the Appellate Division of the High Court; the Court of Appeal | a District Judge |
| "Malaya" | 1 | Singapore; the States of Malaya | Sabah |
| "oath" | 2 | affirmation; declaration; affirm; declare | promise |
| "person" | 1 | any company; association; body of persons | a trust |
| "Singapore" | 1 | the Island of Singapore; all islands and places which on 2 June 1959 were administered as part of Singapore; all territorial waters adjacent thereto | Johore |
| "States of Malaya" | 1 | Johore; Kedah; Kelantan; Malacca; Negri Sembilan; Pahang; Penang; Perak; Perlis; Selangor; Trengganu | Sabah |
| "statutory declaration" | 2 | a justice of the peace; notary public; other person having authority therein under any law for the time being in force to take or receive a declaration; a consul; vice-consul; any person having authority under any law for the time being in force to take or receive a declaration | a police officer |
| "subsidiary legislation" | 1 | order in council; proclamation; rule; regulation; order; notification; by-law; other instrument made under any Act, Ordinance or other lawful authority and having legislative effect | a circular |
| "Supreme Court Judge" | 1 | the Chief Justice; a Justice of the Court of Appeal; a Judge of the Appellate Division; a Judge of the High Court | a District Judge |
| "United Kingdom" | 1 | Great Britain; Northern Ireland | Scotland |
| "writing" | 1 | printing; lithography; typewriting; photography; other modes of representing or reproducing words or figures in visible form | handwriting |
| "written law" | 2 | the Constitution; all previous Constitutions having application to Singapore; all Acts; Ordinances; enactments by whatever name called; subsidiary legislation made thereunder | a judgment |
| "Yang di-Pertuan Agong" | 2 | the Yang di-Pertuan Agong; Supreme Head of Malaysia; the Deputy Supreme Head of Malaysia; a Ruler of a Malay State | a Menteri Besar |

**Entries checked and left whole (21 printed items).**
"consular officer" and "statutory declaration" appear in both lists: one of their printed items is split and another is left.

| entry | printed item (its first words) | why it is left whole |
| --- | --- | --- |
| "Act" | Ordinance or Act of Singapore or Malaysia | the text does not fix whether "of Singapore or Malaysia having the force of law in Singapore" qualifies "Ordinance" as well as "Act"; splitting would settle that silently |
| "advocate" | advocate and solicitor of the Supreme | "advocate and solicitor" is one title |
| "Attorney-General" | a Deputy Attorney-General so assigned | "function, power or duty" restates the function the context is about; it is not a list of things named |
| "citizen of Singapore" | any person who, under the provisions | the commas set off a parenthesis; there is no list |
| "consular officer" | any person for the time being authorised | the offices it lists are the offices of the first item, already split |
| "contravene" | a failure to comply with a requirement | the thing named is the failure; "requirement or condition" is what it is a failure to comply with |
| "Criminal Procedure Rules" | the Criminal Procedure Rules made under | the "and" joins the laws the rules are made under, inside one description; the limbs are laws, not rules |
| "Crown Agents" | the persons for the time being acting | "Overseas Governments and Administrations" is part of a title |
| "Family Justice Rules" | the Family Justice Rules made under | as Criminal Procedure Rules |
| "immovable property" | things attached to the earth or permanently | the two limbs share the head "things", so the second ("permanently fastened to anything attached to the earth") cannot be quoted as a phrase of its own |
| "Malaysian citizen" | any person who is a citizen of Malaysia | the limbs (a law, an instrument) are the source of the citizenship, not kinds of citizen |
| "master" | any person, except a pilot or harbour | "except a pilot or harbour master" is an exception, not an item named; the table records what the Act names, not what it leaves out |
| "military" | the digital and intelligence service | one name |
| "Minister" | the Minister for the time being charged | "department or subject" restates what the context refers to |
| "monogamous marriage" | a marriage which is recognised by the law | "one man and one woman" is part of the definition of the one thing |
| "Ordinance" | any Ordinance of the Colony of Singapore or | the limbs (the Colony, the State) made the Ordinance; they are not kinds of Ordinance |
| "prescribed" | prescribed by the Act in which | the limbs (the Act, subsidiary legislation) are what does the prescribing, not kinds of prescribed thing |
| "public holiday" | any day which is declared to be or proclaimed | "declared" and "proclaimed" are two ways one kind of day comes to be a public holiday; no second thing is named |
| "Rules of Court" | the Rules of Court made under | as Criminal Procedure Rules |
| "ship" | every description of vessel used in navigation | "oars or paddles" is a negative qualifier (what propels it), not something named |
| "statutory declaration" | a declaration made under the Oaths | "Oaths and Declarations" is part of the title of an Act |

## The worked cases

Expected values were written from the text and a calendar (the system's `date -j`), then run.
"Silent" means the Act has no rule, the encoding returns its explicit not-covered value, and a test asserts it.
Where the Act is silent on the *last day* but the person has worked one out, the seat's second question applies s 50(b) to the day they supply; that second column is what the Act then decides.

| case | what the Act decides about the last day | then s 50(b), on the day the person works out (weekday by calendar) |
| --- | --- | --- |
| 3 years from 2025-07-16 | silent: s 2(1) defines "year" (a year reckoned according to the Gregorian calendar, lines 575-576) and nothing else | if worked out as 2028-07-16 (Sunday): the period includes Monday 2028-07-17 (s 50(b)) |
| 5 years from 2025-01-15 | silent (same) | if worked out as 2030-01-15 (Tuesday): unchanged |
| 5 years from 2025-09-01 | silent (same) | if worked out as 2030-09-01 (Sunday): includes Monday 2030-09-02; Tuesday 2030-09-03 if the 2nd is a public holiday |
| 30 days from 2026-01-01 | s 50(a): the day of the event is left out, so day 1 is 2026-01-02 and the last day is **2026-01-31** | 2026-01-31 is a Saturday, not an excluded day (s 50(b) names Sundays and public holidays only): unchanged. If 31 January were a public holiday: 1 February is a Sunday, so the period would include Monday 2026-02-02 |
| 2 months from 2025-12-31 | silent: s 2(1) defines "month" as "calendar month" (line 406) and gives no rule for a start on the 31st | if worked out as 2026-02-28 (Saturday): unchanged |
| 1 month from 2024-01-31 | silent (same) | if worked out as 2024-02-29 (Thursday): unchanged |
| 1 year from 2024-02-29 | silent (same) | if worked out as 2025-02-28 (Friday): unchanged |

All seven rows are asserted: the silence in `sgia-tests-time.l4` and `sgia-cases-seat.l4`, the s 50(b) outcomes in both.
Which day a person *should* work out for the months and years is not decided here; a library that counts months will clamp 2024-01-31 plus one month to 2024-02-29, and finding 4 records that this is the library's habit and not the Act's.

## Jural relations

Hohfeld positions: right and duty, privilege and no-right, power and liability, immunity and disability.
A provision that creates one has its own row, with the party who holds it, the party who bears the correlative, and the L4 rule that encodes it.
A provision that creates none (a definition, a counting rule, a rule of reading, a rule of evidence) is listed once as `none`; adjacent provisions of that kind share a row.
Most of this Act creates no relation: it defines, counts, directs how to read, or says what is taken notice of.
Where the Act names no right-holder for a duty, the row says so and does not supply one.

| provision | relation | holder; counterparty | note | L4 rule that encodes it |
| --- | --- | --- | --- | --- |
| s 1 | none |  | short title | none |
| s 2(1) chapeau and the 92 defined terms | none |  | definitions | none |
| s 2(1) rules of reading (masculine, singular and plural) | none |  | rules of reading | none |
| s 2(2), 2(2A) | none |  | other forms of a defined word; a written law's own definition prevails unless the context otherwise requires | none |
| s 2(3) | none |  | twelve construction rows for laws enacted before 28 December 1965 | none |
| s 2(4), 2(6) | none |  | deleted | none |
| s 2(5) | none |  | a deeming rule: it fixes when service by post is treated as done, and creates no new duty | none |
| s 2A(1) | none |  | when a person has died | none |
| s 2A(2) to (6) | duty | whoever determines or certifies death; no right-holder is named | the determination "must be" made by the standards and certified in the prescribed form | `what the determination of death requires`; `the certificate meets section 2A(4)`; `the certificate meets section 2A(5)`; `the certificate meets section 2A(6)` |
| s 2A(7) | power / liability | Minister; persons the regulations bind | regulation-making power (inert, machinery) | (machinery, not encoded) |
| s 2A(8), 2A(9) | none |  | savings for the presumption of death and for a body not found; who counts as a medical practitioner | none |
| ss 3, 4, 5, 6 | none |  | public Acts; division into sections; Schedules; judicial notice of divisions | none |
| s 7 | immunity / disability | the user of a form with a slight deviation; anyone who would treat it as invalid | slight deviations "do not invalidate" | `a deviation from a prescribed form invalidates it` |
| ss 7A, 8, 9, 9A, 9B, 10, 11 | none |  | examples; how a written law may be cited; where a bare reference points; purposive interpretation; style changes; the moment of commencement; subsidiary legislation stays in force | none |
| ss 12, 13, 14, 15 | none |  | repeal of repealing laws; repeal of amended law; the repealed law remains in force until the substitute operates; references to amended and re-enacted provisions | none |
| s 16(1) | immunity / disability | a holder of an accrued right, privilege, obligation or liability; the repeal | the repeal "does not" affect them | `the repeal does this` |
| s 16(1)(e) | power / liability | the person who may institute, continue or enforce; the counterparty | may go on "as if the repealing law had not been passed" | `it may be instituted, continued or enforced, or the penalty imposed, as if the repealing law had not been passed` |
| s 16(2) to (4), s 17 | none |  | what counts as a repeal; amending Act read as one with the amended Act | none |
| s 18 | power / liability | a party to a proceeding begun before the law expired; the other party | the proceeding "may be continued" | `the proceeding may be continued as if the written law continued in force` |
| s 19(a), (a)(i), (a)(ii) | power / liability | the authority making subsidiary legislation; those it binds | amend, vary, rescind or revoke; successor authority | `subsidiary legislation may be amended, varied, rescinded or revoked at any time`; `the power to fix the date includes the power to amend, revoke or suspend the subsidiary legislation fixing it`; `the replacing authority may exercise the power over matters within its jurisdiction as if it were the original authority` |
| s 19(b), (c) | none |  | the general power is not narrowed; inconsistency with an Act | none |
| s 20(a), (b) | power / liability | the maker of subsidiary legislation; those it binds | includes penalties up to $2,000 or 12 months or both, forms, electronic delivery, fees and interest | `authority to make subsidiary legislation also includes`; `the penalty is within the limits of section 20(a)(i)` |
| s 20(c), 21 | none |  | references to written laws include subsidiary legislation; defined terms carry over | none |
| s 22 | power / liability | the person with the power; those affected | anticipatory exercise | `the power may be exercised after the passing of the Act so as to take effect at any time after it` |
| s 23(1)(a) | duty | the maker; no right-holder named | subsidiary legislation "must be published in the Gazette" | `subsidiary legislation must be published in the Gazette` |
| s 23(1)(b) | none |  | the day it takes effect | none |
| s 23(2) | disability | the maker | cannot operate earlier than the Act's commencement or the authority's establishment | `the subsidiary legislation may be made to operate retrospectively to that date` |
| ss 24, 25, 26, 26A | none |  | judicial notice; read as one; acts done under; references to an Act | none |
| s 27(1) | power | the holder of a power; no counterparty named | may be exercised "from time to time as occasion requires" | `the power may be exercised and the duty must be performed from time to time as occasion requires` |
| s 27(2) | power | the office-holder for the time being, or one duly appointed to act |  | `the person may exercise the power or must perform the duty` |
| s 27(3) | power | the holder of a power to make subsidiary legislation, issue an order or act | includes amending, varying, rescinding, revoking, suspending | `the power includes this, exercisable in like manner and subject to the like consent and conditions` |
| s 28 | power / liability | the appointing authority; the appointee | includes dismissal and suspension | `the power to appoint includes this`; `the power of dismissal is exercisable` |
| s 29 | power / liability | the person with the power; those affected | enabling words; licensing; conditions | `the power is understood to be also conferred`; `the power includes this, without limiting section 29(1)` |
| ss 30, 32 | power / liability | the appointing authority; the appointee | appointments by name or office; retrospective effect | `the appointment is made in a way section 30 allows`; `the appointment may be made with retrospective effect to that date`; `the day from which the appointment may be declared to have effect` |
| s 31 | none |  | an official designation includes the officer executing the duties | none |
| s 32A(1), (2)(b), (3) | power | a statutory body of 3 or more; its chairperson | a majority acts for the body; the chairperson has a casting vote | `the power may be exercised or the function or duty performed by a majority of those persons`; `the act or thing is regarded as done by the body`; `the chairperson or other member presiding has a casting as well as a deliberative vote` |
| s 32A(2)(a), (4), (5) | none |  | quorum; the section yields to a contrary written law; the meaning of statutory body | none |
| s 33 | immunity / disability | the board; anyone who would challenge its powers | not affected by a vacancy or a defect | `the powers of the body are affected` |
| s 33A | privilege / no-right | a statutory body; those who would object | may invest, subject to directions | `the body may invest the moneys in the manner it thinks fit, and engage in financial activity or arrangements to manage or hedge risk from the investment` |
| ss 34, 35, 35A(2), 37 | none |  | how an order or document is signified or signed | none |
| s 35A(1) | disability | a statutory body | its power to delegate does not reach making subsidiary legislation | `the power to delegate extends to making subsidiary legislation` |
| s 36 | power / liability | the Minister; the delegate | delegation by order, with limits | `the delegation is permitted by section 36`; `the delegate may exercise the function based on the delegate's own opinion, belief or state of mind` |
| s 38 | duty | everyone; no right-holder named | an attempt to commit the offence is an offence | `an attempt to commit the offence is an offence against the provision, punishable as if the offence itself had been committed` |
| s 39 | right / duty | the person injured; the offender | liability for damages survives the penalty | `the penalty relieves the person from liability to answer for damages to a person injured` |
| s 40 | immunity / disability | the offender; the prosecutor | not liable to be punished twice for the same offence | `the offender is liable to be punished twice for the same offence` |
| s 41 | immunity / disability | the offender; the court | the penalty is a maximum | `the most the offence is punishable by on conviction`; `the penalty imposed is within what section 41 allows` |
| s 41A(1) to (6) | duty | the applicant; no right-holder named | an application "must be made" by originating application or summons; (2)(b) gives the Court a power to give directions | `the process the application must be made by`; `the application must be made in accordance with the Rules of Court`; `the Court may give the parties directions the Court thinks just and expedient to facilitate the progress of the application` |
| ss 41B, 41C, 41D, 41E | none |  | renaming and reading of old expressions | none |
| s 42 | power / liability | the appointing authority; the public officer appointed by designation |  | `it is lawful to appoint the public officer by his or her official designation` |
| ss 43, 44 | none |  | prima facie evidence of signature; public officers | none |
| s 45(1) | privilege / no-right | the office; the person who wants the thing done | may decline until the fee (or the estimate) is paid | `the person, officer, department or authority may decline to do the thing` |
| s 45(2) | right / duty | the office or the payer, whichever is owed | adjust by further payment or refund | `the adjustment after the thing has been done` |
| s 46 | power / liability | the Minister; those who pay | fees by order; reduce, remit or refund | `the Minister may by order published in the Gazette provide for fees or charges, charges and penalties for late payment, and interest`; `the Minister may by order reduce, remit or refund it in whole or in part in the circumstances of a particular case` |
| s 47 | power / liability | the person appointed to the office; the other party | proceedings do not abate and may be carried on | `the proceedings may be carried on by or against the person appointed to perform the duties of the office` |
| s 48 | none |  | the Gazette: form, date, evidence; (8) is a regulation-making power (inert, machinery) | none |
| s 48A(1) | privilege / no-right | the person serving; the person served | may serve in the listed ways; (2) saves other ways | `the document may be served this way` |
| s 49 | none |  | distance is measured in a straight line | none |
| s 50(a), (b), (d) | none |  | counting rules | none |
| s 50(c) | immunity / disability | the person who acts on the next day that is not an excluded day; anyone who would call the act late | the act "is considered as done in due time" | `section 50(c) treats the act as done in due time`; `the last day for an act directed for a day` |
| s 51 | none |  | the clock | none |
| s 52 | duty | whoever must do the thing; no right-holder named | "with all convenient speed" | `the time for doing a thing` |
| s 53 | power / liability | the court or authority; the applicant | the power to extend may be exercised after the time has run out | `the power to extend may be exercised after the time has run out` |
| s 54 | immunity | the Government | its rights are not affected unless the Act says so or necessarily implies it | `the Act affects the rights of the Government` |
| s 55 | none |  | the Act binds the Government | none |

## Fork register

A fork is a place where the text can be read two or more ways with different outcomes.
Each entry gives the readings, the one taken, the lines that license each, and where the chosen reading lives.
Line numbers are lines of `../../registers/source-bundle/IA1965.txt`.

**F1. Does a period "from" a day leave that day out? (s 50(a), lines 2149-2151.)**
Reading A (taken): a period of days "from the happening of an event or the doing of any act or thing" is "exclusive of the day on which the event happens or the act or thing is done", so the seat asks for the day of the event or act and counts from the next day.
Reading B: a period running from a bare calendar date that is neither an event nor an act is outside (a) and the Act is silent.
The text for A is 2149-2151.
The text for B is that the words are "event" and "act or thing", not "date".
Chosen rule: `the first day of a period of days from the event`, used by `the last day of a period`.
The seat does not ask for a bare date; it asks for the day the event happened or the act was done.

**F2. Does a period "after" an event count the same way? (s 50(a), lines 2146-2151.)**
Reading A: the chapeau, "in computing time for the purposes of any written law" (2146-2147), covers every period running from an event, so "after" gets the same last day as "from".
Reading B (taken): paragraph (a) names only "from" (2149), so "after" is not covered.
Chosen: B. `the last day of a period` returns `NOTHING` for `After`, and the seat says "The Interpretation Act does not say."
Asserted in `sgia-tests-time.l4` and `sgia-cases-seat.l4`.
If A is wanted instead, the change is one branch in `the last day of a period`.

**F3. Is the last day inside the period? (s 50(a), (b), lines 2149-2156.)**
Reading A (taken): the last day is the Nth day counted from the day after the event, and it is inside the period, because (b) says that when it is an excluded day "the period includes the next following day".
Reading B: the period ends at the start of the last day.
The text for A is the verb "includes" in 2155; no text licenses B.

**F4. Does s 50(b) reach periods in weeks, months and years, or only periods of days? (lines 2146-2156.)**
Reading A (taken): (b) speaks of "the last day of the period" and the chapeau speaks of "computing time" generally, so it reaches every period.
Reading B: (b) belongs to the "period of days" of (a).
Both are coded: `the last day of the period once section 50(b) is applied` (A) and `...if it reaches periods of days only` (B); both are tested.
They differ only when the person has worked out a last day in weeks, months or years that is a Sunday or public holiday (for example Sunday 2028-07-16: A gives Monday 2028-07-17, B leaves it).
The public wrapper and the seat use A.
Round 2: the fix list named this fork again and nothing in the reading changed; the quotation under the rule that codes B was re-cut so that `srcrefs.py --strict` passes (see "Changes to existing modules").

**F5. Is a day on which an office is closed, or a Saturday, an excluded day? (s 50(b), lines 2153-2156.)**
Reading A (taken): no.
Section 50 defines "excluded days" as exactly "a Sunday or a public holiday", and the words "Saturday" and "closed" do not occur anywhere in the text (searched).
Reading B: a closed office counts, by analogy with a public holiday.
No text licenses B.
The encoding therefore leaves a Saturday, and an office-closure day, as ordinary days; the person who must add a day for closure has to find another law.

**F6. s 23(2), "not being a date earlier than the commencement of the Act or the establishment of the authority" (lines 1271-1274).**
Reading A (taken): both limits bind, so the date may be no earlier than the Act's commencement and, when the authority has an establishment date, no earlier than that either.
Reading B: "or" offers a choice of which limit applies.
Text for A: "not being a date earlier than X or Y" denies both.
Chosen rule: `the subsidiary legislation may be made to operate retrospectively to that date`.
Round 2: the fix list named this fork again and nothing in the reading changed.
Compare F22 (ss 30(3) and 32), which use similar words with one limit each.

**F7. "2 medical practitioners" (ss 2A(4), (5), (6), lines 687-748).**
Reading A (taken): at least 2.
Reading B: exactly 2.
Text: the Act gives the number 2 and no ceiling; a certificate signed by three would meet its purpose.

**F8. "subject to subsection (5)" (s 2A(2), line 679) and "subject to subsections (4) and (6)" (s 2A(3), line 684).**
Reading A (taken): the ordinary standards of medical practice (2) and the prescribed criteria (3) still apply when (5) or (4) and (6) add requirements.
Reading B: the later subsection replaces the earlier one.
Chosen: `what the determination of death requires` sets both the standards flag and the extra requirements.

**F9. s 2(3)(e), "references to the Chief Justice or to any court, judge or magistrate of the Malayan Union ..." (lines 617-622).**
The row's construed-as words are "the Chief Justice or the corresponding court, judge or magistrate of Malaysia or the territories comprised therein", and the row carries the flag `as the case may require` (the Act's closing words).
Reading A (taken): return the Act's words and the flag as stated and leave "as the case may require" to the reader.
Reading B: resolve which alternative applies to which old expression.
Text: the Act does not say which; so no rule is invented.

**F10. s 14, after the substituted provision comes into operation (lines 1040-1043).**
The Act says the repealed written law "remains in force until the substituted provision comes into operation".
It does not say what the repealed law is after that moment.
Chosen: the rule returns `JUST TRUE` before the moment and `NOTHING` after it; the seat says "The Interpretation Act does not say."
Reading B (not taken): it is no longer in force.
That reading is natural but is not the Act's text.
Text for A: the section's only operative words are "remains in force until the substituted provision comes into operation"; they say how long the repealed law is kept alive and not what it is afterwards.
Text for B: "until" marks an end, and the first limb says the written law "repeals" the former law, so once the substitute operates the repeal is complete.
Round 2: the fix list named this fork again; the reading is unchanged, and a test asserts `NOTHING` once the substitute operates.

**F11. s 50(d), "any time not exceeding 6 days" (lines 2167-2170).**
Reading A (taken): the number of days the law states, 1 to 6.
Reading B: the length once excluded days are removed.
Under A, 6 days from Monday 2026-01-05 skip Sunday 11 January and end on Monday 12 January; a stated period of 7 days is counted straight through.
Consequence in finding 8: a longer period can end before a shorter one.

**F12. Service by post: s 2(5) and s 48A (lines 657-663, 2095-2127).**
Both speak of service by post.
Reading A (taken): they operate side by side: s 48A says *how and where* one may serve; s 2(5), when an Act authorises service by post, says that properly addressing, prepaying and posting *is* service and when it is deemed effected.
Reading B: s 48A displaces s 2(5) where both apply.
The Act does not say which prevails.
The seat has a separate question for each.

**F13. s 32A(1), "a majority of those persons" (lines 1414-1418).**
Reading A (taken): more than half of all the persons the body consists of.
Reading B: more than half of those present or in office.
Text: "those persons" refers back to "a statutory body consisting of 3 or more persons"; s 32A(2)(b) is the separate rule for those present at a meeting.
F23 is the next question: what the two rules do together.

**F14. s 2(1), the masculine and the feminine (lines 554-555).**
The Act says words importing the masculine gender include females.
It says nothing about words importing the feminine gender.
Chosen: `section 2(1) extends a word importing the feminine gender to` returns `NOTHING` for every input; the singular and plural rule is two-way as the Act says.

**F15. s 10(1), how the day of commencement is fixed (lines 994-1004).**
Two cases are named: a day "specified by the written law or by a notification made under" it, and "the date of its publication in the Gazette"; both operate "on the expiration of the previous day".
A law that fixes its day in neither way is not covered: `the moment a written law comes into operation` returns `NOTHING`.
The moment is taken as the first instant of that day on the standard-time clock.

**F16. s 20(a)(i), "a fine not exceeding $2,000 or with imprisonment for a term not exceeding 12 months or both" (lines 1183-1186).**
Reading A (taken): each limit applies to its own penalty, and both may be imposed together.
Reading B: an aggregate limit.
Text: "or both" is there to say that both may be combined.

**F17. s 45(1), (a) and (b) joined by "and" (lines 1979-1991).**
Reading A (taken): where the precise amount cannot be ascertained until the thing is done, the estimate stands in for the fee in (a): the office may decline until the estimate is paid, and may not decline once it is.
Reading B: both must be paid, which would be impossible when the amount is unknown.
Chosen rule: `the person, officer, department or authority may decline to do the thing`.

**F18. ss 41D and 41E together (lines 1829-1916).**
Section 41D(1) is "subject to the exceptions in subsection (2) and section 41E".
Reading A (taken): 41E displaces 41D(1) for the matters 41E lists, in the Singapore International Commercial Court; 41D(1) applies to every other matter, including a matter 41E does not list that is raised in that Court; 41D(2) reverses only a reference to a second-column matter in the Family proceedings it names.
Reading B: in the SICC 41D does not apply at all.
Chosen rule: `the reference is construed as a reference to`.
Asserted: SICC with "Plaintiff" gives "Claimant".

**F19. s 36(1) to (3), "in accordance with this section" (lines 1539-1549).**
Subsection (1) lets the responsible Minister delegate the function "in accordance with this section".
Subsection (2) names a Minister, Minister of State or Parliamentary Secretary assigned by the Prime Minister to assist the responsible Minister, with the Prime Minister's approval and unless an Act expressly provides otherwise.
Subsection (3) names a public body or a public officer, unless the contrary intention appears in an Act.
Reading A (taken): those are the only delegates the section provides for, and a delegation to anyone else is not covered by s 36, so the rule returns `NOTHING` and not `JUST FALSE`.
Text for A: (2) and (3) say what "may be delegated to" the named delegates and never say "only"; the section does not say that a delegation outside it is forbidden, and another law may allow it.
Reading B: "in accordance with this section" makes the two lists exhaustive, so the Act says no to anyone else (`JUST FALSE`).
Text for B: (1) permits delegation only "in accordance with this section".
Chosen rule: `the delegation is permitted by section 36`, with the choice `someone else`.
Asserted: `someone else` gives `NOTHING`, as does a delegate of (2) when an Act expressly provides otherwise and a delegate of (3) when a contrary intention appears (`sgia-tests-p4.l4`).

**F20. s 46(2), the parenthesis "(not being any fee, charge, penalty or interest which is regulated by Rules of Court)" (lines 2024-2025).**
The Minister may by order reduce, remit or refund a fee, charge, penalty or interest payable to the Government or a public body, "not being" one that Rules of Court regulate.
Reading A (taken): the parenthesis describes the class of items the power reaches; for an item that Rules of Court regulate the section grants no power and says nothing more, so the rule returns `NOTHING` (the Rules of Court, or another law, may provide for reduction).
Text for A: "not being" is a description of the subject matter, not an imperative such as "must not" or "does not apply to".
Reading B: the parenthesis forbids it, so the Act says the Minister may not reduce, remit or refund such an item (`JUST FALSE`).
Text for B: the parenthesis is the only thing that sets such items apart, and its only effect is to take them out of the power.
Chosen rule: `the Minister may by order reduce, remit or refund it in whole or in part in the circumstances of a particular case`.
Whether an item is "regulated by Rules of Court" is a plain yes/no input; the Act does not say what "regulated" covers.
Asserted: an item regulated by Rules of Court gives `NOTHING` (`sgia-tests-p6.l4`).

**F21. s 41A(6)(e), "such other court as may be prescribed" (line 1769).**
Reading A (taken): the list in (a) to (d) is open at its end, so a court counts if it is one of those or has been prescribed under s 41A(7); the prescribing order is not among the inputs.
A court the person says is prescribed gives `JUST TRUE` (`another court prescribed under section 41A(7)`), and any other court gives `NOTHING` (`some other court`), because the encoding cannot see whether an order exists.
Text for A: (e) itself, which would have nothing to say under B.
Reading B: the list is closed and every other court is not a Court for s 41A (`JUST FALSE`).
Text for B: none beyond the word "means", which closes a list that (e) has already opened.
Chosen rule: `is a Court for section 41A`.
Asserted: both choices (`sgia-tests-p5.l4`).

**F22. s 32 against s 30(3) (lines 1387-1389 and 1406-1410).**
Both let an appointment take effect from an earlier day.
Section 30(3): "Any such appointment" (an appointment under s 30(1), by name or by office) "may be made with retrospective effect to any date not being a date earlier than the commencement of the Act under which the appointment is made".
Section 32: "Any appointment may be declared to have effect as from the date upon which the appointee commenced to exercise the powers and discharge the duties of his or her appointment, not being a date earlier than the date of the commencement of the written law under which the appointment is made".
They differ in the date (any date, against the day the appointee began to act) and in the limit (the Act, against the written law).
Reading A (taken): they are separate rules; an s 30 appointment may take effect from any date not earlier than the Act's commencement, and s 32 adds the day the appointee began to act, for any appointment, if that day is not earlier than the commencement of the written law.
Text for A: s 30(3) says "any date", and s 32 says "may be declared", not "only".
Reading B: s 32 narrows s 30(3), so no appointment, under s 30 or not, may be given effect from any date other than the day the appointee began to act.
Text for B: s 32 says "Any appointment", which includes an appointment under s 30.
Chosen rules: `the appointment may be made with retrospective effect to that date` (s 30(3), a yes/no) and `the day from which the appointment may be declared to have effect` (s 32, a day or `NOTHING`); nothing combines them, and the two limits are separate inputs.
Asserted: each rule on its own (`sgia-tests-p4.l4`).

**F23. s 32A(1) against s 32A(2)(b) (lines 1414-1417 and 1432-1434).**
F13 settles what "those persons" means; this fork is about the two rules together.
Subsection (1): a power or duty "may be exercised" or "performed" "by a majority of those persons", the persons the body consists of.
Subsection (2)(b): an act done "by a majority of the members of the body present at the meeting, if those members constitute a quorum, is to be regarded as having been done by the body".
On the same facts they differ: a body of 5, three present who are a quorum, two of the three agree; (2)(b) says the act is the body's and (1) says two of five is not a majority.
Reading A (taken): they are two rules, the encoding answers each on its own terms, and the Act does not say which prevails when both are asked of the same act, so no rule combines them.
Text for A: both are permissions ("may be exercised", "is to be regarded as"), and neither says "only" or "subject to subsection (1)" or "subject to subsection (2)".
Reading B: (2)(b) governs acts done at a meeting and (1) governs the rest, so there is no clash.
Reading C: (1) is a floor, so an act that passes (2)(b) but fails (1) is not the body's.
Text for B and C: none; subsection (4) makes the section "subject to any provision to the contrary in any written law" and says nothing about (1) and (2)(b) between themselves.
Chosen rules: `the power may be exercised or the function or duty performed by a majority of those persons` and `the act or thing is regarded as done by the body`.
Asserted on the 5, 3, 2 facts above: `JUST FALSE` from the first and `JUST TRUE` from the second (`sgia-tests-p4.l4`).

**F24. s 2(1) "written law", "for the time being in force in Singapore" (lines 563-567).**
The definition is "the Constitution and all previous Constitutions having application to Singapore and all Acts, Ordinances and enactments by whatever name called and subsidiary legislation made thereunder for the time being in force in Singapore".
Reading A: "for the time being in force in Singapore" qualifies every limb, including "all previous Constitutions", so a previous Constitution is written law only while it is in force.
Text for A: one sentence with one qualifier at its end.
Reading B: it qualifies only the Acts, Ordinances, enactments and subsidiary legislation, so a previous Constitution having application to Singapore is written law whether or not it is in force now.
Text for B: otherwise "previous" leaves the first limb nearly empty, since a previous Constitution is usually one no longer in force.
Taken: neither.
No rule answers "is this instrument a written law": the table (`s 2(1) definition 89: written law`) lists the limbs the Act names, with the qualifier inside the phrase as printed, and applies it to no limb.
A question of that form is not covered by this encoding, it is not in the seat, and a function that answered it would have to rule on this fork first.

**F25. s 9A(3), "includes" (lines 932-958).**
Subsection (3) says that the material that may be considered under (2) "includes" six kinds it names, "Without limiting subsection (2)".
Reading A (taken): the list is not exhaustive, so a newspaper article, say, is neither listed nor excluded by (3), and `section 9A(3) names the material as material that may be considered` returns `NOTHING` for `any other material`.
Whether such material may be considered is for (2): any material not forming part of the written law "that is capable of assisting" may be considered for the purposes in (a) and (b), subject to (4); that rule takes "capable of assisting" as a plain yes/no input.
Text for A: "includes", and "Without limiting subsection (2)".
Reading B: the list is exhaustive and other material is excluded (`JUST FALSE`).
Text for B: none.
Asserted: `any other material` gives `NOTHING` (`sgia-tests-p2.l4`).

**F26. s 20(c) against s 26A, and ss 29 and 37, which print no proviso (lines 1224-1225, 1303-1305, 1354-1370, 1611-1616).**
Section 26A says "Unless the contrary intention appears, a reference in any written law to an Act is to be construed so as to include a reference to any subsidiary legislation made under that Act".
Section 20(c) says "a reference in a written law to another written law includes a reference to any subsidiary legislation made thereunder", with no proviso, and an Act is a written law.
Section 36(3) prints a proviso ("Unless the contrary intention appears in any Act").
None of "contrary intention", "expressly provides otherwise", "otherwise expressly provided" or "to the contrary" occurs in ss 20, 29 or 37 (searched).
Reading A (taken): each section is coded as printed; s 20(c), s 29 and s 37 answer on the text alone, with no contrary-intention input, and s 26A has the input and returns `NOTHING` when it is true.
So for a reference to an Act in a law that shows a contrary intention, s 20(c) says the reference includes subsidiary legislation (`TRUE`) and s 26A says nothing (`NOTHING`); the Act does not say which prevails.
Text for A: the Act writes the proviso where it means it (ss 26A and 36(3)) and does not write it in ss 20, 29 and 37.
Reading B: a contrary intention in the law being read displaces every rule of the Act whether or not the rule says so, so s 20(c), s 29 and s 37 would also return `NOTHING` when one appears.
Text for B: none directly; the argument is that s 26A would be pointless if s 20(c) already did its work without a proviso.
Chosen rules: `the reference includes any subsidiary legislation made under the other written law` (s 20(c)), `the reference includes subsidiary legislation made under that Act` (s 26A), `the power is understood to be also conferred` and `the power includes this, without limiting section 29(1)` (s 29), and `the requirement that a document be under the hand of or countersigned by a Minister is met` (s 37).
Asserted: s 20(c) and s 26A each on its own (`sgia-tests-p3.l4`).

## What the text turns out to say

Numbered findings.
A finding ends "Asserted." when a case asserts it.

1. **Text and edition.** The text is a converter rendering of the informal consolidation in force from 5/12/2025, with a 2020 Revised Edition cover; the recorded hash of the file does not match the file (see the first section).
2. **The contrary-intention policy.** Where the Act says "unless the contrary intention appears" or "unless the context otherwise requires", it gives the default and not what replaces it. Every such rule takes a plain yes/no input and answers `NOTHING` when it is true, so the encoding never invents a replacement. Asserted.
3. **No counting rule for weeks, months or years.** The Act defines "month" as "calendar month" (line 406) and "year" as a year reckoned according to the Gregorian calendar (575-576). It does not define "day" or "week", and it says nothing about a start on the 31st, a start on 29 February, or a month that lacks the start day's number. The last day of 3 years from 2025-07-16, 5 years from 2025-01-15 or 2025-09-01, 2 months from 2025-12-31, 1 month from 2024-01-31 and 1 year from 2024-02-29 is therefore not given by the Act. Asserted.
4. **The library clamps; the Act does not say to.** `daydate`'s `add months` and `add years` return the last day of a shorter month (2024-01-31 plus one month is 2024-02-29; 2025-12-31 plus two months is 2026-02-28; 2024-02-29 plus one year is 2025-02-28). The Act does not authorise or forbid that, so no rule of the encoding uses those functions. Asserted, as library behaviour.
5. **"After" is not covered.** Section 50(a) names "from"; a period "after" an event gets no last day from the Act. Asserted.
6. **Excluded days are Sundays and public holidays only.** A Saturday is a day like any other, and a day on which an office is closed is not defined anywhere in the text. 30 days from 2026-01-01 end on Saturday 2026-01-31. Asserted.
7. **Public holidays are a borrowed fact.** s 2(1) "public holiday" means a day declared or proclaimed a public holiday, or observed as one under any written law. The Act has no list, so the seat takes the dates from the person. Asserted.
8. **A longer period can end before a shorter one.** With Wednesday 2026-01-07 a public holiday, 6 days from Monday 2026-01-05 end on Tuesday 2026-01-13 (s 50(d) skips the Sunday and the holiday) while 7 days from the same day end on Monday 2026-01-12 (counted straight through; Monday is not an excluded day). Asserted.
9. **Section 50(c) is narrower than it looks.** It covers an act directed or allowed to be done on a day that is an excluded day, and only the next day that is not excluded. An act done two days later is not covered, and neither is an act directed for an ordinary day. Asserted.
10. **A law published in the Gazette is in operation from the start of its publication day.** Section 10(1)(b): "on the expiration of the previous day", so from the first moment of the day, hours before it may have been published. Asserted.
11. **The clock.** Standard time is 8 hours ahead of UTC unless the President notifies another figure (s 51(2)); a time of day in a law or instrument is standard time unless specifically stated otherwise (s 51(1)). Asserted.
12. **Deemed service by post gives no number of days.** Section 2(5) deems service effected when the letter would be delivered "in the ordinary course of post" and is rebuttable ("unless the contrary is proved"), but the Act does not say how many days that is, so the seat asks the day. Asserted.
13. **Late applications for more time.** Where a written law prescribes a time and gives a court or authority power to extend it, the power may be exercised after the time has run out, unless a contrary intention appears (s 53). Where no time is prescribed, the thing is done "with all convenient speed" (s 52). Asserted.
14. **Death has two grounds, either of which suffices "for all purposes"** (s 2A(1)); the extra requirements of s 2A(2) to (6) govern the *determination*, not the definition. Asserted.
15. **Repeal does not take accrued rights away** (s 16(1)); a proceeding about an accrued right or penalty may be instituted, continued or enforced as if the repealing law had not been passed, and s 16(3) treats a law that expires, lapses or otherwise ceases to have effect as repealed for the purposes of the section. A law that repealed an older law does not revive it when itself repealed, unless words are added (s 12). Asserted.
16. **Section 14 goes silent.** After the substituted provision comes into operation the Act does not say what the repealed law is (F10). Asserted.
17. **Dated boundaries.** A Court application made on or after 1 April 2022 is by originating application or summons in the cases s 41A(1) names (the day before is not covered); s 41B applies from 1 January 2006; s 41C marks 2 January 2021; ss 41D and 41E mark 1 April 2022. The dates are asserted on both sides; 15 October 2024 in s 41D(2) is a class of proceedings, asserted as a choice.
18. **Three subsections are shown deleted:** s 2(4) (Act 5 of 2014), s 2(6) (Act 5 of 2025 wef 09/03/2025) and s 41D(3) (Act 19 of 2025 wef 05/12/2025). The text shows only the bracketed words. Asserted (the stubs quote them).
19. **Table rows are normalised.** The text writes "Defendant’s statement" with a curly apostrophe; the table rows in `sgia-p5-penal-court.l4` use a straight one, and the seat returns the straight form. The header line of the s 41B table reads "First column . Second column" in the text, with a stray full stop, and is quoted as it is. Not asserted.
20. **The converter text carries page furniture and wrapped history notes.** Page footers ("Informal Consolidation – version in force from 5/12/2025", "2020 Ed. Interpretation Act 1965") and amendment notes in square brackets sit inside the sections. The coverage generator treats them as non-operative lines; `qx.py` leaves them out of quotations. Not asserted.
21. **A deployment point, not a finding about the Act:** the holidays input is a list of dates (see Seat).
22. **Section 48(6) and (7) tell the loser no.** After the appointed date a Gazette on the prescribed website prevails, to the extent of any inconsistency, over the same Gazette in any other form, and before it a Gazette in print does. The encoding returns `JUST TRUE` for the form that prevails, `JUST FALSE` for the form it prevails over, and `NOTHING` for a pair the two subsections do not speak to (print against another electronic form after the appointed date, where neither is the website). The seat asks it as the Gazette question. Asserted.
23. **Only one row of s 2(3) says "respectively", and it pairs.** Row (l) reads a Judge of the High Court as a Judge of the Supreme Court and the Registrar of the High Court as the Registrar of the Supreme Court; each old expression has its own replacement and the printed words stay queryable (`the words section 2(3) prints for`). "respectively" occurs once in the whole text, in (l) (searched); rows (e) and (f) pair by "corresponding" and are left as the Act words them (F9). Asserted.
24. **Lists printed in s 2(1) are named twice, as the phrase and as its parts.** See "List members in the s 2(1) table". A thing the Act does not list is not named, which is weaker than excluded. Asserted.

## Reading a result: FALSE and NOTHING

The rule in force for this row, from 2026-10-29 (assumed, not ruled by a lawyer). This row already answered by it where it matters: fork F19 chose `NOTHING` for a list the text does not close.

A function answers `JUST FALSE` only where the text itself says no to the case in its own words: a definition that says "means", a condition introduced by "if", "only if", "as long as" or "unless", or a list the text closes with "only" or an equivalent. Where the text lists things without closing the list, says "includes", leaves a term undefined, is silent, or points to a power or authority outside the text, the function answers `NOTHING`, and a comment on that branch names which of those it is. The function's name carries the scope its `FALSE` claims ("under section 47 ...", not "may I ..."), and a seat question that asks Act-wide inherits `NOTHING` wherever the Act points outside itself.

In plain words: `JUST FALSE` is the Act's own "no"; `NOTHING` is "the Act does not say". The seat renders them "No." and "The Interpretation Act does not say."

**Checked on 2026-10-29 under this rule.** The 22 `JUST FALSE` sites in the modules were read against the text by a second reader and all were kept, with no change to a function or an assertion. Twenty rest on an express negation in the text ("does not extend", "does not permit", "may not be further delegated", "are not discontinued or abated", "do not invalidate" and the like), which the reader counted as the text saying no in its own words; that is a reading for a lawyer to confirm, and 45 `JUST FALSE` assertions depend on it. Two are marginal and are for a lawyer: s 48(6) and (7), where the text says one form "prevails over" another and the function answers `JUST FALSE` for the form that loses, which is the converse of the text's sentence (the reader leaned to `NOTHING`; this row keeps `JUST FALSE` because the independent test author expected "No." and the encoder had first returned `NOTHING`, which could never say who loses; finding 22).

**Not changed, and open (counts are the second reader's, read from the code and not re-run):** only 2 of the 15 function names that return `JUST FALSE` say "under section N"; the section is in each `@ref` and the comment above the function. The `JUST FALSE` of `that provision has any effect in relation to the application` (s 41A(2)(c)) is unqualified although the text says "to the extent of the inconsistency". The reader found at least 19 `JUST <expression>` branches that can also evaluate to `FALSE` and did not classify them. It found none of the 38 plain-`BOOLEAN` functions answering `FALSE` for a catch-all value.

## Known limits

What the encoding cannot answer, stated so that nobody looks for it.
They are limits of the encoding, not findings about the Act.

1. **Negative and instance questions about the s 2(1) table.** Of the 68 gaps the independent test pass found, 36 (the team lead's triage) were of the forms "is X not a Y" or "is this particular thing a Y". The table answers "does the Act name X in defining Y" (and, since round 2, "does it name each part of a list it prints"). It cannot say that X is NOT a Y, because "includes" lists are open and "not named" is not "excluded"; and it cannot say that a particular body or instrument is a Y, because that takes facts the table does not hold. No function answers either.
2. **Rule-side bundled lists.** Where a rule's own wording is a list of alternatives, the rule takes the list as printed, as one input or one choice, and does not split it by member: s 9(1) and (2) (a section, Part, Chapter or Schedule is one choice, and a subsection, paragraph or sub-paragraph is the other), s 36(2) and (3) (the delegates of each subsection are one choice), s 41A(6) (a court "or a judge sitting in" it is one choice), s 43 (the eight officers are one input), s 46(2) (fee, charge, penalty or interest, and the Government, public body, statutory authority or public officer, are one input) and s 47 (death, resignation, absence and removal are not told apart: the rule has no input for which of them happened). A question about one member of such a list has to be asked about the list.
3. **Powers to prescribe or regulate are machinery and have no function.** The regulation-making power of s 2A(7), the order-making power of s 41A(7) and the regulation-making power of s 48(8) are inert rows (reason 2); what they would prescribe enters as plain inputs (the criteria and qualifications of s 2A, the classes and courts of s 41A, another form of the Gazette in s 48). The encoding cannot say whether an instrument was in fact made.
4. **Cut-off dates held as yes/no inputs.** Two rules take a date that the Act fixes as a plain yes/no input and not as a date to compare: `it is a revised edition published before 1 March 2021 under a law providing for a revised edition` (s 8(1)(a)(iii)) and `it is pending on or after 1 April 2022` (s 41A(5)). They were found by searching the inputs of every layer-1 module for a yes/no whose name holds a year. The person, or the deployer, has to decide the date question first.
5. **"master" cannot be asked about a particular person.** The table holds the phrase as printed, including "except a pilot or harbour master"; whether a given person is the master of a ship is an instance question (limit 1).

## What the stable binary does not accept

The stable binary is `l4-stable-98` (1.6.98, main, 7689b0d, 2026-10-19), sha256 `82ea44ad...263e`; the main build it was compared with is 1.6.102 (e4f2553, 2026-10-26).
Sorted by how the failure shows up.

**Loud (an error, so you learn at once):**
- `YMD` is not defined in `daydate`, and this encoding defines no shim for it: every module writes dates as `Date day month year`. Round 1 defined a local shim in `sgia-interpretation-time.l4` and every other file got it by import (a diamond import was verified to work); the lead renamed it to `YearMonthDay` after round 1 and, after round 2, removed it and rewrote every use as `Date`.
- `BRANCH` inside parentheses as an argument does not parse (`unexpected (`): put the `BRANCH` in a named helper (`the proceedings named` in `sgia-seat.l4`).
- The parameter names of a `GIVEN` must come in the same order as the definition head, or the type signature and the definition disagree.
- A list element that is a record must be wrapped in parentheses; `elem x (r's field)` needs the parentheses around the genitive; `NOT (a EQUALS b)`, not `NOT EQUALS`; `ELSE IF` nested in a `CONSIDER` gives a layout error (use one `IF` or a `BRANCH`).
- `minimum` is ambiguous over dates: use `Date (minimum (map (GIVEN d YIELD Day d) xs))`.
- A pattern variable that has the name of a constructor in an imported module (`words` in `JUST words`) is read as that constructor, and the error is a type mismatch far from the cause.
- No `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` or section-level `GIVEN`; the encoding uses per-rule `GIVEN` and `MAYBE`/`NOTHING` for "not covered".
- An `#ASSERT` continued onto a second line.

**Silent (wrong answer, exit code 0):**
- `NOT a AND b` parses as `NOT (a AND b)`; every `NOT` in this encoding is parenthesised.
- `daydate`'s `add months` and `add years` clamp without warning (finding 4).
- `l4 check` prints `Check succeeded.` and says nothing about assertions; `check.sh` reads the counts, because an exit code cannot say how many assertions ran, failed or were refused.

## What `check.sh` prints

**Target: `main`.**
The encoding is written to be read by the stable (main) compiler, and `check.sh` ran every module with both builds: the one it was written with, `l4 --version` = `1.6.98 (main, 7689b0d, 2026-10-19)`, and the main build it compared with, `1.6.102 (main, e4f2553, 2026-10-26)`.
Command, from this folder: `L4=<L4_BIN> L4_MAIN=<L4_MAIN> ./check.sh`.
Round 1's run (18 modules, 1165 satisfied, 0 failed, 0 refused) is replaced by the one below: round 2 adds 187 satisfied assertions (the seat cases +14, the definitions +143, `sgia-tests-p1-other.l4` +7, `sgia-tests-p4.l4` +2, `sgia-tests-p6.l4` +21).
The run below is a point-in-time record.

<!-- CHECK-OUTPUT:BEGIN -->

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.102 (main, e4f2553, 2026-10-26)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sgia-cases-seat.l4                             0       161       0        0         0 |      0       161       0        0  same
sgia-interpretation-time.l4                    0         0       0        0         0 |      0         0       0        0  same
sgia-p1-definitions.l4                         0         0       0        0         0 |      0         0       0        0  same
sgia-p1-other.l4                               0         0       0        0         0 |      0         0       0        0  same
sgia-p2-written-law.l4                         0         0       0        0         0 |      0         0       0        0  same
sgia-p3-subsidiary.l4                          0         0       0        0         0 |      0         0       0        0  same
sgia-p4-powers.l4                              0         0       0        0         0 |      0         0       0        0  same
sgia-p5-penal-court.l4                         0         0       0        0         0 |      0         0       0        0  same
sgia-p6-misc.l4                                0         0       0        0         0 |      0         0       0        0  same
sgia-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgia-tests-definitions.l4                      0       440       0        0         0 |      0       440       0        0  same
sgia-tests-p1-other.l4                         0       116       0        0         0 |      0       116       0        0  same
sgia-tests-p2.l4                               0       119       0        0         0 |      0       119       0        0  same
sgia-tests-p3.l4                               0        61       0        0         0 |      0        61       0        0  same
sgia-tests-p4.l4                               0       130       0        0         0 |      0       130       0        0  same
sgia-tests-p5.l4                               0       102       0        0         0 |      0       102       0        0  same
sgia-tests-p6.l4                               0       101       0        0         0 |      0       101       0        0  same
sgia-tests-time.l4                             0       122       0        0         0 |      0       122       0        0  same
TOTAL (18 modules)                             0      1352       0        0           |      0      1352       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

<!-- CHECK-OUTPUT:END -->

Other checks, all run at the end:
`python3 -I srcrefs.py check --refs ../../registers/source-bundle/IA1965.txt sgia-*.l4` (every quotation equals the text and every locator ends on a quoted line), and the same with `--strict` in place of `--refs` (every locator's end lines are also covered by the quotation lines directly above it); both read 289 locators and 0 problems after round 2;
`python3 -I gen-defs.py ../../registers/source-bundle/IA1965.txt --verify` (every term, named member and pointer in the hand-read table of s 2(1) occurs in its own entry's text);
`python3 -I gen-coverage.py ../../registers/source-bundle/IA1965.txt .` (the coverage table, and the audit below).

## Before the encoding is worth relying on

- A person who knows Singapore law should read it against the official text; the converter text is not that, and its hash does not match its record.
- An expert should rule F1, F2 and F4 first: they decide what the seat says for "after" an event and for months and years.
- Decide how a period in weeks, months or years is to be counted for Singapore; the Act does not, and the encoding refuses to guess.
- The public holidays are a list the person supplies; no list of Singapore public holidays is among the inputs.
- The seat's Interact form must accept a list of dates for the holidays input.
- The prescribed criteria (s 2A), the classes and courts prescribed under s 41A(7), and the "appointed date" in s 48 are asked as facts; whoever deploys this must supply the instruments that set them.
- The Act has been amended since the text was taken; compare the text's in-force date, 5 December 2025, with the date of use.
- Rule F19, F20, F21 and F25 (round 2): they decide whether a delegation to anyone else, an item regulated by Rules of Court, a court not shown to be prescribed, or material s 9A(3) does not name is told "no" (`JUST FALSE`) or "not covered" (`NOTHING`); the encoding says `NOTHING` throughout, and each is one branch to change.

## Changes to existing modules

Round 2 (the fix list from the independent test pass) changed these round-1 files; every other file in this folder is byte-identical to the files as they stood at the start of round 2 (which already carried the team lead's rename of the date shim to `YearMonthDay`), except `NOTES.md`, `PROGRESS.md` and `encoding.json`. That statement describes round 2 only: afterwards the lead removed the shim and rewrote every use as `Date day month year`, which touched every `.l4` file that builds a date.
A diff against a snapshot taken at the start of round 2 lists exactly the files below.

- `sgia-p6-misc.l4`: the rule `this form prevails over the other form to the extent of any inconsistency` (s 48(6) and (7)) now returns `JUST FALSE` for the form that loses (the prescribed website against print on or after the appointed date, print against the prescribed website before it) and `NOTHING` for a pair neither subsection speaks to.
  Before, the loser was `NOTHING`.
  The rule's parameters and its `@ref` locator are unchanged; its head comment was rewritten.
- `sgia-tests-p6.l4`: the two s 48(6) and (7) assertions that expected `NOTHING` for the loser are replaced by 23 that assert both sides, the day boundaries and the pairs left `NOTHING` (the file now has 101).
- `sgia-seat.l4`: one question added, `If two forms of the Gazette differ, does this form control (s 48(6) and (7))?`, with a helper `the form of the Gazette named`; it answers in words and says "Please choose one of: ..." for a form it does not know (the seat now has 31 questions).
- `sgia-cases-seat.l4`: 14 cases for that question, with the appointed date taken as 2026-06-01 (the file now has 161).
- `sgia-p1-other.l4`: s 2(3)(l) "respectively".
  A new record `Paired replacement` (an old expression and its replacement) and a new field `each construed as` on `Old reference`, empty on every row except (l), where it pairs "a Judge of the High Court" with "a Judge of the Supreme Court" and "the Registrar of the High Court" with "the Registrar of the Supreme Court".
  `a reference in an old written law is to be construed as` uses the pair when the row has one and falls back to the row's `construed as` otherwise.
  A new function `the words section 2(3) prints for` returns the words the Act prints for the row that lists an old expression, whole (for row (l) both replacements and "respectively"), and `NOTHING` for an expression no row lists.
  Rows (e) and (f) are left whole: they pair by "corresponding" and F9 stays.
- `sgia-tests-p1-other.l4`: the two assertions for row (l) are replaced by nine that assert each old expression's own replacement, the printed words, and that the two replacements cannot be mixed (the file now has 116).
- `gen-defs.py`, and so the two files it writes, `sgia-p1-definitions.l4` and `sgia-tests-definitions.l4`: the list-member tables `EXTEND`, `UNLISTED` and `LEFT` and the sweep (see "List members in the s 2(1) table").
  Regenerating before the change reproduced the round-1 files byte for byte; after it, the definitions module differs only in the longer `what the Act names` lists of the 21 extended entries and in its header comment, and the tests file has 143 more assertions (440 in all).
- `sgia-tests-p4.l4`: two assertions added for F23 (the file now has 130).
- `sgia-interpretation-time.l4`: only the quotation under `s 50(b) read as reaching periods of days only` was re-cut into two runs of lines (2149-2151 and 2153-2156) so that its locator 2149-2156 is covered by the lines directly above it and `srcrefs.py check --strict` passes; no rule changed.
- `coverage-dispositions.py`: the `FORKS` table maps the units of F19 to F26 (15 rows move from `encoded` to `fork`; the row count stays 496) and the text for `s 32A(1)` now names F23.

## Coverage

Built from the text by `gen-coverage.py`, with its hand-written dispositions in `coverage-dispositions.py`.
It cuts the text into units with `gen-units.py` (sections, subsections, paragraphs, sub-paragraphs, defined terms, Part headings and blocks) and gives every section its marginal heading as a row of its own.
A unit is `encoded` when every operative line of it lies inside the `@ref` locator of a rule that has at least one assertion; the rule names are in the table.
A unit falls under `fork` when it is named in `FORKS`; the table cell names the fork and the rule that encodes the chosen reading (or the explicit not-covered value).
Everything else is `inert` with its reason or `repealed or blank in this text`; there is no out-of-scope and no deferred row.
**Audit** (printed by the script on every run): every non-blank line of the text lies in exactly one row, with no gaps and no overlaps; the counts are in the summary line under the table.
Operative lines exclude blank lines, page footers and bracketed amendment notes.
The script also prints "weakly cited rows" on every run: rows whose only citing rule is one whose quotation spans a whole section (ss 20, 36, 41A, 48A, and the death criteria of s 2A); that is the text's own shape, one function over a section's branches, and not a gap.

<!-- COVERAGE-TABLE:BEGIN -->

| lines | provision | disposition | rule(s) with @ref, or reason | assertions |
| --- | --- | --- | --- | --- |
| 1-148 | cover and arrangement of sections | inert | reason 1 (the cover, the contents list and the arrangement of sections) |  |
| 149-153 | long title and date of enactment | inert | reason 1 (the long title and the date of enactment) |  |
| 154-154 | s 1 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 155-159 | s 1 | inert | reason 2 (machinery: the Act's own short title) |  |
| 160-163 | Part 1 heading | inert | reason 1 (a Part heading: groups the sections that follow and creates no rule) |  |
| 164-165 | s 2 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 166-169 | s 2(1) | encoded | `the definitions in section 2(1) apply to a written law enacted on` (p1-other) | 3 |
| 170-172 | s 2(1) “abet” | encoded | `s 2(1) definition 01: abet` (p1-definitions) | 3 |
| 173-175 | s 2(1) “Accountant-General” | encoded | `s 2(1) definition 02: Accountant-General` (p1-definitions) | 3 |
| 176-179 | s 2(1) “act” | encoded | `s 2(1) definition 03: act` (p1-definitions) | 3 |
| 180-185 | s 2(1) “Act” | encoded | `s 2(1) definition 04: Act` (p1-definitions) | 3 |
| 186-188 | s 2(1) “advocate” | encoded | `s 2(1) definition 05: advocate` (p1-definitions) | 3 |
| 189-191 | s 2(1) “animal” | encoded | `s 2(1) definition 06: animal` (p1-definitions) | 7 |
| 192-193 | s 2(1) “appoint” | encoded | `s 2(1) definition 07: appoint` (p1-definitions) | 3 |
| 194-199 | s 2(1) “Attorney‑General” | encoded | `s 2(1) definition 08: Attorney-General` (p1-definitions) | 3 |
| 200-201 | s 2(1) “Auditor-General” | encoded | `s 2(1) definition 09: Auditor-General` (p1-definitions) | 3 |
| 202-203 | s 2(1) “Cabinet” | encoded | `s 2(1) definition 10: Cabinet` (p1-definitions) | 3 |
| 204-208 | s 2(1) “Chief Justice” | encoded | `s 2(1) definition 11: Chief Justice` (p1-definitions) | 3 |
| 209-212 | s 2(1) “citizen of Singapore” | encoded | `s 2(1) definition 12: citizen of Singapore` (p1-definitions) | 3 |
| 213-215 | s 2(1) “civil list” | encoded | `s 2(1) definition 13: civil list` (p1-definitions) | 3 |
| 216-218 | s 2(1) “commencement” | encoded | `s 2(1) definition 14: commencement` (p1-definitions) | 3 |
| 219-222 | s 2(1) “common law” | encoded | `s 2(1) definition 15: common law` (p1-definitions) | 7 |
| 223-227 | s 2(1) “Commonwealth” | encoded | `s 2(1) definition 16: Commonwealth` (p1-definitions) | 9 |
| 228-234 | s 2(1) “Commonwealth country” | encoded | `s 2(1) definition 17: Commonwealth country` (p1-definitions) | 10 |
| 235-237 | s 2(1) “Consolidated Fund” | encoded | `s 2(1) definition 18: Consolidated Fund` (p1-definitions) | 3 |
| 238-240 | s 2(1) “Constitution” | encoded | `s 2(1) definition 19: Constitution` (p1-definitions) | 17 |
| 241-245 | s 2(1) “consular officer” | encoded | `s 2(1) definition 20: consular officer` (p1-definitions) | 9 |
| 246-249 | s 2(1) “contravene” | encoded | `s 2(1) definition 21: contravene` (p1-definitions) | 3 |
| 250-254 | s 2(1) “court” | encoded | `s 2(1) definition 22: court` (p1-definitions) | 3 |
| 255-256 | s 2(1) “Criminal Procedure Rules” | encoded | `s 2(1) definition 23: Criminal Procedure Rules` (p1-definitions) | 3 |
| 257-261 | s 2(1)(a) | encoded | `s 2(1) definition 23: Criminal Procedure Rules` (p1-definitions) | 3 |
| 262-265 | s 2(1)(b) | encoded | `s 2(1) definition 23: Criminal Procedure Rules` (p1-definitions) | 3 |
| 266-269 | s 2(1) “Crown Agents” | encoded | `s 2(1) definition 24: Crown Agents` (p1-definitions) | 3 |
| 270-272 | s 2(1) “Deputy Attorney-General” | encoded | `s 2(1) definition 25: Deputy Attorney-General` (p1-definitions) | 3 |
| 273-275 | s 2(1) “Deputy Speaker” | encoded | `s 2(1) definition 26: Deputy Speaker` (p1-definitions) | 3 |
| 276-278 | s 2(1) “District Court” | encoded | `s 2(1) definition 27: District Court` (p1-definitions) | 3 |
| 279-282 | s 2(1) “District Judge” | encoded | `s 2(1) definition 28: District Judge` (p1-definitions) | 3 |
| 283-286 | s 2(1) “export” | encoded | `s 2(1) definition 29: export` (p1-definitions) | 8 |
| 287-289 | s 2(1) “Family Court” | encoded | `s 2(1) definition 30: Family Court` (p1-definitions) | 3 |
| 290-294 | s 2(1) “Family Justice Rules” | encoded | `s 2(1) definition 31: Family Justice Rules` (p1-definitions) | 3 |
| 295-303 | s 2(1) “Gazette” | encoded | `s 2(1) definition 32: Gazette` (p1-definitions) | 3 |
| 304-305 | s 2(1) “Government” | encoded | `s 2(1) definition 33: Government` (p1-definitions) | 3 |
| 306-312 | s 2(1) “Government Printer” | encoded | `s 2(1) definition 34: Government Printer` (p1-definitions) | 10 |
| 313-315 | s 2(1) “High Court” | encoded | `s 2(1) definition 35: High Court` (p1-definitions) | 3 |
| 316-323 | s 2(1) “His Majesty” | encoded | `s 2(1) definition 36: His Majesty` (p1-definitions) | 3 |
| 324-327 | s 2(1) “immovable property” | encoded | `s 2(1) definition 37: immovable property` (p1-definitions) | 3 |
| 328-331 | s 2(1) “import” | encoded | `s 2(1) definition 38: import` (p1-definitions) | 8 |
| 332-341 | s 2(1) “Judge” | encoded | `s 2(1) definition 39: Judge` (p1-definitions) | 16 |
| 342-350 | s 2(1) “Judicial Service Commission” | encoded | `s 2(1) definition 40: Judicial Service Commission` (p1-definitions) | 3 |
| 351-355 | s 2(1) “Judicial Service Officer” | encoded | `s 2(1) definition 41: Judicial Service Officer` (p1-definitions) | 3 |
| 356-361 | s 2(1) “Legal Service Commission” | encoded | `s 2(1) definition 42: Legal Service Commission` (p1-definitions) | 3 |
| 362-366 | s 2(1) “Legal Service Officer” | encoded | `s 2(1) definition 43: Legal Service Officer` (p1-definitions) | 3 |
| 367-370 | s 2(1) “legislature” | encoded | `s 2(1) definition 44: legislature` (p1-definitions) | 3 |
| 371-373 | s 2(1) “Magistrate” | encoded | `s 2(1) definition 45: Magistrate` (p1-definitions) | 3 |
| 374-375 | s 2(1) “Malaya” | encoded | `s 2(1) definition 46: Malaya` (p1-definitions) | 7 |
| 376-377 | s 2(1) “Malaysia” | encoded | `s 2(1) definition 47: Malaysia` (p1-definitions) | 3 |
| 378-382 | s 2(1) “Malaysian citizen” | encoded | `s 2(1) definition 48: Malaysian citizen` (p1-definitions) | 3 |
| 383-386 | s 2(1) “master” | encoded | `s 2(1) definition 49: master` (p1-definitions) | 3 |
| 387-392 | s 2(1) “military” | encoded | `s 2(1) definition 50: military` (p1-definitions) | 3 |
| 393-396 | s 2(1) “Minister” | encoded | `s 2(1) definition 51: Minister` (p1-definitions) | 3 |
| 397-405 | s 2(1) “monogamous marriage” | encoded | `s 2(1) definition 52: monogamous marriage` (p1-definitions) | 3 |
| 406-407 | s 2(1) “month” | encoded | `s 2(1) definition 53: month` (p1-definitions) | 6 |
| 408-410 | s 2(1) “movable property” | encoded | `s 2(1) definition 54: movable property` (p1-definitions) | 3 |
| 411-412 | s 2(1) “national language” | encoded | `s 2(1) definition 55: national language` (p1-definitions) | 3 |
| 413-417 | s 2(1) “oath” | encoded | `s 2(1) definition 56: oath` (p1-definitions) | 11 |
| 418-425 | s 2(1) “Ordinance” | encoded | `s 2(1) definition 57: Ordinance` (p1-definitions) | 3 |
| 426-427 | s 2(1) “Parliament” | encoded | `s 2(1) definition 58: Parliament` (p1-definitions) | 3 |
| 428-430 | s 2(1) “person” | encoded | `s 2(1) definition 59: person` (p1-definitions) | 8 |
| 431-433 | s 2(1) “police officer” | encoded | `s 2(1) definition 60: police officer` (p1-definitions) | 3 |
| 434-440 | s 2(1) “prescribed” | encoded | `s 2(1) definition 61: prescribed` (p1-definitions) | 3 |
| 441-444 | s 2(1) “President” | encoded | `s 2(1) definition 62: President` (p1-definitions) | 3 |
| 445-451 | s 2(1) “public holiday” | encoded | `s 2(1) definition 63: public holiday` (p1-definitions) | 3 |
| 452-454 | s 2(1) “public officer” | encoded | `s 2(1) definition 64: public officer` (p1-definitions) | 3 |
| 455-456 | s 2(1) “public seal” | encoded | `s 2(1) definition 65: public seal` (p1-definitions) | 3 |
| 457-458 | s 2(1) “public service” | encoded | `s 2(1) definition 66: public service` (p1-definitions) | 3 |
| 459-462 | s 2(1) “Public Service Commission” | encoded | `s 2(1) definition 67: Public Service Commission` (p1-definitions) | 3 |
| 463-466 | s 2(1) “registered” | encoded | `s 2(1) definition 68: registered` (p1-definitions) | 3 |
| 467-470 | s 2(1) “repeal” | encoded | `s 2(1) definition 69: repeal` (p1-definitions) | 3 |
| 471-475 | s 2(1) “Rules of Court” | encoded | `s 2(1) definition 70: Rules of Court` (p1-definitions) | 3 |
| 476-479 | s 2(1) “Secretary to the Cabinet” | encoded | `s 2(1) definition 71: Secretary to the Cabinet` (p1-definitions) | 3 |
| 480-482 | s 2(1) “ship” | encoded | `s 2(1) definition 72: ship` (p1-definitions) | 3 |
| 483-487 | s 2(1) “sign” | encoded | `s 2(1) definition 73: sign` (p1-definitions) | 3 |
| 488-492 | s 2(1) “Singapore” | encoded | `s 2(1) definition 74: Singapore` (p1-definitions) | 18 |
| 493-494 | s 2(1) “Solicitor-General” | encoded | `s 2(1) definition 75: Solicitor-General` (p1-definitions) | 3 |
| 495-500 | s 2(1) “Speaker” | encoded | `s 2(1) definition 76: Speaker` (p1-definitions) | 3 |
| 501-502 | s 2(1) “States of Malaya” | encoded | `s 2(1) definition 77: States of Malaya` (p1-definitions) | 16 |
| 503-506 | s 2(1)(a) | encoded | `s 2(1) definition 77: States of Malaya` (p1-definitions) | 16 |
| 507-512 | s 2(1)(b) | encoded | `s 2(1) definition 77: States of Malaya` (p1-definitions) | 16 |
| 513-514 | s 2(1) “statutory declaration” | encoded | `s 2(1) definition 78: statutory declaration` (p1-definitions) | 12 |
| 515-517 | s 2(1)(a) | encoded | `s 2(1) definition 78: statutory declaration` (p1-definitions) | 12 |
| 518-524 | s 2(1)(b) | encoded | `s 2(1) definition 78: statutory declaration` (p1-definitions) | 12 |
| 525-529 | s 2(1)(c) | encoded | `s 2(1) definition 78: statutory declaration` (p1-definitions) | 12 |
| 530-534 | s 2(1) “subsidiary legislation” | encoded | `s 2(1) definition 79: subsidiary legislation` (p1-definitions) | 13 |
| 535-537 | s 2(1) “Supreme Court” | encoded | `s 2(1) definition 80: Supreme Court` (p1-definitions) | 3 |
| 538-541 | s 2(1) “Supreme Court Judge” | encoded | `s 2(1) definition 81: Supreme Court Judge` (p1-definitions) | 9 |
| 542-543 | s 2(1) “United Kingdom” | encoded | `s 2(1) definition 82: United Kingdom` (p1-definitions) | 7 |
| 544-549 | s 2(1) “value” | encoded | `s 2(1) definition 83: value` (p1-definitions) | 3 |
| 550-551 | s 2(1) “vessel” | encoded | `s 2(1) definition 84: vessel` (p1-definitions) | 3 |
| 552-553 | s 2(1) “will” | encoded | `s 2(1) definition 85: will` (p1-definitions) | 3 |
| 554-555 | s 2(1) words importing the masculine gender inc | fork | F14: the Act extends the masculine to females and says nothing about the feminine, so the feminine rule returns NOTHING -- `s 2(1) definition 86: words importing the masculine gender` (p1-definitions); `section 2(1) extends a word importing the masculine gender to` (p1-other) | 6 |
| 556-558 | s 2(1) words in the singular include the plural | encoded | `s 2(1) definition 87: words in the singular` (p1-definitions); `section 2(1) extends a word in one number to what is meant in the other` (p1-other) | 8 |
| 559-562 | s 2(1) “writing” | encoded | `s 2(1) definition 88: writing` (p1-definitions) | 10 |
| 563-568 | s 2(1) “written law” | fork | F24: the table lists the limbs the Act names; no rule decides whether "for the time being in force" reaches the previous Constitutions -- `s 2(1) definition 89: written law` (p1-definitions) | 12 |
| 569-574 | s 2(1) “Yang di-Pertuan Agong” | encoded | `s 2(1) definition 90: Yang di-Pertuan Agong` (p1-definitions) | 10 |
| 575-577 | s 2(1) “year” | encoded | `s 2(1) definition 91: year` (p1-definitions) | 5 |
| 578-585 | s 2(1) “Youth Court” | encoded | `s 2(1) definition 92: Youth Court` (p1-definitions) | 3 |
| 586-590 | s 2(2) | encoded | `a variant of a defined word has a corresponding meaning in that law` (p1-other) | 5 |
| 591-598 | s 2(2A) | encoded | `the definition a written law provides applies` (p1-other) | 4 |
| 599-600 | s 2(3) | encoded | `a reference in an old written law is to be construed as` (p1-other); `the twelve rows of section 2(3)` (p1-other); `the words section 2(3) prints for` (p1-other) | 36 |
| 601-605 | s 2(3)(a) | encoded | `s 2(3)(a)` (p1-other) | 18 |
| 606-609 | s 2(3)(b) | encoded | `s 2(3)(b)` (p1-other) | 3 |
| 610-612 | s 2(3)(c) | encoded | `s 2(3)(c)` (p1-other) | 3 |
| 613-616 | s 2(3)(d) | encoded | `s 2(3)(d)` (p1-other) | 1 |
| 617-623 | s 2(3)(e) | fork | F9: the construed-as words are returned as the Act states them, "as the case may require" being left to the reader -- `s 2(3)(e)` (p1-other) | 3 |
| 624-630 | s 2(3)(f) | encoded | `s 2(3)(f)` (p1-other) | 2 |
| 631-633 | s 2(3)(g) | encoded | `s 2(3)(g)` (p1-other) | 5 |
| 634-636 | s 2(3)(h) | encoded | `s 2(3)(h)` (p1-other) | 1 |
| 637-639 | s 2(3)(i) | encoded | `s 2(3)(i)` (p1-other) | 1 |
| 640-645 | s 2(3)(j) | encoded | `s 2(3)(j)` (p1-other) | 1 |
| 646-649 | s 2(3)(k) | encoded | `s 2(3)(k)` (p1-other) | 1 |
| 650-654 | s 2(3)(l) | encoded | `s 2(3)(l)` (p1-other) | 5 |
| 655-656 | s 2(4) | repealed or blank | the text shows `(4) [Deleted by Act 5 of 2014]`; the stub `s 2(4) is deleted` quotes it and a test asserts it | 1 |
| 657-664 | s 2(5) | fork | F12: s 2(5) and s 48A both speak of service by post; each is encoded as its own rule and the Act does not say which prevails -- `service by post is deemed effected` (interpretation-time) | 6 |
| 665-666 | s 2(6) | repealed or blank | the text shows `(6) [Deleted by Act 5 of 2025 wef 09/03/2025]`; the stub `s 2(6) is deleted` quotes it and a test asserts it | 1 |
| 667-668 | s 2A marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 669-671 | s 2A(1) | encoded | `a person has died` (p1-other) | 4 |
| 672-674 | s 2A(1)(a) | encoded | `a person has died` (p1-other) | 4 |
| 675-677 | s 2A(1)(b) | encoded | `a person has died` (p1-other) | 4 |
| 678-682 | s 2A(2) | fork | F8: the ordinary standards of medical practice still apply when s 2A(5) adds requirements -- `what the determination of death requires` (p1-other) | 18 |
| 683-686 | s 2A(3) | fork | F8: the prescribed criteria still apply when s 2A(4) and (6) add requirements -- `what the determination of death requires` (p1-other) | 18 |
| 687-695 | s 2A(4) | fork | F7: "2 medical practitioners" read as at least 2 -- `the certificate meets section 2A(4)` (p1-other); `what the determination of death requires` (p1-other) | 24 |
| 696-698 | s 2A(4)(a) | fork | F7: "2 medical practitioners" read as at least 2 -- `the certificate meets section 2A(4)` (p1-other); `what the determination of death requires` (p1-other) | 24 |
| 699-701 | s 2A(4)(b) | fork | F7: "2 medical practitioners" read as at least 2 -- `the certificate meets section 2A(4)` (p1-other); `what the determination of death requires` (p1-other) | 24 |
| 702-709 | s 2A(5) | fork | F7, F8: "2 medical practitioners" read as at least 2; the ordinary standards of s 2A(2) still apply -- `the certificate meets section 2A(5)` (p1-other); `what the determination of death requires` (p1-other) | 25 |
| 710-712 | s 2A(5)(a) | fork | F7, F8: "2 medical practitioners" read as at least 2; the ordinary standards of s 2A(2) still apply -- `the certificate meets section 2A(5)` (p1-other); `what the determination of death requires` (p1-other) | 25 |
| 713-715 | s 2A(5)(b) | fork | F7, F8: "2 medical practitioners" read as at least 2; the ordinary standards of s 2A(2) still apply -- `the certificate meets section 2A(5)` (p1-other); `what the determination of death requires` (p1-other) | 25 |
| 716-718 | s 2A(5)(c) | fork | F7, F8: "2 medical practitioners" read as at least 2; the ordinary standards of s 2A(2) still apply -- `the certificate meets section 2A(5)` (p1-other); `what the determination of death requires` (p1-other) | 25 |
| 719-722 | s 2A(5)(d) | fork | F7, F8: "2 medical practitioners" read as at least 2; the ordinary standards of s 2A(2) still apply -- `the certificate meets section 2A(5)` (p1-other); `what the determination of death requires` (p1-other) | 25 |
| 723-730 | s 2A(6) | fork | F7, F8: "2 medical practitioners" read as at least 2; the prescribed criteria of s 2A(3) still apply -- `the certificate meets section 2A(6)` (p1-other); `what the determination of death requires` (p1-other) | 26 |
| 731-733 | s 2A(6)(a) | fork | F7, F8: "2 medical practitioners" read as at least 2; the prescribed criteria of s 2A(3) still apply -- `the certificate meets section 2A(6)` (p1-other); `what the determination of death requires` (p1-other) | 26 |
| 734-739 | s 2A(6)(b) | fork | F7, F8: "2 medical practitioners" read as at least 2; the prescribed criteria of s 2A(3) still apply -- `the certificate meets section 2A(6)` (p1-other); `what the determination of death requires` (p1-other) | 26 |
| 740-742 | s 2A(6)(c) | fork | F7, F8: "2 medical practitioners" read as at least 2; the prescribed criteria of s 2A(3) still apply -- `the certificate meets section 2A(6)` (p1-other); `what the determination of death requires` (p1-other) | 26 |
| 743-746 | s 2A(6)(d) | fork | F7, F8: "2 medical practitioners" read as at least 2; the prescribed criteria of s 2A(3) still apply -- `the certificate meets section 2A(6)` (p1-other); `what the determination of death requires` (p1-other) | 26 |
| 747-749 | s 2A(6)(e) | fork | F7, F8: "2 medical practitioners" read as at least 2; the prescribed criteria of s 2A(3) still apply -- `the certificate meets section 2A(6)` (p1-other); `what the determination of death requires` (p1-other) | 26 |
| 750-752 | s 2A(7) | inert | reason 2 (machinery: a power of the Minister to make regulations; the criteria and qualifications it would prescribe are inputs `the prescribed criteria` and `they possess the prescribed postgraduate medical qualifications`) |  |
| 753-756 | s 2A(7)(a) | inert | reason 2 (machinery: the regulation-making power of s 2A(7), limb (a)) |  |
| 757-760 | s 2A(7)(b) | inert | reason 2 (machinery: the regulation-making power of s 2A(7), limb (b)) |  |
| 761-762 | s 2A(8) | encoded | `section 2A affects the operation of a written law on the presumption of death` (p1-other) | 1 |
| 763-769 | s 2A(8)(a) | encoded | `section 2A affects the operation of a written law on the presumption of death` (p1-other) | 1 |
| 770-774 | s 2A(8)(b) | encoded | `section 2A prevents the certification or determination of death` (p1-other) | 1 |
| 775-781 | s 2A(9) | encoded | `is a medical practitioner for section 2A` (p1-other) | 3 |
| 782-785 | Part 2 heading | inert | reason 1 (a Part heading: groups the sections that follow and creates no rule) |  |
| 786-787 | s 3 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 788-790 | s 3 | encoded | `an Act is judicially noticed as a public Act` (p2-written-law) | 2 |
| 791-792 | s 4 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 793-796 | s 4 | encoded | `an Act must be divided into sections` (p2-written-law) | 3 |
| 797-798 | s 5 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 799-801 | s 5 | encoded | `is part of the Act and has effect as part of it` (p2-written-law) | 3 |
| 802-803 | s 6 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 804-808 | s 6 | encoded | `the division of an Act is taken notice of in all courts and for all purposes` (p2-written-law) | 3 |
| 809-810 | s 7 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 811-814 | s 7 | encoded | `a deviation from a prescribed form invalidates it` (p2-written-law) | 6 |
| 815-816 | s 7A marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 817-819 | s 7A | encoded | `the example or illustration is exhaustive` (p2-written-law) | 2 |
| 820-822 | s 7A(a) | encoded | `the example or illustration is exhaustive` (p2-written-law) | 2 |
| 823-828 | s 7A(b) | encoded | `which prevails when an example is inconsistent with the provision` (p2-written-law) | 3 |
| 829-830 | s 8 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 831-832 | s 8(1) | encoded | `it is sufficient for all purposes to refer to the written law in this way` (p2-written-law) | 9 |
| 833-834 | s 8(1)(a) | encoded | `it is sufficient for all purposes to refer to the written law in this way` (p2-written-law) | 9 |
| 835-837 | s 8(1)(a)(i) | encoded | `it is sufficient for all purposes to refer to the written law in this way` (p2-written-law) | 9 |
| 838-840 | s 8(1)(a)(ii) | encoded | `it is sufficient for all purposes to refer to the written law in this way` (p2-written-law) | 9 |
| 841-845 | s 8(1)(a)(iii) | encoded | `it is sufficient for all purposes to refer to the written law in this way` (p2-written-law) | 9 |
| 846-851 | s 8(1)(b) | encoded | `it is sufficient for all purposes to refer to the written law in this way` (p2-written-law) | 9 |
| 852-859 | s 8(2) | encoded | `a reference may be made according to a copy of a written law` (p2-written-law) | 2 |
| 860-866 | s 8(3) | encoded | `the reference is read as a reference to the written law as amended from time to time` (p2-written-law) | 3 |
| 867-868 | s 8(4) | encoded | `the reference is read as a reference to the changed short title or citation` (p2-written-law) | 4 |
| 869-871 | s 8(4)(a) | encoded | `the reference is read as a reference to the changed short title or citation` (p2-written-law) | 4 |
| 872-881 | s 8(4)(b) | encoded | `the reference is read as a reference to the changed short title or citation` (p2-written-law) | 4 |
| 882-883 | s 9 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 884-889 | s 9(1) | encoded | `where a reference by number or letter only points` (p2-written-law) | 3 |
| 890-895 | s 9(2) | encoded | `where a reference by number or letter only points` (p2-written-law) | 3 |
| 896-898 | s 9(3) | encoded | `section 9 applies, with suitable modification` (p2-written-law) | 2 |
| 899-901 | s 9A marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 902-907 | s 9A(1) | encoded | `the interpretation to be preferred` (p2-written-law) | 4 |
| 908-912 | s 9A(2) | encoded | `consideration may be given to the material` (p2-written-law) | 4 |
| 913-917 | s 9A(2)(a) | encoded | `consideration may be given to the material` (p2-written-law) | 4 |
| 918-919 | s 9A(2)(b) | encoded | `consideration may be given to the material` (p2-written-law) | 4 |
| 920-921 | s 9A(2)(b)(i) | encoded | `consideration may be given to the material` (p2-written-law) | 4 |
| 922-931 | s 9A(2)(b)(ii) | encoded | `consideration may be given to the material` (p2-written-law) | 4 |
| 932-935 | s 9A(3) | fork | F25: s 9A(3) only includes; material it does not name returns NOTHING -- `section 9A(3) names the material as material that may be considered` (p2-written-law) | 7 |
| 936-942 | s 9A(3)(a) | encoded | `section 9A(3) names the material as material that may be considered` (p2-written-law) | 7 |
| 943-945 | s 9A(3)(b) | encoded | `section 9A(3) names the material as material that may be considered` (p2-written-law) | 7 |
| 946-950 | s 9A(3)(c) | encoded | `section 9A(3) names the material as material that may be considered` (p2-written-law) | 7 |
| 951-953 | s 9A(3)(d) | encoded | `section 9A(3) names the material as material that may be considered` (p2-written-law) | 7 |
| 954-956 | s 9A(3)(e) | encoded | `section 9A(3) names the material as material that may be considered` (p2-written-law) | 7 |
| 957-959 | s 9A(3)(f) | encoded | `section 9A(3) names the material as material that may be considered` (p2-written-law) | 7 |
| 960-964 | s 9A(4) | encoded | `the matters to which regard must be had in deciding whether to consider material and what weight to give it` (p2-written-law) | 1 |
| 965-969 | s 9A(4)(a) | encoded | `the matters to which regard must be had in deciding whether to consider material and what weight to give it` (p2-written-law) | 1 |
| 970-975 | s 9A(4)(b) | encoded | `the matters to which regard must be had in deciding whether to consider material and what weight to give it` (p2-written-law) | 1 |
| 976-977 | s 9B marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 978-979 | s 9B | encoded | `the ideas are taken to be different merely because the forms of words differ` (p2-written-law) | 3 |
| 980-982 | s 9B(a) | encoded | `the ideas are taken to be different merely because the forms of words differ` (p2-written-law) | 3 |
| 983-991 | s 9B(b) | encoded | `the ideas are taken to be different merely because the forms of words differ` (p2-written-law) | 3 |
| 992-993 | s 10 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 994-996 | s 10(1) | fork | F15: the day is fixed by the law or a notification, or is the Gazette date; any other way of fixing it returns NOTHING; the moment is the start of that day -- `the expiration of the day before` (interpretation-time); `the first moment of the day` (interpretation-time); `the moment a written law comes into operation` (interpretation-time) | 6 |
| 997-1001 | s 10(1)(a) | fork | F15: see s 10(1) -- `the expiration of the day before` (interpretation-time); `the first moment of the day` (interpretation-time); `the moment a written law comes into operation` (interpretation-time) | 6 |
| 1002-1005 | s 10(1)(b) | fork | F15: see s 10(1) -- `the expiration of the day before` (interpretation-time); `the first moment of the day` (interpretation-time); `the moment a written law comes into operation` (interpretation-time) | 6 |
| 1006-1010 | s 10(2) | encoded | `the day a notification brings a provision into operation` (interpretation-time) | 3 |
| 1011-1013 | s 11 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1014-1023 | s 11 | encoded | `the subsidiary legislation remains in force after the Act or part is repealed` (p2-written-law) | 5 |
| 1024-1025 | s 12 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1026-1030 | s 12 | encoded | `the last repeal revives the written law or provisions previously repealed` (p2-written-law) | 3 |
| 1031-1032 | s 13 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1033-1037 | s 13 | encoded | `the repeal is deemed to include the repeal of the amending written law` (p2-written-law) | 3 |
| 1038-1039 | s 14 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1040-1044 | s 14 | fork | F10: after the substituted provision comes into operation the Act says nothing about the repealed law, so the rule returns NOTHING -- `the repealed written law remains in force` (p2-written-law) | 3 |
| 1045-1046 | s 15 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1047-1051 | s 15(1) | encoded | `the reference includes the other written law as amended from time to time` (p2-written-law) | 3 |
| 1052-1055 | s 15(2) | encoded | `a reference to the provision repealed is construed as a reference to the provision re-enacted` (p2-written-law); `subsidiary legislation made or a thing done under the provision repealed has effect as if made or done under the provision re-enacted` (p2-written-law) | 7 |
| 1056-1059 | s 15(2)(a) | encoded | `a reference to the provision repealed is construed as a reference to the provision re-enacted` (p2-written-law) | 3 |
| 1060-1068 | s 15(2)(b) | encoded | `subsidiary legislation made or a thing done under the provision repealed has effect as if made or done under the provision re-enacted` (p2-written-law) | 4 |
| 1069-1070 | s 16 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1071-1074 | s 16(1) | encoded | `the repeal does this` (p2-written-law) | 7 |
| 1075-1077 | s 16(1)(a) | encoded | `the repeal does this` (p2-written-law) | 7 |
| 1078-1081 | s 16(1)(b) | encoded | `the repeal does this` (p2-written-law) | 7 |
| 1082-1084 | s 16(1)(c) | encoded | `the repeal does this` (p2-written-law) | 7 |
| 1085-1088 | s 16(1)(d) | encoded | `the repeal does this` (p2-written-law) | 7 |
| 1089-1096 | s 16(1)(e) | encoded | `it may be instituted, continued or enforced, or the penalty imposed, as if the repealing law had not been passed` (p2-written-law); `the repeal does this` (p2-written-law) | 10 |
| 1097-1099 | s 16(2) | encoded | `section 16 treats the event as a repeal` (p2-written-law) | 5 |
| 1100-1101 | s 16(2)(a) | encoded | `section 16 treats the event as a repeal` (p2-written-law) | 5 |
| 1102-1104 | s 16(2)(b) | encoded | `section 16 treats the event as a repeal` (p2-written-law) | 5 |
| 1105-1107 | s 16(2)(c) | encoded | `section 16 treats the event as a repeal` (p2-written-law) | 5 |
| 1108-1114 | s 16(3) | encoded | `section 16 treats the event as a repeal` (p2-written-law) | 5 |
| 1115-1118 | s 16(4) | encoded | `is a part of a written law for section 16` (p2-written-law) | 6 |
| 1119-1120 | s 17 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1121-1125 | s 17 | encoded | `the amending Act is construed as one with the amended Act and as part of it` (p2-written-law) | 4 |
| 1126-1127 | s 18 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1128-1133 | s 18 | encoded | `the proceeding may be continued as if the written law continued in force` (p2-written-law) | 4 |
| 1134-1137 | Part 3 heading | inert | reason 1 (a Part heading: groups the sections that follow and creates no rule) |  |
| 1138-1140 | s 19 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1141-1145 | s 19 | encoded | `subsidiary legislation may be amended, varied, rescinded or revoked at any time` (p3-subsidiary) | 4 |
| 1146-1150 | s 19(a) | encoded | `subsidiary legislation may be amended, varied, rescinded or revoked at any time` (p3-subsidiary) | 4 |
| 1151-1155 | s 19(a)(i) | encoded | `the power to fix the date includes the power to amend, revoke or suspend the subsidiary legislation fixing it` (p3-subsidiary) | 3 |
| 1156-1166 | s 19(a)(ii) | encoded | `the replacing authority may exercise the power over matters within its jurisdiction as if it were the original authority` (p3-subsidiary) | 3 |
| 1167-1173 | s 19(b) | encoded | `the enumeration of the special purposes derogates from the generality of the power` (p3-subsidiary) | 3 |
| 1174-1176 | s 19(c) | encoded | `subsidiary legislation made under an Act is permitted` (p3-subsidiary) | 3 |
| 1177-1178 | s 20 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1179-1180 | s 20 | encoded | `authority to make subsidiary legislation also includes` (p3-subsidiary) | 8 |
| 1181-1182 | s 20(a) | encoded | `authority to make subsidiary legislation also includes` (p3-subsidiary) | 8 |
| 1183-1187 | s 20(a)(i) | fork | F16: "or both" lets fine and imprisonment be combined, each within its own limit -- `authority to make subsidiary legislation also includes` (p3-subsidiary); `the penalty is within the limits of section 20(a)(i)` (p3-subsidiary) | 14 |
| 1188-1191 | s 20(a)(ii) | encoded | `authority to make subsidiary legislation also includes` (p3-subsidiary) | 8 |
| 1192-1195 | s 20(a)(iii) | encoded | `authority to make subsidiary legislation also includes` (p3-subsidiary) | 8 |
| 1196-1201 | s 20(a)(iv) | encoded | `authority to make subsidiary legislation also includes` (p3-subsidiary) | 8 |
| 1202-1207 | s 20(b) | encoded | `authority to make subsidiary legislation also includes` (p3-subsidiary) | 8 |
| 1208-1212 | s 20(b)(i) | encoded | `authority to make subsidiary legislation also includes` (p3-subsidiary) | 8 |
| 1213-1214 | s 20(b)(ii) | encoded | `authority to make subsidiary legislation also includes` (p3-subsidiary) | 8 |
| 1215-1217 | s 20(b)(ii)(A) | encoded | `authority to make subsidiary legislation also includes` (p3-subsidiary) | 8 |
| 1218-1223 | s 20(b)(ii)(B) | encoded | `authority to make subsidiary legislation also includes` (p3-subsidiary) | 8 |
| 1224-1226 | s 20(c) | fork | F26: s 20(c) prints no contrary-intention proviso and s 26A does; the two rules are coded as printed and can differ on the same facts -- `the reference includes any subsidiary legislation made under the other written law` (p3-subsidiary) | 2 |
| 1227-1228 | s 21 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1229-1233 | s 21 | encoded | `expressions in the subsidiary legislation have the same meanings as in the Act conferring the power` (p3-subsidiary) | 3 |
| 1234-1235 | s 22 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1236-1247 | s 22 | encoded | `the power may be exercised after the passing of the Act so as to take effect at any time after it` (p3-subsidiary) | 6 |
| 1248-1252 | s 22(a) | encoded | `the power may be exercised after the passing of the Act so as to take effect at any time after it` (p3-subsidiary) | 6 |
| 1253-1258 | s 22(b) | encoded | `the power may be exercised after the passing of the Act so as to take effect at any time after it` (p3-subsidiary) | 6 |
| 1259-1260 | s 23 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1261-1263 | s 23(1) | encoded | `subsidiary legislation must be published in the Gazette` (p3-subsidiary) | 2 |
| 1264-1266 | s 23(1)(a) | encoded | `subsidiary legislation must be published in the Gazette` (p3-subsidiary) | 2 |
| 1267-1270 | s 23(1)(b) | encoded | `the day subsidiary legislation takes effect and comes into operation` (p3-subsidiary) | 2 |
| 1271-1275 | s 23(2) | fork | F6: the date may be no earlier than the Act's commencement and, if the authority has an establishment date, no earlier than that too -- `the subsidiary legislation may be made to operate retrospectively to that date` (p3-subsidiary) | 5 |
| 1276-1277 | s 24 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1278-1280 | s 24 | encoded | `judicial notice is to be taken of the subsidiary legislation` (p3-subsidiary) | 2 |
| 1281-1282 | s 25 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1283-1288 | s 25 | encoded | `the amending subsidiary legislation is construed as one with the amended subsidiary legislation` (p3-subsidiary) | 4 |
| 1289-1291 | s 26 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1292-1300 | s 26 | encoded | `the act is deemed to be done under the Act` (p3-subsidiary) | 2 |
| 1301-1302 | s 26A marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1303-1306 | s 26A | fork | F26: see s 20(c) -- `the reference includes subsidiary legislation made under that Act` (p3-subsidiary) | 3 |
| 1307-1310 | Part 4 heading | inert | reason 1 (a Part heading: groups the sections that follow and creates no rule) |  |
| 1311-1312 | s 27 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1313-1317 | s 27(1) | encoded | `the power may be exercised and the duty must be performed from time to time as occasion requires` (p4-powers) | 3 |
| 1318-1323 | s 27(2) | encoded | `the person may exercise the power or must perform the duty` (p4-powers) | 5 |
| 1324-1331 | s 27(3) | encoded | `the power includes this, exercisable in like manner and subject to the like consent and conditions` (p4-powers) | 9 |
| 1332-1333 | s 28 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1334-1340 | s 28(1) | encoded | `the power to appoint includes this` (p4-powers) | 7 |
| 1341-1351 | s 28(2) | encoded | `the power of dismissal is exercisable` (p4-powers) | 4 |
| 1352-1353 | s 29 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1354-1358 | s 29(1) | fork | F26: s 29 prints no contrary-intention proviso and is coded as printed -- `the power is understood to be also conferred` (p4-powers) | 3 |
| 1359-1360 | s 29(2) | fork | F26: see s 29(1) -- `the power includes this, without limiting section 29(1)` (p4-powers) | 6 |
| 1361-1366 | s 29(2)(a) | encoded | `the power includes this, without limiting section 29(1)` (p4-powers) | 6 |
| 1367-1371 | s 29(2)(b) | encoded | `the power includes this, without limiting section 29(1)` (p4-powers) | 6 |
| 1372-1373 | s 30 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1374-1381 | s 30(1) | encoded | `the appointment is made in a way section 30 allows` (p4-powers) | 4 |
| 1382-1386 | s 30(2) | encoded | `the appointment is made in a way section 30 allows` (p4-powers) | 4 |
| 1387-1393 | s 30(3) | fork | F22: s 30(3) and s 32 are separate rules; each answers for its own section and nothing combines them -- `the appointment may be made with retrospective effect to that date` (p4-powers) | 3 |
| 1394-1395 | s 31 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1396-1403 | s 31 | encoded | `the public officer referred to includes this officer` (p4-powers) | 3 |
| 1404-1405 | s 32 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1406-1411 | s 32 | fork | F22: see s 30(3) -- `the day from which the appointment may be declared to have effect` (p4-powers) | 3 |
| 1412-1413 | s 32A marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1414-1418 | s 32A(1) | fork | F13, F23: "a majority of those persons" is more than half of all the persons the body consists of; (1) and (2)(b) are separate rules and nothing combines them -- `the power may be exercised or the function or duty performed by a majority of those persons` (p4-powers) | 7 |
| 1419-1420 | s 32A(2) | encoded | `a quorum is constituted at the meeting` (p4-powers); `the act or thing is regarded as done by the body` (p4-powers) | 15 |
| 1421-1423 | s 32A(2)(a) | encoded | `a quorum is constituted at the meeting` (p4-powers) | 9 |
| 1424-1427 | s 32A(2)(a)(i) | encoded | `a quorum is constituted at the meeting` (p4-powers) | 9 |
| 1428-1431 | s 32A(2)(a)(ii) | encoded | `a quorum is constituted at the meeting` (p4-powers) | 9 |
| 1432-1438 | s 32A(2)(b) | fork | F23: see s 32A(1); on the same facts (2)(b) and (1) can give different answers and the Act does not say which prevails -- `the act or thing is regarded as done by the body` (p4-powers) | 6 |
| 1439-1442 | s 32A(3) | encoded | `the chairperson or other member presiding has a casting as well as a deliberative vote` (p4-powers) | 4 |
| 1443-1445 | s 32A(4) | encoded | `the power may be exercised or the function or duty performed by a majority of those persons` (p4-powers) | 7 |
| 1446-1449 | s 32A(5) | encoded | `is a statutory body for section 32A` (p4-powers) | 3 |
| 1450-1451 | s 33 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1452-1456 | s 33 | encoded | `the powers of the body are affected` (p4-powers) | 6 |
| 1457-1458 | s 33(a) | encoded | `the powers of the body are affected` (p4-powers) | 6 |
| 1459-1462 | s 33(b) | encoded | `the powers of the body are affected` (p4-powers) | 6 |
| 1463-1465 | s 33(c) | encoded | `the powers of the body are affected` (p4-powers) | 6 |
| 1466-1467 | s 33A marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1468-1473 | s 33A | encoded | `the body may invest the moneys in the manner it thinks fit, and engage in financial activity or arrangements to manage or hedge risk from the investment` (p4-powers) | 3 |
| 1474-1475 | s 33A(a) | encoded | `the body may invest the moneys in the manner it thinks fit, and engage in financial activity or arrangements to manage or hedge risk from the investment` (p4-powers) | 3 |
| 1476-1485 | s 33A(b) | encoded | `the body may invest the moneys in the manner it thinks fit, and engage in financial activity or arrangements to manage or hedge risk from the investment` (p4-powers) | 3 |
| 1486-1487 | s 34 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1488-1495 | s 34(1) | encoded | `the exercise of the President's power is sufficiently signified` (p4-powers) | 5 |
| 1496-1499 | s 34(2) | encoded | `the exercise of the President's power is sufficiently signified` (p4-powers) | 5 |
| 1500-1501 | s 35 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1502-1511 | s 35 | encoded | `the exercise of the Minister's power is sufficiently signified` (p4-powers) | 4 |
| 1512-1513 | s 35A marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1514-1521 | s 35A(1) | encoded | `the power to delegate extends to making subsidiary legislation` (p4-powers) | 2 |
| 1522-1526 | s 35A(2) | encoded | `the exercise of the statutory body's power to make subsidiary legislation is sufficiently signified` (p4-powers) | 4 |
| 1527-1531 | s 35A(2)(a) | encoded | `the exercise of the statutory body's power to make subsidiary legislation is sufficiently signified` (p4-powers) | 4 |
| 1532-1536 | s 35A(2)(b) | encoded | `the exercise of the statutory body's power to make subsidiary legislation is sufficiently signified` (p4-powers) | 4 |
| 1537-1538 | s 36 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1539-1542 | s 36(1) | fork | F19: the delegates s 36(2) and (3) name are the only ones the section provides for; a delegation to anyone else returns NOTHING -- `the delegation is permitted by section 36` (p4-powers) | 10 |
| 1543-1547 | s 36(2) | fork | F19: see s 36(1) -- `the delegation is permitted by section 36` (p4-powers) | 10 |
| 1548-1550 | s 36(3) | fork | F19: see s 36(1) -- `the delegation is permitted by section 36` (p4-powers) | 10 |
| 1551-1552 | s 36(4) | encoded | `the delegate may exercise the function based on the delegate's own opinion, belief or state of mind` (p4-powers) | 3 |
| 1553-1555 | s 36(4)(a) | encoded | `the delegate may exercise the function based on the delegate's own opinion, belief or state of mind` (p4-powers) | 3 |
| 1556-1561 | s 36(4)(b) | encoded | `the delegate may exercise the function based on the delegate's own opinion, belief or state of mind` (p4-powers) | 3 |
| 1562-1563 | s 36(5) | encoded | `section 36(5) says a delegation` (p4-powers); `the delegation meets the requirement of form in section 36(5)(a)` (p4-powers) | 9 |
| 1564-1565 | s 36(5)(a) | encoded | `section 36(5) says a delegation` (p4-powers); `the delegation meets the requirement of form in section 36(5)(a)` (p4-powers) | 9 |
| 1566-1567 | s 36(5)(b) | encoded | `section 36(5) says a delegation` (p4-powers) | 7 |
| 1568-1570 | s 36(5)(c) | encoded | `section 36(5) says a delegation` (p4-powers) | 7 |
| 1571-1572 | s 36(5)(d) | encoded | `section 36(5) says a delegation` (p4-powers) | 7 |
| 1573-1574 | s 36(5)(e) | encoded | `section 36(5) says a delegation` (p4-powers) | 7 |
| 1575-1577 | s 36(5)(f) | encoded | `section 36(5) says a delegation` (p4-powers) | 7 |
| 1578-1579 | s 36(6) | encoded | `the delegation is permitted by section 36` (p4-powers) | 10 |
| 1580-1584 | s 36(6)(a) | encoded | `the delegation is permitted by section 36` (p4-powers) | 10 |
| 1585-1586 | s 36(6)(b) | encoded | `the delegation is permitted by section 36` (p4-powers) | 10 |
| 1587-1589 | s 36(7) | encoded | `the delegation is permitted by section 36` (p4-powers) | 10 |
| 1590-1593 | s 36(8) | encoded | `section 36 affects the operation of that rule of law` (p4-powers) | 1 |
| 1594-1595 | s 36(9) | encoded | `in section 36 a reference to an Act includes subsidiary legislation made under the Act` (p4-powers) | 1 |
| 1596-1598 | s 36(9)(a) | encoded | `in section 36 a reference to an Act includes subsidiary legislation made under the Act` (p4-powers) | 1 |
| 1599-1603 | s 36(9)(b) | encoded | `in section 36 a reference to an Act includes subsidiary legislation made under the Act` (p4-powers) | 1 |
| 1604-1608 | s 36(9)(c) | encoded | `in section 36 a reference to an Act includes subsidiary legislation made under the Act` (p4-powers) | 1 |
| 1609-1610 | s 37 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1611-1617 | s 37 | fork | F26: s 37 prints no contrary-intention proviso and is coded as printed -- `the requirement that a document be under the hand of or countersigned by a Minister is met` (p4-powers) | 3 |
| 1618-1621 | Part 5 heading | inert | reason 1 (a Part heading: groups the sections that follow and creates no rule) |  |
| 1622-1623 | s 38 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1624-1631 | s 38 | encoded | `an attempt to commit the offence is an offence against the provision, punishable as if the offence itself had been committed` (p5-penal-court) | 3 |
| 1632-1633 | s 39 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1634-1637 | s 39 | encoded | `the penalty relieves the person from liability to answer for damages to a person injured` (p5-penal-court) | 3 |
| 1638-1639 | s 40 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1640-1645 | s 40 | encoded | `the offender is liable to be prosecuted and punished under any one of those written laws` (p5-penal-court) | 4 |
| 1646-1647 | s 41 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1648-1653 | s 41 | encoded | `the most the offence is punishable by on conviction` (p5-penal-court) | 2 |
| 1654-1657 | Part 5A heading | inert | reason 1 (a Part heading: groups the sections that follow and creates no rule) |  |
| 1658-1659 | s 41A marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1660-1662 | s 41A(1) | encoded | `the process the application must be made by` (p5-penal-court) | 9 |
| 1663-1665 | s 41A(1)(a) | encoded | `the process the application must be made by` (p5-penal-court) | 9 |
| 1666-1676 | s 41A(1)(b) | encoded | `the process the application must be made by` (p5-penal-court) | 9 |
| 1677-1681 | s 41A(1)(c) | encoded | `the process the application must be made by` (p5-penal-court) | 9 |
| 1682-1690 | s 41A(1)(d) | encoded | `the process the application must be made by` (p5-penal-court) | 9 |
| 1691-1694 | s 41A(2) | encoded | `that provision has any effect in relation to the application` (p5-penal-court) | 3 |
| 1695-1697 | s 41A(2)(a) | encoded | `that provision has any effect in relation to the application` (p5-penal-court); `the application must be made in accordance with the Rules of Court` (p5-penal-court) | 5 |
| 1698-1705 | s 41A(2)(b) | encoded | `that provision has any effect in relation to the application` (p5-penal-court); `the Court may give the parties directions the Court thinks just and expedient to facilitate the progress of the application` (p5-penal-court) | 5 |
| 1706-1715 | s 41A(2)(c) | encoded | `that provision has any effect in relation to the application` (p5-penal-court) | 3 |
| 1716-1717 | s 41A(3) | encoded | `the process the application must be made by` (p5-penal-court) | 9 |
| 1718-1719 | s 41A(3)(a) | encoded | `the process the application must be made by` (p5-penal-court) | 9 |
| 1720-1724 | s 41A(3)(b) | encoded | `the process the application must be made by` (p5-penal-court) | 9 |
| 1725-1737 | s 41A(4) | encoded | `section 41A prevents the relief being included among the reliefs sought in an originating claim` (p5-penal-court) | 1 |
| 1738-1739 | s 41A(5) | encoded | `the application continues under the practice and procedure in force immediately before 1 April 2022` (p5-penal-court) | 5 |
| 1740-1744 | s 41A(5)(a) | encoded | `the application continues under the practice and procedure in force immediately before 1 April 2022` (p5-penal-court) | 5 |
| 1745-1754 | s 41A(5)(b) | encoded | `the application continues under the practice and procedure in force immediately before 1 April 2022` (p5-penal-court) | 5 |
| 1755-1756 | s 41A(6) | encoded | `is a Court for section 41A` (p5-penal-court) | 7 |
| 1757-1758 | s 41A(6)(a) | encoded | `is a Court for section 41A` (p5-penal-court) | 7 |
| 1759-1761 | s 41A(6)(b) | encoded | `is a Court for section 41A` (p5-penal-court) | 7 |
| 1762-1764 | s 41A(6)(ba) | encoded | `is a Court for section 41A` (p5-penal-court) | 7 |
| 1765-1766 | s 41A(6)(c) | encoded | `is a Court for section 41A` (p5-penal-court) | 7 |
| 1767-1768 | s 41A(6)(d) | encoded | `is a Court for section 41A` (p5-penal-court) | 7 |
| 1769-1772 | s 41A(6)(e) | fork | F21: a court counts if prescribed under s 41A(7); a court not shown to be prescribed returns NOTHING -- `is a Court for section 41A` (p5-penal-court) | 7 |
| 1773-1775 | s 41A(7) | inert | reason 2 (machinery: a power of the Minister to prescribe by order in the Gazette; the classes it would prescribe are the input `it is in a class prescribed under section 41A(7)`) |  |
| 1776-1778 | s 41A(7)(a) | inert | reason 2 (machinery: the order-making power of s 41A(7), limb (a)) |  |
| 1779-1785 | s 41A(7)(b) | inert | reason 2 (machinery: the order-making power of s 41A(7), limb (b); the courts it would prescribe are the choice `another court prescribed under section 41A(7)`) |  |
| 1786-1787 | s 41B marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1788-1795 | s 41B | encoded | `the prerogative order or writ issuable by the High Court is referred to as` (p5-penal-court); `the table of section 41B` (p5-penal-court) | 8 |
| 1796-1796 | s 41B(a) | encoded | `s 41B (a)` (p5-penal-court) | 3 |
| 1797-1798 | s 41B(b) | encoded | `s 41B (b)` (p5-penal-court) | 1 |
| 1799-1800 | s 41B(c) | encoded | `s 41B (c)` (p5-penal-court) | 1 |
| 1801-1804 | s 41B(d) | encoded | `s 41B (d)` (p5-penal-court) | 1 |
| 1805-1806 | s 41C marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1807-1808 | s 41C | encoded | `the reference to the High Court is read as` (p5-penal-court) | 6 |
| 1809-1813 | s 41C(a) | encoded | `the reference to the High Court is read as` (p5-penal-court) | 6 |
| 1814-1818 | s 41C(b) | encoded | `the reference to the High Court is read as` (p5-penal-court) | 6 |
| 1819-1826 | s 41C(c) | encoded | `the reference to the High Court is read as` (p5-penal-court) | 6 |
| 1827-1828 | s 41D marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1829-1841 | s 41D(1) | fork | F18: 41E displaces 41D(1) only for the matters 41E lists -- `the table of section 41D(1)` (p5-penal-court) | 1 |
| 1842-1843 | s 41D(1)(a) | encoded | `s 41D(1) (a)` (p5-penal-court) | 10 |
| 1844-1845 | s 41D(1)(b) | encoded | `s 41D(1) (b)` (p5-penal-court) | 5 |
| 1846-1846 | s 41D(1)(c) | encoded | `s 41D(1) (c)` (p5-penal-court) | 3 |
| 1847-1848 | s 41D(1)(d) | encoded | `s 41D(1) (d)` (p5-penal-court) | 2 |
| 1849-1851 | s 41D(1)(e) | encoded | `s 41D(1) (e)` (p5-penal-court) | 2 |
| 1852-1854 | s 41D(1)(f) | encoded | `s 41D(1) (f)` (p5-penal-court) | 2 |
| 1855-1857 | s 41D(1)(g) | encoded | `s 41D(1) (g)` (p5-penal-court) | 2 |
| 1858-1860 | s 41D(1)(h) | encoded | `s 41D(1) (h)` (p5-penal-court) | 4 |
| 1861-1864 | s 41D(1)(i) | encoded | `s 41D(1) (i)` (p5-penal-court) | 3 |
| 1865-1866 | s 41D(1)(j) | encoded | `s 41D(1) (j)` (p5-penal-court) | 2 |
| 1867-1868 | s 41D(1)(k) | encoded | `s 41D(1) (k)` (p5-penal-court) | 6 |
| 1869-1872 | s 41D(1)(l) | encoded | `s 41D(1) (l)` (p5-penal-court) | 2 |
| 1873-1881 | s 41D(2) | fork | F18: 41D(2) reverses only a reference to a second-column matter -- `the reference is construed as a reference to` (p5-penal-court) | 37 |
| 1882-1886 | s 41D(3) | repealed or blank | the text shows `(3) [Deleted by Act 19 of 2025 wef 05/12/2025]`; the stub `s 41D(3) is deleted` quotes it and a test asserts it | 1 |
| 1887-1889 | s 41E marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1890-1896 | s 41E | fork | F18: 41E displaces 41D(1) only for the matters 41E lists -- `the table of section 41E` (p5-penal-court) | 1 |
| 1897-1898 | s 41E(a) | encoded | `s 41E (a)` (p5-penal-court) | 5 |
| 1899-1900 | s 41E(b) | encoded | `s 41E (b)` (p5-penal-court) | 10 |
| 1901-1903 | s 41E(c) | encoded | `s 41E (c)` (p5-penal-court) | 3 |
| 1904-1905 | s 41E(d) | encoded | `s 41E (d)` (p5-penal-court) | 4 |
| 1906-1909 | s 41E(e) | encoded | `s 41E (e)` (p5-penal-court) | 3 |
| 1910-1916 | s 41E(f) | encoded | `s 41E (f)` (p5-penal-court) | 3 |
| 1917-1920 | Part 6 heading | inert | reason 1 (a Part heading: groups the sections that follow and creates no rule) |  |
| 1921-1923 | s 42 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1924-1933 | s 42(1) | encoded | `it is lawful to appoint the public officer by his or her official designation` (p6-misc) | 5 |
| 1934-1938 | s 42(2) | encoded | `the person for the time being holding or carrying out the duties of the office is a member of the board` (p6-misc) | 3 |
| 1939-1945 | s 42(3) | encoded | `it is lawful to appoint a chairperson of the body` (p6-misc) | 3 |
| 1946-1947 | s 43 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1948-1964 | s 43 | encoded | `the document is received as prima facie evidence without proof that the signature is that of the officer` (p6-misc) | 3 |
| 1965-1966 | s 44 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1967-1975 | s 44 | encoded | `the reference is read as referring to the person for the time being holding or carrying out the duties of that office in Singapore` (p6-misc) | 4 |
| 1976-1978 | s 45 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 1979-1984 | s 45(1) | fork | F17: where the amount cannot be known, the estimate stands in for the fee in (a) -- `the person, officer, department or authority may decline to do the thing` (p6-misc) | 5 |
| 1985-1986 | s 45(1)(a) | fork | F17: see s 45(1) -- `the person, officer, department or authority may decline to do the thing` (p6-misc) | 5 |
| 1987-1992 | s 45(1)(b) | fork | F17: see s 45(1) -- `the person, officer, department or authority may decline to do the thing` (p6-misc) | 5 |
| 1993-1996 | s 45(2) | encoded | `the adjustment after the thing has been done` (p6-misc) | 3 |
| 1997-1999 | s 46 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 2000-2006 | s 46(1) | encoded | `the Minister may by order published in the Gazette provide for fees or charges, charges and penalties for late payment, and interest` (p6-misc) | 3 |
| 2007-2008 | s 46(1)(a) | encoded | `the Minister may by order published in the Gazette provide for fees or charges, charges and penalties for late payment, and interest` (p6-misc) | 3 |
| 2009-2011 | s 46(1)(b) | encoded | `the Minister may by order published in the Gazette provide for fees or charges, charges and penalties for late payment, and interest` (p6-misc) | 3 |
| 2012-2015 | s 46(1)(c) | encoded | `the Minister may by order published in the Gazette provide for fees or charges, charges and penalties for late payment, and interest` (p6-misc) | 3 |
| 2016-2030 | s 46(2) | fork | F20: an item regulated by Rules of Court is outside the Minister's power and the Act says nothing more, so the rule returns NOTHING -- `the Minister may by order reduce, remit or refund it in whole or in part in the circumstances of a particular case` (p6-misc) | 3 |
| 2031-2032 | s 47 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 2033-2038 | s 47 | encoded | `the proceedings are discontinued or abated by the death, resignation, absence or removal from office` (p6-misc) | 2 |
| 2039-2040 | s 48 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 2041-2043 | s 48(1) | encoded | `the Gazette may be published in this form` (p6-misc) | 5 |
| 2044-2046 | s 48(2) | encoded | `the Gazette may be published in this form` (p6-misc) | 5 |
| 2047-2050 | s 48(3) | encoded | `the date a Gazette published in 2 or more forms is deemed published` (p6-misc) | 4 |
| 2051-2053 | s 48(4) | encoded | `the Gazette in this form is to be judicially noticed` (p6-misc) | 6 |
| 2054-2056 | s 48(4)(a) | encoded | `the Gazette in this form is to be judicially noticed` (p6-misc) | 6 |
| 2057-2058 | s 48(4)(b) | encoded | `the Gazette in this form is to be judicially noticed` (p6-misc) | 6 |
| 2059-2064 | s 48(4)(c) | encoded | `the Gazette in this form is to be judicially noticed` (p6-misc) | 6 |
| 2065-2071 | s 48(5) | encoded | `it is, in all courts and for all purposes, prima facie evidence of the matters published in it` (p6-misc) | 2 |
| 2072-2075 | s 48(6) | encoded | `this form prevails over the other form to the extent of any inconsistency` (p6-misc) | 26 |
| 2076-2079 | s 48(7) | encoded | `this form prevails over the other form to the extent of any inconsistency` (p6-misc) | 26 |
| 2080-2082 | s 48(8) | inert | reason 2 (machinery: a power of the Minister charged with Government publications to make regulations; the matters it would prescribe, such as another form of the Gazette, enter as plain inputs of the s 48 rules) |  |
| 2083-2084 | s 48(8)(a) | inert | reason 2 (machinery: the regulation-making power of s 48(8), limb (a)) |  |
| 2085-2086 | s 48(8)(b) | inert | reason 2 (machinery: the regulation-making power of s 48(8), limb (b)) |  |
| 2087-2092 | s 48(9) | encoded | `this form prevails over the other form to the extent of any inconsistency` (p6-misc) | 26 |
| 2093-2094 | s 48A marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 2095-2099 | s 48A(1) | encoded | `the document may be served this way` (p6-misc) | 14 |
| 2100-2101 | s 48A(1)(a) | encoded | `the document may be served this way` (p6-misc) | 14 |
| 2102-2103 | s 48A(1)(a)(i) | encoded | `the document may be served this way` (p6-misc) | 14 |
| 2104-2107 | s 48A(1)(a)(ii) | fork | F12: see s 2(5) -- `the document may be served this way` (p6-misc) | 14 |
| 2108-2109 | s 48A(1)(b) | encoded | `the document may be served this way` (p6-misc) | 14 |
| 2110-2112 | s 48A(1)(b)(i) | encoded | `the document may be served this way` (p6-misc) | 14 |
| 2113-2119 | s 48A(1)(b)(ii) | fork | F12: see s 2(5) -- `the document may be served this way` (p6-misc) | 14 |
| 2120-2121 | s 48A(1)(c) | encoded | `the document may be served this way` (p6-misc) | 14 |
| 2122-2124 | s 48A(1)(c)(i) | encoded | `the document may be served this way` (p6-misc) | 14 |
| 2125-2128 | s 48A(1)(c)(ii) | fork | F12: see s 2(5) -- `the document may be served this way` (p6-misc) | 14 |
| 2129-2130 | s 48A(2) | encoded | `section 48A(1) affects that other way of serving` (p6-misc) | 1 |
| 2131-2134 | s 48A(2)(a) | encoded | `section 48A(1) affects that other way of serving` (p6-misc) | 1 |
| 2135-2137 | s 48A(2)(b) | encoded | `section 48A(1) affects that other way of serving` (p6-misc) | 1 |
| 2138-2139 | s 49 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 2140-2143 | s 49 | encoded | `the distance is measured in a straight line on a horizontal plane` (p6-misc) | 3 |
| 2144-2145 | s 50 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 2146-2148 | s 50 | encoded | `section 50(c) treats the act as done in due time` (interpretation-time); `the last day of a period of days from the event` (interpretation-time); `the last day of the period once section 50(b) is applied` (interpretation-time) | 35 |
| 2149-2152 | s 50(a) | fork | F1, F2: a period of days FROM an event is counted with the event's day left out; AFTER an event is not named, so the chosen rules return NOTHING (the explicit not-covered value) -- `the first day of a period of days from the event` (interpretation-time); `the last day of a period of days from the event` (interpretation-time); `the last day of the period once section 50(b) is applied, if it reaches periods of days only` (interpretation-time) | 24 |
| 2153-2157 | s 50(b) | fork | F3, F4, F5: the last day is inside the period; the rule reaches the last day of every period (the other reading is also coded and tested); only Sundays and public holidays are excluded days -- `is an excluded day` (interpretation-time); `the last day of a period of days from the event` (interpretation-time); `the last day of the period after section 50(b)` (interpretation-time); `the last day of the period once section 50(b) is applied, if it reaches periods of days only` (interpretation-time); and 6 rule(s) in all | 47 |
| 2158-2166 | s 50(c) | encoded | `section 50(c) treats the act as done in due time` (interpretation-time); `the last day for an act directed for a day` (interpretation-time); `the last day of a period of days from the event` (interpretation-time) | 29 |
| 2167-2171 | s 50(d) | fork | F11: "a time not exceeding 6 days" is the number of days the law states, 1 to 6 -- `excluded days are not reckoned` (interpretation-time); `the last day of a period of days from the event` (interpretation-time); `the nth day that is not an excluded day after` (interpretation-time) | 25 |
| 2172-2173 | s 51 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 2174-2180 | s 51(1) | encoded | `a time of day is held to be standard time` (interpretation-time) | 2 |
| 2181-2185 | s 51(2) | encoded | `standard time, in hours ahead of UTC` (interpretation-time); `the moment on the UTC clock` (interpretation-time) | 8 |
| 2186-2187 | s 52 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 2188-2191 | s 52 | encoded | `the time for doing a thing` (interpretation-time) | 2 |
| 2192-2193 | s 53 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 2194-2200 | s 53 | encoded | `the power to extend may be exercised after the time has run out` (interpretation-time) | 3 |
| 2201-2202 | s 54 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 2203-2206 | s 54 | encoded | `the Act affects the rights of the Government` (p6-misc) | 3 |
| 2207-2207 | s 55 marginal heading | inert | reason 1 (a marginal heading: a label for the section below it, which the Act gives no operative role) |  |
| 2208-2209 | s 55 | encoded | `this Act binds the Government` (p6-misc) | 1 |
| 2210-3047 | legislative history (not part of the Act) | inert | reason 1 (the legislative history, which the text itself marks as not part of the Act) |  |

<!-- COVERAGE-TABLE:END -->

<!-- COVERAGE-SUMMARY:BEGIN -->

**Coverage summary** (printed by `gen-coverage.py` on every run):

- text lines 3046, of which non-blank 2042; units cut by `gen-units.py` 452; rows in the table 496 (the difference is the marginal headings given their own rows, less the single-line section rows that share their line with subsection (1))
- rows by disposition: `encoded` 351, `fork` 53, `inert` 89, `repealed or blank` 3
- `inert` by reason: reason 1 79, reason 2 10
- audit: non-blank lines in no row 0; lines in more than one row 0
- rules carrying an `@ref` 289; of them with no assertion 0
- fork-register entries that rows point at: F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23, F24, F25, F26

<!-- COVERAGE-SUMMARY:END -->

## Generators and checkers used and not shipped

Some files this document names were used while the encoding was written and are not in this folder: `coverage-dispositions.py`, `gen-coverage.py`, `gen-defs.py`, `gen-units.py`, `qx.py`.
They were scripts and tables written for one run and are not part of the encoding.
The counts and tables they produced are copied into this file, and the `.l4` modules, not the scripts, are the source of truth.
Where a script generated a module, the module in this folder is the file to edit, and its template is not shipped.
The lead keeps them outside this repository.

## Independent test pass

A separate agent that had not seen this encoding, its NOTES.md or its brief wrote `ANSWERS.md` from the text alone before it opened any `.l4` file: 658 numbered scenarios (529 over the Act, 93 seat questions in the individual's own facts, 36 added in a second round), including cases where the text is silent.
It then wrote `tests-independent.l4`, one `#ASSERT` per scenario that the encoding has a function for (900 assertions, because lettered sub-cases are separate), and ran it against this encoding with the stable binary.
`ANSWERS.md` is not kept in this folder; the scenario numbers `S<n>`, `B<n>` and `R<n>` in `tests-independent.l4` refer to it, and each assertion carries its provision.

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run against the first version of this encoding | 900 | 892 | 8 | 0 |
| after the changes below and the reconciliation | 900 | 900 | 0 | 0 |

The 68 scenarios the encoding has no function for are the `-- GAP` lines at the end of the test file; 36 of them are negative or instance questions about the s 2(1) table (see "Known limits").
Seven deliberately wrong control assertions failed in the author's run, so its harness can fail.

**What the eight disagreements turned out to be.** All eight had the same shape: the author expected `JUST FALSE` (or "No.") and the encoding answered `NOTHING` ("the Act does not say").

- **Two were an encoder defect, now fixed (R11, R13; s 48(6),(7)).**
  `this form prevails over the other form to the extent of any inconsistency` returned `JUST TRUE` for the winner and `NOTHING` for every other pair, so it could say who wins and never who loses.
  The loser now gets `JUST FALSE` (the website against print on or after the appointed date, print against the website before it); a pair neither subsection speaks to stays `NOTHING`.
  The seat has a new question for it.
- **Five are genuine forks, kept as `NOTHING` and registered:** s 14 "until the substituted provision comes into operation" (S244 and the seat question B31; F10, expanded); s 36(1)-(3) "in accordance with this section" (S351 and S355; F19); s 46(2) "(not being any fee ... regulated by Rules of Court)" (S452; F20).
  The author's own verdict was fork for S244, B31, S351 and S355 and "encoder, probably" for S452; each assertion is rewritten in place to the encoding's answer with a `-- RECONCILED` comment above it that quotes the original; none is deleted.
- **One was the author's error (S395):** s 41A(6)(e) adds "such other court as may be prescribed", so the list is open at the tail and `some other court` is not answered (F21).

The author's report also found, outside the failing assertions, that the "respectively" pairing of s 2(3)(l) was lost (one string for both the Judge and the Registrar); it is fixed, and each old expression now maps to its own replacement.
It also found that 21 entries of the s 2(1) table stored a list the Act prints as one item, so the encoding could only return the whole phrase; these now hold the printed phrase and each constituent (section "List members in the s 2(1) table"), and 21 printed items were checked and left whole, each with its reason.

**Known limits** are listed under "Known limits": negative and instance questions about the s 2(1) table, rule-side lists held as one constructor, the prescribing powers of ss 2A(7), 41A(7) and 48(8), and cut-off dates held as yes/no inputs.

**Check.** `check.sh` with `tests-independent.l4` in the folder: 19 modules, 2252 satisfied, 0 failed, 0 refused, and every module `same` on the `main` build, run on 2026-10-29. Dates in the author's file are written `Date day month year`, as in the encoding.
