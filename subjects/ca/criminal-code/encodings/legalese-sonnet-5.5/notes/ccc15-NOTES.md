# NOTES.md -- ccc15: the Criminal Code (Canada), R.S.C., 1985, c. C-46, lines 8524-8718 (Part XIV, Jurisdiction: sections 468 to 482.1)

Status (2026-11-16, part agent `ccc15`): layer 1, its tests, the regulative rules, the seat layer and its cases are written and pass.
How this was verified: every number below was produced by a command run after the last edit to a `.l4` file.
The commands are `check.sh` on the stable `l4` 1.6.110 against 1.6.109 (section "What check.sh prints"), `srcrefs.py check --refs` and `--strict` over every `ccc15-*.l4` file, `work/lint.py`, `work/coverage.py`, and a diff of the `#TRACE` outputs of the two builds.
The text is a plain-text rendering, made by a converter script, of the Justice Laws Website consolidation (current to 2026-09-30; last amended 2026-07-18).
It is not the official text, and nothing here is claimed verified against the official text.
The French version is equally authoritative and is not among the sources.
The quotation lines in the modules are whole lines of the text, inserted by script (`srcrefs.py quote`), never retyped.

Not done: the independent test pass that the `encoding-a-subject` workflow lists (`inputs/COMMONS-CLAUDE.md` line 20), which `inputs/KEEL-NOTES.md` line 255 describes as a fresh session that decides the answers before reading the encoding.
The brief forbids subagents, so none was used.
Every expected value was written by the agent that wrote the rules, from the text, before the run.

## What is encoded and what is not

Lines 8524-8718 hold the heading of Part XIV, its three division headings, and sections 468 to 482.1.
They cover which court may try an indictable offence (ss 468, 469), jurisdiction over the person (s 470), trial by jury and without a jury (ss 471, 473), the clerk's power to adjourn (s 474), the accused who absconds (s 475), where an offence is deemed committed (s 476), offences at sea and outside Canada (ss 477 to 477.4), the province in which an offence is tried and pleading guilty elsewhere (ss 478, 479), unorganized territory, offences not in a province, in Canadian waters and outside Canada (ss 480 to 481.2), the appearance of the accused (s 481.3), rules of court (s 482) and case management (s 482.1).
Every non-blank line of the range is in exactly one row of the coverage table, and every row has one disposition.
There is no `out-of-scope` and no `deferred` row.
Four headings are inert (reason 1, not operative).
Four units are shown repealed in the text (`s 469(a)(ii)`, `s 472`, `s 477.4(1) and (2)`, `s 482.1(6)`), carried as string constants with a test each.
Every other row is encoded or a fork.
The rule-making powers of ss 482(1) to (3), 482(5) and 482.1(1) are machinery (the brief's reason 2 for inert), but each is the source of the rules that apply to the accused's own case.
They are therefore encoded for what they decide (who may make rules, what the rules cover and reach, what follows for the accused) and are not left inert.
Not in this range, and taken as inputs from the parts or sections that own them: the section 2 terms, section 297 "newspaper", section 812 "appeal court", the provisions that give a trial without a jury elsewhere (the elections of s 536, line 11884, for example), and the provisions that displace the venue rule of s 478(1).

Files (all under `DEPOSIT/encodings/legalese-sonnet-5.5/`):
- layer 1: `ccc15-general.l4` (ss 468-475), `ccc15-special.l4` (ss 476-477.4), `ccc15-venue.l4` (ss 478-481.3), `ccc15-rules.l4` (ss 482, 482.1), `ccc15-duties.l4` (the regulative rules);
- tests: `ccc15-tests-general.l4`, `ccc15-tests-special.l4`, `ccc15-tests-venue.l4`, `ccc15-tests-rules.l4`, `ccc15-tests-duties.l4` (17 assertions and 26 `#TRACE`s);
- layer 2: `ccc15-seat.l4` and `ccc15-cases-seat.l4`;
- `NOTES.md`, `PROGRESS.md`.

`NEEDS-CORE.md` is not written: the core had every type and constructor needed.
The Party constructors named in `ccc15-duties.l4` are `the court`, `a judge` and `the clerk of the court`; its rules for `s 482.1(2)` and `(3)` take the party as an input, and `ccc15-tests-duties.l4` runs them with `the accused`, `the prosecutor` and `a justice`.
The other core types used are `Province or territory`, `Provision of the Code`, `Class of offence` and `Mode of proceeding`.
The modules are assembled from sources in `DEPOSIT/../work/src/` (not shipped) by `work/build.py`, which inserts the `-- src:N | ...` quotation lines mechanically from the text.

## Where this brief governs over PLAN.md, and where PLAN.md governs

- The brief says layer 1 imports `ccc-core.l4` and `ccc-definitions.l4`; PLAN.md section 1 says a part gets the core only and takes every section 2 answer as an input.
  Layer 1 imports `ccc-core` only (plus `prelude`, and `daydate` in `ccc15-special.l4`) and takes each section 2 answer as an input.
  The seat layer imports `ccc-definitions` as well and computes those inputs by calling the keel's `s 2 ...` functions from the court and province the accused names, so the answer is the keel's and is not restated here.
- Input names follow PLAN.md section 3, rule R4, and section 4: an answer taken from another part or from section 2 is an input named for the section it comes from, `s <label> <what is asked>`, and for section 2 terms `s 2 <term>: <the thing asked>`.
  The cross-part inputs (ten names, covering the section 2 terms, section 297 and section 812) are listed in "Seams (ccc15)".
  Answers taken from another function of this same part are wired in under the name of the thing asked followed by `, by s <label>`.
- The brief (2026-11-12, "three limits") gives a function named for a grant or a power the answer `NOTHING`, not `JUST FALSE`, when an "if" gate fails.
  It is applied at the eight sites of fork F5, and the two groups the brief says not to decide are listed with counts (F6, F7).
- Every constructor and type declared here begins with its section label, including the constructors that mean "not covered" (`s 477(2) something else`, `s 481.3 another matter`, `s 482(2) another court that no paragraph names`).
- The brief names the tests `ccc15-tests-*.l4`, where PLAN.md's example puts `-tests` last; the brief governs.

## Seat

The seat is a person who is, or may be, accused of an offence under the Criminal Code (the accused).
The brief fixes it: they ask, on facts they can state, whether what they did is an offence, what its gravity and penalty are, what defences, rights and procedures apply at each stage from arrest through trial, sentence and appeal, and what follows from a conviction.
(Assumed, not ruled: Singapore's Penal Code is the model, per the maintainer's instruction of 2026-11-09, but this is a plain seat layer with no charge-generator contract.)
Part XIV answers, for that person: which court may try them (ss 468 to 471), whether they must have a jury (ss 471, 473), what happens if they abscond (s 475), where the offence is treated as committed (s 476), what follows for an offence at sea or abroad (ss 477 to 477.4), in which province they may be tried and may plead guilty (ss 478 to 481.3), and what the rules of court and case management ask of them (ss 482, 482.1).
`ccc15-seat.l4` has 59 `@export` questions, each named "Under section N, ...", grouped under `§` headings in the text's order.
A heading for a situation the accused may not be in (a trial with no jury panel, absconding, a trial at sea, pleading guilty in another province, case management) says so in its comment, so the form can ask "Has this happened to you?" first.

There is no seat for an official.
The provisions that address only an official are encoded in layer 1 for what they decide, and asked in layer 2 only for what they mean to the accused.
The clerk's powers are asked as "may the clerk adjourn my court"; the rule-making powers are asked only as "do the rules apply to my case"; the Governor in Council's power is asked only as "do the uniform rules prevail".
The rule-making powers of ss 482(3) and 482.1(1), and the court list of s 482(2) as a power, have no seat question.

Inputs are plain: yes or no, a number, a date, or a choice from a list (the core's `Province or territory`, `Class of offence` and `Mode of proceeding`, the keel's `s 2 named court`, and this part's own small choice types).
The seat builds this part's records inside each question's `WHERE` or arguments from those inputs and calls the layer-1 rule; it restates no rule.
Placeholders in the seat, each with a comment in the file:
- `s 477(1) ship` and `s 477(2)` fix the provision at 477.1, because the questions are about sections 477.1 to 477.4;
- `s 477.3(2)` fixes "the person is a justice or judge" as `JUST TRUE`, because the question names a justice or judge;
- `s 478(5)` fixes the provision at 478;
- the `s 476` question gives every paragraph other than the one the accused chose a fixed "not that circumstance" value, so only the chosen paragraph can answer;
- the `s 477.2` questions ask for a consent date even when there is no consent yet (the description says "give any date"); it is read only when the consent has been given.

Questions that take another provision's answer as a plain fact the accused can state, so as not to ask the same facts twice (fork F18):
- `s 477.3(1)` and `s 477.3(2)` take "does section 477.1 apply to what I did", which `Under section 477.1, ...` answers from its own facts;
- the three questions after the first under `s 478(3)`, and those under `s 479`, take "I have appeared as the subsection allows", which the first question under each answers;
- `s 471` takes "a provision of the Code expressly provides that I am to be tried without a jury", of which `Under section 473(1), ...` answers one route;
- `s 470` takes "another provision of the Code takes the competence away";
- `s 478(1)` takes "another provision of the Code displaces the bar", and `s 481.2` takes "another provision of an Act of Parliament limits the section".

This part has one seat, so there are no mirror cases between seats.

### Reading a result: FALSE and NOTHING (ccc15)

72 of the 74 layer-1 functions answer a `MAYBE BOOLEAN`.
Two helpers differ: `s 477.2 the consent was not obtained not later than eight days after the proceedings were commenced` answers a `BOOLEAN`, and `s 477.2 the last day on which the consent of the Attorney General of Canada may be obtained` answers a `DATE`.
In the accused's terms:
- `JUST TRUE` is a "yes" on the text's own words.
  Examples: the Ontario Court of Justice has jurisdiction to try an indictable offence that is not one of those listed in section 469; the Attorney General's consent was obtained on the eighth day, so the proceedings are not barred.
- `JUST FALSE` is a "no" because the text says no in its own words.
  The words are a "where", an "if" or an "unless" that the facts do not meet, an "other than" or "except" carve-out, a flat negative ("is not entitled", "does not apply", "shall not be withdrawn unless"), or a period or distance the text fixes in its own words ("within five hundred metres", "on the day of the opening of the term or sittings").
  Example: a court of criminal jurisdiction does not have jurisdiction to try murder, because section 469 says "other than" and lists it.
  Every such branch carries `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`.
- `NOTHING` is "not covered".
  The text is silent (it does not say whether an offence that is both indictable and punishable on summary conviction is "an indictable offence"), points outside the sources (what a section 2 term, section 297 or section 812 answers is an input), leaves a list open ("includes", a list of courts that "may" make rules and does not say "only"), or limits a grant or a prohibition in its own wording ("with the consent of", "on the instructions of", "without the consent of", "an offence listed in section 469", "if a judge is not present") and the case falls outside the limit.
  It is not "no": an accused who is told `NOTHING` has not been told that the section refuses them anything, only that this section does not decide it.
  Every such branch carries `-- NOTHING-kind (<why>)`, where <why> is one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- A caller never turns `NOTHING` into `FALSE`.
  Every input that is another provision's answer is a `MAYBE BOOLEAN`, and a `NOTHING` from it is carried through as `NOTHING`.
- A bar is titled as the bar: `s 473(2) the withdrawal of the consent is barred`, `s 477.2(1) the proceedings are barred ...`, `s 477.3(3) the powers are barred ...`, `s 478(1) a court in a province is barred ...`.
  `JUST TRUE` means barred, `JUST FALSE` means this subsection does not bar it, and `NOTHING` means the subsection does not speak to the case.
  Negating a bar's answer is not a grant: a bar's `JUST FALSE` is not "you may".
- `REFUSE` is not used: "not covered" is `NOTHING`, asserted with `EQUALS NOTHING`.

### Seat questions (59)

The list is generated from the code by `work/notes_build.py`: each question's name, and the layer-1 function its body calls.

1. Under section 468, does a superior court of criminal jurisdiction have jurisdiction to try the offence I am charged with?
   calls `s 468 the superior court of criminal jurisdiction has jurisdiction to try the offence`
2. Under section 469, is the offence I am charged with one of those listed in section 469?
   calls `s 469 the offence charged is one listed in section 469`
3. Under section 469, does a court of criminal jurisdiction have jurisdiction to try the offence I am charged with?
   calls `s 469 the court of criminal jurisdiction has jurisdiction to try the offence`
4. Under section 470, is the court competent to try me for the offence?
   calls `s 470 the court is competent to try the accused for the offence`
5. Under section 471, must I be tried by a court composed of a judge and jury?
   calls `s 471 the accused shall be tried by a court composed of a judge and jury`
6. Under section 473(1), may I be tried without a jury by a judge of a superior court of criminal jurisdiction?
   calls `s 473(1) the accused may be tried without a jury by a judge of a superior court of criminal jurisdiction`
7. Under section 473(1.1), may the judge order that another offence be tried by that judge together with the offence listed in section 469?
   calls `s 473(1.1) the judge of the superior court of criminal jurisdiction may order that any offence be tried by that judge in conjunction with the offence listed in section 469`
8. Under section 473(2), is the withdrawal of my consent to be tried without a jury barred?
   calls `s 473(2) the withdrawal of the consent is barred`
9. Under section 474(1), may the clerk of the court adjourn the court and its business to a later day, on the opening day of a term or sittings for which no jury panel is to be summoned, if no judge is present to preside?
   calls `s 474(1) the clerk of the court may adjourn the court and the business of the court to a subsequent day`
10. Under section 474(2), may the clerk of the court adjourn the court and its business to a later day on a judge's instructions?
   calls `s 474(2) the clerk of the court may adjourn the court and the business of the court to a subsequent day on the instructions of a judge`
11. Under section 475(1)(a), am I deemed to have waived my right to be present at my trial if I abscond?
   calls `s 475(1)(a) the accused is deemed to have waived the right to be present at the trial`
12. Under section 475(1)(b)(i), may the court continue my trial and proceed to a judgment or verdict in my absence?
   calls `s 475(1)(b)(i) the court may continue the trial and proceed to a judgment or verdict`
13. Under section 475(1)(b)(i), may the court sentence me in my absence if it finds me guilty?
   calls `s 475(1)(b)(i) the court may impose a sentence on the accused in the accused's absence`
14. Under section 475(1)(b)(ii), may the court adjourn my trial to await my appearance?
   calls `s 475(1)(b)(ii) the court may adjourn the trial to await the accused's appearance`
15. Under section 475(1), may the court continue my trial at any time after adjourning it to await my appearance?
   calls `s 475(1) the court may, at any time, continue a trial adjourned pursuant to subparagraph (b)(ii)`
16. Under section 475(2), may the court draw an inference adverse to me from the fact that I absconded?
   calls `s 475(2) the court may draw an inference adverse to the accused from the fact that the accused has absconded`
17. Under section 475(3), am I barred from having the part of my trial conducted in my absence re-opened?
   calls `s 475(3) the accused is not entitled to have any part of the proceedings conducted in the accused's absence re-opened`
18. Under section 475(4), does the section preserve my counsel's authority to continue to act for me when I abscond and my trial continues?
   calls `s 475(4) the subsection preserves any authority counsel for the accused has to continue to act for the accused in the proceedings`
19. Under section 476, is my offence treated as having been committed in this territorial division?
   calls `s 476 the offence is deemed to have been committed in the territorial division`
20. Under section 477(1), is the vessel a "ship" for sections 477.1 to 477.4?
   calls `s 477(1) ship`
21. Under section 477(2), do sections 477.1 to 477.4 limit the operation of another Act of Parliament or a court's jurisdiction apart from them?
   calls `s 477(2) the section limits the operation of any other Act of Parliament or the jurisdiction that a court may exercise apart from sections 477.1 to 477.4`
22. Under section 477.1, am I deemed to have committed the act or omission in Canada?
   calls `s 477.1 the person is deemed to have committed the act or omission in Canada`
23. Under section 477.2(1), are the proceedings barred from being continued for want of the Attorney General of Canada's consent?
   calls `s 477.2(1) the proceedings are barred from being continued for want of the consent of the Attorney General of Canada`
24. Under section 477.2(1), what is the last day by which the Attorney General of Canada's consent must be obtained for the proceedings to be continued?
   calls `s 477.2 the last day on which the consent of the Attorney General of Canada may be obtained`
25. Under section 477.2(2), are the proceedings barred from being continued for want of the Attorney General of Canada's consent, the courts having jurisdiction only by virtue of paragraph 477.1(a) or (b)?
   calls `s 477.2(2) the proceedings are barred from being continued for want of the consent of the Attorney General of Canada`
26. Under section 477.2(3), are the proceedings barred from being continued for want of the Attorney General of Canada's consent, the courts having jurisdiction only by virtue of paragraph 477.1(d) or (e)?
   calls `s 477.2(3) the proceedings are barred from being continued for want of the consent of the Attorney General of Canada`
27. Under section 477.2(4), has the Attorney General's consent been filed with the clerk of the court as the subsection requires?
   calls `s 477.2(4) the consent has been filed as the subsection requires`
28. Under section 477.3(1), may a power of arrest, entry, search or seizure be exercised at this place?
   calls `s 477.3(1) the power may be exercised at the place`
29. Under section 477.3(2), does a justice or judge in any territorial division in Canada have jurisdiction to authorize an arrest, entry, search or seizure, or an investigation or other ancillary matter, related to my offence?
   calls `s 477.3(2) a justice or judge in any territorial division in Canada has jurisdiction to authorize the matter`
30. Under section 477.3(3), are the powers barred from being exercised outside Canada without the Attorney General of Canada's consent?
   calls `s 477.3(3) the powers are barred from being exercised outside Canada without the consent of the Attorney General of Canada`
31. Under section 477.4(3), is the certificate conclusive proof of the truth of its statement, without proof of the signature or official character of the person who appears to have issued it?
   calls `s 477.4(3) the certificate is conclusive proof of the truth of the statement without proof of the signature or official character of the person appearing to have issued it`
32. Under section 477.4(4), is the certificate admissible in evidence in my proceedings?
   calls `s 477.4(4) the certificate is admissible in evidence in the proceedings`
33. Under section 477.4(4), is it the case that the production of the certificate cannot be compelled?
   calls `s 477.4(4) the production of the certificate cannot be compelled`
34. Under section 478(1), is a court in a province barred from trying an offence committed entirely in another province?
   calls `s 478(1) a court in a province is barred from trying an offence committed entirely in another province`
35. Under section 478(2), am I dealt with, indicted, tried and punished in the province where I reside or in which the newspaper is printed?
   calls `s 478(2) the person is dealt with, indicted, tried and punished in the province where the person resides or in which the newspaper is printed`
36. Under section 478(3), may I appear before a court or judge that would have had jurisdiction to try the offence if it had been committed in the province where I am, when I am charged with an offence alleged to have been committed in Canada outside that province?
   calls `s 478(3) the accused may appear before a court or judge that would have had jurisdiction to try the offence if it had been committed in the province where the accused is`
37. Under section 478(3), shall the court or judge determine me to be guilty and impose the punishment warranted by law?
   calls `s 478(3) the court or judge shall determine the accused to be guilty of the offence and impose the punishment warranted by law`
38. Under section 478(3), shall I be returned to custody?
   calls `s 478(3) the accused shall be returned to custody`
39. Under section 478(3), shall I be dealt with according to law?
   calls `s 478(3) the accused shall be dealt with according to law`
40. Under section 478(4), am I deemed simply to stand charged of the offence, without a preliminary inquiry or an indictment?
   calls `s 478(4) the accused is deemed simply to stand charged of the offence without a preliminary inquiry having been conducted or an indictment having been preferred`
41. Under section 478(5), is the publication a newspaper, as section 297 defines the word, for the purposes of section 478?
   calls `s 478(5) newspaper`
42. Under section 479, may I appear before a court or judge that would have had jurisdiction to try the offence if it had been committed in the place where I am, when I am charged with an offence alleged to have been committed in the province where I am?
   calls `s 479 the accused may appear before a court or judge that would have had jurisdiction to try the offence if it had been committed in the place where the accused is`
43. Under section 479, shall the court or judge determine me to be guilty and impose the punishment warranted by law?
   calls `s 479 the court or judge shall determine the accused to be guilty of the offence and impose the punishment warranted by law`
44. Under section 479, shall I be returned to custody?
   calls `s 479 the accused shall be returned to custody`
45. Under section 479, shall I be dealt with according to law?
   calls `s 479 the accused shall be dealt with according to law`
46. Under section 480(1), may proceedings be commenced and may I be charged, tried and punished within this territorial division or provisional judicial district for an offence in an unorganized tract?
   calls `s 480(1) proceedings may be commenced and the accused may be charged, tried and punished within the territorial division or provisional judicial district`
47. Under section 480(2), does the jurisdiction conferred by section 480(1) continue after a new district or division is constituted in the tract?
   calls `s 480(2) subsection (2) continues the jurisdiction conferred by subsection (1)`
48. Under section 481, may proceedings be commenced and may I be charged, tried and punished within this territorial division for an offence in a part of Canada not in a province?
   calls `s 481 proceedings may be commenced and the accused may be charged, tried and punished within the territorial division`
49. Under section 481.1, may proceedings be commenced and may I be charged, tried and punished within this territorial division for an offence in Canadian waters?
   calls `s 481.1 proceedings may be commenced and the accused may be charged, tried and punished within the territorial division`
50. Under section 481.2, may proceedings be commenced and may I be charged, tried and punished within this territorial division for an act or omission committed outside Canada?
   calls `s 481.2 proceedings may be commenced and the accused may be charged, tried and punished within the territorial division`
51. Under section 481.3, do the provisions of the Criminal Code on my appearance at proceedings apply to proceedings commenced under section 481, 481.1 or 481.2?
   calls `s 481.3 the provisions of this Act relating to the matter apply to the proceedings`
52. Under section 482(1), do the rules of court made by the court that is to hear my case apply to my prosecution, proceeding, action or appeal?
   calls `s 482(1) the rules so made apply to the prosecution, proceeding, action or appeal`
53. Under section 482(2), are the rules of court made by the court that is to hear my case applicable to my prosecution, proceeding, action or appeal?
   calls `s 482(2) the rules so made are applicable to the prosecution, proceeding, action or appeal`
54. Under section 482(4), have the rules of court been published or otherwise made available to the public as the subsection requires?
   calls `s 482(4) the rules of court have been published or otherwise made available to the public as the subsection requires`
55. Under section 482(5), do the uniform rules made by the Governor in Council prevail and have effect as if enacted by the Criminal Code?
   calls `s 482(5) the uniform rules prevail and have effect as if enacted by this Act`
56. Under section 482.1(2), have I complied with the case management direction as the subsection requires?
   calls `s 482.1(2) the party has complied with the direction as the subsection requires`
57. Under section 482.1(3), may a court, justice or judge issue a summons or warrant to compel my presence at case management proceedings?
   calls `s 482.1(3) a court, justice or judge may issue a summons or warrant to compel the presence of the accused at case management proceedings`
58. Under section 482.1(4), do sections 512 and 512.3 apply to the issuing of a summons or warrant to compel my presence at case management proceedings?
   calls `s 482.1(4) the provision applies, with any modifications that the circumstances require, to the issuance of the summons or warrant`
59. Under section 482.1(5), do subsections 482(4) and (5) apply to the rules of court for case management?
   calls `s 482.1(5) the provision applies, with any modifications that the circumstances require, to the rules`

### Seat-title audit (second pass of 2026-11-12)

Every seat question's name and `@export` text were read against the body of the layer-1 function it calls, not against its own title: 59 read, 5 retitled, 54 read and left.
The first pass (against the titles) had already retitled two: `Under section 477.4(4), is it the case that the production of the certificate cannot be compelled` and `Under section 478(5), is the publication a newspaper, as section 297 defines the word, for the purposes of section 478`.
A retitled question changes its name, its `@export` text and the assertions that name it.
Each affected assertion in `ccc15-cases-seat.l4` is restated in place with `-- RECONCILED 2026-11-12: was <the original assertion>; ...` (21 assertions); no expected value or argument of any of them differs from the restated original.

Retitled (the new name, and what the body answers):
1. `Under section 474(1), may the clerk of the court adjourn the court and its business to a later day, on the opening day of a term or sittings for which no jury panel is to be summoned, if no judge is present to preside` (scope).
   The old title named one of the three gates of the subsection (no panel to be summoned), so a `JUST FALSE` caused by the other two would have been misread.
2. `Under section 477.2(1), what is the last day by which the Attorney General of Canada's consent must be obtained for the proceedings to be continued` (modal).
   The body computes the commencement date plus eight days, a deadline for a condition on continuing the proceedings; the old title said "may be obtained", which reads as a permission and suggests a later consent is impossible.
3. `Under section 477.3(2), does a justice or judge in any territorial division in Canada have jurisdiction to authorize an arrest, entry, search or seizure, or an investigation or other ancillary matter, related to my offence` (limb).
   The old title dropped "or an investigation or other ancillary matter", which the function's input and the text both carry.
4. `Under section 478(3), may I appear before a court or judge that would have had jurisdiction to try the offence if it had been committed in the province where I am, when I am charged with an offence alleged to have been committed in Canada outside that province` (scope and qualifier).
   The old title said "another province" (the text says "in Canada outside the province", which takes in the territories) and added "to plead guilty", a purpose the permission to appear does not carry: the plea decides what follows the appearance, in the questions after it.
5. `Under section 479, may I appear before a court or judge that would have had jurisdiction to try the offence if it had been committed in the place where I am, when I am charged with an offence alleged to have been committed in the province where I am` (qualifier).
   The same "to plead guilty" qualifier is removed.

By class: one modal (item 2), four scope or limb or qualifier (items 1, 3, 4, 5); none of the five is a polarity error.

Read and left, with a reason where it was a close call:
- `Under section 475(3), am I barred from having the part of my trial conducted in my absence re-opened`: "barred" and the function's "is not entitled" give the accused the same answer (`JUST TRUE` is "not entitled"); wording.
- `Under section 477(1), is the vessel a "ship" for sections 477.1 to 477.4`: "vessel" is the first limb of the text's own definition and is an input of the function; the function can only answer `JUST TRUE` or `NOTHING` ("includes"), which the question does not claim otherwise.
- `Under section 477.2(1), are the proceedings barred from being continued for want of the Attorney General of Canada's consent`: the "Under section 477.2(1)" prefix scopes the answer to that subsection, whose own words are the function's name; the sibling titles for subsections (2) and (3) carry their route because those subsections' own words do.
- `Under section 480(2), does the jurisdiction conferred by section 480(1) continue after a new district or division is constituted in the tract`: the constitution of the district is the subsection's own "where", and an input of the function.
- `Under section 481.3, do the provisions of the Criminal Code on my appearance at proceedings apply ...`: the function's `matter` input names both limbs (the requirement of the appearance and the exceptions to it); "on my appearance" covers both.
- `Under section 482.1(4)` and `Under section 482.1(5)`: the titles restate the subsection's own claim (sections 512 and 512.3; subsections 482(4) and (5)) and the function answers per section named, `JUST TRUE` for each of those and `NOTHING` for any other.
- The other 47 questions restate the function's own name, differing from it only by "my" for "the", a synonym, or a status the function tests as an input.

## Rulings applied (copied from the brief)

The brief says each ruling is recorded again, word for word, in the NOTES of each row that carries that rule's `NOTHING-kind` tags.
These are copied by `work/notes_build.py` from `BRIEF.md`, line for line; the fork register applies them.

> **A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails (ruling of 2026-11-12, three limits).** A layer-1 function NAMED for a grant or a power ("may", "is permitted to", "has power to") that answers `JUST FALSE` because an "if" gate failed reads as "may not", a grant turned into a bar. The guide's "In short" sentence gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit". (1) Answer `NOTHING` for such a function, with one fork line in NOTES.md (fork register and marginal readings) that names the other reading. (2) Keep `JUST FALSE` wherever the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question. (3) Do NOT decide two groups by yourself; list them in the fork register with a count and leave the answer as the guide's rulings give it: "may" functions whose gate is "where", "when" or "upon" (ruling (b) says `JUST FALSE`, the line on grants points the other way: a question for a lawyer), and "entitled"-named functions (a claim, not a power).

> - **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## Coverage (ccc15)

One row per unit of the text, with exactly one disposition and the layer-1 name that encodes it.
`work/units.py` cuts lines 8524-8718 into units (the four headings, then each section, subsection, paragraph and subparagraph, with a marginal note belonging to the unit it heads, and the six unlabelled tails that follow a list); `work/coverage.py` builds the table below and audits it.
The audit: 138 units, 138 rows, 191 non-blank lines in the range, and every non-blank line is in exactly one row.
A count of the text that does not use `units.py`: 128 lines of the range begin with a section number or a `(n)` / `(a)` / `(i)` label; 138 rows less the four headings and the six tails is 128, which equals that count.
Dispositions: 88 encoded, 42 fork, 4 inert (reason 1, headings), 4 repealed in the text (reason 3; each carried as a string constant with a test).
No row is `inert` for reason 2 and none is `out-of-scope` or `deferred`.
`fork (F..)` cites the fork register; the "asserts" column counts `#ASSERT`s in the test modules that name the rule (rules shared by several rows are counted in each row); the regulative twins of F19 are named in the "encoded by" column.

| unit | text lines | text begins | disposition | encoded by (layer 1) | asserts | seat questions |
| --- | --- | --- | --- | --- | --- | --- |
| PART XIV heading | 8524 | PART XIV Jurisdiction | inert (reason 1: not operative, a heading) | - | 0 | - |
| Division heading "General" | 8526 | General | inert (reason 1: not operative, a heading) | - | 0 | - |
| s 468 | 8527-8528 | 468 Every superior court of criminal jurisdiction has juri | fork (F1 hybrid) | `s 468 the superior court of criminal jurisdiction has jurisdiction to try the offence` | 5 | 1 |
| s 469 | 8529-8530 | 469 Every court of criminal jurisdiction has jurisdiction  | fork (F1 hybrid, F3 other-than) | `s 469 the court of criminal jurisdiction has jurisdiction to try the offence` | 7 | 2 |
| s 469(a) | 8531 | (a) an offence under any of the following sections: | fork (F2 closed-list) | `s 469 the offence charged is one listed in section 469` | 35 | - |
| s 469(a)(i) | 8532 | (i) section 47 (treason), | encoded | `s 469 the offence charged is one listed in section 469` | 35 | - |
| s 469(a)(ii) | 8533 | (ii) [Repealed, 2018, c. 29, s. 61] | repealed or blank in this text: the text shows "(ii) [Repealed, 2018, c. 29, s. 61]" | `s 469(a)(ii) as the text shows it` | 1 | - |
| s 469(a)(iii) | 8534 | (iii) section 51 (intimidating Parliament or a legislature | encoded | `s 469 the offence charged is one listed in section 469` | 35 | - |
| s 469(a)(iv) | 8535 | (iv) section 53 (inciting to mutiny), | encoded | `s 469 the offence charged is one listed in section 469` | 35 | - |
| s 469(a)(v) | 8536 | (v) section 61 (seditious offences), | encoded | `s 469 the offence charged is one listed in section 469` | 35 | - |
| s 469(a)(vi) | 8537 | (vi) section 74 (piracy), | encoded | `s 469 the offence charged is one listed in section 469` | 35 | - |
| s 469(a)(vii) | 8538 | (vii) section 75 (piratical acts), or | encoded | `s 469 the offence charged is one listed in section 469` | 35 | - |
| s 469(a)(viii) | 8539 | (viii) section 235 (murder); | encoded | `s 469 the offence charged is one listed in section 469` | 35 | - |
| s 469(b) | 8540-8541 | (b) the offence of being an accessory after the fact to hi | fork (F21 names-not-numbers) | `s 469 the offence charged is one listed in section 469` | 35 | - |
| s 469(c) | 8542 | (c) an offence under section 119 (bribery) by the holder o | encoded | `s 469 the offence charged is one listed in section 469` | 35 | - |
| s 469(c.1) | 8543-8544 | (c.1) an offence under any of sections 4 to 7 of the Crime | encoded | `s 469 the offence charged is one listed in section 469` | 35 | - |
| s 469(d) | 8545-8546 | (d) the offence of attempting to commit any offence mentio | encoded | `s 469 the offence charged is one listed in section 469` | 35 | - |
| s 469(e) | 8547-8548 | (e) the offence of conspiring to commit any offence mentio | encoded | `s 469 the offence charged is one listed in section 469` | 35 | - |
| s 470 | 8549-8550 | 470 Subject to this Act, every superior court of criminal  | fork (F4 subject-to, F5 if-on-power) | `s 470 the court is competent to try the accused for the offence` | 10 | 1 |
| s 470(a) | 8551 | (a) if the accused is found, is arrested or is in custody  | encoded | `s 470 the court is competent to try the accused for the offence` | 10 | - |
| s 470(b) | 8552 | (b) if the accused has been ordered to be tried by | encoded | `s 470 the court is competent to try the accused for the offence` | 10 | - |
| s 470(b)(i) | 8553 | (i) that court, or | encoded | `s 470 the court is competent to try the accused for the offence` | 10 | - |
| s 470(b)(ii) | 8554 | (ii) any other court, the jurisdiction of which has by law | encoded | `s 470 the court is competent to try the accused for the offence` | 10 | - |
| s 471 | 8555-8556 | 471 Except where otherwise expressly provided by law, ever | fork (F1 hybrid) | `s 471 the accused shall be tried by a court composed of a judge and jury` | 5 | 1 |
| s 472 | 8557 | 472 [Repealed, R.S., 1985, c. 27 (1st Supp.), s. 63] | repealed or blank in this text: the text shows "472 [Repealed, R.S., 1985, c. 27 (1st Supp.), s. 63]" | `s 472 as the text shows it` | 1 | - |
| s 473(1) | 8558-8559 | 473 (1) Notwithstanding anything in this Act, an accused c | encoded | `s 473(1) the accused may be tried without a jury by a judge of a superior court of criminal jurisdiction` | 7 | 1 |
| s 473(1.1) | 8560-8561 | (1.1) Where the consent of the accused and the Attorney Ge | fork (F6 where-on-power) | `s 473(1.1) the judge of the superior court of criminal jurisdiction may order that any offence be tried by that judge in conjunction with the offence listed in section 469`; `s 473(1.1) the judge's permission to order that any offence be tried in conjunction with the listed offence` | 4 + 2 traces | 1 |
| s 473(2) | 8562-8563 | (2) Notwithstanding anything in this Act, where the consen | fork (F8 bare-must, F9 unless-met) | `s 473(2) the withdrawal of the consent is barred` | 4 | 1 |
| s 474(1) | 8564-8565 | 474 (1) Where the competent authority has determined that  | fork (F6 where-on-power, F5 if-on-power) | `s 474(1) the clerk of the court may adjourn the court and the business of the court to a subsequent day`; `s 474(1) the clerk of the court's permission to adjourn when no jury panel is to be summoned` | 8 + 2 traces | 1 |
| s 474(2) | 8566-8567 | (2) A clerk of the court for the trial of criminal cases i | encoded | `s 474(2) the clerk of the court may adjourn the court and the business of the court to a subsequent day on the instructions of a judge`; `s 474(2) the clerk of the court's permission to adjourn on the instructions of a judge` | 5 + 2 traces | 1 |
| s 475(1) | 8568-8569 | 475 (1) Notwithstanding any other provision of this Act, w | fork (F6 where-on-power) | `s 475(1)(a) the accused is deemed to have waived the right to be present at the trial` | 2 | 1 |
| s 475(1)(a) | 8570 | (a) he shall be deemed to have waived his right to be pres | encoded | `s 475(1)(a) the accused is deemed to have waived the right to be present at the trial` | 2 | 1 |
| s 475(1)(b) | 8571 | (b) the court may | fork (F6 where-on-power) | `s 475(1)(b)(i) the court may continue the trial and proceed to a judgment or verdict` | 2 | - |
| s 475(1)(b)(i) | 8572 | (i) continue the trial and proceed to a judgment or verdic | fork (F6 where-on-power, F5 if-on-power) | `s 475(1)(b)(i) the court may continue the trial and proceed to a judgment or verdict`; `s 475(1)(b)(i) the court may impose a sentence on the accused in the accused's absence`; `s 475(1)(b)(i) the court's permission to continue the trial and proceed to a judgment or verdict` | 6 + 2 traces | 2 |
| s 475(1)(b)(ii) | 8573 | (ii) if a warrant in Form 7 is issued for the arrest of th | fork (F6 where-on-power, F5 if-on-power) | `s 475(1)(b)(ii) the court may adjourn the trial to await the accused's appearance`; `s 475(1)(b)(ii) the court's permission to adjourn the trial to await the accused's appearance` | 5 + 1 traces | 1 |
| s 475(1) proviso | 8574 | but where the trial is adjourned pursuant to subparagraph  | fork (F6 where-on-power, F5 if-on-power) | `s 475(1) the court may, at any time, continue a trial adjourned pursuant to subparagraph (b)(ii)`; `s 475(1) the court's permission to continue a trial adjourned pursuant to subparagraph (b)(ii)` | 5 + 1 traces | - |
| s 475(2) | 8575-8576 | (2) Where a court continues a trial pursuant to subsection | fork (F6 where-on-power) | `s 475(2) the court may draw an inference adverse to the accused from the fact that the accused has absconded`; `s 475(2) the court's permission to draw an adverse inference` | 3 + 1 traces | 1 |
| s 475(3) | 8577-8578 | (3) Where an accused reappears at his trial that is contin | fork (F7 entitled, F9 unless-met) | `s 475(3) the accused is not entitled to have any part of the proceedings conducted in the accused's absence re-opened` | 3 | 1 |
| s 475(4) | 8579-8580 | (4) Where an accused has absconded during the course of hi | encoded | `s 475(4) the subsection preserves any authority counsel for the accused has to continue to act for the accused in the proceedings` | 3 | 1 |
| Division heading "Special Jurisdiction" | 8582 | Special Jurisdiction | inert (reason 1: not operative, a heading) | - | 0 | - |
| s 476 | 8583-8584 | 476 For the purposes of this Act, | encoded | `s 476 the offence is deemed to have been committed in the territorial division` | 11 | 1 |
| s 476(a) | 8585 | (a) where an offence is committed in or on any water or on | encoded | `s 476(a) the offence is deemed to have been committed in the territorial division` | 3 | - |
| s 476(b) | 8586 | (b) where an offence is committed on the boundary of two o | fork (F12 metres) | `s 476(b) the offence is deemed to have been committed in the territorial division, the offence being committed on or within five hundred metres of the boundary`; `s 476(b) the offence is deemed to have been committed in the territorial division, the offence being commenced within one territorial division and completed within another` | 8 | - |
| s 476(c) | 8587 | (c) where an offence is committed in or on a vehicle emplo | fork (F13 road-boundary) | `s 476(c) the offence is deemed to have been committed in the territorial division, the offence being committed in or on a vehicle or on board a vessel`; `s 476(c) the offence is deemed to have been committed in the territorial division, the road or water on which the vehicle or vessel passed being the boundary of two or more territorial divisions` | 7 | - |
| s 476(d) | 8588 | (d) where an offence is committed in an aircraft in the co | encoded | `s 476(d) the offence is deemed to have been committed in the territorial division, the offence being committed in an aircraft in the course of a flight` | 5 | - |
| s 476(d)(i) | 8589 | (i) in the territorial division in which the flight commen | encoded | `s 476(d) the offence is deemed to have been committed in the territorial division, the offence being committed in an aircraft in the course of a flight` | 5 | - |
| s 476(d)(ii) | 8590 | (ii) in any territorial division over which the aircraft p | encoded | `s 476(d) the offence is deemed to have been committed in the territorial division, the offence being committed in an aircraft in the course of a flight` | 5 | - |
| s 476(d)(iii) | 8591 | (iii) in the territorial division in which the flight ende | encoded | `s 476(d) the offence is deemed to have been committed in the territorial division, the offence being committed in an aircraft in the course of a flight` | 5 | - |
| s 476(e) | 8592 | (e) where an offence is committed in respect of the mail i | encoded | `s 476(e) the offence is deemed to have been committed in the territorial division, the offence being committed in respect of the mail` | 3 | - |
| s 477(1) | 8593-8594 | 477 (1) In sections 477.1 to 477.4, ship includes any desc | encoded | `s 477(1) ship` | 8 | 1 |
| s 477(2) | 8595-8596 | (2) Nothing in sections 477.1 to 477.4 limits the operatio | encoded | `s 477(2) the section limits the operation of any other Act of Parliament or the jurisdiction that a court may exercise apart from sections 477.1 to 477.4` | 4 | 1 |
| s 477.1 | 8597-8598 | 477.1 Every person who commits an act or omission that, if | fork (F15 if-on-deeming) | `s 477.1 the person is deemed to have committed the act or omission in Canada` | 13 | 1 |
| s 477.1(a) | 8599 | (a) in the exclusive economic zone of Canada that | encoded | `s 477.1 the person is deemed to have committed the act or omission in Canada` | 13 | - |
| s 477.1(a)(i) | 8600 | (i) is committed by a person who is in the exclusive econo | encoded | `s 477.1 the person is deemed to have committed the act or omission in Canada` | 13 | - |
| s 477.1(a)(ii) | 8601 | (ii) is committed by or in relation to a person who is a C | encoded | `s 477.1 the person is deemed to have committed the act or omission in Canada` | 13 | - |
| s 477.1(b) | 8602 | (b) that is committed in a place in or above the continent | encoded | `s 477.1 the person is deemed to have committed the act or omission in Canada` | 13 | - |
| s 477.1(c) | 8603 | (c) that is committed outside Canada on board or by means  | encoded | `s 477.1 the person is deemed to have committed the act or omission in Canada` | 13 | - |
| s 477.1(d) | 8604 | (d) that is committed outside Canada in the course of hot  | encoded | `s 477.1 the person is deemed to have committed the act or omission in Canada` | 13 | - |
| s 477.1(e) | 8605 | (e) that is committed outside the territory of any state b | encoded | `s 477.1 the person is deemed to have committed the act or omission in Canada` | 13 | - |
| s 477.2(1) | 8606-8607 | 477.2 (1) No proceedings in respect of an offence committe | fork (F10 as-at-date, F11 eight-days-inclusive) | `s 477.2(1) the proceedings are barred from being continued for want of the consent of the Attorney General of Canada`; `s 477.2 the consent was not obtained not later than eight days after the proceedings were commenced`; `s 477.2 the last day on which the consent of the Attorney General of Canada may be obtained` | 20 | 2 |
| s 477.2(1.1) | 8608-8609 | (1.1) Subsection (1) does not apply to proceedings by way  | encoded | `s 477.2(1.1) subsection (1) does not apply to the proceedings` | 2 | - |
| s 477.2(2) | 8610-8611 | (2) No proceedings in respect of which courts have jurisdi | fork (F10 as-at-date) | `s 477.2(2) the proceedings are barred from being continued for want of the consent of the Attorney General of Canada`; `s 477.2 the consent was not obtained not later than eight days after the proceedings were commenced` | 15 | 1 |
| s 477.2(3) | 8612-8613 | (3) No proceedings in respect of which courts have jurisdi | fork (F10 as-at-date) | `s 477.2(3) the proceedings are barred from being continued for want of the consent of the Attorney General of Canada`; `s 477.2 the consent was not obtained not later than eight days after the proceedings were commenced` | 13 | 1 |
| s 477.2(4) | 8614-8615 | (4) The consent of the Attorney General required by subsec | fork (F8 bare-must) | `s 477.2(4) the consent has been filed as the subsection requires` | 4 | 1 |
| s 477.3(1) | 8616-8617 | 477.3 (1) Every power of arrest, entry, search or seizure  | fork (F3 other-than) | `s 477.3(1) the power may be exercised at the place` | 10 | 1 |
| s 477.3(1)(a) | 8618 | (a) at the place or on board the ship or marine installati | encoded | `s 477.3(1) the power may be exercised at the place` | 10 | - |
| s 477.3(1)(b) | 8619 | (b) where hot pursuit has been commenced, at any place on  | fork (F3 other-than) | `s 477.3(1) the power may be exercised at the place` | 10 | - |
| s 477.3(2) | 8620-8621 | (2) A justice or judge in any territorial division in Cana | encoded | `s 477.3(2) a justice or judge in any territorial division in Canada has jurisdiction to authorize the matter` | 7 | 1 |
| s 477.3(2)(a) | 8622 | (a) committed in or on the territorial sea of Canada or an | encoded | `s 477.3(2) a justice or judge in any territorial division in Canada has jurisdiction to authorize the matter` | 7 | - |
| s 477.3(2)(b) | 8623 | (b) referred to in section 477.1 | encoded | `s 477.3(2) a justice or judge in any territorial division in Canada has jurisdiction to authorize the matter` | 7 | - |
| s 477.3(2) tail | 8624 | in the same manner as if the offence had been committed in | encoded | `s 477.3(2) a justice or judge in any territorial division in Canada has jurisdiction to authorize the matter` | 7 | - |
| s 477.3(3) | 8625-8626 | (3) Where an act or omission that is an offence by virtue  | fork (F17 without-consent) | `s 477.3(3) the powers are barred from being exercised outside Canada without the consent of the Attorney General of Canada` | 5 | 1 |
| s 477.4(1) and (2) | 8627 | 477.4 (1) and (2) [Repealed, 1996, c. 31, s. 71] | repealed or blank in this text: the text shows "477.4 (1) and (2) [Repealed, 1996, c. 31, s. 71]" | `s 477.4(1) and (2) as the text shows them` | 1 | - |
| s 477.4(3) | 8628-8629 | (3) In proceedings in respect of an offence, | encoded | `s 477.4(3) the certificate is conclusive proof of the truth of the statement without proof of the signature or official character of the person appearing to have issued it`; `s 477.4(3) the certificate is one referred to in subsection (3)` | 9 | 1 |
| s 477.4(3)(a) | 8630 | (a) a certificate referred to in subsection 23(1) of the O | encoded | `s 477.4(3) the certificate is one referred to in subsection (3)` | 5 | - |
| s 477.4(3)(b) | 8631 | (b) a certificate issued by or under the authority of the  | fork (F14 certificate-statement) | `s 477.4(3) the certificate is one referred to in subsection (3)` | 5 | - |
| s 477.4(3) tail | 8632 | is conclusive proof of the truth of the statement without  | encoded | `s 477.4(3) the certificate is conclusive proof of the truth of the statement without proof of the signature or official character of the person appearing to have issued it` | 4 | - |
| s 477.4(4) | 8633-8634 | (4) A certificate referred to in subsection (3) is admissi | encoded | `s 477.4(4) the certificate is admissible in evidence in the proceedings`; `s 477.4(4) the production of the certificate cannot be compelled` | 6 | 2 |
| s 478(1) | 8635-8636 | 478 (1) Subject to this Act, a court in a province shall n | fork (F4 subject-to, F20 territories) | `s 478(1) a court in a province is barred from trying an offence committed entirely in another province`; `s 478(1) the prohibition on a court in a province from trying an offence committed entirely in another province` | 13 + 4 traces | 1 |
| s 478(2) | 8637-8638 | (2) Every proprietor, publisher, editor or other person ch | fork (F8 bare-must) | `s 478(2) the person is dealt with, indicted, tried and punished in the province where the person resides or in which the newspaper is printed` | 7 | 1 |
| s 478(3) | 8639-8640 | (3) An accused who is charged with an offence that is alle | fork (F5 if-on-power) | `s 478(3) the accused may appear before a court or judge that would have had jurisdiction to try the offence if it had been committed in the province where the accused is` | 8 | 4 |
| s 478(3)(a) | 8641 | (a) in the case of proceedings instituted at the instance  | encoded | `s 478(3) the accused may appear before a court or judge that would have had jurisdiction to try the offence if it had been committed in the province where the accused is` | 8 | - |
| s 478(3)(b) | 8642 | (b) in any other case, if the Attorney General of the prov | encoded | `s 478(3) the accused may appear before a court or judge that would have had jurisdiction to try the offence if it had been committed in the province where the accused is` | 8 | - |
| s 478(3) tail | 8643 | appear before a court or judge that would have had jurisdi | fork (F8 bare-must) | `s 478(3) the court or judge shall determine the accused to be guilty of the offence and impose the punishment warranted by law`; `s 478(3) the accused shall be returned to custody`; `s 478(3) the accused shall be dealt with according to law`; `s 478(3) the court's duty to determine the accused to be guilty and impose the punishment warranted by law` | 19 + 3 traces | - |
| s 478(4) | 8644-8645 | (4) Notwithstanding that an accused described in subsectio | encoded | `s 478(4) the accused is deemed simply to stand charged of the offence without a preliminary inquiry having been conducted or an indictment having been preferred` | 3 | 1 |
| s 478(5) | 8646-8647 | (5) In this section, newspaper has the same meaning as in  | encoded | `s 478(5) newspaper` | 5 | 1 |
| s 479 | 8648-8649 | 479 Where an accused is charged with an offence that is al | fork (F6 where-on-power, F5 if-on-power) | `s 479 the accused may appear before a court or judge that would have had jurisdiction to try the offence if it had been committed in the place where the accused is` | 7 | 4 |
| s 479(a) | 8650 | (a) in the case of proceedings instituted at the instance  | encoded | `s 479 the accused may appear before a court or judge that would have had jurisdiction to try the offence if it had been committed in the place where the accused is` | 7 | - |
| s 479(b) | 8651 | (b) in any other case, the Attorney General of the provinc | encoded | `s 479 the accused may appear before a court or judge that would have had jurisdiction to try the offence if it had been committed in the place where the accused is` | 7 | - |
| s 479 tail | 8652 | appear before a court or judge that would have had jurisdi | fork (F8 bare-must) | `s 479 the court or judge shall determine the accused to be guilty of the offence and impose the punishment warranted by law`; `s 479 the accused shall be returned to custody`; `s 479 the accused shall be dealt with according to law`; `s 479 the court's duty to determine the accused to be guilty and impose the punishment warranted by law` | 17 + 2 traces | - |
| s 480(1) | 8653-8654 | 480 (1) Where an offence is committed in an unorganized tr | fork (F6 where-on-power) | `s 480(1) proceedings may be commenced and the accused may be charged, tried and punished within the territorial division or provisional judicial district` | 3 | 1 |
| s 480(2) | 8655-8656 | (2) Where a provisional judicial district or a new territo | fork (F16 until) | `s 480(2) subsection (2) continues the jurisdiction conferred by subsection (1)` | 3 | 1 |
| s 481 | 8657-8658 | 481 Where an offence is committed in a part of Canada not  | fork (F6 where-on-power) | `s 481 proceedings may be commenced and the accused may be charged, tried and punished within the territorial division` | 3 | 1 |
| s 481.1 | 8659-8660 | 481.1 Where an offence is committed in or on the territori | fork (F6 where-on-power) | `s 481.1 proceedings may be commenced and the accused may be charged, tried and punished within the territorial division` | 3 | 1 |
| s 481.2 | 8661-8662 | 481.2 Subject to this or any other Act of Parliament, wher | fork (F4 subject-to, F6 where-on-power) | `s 481.2 proceedings may be commenced and the accused may be charged, tried and punished within the territorial division` | 6 | 1 |
| s 481.3 | 8663-8664 | 481.3 For greater certainty, the provisions of this Act re | encoded | `s 481.3 the provisions of this Act relating to the matter apply to the proceedings` | 6 | 1 |
| s 481.3(a) | 8665 | (a) the requirement of the appearance of an accused at pro | encoded | `s 481.3 the provisions of this Act relating to the matter apply to the proceedings` | 6 | - |
| s 481.3(b) | 8666 | (b) the exceptions to that requirement | encoded | `s 481.3 the provisions of this Act relating to the matter apply to the proceedings` | 6 | - |
| s 481.3 tail | 8667 | apply to proceedings commenced in any territorial division | encoded | `s 481.3 the provisions of this Act relating to the matter apply to the proceedings` | 6 | - |
| Division heading "Rules of Court" | 8669 | Rules of Court | inert (reason 1: not operative, a heading) | - | 0 | - |
| s 482(1) | 8670-8671 | 482 (1) Every superior court of criminal jurisdiction and  | encoded | `s 482(1) the court may make rules of court not inconsistent with this or any other Act of Parliament`; `s 482(1) the rules so made apply to the prosecution, proceeding, action or appeal` | 14 | 1 |
| s 482(2) | 8672-8673 | (2) The following courts may make rules of court not incon | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament`; `s 482(2) the rules so made are applicable to the prosecution, proceeding, action or appeal` | 31 | 1 |
| s 482(2)(a) | 8674 | (a) every court of criminal jurisdiction for a province; | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(2)(b) | 8675 | (b) every appeal court within the meaning of section 812 t | fork (F3 other-than) | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(2)(c) | 8676 | (c) the Ontario Court of Justice; | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(2)(d) | 8677 | (d) the Court of Quebec and every municipal court in the P | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(2)(e) | 8678 | (e) the Provincial Court of Nova Scotia; | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(2)(f) | 8679 | (f) the Provincial Court of New Brunswick; | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(2)(g) | 8680 | (g) the Provincial Court of Manitoba; | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(2)(h) | 8681 | (h) the Provincial Court of British Columbia; | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(2)(i) | 8682 | (i) the Provincial Court of Prince Edward Island; | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(2)(j) | 8683 | (j) the Provincial Court of Saskatchewan; | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(2)(k) | 8684 | (k) the Provincial Court of Alberta; | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(2)(l) | 8685 | (l) the Provincial Court of Newfoundland and Labrador; | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(2)(m) | 8686 | (m) the Territorial Court of Yukon; | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(2)(n) | 8687 | (n) the Territorial Court of the Northwest Territories; an | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(2)(o) | 8688 | (o) the Nunavut Court of Justice. | encoded | `s 482(2) the court may make rules of court not inconsistent with this Act or any other Act of Parliament` | 26 | - |
| s 482(3) | 8689-8690 | (3) Rules under subsection (1) or (2) may be made | encoded | `s 482(3) rules may be made for the purpose` | 22 | - |
| s 482(3)(a) | 8691 | (a) generally to regulate the duties of the officers of th | encoded | `s 482(3) rules may be made for the purpose` | 22 | - |
| s 482(3)(b) | 8692 | (b) to regulate the sittings of the court or any division  | encoded | `s 482(3) rules may be made for the purpose` | 22 | - |
| s 482(3)(c) | 8693 | (c) to regulate the pleading, practice and procedure in cr | encoded | `s 482(3) rules may be made for the purpose` | 22 | - |
| s 482(3)(d) | 8694 | (d) to carry out the provisions of this Act relating to ap | encoded | `s 482(3) rules may be made for the purpose` | 22 | - |
| s 482(3)(d)(i) | 8695 | (i) for furnishing necessary forms and instructions in rel | encoded | `s 482(3) rules may be made for the purpose` | 22 | - |
| s 482(3)(d)(ii) | 8696 | (ii) for ensuring the accuracy of notes taken at a trial a | encoded | `s 482(3) rules may be made for the purpose` | 22 | - |
| s 482(3)(d)(iii) | 8697 | (iii) for keeping writings, exhibits or other things conne | encoded | `s 482(3) rules may be made for the purpose` | 22 | - |
| s 482(3)(d)(iv) | 8698 | (iv) for securing the safe custody of property during the  | encoded | `s 482(3) rules may be made for the purpose` | 22 | - |
| s 482(3)(d)(v) | 8699 | (v) for providing that the Attorney General and counsel wh | encoded | `s 482(3) rules may be made for the purpose` | 22 | - |
| s 482(4) | 8700-8701 | (4) Rules of court that are made under this section must b | fork (F8 bare-must) | `s 482(4) the rules of court have been published or otherwise made available to the public as the subsection requires` | 4 | 1 |
| s 482(5) | 8702-8703 | (5) Notwithstanding anything in this section, the Governor | encoded | `s 482(5) the Governor in Council may make the provision to secure uniformity in the rules of court in criminal matters`; `s 482(5) the uniform rules prevail and have effect as if enacted by this Act` | 4 | 1 |
| s 482.1(1) | 8704-8705 | 482.1 (1) A court referred to in subsection 482(1) or (2)  | encoded | `s 482.1(1) the court may make rules for case management` | 6 | - |
| s 482.1(1)(a) | 8706 | (a) for the determination of any matter that would assist  | encoded | `s 482.1(1) the court may make rules for case management` | 6 | - |
| s 482.1(1)(b) | 8707 | (b) permitting personnel of the court to deal with adminis | encoded | `s 482.1(1) the court may make rules for case management` | 6 | - |
| s 482.1(1)(c) | 8708 | (c) establishing case management schedules. | encoded | `s 482.1(1) the court may make rules for case management` | 6 | - |
| s 482.1(2) | 8709-8710 | (2) The parties to a case shall comply with any direction  | fork (F8 bare-must) | `s 482.1(2) the party has complied with the direction as the subsection requires`; `s 482.1(2) the party's duty to comply with the direction` | 5 + 4 traces | 1 |
| s 482.1(3) | 8711-8712 | (3) If rules are made under subsection (1), a court, justi | fork (F5 if-on-power) | `s 482.1(3) a court, justice or judge may issue a summons or warrant to compel the presence of the accused at case management proceedings`; `s 482.1(3) the permission of a court, justice or judge to issue a summons or warrant to compel the presence of the accused` | 4 + 2 traces | 1 |
| s 482.1(4) | 8713-8714 | (4) Sections 512 and 512.3 apply, with any modifications t | encoded | `s 482.1(4) the provision applies, with any modifications that the circumstances require, to the issuance of the summons or warrant` | 5 | 1 |
| s 482.1(5) | 8715-8716 | (5) Subsections 482(4) and (5) apply, with any modificatio | encoded | `s 482.1(5) the provision applies, with any modifications that the circumstances require, to the rules` | 5 | 1 |
| s 482.1(6) | 8717 | (6) [Repealed, 2019, c. 25, s. 187] | repealed or blank in this text: the text shows "(6) [Repealed, 2019, c. 25, s. 187]" | `s 482.1(6) as the text shows it` | 1 | - |

## Fork register (ccc15)

A fork is a place where the text can be read two or more ways with different outcomes.
Each entry gives the provision and function, the readings and the text that licenses each, and the reading taken.
The taken reading is the status quo for a lawyer to overrule.
Each entry's tag is the word the modules use in their `(fork: <tag>)` comments, so a grep finds the sites; `work/notes_build.py` checks that every tag below exists in the code and that the counts stated here match it.

- **F1.
  An offence that is both indictable and punishable on summary conviction (hybrid)** (tag `hybrid`; three functions: `s 468`, `s 469` court of criminal jurisdiction, `s 471`).
  The text says "any indictable offence" (s 468), "an indictable offence" (s 469) and "charged with an indictable offence" (s 471).
  The core's `Class of offence` has a third value for an offence that the section makes both.
  Reading A (taken): the text is silent on whether such an offence is "an indictable offence" before the mode of proceeding is chosen, so `NOTHING` (silent).
  Reading B: it is an indictable offence (`JUST TRUE`) because one of its limbs is.
  Another Act, not among the sources, may deal with the point; this encoding does not say what it provides.
  The seat takes the class "as you are being prosecuted now", so an accused whose prosecutor has chosen how to proceed names that way.
- **F2.
  "Listed in section 469" is a closed list** (tag `closed-list`; `s 469 the offence charged is one listed in section 469`).
  It is the seam PLAN.md section 6 gives for ss 498, 515, 522, 523 (ccc20) and ss 536, 536.1, 554 (ccc21).
  Section 469 says "other than (a) ... (e)", and ss 473(1), 478(3) and 479 refer to "an offence listed in section 469" or "mentioned in section 469", handing the question to the list.
  Reading A (taken): an offence in none of (a) to (e) is not listed (`JUST FALSE`), which is the 2026-11-05 case-by-case ruling on "listed in Schedule N".
  Reading B: the list is not closed with "only", so `NOTHING` (list not closed); then every other part's answer to "is it listed" would be `NOTHING` for nearly every offence.
- **F3.
  "Other than" and "that is not a court referred to in"** (tag `other-than`; three functions: `s 469` court of criminal jurisdiction, for a listed offence; `s 477.3(1)`, for a place that is part of another state's territorial sea; `s 482(2)`, for an appeal court that is a court of subsection (1)).
  The 2026-11-05 case-by-case ruling lists "(other than X)".
  Reading A (taken): the carve-out is the text's own no in its own words, `JUST FALSE`; the brief lists "except" among the words that give the text's no, and "other than" is read with it.
  Reading B: each is a grant limited by its own wording, and the case outside the limit is `NOTHING`.
  Also marginal reading (a).
- **F4.
  "Subject to ..."** (tag `subject-to`; three functions: `s 470`, `s 478(1)`, `s 481.2`).
  `s 470` and `s 481.2` are grants; `s 478(1)` is a prohibition.
  Another provision that limits the section is an input.
  Reading A (taken): for a grant, where the limiting provision does not say `JUST FALSE` the answer is `NOTHING` (limited by its own wording, and the limiting provision's own answer is outside this section); for a bar, the exception being met answers `JUST FALSE`.
  Reading B: all three `NOTHING`, or all three `JUST FALSE`.
- **F5.
  An "if" on a power (the brief's ruling of 2026-11-12, limit (1))** (tag `if-on-power`; eight functions).
  Each is named for a power or a grant and answers `NOTHING` where an "if" gate fails:
  `s 470 the court is competent to try the accused ...` (the "if" limbs (a) and (b));
  `s 474(1) the clerk of the court may adjourn ...` ("if a judge is not present");
  `s 475(1)(b)(i) the court may impose a sentence ...` ("if it finds the accused guilty");
  `s 475(1)(b)(ii) the court may adjourn the trial ...` ("if a warrant in Form 7 is issued");
  `s 475(1) the court may, at any time, continue a trial adjourned ...` ("if it is satisfied");
  `s 478(3) the accused may appear ...` and `s 479 the accused may appear ...` ("if the offence is not an offence mentioned in section 469" and the consent of the Attorney General);
  `s 482.1(3) a court, justice or judge may issue ...` ("If rules are made under subsection (1)").
  The other reading is `JUST FALSE` (the brief's rule: a condition the text introduces with "if" is the text's no); under it each of these eight reads as "may not".
- **F6.
  A "where", "when" or "upon" on a power: group (3) of the brief's ruling, NOT decided here** (tag `where-on-power`; twelve functions).
  Each is named for a power ("may") and answers `JUST FALSE` where its "where" gate fails, which is rule (b) of the 2026-11-05 ruling on periods, "where" and scope limits as the guide gives it (and, for "on the day of the opening", rule (a)).
  The line on grants in the 2026-11-12 ruling points the other way (`NOTHING`), so this is a question for a lawyer.
  The twelve are `s 473(1.1)`, `s 474(1)` (the lead-in "Where the competent authority has determined" and "on the day of the opening"), `s 475(1)(b)(i)` (two functions: continue the trial; impose a sentence), `s 475(1)(b)(ii)`, `s 475(1)` proviso, `s 475(2)`, `s 479`, `s 480(1)`, `s 481`, `s 481.1` and `s 481.2`.
  Left as the guide's rulings give it, `JUST FALSE`.
  `s 478(3)`'s first branch answers `NOTHING` because its words are a relative clause ("An accused who is charged with an offence that is alleged ...") that defines whom the subsection is about, a scope limit (rule (c)).
- **F7.
  "Entitled"-named functions: group (3), NOT decided here** (tag `entitled`; one function: `s 475(3) the accused is not entitled to have any part of the proceedings conducted in the accused's absence re-opened`).
  An entitlement is a claim, not a power.
  The text's own words are a flat negative ("is not entitled"), and ruling N2 (option A) counts a flat negative as the text's no, so the function is the bar and answers `JUST TRUE` (not entitled) or `JUST FALSE`.
  The other reading would answer `NOTHING` where its "where" is unmet.
- **F8.
  A "must", "shall" or "cannot" with no named actor, or with a "where" or "if" unmet** (tag `bare-must`; eleven functions).
  (i) No actor named, so no actor is invented and there is no regulative rule: `s 473(2)` (shall not be withdrawn), `s 477.2(4)` (must be filed), `s 482(4)` (must be published) and `s 478(2)` (shall be dealt with in the province).
  They are decision functions; a duty not done is `JUST FALSE`, a duty outside its scope `NOTHING`.
  (ii) A named actor with a duty whose "where" or "if" is unmet: `s 478(3)` (three functions: determine guilty; returned to custody; dealt with according to law) and `s 479` (the same three) answer `JUST FALSE` ("the duty does not arise").
  (iii) `s 482.1(2)` (the parties shall comply) answers `NOTHING` when the direction was not made under a rule, and `JUST FALSE` when it was and was not complied with.
  The other reading is `NOTHING` for the unmet "where" or "if" of a duty in (ii).
  The 2026-11-05 case-by-case ruling covers "a bare must not done" and "a duty whose if or where is unmet".
- **F9.
  An "unless" once it is met** (tag `unless-met`, on `s 475(3)`; the same reading is taken at the "unless" of `s 473(2)` and of `s 477.2(1)` to `(3)`, whose comments quote it).
  "Shall not be withdrawn unless both agree", "not entitled ... unless the court is satisfied", "shall not be continued unless the consent ... is obtained not later than eight days after": when the "unless" is met the bar does not apply, so the bar's function answers `JUST FALSE` (the text's no to the bar).
  That does not say the accused is entitled or free.
  Reading B: `NOTHING`.
  The 2026-11-05 case-by-case ruling covers "an unless or except once it is met".
- **F10.
  As at what date is "the consent not obtained within eight days" asked** (tag `as-at-date`, on the helper `s 477.2 the consent was not obtained not later than eight days after the proceedings were commenced`, used by `s 477.2(1)` to `(3)`).
  With no consent yet, the question needs a date: the bar has bitten only once the as-at date is more than eight days after the day the proceedings were commenced.
  The helper answers `FALSE` inside the eight days, and `s 477.2(1)`, `(2)` and `(3)` then answer `JUST FALSE` ("not yet barred"; the date to watch is `s 477.2 the last day ...`).
  Reading B: `NOTHING` inside the period (the text says what is barred only once the period has run).
  Taken: A, because "not later than eight days after" fixes the period in its own words (rule (a) of the periods ruling).
- **F11.
  "Not later than eight days after the proceedings are commenced" is inclusive** (tag `eight-days-inclusive`, same helper).
  With proceedings commenced on 1 January 2026, a consent obtained on 9 January (1 January plus eight days) is in time, and a consent obtained on 10 January is late.
  Reading B (exclusive of the eighth day) is not taken: "not later than" includes the day named.
  Tested at 9 and 10 January 2026 (seat cases), across a month end and a leap day (25 and 28 February 2024) and across a year end (28 December 2025).
- **F12.
  "Within five hundred metres"** (tag `metres`; `s 476(b)`).
  Exactly 500 metres is within (at most 500); 501 is not.
  Reading B (fewer than 500) is not taken.
  Tested at 0, 500 and 501.
- **F13.
  The second limb of paragraph (c) of section 476** (tag `road-boundary`): "and where the center or other part of the road, or navigable river, canal or inland water on which the vehicle or vessel passed in the course of the journey or voyage is the boundary of two or more territorial divisions, the offence shall be deemed to have been committed in any of the territorial divisions".
  Reading A (taken): it continues the sentence about an offence "in or on a vehicle employed in a journey, or on board a vessel", so it needs that circumstance.
  Reading B: it is independent.
  They differ only for an offence not in or on a vehicle or vessel, on a road that is a boundary.
- **F14.
  The last words of section 477.4(3)(b)** (tag `certificate-statement`): "in an area of a fishing zone of Canada that is not within the internal waters of Canada or the territorial sea of Canada or outside the territory of any state".
  Reading A (taken): the statement is either that the location was in an area of a fishing zone of Canada that is not within the internal waters or the territorial sea, or that it was outside the territory of any state.
  Reading B: "not within" governs all three places, which reads oddly.
  The two statements are two inputs of the certificate record; either suffices.
- **F15.
  "Is deemed ... if it is an act or omission (a) ... (e)"** (tag `if-on-deeming`; `s 477.1`).
  Where none of (a) to (e) holds the function answers `JUST FALSE` (a failed "if" on a deeming, which is not a grant or a power).
  Where the lead-in ("Every person who commits an act or omission that, if it occurred in Canada, would be an offence under a federal law") is not met it answers `NOTHING`, a scope limit with no "only" (rule (c)).
  Reading B: `NOTHING` for both.
  The lead-in could equally be read as a condition (`JUST FALSE`).
- **F16.
  "Continues until appropriate provision is made by law"** (tag `until`; `s 480(2)`).
  Before the provision the jurisdiction continues (`JUST TRUE`); after it, `JUST FALSE` (the text's "until").
  A new district not constituted answers `JUST FALSE` ("Where" unmet; F6 applies by analogy, though the function is named for what the subsection does and not "may").
- **F17.
  "Without the consent" against "unless the consent is obtained"** (tag `without-consent`; `s 477.3(3)` against `s 477.2`).
  The brief's list of limits that give `NOTHING` includes "without"; its list of words that give the text's no includes "unless".
  Section 477.3(3) says the powers "shall not be exercised outside Canada ... without the consent of the Attorney General of Canada", so with the consent the function answers `NOTHING`.
  Section 477.2 says proceedings "shall be continued unless the consent ... is obtained", so with the consent in time it answers `JUST FALSE`.
  Two different answers for two different words, and a reviewer may well find them the same thing.
  Reading B: both `JUST FALSE`, or both `NOTHING`.
- **F18.
  Another provision's answer taken as a plain fact in the seat** (tag `plain-fact-seams`, in the seat header; the list is in "Seat").
  The seat takes "does section 477.1 apply", "I have appeared as the subsection allows", "a provision of the Code expressly provides that I am to be tried without a jury", "another provision takes the competence away", "another provision displaces the bar" and "another provision limits the section" as plain yes-or-no facts, because asking them from their own facts again would ask the accused many facts twice.
  The question for each of the first two is also asked in the seat.
  Reading B: build each from its own facts in every question.
- **F19.
  Which provisions have a regulative form** (tag `regulative-form`, in the header of `ccc15-duties.l4`).
  The criterion, the same for every provision of the range: the text names both the party and the act.
  Written in regulative form: `s 473(1.1)` (a judge may order), `s 474(1)` and `(2)` (the clerk may adjourn), `s 475(1)(b)(i)`, `(ii)`, the proviso and `s 475(2)` (the court may), `s 478(1)` (the court shall not try, derived from the decision function's answer, ruling N2), `s 478(3)` and `s 479` (the court shall determine), `s 482.1(2)` (the parties shall comply) and `s 482.1(3)` (a court, justice or judge may issue).
  Not regulative: provisions that name no party ("must be filed", "must be published", "shall not be withdrawn", "proceedings may be commenced"), deemings, definitions, statements of jurisdiction and bars on proceedings.
  The other reading: write more or fewer.
- **F20.
  "A court in a province" and "another province" exclude the territories** (tag `territories`; `s 478(1)`).
  Yukon, the Northwest Territories and Nunavut are in the core's `Province or territory` and are not provinces: a court in a territory answers `NOTHING` (a scope limit).
  An offence committed entirely in a territory also answers `NOTHING`.
  Reading B: the section is read as covering territories.
- **F21.
  Section 469(b) names "high treason or treason or murder", not section numbers** (tag `names-not-numbers`; `s 469 facts of the charge`).
  Reading A (taken): a plain fact (`the offence of which the accused is alleged to be an accessory after the fact is high treason, treason or murder`), asked as the accused can state it.
  Reading B: map the three names to section numbers; not done, because of finding 2 (the numbers and the parenthesised words disagree across ss 46, 47, 183 and 469).

### Name-test sweep of 2026-11-12

The sweep applies the brief's three limits to every layer-1 function whose name contains "may", "permitted", "power", "entitled" or "authorise"/"authorize".
`work/notes_build.py` selects the set by that test, classifies each function by its `JUST FALSE` branches, and stops if a function is missing from, or twice in, the lists below.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 0 | 4 | 12 | 1 |

25 layer-1 functions have "may", "power", "entitled" or "authorize" in their name: 0 + 4 + 12 + 1 in the table, and 8 that have no `JUST FALSE` branch at all.
The sweep flips none: no function named for a grant or a power answers `JUST FALSE` at an "if" gate.
Seven of the 25 answer `NOTHING` where an "if" gate fails (F5), which is what the ruling asks for: `s 474(1) the clerk of the court may ...`, `s 475(1)(b)(i) the court may impose a sentence ...`, `s 475(1)(b)(ii) the court may adjourn the trial ...`, `s 475(1) the court may, at any time, ...`, `s 478(3) the accused may appear before a ...`, `s 479 the accused may appear before a ...`, `s 482.1(3) a court, justice or judge may ...`.
(`s 470`, named "is competent to try", is the eighth of F5 and lies outside the keyword test.)

Flipped to `NOTHING` by this sweep: none.

Kept `JUST FALSE`, the gate closed by the text (an exclusion or an exception in its own words, or a bar):
  - `s 477.3(1) the power may be exercised at the place` (JUST FALSE at: "other than a place that is part of the territorial sea of any other st")
  - `s 477.3(3) the powers are barred from being exercised outside Canada ...` (JUST FALSE at: "Where an act or omission that is an offence by virtue only of section ")
  - `s 482(2) the court may make rules of court not inconsistent ...` (JUST FALSE at: "that is not a court referred to in subsection (1)")
  - `s 482(3) rules may be made for the purpose` (JUST FALSE at: "except in so far as they are regulated by law")

One of the four is a bar (`s 477.3(3)`, titled "barred").
The other three answer `JUST FALSE` at an exclusion that the text states in its own words ("other than", "that is not a court referred to in", "except in so far as"), none of which is an "if" gate.
This encoding reads each of them as the text closing the gate itself (assumed, not ruled); the other reading is `NOTHING`, and F3 names it for the first two.

Listed, "may" with a where/when/upon-kind gate (F6; assumed, not ruled, that "on the day of the opening" goes with this group):
  - `s 473(1.1) the judge of the superior court of criminal jurisdiction ...` (JUST FALSE at: "Where the consent of the accused and the Attorney General is given in ")
  - `s 474(1) the clerk of the court may adjourn the court ...` (JUST FALSE at: "Where the competent authority has determined that a panel of jurors is")
  - `s 475(1)(b)(i) the court may continue the trial and proceed to ...` (JUST FALSE at: "where an accused, whether or not he is charged jointly with another, a")
  - `s 475(1)(b)(i) the court may impose a sentence on the accused ...` (JUST FALSE at: "where an accused, whether or not he is charged jointly with another, a")
  - `s 475(1)(b)(ii) the court may adjourn the trial to await the ...` (JUST FALSE at: "where an accused, whether or not he is charged jointly with another, a")
  - `s 475(1) the court may, at any time, continue a trial ...` (JUST FALSE at: "but where the trial is adjourned pursuant to subparagraph (b)(ii)")
  - `s 475(2) the court may draw an inference adverse to the ...` (JUST FALSE at: "Where a court continues a trial pursuant to subsection (1)")
  - `s 479 the accused may appear before a court or judge ...` (JUST FALSE at: "Where an accused is charged with an offence that is alleged to have be")
  - `s 480(1) proceedings may be commenced and the accused may be ...` (JUST FALSE at: "Where an offence is committed in an unorganized tract of country in an")
  - `s 481 proceedings may be commenced and the accused may be ...` (JUST FALSE at: "Where an offence is committed in a part of Canada not in a province")
  - `s 481.1 proceedings may be commenced and the accused may be ...` (JUST FALSE at: "Where an offence is committed in or on the territorial sea of Canada o")
  - `s 481.2 proceedings may be commenced and the accused may be ...` (JUST FALSE at: "where an act or omission is committed outside Canada and the act or om")

Listed, "entitled" (F7):
  - `s 475(3) the accused is not entitled to have any part ...` (JUST FALSE at: "Where an accused reappears at his trial that is continuing pursuant to")

No `JUST FALSE` branch at all, so nothing to decide (8):
  - `s 473(1) the accused may be tried without a jury by ...`
  - `s 474(2) the clerk of the court may adjourn the court ...`
  - `s 477.3(2) a justice or judge in any territorial division in ...`
  - `s 478(3) the accused may appear before a court or judge ...`
  - `s 482(1) the court may make rules of court not inconsistent ...`
  - `s 482(5) the Governor in Council may make the provision to ...`
  - `s 482.1(1) the court may make rules for case management`
  - `s 482.1(3) a court, justice or judge may issue a summons ...`

Outside the sweep although "may" is in the name (2):
  - `s 477(2) the section limits the operation of any other Act ...`: its "may" is in "the jurisdiction that a court may exercise"
  - `s 477.2 the last day on which the consent of the ...`: it answers a DATE

Functions named "it is lawful ...": none in this part.
- it is lawful, scoped: 0.
- it is lawful, unscoped and retitled: 0.

Outside the keyword test but the same class, and left as they are:
- `s 468` and `s 469` (named "has jurisdiction to try"): `s 469` answers `JUST FALSE` for the "other than" carve-out (F3, kept); neither has a `JUST FALSE` from an "if" gate.
- `s 470` (named "is competent to try"): answers `NOTHING` where its "if" limbs fail (F5).
- the eight regulative rules in `ccc15-duties.l4` whose names contain "permission" answer `FULFILLED` where their gate is unmet; they are not `MAYBE BOOLEAN` functions.
- `s 477(2)` (its name contains "may" only in "the jurisdiction that a court may exercise") and `s 477.2 the last day ...` (answers a `DATE`) are not named for a grant.

The sweep flips no function, so it changes no assertion and no assertion carries a `RECONCILED` line for it.

## Jural relations (ccc15)

One row per provision (or group of paragraphs) that creates a relation.
Hohfeld's correlatives: right and duty; privilege and no-right; power and liability (being subject to the power, not an obligation); immunity and disability.
A provision that creates none (a definition, a counting rule, a rule of application) is listed once as `none`.
Ruling N2: where the text names the bearer of a flat prohibition, the prohibition (`SHANT`) is derived from the decision function's answer; the kinds stay in this table.

| provision | holder (right, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | section | L4 rule |
| --- | --- | --- | --- | --- |
| the headings of Part XIV and its divisions | none | none | -- | -- |
| jurisdiction of a superior court | power: a superior court of criminal jurisdiction, to try any indictable offence | liability: the accused, to be tried there | s 468 | `s 468 ...` |
| jurisdiction of a court of criminal jurisdiction | power: a court of criminal jurisdiction, to try an indictable offence other than those listed | disability: that court, as to the listed offences; liability: the accused; immunity: the accused charged with a listed offence, from trial by that court | s 469 | `s 469 the court of criminal jurisdiction has jurisdiction ...` |
| the list of offences | none (a list the other sections refer to) | none | s 469(a) to (e) | `s 469 the offence charged is one listed in section 469` |
| jurisdiction over the person | power: a court with power to try the offence, to try an accused who is found, arrested or in custody in its territory, or ordered to be tried by it | liability: the accused | s 470 | `s 470 ...` |
| trial by judge and jury | right (a claim): the accused charged with an indictable offence, to be tried by a court composed of a judge and jury | duty: the court (no named bearer; "shall be tried") | s 471 | `s 471 ...` |
| trial without a jury | power (jointly): the accused and the Attorney General, to have the accused tried without a jury by a judge of a superior court | liability: the judge and the court | s 473(1) | `s 473(1) ...` |
| joinder of other offences | power: the judge of the superior court, to order any offence tried in conjunction | liability: the accused | s 473(1.1) | `s 473(1.1) ...`; regulative: `s 473(1.1) the judge's permission ...` |
| consent not to be withdrawn | immunity: each of the accused and the Attorney General, against the other's unilateral withdrawal | disability: each of them, to withdraw alone (no bearer is named for a duty, so none is invented) | s 473(2) | `s 473(2) the withdrawal of the consent is barred` |
| the clerk's adjournment | power: the clerk of the court, to adjourn the court and its business | liability: the accused whose trial is put off | s 474(1), (2) | `s 474(1) ...`, `s 474(2) ...`; regulative: `s 474(1) the clerk ...`, `s 474(2) the clerk ...` |
| the accused who absconds: waiver | privilege: the court, to proceed with the trial in the accused's absence, the accused being deemed to have waived the right to be present | no-right: the accused, who loses the right to be present | s 475(1)(a) | `s 475(1)(a) ...` |
| the accused who absconds: the court's powers | power: the court, to continue the trial to judgment or verdict, to sentence in absence if it finds the accused guilty, to adjourn to await appearance if a warrant in Form 7 is issued, and to continue after adjourning | liability: the accused | s 475(1)(b), the proviso | `s 475(1)(b)(i) ...` (two), `s 475(1)(b)(ii) ...`, `s 475(1) the court may, at any time, ...`; regulative: `s 475(1)(b)(i) the court's permission ...`, `(ii)`, the proviso |
| adverse inference | power: the court, to draw an inference adverse to the accused | liability: the accused | s 475(2) | `s 475(2) ...`; regulative |
| no re-opening | immunity: the court, against a claim by the accused who reappears to have the proceedings conducted in absence re-opened | disability: the accused, to have them re-opened (no claim) unless the court is satisfied that, because of exceptional circumstances, it is in the interests of justice to re-open | s 475(3) | `s 475(3) the accused is not entitled ...` |
| counsel's authority | immunity: counsel for the accused, against loss of any authority to act for the accused because the court continued the trial | disability: the court, to deprive counsel of that authority by continuing the trial | s 475(4) | `s 475(4) ...` |
| where an offence is deemed committed | power: the court and the prosecutor of any named territorial division, to proceed in it | liability: the accused, to be tried in any of those divisions | s 476(a) to (e) | `s 476 ...` and the paragraph functions |
| definition of ship; saving | none; (2): immunity: another Act and a court's other jurisdiction, from being limited by ss 477.1 to 477.4 | disability: ss 477.1 to 477.4, to limit them | s 477(1), (2) | `s 477(1) ship`, `s 477(2) ...` |
| offences outside Canada deemed committed in Canada | power: Canadian courts, to try the act or omission as if committed in Canada | liability: the person who commits it | s 477.1 | `s 477.1 ...` |
| the consent of the Attorney General of Canada | immunity: the accused who is not a Canadian citizen (on a foreign-registered ship), or any accused where jurisdiction is only by virtue of 477.1(d) or (e), against proceedings continuing without the consent in time | disability: the prosecutor and the court, to continue the proceedings without it | s 477.2(1), (2), (3) | `s 477.2(1) ...`, `(2)`, `(3)`, `s 477.2 the consent was not obtained ...` |
| summary conviction exception | none (it limits subsection (1)) | none | s 477.2(1.1) | `s 477.2(1.1) ...` |
| filing of the consent | claim: the clerk of the court in which the proceedings were instituted, to receive the consent (the text names the clerk, not a claim) | duty: whoever files the consent (no bearer is named) | s 477.2(4) | `s 477.2(4) ...` |
| powers of arrest, entry, search or seizure | power: the person who exercises the power (no bearer named), at the places listed | liability: the accused and other persons | s 477.3(1) | `s 477.3(1) ...` |
| jurisdiction to authorize | power: a justice or judge in any territorial division | liability: the accused | s 477.3(2) | `s 477.3(2) ...` |
| limitation on the powers | immunity: the person alleged to have committed the act on a foreign-registered ship, against powers exercised outside Canada without the consent of the Attorney General of Canada | disability: the person who would exercise the powers | s 477.3(3) | `s 477.3(3) ...` |
| certificates | privilege: the party that tenders the certificate (no party is named), to prove the statement by the certificate alone, without proof of the signature or official character; immunity: the certificate, against compulsion to produce it (the holder is not named) | no-right: any other party, to contest the statement by requiring proof of signature; disability: the accused and the court, to compel production | s 477.4(3), (4) | `s 477.4(3) ...`, `s 477.4(4) ...` |
| the venue rule | immunity: the accused, from trial in a province other than where the offence was entirely committed | disability: a court in a province (derived prohibition, ruling N2) | s 478(1) | `s 478(1) ...`; regulative: `s 478(1) the prohibition ...` |
| newspaper libel | claim: every proprietor, publisher, editor or other person charged with a defamatory libel in a newspaper (or a conspiracy to publish one), to be dealt with, indicted, tried and punished in the province where they reside or in which the newspaper is printed | duty: whoever deals with, indicts, tries or punishes them (no bearer is named) | s 478(2) | `s 478(2) ...` |
| appearing before a court that would have had jurisdiction, and the plea | privilege: the accused, to appear before that court or judge on the conditions the text sets (the offence is not one mentioned in section 469, and the Attorney General of Canada or of the province consents); power: that Attorney General, to give the consent | no-right: no bearer is named for the privilege; duty: the court or judge, to determine the accused guilty and impose the punishment warranted by law where the accused consents to plead guilty and pleads guilty; duty (no bearer named): to return the accused to custody and deal with them according to law where the accused does not consent and does not plead guilty and was in custody before appearing | s 478(3), 479 | `s 478(3) ...` (four), `s 479 ...` (four); regulative: `s 478(3) the court's duty ...`, `s 479 ...` |
| the accused deemed simply to stand charged | none (a deeming: the accused who is ordered to stand trial or against whom an indictment is preferred is treated as simply charged, without a preliminary inquiry or an indictment) | none | s 478(4) | `s 478(4) ...` |
| definition of newspaper | none | none | s 478(5) | `s 478(5) newspaper` |
| unorganized territory, not in a province, Canadian waters, outside Canada | power: the Crown and the court, to commence and conduct proceedings in any territorial division | liability: the accused | ss 480, 481, 481.1, 481.2 | `s 480(1) ...`, `s 480(2) ...`, `s 481 ...`, `s 481.1 ...`, `s 481.2 ...` |
| appearance of the accused | none (a rule of application, "for greater certainty": the provisions on the requirement of appearance and its exceptions apply to proceedings commenced under ss 481 to 481.2) | none | s 481.3 | `s 481.3 ...` |
| the courts' power to make rules; their purposes | power: the courts named, to make rules of court | liability: the persons whose proceedings the rules apply to (the accused) | s 482(1), (2), (3) | `s 482(1) the court may ...`, `s 482(2) the court may ...`, `s 482(3) rules may be made ...`, `s 482(1) the rules so made apply ...`, `s 482(2) the rules so made are applicable ...` |
| publication of the rules | claim: the public (the text names no holder; the accused is one of the public) | duty: whoever makes the rules (no bearer is named) | s 482(4) | `s 482(4) ...` |
| uniform rules | power: the Governor in Council, to make such provision as he considers proper to secure uniformity in the rules of court in criminal matters | liability: the courts, whose rules yield (the uniform rules "prevail and have effect as if enacted by this Act") | s 482(5) | `s 482(5) ...` (two) |
| case management: rules and matters | power: the courts of s 482(1) and (2), to make rules for case management | liability: the parties | s 482.1(1) | `s 482.1(1) ...` |
| case management: compliance | claim: no holder is named (the court that gave the direction is the natural holder, assumed) | duty: the parties to a case (the accused and the prosecutor) | s 482.1(2) | `s 482.1(2) ...`; regulative: `s 482.1(2) the party's duty ...` |
| summons or warrant | power: a court, justice or judge | liability: the accused | s 482.1(3) | `s 482.1(3) ...`; regulative |
| the provisions that apply | none (rules of application: ss 512, 512.3; 482(4), (5)) | none | s 482.1(4), (5) | `s 482.1(4) ...`, `s 482.1(5) ...` |
| the repealed rows | none | none | s 469(a)(ii), 472, 477.4(1) and (2), 482.1(6) | the four "as the text shows it" constants |

## Marginal readings for a lawyer (ccc15)

The brief takes two readings as the status quo and leaves them for a lawyer.
(a) A failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no.
(b) A prohibition or grant limited by its own wording does not: the case outside the limit is `NOTHING`.
The lists below are generated from the code by `work/notes_build.py`, so they cover every branch that carries a `FALSE-kind` or a `NOTHING-kind` comment.
The fork register (F1 to F21) says, for the sites that are forks, what the other reading is.

### Reading (a): branches that answer `JUST FALSE` as the text's own no

The other reading answers `NOTHING` for each of them.
The first class, the exclusions ("other than", "except", "that is not"), is put here because the brief's list of the text's own words for a no includes "except"; whether an exclusion belongs with reading (a) or with reading (b) is itself for a lawyer (F3).

59 branches in 48 functions, by the kind of gate the text uses:
- an exclusion in the text ("other than", "except", "that is not"): 6 branches in 6 functions
  - `s 469 the offence charged is one listed in section ...`
  - `s 469 the court of criminal jurisdiction has jurisdiction to ...`
  - `s 471 the accused shall be tried by a court ...`
  - `s 477.3(1) the power may be exercised at the place`
  - `s 482(2) the court may make rules of court not ...`
  - `s 482(3) rules may be made for the purpose`
- a failed "where": 32 branches in 31 functions
  - `s 473(1.1) the judge of the superior court of criminal ...`
  - `s 473(2) the withdrawal of the consent is barred`
  - `s 474(1) the clerk of the court may adjourn the ...`
  - `s 475(1)(a) the accused is deemed to have waived the ...`
  - `s 475(1)(b)(i) the court may continue the trial and proceed ...`
  - `s 475(1)(b)(i) the court may impose a sentence on the ...`
  - `s 475(1)(b)(ii) the court may adjourn the trial to await ...`
  - `s 475(1) the court may, at any time, continue a ...`
  - `s 475(2) the court may draw an inference adverse to ...`
  - `s 475(3) the accused is not entitled to have any ...`
  - `s 475(4) the subsection preserves any authority counsel for the ...`
  - `s 476(a) the offence is deemed to have been committed ...`
  - `s 476(b) the offence is deemed to have been committed ...`
  - `s 476(c) the offence is deemed to have been committed ...`
  - `s 476(c) the offence is deemed to have been committed ...`
  - `s 476(d) the offence is deemed to have been committed ...`
  - `s 476(e) the offence is deemed to have been committed ...`
  - `s 476 the offence is deemed to have been committed ...`
  - `s 477.3(3) the powers are barred from being exercised outside ...`
  - `s 478(3) the court or judge shall determine the accused ...`
  - `s 478(3) the accused shall be returned to custody`
  - `s 478(3) the accused shall be dealt with according to ...`
  - `s 479 the accused may appear before a court or ...`
  - `s 479 the court or judge shall determine the accused ...`
  - `s 479 the accused shall be returned to custody`
  - `s 479 the accused shall be dealt with according to ...`
  - `s 480(1) proceedings may be commenced and the accused may ...`
  - `s 480(2) subsection (2) continues the jurisdiction conferred by subsection ...`
  - `s 481 proceedings may be commenced and the accused may ...`
  - `s 481.1 proceedings may be commenced and the accused may ...`
  - `s 481.2 proceedings may be commenced and the accused may ...`
- an "unless" that is met: 5 branches in 5 functions
  - `s 473(2) the withdrawal of the consent is barred`
  - `s 475(3) the accused is not entitled to have any ...`
  - `s 477.2(1) the proceedings are barred from being continued for ...`
  - `s 477.2(2) the proceedings are barred from being continued for ...`
  - `s 477.2(3) the proceedings are barred from being continued for ...`
- a period, distance or event the text fixes in its own words: 3 branches in 3 functions
  - `s 474(1) the clerk of the court may adjourn the ...`
  - `s 476(b) the offence is deemed to have been committed ...`
  - `s 476(b) the offence is deemed to have been committed ...`
- a flat negative ("does not apply", "is not entitled", "Nothing in"): 2 branches in 2 functions
  - `s 477(2) the section limits the operation of any other ...`
  - `s 477.2(1) the proceedings are barred from being continued for ...`
- a failed "if" on a deeming (F15): 1 branch in 1 function
  - `s 477.1 the person is deemed to have committed the ...`
- a failed "if": 4 branches in 4 functions
  - `s 477.2(1) the proceedings are barred from being continued for ...`
  - `s 477.2(2) the proceedings are barred from being continued for ...`
  - `s 478(3) the accused shall be returned to custody`
  - `s 479 the accused shall be returned to custody`
- a duty not done: 4 branches in 4 functions
  - `s 477.2(4) the consent has been filed as the subsection ...`
  - `s 478(2) the person is dealt with, indicted, tried and ...`
  - `s 482(4) the rules of court have been published or ...`
  - `s 482.1(2) the party has complied with the direction as ...`
- "Subject to" with the exception met: 1 branch in 1 function
  - `s 478(1) a court in a province is barred from ...`
- an "until" that has passed: 1 branch in 1 function
  - `s 480(2) subsection (2) continues the jurisdiction conferred by subsection ...`

### Reading (b): branches that answer `NOTHING` because a grant or prohibition is limited by its own wording

The other reading answers `JUST FALSE` for each of them.

99 branches in 63 functions:
- `s 468 the superior court of criminal jurisdiction has jurisdiction ...` (2)
- `s 469 the court of criminal jurisdiction has jurisdiction to ...` (2)
- `s 470 the court is competent to try the accused ...` (2)
- `s 471 the accused shall be tried by a court ...` (1)
- `s 473(1) the accused may be tried without a jury ...` (4)
- `s 474(1) the clerk of the court may adjourn the ...` (2)
- `s 474(2) the clerk of the court may adjourn the ...` (2)
- `s 475(1)(b)(i) the court may impose a sentence on the ...` (1)
- `s 475(1)(b)(ii) the court may adjourn the trial to await ...` (1)
- `s 475(1) the court may, at any time, continue a ...` (1)
- `s 476(a) the offence is deemed to have been committed ...` (1)
- `s 476(b) the offence is deemed to have been committed ...` (1)
- `s 476(b) the offence is deemed to have been committed ...` (1)
- `s 476(c) the offence is deemed to have been committed ...` (1)
- `s 476(c) the offence is deemed to have been committed ...` (1)
- `s 476(d) the offence is deemed to have been committed ...` (1)
- `s 476(e) the offence is deemed to have been committed ...` (1)
- `s 476 the offence is deemed to have been committed ...` (1)
- `s 477(1) ship` (1)
- `s 477(2) the section limits the operation of any other ...` (2)
- `s 477.1 the person is deemed to have committed the ...` (1)
- `s 477.2(1) the proceedings are barred from being continued for ...` (1)
- `s 477.2(1.1) subsection (1) does not apply to the proceedings` (1)
- `s 477.2(2) the proceedings are barred from being continued for ...` (1)
- `s 477.2(3) the proceedings are barred from being continued for ...` (1)
- `s 477.2(4) the consent has been filed as the subsection ...` (1)
- `s 477.3(1) the power may be exercised at the place` (4)
- `s 477.3(2) a justice or judge in any territorial division ...` (2)
- `s 477.3(3) the powers are barred from being exercised outside ...` (2)
- `s 477.4(3) the certificate is one referred to in subsection ...` (1)
- `s 477.4(3) the certificate is conclusive proof of the truth ...` (2)
- `s 477.4(4) the certificate is admissible in evidence in the ...` (2)
- `s 477.4(4) the production of the certificate cannot be compelled` (1)
- `s 478(1) a court in a province is barred from ...` (3)
- `s 478(2) the person is dealt with, indicted, tried and ...` (2)
- `s 478(3) the accused may appear before a court or ...` (4)
- `s 478(3) the court or judge shall determine the accused ...` (1)
- `s 478(3) the accused shall be returned to custody` (1)
- `s 478(3) the accused shall be dealt with according to ...` (1)
- `s 478(4) the accused is deemed simply to stand charged ...` (2)
- `s 478(5) newspaper` (1)
- `s 479 the accused may appear before a court or ...` (3)
- `s 479 the court or judge shall determine the accused ...` (1)
- `s 479 the accused shall be returned to custody` (1)
- `s 479 the accused shall be dealt with according to ...` (1)
- `s 480(1) proceedings may be commenced and the accused may ...` (1)
- `s 481 proceedings may be commenced and the accused may ...` (1)
- `s 481.1 proceedings may be commenced and the accused may ...` (1)
- `s 481.2 proceedings may be commenced and the accused may ...` (2)
- `s 481.3 the provisions of this Act relating to the ...` (1)
- `s 482(1) the court may make rules of court not ...` (2)
- `s 482(1) the rules so made apply to the prosecution, ...` (3)
- `s 482(2) the court may make rules of court not ...` (3)
- `s 482(2) the rules so made are applicable to the ...` (3)
- `s 482(3) rules may be made for the purpose` (1)
- `s 482(4) the rules of court have been published or ...` (1)
- `s 482(5) the Governor in Council may make the provision ...` (1)
- `s 482(5) the uniform rules prevail and have effect as ...` (1)
- `s 482.1(1) the court may make rules for case management` (1)
- `s 482.1(2) the party has complied with the direction as ...` (1)
- `s 482.1(3) a court, justice or judge may issue a ...` (2)
- `s 482.1(4) the provision applies, with any modifications that the ...` (2)
- `s 482.1(5) the provision applies, with any modifications that the ...` (2)

### The other kinds of `NOTHING`

The remaining 39 `NOTHING` branches carry the other reasons, which are not marginal readings: includes 2, list not closed 4, points outside the text 28, silent 5.

## Seams (ccc15)

Each answer taken from another part or from section 2 is an input named as PLAN.md section 3 (rule R4) and section 4 name it.
First, the ones PLAN.md section 6 lists for this part, and then the ones it lacks.

Taken as inputs (this part asks):
- [T] `s 297 the publication is a newspaper` (`MAYBE BOOLEAN`), for `s 478(5)`, which `s 478(2)` calls through `s 478(5) newspaper`.
  PLAN.md lists it.
  Section 297 itself defines newspaper for "sections 303, 304 and 308" (line 5913), not for section 478: the borrowed meaning is a definition scoped to other sections (finding 6).
- Every cross-part input of the layer-1 modules, generated from the code, with the functions that take it (ten names; a name is shared by the functions that ask the same thing):
  - `s 2 superior court of criminal jurisdiction: the court is a superior court of criminal jurisdiction` (2 functions: s 468, s 482(1))
  - `s 2 court of criminal jurisdiction: the court is a court of criminal jurisdiction` (1 function: s 469)
  - `s 2 superior court of criminal jurisdiction: the trial is by a judge of a superior court of criminal jurisdiction` (1 function: s 473(1))
  - `s 2 clerk of the court: the person is the clerk of the court` (1 function: s 474(1))
  - `s 2 clerk of the court: the person is a clerk of the court for the trial of criminal cases in the territorial division` (1 function: s 474(2))
  - `s 2 justice: the person is a justice or judge` (1 function: s 477.3(2))
  - `s 297 the publication is a newspaper` (1 function: s 478(5))
  - `s 2 court of appeal: the court is a court of appeal` (1 function: s 482(1))
  - `s 2 court of criminal jurisdiction: the court is a court of criminal jurisdiction for a province` (1 function: s 482(2))
  - `s 812 the court is an appeal court within the meaning of section 812` (1 function: s 482(2))
  PLAN.md's row for this part lists five section 2 terms met in the range: `territorial division`, `Attorney General`, `court of criminal jurisdiction`, `superior court of criminal jurisdiction` and `clerk of the court`.
  Three of those are taken as inputs here.
  `territorial division` and `Attorney General` are not: no rule of this part turns on their section 2 definitions, so the rules ask plain facts ("the territorial division is in Canada", "the Attorney General of Canada consents"), and the part does not ask who the Attorney General is.
  `justice` and `court of appeal` are met in the range and are not on PLAN.md's list.

Seams the plan lacks:
- `s 812 the court is an appeal court within the meaning of section 812` (`MAYBE BOOLEAN`), for `s 482(2)(b)`; PLAN.md section 5 names section 812 as the definition of appeal court (line 17120, ccc29) and does not list it for this part.
- Inputs for provisions elsewhere that limit or displace a section of this part, each `MAYBE BOOLEAN` with `NOTHING` carried through: the provisions that limit s 470 ("Subject to this Act"), the provisions that expressly provide a trial without a jury (for `s 471`; `s 473` here and others elsewhere), the provisions that give the exceptions to the venue rule of `s 478(1)` (ss 478(2), (3), 479 to 481.2 here and others), and the provisions that limit `s 481.2` ("this or any other Act of Parliament").
  They have no single section label to be named for, so they are named for the thing asked and the provisions that answer it.
- Facts of other Acts, asked as plain facts: the Crimes Against Humanity and War Crimes Act (s 469(c.1)), the Oceans Act and the Immigration and Refugee Protection Act (s 477.1), and a warrant "in Form 7" (s 475(1)(b)(ii)).
- Section numbers cited by this part's text and tested as numbers only: ss 512 and 512.3 (s 482.1(4)) and ss 482(4), (5) (s 482.1(5)).
  Sections 625.1, 830 and 689(1) appear in the table of purposes of s 482(3), inside constructor names, and are not tested.

Answered to other parts (other parts ask this part):
- [T] ss 498, 515, 522, 523 (ccc20) and ss 536, 536.1, 554 (ccc21) ask for `s 469 the offence charged is one listed in section 469` (`MAYBE BOOLEAN`), which is the function of that name here.
  It takes a record, `s 469 facts of the charge` (the offence named as a `Provision of the Code`, the form of the charge, and three facts), and not only a section number, because paragraphs (b), (c), (c.1), (d) and (e) turn on more than the number.
  PLAN.md rule R1 says a provision that names offences by section number needs no input from the part that owns the offence; that holds for paragraph (a) alone.
  ccc20 and ccc21 will have to build the record at the merge, or take the answer as the input PLAN.md names.
  It answers `JUST FALSE` for an offence in none of (a) to (e) (F2).
- Not on the plan: `s 473(1)` is one of the routes by which the law "otherwise expressly provides" that `s 471` takes.

## Findings

### What the text turns out to say (numbered)

1. **Section 469(d) stops at (a)(vii).**
   An attempt to commit any offence mentioned in "subparagraphs (a)(i) to (vii)" is listed.
   (a)(viii), section 235 (murder), is not named in (d), so an attempt to commit murder is not listed by (d), while (e) ("conspiring to commit any offence mentioned in paragraph (a)") takes in murder.
   Attempted murder is section 239, which is not listed either.
   Asserted in `ccc15-tests-general.l4`: section 235 charged as an attempt is `JUST FALSE`; section 235 charged as a conspiracy is `JUST TRUE`; section 239 itself is `JUST FALSE`.
2. **Section 469(a)(i) names section 47 "(treason)"; section 183 names the same section 47 "(high treason)" (line 3529); section 46 is where high treason and treason are defined (lines 854 and 859).**
   Section 47 is the punishment section, headed "Punishment for high treason" (line 871) and "Punishment for treason" (line 873).
   Section 3 says the words in parenthesis form no part of the provision (line 256), so the list says section 47, and a charge named by section 46 alone is in none of (a) to (e) as the numbers stand.
   Asserted: section 46 itself is `JUST FALSE`.
   Paragraph (a)(ii) is shown repealed, yet (d) still counts through "(a)(i) to (vii)".
   Whether the omission of section 46 is a drafting gap, or a charge of high treason is always laid under section 47, is for a lawyer.
3. **Section 477.2(1.1) exempts only subsection (1) from summary conviction.**
   Subsections (2) and (3) have no such exception: a summary conviction proceeding is outside (1) but inside (2) and (3).
   `s 477.2(2)` and `(3)` have no mode-of-proceeding input.
4. **Section 477.3(3) says "without the consent" where section 477.2 says "unless the consent ... is obtained"**, and the brief's word lists give the two different answers (F17).
5. **Section 479's marginal note is "Offence outstanding in same province" but its text covers an offence "alleged to have been committed in the province in which he is" and a court "that would have had jurisdiction ... if it had been committed in the place where the accused is".**
   The place is a territorial division of that province, not another province.
   Section 478(1) is the only bar of the two sections; ss 478(2) to (4) and 479 give a rule for the place of trial, a permission to appear, duties and a deeming.
6. **Section 478(5) borrows a definition that is scoped to other sections.**
   "Newspaper has the same meaning as in section 297", and section 297 says "In sections 303, 304 and 308, newspaper means" (line 5913).
   Whether a definition scoped to three other sections reaches section 478 through the reference is not decided here.
   `s 478(5) newspaper` passes the answer of section 297 through, and is scoped by "In this section".
7. **Section 475(1) puts three powers and a proviso in one sentence, with different gates.**
   A "where" (the accused absconds) and, inside (b), two "if"s ("if it finds the accused guilty", "if a warrant in Form 7 is issued") and the proviso's "if it is satisfied".
   The functions separate them so that the gate that fails is visible (F5, F6).
8. **Section 482(2)(b) takes in "every appeal court within the meaning of section 812 that is not a court referred to in subsection (1)".**
   For a court that is also a court of subsection (1), `s 482(2) the court may make rules ...` answers `JUST FALSE` at paragraph (b), the text's own exclusion (F3).
   That court's power is the one in `s 482(1)`, which answers `JUST TRUE` for a court of appeal whose rules are not inconsistent with an Act of Parliament.
9. **"The parties to a case" (s 482.1(2)) is not defined in the range.**
   The accused and the prosecutor are both parties (the regulative rule is run for both).
   Whether any other participant is a party is not answered.
10. **Paragraph 476(c) has two limbs, and the section answers for all its paragraphs.**
    For a vehicle on a journey, on a road that is not a boundary, the second limb alone answers `JUST FALSE` (asserted at paragraph level in `ccc15-tests-special.l4`).
    The first limb applies but names only the divisions the vehicle passed through, so for a division it is not known to have passed through the section as a whole answers `NOTHING` (asserted in `ccc15-cases-seat.l4`).
11. **The "where" of section 479 and the relative clause of section 478(3) are different kinds of gate.**
    Section 479 opens "Where an accused is charged with an offence that is alleged to have been committed in the province in which he is", a "where" on a power, which answers `JUST FALSE` with the other "where" gates on powers (F6).
    Section 478(3) opens "An accused who is charged with an offence that is alleged ...", a relative clause that defines whom the subsection is about, a scope limit with no "only", which answers `NOTHING`.
12. **A rule whose gate is unmet is `FULFILLED`, and that is the only `DEONTIC` value an `#ASSERT` can compare** (see the next heading).

### What the stable binary does not accept (measured 2026-11-16)

The first item was measured with a small probe file run with `l4 run` on 1.6.110 (main, e51181d) and on 1.6.109 (main, 4c887e0), with the same answers on both; the rest are shown by the modules of this deposit, which `check.sh` runs on both builds:
- `#ASSERT <a DEONTIC rule whose gate is unmet> EQUALS FULFILLED` is accepted, `assertion satisfied`.
  `#ASSERT <a DEONTIC rule whose gate is met> EQUALS FULFILLED` (a standing obligation or permission) gives `assertion could not be evaluated: Trying to check equality on types that do not support it`, which `check.sh` counts as failed.
  Hence `ccc15-tests-duties.l4` asserts only the unmet-gate side (17 assertions) and exercises the met side with 26 `#TRACE`s.
  The traces print their outcomes and no assertion checks them; the whole run output of that module is identical on the two builds (diffed on 2026-11-16).
  The 26 trace results were read against the text and agree with it; none is asserted: 21 are `FULFILLED` (a permission exercised, a duty done, or a rule whose gate is unmet, which does not bind), 1 is a `BREACH` (`s 478(1)`: a court in a province tries an offence committed entirely in another province, which the text forbids), and 4 are standing residual obligations (the rule is in force and nothing has yet happened: `s 478(1)` as a prohibition, `s 478(3)` and `s 479` as duties to determine, `s 482.1(2)` as a duty to comply).
- As the brief asks for a regulative construct that cannot be asserted (`BRIEF.md` line 72), every rule in `ccc15-duties.l4` is also encoded as a decision function over the facts, in the layer-1 module named in the header of `ccc15-duties.l4`, and that function carries the assertions.
- A colon inside a backticked input name (`s 2 justice: the person is a justice or judge`) parses and evaluates on both builds.
- Accepted, and used: `PARTY party MUST ... LEST BREACH BY party BECAUSE "..."` with `party` a `GIVEN` (the residual prints `BY party` unresolved, which is cosmetic); `SHANT` with no `WITHIN` (prints `MUST NOT` and stands); `(WAITUNTIL n)`; a top-level definition used before the line that defines it (`s 477.2(1)` calls `s 477.2(1.1)`, which is defined below it); `Date (DATE_DAY d PLUS 8) (DATE_MONTH d) (DATE_YEAR d)` (day overflow rolls forward across a month end and a leap day: 25 February 2024 gives 4 March 2024, 25 February 2025 gives 5 March 2025, 28 December 2025 gives 5 January 2026, all asserted); `Day d MINUS Day c` for the number of days between two dates.
- Not used, so not probed: `REFUSE`, `#ASSERT REFUSED`, `YMD`, `EVERY`, `TYPICALLY`, a section `GIVEN`.
  The brief's rules for the stable line (parenthesise every `NOT`, one `#ASSERT` per line, no bulleted lists of strings) were followed.

### What the text does not answer

- Whether an offence that is both indictable and punishable on summary conviction is "an indictable offence" before the mode of proceeding is chosen (F1).
- Which Attorney General consents under s 473(1), which says only "the Attorney General": the input is a plain "the Attorney General consents" (ss 478(3) and 479 themselves name the Attorney General of Canada or of the province, by who instituted the proceedings).
- What "absconds" (s 475) and "found, arrested or in custody within the territorial jurisdiction" (s 470) mean: plain facts.
- Who must file the Attorney General's consent (s 477.2(4)), who must publish the rules of court (s 482(4)), and who may not withdraw the consent to trial without a jury (s 473(2)): no actor is named, and none is invented.
- What happens inside the eight days of s 477.2 with no consent yet, and whether the date is the court's or the accused's to watch (F10).
- Whether section 479's "place where the accused is" is a territorial division, a court's territorial jurisdiction or a place in the ordinary sense (finding 5).
- Terms of other Acts: "federal law" (section 2 of the Oceans Act), "permanent resident" (the Immigration and Refugee Protection Act), sections 4 to 7 of the Crimes Against Humanity and War Crimes Act, "marine installation or structure": plain facts.
- Whether a definition scoped to other sections reaches section 478 through the reference (finding 6), and whether a charge under section 46 is "listed" (finding 2).

### Limits of this work

- The independent test pass was not run: the brief forbids subagents, so none was used.
  The expected values are written by hand from the text, before the run, by the agent that wrote the rules.
- The tests exercise each branch and each threshold of each function: the eight-day period at both sides of its end, 500 and 501 metres, 47 and 48, 235 and 236, 477.1 and 477.4 and their neighbours, 512 and 512.3 and their neighbours.
  They do not test that a caller composes the functions correctly across parts: that is the merge's job (ccc20 and ccc21 will have to build `s 469 facts of the charge`).
- The `@ref` locators and quotations are checked by `srcrefs.py check --refs` and `--strict`; the `FALSE-kind` and `NOTHING-kind` quotations by `work/lint.py`, which looks each up in the text of lines 8524-8718.
  Neither checks that an encoding means what the text says: that is for a reviewer.
- Before the encoding is worth relying on: a lawyer's reading of the two marginal readings above and of F1, F2, F3, F5, F6, F8, F9, F17; the seams at the merge; and the seat's plain-fact seams (F18).

### What check.sh prints

Run on 2026-11-16 as `L4=<scratchpad>/bin/l4-main-110 L4_MAIN=<scratchpad>/bin/l4-main-109 L4_MAIN_TIMEOUT=0 ./check.sh`, target main; the output is verbatim.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc15-cases-seat.l4                            0       198       0        0         0 |      0       198       0        0  same
ccc15-duties.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc15-general.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc15-rules.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc15-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc15-special.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc15-tests-duties.l4                          0        17       0        0         0 |      0        17       0        0  same
ccc15-tests-general.l4                         0       109       0        0         0 |      0       109       0        0  same
ccc15-tests-rules.l4                           0        99       0        0         0 |      0        99       0        0  same
ccc15-tests-special.l4                         0       138       0        0         0 |      0       138       0        0  same
ccc15-tests-venue.l4                           0        98       0        0         0 |      0        98       0        0  same
ccc15-venue.l4                                 0         0       0        0         0 |      0         0       0        0  same
TOTAL (15 modules)                             0       659       0        0           |      0       659       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```
