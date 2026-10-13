# NOTES: Israel's HVAC work-licensing Law 5785-2025 and its Fees Regulations, encoded in L4 by a fleet

Row `legalese-full-sonnet-5.5`.
Status: `draft`.
No domain expert has read any of it against the Law.
One reading is ruled by the owner: day X of s.63(a)(1) is 16 July 2025, and the 16 October 2025 alternative is documented (section "Day X: the default and the 16 October alternative", under "Owner rulings").
Every other reading is the fleet's, assumed, not ruled, and is marked "assumed, not ruled" in the FRAGMENT that registers it.
The Wikisource text of the Law (revision 2947808, 10 July 2025) is unofficial; the gazette (Sefer HaChukim 3349) governs where the two differ, and `FRAGMENT-G*.md` say what each encoder checked against it.
Nothing is claimed verified against the gazette beyond what the encoders and the PLAN (section (f), trap T41) say they checked.
The numbers in this file were produced by `check.sh` (see "What check.sh prints") against the `l4` binary named there.

## What is encoded, and what is not

**Encoded.**
The whole of the Law: sections 1 to 63 and the First, Second, Third and Fourth Schedules.
The Fees Regulations made under ss.59 and 60, regulations 1 to 5, in three vintages (the SimpLEX draft of Figure 4, as made in Kovetz HaTakanot 11951, as amended in Kovetz HaTakanot 12383), and the SimpLEX test table (rows 5 to 8 and the worked example) run against all three.
Eight groups encoded it in parallel, each in modules of its own prefix, with tests in modules of their own: G1 ss.1 to 5 and 10 to 11 and the First Schedule; G2 ss.6 to 9 and the Second Schedule; G3 ss.12 to 18; G4 ss.19 to 29; G5 ss.30 to 40; G6 ss.41 to 57 and the Third Schedule; G7 ss.58 to 63 and the Fourth Schedule; G8 the Fees Regulations.
A ninth stage, the integration layer (modules `int-*.l4`), wires the eight together; it is the only place where one group's function is fed to another.

**Not encoded, and what stands in for it.**
The text of other statutes the Law refers to (the Electricity Law, the Engineers and Technicians Law, the Penal Law, the Interest and Linkage Law, the Budget Principles Law, the Securities Law, the Mandatory Tenders Law, the Freedom of Information Law, the Administrative Courts Law, the Collection Centre Law): what they decide is an input, named in the module that needs it.
Any order or regulation the Law lets the Minister make, other than the Fees Regulations: none appears in the sources, so the Schedules as enacted are the only vintage of each, the content of an order is an input, and a rule that needs a missing instrument returns a named refusal (orders under ss.3(b) and (c), 6(b), 41(b) and 63(a)(1); regulations under ss.36(a) via 60(1)(c), 46(b), 59 other than the Fees Regulations, 60(1) and 60(2)).
The Law after Wikisource revision 2947808 and the Fees Regulations after revision 3011135 (4 May 2026).
The consumer price index readings, the Director General's notices of updated fees under regulation 3(b), the calendar of days of rest, recess and holiday for any year, the identity and the opinions of the Registrar, the Commissioner, the Minister and the Council.
The SimpLEX draft beyond regulations 1 and 2(a) to (e) (regulations 3 to 5 are not visible in the screenshot) and the rows 1 to 4 and the second panel of its test table.

**One source is not what it was called.**
`knesset-bill-25_ls2_5256851.pdf` is the committee's text for the second and third readings, dated 11 December 2024, not the bill as tabled.
Wherever the brief or a FRAGMENT calls it "the bill as tabled", read it that way.

## Owner rulings

Rulings by the owner are recorded here, in the fork index below, and in `int-rulings.tsv`, which `int-gen-forks.py` merges into the index.
A ruling changes no default in any group module unless the line says so.
Every other reading in this encoding is "assumed, not ruled".

### Day X: the default and the 16 October alternative

This section concerns s.63(a)(1) and fork F-C-3 of group 7.

**Ruling line.** Fork F-C-3 (group 7); option: default (day X = 16 July 2025); condition: none; the owner's words, verbatim: "Use 16 July but document the 16 Oct alternative in the forks register or in notes."; ruled 2026-10-14 by Meng Wong, relayed to the integrator by the fleet lead in a message (no bench).

**The two readings.**
Section 63(a)(1) fixes "day X", the commencement day, as "three months from its publication or the entry into force of the regulations under section 59, whichever is later".
The default reading is the later of two DATES: three months after publication (the Law was published in Sefer HaChukim on 14.1.2025, so 14.4.2025) and the day the section 59 regulations came into force (16.7.2025, regulation 5 of the Fees Regulations), so day X is 16.7.2025.
This is group 7's default for fork F-C-3, and it is unchanged.
The documented alternative reads the single preposition "from" (in Hebrew a one-word prefix) as governing both limbs, so the three months run from the LATER of the two days, 16.7.2025, and day X is 16.10.2025.
The alternative comes from two sources that worked independently of the encoders, as the fleet lead reported them: an independent test author, and an independent blind hunt for contradictions in the sources (its finding E1, marked "probable").
Both point out that (a)(1) has no preposition before the date of entry into force of the regulations, whereas s.63(b) introduces the same kind of limb with the preposition "on".
The wiki's editorial note under (a)(1) names the date of the regulations (16.7.2025) and not of the Law, so it settles neither reading.
The owner chose the default and asked that the alternative be documented.

**What each reading moves.**

| what | default (ruled) | alternative (callable) |
| --- | --- | --- |
| day X, the commencement day (s.63(a)(1)) | 16.7.2025 | 16.10.2025 |
| lawful listed flammable refrigerant (paragraph (1)): the Law binds work from | 16.7.2025 | 16.10.2025 |
| any other refrigerant (paragraph (2)): 18 months after day X | 16.1.2027, a Saturday (IL s.10(c) is not applied to a commencement counted from another date: group 7, fork F-C-1) | 16.4.2027 |
| the Second Schedule's three-year transitional notes (items A2, B4, C5): three years after day X | end 16.7.2028 | end 16.10.2028 |
| the first limb of s.63(b), 18 months after day X, which matters for Chapter 6 only once a regulation under s.46 is known (none is in the sources) | 16.1.2027 | 16.4.2027 (callable in group 7; the integration's Chapter 6 functions use the default only) |
| the Fees Regulations (regulation 5: seven days from 9.7.2025) | in force 16.7.2025 | in force 16.7.2025: unaffected |

**How to run each reading.**
The default is every headline function of the integration: `int — the commencement day`, `int — the day the Law commences for work on a system with any other refrigerant`, `int — the Law has commenced for work on the system on the day`, and `int — the training the Second Schedule requires for`.
The alternative is `int (three months from the later of the two days) — the commencement day`, `int (three months from the later of the two days) — the day the Law commences for work on a system with any other refrigerant`, `int (three months from the later of the two days) — the Law has commenced for work on the system on the day` (all in `int-commencement.l4`) and `int (three months from the later of the two days) — the training the Second Schedule requires for` (`int-grant.l4`).
Group 7's own record is `the readings of the dates with the three months counted from the later of the two days`, and group 2 takes day X as an input date, so no group module changed.

**Tests.**
S23 and S24 in `int-tests-commencement-and-fees.l4` run, for each reading, the Second Schedule route and the paragraph (1) and (2) regimes on the days either side of each boundary, and S25 runs both readings side by side for the same applicant on the same days (an application on 17.7.2028, 16.10.2028 and 17.10.2028; R134a work on 16.1.2027, 15.4.2027 and 16.4.2027), where they differ on exactly the days the table above predicts.
Their expected values were worked by hand from the text and the ruling before they were run (`expectations.md`), and they are in the answer table below.
Question O38 below is answered for the default and stays open for a domain expert as to which reading the Law means.

## Layout and import graph

Everything is in one flat directory.
`domain.l4` is the shared vocabulary (parties, the licence kinds, the refrigerant, the record of offences and the other nouns the eight groups share), and `il-interpretation-time.l4` is the vendored module for the Interpretation Law's rules on counting time; it is pinned by its sha256 and is not edited.
Each group's modules start with its own prefix, `g1-` to `g8-`: rule modules first, then modules named `gN-tests-*`, which hold the group's own tests (including one `gN-tests-red.l4` of assertions that are meant to fail, each one a recorded alternative reading or a recorded contradiction).
`FRAGMENT-G1.md` to `FRAGMENT-G8.md` are the encoders' own notes: the forks, the coverage table, the nouns requests, the standard inputs, the open questions.
This file does not repeat them; it consolidates them across groups.
The modules with the prefix `int-` are the integration layer: `int-commencement`, `int-licence-status`, `int-work`, `int-sanction`, `int-grant`, `int-fees` and `int-council` wire the groups; `int-tests-*` test the wiring.
The modules with the prefixes `ind-a-`, `ind-b-` and `ind-c-` are the independent test authors' files, and `INDEPENDENT-ind-a-expectations.md`, `INDEPENDENT-ind-b-expectations.md` and `INDEPENDENT-ind-c-expectations.md` are their expectations documents (section "Independent tests").
They import across groups, as the integration modules do, because they test through the groups' exported functions.
`check.sh`, `check-traces.py` and `int-trace-expect.tsv` run the whole directory.
`int-rulings.tsv` holds the owner's rulings on forks, which `int-gen-forks.py` merges into the fork index.
`coverage-all.tsv` is the coverage table of all eight FRAGMENTs in one file.
`int-gen-graph.py`, `int-gen-forks.py` and `int-gen-coverage.py` produced the three generated tables in this file; run them again after editing a FRAGMENT or an `IMPORT` line (the first two take the name of an existing directory to write into; the third rewrites `coverage-all.tsv`).

Two rules keep the groups independent, and `check.sh` enforces the second.
A group module imports only `prelude`, `daydate`, `il-interpretation-time`, `domain` and modules of its own group.
Only an `int-` module may import across groups to wire them, and an `int-` module that imports a group is how that group's function reaches another's input; the `ind-` files import across groups only to test.

The import graph below is generated from the `IMPORT` lines of the files in this directory.
The order is a dependency order, which is also the order of `modules` in `encoding.json`.

| module | kind | imports |
| --- | --- | --- |
| `il-interpretation-time` | shared | `prelude`, `daydate` |
| `domain` | shared | `prelude`, `daydate` |
| `g1-adverse-action` | rule module of g1 | `prelude`, `daydate`, `il-interpretation-time`, `domain` |
| `g1-application` | rule module of g1 | `prelude`, `daydate`, `domain` |
| `g1-first-schedule` | rule module of g1 | `prelude`, `daydate`, `domain` |
| `g1-interpretation` | rule module of g1 | `prelude`, `daydate`, `domain`, `g1-first-schedule` |
| `g1-licensing-duty` | rule module of g1 | `prelude`, `daydate`, `domain`, `g1-first-schedule`, `g1-interpretation` |
| `g1-register` | rule module of g1 | `prelude`, `daydate`, `domain` |
| `g1-tests-adverse` | test of g1 | `prelude`, `daydate`, `domain`, `g1-adverse-action` |
| `g1-tests-application` | test of g1 | `prelude`, `daydate`, `domain`, `g1-application` |
| `g1-tests-first-schedule` | test of g1 | `prelude`, `daydate`, `domain`, `g1-first-schedule` |
| `g1-tests-interpretation` | test of g1 | `prelude`, `daydate`, `domain`, `g1-first-schedule`, `g1-interpretation` |
| `g1-tests-licensing` | test of g1 | `prelude`, `daydate`, `domain`, `g1-first-schedule`, `g1-interpretation`, `g1-licensing-duty` |
| `g1-tests-register` | test of g1 | `prelude`, `daydate`, `domain`, `g1-register` |
| `g1-tests-red` | test of g1 | `prelude`, `daydate`, `domain`, `g1-first-schedule`, `g1-interpretation`, `g1-licensing-duty`, `g1-adverse-action`, `g1-tests-licensing`, `g1-tests-adverse` |
| `g2-exemption` | rule module of g2 | `prelude`, `daydate`, `domain` |
| `g2-validity` | rule module of g2 | `prelude`, `daydate`, `il-interpretation-time`, `domain` |
| `g2-second-schedule` | rule module of g2 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g2-validity` |
| `g2-conditions` | rule module of g2 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g2-validity`, `g2-second-schedule` |
| `g2-temporary-licence` | rule module of g2 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g2-validity`, `g2-conditions` |
| `g2-renewal` | rule module of g2 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g2-validity`, `g2-conditions`, `g2-temporary-licence` |
| `g2-tests-fixtures` | test of g2 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g2-validity`, `g2-second-schedule`, `g2-conditions`, `g2-temporary-licence` |
| `g2-tests-conditions` | test of g2 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g2-validity`, `g2-second-schedule`, `g2-conditions`, `g2-tests-fixtures` |
| `g2-tests-exemption` | test of g2 | `prelude`, `daydate`, `domain`, `g2-exemption`, `g2-tests-fixtures` |
| `g2-tests-renewal` | test of g2 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g2-validity`, `g2-conditions`, `g2-temporary-licence`, `g2-renewal`, `g2-tests-fixtures` |
| `g2-tests-second-schedule` | test of g2 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g2-validity`, `g2-second-schedule`, `g2-tests-fixtures` |
| `g2-tests-temporary-licence` | test of g2 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g2-validity`, `g2-conditions`, `g2-temporary-licence`, `g2-tests-fixtures` |
| `g2-tests-validity` | test of g2 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g2-validity`, `g2-tests-fixtures` |
| `g2-tests-red` | test of g2 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g2-validity`, `g2-second-schedule`, `g2-conditions`, `g2-temporary-licence`, `g2-renewal`, `g2-tests-fixtures` |
| `g3-licensee-duties` | rule module of g3 | `prelude`, `daydate`, `il-interpretation-time`, `domain` |
| `g3-operator` | rule module of g3 | `prelude`, `daydate`, `domain` |
| `g3-training-duty` | rule module of g3 | `prelude`, `daydate`, `il-interpretation-time`, `domain` |
| `g3-tests-licensee-duties` | test of g3 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g3-licensee-duties` |
| `g3-tests-operator` | test of g3 | `prelude`, `daydate`, `domain`, `g3-operator` |
| `g3-tests-training-duty` | test of g3 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g3-training-duty` |
| `g3-tests-red` | test of g3 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g3-licensee-duties`, `g3-training-duty`, `g3-operator` |
| `g4-conflict` | rule module of g4 | `prelude`, `domain` |
| `g4-council-membership` | rule module of g4 | `prelude`, `daydate`, `il-interpretation-time`, `domain` |
| `g4-council-work` | rule module of g4 | `prelude`, `domain` |
| `g4-registrar` | rule module of g4 | `prelude`, `domain` |
| `g4-composition` | rule module of g4 | `prelude`, `daydate`, `domain`, `g4-registrar`, `g4-council-membership`, `g4-council-work`, `g4-conflict` |
| `g4-tests-composition` | test of g4 | `prelude`, `daydate`, `domain`, `g4-registrar`, `g4-council-membership`, `g4-council-work`, `g4-conflict`, `g4-composition` |
| `g4-tests-conflict` | test of g4 | `prelude`, `domain`, `g4-conflict` |
| `g4-tests-council-work` | test of g4 | `prelude`, `domain`, `g4-council-membership`, `g4-council-work` |
| `g4-tests-membership` | test of g4 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g4-council-membership` |
| `g4-tests-registrar` | test of g4 | `prelude`, `domain`, `g4-registrar` |
| `g4-tests-red` | test of g4 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g4-registrar`, `g4-council-membership`, `g4-council-work`, `g4-conflict` |
| `g5-inspectors` | rule module of g5 | `prelude`, `daydate`, `il-interpretation-time`, `domain` |
| `g5-senior-inspector` | rule module of g5 | `prelude`, `domain` |
| `g5-test-conduct` | rule module of g5 | `prelude`, `domain` |
| `g5-testing-bodies` | rule module of g5 | `prelude`, `daydate`, `il-interpretation-time`, `domain` |
| `g5-withdrawal` | rule module of g5 | `prelude`, `daydate`, `il-interpretation-time`, `domain` |
| `g5-tests-entry` | test of g5 | `prelude`, `domain`, `g5-inspectors`, `g5-test-conduct` |
| `g5-tests-inspectors` | test of g5 | `prelude`, `daydate`, `domain`, `g5-inspectors` |
| `g5-tests-senior-inspector` | test of g5 | `prelude`, `domain`, `g5-senior-inspector` |
| `g5-tests-test-conduct` | test of g5 | `prelude`, `domain`, `g5-test-conduct` |
| `g5-tests-testing-bodies` | test of g5 | `prelude`, `daydate`, `domain`, `g5-testing-bodies` |
| `g5-tests-withdrawal` | test of g5 | `prelude`, `daydate`, `domain`, `g5-withdrawal` |
| `g5-tests-red` | test of g5 | `prelude`, `daydate`, `domain`, `g5-inspectors`, `g5-senior-inspector`, `g5-testing-bodies`, `g5-test-conduct`, `g5-withdrawal` |
| `g6-nouns` | rule module of g6 | `prelude`, `daydate`, `domain` |
| `g6-notice-and-hearing` | rule module of g6 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g6-nouns` |
| `g6-appeal-and-publication` | rule module of g6 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g6-nouns`, `g6-notice-and-hearing` |
| `g6-payment` | rule module of g6 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g6-nouns`, `g6-notice-and-hearing` |
| `g6-schedule-three` | rule module of g6 | `prelude`, `daydate`, `domain`, `g6-nouns` |
| `g6-amount` | rule module of g6 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g6-nouns`, `g6-schedule-three`, `g6-notice-and-hearing` |
| `g6-warning` | rule module of g6 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g6-nouns`, `g6-schedule-three`, `g6-notice-and-hearing`, `g6-amount` |
| `g6-tests-amount` | test of g6 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g6-nouns`, `g6-schedule-three`, `g6-notice-and-hearing`, `g6-amount` |
| `g6-tests-appeal-and-publication` | test of g6 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g6-nouns`, `g6-notice-and-hearing`, `g6-appeal-and-publication` |
| `g6-tests-notice-and-hearing` | test of g6 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g6-nouns`, `g6-notice-and-hearing` |
| `g6-tests-payment` | test of g6 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g6-nouns`, `g6-notice-and-hearing`, `g6-payment` |
| `g6-tests-scenarios` | test of g6 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g6-nouns`, `g6-schedule-three`, `g6-notice-and-hearing`, `g6-amount`, `g6-payment`, `g6-warning`, `g6-appeal-and-publication` |
| `g6-tests-schedule-three` | test of g6 | `prelude`, `daydate`, `domain`, `g6-nouns`, `g6-schedule-three` |
| `g6-tests-warning` | test of g6 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g6-nouns`, `g6-schedule-three`, `g6-notice-and-hearing`, `g6-amount`, `g6-warning` |
| `g6-tests-red` | test of g6 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g6-nouns`, `g6-schedule-three`, `g6-notice-and-hearing`, `g6-amount`, `g6-payment`, `g6-warning`, `g6-appeal-and-publication` |
| `g7-administrative-courts` | rule module of g7 | `prelude`, `domain` |
| `g7-electrical` | rule module of g7 | `prelude`, `domain` |
| `g7-fourth-schedule` | rule module of g7 | `prelude`, `domain` |
| `g7-commencement` | rule module of g7 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g7-fourth-schedule` |
| `g7-regulations` | rule module of g7 | `prelude`, `daydate`, `il-interpretation-time`, `domain` |
| `g7-tests-administrative-courts` | test of g7 | `prelude`, `domain`, `g7-administrative-courts` |
| `g7-tests-commencement` | test of g7 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g7-fourth-schedule`, `g7-commencement` |
| `g7-tests-electrical` | test of g7 | `prelude`, `domain`, `g7-electrical` |
| `g7-tests-fourth-schedule` | test of g7 | `prelude`, `domain`, `g7-fourth-schedule` |
| `g7-tests-regulations` | test of g7 | `prelude`, `daydate`, `domain`, `g7-regulations` |
| `g7-tests-red` | test of g7 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g7-fourth-schedule`, `g7-electrical`, `g7-administrative-courts`, `g7-regulations`, `g7-commencement` |
| `g8-fees-nouns` | rule module of g8 | `prelude`, `daydate`, `domain` |
| `g8-fees-as-made` | rule module of g8 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g8-fees-nouns` |
| `g8-fees-as-amended` | rule module of g8 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g8-fees-nouns`, `g8-fees-as-made` |
| `g8-fees-draft` | rule module of g8 | `prelude`, `daydate`, `g8-fees-nouns` |
| `g8-fees` | rule module of g8 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g8-fees-nouns`, `g8-fees-draft`, `g8-fees-as-made`, `g8-fees-as-amended` |
| `g8-simplex-table` | rule module of g8 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g8-fees-nouns`, `g8-fees-draft`, `g8-fees-as-made`, `g8-fees-as-amended`, `g8-fees` |
| `g8-tests-dates` | test of g8 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g8-fees-nouns`, `g8-fees-draft`, `g8-fees-as-made`, `g8-fees-as-amended`, `g8-fees` |
| `g8-tests-fees` | test of g8 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g8-fees-nouns`, `g8-fees-draft`, `g8-fees-as-made`, `g8-fees-as-amended`, `g8-fees` |
| `g8-tests-reg3` | test of g8 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g8-fees-nouns`, `g8-fees-draft`, `g8-fees-as-made`, `g8-fees-as-amended`, `g8-fees` |
| `g8-tests-reg4` | test of g8 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g8-fees-nouns`, `g8-fees-draft`, `g8-fees-as-made`, `g8-fees-as-amended`, `g8-fees` |
| `g8-tests-simplex` | test of g8 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g8-fees-nouns`, `g8-fees-draft`, `g8-fees-as-made`, `g8-fees-as-amended`, `g8-fees`, `g8-simplex-table` |
| `g8-tests-red` | test of g8 | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g8-fees-nouns`, `g8-fees-draft`, `g8-fees-as-made`, `g8-fees-as-amended`, `g8-fees`, `g8-simplex-table` |
| `int-commencement` | integration | `prelude`, `daydate`, `domain`, `g7-commencement`, `g8-fees` |
| `int-council` | integration | `prelude`, `daydate`, `domain`, `g1-licensing-duty`, `g1-adverse-action`, `g3-training-duty`, `g4-council-work` |
| `int-fees` | integration | `prelude`, `daydate`, `domain`, `g7-regulations`, `g8-fees-nouns`, `g8-fees` |
| `int-grant` | integration | `prelude`, `daydate`, `domain`, `g2-second-schedule`, `g2-conditions`, `g2-renewal`, `g2-temporary-licence`, `g4-registrar`, `g4-council-work`, `g4-composition`, `g8-fees-nouns`, `g8-fees`, `int-commencement` |
| `int-licence-status` | integration | `prelude`, `daydate`, `domain`, `g1-adverse-action`, `g2-renewal`, `g2-validity`, `g3-training-duty`, `g4-council-work` |
| `int-work` | integration | `prelude`, `daydate`, `domain`, `g1-first-schedule`, `g1-interpretation`, `g1-licensing-duty`, `g1-adverse-action`, `g2-validity`, `g3-licensee-duties`, `g3-training-duty`, `g3-operator`, `g5-inspectors`, `g7-electrical`, `int-commencement`, `int-licence-status` |
| `int-sanction` | integration | `prelude`, `daydate`, `domain`, `g6-nouns`, `g6-schedule-three`, `g6-amount`, `int-commencement`, `int-work` |
| `int-tests-fixtures` | integration test | `prelude`, `daydate`, `domain`, `g1-first-schedule`, `g1-adverse-action`, `g2-temporary-licence`, `g3-licensee-duties`, `g3-operator`, `g4-registrar`, `g4-council-work`, `g6-nouns`, `g8-fees-nouns`, `int-commencement`, `int-work`, `int-sanction`, `int-council`, `int-grant` |
| `int-tests-commencement-and-fees` | integration test | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g2-second-schedule`, `g7-regulations`, `g8-fees-nouns`, `g8-fees`, `int-commencement`, `int-fees`, `int-grant`, `int-tests-fixtures` |
| `int-tests-consistency` | integration test | `prelude`, `daydate`, `il-interpretation-time`, `domain`, `g1-first-schedule`, `g1-adverse-action`, `g2-validity`, `g2-conditions`, `g3-licensee-duties`, `g3-training-duty`, `g4-council-membership`, `g5-inspectors`, `g5-testing-bodies`, `g6-nouns`, `g6-amount`, `g6-payment`, `g6-warning`, `g7-commencement`, `g7-electrical`, `g8-fees-nouns`, `g8-fees`, `int-commencement`, `int-licence-status`, `int-work`, `int-council`, `int-grant`, `int-tests-fixtures` |
| `int-tests-licence-life` | integration test | `prelude`, `daydate`, `domain`, `g1-first-schedule`, `g1-licensing-duty`, `g1-adverse-action`, `g2-validity`, `g2-second-schedule`, `g2-temporary-licence`, `g3-training-duty`, `g4-council-work`, `g6-nouns`, `int-commencement`, `int-licence-status`, `int-work`, `int-sanction`, `int-council`, `int-grant`, `int-tests-fixtures` |
| `int-tests-work-and-sanction` | integration test | `prelude`, `daydate`, `domain`, `g1-first-schedule`, `g1-interpretation`, `g1-licensing-duty`, `g2-temporary-licence`, `g3-licensee-duties`, `g3-operator`, `g5-inspectors`, `g6-nouns`, `g6-notice-and-hearing`, `g6-payment`, `g6-appeal-and-publication`, `int-commencement`, `int-licence-status`, `int-work`, `int-sanction`, `int-council`, `int-grant`, `int-tests-fixtures` |
| `int-tests-red` | integration test | `prelude`, `daydate`, `domain`, `g1-first-schedule`, `g1-licensing-duty`, `g2-validity`, `g3-training-duty`, `g4-council-work`, `g5-inspectors`, `g7-regulations`, `g8-fees-nouns`, `int-commencement`, `int-fees`, `int-licence-status`, `int-work`, `int-sanction`, `int-council`, `int-grant`, `int-tests-fixtures` |
| `ind-a-tests-commencement` | independent test (ind-a) | `prelude`, `daydate`, `domain`, `g7-commencement` |
| `ind-a-tests-fixtures` | independent test (ind-a) | `prelude`, `daydate`, `domain` |
| `ind-a-tests-duties` | independent test (ind-a) | `prelude`, `daydate`, `domain`, `ind-a-tests-fixtures`, `g1-application`, `g1-adverse-action`, `g1-register`, `g2-second-schedule`, `g2-conditions`, `g2-exemption`, `g3-training-duty` |
| `ind-a-tests-s10-s11` | independent test (ind-a) | `prelude`, `daydate`, `domain`, `ind-a-tests-fixtures`, `g1-adverse-action`, `g1-register` |
| `ind-a-tests-s12-s18` | independent test (ind-a) | `prelude`, `daydate`, `domain`, `ind-a-tests-fixtures`, `g1-interpretation`, `g3-licensee-duties`, `g3-training-duty`, `g3-operator` |
| `ind-a-tests-s2-s4` | independent test (ind-a) | `prelude`, `daydate`, `domain`, `g1-first-schedule`, `g1-interpretation`, `g1-licensing-duty` |
| `ind-a-tests-s5-s9` | independent test (ind-a) | `prelude`, `daydate`, `domain`, `ind-a-tests-fixtures`, `g1-application`, `g2-validity`, `g2-second-schedule`, `g2-conditions`, `g2-exemption`, `g2-temporary-licence`, `g2-renewal` |
| `ind-a-tests-sch2` | independent test (ind-a) | `prelude`, `daydate`, `domain`, `ind-a-tests-fixtures`, `g2-validity`, `g2-second-schedule`, `g2-conditions` |
| `ind-a-tests-ambiguous` | independent test (ind-a) | `prelude`, `daydate`, `domain`, `ind-a-tests-fixtures`, `g1-adverse-action`, `g2-second-schedule`, `g2-conditions` |
| `ind-a-tests-disagree` | independent test (ind-a) | `prelude`, `daydate`, `domain`, `ind-a-tests-fixtures`, `g2-second-schedule`, `g2-conditions` |
| `ind-b-tests-g4` | independent test (ind-b) | `prelude`, `daydate`, `domain`, `g4-registrar`, `g4-council-membership`, `g4-council-work`, `g4-conflict`, `g4-composition` |
| `ind-b-tests-g5` | independent test (ind-b) | `prelude`, `daydate`, `domain`, `g5-inspectors`, `g5-senior-inspector`, `g5-testing-bodies`, `g5-test-conduct`, `g5-withdrawal` |
| `ind-b-tests-g7` | independent test (ind-b) | `prelude`, `daydate`, `domain`, `g7-fourth-schedule`, `g7-commencement`, `g7-electrical`, `g7-regulations` |
| `ind-b-tests-ambiguous` | independent test (ind-b) | `prelude`, `daydate`, `domain`, `g4-council-work`, `g5-testing-bodies`, `g7-commencement` |
| `ind-b-tests-disagree` | independent test (ind-b) | `prelude`, `daydate`, `domain`, `g5-inspectors`, `g7-fourth-schedule` |
| `ind-c-tests-amount` | independent test (ind-c) | `prelude`, `daydate`, `domain`, `g6-nouns`, `g6-schedule-three`, `g6-notice-and-hearing`, `g6-amount` |
| `ind-c-tests-appeal` | independent test (ind-c) | `prelude`, `daydate`, `domain`, `g6-nouns`, `g6-notice-and-hearing`, `g6-appeal-and-publication` |
| `ind-c-tests-commencement` | independent test (ind-c) | `prelude`, `daydate`, `domain`, `g7-commencement`, `g8-fees` |
| `ind-c-tests-fees` | independent test (ind-c) | `prelude`, `daydate`, `domain`, `g8-fees-nouns`, `g8-fees-draft`, `g8-fees-as-made`, `g8-fees-as-amended`, `g8-fees` |
| `ind-c-tests-powers` | independent test (ind-c) | `prelude`, `daydate`, `domain`, `g6-nouns`, `g6-schedule-three`, `g6-notice-and-hearing`, `g6-amount`, `g6-payment`, `g6-warning`, `g6-appeal-and-publication` |
| `ind-c-tests-procedure` | independent test (ind-c) | `prelude`, `daydate`, `domain`, `g6-nouns`, `g6-notice-and-hearing`, `g6-payment` |
| `ind-c-tests-routes` | independent test (ind-c) | `prelude`, `daydate`, `domain`, `g1-first-schedule`, `g1-licensing-duty`, `g3-licensee-duties`, `g3-operator`, `g5-inspectors` |
| `ind-c-tests-schedule` | independent test (ind-c) | `prelude`, `daydate`, `domain`, `g6-nouns`, `g6-schedule-three` |
| `ind-c-tests-simplex` | independent test (ind-c) | `prelude`, `daydate`, `domain`, `g8-fees-nouns`, `g8-fees-draft`, `g8-fees-as-made`, `g8-fees-as-amended`, `g8-fees`, `g8-simplex-table` |
| `ind-c-tests-warning` | independent test (ind-c) | `prelude`, `daydate`, `domain`, `g6-nouns`, `g6-schedule-three`, `g6-notice-and-hearing`, `g6-amount`, `g6-warning` |
| `ind-c-tests-ambiguous` | independent test (ind-c) | `prelude`, `daydate`, `domain`, `g8-fees-nouns`, `g8-fees-draft`, `g8-fees-as-made`, `g8-fees-as-amended`, `g8-fees`, `g8-simplex-table` |
| `ind-c-tests-disagree` | independent test (ind-c) | `prelude`, `daydate`, `domain`, `g6-nouns`, `g6-schedule-three`, `g6-notice-and-hearing`, `g6-payment`, `g6-warning`, `g6-appeal-and-publication`, `g8-fees-nouns`, `g8-fees` |

Which groups each integration rule module imports:
| integration module | imports modules of groups (and how many modules of each) |
| --- | --- |
| `int-commencement` | G7 (1), G8 (1) |
| `int-council` | G1 (2), G3 (1), G4 (1) |
| `int-fees` | G7 (1), G8 (2) |
| `int-grant` | G2 (4), G4 (3), G8 (2) |
| `int-licence-status` | G1 (1), G2 (2), G3 (1), G4 (1) |
| `int-sanction` | G6 (3) |
| `int-work` | G1 (4), G2 (1), G3 (3), G5 (1), G7 (1) |

## The integration layer

### How each integration point is wired

The eight groups share no module: every fact one group needs from another is a `GIVEN` input under a standard name (PLAN section (c)).
Seven modules of the integration layer import the group modules and feed each group's inputs from the group that decides them.
Where the PLAN's input name and the encoder's exported name differ, the encoder's file governs and the wrapper adapts.
No group module was edited; no exported name was changed; no name clash was found, so there is no rename to list.

| IP | what is shared | wired in | note |
| --- | --- | --- | --- |
| IP1 | a licence is in force on a day | `int-licence-status`: `int — the licence kinds in force on the day`, `int — a licence of the person is not in force on the day` (group 2's function; group 1's s.10 functions read the same register fields) | group 5 does not consume IP1 (it asks for the inspector's reason to suppose); group 6 consumes it only inside the violation records |
| IP2 | the Law has commenced for the work on the system | `int-commencement`: `int — the Law has commenced for work on the system on the day` (group 7, the facts as the sources give them); fed to group 1 (s.3(a), s.4), group 3 (ss.13, 18), group 5 (the inspector's occasion, `int-work`) | group 3's ss.12 to 17(d) take the same boolean (fork COM); group 2 takes the commencement DAY (IP2's other form) |
| IP3 | which licence kinds fit a system | `int-work`: `int — the kinds appropriate to the work of` feeds group 3's input from group 1's activity-appropriate kinds (the lead's finding P1, row R1 of the register) | the capacity-only reading is callable |
| IP4 | whether the act is work on a cooling system | `int-work`: `int — the act of the situation is work on a cooling system` (group 1's s.2 and the First Schedule) fed to groups 3 and 7 | row R11 |
| IP5 | final certificate, programme approved, foreign qualification recognised | `int-grant`: `int — the Registrar approved the programme in`, `int — the foreign qualification was recognised in` (group 4, with IP7) | row R8; group 1's `s 2 — the certificate is a final certificate` is NOT wired to group 2: group 2 keeps a stand-in over the domain's `Certificate` and the Second Schedule's own wording decides |
| IP6 | the training required | `int-grant`: `int — the training the Second Schedule requires for` (group 2, with the commencement day from group 7) | group 1's field `further training the Registrar required` (s.10(d)) is the Registrar's input and no function computes it: not wired |
| IP7 | the Council was consulted and its advice validly given | `int-council`: a `Consultation of the Council` record builds both booleans for s.3(b), s.10(a), s.10(b), s.17(b), s.17(c) (through `int-licence-status`) and s.19(c) | row R6, A4 |
| IP8 | a licence condition was breached (the training duty) | `int-licence-status`: `int — the training duty was breached under the licence on the day`; `int-work`: `int — a licence condition was breached in the situation` | the conditions other than the training duty are an input |
| IP9 | a listed violation occurred | `int-work`: the producers of s.3(a), s.4, s.13, s.18(a) and s.31(2), each returning a `MAYBE Violation`; `int-sanction` consumes them | group 1 returns only the `Listed violation`; the wrapper builds the record |
| IP10 | the demand for a document was lawfully made | `int-work`: `int — the violation committed under section 31(2) by` calls group 5's test of the demand (the badge and certificate of s.32) | group 6 has no boolean input of that name; it takes the `Violation` |
| IP11 | the fee was paid in full | `int-grant`: regulation 4 of group 8 with the vintage, the service and the day, for a grant, a temporary licence and a renewal | row R9 |
| IP12 | index readings | inputs of `int-sanction` (`Facts for pricing a violation`) and `int-fees` | row R12; never defaulted |
| IP13 | entry into force of the s.59 regulations | `int-commencement`: group 8's regulation 5 date handed to group 7's record of facts | 16.7.2025 |
| IP14 | no order or regulation changes a Schedule or cap | no wiring: the assumption is stated in the groups' FRAGMENTs and in "What is encoded" above | |
| IP15 | days of rest, recess and holiday | no wiring: no headline function counts a D or W period; the calendar is an argument of the groups' own functions | row R3 |
| IP16 | Chapter 6 was in force on the day of the act | `int-commencement`: `int — Chapter 6 was in force on the day of the act` (and the `given the facts` form); `int-sanction` applies it | a refusal while no regulation under s.46 is known and the first limb has run |
| IP17 | the Registrar's discretions | inputs, named `in the Registrar's opinion ...`, on the records of `int-grant` and `int-council` | |
| IP18 | the s.6 conditions still hold | `int-licence-status`: `int — a condition for the grant of the licence ceased to hold` (negation of group 2's test) | S19 |
| IP19 | the end of validity and an extension under s.17(c) | `int-licence-status`: `int — the licence after the decision to extend` rebuilds the register's `Licence` with the recorded end | S11 |
| IP20 | a temporary licence is a grade 3 licence | `int-licence-status`: it enters the list of kinds like any other | group 2 refuses for the whole list if one temporary licence has no recorded last day (Q13) |
| IP21 | the licensee as a service electrician | `int-work`: `int — the licensee of the situation is treated as a service electrician`, `... may do the electrical work under section 61` | row R11 |

### The five headline functions

Each returns an answer or a named refusal with its reason, never a default.
`@export` is on every one, with `@desc` on every parameter; a function-typed parameter would have prevented it, and none is used.

| headline | function (module) | answers | refuses |
| --- | --- | --- | --- |
| (a) may this person be granted this licence on this day | `int — the Registrar must grant the licence on` (`int-grant`), for a temporary licence `int — the Registrar may grant a temporary licence on`, and for a renewal `int — the licence can be renewed on` (`int-grant`) | TRUE or FALSE: s.6(a)(1) to (4) all hold (the Second Schedule route completed in an approved programme, or a foreign qualification recognised after the Council's valid advice), regulation 4 does not bar the Registrar (the fee in the vintage, updated by regulation 3, was paid), and the application is made on or after the commencement day | an application made before the commencement day (the sources do not say whether the Registrar's duty had begun); a fee that needs a reading of the index that was not supplied; a subcommittee's advice whose procedure is unknown |
| (b) may this person do this work on this day | `int — the person may do the work of`, `int — the outcome of section 3(a) for the work of` (`int-work`) | the outcome of s.3(a) with the reason (not work, not yet commenced, exempted, permitted, no licence at all, no licence of the appropriate kind, works outside the conditions) | a system with no refrigerant recorded on the day group 7 cannot classify; a temporary licence with no recorded last day |
| (c) what is the sanction for this violation | `int — the sanction for` (and the wrappers for work, engagement and self-description) (`int-sanction`) | no listed violation; or no sanction because Chapter 6 had not commenced; or a sanction of an amount (the Third Schedule's column B updated by the index on the s.47(a) day, plus the s.45(a) and s.45(b) additions) | a dash in the corporation column (items (1), (2), (4)); Chapter 6 once the first limb of s.63(b) has run while no regulation under s.46 is known; an index reading that was not supplied |
| (d) the commencement day and the dates of the Fees Regulations | `int — the commencement day`, `int — the day the Law commences for work on a system with any other refrigerant`, `int — the Fees Regulations came into force on`, `int — the amending regulations came into force on`, `int — the day Chapter 6 commences` (`int-commencement`) | 16.7.2025; 16.1.2027; 16.7.2025; 4.5.2026 | the day Chapter 6 commences, without a regulation under s.46 |
| (e) the fee for a service in a vintage | `int — the fee in the vintage for the service on the day` (`int-fees`) | a figure, or NOTHING for a vintage silent on the service | a day on or after 1.1.2026 without the readings regulation 3 needs; the draft, which was never in force |

### What the headlines do not decide

The Commissioner's authorisation (s.41(a)) is a precondition of imposing a sanction and is not asked by headline (c), which gives the amount.
The Registrar's duty to grant is answered only from the commencement day of s.63(a)(1) on (row R4).
Headline (b) takes the First Schedule activity the act amounts to from the caller: the Law does not classify acts, and group 1 takes one activity per call.
No headline takes a calendar of rest days.

## Coverage, and the index of forks

### Coverage

Every provision of the Law and of the Fees Regulations has a disposition in the FRAGMENT of the group that owns it.
**Encoded** means a rule, a definition or a function in a module of that group.
**Inert** means the provision cannot be made executable; the coverage row says why (the brief asks for a reason of real length).
**Refused** means the provision is carried by a named refusal, because it depends on something the sources do not contain.
**Out of scope** means the text of another statute, or an amendment of another statute (ss.61 and 62 amend other laws), whose effect is taken as an input.
**Deferred** would mean a provision not yet encoded; there are none.
The counts below are produced from the eight tables by `int-gen-coverage.py`; the full table, one row per provision, is `coverage-all.tsv` (columns: provision, disposition, module, group).

| group | provisions listed | encoded | inert | refused | out of scope | deferred |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | 112 | 85 | 23 | 0 | 4 | 0 |
| G2 | 44 | 41 | 3 | 0 | 0 | 0 |
| G3 | 16 | 16 | 0 | 0 | 0 | 0 |
| G4 | 70 | 51 | 12 | 0 | 7 | 0 |
| G5 | 74 | 69 | 1 | 1 | 3 | 0 |
| G6 | 73 | 68 | 1 | 2 | 2 | 0 |
| G7 | 18 | 14 | 1 | 1 | 2 | 0 |
| G8 | 34 | 31 | 3 | 0 | 0 | 0 |
| ALL | 441 | 375 | 44 | 4 | 18 | 0 |

The row counts are the encoders' own, so a provision with sub-provisions can be one row in one group and several in another.
Sections 1 to 63 each have at least one row, and no section is listed by two groups (checked by script when this file was written).

### The index of forks

A fork is a place where the text supports more than one reading, or where two provisions give different answers to one question.
The reading taken is the one the brief's rulings or the encoder's judgement chose, and each is marked "assumed, not ruled" in the FRAGMENT that registers it.
The brief required that the other reading be a callable function with a test; the FRAGMENT says, fork by fork, which function and which test.
The table below lists every fork id with its group, what it is about, and the first sentence of the FRAGMENT that says which reading was taken.
The sentence is cut mechanically from the FRAGMENT and can read as a fragment of the reasoning; for the reasoning, the alternative's function name and the test, read the FRAGMENT at the line shown.

| fork | group | what it is about | reading taken (first sentence that says so) | FRAGMENT line |
| --- | --- | --- | --- | --- |
| `F1` | G1 | Whether "up to 18" and "up to 70" kilowatts include the limit | - Readings: (a) taken: the limit is inside, so grade 1 covers a system of exactly 18 kW and grade 2 one of exactly 70 kW; (b) the limit is outside. | FRAGMENT-G1.md:168 |
| `F2` | G1 | A cooling capacity that is not above zero (*assumed, not ruled*) | - Readings: (a) taken: a named refusal, `a cooling capacity that is not above zero cannot be matched to a licence kind`, wherever a capacity limit is read (grade 1 and grade 2, and so the list function); (b) read the limit literally, so that 0 and a negative number are "up to 18" and grade 1 covers ... | FRAGMENT-G1.md:176 |
| `F3` | G1 | Oil work, installation or maintenance (trap T8) | Taken: the Part is part of the classification the caller supplies, so the decision takes the activity, and the activity carries its Part (`the job kind of the activity`). | FRAGMENT-G1.md:184 |
| `F4` | G1 | B.1(3) and B.3(2) both reach components (trap T9) | Taken: the decision takes ONE activity; an act that both items describe is read, with Column A ("the kind appropriate . | FRAGMENT-G1.md:192 |
| `F5` | G1 | "Integral", and items A.1(11), A.1(12), B.1(14) (trap T10) | Taken: an act that does not stay inside the "only" limit of the item it is classified under is not work under that item (`s 2 — the act is work on a cooling system` is false; s.3(a) does not apply): electrical work outside the integral system belongs to the Electricity Law (ss.58 and 61, G7), and ac... | FRAGMENT-G1.md:202 |
| `F6` | G1 | "Monitoring, warning and control": any one function, or all three | - Readings: (a) taken: a permanently connected part is an accessory if it serves at least one of the three (a sensor that only monitors qualifies); (b) it must serve all three. | FRAGMENT-G1.md:210 |
| `F7` | G1 | The parenthesis of "integral electrical system" | - Readings: (a) taken: the parenthesis is part of the definition: a dedicated system that is part of the cooling system, part of the dedicated panel, and supplied by the manufacturer or supplied to its requirements or intended for it; (b) it only illustrates: a dedicated system that is part of a coo... | FRAGMENT-G1.md:217 |
| `F8` | G1 | A licence that is not in force: "no licence at all" or "not of the appropriate kind" | - Readings: (a) taken: a licence that is not in force is no licence: item (1); (b) the person holds a licence, but not one that is in force and appropriate: item (2). | FRAGMENT-G1.md:224 |
| `F9` | G1 | Work outside the conditions of a licence of the right kind (trap T12) | - Readings: (a) taken: the work is forbidden and no item prices it: `the listed violation committed under section 3(a)` is NOTHING; (b) it is counted as work without the appropriate kind: item (2). | FRAGMENT-G1.md:232 |
| `F10` | G1 | Whether the duties or conditions of an exemption order are conditions of the exemption | - Readings: (a) taken: the exemption lifts the s.3(a) licence requirement and stands; the order's duties bind as the order says; (b) the duties or conditions are conditions of the exemption: a person who does not meet them is not exempt. | FRAGMENT-G1.md:240 |
| `F11` | G1 | A consultation of the Council whose advice was not validly given (IP7) | - Readings: (a) taken: a consultation counts if the Council was consulted AND its advice was validly given (quorum, majority, subcommittee delegation: ss.24 to 26, G4); (b) it counts once the Council was asked. | FRAGMENT-G1.md:248 |
| `F12` | G1 | The reach of an exemption order | Taken: only the s.3(a) licence requirement is lifted; the person does not become a licensee, so s.4 still forbids advertising as one (the s.4 function has no exemption input); s.18(a) (an operator may not engage an unlicensed person) is G3's, and the INTEGRATOR decides whether it reads the exemption... | FRAGMENT-G1.md:255 |
| `F13` | G1 | "A licence of that kind" in s.4: the same kind, or a higher grade | - Readings: (a) taken: the same kind: a grade 3 holder who advertises as a grade 2 licensee holds no grade 2 licence (though he may lawfully do all grade 2 work, which s.3(a) allows); (b) a licence of a higher grade counts. | FRAGMENT-G1.md:261 |
| `F14` | G1 | When s.4 commences for an advertisement (*assumed, not ruled*) | - s.63(a) states the commencement of the Law for work on a system with a listed flammable refrigerant ((a)(1)) and for work on any other system ((a)(2)); an advertisement is not work on a system, and ... | FRAGMENT-G1.md:268 |
| `F15` | G1 | s.5(a): a duty to apply, or only the definitions of "applicant" and "licence application" | - Readings: (a) taken: a duty in form, `s 5(a) — the applicant must submit a licence application`, a MUST with no period and no consequence the Law names (no Third Schedule item prices it); (b) a procedural step that only defines "applicant" and "licence application". | FRAGMENT-G1.md:274 |
| `F16` | G1 | The order of the reasons s.3(a) does not apply (*assumed, not ruled*) | - The outcome function asks, in order: is the act work on a cooling system, has the Law commenced for it, is the system exempted by order; the first yes names the reason. - The text does not rank the ... | FRAGMENT-G1.md:282 |
| `F17` | G1 | Whether the three-year cap of s.10(a) reaches a restriction as well as a suspension (kind V) | - Readings: (a) taken: "for a period not exceeding three years" follows "restrict it or suspend it" (one item, the comma after "revoke a licence" closing the earlier items), so it reaches both; a restriction with no end is then outside the power; (b) it reaches the suspension only (the survey's read... | FRAGMENT-G1.md:288 |
| `F18` | G1 | Whether the day a suspension begins is its first day (kind V) | - Readings: (a) taken: the day the suspension begins is the event, so the last day allowed is the third anniversary (a suspension from 2026-03-01 may run to 2029-03-01); (b) the day it begins counts as its first day, so the last day allowed is the day before (2029-02-28). | FRAGMENT-G1.md:295 |
| `F19` | G1 | IL s.10(c) applied to the three-year cap (kind V, *assumed, not ruled*) | - Tests: begin 2026-03-01, ends 2029-03-02, with 2029-03-01 a day of rest (in on the alternative, out on the reading taken); two rest days in a row (1 and 2 March 2029, ends 2029-03-03: in); a rest day elsewhere (no effect) (`g1-tests-adverse`); red: one assertion. | FRAGMENT-G1.md:302 |
| `F20` | G1 | Ground (2) of s.10(a) and the renewal conditions of s.8 (see contradiction C4) | - Readings: (a) taken, the words: any condition ceasing grounds every measure, including a refusal to renew; (b) s.8 is carried into ground (2): the loss of the s.6(a)(4) condition alone cannot ground a REFUSAL TO RENEW (it can still ground a revocation). | FRAGMENT-G1.md:308 |
| `F21` | G1 | "Until final judgment" in s.10(b): the day of the judgment (kind V, trap T27) | - Readings: (a) taken: the suspension is in force through the day of the judgment; (b) it ends the day before. | FRAGMENT-G1.md:316 |
| `F22` | G1 | s.10(c), first limb: whether a written hearing is needed | - Readings: (a) taken, the words: no hearing is required for the direction, so the record has no field for one; (b) the hearing is required here too. | FRAGMENT-G1.md:325 |
| `F23` | G1 | s.10(c), second limb: whether the Council is consulted again | - Readings: (a) taken, the words: the preconditions are the limb's own (the period passed, the defect not cured to the Registrar's satisfaction, the hearing) and (a)'s ground, cap and hearing; the Council's consultation made for the direction suffices; (b) (a)'s Council consultation is carried in. | FRAGMENT-G1.md:332 |
| `F24` | G1 | IL s.10(c) applied to the period the Registrar sets for the cure (kind D, P12, *assumed, not ruled*) | - Discriminating case: 30 days from 2026-01-01 end on 2026-01-31; with that day a day of rest, IL s.10(c) moves the end to 2026-02-01, so the measure may be taken on 2026-02-02 and not on 2026-02-01 (on the alternative, on 2026-02-01). | FRAGMENT-G1.md:339 |
| `F25` | G1 | s.10(d): whether the power to add conditions to a new licence needs the Council | - Readings: (a) taken: the consultation is named in the first clause only, so the power needs only the revocation; (b) the power needs the consultation too. | FRAGMENT-G1.md:347 |
| `F26` | G1 | IL s.10(c) applied to the bar after a revocation (kind W, P13, *assumed, not ruled*) | - The period before which the person may not apply again is the complement of a window in which an application may be made; the brief's default for a window is to apply IL s.10(c). - The length and un... | FRAGMENT-G1.md:354 |
| `F27` | G1 | The day a revocation takes effect (*assumed, not ruled*) | - Readings: (a) taken: the licence is out of force from that day on; (b) from the day after. | FRAGMENT-G1.md:363 |
| `F28` | G1 | "Final certificate": what the domain certificate says | Taken: `s 2 — the certificate is a final certificate` tests the facts in a record of its own; `the Second Schedule calls the certificate a final certificate` states, for the seven constructors of the domain, that the Second Schedule's column A calls each of them a "final certificate". | FRAGMENT-G1.md:371 |
| `F29` | G1 | s.11(b): a passive sentence, a constitutive rule or a duty of the Registrar | - Readings: (a) taken: a passive sentence with no actor is not a duty (the phrasebook's entry 5.2): `s 11(b) — the register shows, on a query` (an EITHER: a query without identifying details is a named problem); (b) it implies a duty of the Registrar, who keeps the register. | FRAGMENT-G1.md:378 |
| `F30` | G1 | What is an opinion and what is a fact (*assumed, not ruled*) | - Where the Law says "in the opinion of", "if he saw", "holds that", "to his satisfaction" or "needed by him" the fact is the Registrar's (or the Minister's) and is an input named for the opinion: `in... | FRAGMENT-G1.md:385 |
| `FV1` | G2 | (trap T24; kind R and V) | (taken) the year of grant plus five, or (alternative) the year of grant plus four. | FRAGMENT-G2.md:134 |
| `FV2` | G2 | (kind V) | (taken); or it is applied to the five-year limb, 31 March being a date and not a period. | FRAGMENT-G2.md:144 |
| `FV3` | G2 | (P3; kind V) | (taken); or each further period continues from the day after the previous one ends. | FRAGMENT-G2.md:150 |
| `FV4` | G2 |  | (taken); or from the day after (the time module's `first day of a period counted from or after an event`). | FRAGMENT-G2.md:157 |
| `FV5` | G2 |  | (taken), which is how an extension under s 17(c) reaches s 8 (integration point IP19); or the Law alone governs and the register is evidence. | FRAGMENT-G2.md:162 |
| `FV6` | G2 |  | (taken), or on the day after. [Readings: a recorded revocation or suspension takes effect on the day recorded (taken), or on the day after.] | FRAGMENT-G2.md:168 |
| `FV7` | G2 | (trap T25; kind V) | (taken); or it is capped at the 31 March limb of the period it extends. | FRAGMENT-G2.md:174 |
| `FS1` | G2 | (trap T1) | Readings: the ungraded entry covers every Training Division certificate that no graded entry of the same Part names (taken: graded over general, so no Division certificate is in two items and each graded item keeps its purpose); or the ungraded entry covers every Division certificate of any grade (t... | FRAGMENT-G2.md:188 |
| `FS2` | G2 | (trap T2) | (taken); (a) item 1 applies only to an applicant with no prior training or experience at all; (b) item 1 also applies to the holder of a certificate its own column B names. | FRAGMENT-G2.md:196 |
| `FS3` | G2 | (trap T3) | Readings: the registration-alone item reaches the registered applicant who did not complete the programme (taken: the pair partitions on the programme, in line with s 6(a)(4)(b) and (c)); or it reaches every registered applicant (the literal text), so a technician with the programme is in B2 and B6. | FRAGMENT-G2.md:204 |
| `FS4` | G2 | (trap T5) | Part B heads column B "training or complementary studies required"; Parts A and C head it "requirements for the licence sought". The encoding reproduces column B as printed in every Part, so the table... | FRAGMENT-G2.md:210 |
| `FS5` | G2 | (trap T6) | (taken); or it is exactly N. [Readings: "training of up to N hours" is a ceiling on the course the Training Division runs, and the hours the applicant must complete are not stated (taken); or it is exactly N.] | FRAGMENT-G2.md:215 |
| `FS6` | G2 | (trap T4; wiki against gazette) | Taken: the gazette, which governs. | FRAGMENT-G2.md:220 |
| `FS7` | G2 | (kind B, outside IL s 10) | (taken); alternative adds them. | FRAGMENT-G2.md:227 |
| `FS8` | G2 | (kind C; P9; trap T7) | Taken: three years after the commencement day (an input DATE, IP2) by IL s 10(b), the last day inside the period; with a commencement day of 16.7. | FRAGMENT-G2.md:236 |
| `FS9` | G2 |  | "A grade 1 licence" in column A of B3(1), C3(1), C4(1): taken, a licence in force on the day of the application (the Schedule does not say that a lapsed, revoked or suspended licence counts); alternative `the reading with a licence named in column A counting although it has lapsed (FS9)`. | FRAGMENT-G2.md:245 |
| `FS10` | G2 | (the Division certificate of the grade sought; defect D1; repaired 2026-10-14) | Taken, in the engine: the certificate is not a column A entry of the ungraded rows (on both branches of FS1), item 1 applies to its holder whatever other item also fits them, and item 1 is returned with the entry "the certificate itself" added to its column B for the certificate they hold (`Second S... | FRAGMENT-G2.md:249 |
| `FS11` | G2 | (a Division certificate of a HIGHER grade than the one sought) | Readings: a certificate of a higher grade is not the certificate item 1 confers, so graded over general still puts its holder in the ungraded row (A3 for a grade 2 or grade 3 certificate seeking grade 1; B5(1) for a grade 3 certificate seeking grade 2: up to 50 hours) (taken, the unchanged reading: ... | FRAGMENT-G2.md:260 |
| `FC1` | G2 | (s 6(a) against regulation 4 of the Fees Regulations, group G8) | Taken: payment of the fee is a condition of the duty (the duty arises only where the fee was paid; s 59 empowers fees "for the grant of a licence"). | FRAGMENT-G2.md:270 |
| `FC2` | G2 | (s 6(a)(4): the three limbs and "in accordance with the Second Schedule") | Taken: (4) holds when one of (a), (b), (c) holds AND the Schedule's requirement for the licence sought is met. | FRAGMENT-G2.md:276 |
| `FC3` | G2 | (ss 19(b) and 19(c); integration point IP5) | Taken: the training or complementary studies the Schedule requires count as completed when the applicant completed them in a programme the Registrar approved (s 19(b)), or when the foreign qualification was recognised as meeting the training requirements (s 19(c)(1)). | FRAGMENT-G2.md:284 |
| `FC4` | G2 | (s 2 "final certificate"; IP5) | Taken: every certificate that column A names counts as a final certificate (the Schedule itself names each one as a final certificate), the youth school certificate included (`s 2 — the certificate counts as a final certificate`, a stand-in for group G1's test). | FRAGMENT-G2.md:289 |
| `FC5` | G2 |  | s 6(a)(1) asks that the applicant be an adult and states no age; the word is read as the `of full age` flag of the `Applicant` record (domain.l4), which carries the same note. There is no number to gi... | FRAGMENT-G2.md:294 |
| `FC6` | G2 |  | Taken: without the approval no power arises and nothing is permitted (the rule is `FULFILLED`). | FRAGMENT-G2.md:298 |
| `FC7` | G2 | (the certificate the course confers; repaired 2026-10-14, defect D1) | Now taken: the holder has met item 1 and nothing further is asked. | FRAGMENT-G2.md:304 |
| `FT1` | G2 | (s 9(a) "notwithstanding ss 6 and 8") | Taken: the expert need meet only s 9(a)(1) to (3) and be from a foreign state; s 6(a)(1) (adult), (2) (citizen or resident, which a foreign expert cannot be) and (3) (no disqualifying offence) are not asked. | FRAGMENT-G2.md:315 |
| `FT2` | G2 | (kind V) | (taken); alternative: IL s 10(c) applied to that last day (`s 9(a) (Interpretation Law s 10(c) applied) — the latest last day of a temporary licence granted on`). | FRAGMENT-G2.md:320 |
| `FT3` | G2 | (kind V; P5) | The renewal's one-year cap is counted from the last day of the term it renews (the terms run consecutively) (taken: 31.1. | FRAGMENT-G2.md:325 |
| `FT4` | G2 | (kind B) | (taken) or does. | FRAGMENT-G2.md:329 |
| `FT5` | G2 |  | "a system whose cooling capacity is above 70 kW": a single invited system (the text says "a system"), strictly above 70, so a system of exactly 70 kW (a grade 2 system, s 2) does not qualify. No alter... | FRAGMENT-G2.md:333 |
| `FT6` | G2 |  | "similar" systems and "authorised" abroad are facts supplied with the application, not the Registrar's opinion, which the text reserves for (3).... | FRAGMENT-G2.md:337 |
| `FR1` | G2 | (trap T26, groups G1 and G2) | Taken: s 8's second limb states when a licence can be renewed (a boolean test: the passive "can be renewed" is an eligibility test, neither a permission nor a duty), and leaves the Registrar's duty or discretion to ss 5 and 10. | FRAGMENT-G2.md:342 |
| `S16` | G3 | kind D (a deadline for doing something): s.16, 30 days from the day of the change | Taken: (1). [Readings: (1) IL s.10(a) and IL s.10(c) (the brief's default for a deadline: the period does not end on a day of rest, recess or holiday, and then ends on the first later day that is not one); (2) IL ] | FRAGMENT-G3.md:82 |
| `S15` | G3 | kind X (a time an official fixes): s.15, "as he directed" | Taken: an input date, `the day the Registrar directed that the report or supply be made by` (a `MAYBE DATE`), never counted, so there is no IL s.10 question; NOTHING is no time limit, because the text states none. | FRAGMENT-G3.md:91 |
| `S17-B` | G3 | kind B (counted backwards): s.17(a), "the last year of the validity" | Reading taken: the days after the same day one year earlier than the last day of validity, up to and including the last day; found by plain comparison of dates (`s.17(a) — the same day one year earlier than`, clamped to the month's last day when the month lacks the day, IL s.10(b)'s clamp used by an... | FRAGMENT-G3.md:98 |
| `S17-V` | G3 | kind V (a period of validity): s.17(c), "not exceeding three months" | Taken: (1). [Readings: (1) three calendar months counted forwards from the last day of validity by IL s.10(b), without IL s.10(c) (the brief's default: a period of validity is not a time to act); (2) the same with] | FRAGMENT-G3.md:106 |
| `S17-N` | G3 | kind N (vague time): s.17(b) and s.17(f), "a reasonable time before" | Taken: an input judgement on the record (`notice was given a reasonable time before the date of the course`; `the publication was a reasonable time before the training`), together with the one thing the text fixes: the publication precedes the training and the notice precedes the course. | FRAGMENT-G3.md:113 |
| `S17-Q` | G3 | kind Q (a quantity): s.17(a), "eight hours at least" | A constant, 8; "at least" is inclusive. Tests: 8 hours met, 7.99 and 7.5 not met, 9 met, 4 and 4 met, 4 and 3 not.... | FRAGMENT-G3.md:118 |
| `COM` | G3 | (commencement; trap T20): ss.12, 15, 16 and 17 | Taken: the same input is read there as "the Law has commenced for the licensee's work" and gates the duty. | FRAGMENT-G3.md:124 |
| `S13a` | G3 | (the Standard "as its wording is from time to time"): s.13 | Taken: (1). [Readings: (1) the work is judged against the wording in force on the day it was done; (2) against the wording in force on the day it is inspected.] | FRAGMENT-G3.md:133 |
| `S13b` | G3 | (the form of s.13): "shall perform in accordance with" | Taken: (1), because a MUST with no deadline cannot be breached in a trace, and the sentence is a constraint on how work is done and not a duty to do work. | FRAGMENT-G3.md:142 |
| `S13c` | G3 | (s.13 against Third Schedule item (4)): trap T13 | Taken: the tightness test is judged against the wording in force on the day of the work. | FRAGMENT-G3.md:148 |
| `S14` | G3 | (s.14, when failure to show begins) | Taken: the licensee's duty stands from the demand until he shows the licence, with no WITHIN (the orderer's demand is a MAY: an orderer who never demands has used a liberty, not failed in a duty); the input `the licensee failed to show the licence on the demand` carries the judgement that failure ha... | FRAGMENT-G3.md:158 |
| `S15b` | G3 | (s.15, whether the duty to comply reaches a report) | Taken: (1), since a power to demand a report that bound nobody would be empty. | FRAGMENT-G3.md:164 |
| `S16b` | G3 | (s.16, what counts as giving notice) | Taken: the input is the day the notice was given to the Registrar; a notice not in the manner directed does not count (it does not match the act), so the duty runs on. | FRAGMENT-G3.md:171 |
| `S17-A` | G3 | (s.17(a), the window and an extension under (c)) | Taken: (1), since the extension is given "so as to fulfil the duty". | FRAGMENT-G3.md:177 |
| `S17-C` | G3 | (s.17(b), "in addition to the trainings under (a)") | Taken: (1). [Readings: (1) a course required under (b) does not count towards the eight hours of (a); (2) it counts.] | FRAGMENT-G3.md:183 |
| `S17-D` | G3 | (s.17(a), "and shall meet the requirements of those trainings") | Taken: (1). [Readings: (1) the requirements limb reaches every session that qualifies; (2) a session counts only if its requirements were met, and the limb adds nothing.] | FRAGMENT-G3.md:189 |
| `S17-E` | G3 | (s.17(a) with (e), no training available) | Taken: no excuse (the Registrar's remedy for the licensee is the extension of (c)). | FRAGMENT-G3.md:195 |
| `S17-F` | G3 | (s.17(b), reasonable notice) | Taken: (1), because a licensee cannot be bound to attend a course he was not told of in time. | FRAGMENT-G3.md:201 |
| `S17-T` | G3 | (s.17(c), when the decision may be taken) | Taken: (1). [Readings: (1) on or before the last day of validity as it stands (the power is over the validity of a licence that still has validity, and "licensee" means a holder of a licence); (2) at any time, eve] | FRAGMENT-G3.md:207 |
| `S17-V2` | G3 | (s.17(c), several extensions) | Taken: (1). [Readings: (1) each extension is for "a period not exceeding three months" counted from the last day of validity as it stands, and the text limits no number of extensions; (2) the three months are cumu] | FRAGMENT-G3.md:213 |
| `S17-M` | G3 | (s.17(c) against s.8: trap T25) | Taken: (1). [Readings: (1) the extension may pass 31 March of the fifth year, the limit of s.8, because (c) extends the "validity period" that s.8 defines and only an extension can lengthen it; (2) it may not pass] | FRAGMENT-G3.md:219 |
| `S17-d` | G3 | (s.17(d), when the deemed condition is breached; trap T12) | Taken: (1), because under (2) s.3(a) ("in accordance with the conditions of his licence") would bar every licensee from work for the whole of his last year. | FRAGMENT-G3.md:225 |
| `S17-W` | G3 | (s.17(a), a licence whose term is shorter than a year) | Taken: a session counts only if the licence was in force on the day attended (a field of the session), so training before the licence began is not credited. | FRAGMENT-G3.md:232 |
| `S18-B` | G3 | (s.18(b), conduct or result) | Taken: (1), because the text's means include sample checks (text 10.7), which cannot guarantee a result, and the means are listed "inter alia" as ways of making sure. | FRAGMENT-G3.md:238 |
| `S18-C` | G3 | (s.18(c), "including an owner or manager of a business") | Taken: (1), because each limb of the text then has a place in the encoding and (2) would leave the second limb with no effect. | FRAGMENT-G3.md:244 |
| `S18-D` | G3 | (s.18(c) against the Third Schedule) | Taken: (1). [Readings: (1) the word of the items is the operator of s.18(c) (the items are "contrary to s.18(a)"); (2) the definition does not reach the items, which then use an undefined word and cannot be applie] | FRAGMENT-G3.md:252 |
| `S18-H` | G3 | (s.18(a) against Third Schedule items (5) and (6)) | Taken: (1), since the Law speaks of persons who "hold" a licence for the purpose of doing work (s.2: a licensee is a holder of a licence to perform work). | FRAGMENT-G3.md:259 |
| `F-22-V` | G4 | (kind V: IL s.10(c) and a term) | Reading taken (the fleet default for V): IL s.10(c) is not applied; the term's last day is `s 10(b) — the last day of a period of 4 years after an event on` the day of appointment, and that day is inside the term. | FRAGMENT-G4.md:133 |
| `F-22-length` | G4 |  | Reading taken: each further term is four years counted on from the last day of the term before it ("[Hebrew, see the FRAGMENT]": each further one is a term of office, "[Hebrew, see the FRAGMENT]"). | FRAGMENT-G4.md:134 |
| `F-23c-year` | G4 | (kind B) | Reading taken: the year ending on the day of removal; a meeting belongs to it if it is not after that day and the day of removal falls before the first anniversary of the meeting (this uses the time module forwards from the meeting, so no date is ever subtracted). | FRAGMENT-G4.md:135 |
| `F-23c-sub` | G4 |  | Reading taken: they are not meetings of the Council and are filtered out. | FRAGMENT-G4.md:136 |
| `F-19a` | G4 | (s.19(a): is publication a condition of the appointment) | Reading taken: no; the appointment counts when the Minister appointed a Ministry employee. | FRAGMENT-G4.md:138 |
| `F-19a-actor` | G4 |  | Reading taken: the Minister, who appoints (the publication duty is the `HENCE` of the appointment). | FRAGMENT-G4.md:139 |
| `F-19c-advice` | G4 |  | "[Hebrew, see the FRAGMENT]": reading taken, the Council was consulted and its advice was validly given (ss.24 to 26), since a body that could not lawfully give advice was not consulted as the Council; the Registrar is not bound by what the advice says. | FRAGMENT-G4.md:140 |
| `F-base` | G4 | (the base of "[Hebrew, see the FRAGMENT]" in s.24 and s.25(a)) | Reading taken: the eleven seats of s.20, so a majority is six and the quorum is six with the chair among them. | FRAGMENT-G4.md:141 |
| `F-T28` | G4 | (trap T28) | Reading taken: (c) permits discussion only; a decision needs the quorum of (a) and the majority of (b), because (c) says "[Hebrew, see the FRAGMENT]" (deliberate), (b) says "[Hebrew, see the FRAGMENT]" (decisions), and (a) fixes "[Hebrew, see the FRAGMENT]" for meetings. | FRAGMENT-G4.md:142 |
| `F-25b-tie` | G4 |  | Reading taken: a named refusal, not FALSE. | FRAGMENT-G4.md:143 |
| `F-26a` | G4 | (functions as duties or powers) | Reading taken: duties (MUST, no time), since s.20 says the Council "[Hebrew, see the FRAGMENT]". | FRAGMENT-G4.md:144 |
| `F-26-sub` | G4 | (and F-26b) | Reading taken: only for the function of s.26(a)(3), the only one for which s.26(b) lets the Council delegate its powers, and only if the Council delegated and the subcommittee proceeded as the procedure the Council fixed under s.25(e) requires; if the Council fixed no procedure the text does not ans... | FRAGMENT-G4.md:145 |
| `F-21-actor` | G4 | and F-29b-actor | Reading taken: the prohibition falls on the appointer of s.20, the Minister, and, for service, on the member (s.29(b)). | FRAGMENT-G4.md:146 |
| `F-day` | G4 |  | Reading taken: the member does not serve from the day of the event; the last day of the term is a day of service (IL s.10(b)). | FRAGMENT-G4.md:147 |
| `F-20-2` | G4 | (the Registrar's membership and the office) | Reading taken: nothing ends the Registrar's membership with the office; ceasing to be the Registrar is the loss of a condition of seat 2, a ground for removal under s.23(b)(3), so the Registrar serves until the Minister removes him. | FRAGMENT-G4.md:148 |
| `F-23b1` | G4 | (trap T29) | Reading taken: s.23(b)(1) is read as written, so a proceeding on an offence that makes the person unfit is a ground whatever became of it. | FRAGMENT-G4.md:149 |
| `F-23b3` | G4 |  | Reading taken: all the conditions the Law puts on appointment: the item of s.20, the bar of s.21 and the bar of s.29(b). | FRAGMENT-G4.md:150 |
| `C-23a-b3` | G4 |  | Reading taken: the duty to remove arises only while the member still serves. | FRAGMENT-G4.md:151 |
| `C-27` | G4 | and G-27 | Reading taken: s.27(b) prevails over (a). | FRAGMENT-G4.md:152 |
| `F-28-scope` | G4 |  | Reading taken: both, the listed enactment and an act in the Council. | FRAGMENT-G4.md:153 |
| `F-DUTY` | G5 | (ss.30(a), 34(a), 36(a)): "the Minister will authorise" is a duty or a power | Reading taken: a duty to authorise (MUST). | FRAGMENT-G5.md:122 |
| `F-ACTOR` | G5 | (ss.30(c), 34(c), 37(a)(3)): the text names no actor | Inferred and taken: the Minister (s.30(c), who made the authorisation), the Ministry (s.34(c), the State acting through the Minister's office), the senior inspector (s.37(a)(3), who sets the checklist under s.33 def. | FRAGMENT-G5.md:130 |
| `F-COMPLY` | G5 | (s.31(2) with Third Schedule item (7)): is there a duty to comply with a demand | Reading taken: a duty on `a person` to give what was lawfully demanded, arising only on a demand the inspector could lawfully make, with no time limit because the text states none. | FRAGMENT-G5.md:137 |
| `F-REASON` | G5 | (s.31(3), s.37(a)(1)): whose belief, and what it depends on | The inspector's "reason to suppose" (s.31(3)) and the senior inspector's (s.37(a)(1)) are different belief-holders, each an input per limb (the worker; the engager). The truth of the suspicion is not ... | FRAGMENT-G5.md:142 |
| `F-OFFENCE` | G5 | (ss.30(b)(1), 35(2), 36(b)(1)): "offence" is bare | Reading taken: a criminal offence only. | FRAGMENT-G5.md:149 |
| `F-PROCEEDING` | G5 | (ss.35(2), 36(b)(1)): a "criminal proceeding on suspicion of an offence" | Reading taken: a pending indictment, the domain's `charged with a criminal offence and no final judgment yet`. | FRAGMENT-G5.md:155 |
| `F-JUDGE` | G5 | (s.35(2)): whose judgement is "unfit" | Taken: the Minister's, an input (`a conviction is for an offence that makes the person unfit`). | FRAGMENT-G5.md:162 |
| `F-NONE-DIRECTED` | G5 | (ss.30(b)(3), 35(5)): "as the Minister directed", "if set" | The input is a `MAYBE BOOLEAN`: `NOTHING` is "none directed or set", which leaves nothing to meet, so the limb holds; `JUST` says whether what was directed or set is met. Section 35(5) names the absen... | FRAGMENT-G5.md:167 |
| `F-DEMAND` | G5 | (s.32(2)): the certificate "which he will show on demand" | Reading B, taken: the showing is part of limb (2), so an inspector whose certificate was demanded and not shown does not meet it and may not use his powers. | FRAGMENT-G5.md:173 |
| `F-ITEM7` | G5 | (s.31(2) with s.32 and Third Schedule item (7)): is a demand by an inspector who fails s.32 a demand "given under s.31(2)" | Reading taken: no; the demand counts for item (7) only if the inspector could lawfully make it, s.32 included. | FRAGMENT-G5.md:183 |
| `F-WITHDRAW` | G5 | (s.37(b)(2), (3)): consent the occupier withdrew | Reading taken: a consent withdrawn before the tests began no longer stands. | FRAGMENT-G5.md:190 |
| `F-PUBLISH` | G5 | (s.37(a)(3)): is publication of the checklist a condition of using it | Reading taken: no, a duty only (the second clause is a free-standing command, and the consequence of not publishing is unstated). | FRAGMENT-G5.md:197 |
| `F-CHANGE` | G5 | (s.36(d)): the scope of the power to change | Reading A, taken: the change power is narrower than the setting power. | FRAGMENT-G5.md:203 |
| `F-GROUNDS` | G5 | (s.39(a), (b)): which grounds are "under (a)(2) or (3)" | Reading taken: section 39(b) bars only a revocation or suspension resting on (a)(2) or (3); where (a)(1), (4) or (5) also exists the Minister can act under it without a demand. | FRAGMENT-G5.md:210 |
| `F-OVERLAP` | G5 | (s.33 defs 2 and 5): a tester who is also an expert | Reading taken: the definitions literally, so an employee authorised only to test is both a tester and an expert. | FRAGMENT-G5.md:217 |
| `F-LOOP` | G5 | (s.35(3), s.33 defs 2 and 4): the circularity | Reading taken: "testers" in s.35(3) are persons who hold the s.36 authorisation to test, whatever their employer's status. | FRAGMENT-G5.md:223 |
| `F-DISCLOSE` | G5 | (s.38(c) with ss.34(d), (e), 38(b)): the exception "except to carry out the act" | Reading taken: a disclosure the Law itself orders (the reports of s.34(d) and (e), the hand-over of s.38(b)) is not caught. | FRAGMENT-G5.md:229 |
| `F-OVERLAP-RULES` | G5 | (s.34(f) with s.36(d)): two sources of operating rules | See contradiction C4. The sources do not say which prevails, so the answer is a named refusal: `s 34(f), s 36(d) — the party whose rule governs when the instrument of authorisation and the senior insp... | FRAGMENT-G5.md:235 |
| `F-COMMENCE` | G5 | (s.63(a), integration point IP2): the powers are used only where the Law has commenced for the work | The commencement of the Law is "for the work on a system", by refrigerant, so the powers "to supervise implementation of the Law's provisions" are read as used only for work the Law has reached. The i... | FRAGMENT-G5.md:240 |
| `F-P22` | G5 | period the period an inspector directs for keeping measurements and tests, s.31(4) | Kind X, read as V (a duration); IL s.10(c) not applied; taken. | FRAGMENT-G5.md:257 |
| `F-P23` | G5 | period the period of an authorisation of a tester or expert, s.36(e) | Kind X, V; IL s.10(c) not applied; taken. | FRAGMENT-G5.md:258 |
| `F-P24` | G5 | period the period of a suspension, s.39(a) | Kind X, V; IL s.10(c) not applied; taken. | FRAGMENT-G5.md:259 |
| `F-P25` | G5 | period the time the Minister directs for meeting a demand, s.39(b) | Kind X, D; IL s.10(c) applied; taken. | FRAGMENT-G5.md:260 |
| `F-START` | G5 | (P22, P23, P24): is the day the period runs from a day of the period | Reading taken: yes; IL s.10(a) leaves the first day out of the COUNT ("that day is not counted"), not out of the period, so an authorisation granted on a day is in force on that day, a suspension begun on a day suspends that day, and a retention directed on a day covers it. | FRAGMENT-G5.md:267 |
| `F-STATUS-DAY` | G5 | (the status equation of ss.36(e) and 39): the day of a revocation, the day a suspension begins | Reading taken: not in force on the day of a revocation or from the day a suspension begins. | FRAGMENT-G5.md:276 |
| `F-D` | G6 | kind D, a deadline for doing something (P31, s.48: 30 days from delivery of the payment demand) | Taken: IL s.10(a), the day of delivery not counted, and IL s.10(c) applied, so a last day that is a day of rest, recess or holiday moves to the next day that is not one (ruling 4). | FRAGMENT-G6.md:228 |
| `F-W` | G6 | kind W, a window in which a request or an act may be made (P26 s.43, P33 s.53(a), P35 s.56(a)) | Taken: IL s.10(a) and IL s.10(c) applied, as for F-D; the day of delivery is itself timely (F-ACTDAY) and an extension cannot shorten the 30 days (F-SHORTEN), both below. | FRAGMENT-G6.md:234 |
| `F-VALID` | G6 | kind V, a period of validity (P37 s.57(e): publication for four years or two) | Taken: IL s.10(b), years after an event, the last day inside the period; IL s.10(c) NOT applied (ruling 4). | FRAGMENT-G6.md:239 |
| `F-C` | G6 | kind C, a date counted from another date (P27 s.44(d): "at the end of that period") | Taken: the date is the last day of the s.43 period, whose end already has the kind-W reading; IL s.10(c) is NOT applied a second time by s.44(d) itself. | FRAGMENT-G6.md:246 |
| `F-X` | G6 | kind X, a length fixed by an official (s.43 and s.53(b): "the Commissioner may extend the said period") | Taken: the extension is the day the Commissioner chose, an input, used as it is; it is outside IL s.10. | FRAGMENT-G6.md:252 |
| `F-WINDOW` | G6 | kind B, "within two years of the previous violation" (P29 s.45(b)) | Taken, following the lead's note: the window classifies a violation; it is not a time for doing something. | FRAGMENT-G6.md:255 |
| `F-WINDOW-54` | G6 | kind B, "within two years of the day the warning was delivered" (P34 s.54(b)) | Taken and alternative as F-WINDOW. | FRAGMENT-G6.md:263 |
| `F-R` | G6 | kind R, "each 1 January" (P30 s.47(b)) | Taken: the update day is 1 January even when it is a day of rest, and the amount is updated from it; a recurring calendar date is not a period, so IL s.10 does not reach it. | FRAGMENT-G6.md:268 |
| `F-DASH` | G6 | (trap T14): the dashes in the corporation column for items (1), (2) and (4) | Taken: (a), at the decision level (`s 41(a) — the amount the Third Schedule fixes for . | FRAGMENT-G6.md:279 |
| `F-CAP` | G6 | (trap T15): the cap of s.41(b) against s.45 and s.47(b) | (taken); the cap also bounds what is payable after the s.45 additions and the s.47(b) updates. | FRAGMENT-G6.md:288 |
| `F-NOTICE` | G6 | a notice that omits what s.42(b) lists | Readings: it is not "a notice under s.42", so s.43 gives no right of representation and s.44(d) deems nothing: the day the demand is treated as delivered is NOTHING (taken, as the guard on the act); it is a notice that starts the 30 days whatever it states, gives the right, and is deemed a demand wh... | FRAGMENT-G6.md:294 |
| `F-EXT` | G6 | an extension without recorded reasons | (taken); it counts. [Readings: it is ignored (taken); it counts.] | FRAGMENT-G6.md:301 |
| `F-ACTDAY` | G6 | (the independent review, DIS-2): an act on the day of delivery (s.43, s.48, s.53(a), s.56(a)) | (taken); the period starts the day AFTER delivery, so an act on the day of delivery is late. | FRAGMENT-G6.md:307 |
| `F-SHORTEN` | G6 | (the independent review, DIS-3): an "extension" that ends before the 30 days are out (s.43, s.53(b)) | (taken); the Commissioner's day is the end whatever day it is. | FRAGMENT-G6.md:317 |
| `F-DEEMED` | G6 | (trap T16): which day is "the said date" in s.44(d) | (taken); (b) the day after that last day; (c) the day the notice of intention was in fact delivered. | FRAGMENT-G6.md:325 |
| `F-PERIOD` | G6 | (trap T16): the period for payment the notice and the demand state, against s.48's 30 days | (taken); a period stated in the demand governs when there is one. | FRAGMENT-G6.md:332 |
| `F-MONTHS` | G6 | (trap T18): "for each month in which the violation continues" | Readings: the months COMPLETED after the day the violation started, each month ending on the same-numbered day (IL s.10(b)), counting only if the violation was still continuing on that day (taken: the narrower reading, since a sanction is read strictly against the person it burdens); the calendar mo... | FRAGMENT-G6.md:338 |
| `F-START` | G6 | (trap T18): where the months of a violation after a warning are counted from | (taken); from the delivery of the warning. | FRAGMENT-G6.md:344 |
| `F-BASE` | G6 | (trap T18): whether the fiftieth is of the fixed amount as enacted or as updated | (taken); of the amount as enacted, the total then updated and rounded once. | FRAGMENT-G6.md:350 |
| `F-SAME` | G6 | (trap T17): "the same provision" in s.45(b) | (taken), so items (1) and (2) are both s.3(a) and items (5) and (6) both s.18(a); the same Third Schedule item. | FRAGMENT-G6.md:356 |
| `F-FLOOR` | G6 | what "the amounts fixed under this subchapter" are in s.46(a) | (taken); the column B amount alone, as updated. | FRAGMENT-G6.md:362 |
| `F-ADD` | G6 | the additions as a power or as a charge (s.42(b)(4) against s.45) | (taken); s.42(b)(4) tells the Commissioner to state in the notice «[Hebrew, see the FRAGMENT]» ("the authority to add to the amount of the sanction"), which reads like a power. | FRAGMENT-G6.md:367 |
| `F-DAY` | G6 | the order of the three limbs of s.47(a) | (taken); the demand's day, or the notice's for a silent violator, displaces a stayed appeal. | FRAGMENT-G6.md:372 |
| `F-ROUND` | G6 | a half-way amount | (taken); half to the even multiple. [Readings: half up (taken); half to the even multiple.] | FRAGMENT-G6.md:378 |
| `F-CHAIN` | G6 | each year's rounded amount as the next year's base | (taken); the update is applied to the unrounded amount and rounded once at the end. | FRAGMENT-G6.md:384 |
| `F-FIRST` | G6 | the first update day | Taken as an INPUT (`the year of the first update day`); the tests use 2026, the first 1 January after the Law was published on 14 January 2025 (the date line of Sefer HaChukim 3349, p. 182). | FRAGMENT-G6.md:389 |
| `F-ANCHOR` | G6 | what the 30 days of s.53(a) run from | (taken); the day of the breach the warning states. | FRAGMENT-G6.md:395 |
| `F-CANCEL` | G6 | a warning that was cancelled under s.53 and s.54 | (taken); s.54 applies to a warning delivered, cancelled or not. | FRAGMENT-G6.md:401 |
| `F-MUST54` | G6 | whether s.54 keeps s.42(a)'s condition that the Commissioner intends to impose a sanction | (taken); s.42(a) conditions the duty on «[Hebrew, see the FRAGMENT]» ("and he intends to impose"). | FRAGMENT-G6.md:407 |
| `F-APPEAL-DEEMED` | G6 | the day "notice of the decision" counts as delivered, for a violator who made no representations (s.56(a)) | (taken); the day the notice of intention was in fact delivered. | FRAGMENT-G6.md:412 |
| `F-INTEREST` | G6 | the unit of the s.49 input | Readings: the caller supplies the shekel interest and the arrears fees accrued over the delay, as the Interest and Linkage Law computes them (taken: the encoding invents no mechanics); the caller supplies rates for the whole delay and the encoding adds simple interest on the sanction. | FRAGMENT-G6.md:418 |
| `F-C-1` | G7 | (kind C): is IL s.10(c) applied to a commencement counted from another date? | Taken: (a), the fleet lead's ruling 4 (assumed, not ruled by the owner). | FRAGMENT-G7.md:168 |
| `F-C-2` | G7 | what "its publication" is | Taken: (a). [Readings: (a) the day the Law was published in Reshumot, Sefer HaChukim 3349, 14.1.] | FRAGMENT-G7.md:179 |
| `F-C-3` | G7 | "three months from [its publication or the entry into force of the regulations], whichever is later" | Taken: (a), which is also the survey's chain and the lead's assignment, and which treats "the entry into force of the regulations" as the date it is. RULED 2026-10-14 by the owner: option default: the later of the two DATES, so day X (the commencement day of s.63(a)(1)) is 16 July 2025; the alternative (three months from the LATER of the two days, day X 16 October 2025) stays callable; condition: none; the owner's words, verbatim: "Use 16 July but document the 16 Oct alternative in the forks register or in notes." | FRAGMENT-G7.md:194 |
| `F-C-4` | G7 | does the Law commence on the last day of the period, or the day after? | Taken: (a). [Readings: (a) the Law commences on the last day of the period of months, the same-numbered day (IL s.10(b): the period "ends" on that day); (b) the Law commences on the day after the period ends.] | FRAGMENT-G7.md:221 |
| `F-C-5` | G7 | is the commencement day bound for the whole day, or from 00.01? | Taken: (a), because the questions the other groups ask are about the day an act was done (a `DATE`). | FRAGMENT-G7.md:237 |
| `F-C-6a` | G7 | a system with refrigerants of both kinds | Taken: (a), on my reasoning and not the text's: each paragraph states the date from which the Law reaches work on systems of its description, and a later date given to another description does not take away the earlier one. | FRAGMENT-G7.md:245 |
| `F-C-6b` | G7 | a listed refrigerant whose use is not permitted by law | Taken: (a), the complement reading, because (2) is defined as the residual of (1). | FRAGMENT-G7.md:255 |
| `F-C-6c` | G7 | a system with no refrigerant recorded | Taken: a named REFUSE, only where the answer depends on the regime. | FRAGMENT-G7.md:264 |
| `F-C-7` | G7 | (trap T20): the provisions that are not about work on a system | Taken: a named REFUSE, `the Law has commenced, for a provision that is not about work on a system, on the day`. | FRAGMENT-G7.md:271 |
| `F-C-8` | G7 | (trap T19): Chapter 6 and the regulations under section 46 | Taken: (a): the sources cannot show that no regulation exists after their own dates (the Law's wiki revision is 2025-07-10), so "not yet" would be a guess. | FRAGMENT-G7.md:280 |
| `F-C-9` | G7 | the vintage of the Fourth Schedule, and "was permitted" | Taken: the Schedule as enacted is the only vintage modelled (the fleet lead's ruling 2). | FRAGMENT-G7.md:291 |
| `F-C-10` | G7 | where the date 16.7.2025 comes from | - The date the section 59 regulations entered into force is an input (IP13), decided by G8: regulation 5 of the Fees Regulations gives 7 days from the publication of 9.7.2025 (IL s.10(a)), which is 16... | FRAGMENT-G7.md:298 |
| `F-S4-1` | G7 | the Fourth Schedule: item (66), direction marks, and how a designation is matched | Taken: the gazette governs (the brief): `E170`. | FRAGMENT-G7.md:304 |
| `F-E-1` | G7 | (trap T32): s.58 against s.61 | - s.58: a licensee is treated as a service electrician for cooling systems, under s.6 of the Electricity Law, with no limit drawn from the First Schedule. - s.61: adds subsection (e) to s.6 of the Ele... | FRAGMENT-G7.md:316 |
| `F-E-2` | G7 | s.58 and s.61 are not gated on commencement | Taken: no gate. | FRAGMENT-G7.md:326 |
| `F-E-3` | G7 | s.58's status is for an act, not for the person | - The deeming holds "for cooling systems", so the rule takes the input `the act is work on a cooling system` (IP4) as well as the licence list; with a licence and an act that is not work on a cooling ... | FRAGMENT-G7.md:331 |
| `F-A-1` | G7 | (trap T39): s.62 against s.56 | Taken: (a) is the function `the fora for review of a decision, reading section 62 as additional to section 56`; (b) is `the fora for review of a decision, reading section 56 as the only route for a final decision of the Commissioner`; both are callable and neither is the Law's answer (no default is ... | FRAGMENT-G7.md:336 |
| `F-R-1` | G7 | how many heads of fee | Taken: (a). [Readings: (a) six heads, one per phrase; (b) five, the survey's count, with the temporary licence as one head.] | FRAGMENT-G7.md:346 |
| `F-R-2` | G7 | s.60(1)'s general power against s.60(2) | Taken: (a). [Readings: (a) the specific paragraph governs: no approval for the (2) matters; (b) the general power covers every matter, so approval is required for all.] | FRAGMENT-G7.md:353 |
| `F-R-3` | G7 | the powers are not gated on commencement | Taken: ss.59 and 60 carry no commencement gate and no `WITHIN`. | FRAGMENT-G7.md:362 |
| `F-R-4` | G7 | what a MAY rule says when its condition fails | - A DEONTIC cannot be asserted, so the assertable answer is the BOOLEAN gate (`s 59 — the approval the Minister needs to set fees has been given`, `s 60 — the procedure required for regulations on … has been followed …`, `s 63(a)(1) — the consultation needed for an order amending the Fourth Schedule... | FRAGMENT-G7.md:368 |
| `F-R-5` | G7 | the second sentence of s.59 and the approval | Taken: one approval gate for all six heads. | FRAGMENT-G7.md:373 |
| `F-R-6` | G7 | (kind X): the time for an application to renew (s.60(2)(a)) | Taken: `s 60(2)(a) — the last day for an application to renew a licence` takes the NOMINAL last day the regulation gives, as a MAYBE DATE, and a calendar; NOTHING is the named REFUSE `s 60(2)(a) fixes the time for an application to renew by regulations, and no regulation under section 60(2)(a) is in... | FRAGMENT-G7.md:378 |
| `F1` | G8 | vintage silence (T38) | silence is NOTHING (a head) or a named refusal (a regulation not visible); no figure crosses vintages... | FRAGMENT-G8.md:72 |
| `F2` | G8 | "in addition to the payment of the fee as stated in sub-regulation (a)" (T33) | I, which is what SimpLEX row 7 expects... | FRAGMENT-G8.md:73 |
| `F3` | G8 | "the exam" in regulation 2(b) as made | the practical exam only... | FRAGMENT-G8.md:74 |
| `F4` | G8 | whether the wiki's "(adjusted to 2025)" and "(adjusted to 2026)" notes are law | the printed figures take effect on the day their provision commenced and are updated from the first 1 January after it (reg.3(a))... | FRAGMENT-G8.md:75 |
| `F5` | G8 | reg.3(a) "the base index" of the first update day: "the index published in the month before the commencement" | published in the month (T37)... | FRAGMENT-G8.md:76 |
| `F6` | G8 | reg.3(a) "rounded to the nearest whole new shekel" at an exact half | up... | FRAGMENT-G8.md:77 |
| `F7` | G8 | when the rounding is done | after every update day... | FRAGMENT-G8.md:78 |
| `F8` | G8 | the first update day of an amount that took effect after the regulations commenced (158, and the narrowed 2(b)) | after the amount took effect... | FRAGMENT-G8.md:79 |
| `F9` | G8 | from when an update binds (reg.3(a) "shall be updated on 1 January", (b) "shall publish") | the update day... | FRAGMENT-G8.md:80 |
| `F10` | G8 | is the objection charge "a fee" that reg.3(a) updates (T36) | updated like the rest... | FRAGMENT-G8.md:81 |
| `F11` | G8 | reg.3(a) "the commencement day of these regulations" in the amended text | the principal regulations... | FRAGMENT-G8.md:82 |
| `F12` | G8 | reg.4 where the vintage fixes no fee for the service (the discriminator of T34) | not engaged... | FRAGMENT-G8.md:83 |
| `F13` | G8 | reg.4 first limb and a temporary licence (repaired after the independent test author's finding DIS-4) | the fee fixed for the application binds the grant, whether the Registrar is asked about the application or about the grant itself (the first version answered "free" when asked about the grant)... | FRAGMENT-G8.md:84 |
| `F14` | G8 | reg.4 "paid the fee in full" | at least... | FRAGMENT-G8.md:85 |
| `F15` | G8 | SimpLEX rows 5 and 6 say nothing about payment | paid in full ("approved" is not reachable otherwise)... | FRAGMENT-G8.md:86 |
| `F16` | G8 | the draft's regulation 4 is not visible | refusal... | FRAGMENT-G8.md:87 |
| `F17` | G8 | what the table's outcome words mean | as stated... | FRAGMENT-G8.md:88 |
| `F18` | G8 | kind C, regulation 5: seven days from publication, IL s.10(c) | the last day, IL s.10(c) not applied (the fleet default for C)... | FRAGMENT-G8.md:89 |
| `F19` | G8 | kind C, the amending regulations: no commencement clause | the day of publication; 00:01... | FRAGMENT-G8.md:90 |
| `F20` | G8 | kind R, the update day: 1 January each year | outside IL s.10... | FRAGMENT-G8.md:91 |
| `F21` | G8 | kind B, "the month before their commencement" | June 2025... | FRAGMENT-G8.md:92 |
| `F22` | G8 | kinds D, V and W | none... | FRAGMENT-G8.md:93 |
| `F23` | G8 | which day fixes the vintage and the update level for a service | the caller supplies the day; `the vintage of the Fees Regulations in force on` maps a day to a vintage... | FRAGMENT-G8.md:94 |
| `F24` | G8 | the draft's regulation 1 speaks of "the student" where the enacted text speaks of "a learner in a vocational training course" | the same four limbs for both... | FRAGMENT-G8.md:95 |
| `F25` | G8 | reg.4 "paid the fee in full" where the payer paid nothing and the fee needs an index update | nothing paid is not in full, with no index reading needed (assumed: the printed figures are positive and the guard of regulation 3 demands positive readings); anyone who paid something needs the updat... | FRAGMENT-G8.md:96 |

## The cross-group consistency register

This section lists every question that two or more groups answered, and says where they answered it differently or by a different convention.
Groups ran in parallel and could not read one another, so every row below is a place where two readings were made blind.
Nothing here has been silently harmonised.
Each row gives what each group does, which provision of the Law each answer rests on, the answer the integrated row wires (the fleet default), the callable function that gives the other answer, and the test that pins the two.
"Tested" names a test module of this row; the modules `int-tests-consistency.l4`, `int-tests-work-and-sanction.l4` and `int-tests-licence-life.l4` carry the assertions.
Findings first (rows where an answer differs), then conventions that agree.

### Rows where the groups answer differently

**R1. "Appropriate to the work": capacity alone, or capacity and the First Schedule (groups 1, 3, 6).**
Group 1 (s.3(a)) calls a licence kind appropriate to a piece of work when it covers the capacity of the system (s.2) and the First Schedule's column A lists the activity under it.
Group 3 (s.18(a)) was given, by the PLAN's integration point IP3, only the kinds that cover the capacity of the system.
Third Schedule items (2) and (6) use the same Hebrew phrase for the worker and for the operator who engages the worker.
Discriminating case (found by an independent test author, the fleet lead's wiring finding P1): a grade 1 holder adds oil in maintenance (First Schedule B.3(3), listed under grade 3 only) on a 5 kW system.
The worker commits item (2).
Wired from capacity alone, the operator who engaged her commits nothing; wired from the activity-appropriate kinds, the operator commits item (6).
Wired default: the activity-appropriate kinds (`int — the kinds appropriate to the work of`, int-work), by the lead's instruction.
Alternative, callable: `int (capacity only) — the operator may engage the person in` and `int (capacity only) — the violation committed under section 18(a) in`.
Tested: S06 in `int-tests-work-and-sanction.l4` (default and alternative, and the same oil during installation, which is listed under grade 1), Q5 in `int-tests-consistency.l4`, red assertion 1.
Where the two coincide: every activity except B.3(2) and B.3(3), because the First Schedule gives all three grades the same lists; so the question matters only for those two items.

**R2. The first day of a period: does the day of the event belong to it? (groups 1, 2, 3, 4, 5, 6, 7, 8)**
The vendored module reads IL s.10 so that the first day of a period counted from or after an event E is the day after E (its fork F6, and its `is inside` functions).
Two conventions are in use, and they split by the kind of question, not by group alone.
(a) A STATUS that begins on E: E is a day of the status.
Followed by group 1 (a suspension runs from `suspended from`; a revocation takes effect on the day recorded, F27; the three-year cap of s.10(a) may end on the third anniversary, F18), group 2 (a licence is in force on the day it was granted, FV4; the five years end on the anniversary, FV1), group 4 (a member serves from the day of appointment; the four-year term ends on the anniversary, F-22-V and F-day), group 5 (an authorisation is in force on the day granted, F-START; a revocation or suspension takes effect on its day, F-STATUS-DAY), group 7 (the Law commences on the last day of the period of months or days, F-C-4) and group 8 (a text of the regulations is in force from its commencement day).
Groups 1, 2, 4 and 5 therefore give a status of "N units after E" that lasts N units and one day, the day E being its first day and the anniversary its last.
(b) A window in which something is DONE, counted from E: the period is E and the days after, up to the last day IL s.10(a) or (b) gives.
Followed by group 3 (s.16: notice on the day of the change is in time, on the last day is in time, one day later is late; tested) and group 6 after its review (s.43, s.48, s.53(a), s.56(a): an act on the day of delivery is timely, F-ACTDAY; tested here for s.43, s.48, s.53(a) and s.56(a), in S21 and Q3).
Before group 6's review it counted an act on the day of delivery as late, which led s.44(d) to deem a notice a payment demand for a violator who had in fact made representations; group 6 repaired that and moved the old assertions to its red file.
(c) A window COUNTED BACKWARDS from E, or a classification window: the module's convention (E is not inside).
Group 3 (s.17(a): the last year of validity is the days after the anniversary a year earlier, up to and including the last day) and group 6 (s.45(b) and s.54(b): the previous violation must come before the violation, and the violation must be no later than the last day).
Where the conventions of (a) and (c) meet there is a one-day difference with a real answer.
Discriminating case: a temporary licence granted 1.12.2025 and recorded to end 1.12.2026.
Group 2 has it in force on 1.12.2025; group 3's "last year of validity" begins on 2.12.2025, so training attended on the first day of the licence does not count towards the eight hours.
Wired default: each group's own convention; no function of the integration re-counts a period.
Alternative, callable: group 2 `s 8 (validity begins the day after the grant) — the licence ... is within its period of validity on`; group 5 `s 31(4), beginning the day after the direction`, `s 36(e), beginning the day after the grant`, `s 39(a), beginning the day after`; group 1 `the Registrar may take the measure under section 10(a), the cap counting the beginning day`.
Tested: Q2 and Q3 in `int-tests-consistency.l4` and S21 in `int-tests-work-and-sanction.l4` (assertions on groups 2, 3, 4, 5, 6 and 1 on the dates that tell the conventions apart), red assertions 11 and 12.

**R3. IL s.10(c) (days of rest) by kind of period, as coded (all groups).**
The brief's default is to apply IL s.10(c) to a deadline for doing something (D) and a window in which an application may be made (W), and not to a period of validity (V) or a commencement counted from another date (C).
As coded:
D and W, applied: group 1 (the period the Registrar sets for the cure, F24; the bar after a revocation, F26), group 3 (s.16), group 5 (the cure period of s.39(b), F-P25), group 6 (s.43, s.48, s.53(a), s.56(a); not at s.44(d), which counts from the s.43 end), group 7 (the time for a renewal application, s.60(2)(a), F-R-6).
V and C, not applied: group 1 (the cap of s.10(a), F19; "until final judgment", F21), group 2 (s.8, s.9, the three-year note), group 3 (s.17(c)), group 4 (s.22), group 5 (the periods an official fixes for keeping, authorising and suspending, read as V, F-P22 to F-P24), group 6 (s.57(e)), group 7 (s.63), group 8 (regulation 5).
Counted backwards or classifying, outside IL s.10: group 2 (experience, s.9(a)(2)), group 3 (s.17(a)), group 4 (s.23(c)), group 6 (s.45(b), s.54(b)), group 8 (the month before commencement).
Recurring dates, outside IL s.10: group 2 (31 March), group 6 (1 January, s.47(b)), group 8 (1 January, regulation 3).
Departures from the PLAN or from a naive reading: group 6 classifies the two-year windows of s.45(b) and s.54(b) as counted backwards or classifying (kind B, following a note from the fleet lead to that group) where the PLAN had kind W (apply IL s.10(c)); group 5 treats a length an official fixes (kind X) as V except where it is a time for the person to act (s.39(b)); group 1 treats the bar after a revocation as W because it is the complement of a window for making an application.
Wired default: the groups' own defaults; the headline functions take no calendar, because no headline function calls a function that counts a D or W period.
Alternative: every group offers a callable function with and without IL s.10(c); the integration adds none.
Tested: each group's own tests; no cross-group assertion, because no cross-group function counts such a period.

**R4. Commencement: which provisions wait for it, and on what? (groups 1, 2, 3, 4, 5, 6, 7)**
s.63(a) fixes a commencement only "for the performance of work on a system" (two regimes by refrigerant) and, in (b), for Chapter 6.
It fixes none for the Registrar, the Council, applications, the register, inspection or the regulation powers (trap T20).
Seven conventions are in use.
Group 1: s.3(a) and s.4 are gated (s.3(a) by the system's regime; s.4 by an input with two helper readings, F14); ss.5, 10 and 11 are not gated.
Group 2: ss.6 to 9 are not gated; the commencement day is an input only for the three-year note.
Group 3: ss.13, 14 and 18 are gated by the work's regime; ss.12, 15, 16 and 17(a) to (d) are gated by the same boolean read as "the Law has commenced for the licensee's work" (fork COM); ss.17(e) and (f) are not gated.
Group 4: not gated (no input).
Group 5: an inspector's, tester's and expert's powers are gated by a field naming the work supervised (F-COMMENCE); authorisations are not gated.
Group 6: all of Chapter 6 is gated by the boolean of s.63(b).
Group 7: its own answer for a provision that is not about work on a system is a named refusal, and the powers of ss.59 and 60 and the deeming of ss.58 and 61 are not gated.
Wired default: (i) work: group 7's boolean per system and day (`int — the Law has commenced for work on the system on the day`); (ii) the Registrar's duty to grant (headline (a)): answered from the commencement day of s.63(a)(1) on, the first day on which any reading gives the duty a live meaning, and a named refusal before it; (iii) Chapter 6: group 7's boolean, which refuses once the first limb has run while no regulation under s.46 is known, and the headline functions carry that refusal; (iv) an inspector's powers: the field is filled from group 7 (`int — the inspector's occasion with the commencement of the Law for`).
Alternative, callable: for (ii), group 2's ungated function (`int (with no commencement gate) — the Registrar must grant the licence on`), asserted TRUE on 15.7.2025 where the headline refuses.
Tested: S01 and S04 in `int-tests-licence-life.l4` (R134a is reached from 16.1.2027, propane from 16.7.2025), Q7 in `int-tests-consistency.l4`, S08 (continued) in `int-tests-work-and-sanction.l4`, red assertion 2.

**R5. The S13b modality change, and "will appoint" (groups 3, 4, 5).**
s.13 is a MUST in the text ("shall perform ... in accordance with"); group 3 encodes the converse as a SHANT so that a trace can show a breach, and offers the text's own MUST form as a callable function (fork S13b).
It does not change any boolean or any amount; the producers of the item (4) violation read the same facts either way.
Separately, the future tense "the Minister will appoint / authorise" is a duty (MUST) in group 4 (s.19(a), s.20) and in group 5 (ss.30(a), 34(a), 36(a)), while ruling 2 of the brief lists appointing among the powers to be encoded as MAY.
Group 5 registered the question (F-DUTY) and made the power reading callable; group 4 registered no fork and offers no power reading.
Neither reading changes an answer in a trace, because neither rule has a time limit, so the obligation cannot be breached whichever modality it carries.
Wired default: each group's own.
Alternative: group 5's `s 30(a), read as a power` and its siblings; none for group 4 (a finding for the fleet lead, see "Defects found in group modules").
Tested: groups 3 and 5 in their own tests.

**R6. Which function of s.26(a) is a consultation about a course under s.17(b)? (groups 3, 4)**
Group 4 lets a subcommittee give the Council's advice only on function (3) of s.26(a) (individual applications and decisions).
Function (3) names the recognition of a foreign qualification, the refusal to renew, the conditioning of renewal on training, revocation, restriction, suspension and the extension of validity; it does not name the requirement of a particular course under s.17(b) (group 3, contradiction C10).
So the requirement of a course is function (3) if "individual decisions" is read widely, and function (4), "any other function", if not.
Wired default (assumed, not ruled): function (3), for s.10, s.17(c) and s.19(c); function (1) for s.3(b); the caller builds the consultation for s.17(b) and so chooses.
Alternative, callable: `int — a consultation on another function whose advice came from` (function (4)).
Discriminating case: a subcommittee's delegated advice (procedure followed) on a course the licensee then misses: a breach of the deemed condition under function (3), none under function (4).
Tested: Q11 in `int-tests-consistency.l4` (three assertions), S09, S10, S11, S16 and S18 for the other consultations.

**R7. The word "offence" (groups 1, 2, 4, 5).**
s.6(a)(3) says "criminal offence"; s.21 and s.23 say "criminal or disciplinary"; ss.30(b)(1), 35(2) and 36(b)(1) say only "offence".
Group 2 reads s.6(a)(3) as criminal only and the Registrar's opinion as an input; group 4 takes a conviction of either kind that the appointer finds unfit as a bar to the Council and keeps its own record of proceedings; group 5 reads the bare "offence" as criminal (F-OFFENCE) and offers the disciplinary reading callable; group 1 (s.10(b)) takes an indictment and the Registrar's opinion as inputs.
Discriminating case: a conviction for a disciplinary offence that the authority finds makes the person unfit.
Group 2: no bar under s.6(a)(3).
Group 5: no bar to authorisation as an inspector (the alternative bars).
Group 4: a bar to appointment to the Council.
The difference follows the Hebrew; whether the bare "offence" of ss.30, 35 and 36 means both is for a domain expert (open question O-offence).
A second difference in representation: groups 2 and 5 use the domain's `Record of offences`; group 4 keeps a local list of proceedings with an outcome, because s.21 turns on whether a final judgment has been given.
Wired default: each group's own.
Tested: Q6 in `int-tests-consistency.l4` (the three groups on the same fact), red assertion 10.

**R8. Where a requirement of the licence comes from: the programme and the foreign qualification (groups 2, 4).**
Group 2 takes "the programme was approved by the Registrar" and "the foreign qualification was recognised" as inputs and requires the programme's approval even for an applicant who holds a final certificate (its fork FC3 makes the approval not a condition, as an alternative).
Group 4 offers two functions for s.19(b): the programme HAS the Registrar's consent, and it SATISFIES THE REQUIREMENT of consent (true also for a programme that needs none).
Wired default: the stricter (`int — the Registrar approved the programme in`), because a programme that cannot yield a final certificate cannot supply the training of s.6(a)(4)(a) in any case.
Alternative, callable: `int (a programme that needs no consent satisfies the requirement) — the requirement of the Registrar's consent is met by the programme in`.
Tested: S01 (programme with consent, without, none), red assertion 4.

**R9. "The fee was paid in full" (groups 2, 8, 1).**
Group 2's input is a plain "paid in full".
Group 8's regulation 4 is TRUE both when the fee fixed for the service was paid in full and when no fee is fixed for the service (as made, a theoretical exam).
For the services the Registrar gives or renews (a licence, a temporary licence's application) both vintages fix a fee, so the difference does not arise; for the Training Division's exams and objections it does.
Group 1 (s.5) needs no fee test: filing an application is a service neither vintage prices (it is silent), so regulation 4 bars nothing there.
Group 8 repaired its answer for the grant of a temporary licence (its fork F13, after an independent test author's finding): regulation 4 binds the grant by the fee fixed for the application, so asking about the grant service or about the application service gives the same answer, and the integration passes the application service.
Wired default: group 2's inputs from regulation 4's functions, with the service named for each consumer (the licence service for s.6, the temporary licence's application service for s.9).
Tested: S01, S02, S04 and Q8.

**R10. Three counts of what s.59 lets the Minister charge for (groups 7, 8, PLAN).**
The PLAN counted five heads; group 7 enumerates six (one per "for" phrase, the temporary licence's application and grant being two); group 8 prices nine services (the examinations head split into the practical and theoretical sitting and an objection to each).
They do not conflict: the nine services fall under the six heads.
`int — the head of fee under section 59 for the service` is the mapping; group 8's silence on a service is silence on a head only when it is silent on every service under the head.
Tested: S13 in `int-tests-commencement-and-fees.l4` (nine services, six heads, four under the examinations head, three heads priced by each vintage), red assertion 9.

**R11. Electrical work: s.58 and s.61 against group 1's definition of "work on a cooling system" (groups 1, 7).**
Group 7 (F-E-1) distinguishes a wide reading of s.58 from a narrow reading of s.61 for electrical work outside the First Schedule, taking "the act is work on a cooling system" as an independent fact.
Group 1 defines "work on a cooling system" as an act of a kind the First Schedule lists (s.2).
Wired together (IP4), electrical work the First Schedule does not list is not work on a cooling system, so s.58 does not reach it either, and the two readings of group 7 give the same answer.
Wired default: group 1's definition feeds group 7's input.
Alternative: group 7's two functions called with the fact given independently (asserted to differ: Q9).
Tested: S17, Q9, red assertion 5.

**R12. Index readings read two ways (groups 6, 8).**
Both groups consume the domain's `Price index reading`.
Group 6 (s.47(b)) finds "the index known on a day" as the reading of the latest month (year and month fields) among those published by the day.
Group 8 (regulation 3(a)) finds "the index published in November before the update day" and "the index published in the month before the commencement" from the month of `published on`.
A single list serves both only if each reading's month field agrees with the month before its publication.
The fixtures keep two lists (one per group) for that reason.
Group 6 takes the year of the first update as an input; group 8 derives the first update day (1 January 2026) from the commencement of the regulations; they use different rounding units (NIS 10 for the Law's sanctions, the whole shekel for the fees), both rounding a half up, both rounding after every update (each has the other reading callable).
Wired default: each group's own; the headline functions take the readings as inputs and never default them.

### Rows where the groups agree, with the test that shows it

**A1. A licence is in force (groups 1, 2, 3, 7).**
Group 2 decides it from the grant, the renewals and the register's `revoked on`, `suspended from` and `suspended until`; group 1's s.10 functions read the same three fields.
They were written apart and agree on every edge day tried: the day before and the day of a revocation, the first and last days of a suspension, a suspension with no end (until final judgment), a suspension that ends on the day of the judgment (IL s.8: "until" includes the day).
Both offer the effect-the-day-after alternative for a revocation and the two alternatives agree.
Tested: Q1 (`all` over twelve days for four licences), S09, S16.

**A2. A lapsed or revoked licence is no licence (groups 1, 3, 7).**
Group 1 (F8): work with a licence that is not in force is work with "no licence at all", item (1).
Group 3 (S18-H): an operator who engages a person whose licence is not in force commits item (5); and a holder of a lapsed licence is not a licensee for s.12.
Group 7: a lapsed licensee is not treated as a service electrician.
The alternative that counts a lapsed licence as held (item (2)) is callable in groups 1 and 3.
Tested: S01 (both functions), S05, S17, Q4, red assertion 3.

**A3. The capacity limits (groups 1, 2, 3, 6).**
Group 1 reads "up to 18" and "up to 70" kW as including the limit (F1); group 2 reads "over 70 kW" (s.9(a)(1)) as excluding 70; the two draw the same line.
"Not exceeding" and "up to" are inclusive everywhere (the three years of s.10(a), the year and the three months of ss.9 and 17(c), the twelve instalments of s.50, the caps of s.41(b)), "at least" is inclusive (the eight hours), and "more than" is strict (the half of the Council's meetings, s.23(c)).
Tested: S15.

**A4. The Council's valid advice (groups 1, 3, 4).**
Groups 1 and 3 take "consulted" and "advice validly given" as two booleans and require both; group 4 decides them from a consultation record (a request, and advice that is the Council's decision at a quorate meeting, or a delegated subcommittee's on function (3) with the Council's procedure followed).
The integration derives the booleans from one record, so the two cannot disagree.
Tested: S09, S10, S11, S16, S18.

**A5. The commencement day and the Second Schedule's three years (groups 2, 7, 8).**
Group 2 takes the commencement day as an input; group 7 computes it from the publication (14.1.2025) and the day the s.59 regulations came into force; group 8 computes that day (16.7.2025) from regulation 5.
The three years of the experience items end on 16.7.2028 whichever group's function computes them.
Tested: S12.

**A6. Violation identity and "one act, one sanction" (groups 1, 3, 5, 6).**
Groups 3 and 5 produce a `Violation` record; group 1 produces only the `Listed violation`; the integration builds the record (violator, item, reference, day).
Two acts by one person in two capacities (a licensee who is also an operator) are two violations with two references, each priced on its own (s.55 forbids more than one sanction for ONE act).
Items (1) and (2) both contravene s.3(a), items (5) and (6) both s.18(a), and group 6 takes "the same provision" as the provision, so an item (5) violation followed by an item (6) violation within two years is a repeat violation (the read-by-item alternative says it is not).
Tested: Q10, Q12.

**A7. Named refusal and silence (all groups).**
A figure the source leaves out is `NOTHING` where the source itself names the absent case (group 8's vintage silence, group 4's Registrar's term, group 1's "until final judgment") and a named `REFUSE` where the source does not answer (group 6's dash, group 7's missing regulations, group 5's missing conditions of s.60(1)(c), group 1's capacity of zero).
The integrated headlines pass both through: they never turn a refusal into a default.
Tested: S01, S04, S07, S12, S13, Q13.

## The answer table: the integration scenarios

Each scenario crosses three or more groups.
Every expected value was worked out from the Hebrew text before the test module was run (`expectations.md` in the integrator's work directory is the record for S01 to S19; the values of S20, S21, S22 and E1 were worked out the same way, written into the comments of their tests in the same step and recorded in `expectations.md` afterwards; one expectation of mine was wrong, see the note after the table).
"Light" means the dates are the sources' own; "hypothesis" means a date the sources do not give.
Amounts are new shekels.
The sanction scenarios use a hypothetical regulation under s.46 in force from 1.6.2026 (the Chapter 6 commencement is then 16.1.2027), a first update year of 2026, and index readings that give a ratio of 102/100 for 1 January 2026 and 1 for each later 1 January; so every Third Schedule amount is the enacted amount times 1.02 rounded to NIS 10.

| id | scenario | groups | answer | provisions |
| --- | --- | --- | --- | --- |
| S01 | An adult citizen with no prior training and a clean record applies for a grade 1 licence on 1.12.2025 | 2, 4, 8, 7 | the Second Schedule offers Part A item 1 (up to 350 hours conferring the grade 1 certificate, or the 3-unit certificate); the Registrar must grant when the training was completed in a programme with the Registrar's consent and 284 was paid; not when 283 was paid; not without the programme's consent; the headline refuses for an application of 15.7.2025 (the ungated reading says yes) | s.6(a), s.19(b), Second Schedule Part A item 1, regulations 2(c) and 4, s.63(a)(1) |
| S01 | The licence granted 1.12.2025 | 2 | last day of validity 31.3.2030 (five years would end 1.12.2030; 31 March of the fifth year from the year of grant, 2025 + 5, is earlier); in force 1.12.2025 and 31.3.2030, not 30.11.2025 or 1.4.2030 | s.8 |
| S01 | Work on 1.4.2030 on a 10 kW R134a system (activity A.1(2)) with that licence lapsed | 1, 2, 7 | forbidden: "no licence at all" (item (1)); on 31.3.2030 permitted; with a lapsed licence counted as held (the alternative) item (2) | s.3(a), s.63(a)(2), Third Schedule (1), (2) |
| S01 | Priced, a previous violation of s.3(a) on 10.1.2029 for which a sanction was imposed | 1, 6, 7 | repeat violation (two years after 10.1.2029 end 10.1.2031): 20,400 + 20,400 = 40,800; without the previous violation 20,400; on the sources alone (no s.46 regulation known) a refusal | ss.41, 45(b), 47(b), 63(b) |
| S02 | The same application on 1.2.2026 | 2, 8 | the fee is 284 x 101.25 / 100 = 287.55, rounded to 288: paid 288 the Registrar must grant, paid 284 or 287 not; with no index reading a refusal | regulation 3(a) and 4 |
| S03 | An applicant relies on a foreign degree; the Council is consulted | 4, 2, 8 | six of eleven present with the chair, 3 against 2: advice valid, the Registrar must grant; five present: not; never consulted: not; a subcommittee on an individual application with the Council's procedure unknown: refusal, procedure followed: yes, not followed: no | ss.19(c), 24 to 26 |
| S04 | A foreign expert invited for a 100 kW system, application 1.12.2025 | 2, 8, 7, 1, 6 | the Registrar may grant a temporary licence if 398 is paid (not if 397); it ends no later than 1.12.2026; an R134a system is not reached until 16.1.2027 (work on 1.6.2026 and 2.12.2026 permitted), then forbidden item (1) (20,400 on 20.1.2027); propane is reached from 16.7.2025 (work on 1.6.2026 permitted, on 2.12.2026 forbidden but Chapter 6 had not commenced: no sanction) | s.9, regulation 2(d), s.63 |
| S05 | An operator (corporation) engages a person for work A.1(2) on a 25 kW R134a system on 1.4.2030 | 3, 1, 2, 6, 7 | a grade 1 licence in force: grade 1 covers 18 kW only, so item (6), corporation 20,400; a lapsed licence: item (5), 40,800; a grade 2 licence in force: may engage, nothing priced | s.18(a), Third Schedule (5), (6) |
| S06 | A grade 1 holder adds oil in maintenance (B.3(3)) on 5 kW (the lead's finding P1) | 1, 3, 2, 6, 7 | the worker commits item (2), 10,200; the operator who engaged her commits item (6), 20,400; on the capacity-only reading no violation; the same oil added during installation (A.1(5)) is permitted to both | s.3(a), s.18(a), First Schedule A.1(5), B.3(3) |
| S07 | A licensee installs without the tightness test of the testing chapter of part 4 | 3, 2, 7, 6 | item (4): an individual 20,400; a corporation: the dash, a refusal; maintenance without the test: breach of s.13, no listed violation | s.13, Third Schedule (4) |
| S08 | An inspector demands a document and the person does not give it | 5, 6, 7 | item (7): individual 3,060, corporation 6,120; an inspector with no badge: no violation; a person who gave the document: none; where the Law has not commenced for the work supervised the inspector may not use the power | ss.31(2), 32, Third Schedule (7) |
| S09 | The Registrar proposes to revoke on ground (3) | 1, 4, 2, 7, 6 | may, with a valid consultation; not with five present (the unmet precondition is the invalid advice); revoked on 1.5.2028 the licence is in force on 30.4.2028, not on 1.5.2028; work on 1.5.2028 item (1), 20,400 | s.10(a), ss.24 to 26 |
| S10 | A particular course the licensee misses | 3, 4, 2, 1, 6 | not yet breached on 9.6.2027; breached on 11.6.2027, so s.3(a) forbids although the licence is of the right kind, and no Third Schedule item prices it (no sanction row); attended: permitted; Council advice invalid: no duty, no breach | ss.3(a), 17(b), 17(d) |
| S11 | The Registrar extends a licence ending 31.3.2030 by up to three months | 3, 4, 2, 1 | extended to 30.6.2030 after a valid consultation; in force 1.4.2030 and 30.6.2030, not 1.7.2030; work on 1.4.2030 permitted; without the extension item (1); with invalid advice no extension | s.17(c), s.8 |
| S12 | The commencement chain | 8, 7, 2 | regulations in force 16.7.2025; amending regulations 4.5.2026; commencement day 16.7.2025; paragraph (2) 16.1.2027; Chapter 6 refused without a regulation under s.46, 16.1.2027 with one from 1.6.2026, 1.3.2027 with one from 1.3.2027; the Second Schedule's experience item is open on 16.7.2028 and closed on 17.7.2028 (item 1 takes over) | ss.63(a), 63(b), Second Schedule A2 |
| S13 | The fees by vintage and by head of s.59 | 8, 7 | as made on 1.12.2025: practical exam 194, licence 284, temporary application 398, objection to a practical score 40, silent on five services; as amended on 5.5.2026 with readings: 196, 288, 403, theoretical exam 158, objection to a practical score silent; nine services under six heads | regulations 2 to 5, s.59 |
| S14 | Advertising as a grade 3 licensee with only grade 1 | 1, 6, 7 | item (3): 5,100; with a violation that continued three months, 5,406 | s.4, ss.45(a), 47(b) |
| S15 | A 70 kW and a 70.01 kW system | 1, 2, 3, 6 | kinds covering 70 kW: grades 2, 3; 70.01: grade 3; a foreign expert qualifies for 70.01 and not 70; an operator may engage a grade 2 holder for 70 and not for 70.01; the worker commits item (2) (10,200) | ss.2, 9(a)(1), 18(a) |
| S16 | Suspension until final judgment | 1, 4, 2, 6 | the Registrar may suspend; the licence is not in force from 1.3.2028 with no end; item (1) for work on 1.3.2028; with a judgment on 10.6.2029 it is in force again on 11.6.2029 | s.10(b) |
| S17 | The licensee as a service electrician | 7, 1, 2 | treated as one under s.58 and may do the electrical work of the integral system under s.61 with a licence in force; neither with a lapsed licence; neither for electrical work outside the integral system | ss.58, 61, First Schedule A.1(12) |
| S18 | An exemption order | 1, 4, 7 | the Minister may exempt after a valid consultation (function (1)) and satisfaction; a subcommittee cannot give the advice; work in an exempted class: "does not apply: exempted"; before the Law has commenced for the system the first reason is that it has not | s.3(b), s.26 |
| S19 | A condition for the grant ceased to hold | 2, 1, 4 | with the Registrar of the opinion that the offence disqualifies, ground (2) is made out and the Registrar may revoke; otherwise no ground | ss.6(a)(3), 10(a)(2) |
| S20 | A licensee applies to renew a grade 1 licence on 1.10.2026 | 2, 8, 7 | can be renewed when s.6(a)(1) to (3) hold (the training of (4) is not asked again) and the fee of regulation 2(c), updated, is paid: 288 yes, 284 no; a conviction the Registrar finds disqualifying defeats it (and fails with the fee paid), and holds once he finds it does not disqualify; an application before the commencement day: a named refusal | ss.8, 6(a)(1) to (3), regulations 3(a) and 4 |
| S21 | Noa, with no licence, works on a 10 kW R134a system on 1.4.2030; the Commissioner's complete notice of intention is delivered 15.6.2030; she stays silent | 1, 6, 7 | sanction 20,400; representations until 15.7.2030 inclusive (an act on the day of delivery, 15.6, is timely; 16.7 is late); the notice is treated as a payment demand delivered 15.7.2030; payment until 14.8.2030 (15.8 is late); the decision counts as delivered 15.7.2030 and the appeal runs to 29.8.2030 (30.8 is late) | ss.41, 43, 44(d), 47(b), 48, 56(a), Third Schedule (1), IL s.10(a) |
| S22 | An applicant who holds the Training Division certificate of grade 2 applies for a grade 2 licence on 1.12.2025 | 2, 1 | Part B item 1 is the only item that applies and nothing further is asked (group 2 fork FS10); the literal reading, which would add the ungraded certificate row, is group 2's callable alternative | s.6(a)(4), Second Schedule Part B |
| E1 | Unlicensed work on a 10 kW R134a system on 15.1.2027 and on 16.1.2027; a corporation that works with no licence at all | 1, 6, 7 | on 15.1.2027 the Law has not commenced for the system (18 months after 16.7.2025 is 16.1.2027); on 16.1.2027 the work is forbidden, item (1); for a corporation the violation is found and its sanction is a refusal (the dash in the corporation column) | s.63(a)(2), Third Schedule (1) |
| S23 | The owner's ruling on day X, default reading (16.7.2025): the Schedule route and the s.63(a)(1) and (2) regimes | 7, 8, 2 | day X 16.7.2025; paragraph (2) from 16.1.2027; the experience item of the Second Schedule is open on 16.7.2028 and closed on 17.7.2028 and 16.10.2028 (item 1 takes over); an R134a system is reached on 16.1.2027 and not on 15.1.2027; lawful propane on 16.7.2025 and not on 15.7.2025 | s.63(a)(1), (2), Second Schedule A2 |
| S24 | The same on the documented alternative (16.10.2025) | 7, 8, 2 | day X 16.10.2025; paragraph (2) from 16.4.2027; the experience item is open on 16.7.2028, 17.7.2028 and 16.10.2028 and closed on 17.10.2028; an R134a system is reached on 16.4.2027 and not on 16.1.2027 or 15.4.2027; propane on 16.10.2025 and not on 16.7.2025 or 15.10.2025; the Fees Regulations still in force from 16.7.2025 | s.63(a)(1), (2), Second Schedule A2 |
| S25 | Both readings of day X on the same applicant and the same days | 7, 2 | the experience item of the Second Schedule: closed on 17.7.2028 and 16.10.2028 by the default, open on both by the alternative; closed on 17.10.2028 on both. An R134a system: reached on 16.1.2027 and 15.4.2027 by the default only; reached on 16.4.2027 on both | s.63(a)(1), (2), Second Schedule A2 |

**One expectation of mine was wrong.**
I had written that item 1 of the Second Schedule's Part A is present on both 16.7.2028 and 17.7.2028 for an applicant with a year of experience; I had misread group 2's fork FS2.
Item 1 is the Part's default item (it applies where no other open item fits), so with the experience item open it is absent, and on 17.7.2028 the applicant falls back to it; group 2's own answer table says "item A2 / item A1".
The first run failed that one assertion; I corrected the expectation to group 2's recorded reading and noted the correction in `expectations.md`.
A second test error: an assertion on a day after 1.1.2026 used the printed fee of 284; the fee on that day is the updated 288 and needs the index readings.
Both were errors of the integration tests, not of any group module.

## Independent tests

### Who wrote them, and how

Three independent test authors (Opus 5.5) wrote the files with the prefixes `ind-a-`, `ind-b-` and `ind-c-`, and the three documents `INDEPENDENT-ind-a-expectations.md`, `INDEPENDENT-ind-b-expectations.md` and `INDEPENDENT-ind-c-expectations.md`, which are in this directory.
Each author decided the expected answer to every scenario from the sources (the Law, the gazette, the Fees Regulations, the Interpretation Law notes) before opening any group module, any FRAGMENT or the plan; the expectations documents record the scenarios as decided, and ind-a's states the time and the files it had not opened.
They then ran the scenarios against the encoding and kept every assertion that disagreed with it, unedited, in an `-tests-disagree` or `-tests-ambiguous` file.
The fleet lead copied the files into the deposit after the integrator's own tests were written, and reports that the three authors' transcripts were audited: each wrote its expectations before opening any module.
The integrator did not read the authors' work directories or transcripts; it read the expectations documents and the headers of the test files only to describe them here, and runs the test files with `check.sh`.

| author | scope | scenarios decided before opening the encoding | test files |
| --- | --- | --- | --- |
| ind-a | ss.1 to 18, the First and Second Schedules, and the commencement day as those sections use it | 218 (3 gazette dates, 8 on commencement, 207 on ss.2 to 18 and the Schedules; the author's own corrected count) | 10 |
| ind-b | ss.19 to 40 (the Registrar, the Council, inspection), ss.58 to 63 and the Fourth Schedule | 347 (99 of them on the Fourth Schedule) | 5 |
| ind-c | Chapter 6 (ss.41 to 57) with the Third Schedule, s.63(b), the Fees Regulations in three vintages, and the SimpLEX test table | 154 | 12 |

Scenarios written after the author had opened the encoding are not among those counts and are labelled as probes: ind-b's second disagreement (D2), ind-c's DIS-2 to DIS-5, and ind-c's both-readings checks of X3, X6 and X9.
The authors' documents are theirs and are not edited here; where one calls the bill PDF "the bill as tabled" (ind-c, X13), read it as the committee's text for the second and third readings, 11 December 2024.

### What the independent tests found in the row as it stands

| file | satisfied | failed | refused | warnings | expected to fail | expected to refuse |
| --- | --- | --- | --- | --- | --- | --- |
| `ind-a-tests-ambiguous.l4` | 0 | 2 | 0 | 0 | 2 | 0 |
| `ind-a-tests-commencement.l4` | 9 | 0 | 0 | 0 | 0 | 0 |
| `ind-a-tests-disagree.l4` | 6 | 0 | 0 | 0 | 0 | 0 |
| `ind-a-tests-duties.l4` | 16 | 0 | 0 | 0 | 0 | 0 |
| `ind-a-tests-fixtures.l4` | 1 | 0 | 0 | 0 | 0 | 0 |
| `ind-a-tests-s10-s11.l4` | 38 | 0 | 0 | 0 | 0 | 0 |
| `ind-a-tests-s12-s18.l4` | 50 | 0 | 0 | 0 | 0 | 0 |
| `ind-a-tests-s2-s4.l4` | 66 | 0 | 0 | 0 | 0 | 0 |
| `ind-a-tests-s5-s9.l4` | 52 | 0 | 0 | 0 | 0 | 0 |
| `ind-a-tests-sch2.l4` | 70 | 0 | 0 | 0 | 0 | 0 |
| **ind-a, 10 files** | **308** | **2** | **0** | **0** | **2** | **0** |
| `ind-b-tests-ambiguous.l4` | 0 | 16 | 2 | 2 | 16 | 2 |
| `ind-b-tests-disagree.l4` | 2 | 0 | 0 | 0 | 0 | 0 |
| `ind-b-tests-g4.l4` | 127 | 0 | 0 | 0 | 0 | 0 |
| `ind-b-tests-g5.l4` | 99 | 0 | 0 | 0 | 0 | 0 |
| `ind-b-tests-g7.l4` | 271 | 0 | 0 | 0 | 0 | 0 |
| **ind-b, 5 files** | **499** | **16** | **2** | **2** | **16** | **2** |
| `ind-c-tests-ambiguous.l4` | 0 | 2 | 10 | 10 | 2 | 10 |
| `ind-c-tests-amount.l4` | 51 | 0 | 0 | 0 | 0 | 0 |
| `ind-c-tests-appeal.l4` | 33 | 0 | 0 | 0 | 0 | 0 |
| `ind-c-tests-commencement.l4` | 11 | 0 | 0 | 0 | 0 | 0 |
| `ind-c-tests-disagree.l4` | 11 | 0 | 3 | 3 | 0 | 3 |
| `ind-c-tests-fees.l4` | 68 | 0 | 0 | 0 | 0 | 0 |
| `ind-c-tests-powers.l4` | 15 | 0 | 0 | 0 | 0 | 0 |
| `ind-c-tests-procedure.l4` | 36 | 0 | 0 | 0 | 0 | 0 |
| `ind-c-tests-routes.l4` | 11 | 0 | 0 | 0 | 0 | 0 |
| `ind-c-tests-schedule.l4` | 48 | 0 | 0 | 0 | 0 | 0 |
| `ind-c-tests-simplex.l4` | 34 | 0 | 0 | 0 | 0 | 0 |
| `ind-c-tests-warning.l4` | 21 | 0 | 0 | 0 | 0 | 0 |
| **ind-c, 12 files** | **339** | **2** | **13** | **13** | **2** | **13** |
| **all independent files** | **1146** | **20** | **15** | **15** | **20** | **15** |

Every file passes except the five that state a reading the encoding did not take, or a refusal the encoding returns; `check.sh` expects those five at their stated counts (the `expected_failed` and `expected_refused` tables), and reports RED if any count moves in either direction.
The files `ind-a-tests-disagree.l4` and `ind-b-tests-disagree.l4` and the repaired parts of `ind-c-tests-disagree.l4` failed before the groups' repairs and now pass; the headers and section titles in those files still say "meant to fail" and "(5 fail)", because they were written before the repairs, and are left as the authors wrote them.
They are now regression tests.

### Disagreements: the encoding was wrong, and was repaired

Each was found by an independent author, checked by the fleet lead, and repaired by the group before this integration run; no exported name or signature changed.

| id | what the author expected | what the encoding did | disposition |
| --- | --- | --- | --- |
| ind-a D1 (SCH2-A1a, B1a, C1) | an applicant who completed item 1's course holds the certificate of the grade sought and has met item 1, with nothing further | the graded certificate was classified under the ungraded row of the Part (A3, B5(1), C6), which asked for 50, 50 or 200 hours more | G2 repaired it (fork FS10): item 1 comes back alone, with "the certificate itself" added to its column B; the literal reading stays callable. Regression: `ind-a-tests-disagree.l4` (6 assertions). Integration: S22 |
| ind-b D1 (I30-2) | `s 30(b) — the candidate may be authorised as an inspector` is FALSE for a person who is not a Ministry employee | TRUE, because the decision never read the employee field | G5 repaired it: a new decision `s 30(a) — the candidate is an employee of the Ministry` is a limb of the s.30(b) decision and guards its SHANT. Regression: `ind-b-tests-disagree.l4` |
| ind-b D2 (after opening) | a designation preceded by U+200F is recognised by the tolerant reading of the Fourth Schedule | the second REPLACE carried the unsubstituted placeholder `{{MARK2}}` | G7 repaired it and made its build refuse any unsubstituted placeholder. Regression: `ind-b-tests-disagree.l4` |
| ind-c DIS-2 | an act on the day a notice, demand, warning or decision is delivered is "within N days from" it | the day of delivery was counted late at s.43, s.48, s.53(a) and s.56(a), so a violator who argued on the day of delivery was deemed to have stayed silent (s.44(d)) | G6 repaired it (fork F-ACTDAY). Regression: `ind-c-tests-disagree.l4` (5 assertions). Integration: S21 and Q3 |
| ind-c DIS-3 | an "extension" that ends before the 30 days are out is not an extension; the 30 days stand | the official's day was taken whatever it was | G6 repaired it (fork F-SHORTEN). Regression: 2 assertions |
| ind-c DIS-4 | regulation 4 bars the grant of a foreign expert's temporary licence when the application fee (regulation 2(d)) is unpaid, in both vintages | asked about the application it barred; asked about the grant it found no fee | G8 repaired it (fork F13): the fee fixed for the application binds the grant, whichever service is asked about. Regression: 3 assertions. Integration: S04 |
| ind-c DIS-5 | on the encoding's own reading that a notice omitting what s.42(b) requires is no notice (fork F-NOTICE), s.44 deems no payment demand | s.43 gave such a notice no right, yet s.44 deemed it a payment demand | G6 repaired it: `s 44` gives NOTHING for such a notice. Regression: 1 assertion. See the note on `s 56(a)` under "Defects found" |

### Disagreement kept: fork F-DASH

| id | what the author expected | what the encoding does | disposition |
| --- | --- | --- | --- |
| ind-c DIS-1 (decided before; A1, A2, A4) | a corporation at a dash in the corporation column of Third Schedule items (1), (2) and (4) may not be sanctioned, because column B sets no amount to impose (s.41(a)) | the sanction is a named refusal: the dash may mean no sanction or a figure left out | left as the group's fork F-DASH, which is "assumed, not ruled"; open question O34. `ind-c-tests-disagree.l4` holds the author's reading: its 3 assertions refuse by design |

### Ambiguities: the author's reading is not the one taken

In each, the author judged that the source allows both readings; the encoder registered a fork, took the other reading, and (where the table says so) kept the author's reading as a callable alternative.
The assertions in the ambiguous files state the author's reading and fail or refuse against the reading taken; the open question that would settle it is listed.

| file and section | the author's reading (asserted) | the encoding's reading (fork) | outcome | open question |
| --- | --- | --- | --- | --- |
| `ind-a-tests-ambiguous`, A1 (SCH2-B1b) | a Ministry of Education 5-unit certificate meets Part B item 1(2) with nothing further | item 5(3) governs, up to 50 hours (G2 FS2; contradiction K2); the author's reading is G2's callable FS2b, tested in `g2-tests-second-schedule.l4` | 1 fails | O5 |
| `ind-a-tests-ambiguous`, A2 (S10-12) | the day a suspension begins counts as its first day, so a suspension from 1.5.2026 to 1.5.2029 exceeds three years | the beginning day is the event and is not counted (G1 F18); the callable alternative counts it, tested in `g1-tests-adverse.l4` | 1 fails | O12 |
| `ind-b-tests-ambiguous`, A1 (K63-1 to K63-20) | s.63(a)(1): the three months run from the later of the two days (day X 16.10.2025) | the later of the two dates (day X 16.7.2025) (G7 F-C-3) | 15 fail | O38; ruled by the owner for the default, see "Day X: the default and the 16 October alternative"; the author's reading is callable and is run in S24 and S25 |
| `ind-b-tests-ambiguous`, A2 (K63-11) | with no regulation under s.46 Chapter 6 has not commenced (FALSE) | a named refusal (G7 F-C-8); FALSE is the callable alternative | 1 refuses | O39 |
| `ind-b-tests-ambiguous`, A3 (C27-4) | a supported-body employee who is not employed by the body he represents is not entitled to the travel refund (FALSE) | the section is silent about him, so the encoding refuses (G4 G-27, a gap between s.27(a) and (b)) | 1 refuses | O24 |
| `ind-b-tests-ambiguous`, A4 (I36-8) | the power in s.36(d) to change conditions reaches work procedures after a hearing | it reaches modes of action only (G5 F-CHANGE reading A); the author's reading B is callable and passes in `ind-b-tests-g5.l4` | 1 fails | O31 |
| `ind-c-tests-ambiguous`, AMB-1 (H5, H8) | the draft's 284 is the licence fee under s.5, and the draft prices no separate application fee | two heads of s.59: the draft prices the application and is silent on the licence (G8 contradiction 2, K88) | 2 fail | O43 |
| `ind-c-tests-ambiguous`, AMB-2 (I8) | the SimpLEX panel's own statement ("prohibits registration without payment") is the draft's regulation 4 | the draft's regulation 4 is not visible, so a named refusal (G8 F16); the callable alternative takes it as regulation 4 as made, tested in `g8-tests-simplex.l4` | 2 refuse | O44 |
| `ind-c-tests-ambiguous`, AMB-3 (J5 to J9) | the SimpLEX table, run against the draft it was written for, gives the outcomes the table prints | the same refusal, because the draft's regulation 4 is invisible (G8 F15 to F17) | 8 refuse | O44 |

### The five deliberate files

- `ind-a-tests-ambiguous.l4` fails exactly 2 assertions, one for A1 and one for A2: each asserts the author's reading, which the encoding did not take.
- `ind-b-tests-ambiguous.l4` fails 16 (15 for A1 and 1 for A4) and refuses 2 (A2 and A3): the failures assert the author's reading, and the refusals are the refusals the encoding returns, asserted against an expected FALSE.
- `ind-c-tests-ambiguous.l4` fails 2 (AMB-1) and refuses 10 (AMB-2 and AMB-3): the same.
- `ind-c-tests-disagree.l4` passes 11 (the four repaired disagreements DIS-2 to DIS-5) and refuses 3 (DIS-1, the dash, left by the group as its fork F-DASH).
- `ind-a-tests-disagree.l4` (6) and `ind-b-tests-disagree.l4` (2) pass entirely, as regression tests, so they are not among the deliberate files in the sense of `check.sh`; they are listed because they were failing files before the repairs.

A refused assertion is also reported as a warning, so `check.sh` now has an `expected_refused` count beside `expected_failed`.
A module is red if its refusals or its warnings differ from `expected_refused`; any other refusal or warning still makes the run red.

### What the integration did with them

The integrator wrote no assertion of the independent authors and changed none.
The repairs reached the integration tests where the integration had a scenario of its own: S22 (the graded certificate), S21 and Q3 (the day of delivery), S04 (the grant of a temporary licence), and S23 to S25 (day X, from the owner's ruling).
The open questions above are in the consolidated list, so a domain expert who answers one of them settles the corresponding file.

## The register of source contradictions, consolidated

Each entry appears once, with the provisions, the case that discriminates, the groups that found it and where it is recorded (group, entry id or fork id).
"T" ids are the PLAN's first-read traps.
A contradiction is two provisions (or two limbs) that answer one question differently; a gap is a place where the text is silent; an asymmetry is a difference the text does not explain.
The kind is in the second column.
Every contradiction has the reading taken and the other reading callable in the group that found it; the integration adds none of its own.

### The Schedules

| id | kind | provisions | discriminating case | found by | recorded as |
| --- | --- | --- | --- | --- | --- |
| K1 | contradiction | Second Schedule Part B items 3(2) and 5(1); Part C items 3(2), 4(2) and 6: the same Training Division certificate named by grade and named with no grade, with different hours | a grade 1 certificate seeking grade 2 (100 hours or 50), seeking grade 3 (290 or 200); a grade 2 certificate seeking grade 3 (240 or 200) | G2 | T1; G2 FS1, C2 |
| K2 | contradiction | Part B item 1(2) and item 5(3): a 5-unit climate-control certificate is enough with nothing more, and up to 50 hours | a person with only that certificate seeking grade 2 | G2 | T2; G2 FS2, C1 |
| K3 | contradiction | item 1 of Parts A and B is headed "no prior training or experience" yet offers a certificate | a 3-unit certificate seeking grade 1 | G2 | T2; G2 FS2, C3 |
| K4 | contradiction | Part B items 2 and 6, Part C items 2 and 7: registration alone, and registration with the completed programme, with different requirements | a technician who completed the programme | G2 | T3; G2 FS3, C4 |
| K5 | contradiction | the Schedule against s.6(a)(4)(a) and (b): a holder of a final certificate meets (4), yet the Schedule asks the holder of the certificate its own course confers for up to 50, 50 or 200 hours more; registration is a route to a licence of any grade, yet Parts A to C have no item for some registered applicants | the applicant who completed the 720 hours of C1 and holds the grade 3 certificate; a technician with the programme seeking grade 1 | G2 | G2 C5, C6, FC2, FC7 |
| K6 | ambiguity | "training of up to N hours" in every row: a ceiling on the course or the required count | any row with hours | G2 | T6; G2 FS5 |
| K7 | contradiction | the three-year note on A2, B4, C5 runs from the commencement "as stated in s.63(a)(1)", which is the commencement for listed flammable refrigerants only; paragraph (2) systems start 18 months later | an experienced applicant applying on 1.1.2029 for work on an ordinary-refrigerant system | G2, G7 | T7; G2 FS8, C7; G7 contradiction 10 |
| K8 | asymmetry | Part C has no certificate option and no 5-unit route to grade 3 | a 5-unit certificate seeking grade 3 | G2 | G2 C17 |
| K9 | gap | column B's heading: Part B says "training or complementary studies required", Parts A and C say "requirements for the licence sought" | none: both readings return the same column B | G2 | T5; G2 FS4, C13 |
| K10 | source defect | Part C item 4: the Wikisource text puts the hours in column A behind a stray bracket; the gazette (p.204) puts them in column B; A3's column B stops a word short of the gazette's | the gazette governs | G2 | T4; G2 FS6, C14, C15 |
| K11 | source defect | Fourth Schedule item (66): `170E` in the wiki, `E170` in the gazette (p.207, page image); items (69) and (71) carry an invisible direction mark in the wiki and in the gazette's text layer | the gazette governs; marks stripped | G7 | T23; G7 F-S4-1, contradiction 9 |
| K12 | contradiction | First Schedule A.1(5) (oil on installation, grade 1) against B.3(3) (oil in maintenance, grade 3 only) | a grade 1 licensee adds oil while installing, and on a service visit | G1 | T8; G1 F3, C1 |
| K13 | contradiction | B.1(3) (components, grade 1) against B.3(2) (the refrigerant system and its components, grade 3 only) | a grade 1 licensee replaces a compressor | G1 | T9; G1 F4, C2 |
| K14 | overlap | A.1(6) (control components) against A.1(11) (integral control and monitoring accessories only) | a control accessory that is not integral | G1 | G1 C3 |
| K15 | gap | measuring energy consumption is excluded from three items and listed in none | measuring energy consumption, against measuring currents and voltages (B.1(2)) | G1 | G1 C8 |
| K16 | spelling | the defined term "integral electrical system" is spelled with one letter, items A12 and B14 with another (the gazette prints the extra letter too) | a lookup by string finds nothing | G1 | T10; G1 F5 |
| K17 | wording | "work" in s.3(a) and "an act" in Third Schedule item (2) are different Hebrew words | none: taken as the same | G1 | G1 C9 |

### Licensing, validity, adverse action

| id | kind | provisions | discriminating case | found by | recorded as |
| --- | --- | --- | --- | --- | --- |
| K18 | contradiction | s.8, "31 March of the fifth year from the year of grant": year + 4 makes "whichever is earlier" idle, year + 5 does not | grants of 1.2.2026 and 1.6.2026 | G2 | T24; G2 FV1, C8 |
| K19 | contradiction | s.8 (31 March) against s.17(c) (an extension of up to three months) | a licence ending 31.3.2030 extended to 30.6.2030 | G2, G3 | T25; G2 FV7, C9; G3 S17-M, C1 |
| K20 | contradiction | s.6(a) "shall grant", s.8 renewal, s.10(a) "may refuse to renew" | an applicant who meets s.6(a)(1) to (3) and against whom a ground of s.10(a) applies | G1, G2 | T26; G2 FR1, C10 |
| K21 | contradiction | s.8 (renews on the conditions of s.6 except (a)(4)) against ground (2) of s.10(a) (a condition under s.6 or 9 ceased, no exception) | a licensee struck off the register of technicians applying to renew | G1 | G1 F20, C4 |
| K22 | contradiction | s.6(a) "shall grant" against regulation 4 (the Registrar shall not give a licence for which a fee was fixed unless paid) | an applicant who meets s.6(a)(1) to (4) and has not paid | G2, G8 | G2 FC1, C11 |
| K23 | contradiction | s.9(a) "notwithstanding ss.6 and 8" against s.6(a)(1) to (3) | a minor expert, or one the Registrar finds disqualified | G2 | G2 FT1, C12 |
| K24 | overlap | s.6(b) (the Minister may change the Second Schedule by order) against s.60(1)(a) (regulations on training requirements), both with the committee's approval | an order and a regulation that differ | G2, G7 | G2 C16 |
| K25 | contradiction | s.10(a)(2) with s.6(a)(3) (a pending indictment is the loss of a condition: suspension capped at three years) against s.10(b) (suspension until final judgment, uncapped) | an indictment and a five-year trial | G1 | G1 C5, F17, F21 |
| K26 | gap | s.10(c) second limb names the hearing and not the Council, though (a) requires the Council; the other limbs name the Council | revocation after the cure period without a second consultation | G1 | G1 C6, F22, F23 |
| K27 | contradiction | s.3(a) against s.4 for a higher grade | a grade 3 holder who advertises as a grade 2 licensee | G1 | G1 C7, F13 |
| K28 | gap | s.3(a) forbids work outside "the conditions of his licence and the provisions under this Law"; s.17(d) makes the training duty a condition; the Third Schedule prices only no licence or the wrong kind | a licensee who missed a course required under s.17(b) and keeps working | G1, G3 | T12; G1 F9; G3 C9, S17-d |
| K29 | gap | the passive s.11(b): the register "shall be open to public inspection" names no actor | a query that states no identifying detail | G1 | G1 F29 |

### Duties of licensees and operators

| id | kind | provisions | discriminating case | found by | recorded as |
| --- | --- | --- | --- | --- | --- |
| K30 | contradiction | s.13 (parts 4 and 5 of the Standard "as their wording is from time to time") against Third Schedule item (4) (names the testing chapter and the title of part 4 as enacted) | an installation under a wording that moved the tightness test | G3 | T13; G3 S13a, S13c, C6 |
| K31 | gap | the duties of ss.12, 14, 15, 16, 17 and 18(b) have no Third Schedule row | a breach of any of them | G3 | T13; G3 section 8 |
| K32 | contradiction | s.15's heading (a duty to report) against its body (the express duty is to supply information or documents) | a demand for a report | G3 | G3 S15b, C7 |
| K33 | gap | s.17(a) "the last year of validity" against s.9 (a temporary licence runs for up to a year) | training before a six-month licence began | G3 | G3 S17-W, C8 |
| K34 | contradiction | s.17(b) ("in addition to the trainings under (a)") against s.17(c) and (d) ("(a) or (b)") | eight hours that are a (b) course | G3 | G3 S17-C, C5 |
| K35 | gap | s.17(c) extends the end of validity; a (b) duty can fall due in any year | a course missed in the second year of a five-year licence | G3 | G3 C11 |
| K36 | contradiction | s.17(c) ("a licensee who has not fulfilled his duty") against the time the duty falls due | a decision on the day after the last day of validity | G3 | G3 S17-T, C4 |
| K37 | contradiction | s.18(c) defines "operator" "in this section"; Third Schedule items (5) and (6) use the word | any operator violation | G3 | G3 S18-D, C2 |
| K38 | ambiguity | s.18(c) "regularly" against "including an owner or manager of a business offering the work to the public" | the owner of such a business who engages an unlicensed person once | G3 | G3 S18-C, C3 |
| K39 | contradiction | s.18(a) "a licence of the kind appropriate to that system" against Third Schedule items (5) ("no licence at all") and (6) ("not of the appropriate kind"), and against s.3(a)'s reading of "appropriate" | a lapsed licence (G3); the oil of maintenance on 5 kW (an independent test author and the integrator, row R1) | G3, G1 | G3 S18-H; the register row R1 |
| K40 | contradiction | s.26(b) lets a subcommittee take the Council's powers "under (a)(3)", which lists the extension of validity, against s.17(b)'s advice on a required course (not listed) | advice on a required course given by a subcommittee | G3, G4 | G3 C10; the register row R6 |
| K41 | overlap | s.15 (a report as directed) against s.16 (30 days to notify a change); s.5(b) against s.15 for a licensee who has applied to renew | a change notified on day 20 after a report was directed within 10 days | G3 | G3 C12, open question 17 |

### The Registrar and the Council

| id | kind | provisions | discriminating case | found by | recorded as |
| --- | --- | --- | --- | --- | --- |
| K42 | contradiction | s.21 (barred while charged and no final judgment) against s.23(b)(1) (removed who "was charged", no qualifier) | a member charged and later acquitted | G4 | T29; G4 C-T29, F-23b1 |
| K43 | contradiction | s.24 and s.25(a) ("its members": eleven seats or those serving) against s.25(c) (every member summoned, which can only mean those serving) | eight serving, three vacant, the chair and four present | G4 | G4 C-25, F-base |
| K44 | gap | s.25(a) (quorum) against s.25(c) (may "deliberate" in an incomplete composition): can it decide | three present with the chair, every member summoned, 2 to 1 | G4 | T28; G4 F-T28 |
| K45 | gap | s.25(b): a tie in which the chair casts no vote | 2 to 2, the chair abstaining | G4 | G4 F-25b-tie |
| K46 | contradiction | s.27(a) against s.27(b) (travel refund; payment) | an employee of a private body he represents | G4 | G4 C-27, G-27 |
| K47 | contradiction | s.23(a)(2) (service ends when a seat 4 member ceases to be a ministry employee) against s.23(b)(3) (a condition for appointment ceased: removal) | the same event | G4 | G4 C-23a-b3 |
| K48 | ambiguity | s.20(2) makes the Registrar a member; s.22 excludes the Registrar from the four-year term | the Registrar ceases to be the Registrar | G4 | G4 F-20-2 |
| K49 | ambiguity | s.20 (the eleven seats) against "a council of 11 members": counted, no discrepancy; the chair is the division's representative, not the Registrar | none | G4 | T43 |
| K50 | wording | s.29(a), definition 1 (family member): an unusual word stands beside "(step-)" in the list of relatives | a step-relation | G4 | G4 open question 14 |

### Inspection

| id | kind | provisions | discriminating case | found by | recorded as |
| --- | --- | --- | --- | --- | --- |
| K51 | contradiction | s.33 definitions 2 and 5: an employee authorised only to test is both a tester and an expert | s.34(e) then binds every such tester to give an opinion | G5 | G5 C1, F-OVERLAP |
| K52 | contradiction | s.35(3) (a testing body must have testers) against s.33 definitions 2 and 4 (a tester is an employee of a testing body, which is a corporation that meets s.35) | a corporation that is not yet a testing body | G5 | G5 C2, F-LOOP |
| K53 | contradiction | s.38(c) (no disclosure "except to carry out the act") against the reports of s.34(d), (e) and the hand-over of s.38(b) | the hand-over at the end of an engagement | G5 | G5 C3, F-DISCLOSE |
| K54 | gap | s.34(f) (working rules of the senior inspector) against s.36(d) (conditions in the instrument of authorisation): no priority | an instrument condition and a working rule that conflict | G5 | G5 C4, F-OVERLAP-RULES |
| K55 | contradiction | s.36(d): the power to set covers "modes of action and work procedures"; the power to change only "modes of action", after a hearing | a change to a work-procedures condition | G5 | G5 C5, F-CHANGE |
| K56 | contradiction | ss.30(b)(1), 35(2), 36(b)(1): three standards of fitness (the Minister's opinion; unstated; a pending proceeding only in two) | an indictment pending for a serious offence | G5 | G5 C6, F-OFFENCE, F-PROCEEDING, F-JUDGE |
| K57 | contradiction | s.31(2) covers information or a document; Third Schedule item (7) prices only a document | a person who refuses oral information | G5 | G5 C7 |
| K58 | contradiction | s.31(3) (an inspector's entry) against s.37(a)(1) and (b) (a tester's or expert's entry) | a dwelling, on a court order alone | G5 | T30; G5 C8, C10 |
| K59 | contradiction | ss.34(e), 38(a) and 38(c) bind an expert employed by a testing body differently | an expert employed by an engaged body with no engagement of his own | G5 | G5 C9 |
| K60 | asymmetry | reasons are required for a refusal to authorise (s.36(c)) and not for a revocation (s.39) | a revocation without reasons | G5 | G5 C11 |
| K61 | gap | "family member" and "relative" for a corporation (s.33 def.3 carries s.29(a) over) | a testing body | G5 | G5 C12 |
| K62 | circularity | s.33 definition 7 ("checklist") points at s.37(a)(3), which uses the term | none: the two agree | G5 | G5 C13 |
| K63 | gap | s.36(a) points at regulations under s.60(1)(c) that are not in the sources | any individual's authorisation | G5, G7 | T31; G5 section 8 item 1 and F-DUTY; G7 F-R-2 |

### Chapter 6 and its commencement

| id | kind | provisions | discriminating case | found by | recorded as |
| --- | --- | --- | --- | --- | --- |
| K64 | gap | Third Schedule items (1), (2), (4): the corporation column prints a dash; s.41(a) says "the amount set in column B beside it" | a corporation that works without a licence or installs without the test | G6 | T14; G6 F-DASH |
| K65 | contradiction | s.41(b) (cap of NIS 40,000 / 80,000 on what an order sets) against s.45 (additions) and s.47(b) (indexation) | a corporation, item (5), repeat violation | G6 | T15; G6 F-CAP, contradiction 1 |
| K66 | contradiction | s.42(b)(4) ("authority to add") against s.45 ("shall be added") | a continuing violation the Commissioner would not add to | G6 | G6 F-ADD, contradiction 2 |
| K67 | contradiction | s.44(d) ("the said date") against s.47(a) (the update day for a silent violator is the notice's) | a violator who stays silent | G6 | T16; G6 F-DEEMED, contradiction 3 |
| K68 | contradiction | s.42(b)(2) and s.44(b)(1) (the notice and the demand state the period for payment) against s.48 (30 days from the demand) | a demand that states 45 days | G6 | T16; G6 F-PERIOD, contradiction 4 |
| K69 | contradiction | s.45(b) ("repeat violation" anchored to the previous violation for which a sanction was imposed) against s.54(b) (anchored to the warning's delivery) | a violation 20.2.2029 after a sanctioned violation 10.1.2027 and a warning 3.3.2027 | G6 | T17; G6 F-WINDOW, contradiction 5 |
| K70 | ambiguity | s.45(a) "for each month in which the violation continues": first and part months; the fixed or the updated amount | 15 March to 14 June 2027 | G6 | T18; G6 F-MONTHS, F-START, F-BASE |
| K71 | contradiction | s.54(a) ("shall give") against s.42(a) ("intends to impose") | a Commissioner who does not intend to impose | G6 | G6 F-MUST54, contradiction 6 |
| K72 | contradiction | s.46(b) (the Minister "may" make regulations) against s.63(b) (Chapter 6 commences at the later of 18 months and their entry into force) | no regulation is ever made | G6, G7 | T19; G6 contradiction 7; G7 F-C-8 |
| K73 | gap | s.53(a) has no anchor for its 30 days | the warning's delivery or the breach's day | G6 | G6 F-ANCHOR, contradiction 8 |
| K74 | contradiction | s.56(a) (appeal from a "final decision") against s.44(d) (a silent violator has none) | the day notice of the decision counts as delivered | G6 | G6 F-APPEAL-DEEMED, contradiction 9 |
| K75 | ambiguity | "the amounts fixed under this subchapter" are both what s.47 updates and what s.46(a) forbids going below | a repeat violation priced below the floor | G6 | G6 F-FLOOR, F-BASE, contradiction 10 |
| K76 | asymmetry | s.49 (a late payer owes interest and arrears fees) against s.56(c) (a successful appellant is refunded with interest only) | a refund after a late payment | G6 | T40 |
| K77 | gap | s.56 sends the Commissioner's final decisions to the Magistrates' Court; s.62 adds the Law to the Administrative Courts Law's schedule | a decision of the Registrar or the Minister | G6, G7 | T39; G7 F-A-1, contradiction 3 |
| K78 | gap | ss.41(b), 46(b), 49, 51, 57(d): instruments and rates not in the sources | any sanction that needs them | G6 | G6 section 8 |

### Commencement, regulations and electrical work

| id | kind | provisions | discriminating case | found by | recorded as |
| --- | --- | --- | --- | --- | --- |
| K79 | gap | s.63(a) fixes a commencement only for work on a system; nothing for the Registrar, the Council, inspection, applications or the regulation powers | the Registrar's duty to grant, on any day | G7 (and every group that gates or does not gate) | T20; G7 F-C-7; the register row R4 |
| K80 | ambiguity | s.63(a)(1) and (2) for a system with refrigerants of both kinds; a listed refrigerant whose use is not permitted; a Fourth Schedule amended between two dates | lawful propane with R134a on 16.7.2025 | G7 | T21; G7 F-C-6a, F-C-6b, F-C-9 |
| K81 | ambiguity | s.63(a)(1): "three months from its publication or the entry into force of the regulations, whichever is later" as the later of two dates or three months from the later day | 16.7.2025 or 16.10.2025 | G7, G8 | G7 F-C-3, contradiction 5; G8 contradiction 12 (RULED 2026-10-14: default, day X 16.7.2025; see Owner rulings) |
| K82 | ambiguity | "its publication": the gazette's 14.1.2025 or the Knesset's 8.1.2025 | none on the real facts | G7 | T22; G7 F-C-2 |
| K83 | circularity | s.63(a)(1) defines the commencement day by the s.59 regulations, which s.59 lets the Minister make | the power must be usable before the commencement day | G7 | G7 contradiction 8, F-R-3 |
| K84 | contradiction | s.58 (a licensee is a service electrician for cooling systems) against s.61 (electrical work "in accordance with the First Schedule") | electrical work outside the integral electrical system | G7 | T32; G7 F-E-1, contradiction 2; the register row R11 |
| K85 | contradiction | s.60(1) (a general power) against s.60(2) (two matters, no approval) | regulations on the manner of applying, made without the committee's approval | G7 | G7 F-R-2, contradiction 4 |
| K86 | ambiguity | s.59: how many heads of fee (five, six or nine services) | the temporary licence's grant | G7, G8 | T38; G7 F-R-1; the register row R10 |

### The Fees Regulations and the SimpLEX draft

| id | kind | provisions | discriminating case | found by | recorded as |
| --- | --- | --- | --- | --- | --- |
| K87 | gap | s.2 "final certificate" (an exam with a theoretical and a practical part) and s.59 against regulations 1 and 2 as made (only the practical exam is defined and priced) | a theoretical exam, unpaid, as made | G8 | T34; G8 contradiction 1, F12 |
| K88 | ambiguity | regulation 2(c) as made prices "receiving" a licence under s.5, which is the section on applying; the draft priced the application | an application that is refused | G8 | G8 contradiction 2 |
| K89 | contradiction | regulation 4 ("a licence for which a fee was fixed") against regulation 2(d) (the fee is fixed for the application) and s.59 (the grant is priced separately) | a foreign expert whose application fee is unpaid | G8 | G8 contradiction 3, F13 |
| K90 | ambiguity | regulation 2(b) says "an amount" where (a), (c), (d) say "a fee"; regulation 3(a) updates "the amounts of the fees" | the NIS 40 on 1.1.2026 | G8 | T36; G8 F10, contradiction 4 |
| K91 | ambiguity | the consolidated text states 158 "(adjusted to 2026)" and the others "(adjusted to 2025)" after 1.1.2026 while regulation 3(a) updates on every 1 January | a practical exam on 4.5.2026 | G8 | T36; G8 F4, F8, contradiction 5 |
| K92 | ambiguity | the draft's regulation 2(c) adds NIS 40 "to the payment of the fee in (a)", where (a) is the theoretical fee, for an appeal on either exam | a practical-exam appeal in the draft | G8 | T33; G8 F2, contradiction 6 |
| K93 | source defect | the draft cites "section 8" for the temporary licence (the enacted section is 9), prints "section 139" of the Budget Principles Law (enacted 39B), and the worked example cites "Law s.9(a): requires passing an exam", which no enacted section says | the worked example | G8 | T35; G8 contradiction 7 |
| K94 | ambiguity | the test table's rows 8 and the worked example give two outcome words for one effect of regulation 4; its references to regulations 2(a), 2(b), 2(c) match the draft's numbering only | the table run against the as-made text | G8 | T34; G8 contradictions 8, 9 |
| K95 | gap | regulation 4 names "the applicant for the licence or the service" as payer; regulation 2 names three payers | an objector | G8 | G8 contradiction 10 |
| K96 | source defect | regulation 1's heading is singular, exact for one definition and not after the amendment adds a second; the wiki marks it | none | G8 | G8 contradiction 11 |
| K97 | ambiguity | the base index of the first update day: published in June 2025 (the May index) or relating to June | 1.1.2026 | G8 | T37; G8 F5 |

## Open questions for a domain expert, consolidated

These are the questions the eight groups put, merged where two groups asked the same, plus the ones the integration raised.
The group and the number of the original question follow in brackets.
Each is answered by an assumed reading in the encoding; none is ruled, except the first question of O38 (day X), on which the owner has ruled for the default.
A domain expert who answers one can revert that one reading alone, because each reading is a callable function with a test.

### Licensing and the Schedules

- **O1.** Do the limits of s.2 (grade 1 up to 18 kW, grade 2 up to 70 kW) include the limit? [G1 1] The encoding takes them inside, which s.9(a)(1)'s "over 70 kW" supports.
- **O2.** Is a licence that has lapsed, been revoked or been suspended "no licence at all" or "a licence not of the appropriate kind" for Third Schedule items (1) and (2), (5) and (6)? [G1 2, G3 4] The difference is NIS 10,000 for an individual under items (1) and (2). Taken: no licence at all.
- **O3.** Can one act be work under two First Schedule items (A.1(6) and A.1(11); B.1(3) and B.3(2)), and which kind does the Schedule then allow? [G1 3] Where does "work" end: is measuring energy consumption licensed, and is a first service after commissioning installation or maintenance? [G1 4]
- **O4.** Is "a licence of the kind appropriate" in s.18(a) and items (5), (6) the same as in s.3(a) (capacity and column A), or the capacity alone? [integration, row R1] Taken: the same; the lead's finding P1.
- **O5.** Is item 1 of each Part of the Second Schedule the default item, or does it apply only to an applicant with no prior training or experience at all? [G2 1] Is the 5-unit certificate of B1(2) a direct route to grade 2, or is it B5(3)'s up to 50 hours? [G2 2] Does a Division certificate of the grade sought satisfy the Schedule with nothing further? [G2 3] Does "in accordance with the Second Schedule" add a condition to s.6(a)(4)(a) and (b), or is it the content of limb (c)? [G2 4]
- **O6.** How is "a year of cumulative experience" counted: 365 days, twelve months, or the days worked? Do overlapping periods count once? Does work on the application day count? [G2 5]
- **O7.** Does the three-year note on the experience items run from the commencement day of s.63(a)(1) for every refrigerant, or from the later commencement that applies to the system? Is it tested on the application day or the decision day? [G2 6, G7]
- **O8.** Does a youth vocational school certificate satisfy s.2's "final certificate"? [G2 11] Does a licence that has lapsed, been revoked or been suspended still count as "a grade 1 licence" in column A? [G2 12] Which prevails where an order under s.6(b) and regulations under s.60(1)(a) both set training requirements? [G2 13] Does an exemption under s.7 change the hours, and can it be given where no training is asked? [G2 14]
- **O9.** Which year is "the fifth year from the year in which the licence was granted"? Does a renewal count a further validity period from the renewal day or from the end of the previous one? Can a renewal be made after a licence has lapsed? [G2 7] Can an extension under s.17(c) pass 31 March of the fifth year, and may the Registrar extend more than once? [G2 8, G3 1]
- **O10.** Does s.9(a)'s "notwithstanding ss.6 and 8" displace s.6(a)(1) and (3) for a foreign expert? [G2 9] Is the fee a condition of the Registrar's duty under s.6(a), and is s.8's renewal a duty or an eligibility test? [G2 10]

### Adverse action, register, advertising

- **O11.** Do the duties or conditions an exemption order fixes under s.3(b) condition the exemption? Does an exemption lift only s.3(a), or also the operator's duty of s.18(a)? [G1 5]
- **O12.** Does the three-year cap of s.10(a) reach a restriction, and does the day a suspension begins count as its first day? [G1 6] Is the loss of the s.6(a)(4) condition a ground for refusing a renewal? [G1 7]
- **O13.** Does the second limb of s.10(c) need a fresh consultation of the Council, the first limb a hearing, and the power to add conditions under s.10(d) the Council? [G1 8, 9] Which grounds of s.10(a) are "defects" that can be cured? [G1 10] When does a revocation take effect? [G1 11, G2 12]
- **O14.** Which limb of s.63(a) governs an advertisement under s.4, and do the Registrar's own chapters (ss.5, 10, 11) commence with the first limb or the second? [G1 12] Which period units does the Registrar use when he fixes a cure period or a bar? [G1 13] Is the Registrar's duty to publish how to apply, and to keep the register, meant to carry a period? [G1 14]

### Duties of licensees and operators

- **O15.** Is s.18(b) a duty of conduct or of result? [G3 2] Is the owner of a business offering the work to the public an operator even if he engages nobody regularly, and does the s.18(c) definition govern items (5) and (6)? [G3 3]
- **O16.** Which wording of Israeli Standard 994 governs, and what does item (4) mean when the Standard is amended? [G3 5]
- **O17.** Does an extension move the window of the last year, and do hours attended during an extension count? Does a course required under s.17(b) count towards the eight hours? Does the duty to meet "the requirements" reach every session or only those counted? Is a licensee excused when no qualifying training was available? Is reasonable notice of a (b) course a condition of the duty? [G3 6 to 10]
- **O18.** Does s.17 apply to a temporary licence of a foreign expert, and how is the last year counted for a term shorter than a year? [G3 11, and the one-day difference found by the integration, row R2]
- **O19.** When do ss.12, 15, 16 and 17 commence for a person who is a licensee? [G3 12] Does the Registrar's duty to grant under s.6 have a commencement of its own, and does it wait for the first commencement day? [integration, row R4]
- **O20.** Does a duty to report in s.15 reach a report? Is the day of notice under s.16 the day of dispatch or of receipt? [G3 13, 14] Under s.26(b), may a subcommittee give the Council's advice on a required course under s.17(b)? [G3 15, row R6]
- **O21.** A licensee who breached the training condition under s.17(b) and keeps working: what follows under s.3(a), given that the Third Schedule has no row? Is the deemed condition of (a) breached only when its window has closed? [G3 16] Does s.5(b) or s.15 govern a licensee who has applied for renewal? [G3 17]

### The Registrar and the Council

- **O22.** Is "its members" in ss.24 and 25(a) the eleven seats or the members serving? Which is the Ministry's practice? [G4 1] May the Council decide at a meeting held under s.25(c)? [G4 2] What follows from a tie in which the chair casts no vote? [G4 3]
- **O23.** Should a member charged and later acquitted be removed under s.23(b)(1)? [G4 4] Is the Registrar's membership ex officio and does it end when the office does? [G4 5] Which year and which meetings count in s.23(c)? [G4 8]
- **O24.** s.27: does a private-body employee who represents his employer get the travel refund, and what is a supported-body employee's position? [G4 6] Does a subcommittee's delegated advice satisfy a "consultation with the Council" for functions other than s.26(a)(3), and what procedure has the Council fixed? [G4 7]
- **O25.** Is each further term under s.22 four years, and is the number of further terms unlimited? Is IL s.10(c) meant to move the end of a term? [G4 9, 10] Must valid advice precede a recognition under s.19(c)(1)? [G4 11] Does the Registrar's consent under s.19(b) reach the Ministry of Education's programmes? [G4 12] Who publishes notice of the Registrar's appointment, and is publication a condition? [G4 13]
- **O26.** How is seat 7 filled before any licence has been granted? Does Chapter 4 have a commencement of its own? Whose judgement is "a justified reason" (s.23(c)) and "fitness" (s.21), and is it reviewable? [G4 15 to 17] The meaning of the unusual word beside "(step-)" in s.29(a). [G4 14]
- **O27.** (offence) Does the bare "offence" of ss.30(b)(1), 35(2) and 36(b)(1) include a disciplinary offence, when s.6(a)(3) says "criminal" and s.21 says "criminal or disciplinary"? [G5 4, integration, row R7]

### Inspection

- **O28.** Is s.30(a)'s "will authorise" a duty, as taken, or a power? [G5 1] (The same question for ss.19(a) and 20, which group 4 encodes as a duty without a fork: row R5.)
- **O29.** Does s.32(2)'s "which he will show on demand" condition the use of the powers? Is a demand made by an inspector lacking the badge or the certificate a demand "under s.31(2)" for item (7)? [G5 2, 3]
- **O30.** Does "criminal proceeding on suspicion" include an investigation, and whose judgement is "unfit" in s.35(2)? [G5 5] Does withdrawal of consent under s.37(b)(3) end the consent for (b)(2)? [G5 6] Does an unpublished checklist bind, and who must publish it and the notice of an inspector's authorisation? [G5 7]
- **O31.** Which prevails, the Minister's instrument or the senior inspector's working rules? Is the power to change conditions in s.36(d) confined to modes of action? [G5 8, 9] Is an employee authorised only to test an expert as well, and how can a first testing body arise? [G5 10] May the hand-over at the end of an engagement be made under s.38(c)? [G5 11]
- **O32.** Does the cure-first rule of s.39(b) apply when a ground other than (a)(2) or (3) is also present? [G5 12] Is there a duty to comply with a demand for information under s.31(2) beyond the sanction of item (7), and when must compliance be made? [G5 15]
- **O33.** Do authorisations, revocations and suspensions take effect on the day made or the day after? [G5 14] Does IL s.10(c) move the end of a period an official fixes (keeping, authorisation, suspension, cure)? [G5 13]

### Chapter 6

- **O34.** What does a dash in the corporation column mean at items (1), (2), (4): no sanction, or a figure left out? [G6 1]
- **O35.** Are the s.45 additions cumulative and automatic, and is an addition itself rounded to NIS 10? [G6 2, 3] From which 1 January are the amounts updated, and does a half-way amount round up? [G6 4] How are the "months in which the violation continues" counted? [G6 5] What is "the said date" of s.44(d)? [G6 6]
- **O36.** Does IL s.10(c) apply to the s.45(b) and s.54(b) windows and to the s.57(e) publication period? [G6 7] Is the two years of s.45(b) counted from the previous violation's own day or from the day the sanction was imposed? [G6 8] Does a notice that omits what s.42(b) lists start the 30 days? [G6 9]
- **O37.** Does the update of s.47(b) wait for the notice in Reshumot of s.47(c)? [G6 10] Who refunds under s.56(c), and is there a time? [G6 11] For one act that is several breaches, which breach carries the single sanction? [G6 12] May the Commissioner extend the s.43 or s.53 period after it has run? [G6 13] Which court hears an appeal of a decision that is not a final decision of the Commissioner (s.62)? [G6 14] Is an act on the day a notice, demand, warning or decision is delivered within the period "within 30 (or 45) days" of it, and may the Commissioner's extension end the period earlier than the 30 days? [G6 15, 16; row R2] Group 6 takes the first as yes and the second as no, after its review.

### Commencement and regulations

- **O38.** s.63(a)(1): is "three months from [its publication or the entry into force of the regulations], whichever is later" counted from the later of the two days, or the later of two dates? [G7 1, G8 12] Does the Law commence on the last day of a period of months or the day after, and does IL s.10(c) move a commencement that falls on a Saturday? [G7 2] Ruled by the owner on 2026-10-14 for the first question: the later of the two dates (day X 16.7.2025), with the alternative documented (see "Owner rulings"); whether the Law means that reading remains a question for a domain expert.
- **O39.** Which paragraph of s.63(a) governs a system with refrigerants of both kinds, and a listed refrigerant whose use is not permitted? [G7 3] What commences the provisions that are not about work on a system? [G7 4] If no regulation under s.46 is made, does Chapter 6 never commence? [G7 5]
- **O40.** At what day is "provided its use was permitted by any law" judged, and has the Minister amended the Fourth Schedule since January 2025? [G7 6] Is item (66) `E170`, and is a designation matched by its printed letters and case? [G7 7]
- **O41.** s.58 and s.61: does s.58's status let a licensee do electrical work beyond the First Schedule? [G7 8] s.56 and s.62: which court hears the Commissioner's final decision, and which a decision of the Registrar or the Minister? [G7 9] Do the matters of s.60(2) need the committee's approval? [G7 10] How many heads of fee does s.59 give? [G7 11]

### The Fees Regulations

- **O42.** Which index readings and Director General notices exist for 1.1.2026, and what are the amounts now payable? [G8 1] Is the NIS 40 objection charge a fee that regulation 3(a) updates? [G8 2] Does "these regulations" in the amended regulation 3(a) mean the principal or the amending regulations? [G8 3]
- **O43.** Is regulation 2(c) a fee on the application or on the receipt of the licence, and does regulation 4 bar the grant of a temporary licence whose application fee is unpaid? [G8 4] Does "in addition to the payment of the fee in (a)" make an objector pay the exam fee again? [G8 5] Does an exact half shekel round up, and is each update rounded before the next? [G8 6]
- **O44.** Which day fixes the figure for an exam or objection that straddles 1 January or 4 May 2026? [G8 7] Did the 2026 amendment intend that an objection to a practical-exam score carries no charge? [G8 8] Is a theoretical exam as made a "required exam" that regulation 4 failed to reach? [G8 9] What did the SimpLEX draft's regulations 3 to 5 say, and what did the second panel's scenarios assert? [G8 10]

### Raised by the integration

- **O45.** Does a licence granted on a day last the years the Law says AND the day of the grant (groups 1, 2, 4, 5 count the event day as the first day of a status), or exactly the years (the module's convention, which group 3's "last year of validity" follows)? [row R2]
- **O46.** Which function of s.26(a) is a consultation about a particular course (function (3) or (4))? [row R6, see O20]
- **O47.** Should the Registrar's duty to grant under s.6 be answered for an application made before the commencement day of s.63(a)(1)? The headline refuses; group 2 does not gate. [row R4]

## What the sources do not answer, consolidated

Each item is an input or a named refusal in the encoding; none gets a default.
The group or groups that name it follow in brackets.

**Instruments and rates that are not in the sources.**
Any order under s.3(b) (which classes are exempt, with what duties or conditions), s.3(c), s.6(b), s.41(b) and s.63(a)(1); any regulation under s.46, s.60(1) or s.60(2) other than the Fees Regulations; the rates of reduction under s.46(b); the shekel interest and arrears fees of the Interest and Linkage Law (s.49, s.56(c)). [G1, G2, G5, G6, G7]
The consumer price index readings, the first update year of s.47(b), and the Director General's notice of updated fees under regulation 3(b). [G6, G8]
The text of Israeli Standard 994 parts 4 and 5, the date each wording took effect, and the conformity of any work to it. [G3]
The Budget Principles Law's definitions of "State employee", "budgeted body" and "supported body" (s.27) [G4]; the Securities Law's "interested party" (s.29(a)) [G4, G5]; the Mandatory Tenders Law (s.34(c)) [G5]; the Freedom of Information Law (s.57(d)) and the Fines, Fees and Expenses Collection Centre Law (s.51) [G6]; the Administrative Courts Law and item 21 of its First Schedule (s.62) [G7]; the Electricity Law's s.6 and the scope of the service-electrician licence (ss.58, 61) [G1, G7]; the list of electrician licences and the working-at-height approval (s.7) [G2].

**Facts and judgements that belong to officials or to the case.**
The Registrar's opinions and findings (fitness, special cases, circumstances that justify, recognition of a reputed expert, scope and content of foreign studies), the Minister's opinions and directions (the further conditions of eligibility for an inspector, the conditions and instructions of an instrument of authorisation, the period it fixes), the Commissioner's grounds, intention and authorisation, the reasons recorded for an extension, whether the Council's procedure under s.25(e) exists. [G1 to G6]
The age of majority (s.6(a)(1)); the identity of the Registrar, the Commissioner and the Director of the Training Division; the composition of the Council at any date. [G2, G4]
The conditions of a licence and the "provisions under this Law" that s.3(a) requires the work to follow (only s.17(d) names one). [G1, G3]
The classification of an act into a First Schedule activity; what makes a system "similar" or an expert "authorised" abroad; what "regularly", "sufficient measures" and "a reasonable time" mean. [G1, G2, G3]
The days of rest, recess and holiday for any year. [all groups]

**Times, days and effects the Law leaves out.**
When a decision under s.10 takes effect; when a revocation, suspension or authorisation begins and ends. [G1, G2, G5]
When the Law commences for an advertisement, for the Registrar's own chapters (ss.5, 10, 11), for the Council (Chapter 4), for inspection, for the regulation powers; what the Registrar's duty to grant is before the commencement day. [G1, G2, G3, G4, G5, G7]
A time limit for compliance with a demand under s.31(2), for the reports of s.34(d) and (e), for the three steps of s.38(b), for the publication of an inspector's authorisation or of the checklist, for the Registrar's appointment and notice, for filling a vacant seat, for the Council's reply. [G4, G5]
The time within which a renewal must be applied for (a regulation under s.60(2)(a)); whether a renewal can be made after a licence lapsed; from when a renewed licence is valid. [G2, G7]
Which day fixes the vintage and the update level of a fee for a service that straddles a commencement; any transitional provision for exams begun before 4.5.2026. [G8]
What an application made before the three-year note lapsed and decided after it is entitled to. [G2]
What happens when an authorisation's period ends (renewal, extension). [G5]
The date of the Law as amended after Wikisource revision 2947808, and of the Fees Regulations after revision 3011135. [all groups]

**Effects of a failure and gaps in the sanctions.**
Any sanction for a breach of ss.12, 14, 15, 16, 17 or 18(b), or of a licence condition under s.3(a): the Third Schedule has no row, and none is invented. [G3, G1, G6]
The effect of a failure of the proviso of s.24 (the section saves acts if a majority serve and does not say they are void otherwise). [G4]
Which instrument prevails when an instrument of authorisation and the senior inspector's working rules conflict. [G5]
Whether a cancelled warning triggers s.54; whether an addition under s.45 is itself rounded; the first update day for Chapter 6. [G6]
Who is the payer of a refund under s.56(c); whether a successful appellant is refunded the arrears fees (the Law says interest only). [G6]

**The SimpLEX draft.**
Its regulations 3 to 5; the rows 1 to 4 of its test table and the fee-update scenarios of its second panel; what payment its rows 5 and 6 assume. [G8]

**The integration layer's own gaps.**
How the Council classifies a consultation about a particular course (function (3) or (4)): assumed (3), the other callable. [row R6]
Whether the Registrar's duty to grant had begun before the commencement day: the headline refuses. [row R4]
The First Schedule activity an act amounts to, supplied by the caller in headline (b). [row R1]

## Nouns requests, resolved

`domain.l4` was NOT edited.
Its sha256 is `7ab63334a708e592ed172a42231b070280619b72eecd46bd2a7f3b18db2b644b`, byte-identical to the copy the surveyor left (`cmp` reports no difference), so no regression run was owed.
No request could be met by moving a noun into the domain: every noun the groups asked for is already declared locally in a group module, and a group module may not be edited, so a second declaration in `domain.l4` would be a duplicate definition of the same name.
A new field on `Work item`, `Record of offences` or `Certificate` would break every construction of that record in the eight groups, and a new constructor of `Party` would need every `CONSIDER` over it re-checked.
The disposition of each request, by group:

| group | request | disposition |
| --- | --- | --- |
| G1 | `First Schedule activity` into the domain; an activity field on `Work item`; what a `Certificate` attests; `Person` details; shared stand-ins for periods an official fixes | stays in `g1-first-schedule`; the integration's `Situation of one piece of work` carries the activity as its own field (`int-work`); the other requests stay open, with no answer depending on them |
| G2 | the foreign expert's application and the work done abroad; the Second Schedule's private nouns; the acts of ss.6, 7 and 9; the stand-in for the final certificate | stay in `g2-temporary-licence`, `g2-second-schedule`, `g2-conditions`; `int-grant` imports them from there; the request that `Application` carry a system (so that the s.63(a)(2) anchor of the three-year note is an input) is answered by the commencement day being an input (`int — the commencement day`) |
| G3 | the wordings of the Standard, the demands, the training records, the facts about a person who engages others; the licence's first day of the current term | stay; `int-work` and `int-licence-status` import them; the first day of the term is not added (group 3 carries it on each session) |
| G4 | a history of proceedings on `Record of offences` | stays as `Proceeding against a Council candidate or member for an offence` in `g4-council-membership` (row R7); the other nouns are group 4's own |
| G5 | a `Party` for an employee of a testing body; a field for a criminal investigation on `Record of offences`; shared nouns for a period an official states, for an authorisation, for standing as to offences | stay local; the stand-ins work (`a person` with a boolean; a local standing record) |
| G6 | the records of Chapter 6 in the domain; a `Party` for the State Treasury | stay in `g6-nouns`; `int-sanction` imports them; no deontic is written for the refund of s.56(c) because the Law names no payer, and no `Party` was added |
| G7 | `Head of fee under section 59`, `Matter of regulations under section 60`, `Forum for review` into the domain; a note on `Refrigerant`.`designation` | the heads are used from `g7-regulations` by `int-fees` (which imports both groups, as only an integration module may), so G8 never needed them in the domain; the note on the designation is documentation only and is not made (the exact-text rule is stated in `g7-fourth-schedule` and in NOTES) |
| G8 | `Vintage of the Fees Regulations` and `Service under the Fees Regulations` into the domain; a `Party` for the examinee and the objector; a note on `Price index reading` | used from `g8-fees-nouns` by `int-grant` and `int-fees`; the payers stay in `Payer under the Fees Regulations`; the note on the index is carried by row R12 of the register |

New nouns the integration needed are defined in `int-` modules and nowhere else: `Situation of one piece of work`, `Training record under one licence`, `Situation of one self-description`, `Situation of one engagement` (`int-work`); `Decision to extend the validity of a licence` (`int-licence-status`); `Facts of a measure under section 10(a)`, `Facts of a suspension under section 10(b)`, `Requirement of a particular course under section 17(b)` (`int-council`); `Foreign qualification relied on`, `Facts of a grant under section 6`, `Facts of a grant of a temporary licence under section 9`, `Facts of a renewal under section 8` (`int-grant`); `Answer on the sanction for a violation`, `Facts for pricing a violation` (`int-sanction`).
No type or rule of a group module was renamed, so there is no rename to list; the check that no name is defined twice is the import of all 43 group rule modules, the seven integration rule modules, the domain and the time module into one file, which the integrator repeated and which reported no diagnostic.

## Defects found in group modules

No group module was edited.
The defects that the three independent test authors found were repaired by the groups before this integration run; they are listed with their dispositions under "Independent tests".
The integration tests found no failing example in the rule modules as they stood when the tests were written, and one divergence of convention (row R2) that is a difference of design between two modules and not an error in either.
What follows is what I found, each with the file, the rule and the example.

1. **Group 4, modality of "will appoint" (a missing fork, not a wrong answer).** `g4-registrar.l4`, the rule `s 19(a) — the Minister must appoint, from among the Ministry's employees, a person to hold the Registrar's powers`, and `g4-council-membership.l4`, `s 20 — the Minister must appoint a member to the seat`, encode the future tense of "will appoint" as a MUST. Ruling 2 of the brief lists appointing among the powers to be encoded as MAY. Group 5 registered the same question for ss.30(a), 34(a) and 36(a) (fork F-DUTY) and made the power reading callable; group 4 registered no fork and offers no power reading. Failing example: none. Neither rule has a time limit, so an appointment can never be a breach whichever modality it carries, and no trace or assertion differs.
2. **Group 3 and group 2, one day (row R2).** `g3-training-duty.l4`, `s.17(a) — the day is in the last year of validity`, counts the last year back from the last day and leaves out the anniversary; `g2-validity.l4`, `the licence is in force on`, counts the grant day as a day of the licence. Failing example (asserted in `int-tests-consistency.l4`, Q2, and as red assertion 12): a temporary licence granted 1.12.2025 and recorded to end 1.12.2026 is in force on 1.12.2025, and 1.12.2025 is not in its last year of validity, so training attended that day does not count towards the eight hours. Both are defensible readings of the same Interpretation Law; the integration wires neither away.
3. **A defect repaired during this stage, recorded so the count is understood.** Before group 6's independent review an act on the day of delivery was counted late at s.43, s.48, s.53(a) and s.56(a) (fork F-ACTDAY). Group 6 repaired it and the integration's assertion on s.48 passes against the repaired module. I did not see the unrepaired module run in the integration (my first full run of `check.sh` was made while the repair landed: `g6-tests-red.l4` then counted 40 failing assertions and `g2-tests-red.l4` 44, where the fleet lead had given 31 and 33).
4. **`il-interpretation-time.l4` against `srcrefs.py`.** The vendored module quotes the Interpretation Law and the Interpretation Ordinance, not the HVAC Law, so `srcrefs.py check --refs` against the Law reports sixteen problems on it. This is not a defect in the module; `check.sh` pins it by its hash (as the brief says) and leaves it out of the quotation check.
5. **`l4 batch` and imported mixfix names (toolchain, found by groups 6 and 8, confirmed here).** `int-commencement.l4`'s exports fail under `l4 batch` with a check error in the re-printed module (`Expected keyword on the day but found day`), because they call group 7's three-argument mixfix `the Law has commenced for work on the system ... on the day ... given the facts ...` defined in an imported module. `int-fees.l4`'s `int — the vintage of the Fees Regulations in force on the day`, a one-argument export that calls a one-argument function, runs under `l4 batch` and returns `the Fees Regulations as amended` for 2026-05-04. The other `int-` exports were not run under `l4 batch` with real rows; those that call an imported mixfix of three or more arguments can be expected to fail the same way. Every export runs under `l4 run` and in the tests. The compiler defect behind this was filed on 2026-10-14 as smucclaw/l4-ide#1042, with a three-file reproduction and a matrix (a two-argument imported operator works; three and four arguments fail; a three-argument operator defined in the calling module works).
6. **Two functions of one group must not share their first backtick segment.** Not a defect of a group but a trap met here: `int (...) — ...` names were used where a second function would otherwise have shared a head with the first (two `int — the outcome of section 3(a) for the work of ...`), and a mixfix whose last element is a keyword after the last argument does not parse. Both are in the integration modules' history, not in any group module.
7. **Group 6, the `s 56(a)` day function does not ask whether the notice was a valid notice.** `g6-appeal-and-publication.l4`, `s 56(a) — the day notice of the decision counts as delivered to a violator who made no representations`, returns the s.44(d) day for any notice. Failing example (run on 2026-10-14): a notice of intention delivered 15.6.2030 that omits the violator's right to make representations and the statement that it will be treated as a payment demand. `s 44 — the day the payment demand is delivered or treated as delivered` gives NOTHING for it, and `s 44(d) — the notice … is treated as a payment demand, given` gives FALSE, yet the `s 56(a)` function returns 15.7.2030. The fleet lead's repair note says callers ask the s.44 function first. The integration's scenario S21 uses a complete notice and so does not meet it; no integration function calls `s 56(a)` for a defective notice.

## What check.sh prints

`check.sh` runs every module in this directory with `l4 run`, and counts error, satisfied, failed, refused and warning diagnostics from the diagnostics themselves and not from the exit code.
A module is red if it has an error that is not a failed assertion, a number of failed assertions other than its `expected_failed` count, or a number of refused assertions or of warnings other than its `expected_refused` count.
Twelve files are meant to fail, each with an exact count: the nine `*-tests-red.l4` files and the three `ind-*-tests-ambiguous.l4` files of the independent authors; `encoding.json` names them under `expected_red`.
Three files are meant to refuse, each with an exact count: `ind-b-tests-ambiguous.l4`, `ind-c-tests-ambiguous.l4` and `ind-c-tests-disagree.l4`; `encoding.json` names them under `expected_refused`.
A refused assertion is also reported as a warning, so a module is red if its refused assertions or its warnings differ from its `expected_refused`.
After the modules it checks the hash of the vendored time module, the shape of the modules and the import rule, the quotations and locators against the raw sources (`srcrefs.py check --refs`), and every `#TRACE` against its expectation (`check-traces.py`, with `--require-all`, so a trace with no expectation fails the run).
Run it as `L4=<path to l4> bash check.sh`; leave `JL4_LIBRARY_PATH` unset.
`INPUTS` (default `../inputs`) and `SRCREFS` name the raw sources and the quotation checker; if either is missing the step is reported as NOT RUN and the final line says so.

The final run covered 137 modules: 5224 assertions satisfied (4078 in the encoders' and the integrator's own modules, 1146 in the three independent authors' files), 227 failed and 15 refused.
The failures are exactly the 227 expected: the nine `*-tests-red.l4` files and the three `ind-*-tests-ambiguous.l4` failures; the 15 refusals are exactly the expected ones, in three `ind-` files, and each refusal is also one of the 15 warnings, so there is no other warning.
The quotation check read 1032 `src:` lines and 1105 locators and found 0 problems.
The trace check found 458 traces, 331 guarded by an `EXPECT` comment in the module and 127 by a row of `int-trace-expect.tsv`, all 458 as expected and 0 unguarded.
The run took 3 minutes 11 seconds of wall clock, one `l4` process at a time under `nice`, and ended with `check.sh: GREEN`.

The output of the final run, unedited:

```
l4 binary: /Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-41dd7a67/bin/l4 (sha256 matches the fleet's binary)

module                                    errors satisfied  failed  refused  warnings  exp.fail exp.refuse
domain.l4                                      0         0       0        0         0         0         0
g1-adverse-action.l4                           0         0       0        0         0         0         0
g1-application.l4                              0         0       0        0         0         0         0
g1-first-schedule.l4                           0         0       0        0         0         0         0
g1-interpretation.l4                           0         0       0        0         0         0         0
g1-licensing-duty.l4                           0         0       0        0         0         0         0
g1-register.l4                                 0         0       0        0         0         0         0
g1-tests-adverse.l4                            0       192       0        0         0         0         0
g1-tests-application.l4                        0        10       0        0         0         0         0
g1-tests-first-schedule.l4                     0       175       0        0         0         0         0
g1-tests-interpretation.l4                     0        90       0        0         0         0         0
g1-tests-licensing.l4                          0       223       0        0         0         0         0
g1-tests-red.l4                               19         0      19        0         0        19         0
g1-tests-register.l4                           0        18       0        0         0         0         0
g2-conditions.l4                               0         0       0        0         0         0         0
g2-exemption.l4                                0         0       0        0         0         0         0
g2-renewal.l4                                  0         0       0        0         0         0         0
g2-second-schedule.l4                          0         0       0        0         0         0         0
g2-temporary-licence.l4                        0         0       0        0         0         0         0
g2-tests-conditions.l4                         0       110       0        0         0         0         0
g2-tests-exemption.l4                          0        10       0        0         0         0         0
g2-tests-fixtures.l4                           0         0       0        0         0         0         0
g2-tests-red.l4                               44         0      44        0         0        44         0
g2-tests-renewal.l4                            0        16       0        0         0         0         0
g2-tests-second-schedule.l4                    0       210       0        0         0         0         0
g2-tests-temporary-licence.l4                  0        41       0        0         0         0         0
g2-tests-validity.l4                           0        93       0        0         0         0         0
g2-validity.l4                                 0         0       0        0         0         0         0
g3-licensee-duties.l4                          0         0       0        0         0         0         0
g3-operator.l4                                 0         0       0        0         0         0         0
g3-tests-licensee-duties.l4                    0       102       0        0         0         0         0
g3-tests-operator.l4                           0        55       0        0         0         0         0
g3-tests-red.l4                               19         0      19        0         0        19         0
g3-tests-training-duty.l4                      0       136       0        0         0         0         0
g3-training-duty.l4                            0         0       0        0         0         0         0
g4-composition.l4                              0         0       0        0         0         0         0
g4-conflict.l4                                 0         0       0        0         0         0         0
g4-council-membership.l4                       0         0       0        0         0         0         0
g4-council-work.l4                             0         0       0        0         0         0         0
g4-registrar.l4                                0         0       0        0         0         0         0
g4-tests-composition.l4                        0        49       0        0         0         0         0
g4-tests-conflict.l4                           0        59       0        0         0         0         0
g4-tests-council-work.l4                       0       115       0        0         0         0         0
g4-tests-membership.l4                         0       157       0        0         0         0         0
g4-tests-red.l4                               17         0      17        0         0        17         0
g4-tests-registrar.l4                          0        39       0        0         0         0         0
g5-inspectors.l4                               0         0       0        0         0         0         0
g5-senior-inspector.l4                         0         0       0        0         0         0         0
g5-test-conduct.l4                             0         0       0        0         0         0         0
g5-testing-bodies.l4                           0         0       0        0         0         0         0
g5-tests-entry.l4                              0        10       0        0         0         0         0
g5-tests-inspectors.l4                         0       145       0        0         0         0         0
g5-tests-red.l4                               19         0      19        0         0        19         0
g5-tests-senior-inspector.l4                   0        82       0        0         0         0         0
g5-tests-test-conduct.l4                       0        84       0        0         0         0         0
g5-tests-testing-bodies.l4                     0       125       0        0         0         0         0
g5-tests-withdrawal.l4                         0        98       0        0         0         0         0
g5-withdrawal.l4                               0         0       0        0         0         0         0
g6-amount.l4                                   0         0       0        0         0         0         0
g6-appeal-and-publication.l4                   0         0       0        0         0         0         0
g6-notice-and-hearing.l4                       0         0       0        0         0         0         0
g6-nouns.l4                                    0         0       0        0         0         0         0
g6-payment.l4                                  0         0       0        0         0         0         0
g6-schedule-three.l4                           0         0       0        0         0         0         0
g6-tests-amount.l4                             0       137       0        0         0         0         0
g6-tests-appeal-and-publication.l4             0        80       0        0         0         0         0
g6-tests-notice-and-hearing.l4                 0        99       0        0         0         0         0
g6-tests-payment.l4                            0        53       0        0         0         0         0
g6-tests-red.l4                               40         0      40        0         0        40         0
g6-tests-scenarios.l4                          0        28       0        0         0         0         0
g6-tests-schedule-three.l4                     0        80       0        0         0         0         0
g6-tests-warning.l4                            0        72       0        0         0         0         0
g6-warning.l4                                  0         0       0        0         0         0         0
g7-administrative-courts.l4                    0         0       0        0         0         0         0
g7-commencement.l4                             0         0       0        0         0         0         0
g7-electrical.l4                               0         0       0        0         0         0         0
g7-fourth-schedule.l4                          0         0       0        0         0         0         0
g7-regulations.l4                              0         0       0        0         0         0         0
g7-tests-administrative-courts.l4              0        13       0        0         0         0         0
g7-tests-commencement.l4                       0       107       0        0         0         0         0
g7-tests-electrical.l4                         0        19       0        0         0         0         0
g7-tests-fourth-schedule.l4                    0        85       0        0         0         0         0
g7-tests-red.l4                               19         0      19        0         0        19         0
g7-tests-regulations.l4                        0        55       0        0         0         0         0
g8-fees-as-amended.l4                          0         0       0        0         0         0         0
g8-fees-as-made.l4                             0         0       0        0         0         0         0
g8-fees-draft.l4                               0         0       0        0         0         0         0
g8-fees-nouns.l4                               0         0       0        0         0         0         0
g8-fees.l4                                     0         0       0        0         0         0         0
g8-simplex-table.l4                            0         0       0        0         0         0         0
g8-tests-dates.l4                              0        47       0        0         0         0         0
g8-tests-fees.l4                               0       146       0        0         0         0         0
g8-tests-red.l4                               16         0      16        0         0        16         0
g8-tests-reg3.l4                               0       113       0        0         0         0         0
g8-tests-reg4.l4                               0        76       0        0         0         0         0
g8-tests-simplex.l4                            0        64       0        0         0         0         0
il-interpretation-time.l4                      0         0       0        0         0         0         0
ind-a-tests-ambiguous.l4                       2         0       2        0         0         2         0
ind-a-tests-commencement.l4                    0         9       0        0         0         0         0
ind-a-tests-disagree.l4                        0         6       0        0         0         0         0
ind-a-tests-duties.l4                          0        16       0        0         0         0         0
ind-a-tests-fixtures.l4                        0         1       0        0         0         0         0
ind-a-tests-s10-s11.l4                         0        38       0        0         0         0         0
ind-a-tests-s12-s18.l4                         0        50       0        0         0         0         0
ind-a-tests-s2-s4.l4                           0        66       0        0         0         0         0
ind-a-tests-s5-s9.l4                           0        52       0        0         0         0         0
ind-a-tests-sch2.l4                            0        70       0        0         0         0         0
ind-b-tests-ambiguous.l4                      16         0      16        2         2        16         2
ind-b-tests-disagree.l4                        0         2       0        0         0         0         0
ind-b-tests-g4.l4                              0       127       0        0         0         0         0
ind-b-tests-g5.l4                              0        99       0        0         0         0         0
ind-b-tests-g7.l4                              0       271       0        0         0         0         0
ind-c-tests-ambiguous.l4                       2         0       2       10        10         2        10
ind-c-tests-amount.l4                          0        51       0        0         0         0         0
ind-c-tests-appeal.l4                          0        33       0        0         0         0         0
ind-c-tests-commencement.l4                    0        11       0        0         0         0         0
ind-c-tests-disagree.l4                        0        11       0        3         3         0         3
ind-c-tests-fees.l4                            0        68       0        0         0         0         0
ind-c-tests-powers.l4                          0        15       0        0         0         0         0
ind-c-tests-procedure.l4                       0        36       0        0         0         0         0
ind-c-tests-routes.l4                          0        11       0        0         0         0         0
ind-c-tests-schedule.l4                        0        48       0        0         0         0         0
ind-c-tests-simplex.l4                         0        34       0        0         0         0         0
ind-c-tests-warning.l4                         0        21       0        0         0         0         0
int-commencement.l4                            0         0       0        0         0         0         0
int-council.l4                                 0         0       0        0         0         0         0
int-fees.l4                                    0         0       0        0         0         0         0
int-grant.l4                                   0         0       0        0         0         0         0
int-licence-status.l4                          0         0       0        0         0         0         0
int-sanction.l4                                0         0       0        0         0         0         0
int-tests-commencement-and-fees.l4             0        98       0        0         0         0         0
int-tests-consistency.l4                       0        64       0        0         0         0         0
int-tests-fixtures.l4                          0         0       0        0         0         0         0
int-tests-licence-life.l4                      0       113       0        0         0         0         0
int-tests-red.l4                              14         0      14        0         0        14         0
int-tests-work-and-sanction.l4                 0        85       0        0         0         0         0
int-work.l4                                    0         0       0        0         0         0         0
TOTAL (137 modules)                          227      5224     227       15        15       227        15
(a failed assertion is also an error; a refused assertion is also a warning; any other error, any refusal or warning beyond the module's expected_refused, and any failed count other than its expected_failed, make the run red)

il-interpretation-time.l4: sha256 matches the brief (d1552de57266d7dc7a5d2fca43b73e100b8814dc78f33fb755daeb2294cf671f)
shape: every module starts with @lang en, has a plain name, and no group module imports another group's
srcrefs check: 1032 src: lines, 352 runs, 1105 locators, 0 problems
module                                        traces in-module   sidecar     ok   bad  unguarded
g1-tests-adverse.l4                               14        14         0     14     0          0
g1-tests-application.l4                            9         9         0      9     0          0
g1-tests-licensing.l4                             17        17         0     17     0          0
g1-tests-register.l4                               4         4         0      4     0          0
g2-tests-conditions.l4                            10         0        10     10     0          0
g2-tests-exemption.l4                              7         0         7      7     0          0
g2-tests-renewal.l4                                4         0         4      4     0          0
g2-tests-temporary-licence.l4                      9         0         9      9     0          0
g3-tests-licensee-duties.l4                       25        25         0     25     0          0
g3-tests-operator.l4                               8         8         0      8     0          0
g3-tests-training-duty.l4                         17        17         0     17     0          0
g4-tests-conflict.l4                              21        21         0     21     0          0
g4-tests-council-work.l4                          22        22         0     22     0          0
g4-tests-membership.l4                            32        32         0     32     0          0
g4-tests-registrar.l4                             17        17         0     17     0          0
g5-tests-inspectors.l4                            51        51         0     51     0          0
g5-tests-senior-inspector.l4                      23        23         0     23     0          0
g5-tests-test-conduct.l4                          39        39         0     39     0          0
g5-tests-testing-bodies.l4                        21        21         0     21     0          0
g5-tests-withdrawal.l4                            11        11         0     11     0          0
g6-tests-amount.l4                                 6         0         6      6     0          0
g6-tests-appeal-and-publication.l4                21         0        21     21     0          0
g6-tests-notice-and-hearing.l4                    19         0        19     19     0          0
g6-tests-payment.l4                                9         0         9      9     0          0
g6-tests-scenarios.l4                              3         0         3      3     0          0
g6-tests-schedule-three.l4                         5         0         5      5     0          0
g6-tests-warning.l4                               17         0        17     17     0          0
g7-tests-commencement.l4                           2         0         2      2     0          0
g7-tests-regulations.l4                            6         0         6      6     0          0
g8-tests-reg4.l4                                   9         0         9      9     0          0
TOTAL                                            458       331       127    458     0          0
check-traces: all 458 guarded trace(s) behaved as expected

check.sh: GREEN
(a green run is the integrator's: it says nothing about whether a domain expert agrees with any reading in NOTES.md)
```

How to read the trace table: `in-module` traces carry an `-- EXPECT` comment written by the group's author; `sidecar` traces are those whose author wrote the expectation in prose or not at all (groups 2, 6, 7 and 8), and whose expectation is a row of `int-trace-expect.tsv`, keyed by the sha1 of the trace's statement so that adding a trace to a module cannot shift a row onto the wrong trace.
A row whose statement is no longer in the file is reported as stale and fails the run.
The group 2 rows were decided by the integrator from the authors' comments and the rules; the rows for groups 6 to 8 were derived by a separate reader that was told to read the tests and rules and not to run them; the four group 6 traces added by the group's repair were decided by the integrator from the comments in the test files and the rules, as for group 2, before they were run.
Every row matched the printed result on its first run.

The positive controls for `check-traces.py`, run on copies of modules in the integrator's work directory and never on the deposit; each of the failing ones exits 1, and the unmodified copies exit 0 (15 traces, all as expected):

1. one `-- TRACE-EXPECT` of a copy of `g3-tests-operator.l4` changed from BREACHED to FULFILLED: the checker printed the line of the trace, the expectation and the DEONTIC BREACHED result it got, and failed (7 ok, 1 bad);
2. one sidecar row for the second trace of `g2-tests-exemption.l4` changed from STANDING to FULFILLED: the checker printed the result it got (the permission printed back, still open) and failed (6 ok, 1 bad);
3. the same module with an empty sidecar and `--require-all`: all 7 traces were reported unguarded and the run failed;
4. the first trace of a copy of `g6-tests-payment.l4` duplicated in front of itself, which shifts every position: all nine sidecar rows still attached to the trace they were written for (9 ok), and the extra, identical trace was reported unguarded;
5. a comment appended to the last line of the first trace of another copy: its row was reported stale, the trace was reported unguarded, and the run failed.

The same control was applied to the other half of the harness: `int-tests-red.l4` holds fourteen assertions that are meant to fail, and `check.sh` goes red if the count is anything but fourteen, in either direction.

## Toolchain notes

The `l4` binary is the cabal-store build the fleet used, `/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-41dd7a67/bin/l4`, sha256 `2e3d6bd3a154e6b4080a445af6cc189dbc4ac087d8221682d09509212f1ce187`; `check.sh` prints whether the binary it was given matches.
It was run with `JL4_LIBRARY_PATH` unset, so every module resolved the prelude embedded in the binary.
`check-traces.py` reads `l4 run FILE --json`, whose `results` array has one entry per `#TRACE` and `#EVAL`, keyed by the range of the directive; a deontic result is printed back as text, so the checker compares text and never a value.
A run killed by a signal, or one that prints no JSON, is reported as no valid run and fails: the checker cannot tell "all as expected" from "nothing ran" unless it counts what it saw.

`l4 batch` re-prints a module and re-runs it; an export that calls a mixfix function of three or more arguments defined in an imported module fails that re-print (see "Defects found", item 5; filed as smucclaw/l4-ide#1042).
The exports of `int-commencement` are the ones this affects.
Every export runs under `l4 run`, which is how all the tests call them.

Four rules of L4 cost the integrator time and are not obvious from the error text.
Two functions must not share the same first backtick segment of their names (the head keyword of a mixfix); the ambiguity is detected where the second is used.
A mixfix name must end with an argument, not a keyword.
The `GIVEN` list must be in the order the arguments appear in the name.
A type name of several words needs backticks in a `WITH` construction.
An `#ASSERT REFUSED` is satisfied only when the expression refuses; an `#ASSERT` of anything else that refuses is reported as refused, which `check.sh` counts as red.


## Peeked

The three independent authors' transcripts were audited, as the fleet lead reports: each wrote its expectations before opening any module of the encoding.
The integrator did not read those transcripts or the authors' work directories.
The 27 test files and three expectations documents of the independent authors reached the deposit after the integrator's own modules and tests were written, so none of the integrator's expected values was decided with them in view; the authors' documents say which files each of them had opened.

Nothing outside the permitted material was read.
The integrator read the brief, the plan sections named in the assignment, the two skills, `domain.l4`, the eight FRAGMENTs and the group modules, and the raw sources only through `srcrefs.py`.
A directory listing of the fleet's `work/` directory, made while locating a file in it, showed the names of other fleet directories (`ind-a`, `ind-b`, `ind-c`, `hunt`, `overlap`, `surveyor`); none was opened, listed inside or read, and nothing in them was searched for.
A process listing (`pgrep -fl`), made to see whether other `l4` processes were running before starting one, printed the command line of another session's shell, with its scratchpad path; it was a listing of processes, nothing was read from that path, and no process other than the integrator's own was stopped or touched.
No git command was run.
The expectations for the sidecar rows of groups 6 to 8, apart from four rows of group 6 added after its repair, were written by a sub-agent of the integrator, which was shown the test files and rule modules and told not to run them; those of group 2 and the four group 6 rows were decided by the integrator itself.

## Provenance of this run

This section was written by the launching session (Claude Sonnet 5.5, session "IL-hvac", working with Meng Wong) on 2026-10-14, after the integrator had finished. The session was titled "hvac-family" when the earlier commits of this series were made (their `Claude-Session` trailers say so); the title in its transcript now is "IL-hvac".
Everything above this heading was written by the integrator, except where it quotes the fleet lead.
The row is `legalese-full-sonnet-5.5`: the whole Law and the Fees Regulations in three vintages, by a Sonnet 5.5 fleet in the economy shape (one survey, eight parallel group encoders, one integrator), with Opus 5.5 test authors and a blind Opus 5.5 hunt for contradictions.
Its final check, re-run by the launching session on a fresh copy of the directory on 2026-10-14: 137 modules, 5,224 assertions satisfied, 227 failed (all expected), 15 refused (all expected), 458 traces guarded and as expected, 0 problems in the quotation check, and the hashes of the binary and of the vendored time module matching.

### How the row was made

The fleet ran from the evening of 2026-10-13 (about 20:20 +08) to the morning of 2026-10-14, in this order.
1. **Preparation.** The lead wrote a common brief (scope, sources, the cleanroom rules, the time rules) and had it reviewed once before launch. The 13 input files are those of the earlier HVAC rows plus `il-interpretation-time.l4`, the time module of the Interpretation Law row, vendored byte-identical (sha256 `d1552de5...671f`, verified by `check.sh`). The notes of that row were given to the fleet cut before their launch-provenance section.
2. **Survey.** One Sonnet agent wrote `phase1/PLAN.md`, a 441-row coverage skeleton (364 encoded, 55 inert, 4 refused, 18 out-of-scope, 0 deferred), 21 integration points, a register of 46 periods, 43 first-read traps, and `domain.l4`.
3. **Eight encoders in parallel** (about 21:27 +08), one per group G1 to G8, each with its own slice of the plan and its own prefix, each writing modules, tests of their own and a FRAGMENT. The lead then ruled, in the brief, that groups import nothing across groups, that powers are encoded as `MAY` rules, how commencement is passed on, the default reading of IL s.10(c) per kind of period, and that exported names are unique fleet-wide.
4. **Independent stage.** Three Opus test authors (ind-a: G1 to G3; ind-b: G4, G5, G7; ind-c: G6, G8) each decided their expected answers from the sources and wrote them down before opening any module (218, 347 and 154 scenarios), then wrote tests. One Opus agent read the sources only, blind to the plan, the modules and the brief, and wrote a register of contradictions. A Sonnet agent compared the plan's traps, the encoders' contradictions and the hunt.
5. **Repairs.** The test authors found seven encoding defects, each repaired by its group with exported names unchanged (listed under "Independent tests" above). The lead verified each repair in a clean copy.
6. **Integration** by one Sonnet agent, which wired the groups, wrote the headline functions and the integration tests, wrote `check.sh` and the trace checker, and consolidated the registers. It spawned one read-only helper agent of its own (Sonnet, 94 requests) to dig facts out of transcripts, and a sub-agent wrote the expectations for the sidecar trace rows of groups 6 to 8 (see the limits below).
7. **Merge of the independent suites** into the row, with `expected_refused` added to `check.sh`.

The binary is `/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-41dd7a67/bin/l4` (built 2026-10-13 16:13 from l4-ide `unstable`, sha256 `2e3d6bd3a154e6b4080a445af6cc189dbc4ac087d8221682d09509212f1ce187`), with `JL4_LIBRARY_PATH` unset.

### Agents, models and effort

Models were read from the transcripts. Requests and output tokens were counted from them on 2026-10-14; the output figure sums per-request usage, so it is a lower bound. Every agent ran at `effort: high`, the lead's reading of the owner's "Set generous budget"; the earlier solo rows ran at default effort, so this row is not effort-comparable with them.

| role | model | requests | output tokens (at least) |
| --- | --- | --- | --- |
| surveyor | Sonnet 5.5 | 242 | 40,205 |
| encoder G1 | Sonnet 5.5 | 304 | 45,822 |
| encoder G2 | Sonnet 5.5 | 572 | 24,627 |
| encoder G3 | Sonnet 5.5 | 284 | 10,252 |
| encoder G4 | Sonnet 5.5 | 273 | 15,449 |
| encoder G5 | Sonnet 5.5 | 284 | 62,285 |
| encoder G6 | Sonnet 5.5 | 480 | 13,352 |
| encoder G7 | Sonnet 5.5 | 302 | 18,507 |
| encoder G8 | Sonnet 5.5 | 391 | 14,955 |
| independent test author ind-a | Opus 5.5 | 204 | 21,662 |
| independent test author ind-b | Opus 5.5 | 188 | 17,783 |
| independent test author ind-c | Opus 5.5 | 213 | 25,147 |
| blind contradiction hunt | Opus 5.5 | 134 | 41,964 |
| overlap table | Sonnet 5.5 | 65 | 9,082 |
| integrator | Sonnet 5.5 | 740 | 22,290 |
| integrator's helper | Sonnet 5.5 | 94 | 8,612 |

### Rulings by the owner during the run

- The row name, `legalese-full-<model>-5.5`, a fresh run, with the external contribution `legalese-michael` left alone (Meng Wong, 2026-10-13).
- The test authors and the contradiction hunt run on Opus: "Test author and contradiction hunt on opus ok" (2026-10-13).
- Day X: see "Owner rulings" above ("Use 16 July but document the 16 Oct alternative in the forks register or in notes.", 2026-10-14).
- The meaning of "black ink" and "red ink" in the norm-log discussion was ruled for the ledger work and does not appear in this row. This row's two ways of judging a trace carry other names where they are discussed.

The choice of Sonnet with the economy shape, the depth given to the institutional chapters 4 and 5, the inclusion of the Fees Regulations and the SimpLEX table, the deferral of a Hebrew twin, and every other default are the lead's or the encoders' and are "assumed, not ruled".

### What the independent stages found

- **The test authors** decided 719 scenarios from the sources before opening the encoding (218, 347 and 154 for the three authors; their documents are `INDEPENDENT-ind-*-expectations.md`). Against the modules as first written, 19 of their assertions failed, for seven defects, each repaired by its group: G2's graded certificate of the grade sought (6 assertions); G5's employee test for s.30(b) and G7's unsubstituted placeholder, which its own test had repeated (1 each); G6's delivery-day timeliness, extensions that cannot shorten, and defective s.42(b) notices (3 defects, 8 assertions in all); G8's reg 4 and the temporary licence (3 assertions). A further 3 assertions refused and were kept: a corporation at a dash on Third Schedule items (1), (2) and (4), which is G6's fork F-DASH. They also found a wiring error that the plan itself contained (s.18(a) fed from capacity only), which the integrator corrected. The nine ambiguities they found are kept as open questions, with the other reading in a file that fails by design.
- **The blind hunt** found 52 points in the source (28 that change an answer, 9 gaps, 15 drafting defects). In the overlap table, 29 of them were also found by the surveyor, the encoders or both and 15 only by the hunt; the hunt in turn missed 9 of the survey's 43 traps and 42 of the encoders' 90 items. Neither list contains the other.
- **A review of the hunt's inputs** found that `knesset-bill-25_ls2_5256851.pdf` is the committee's text for the second and third readings of 11 December 2024, not the bill as tabled; the brief had called it "the bill as tabled" and that is corrected. The tabled bill (Government Bills 1578, 15 August 2022, p. 1432) is not among the inputs.

### Limits on the independence

- The expectations for the 331 traces guarded by comments in the modules were written by the encoders themselves.
- The expectations for the 127 sidecar trace rows of groups 2, 6, 7 and 8 (`int-trace-expect.tsv`) are not independent of the encoding. The integrator decided the 30 rows of group 2, and four rows of group 6 added after its repair, from the authors' comments and the rules. A sub-agent of the integrator decided the other 93 (groups 6, 7 and 8), having been shown the test files and the rule modules and told not to run them. The independent suites contain no `#TRACE`.
- The quotation check proves that each quoted line and locator matches the raw text; it does not prove that the rule below a quotation means what the quotation says.
- The independent authors decided their answers from the same Wikisource text and gazette pages as the encoders, so a shared misreading of a source would not be caught.

### Audit of the transcripts

The lead audited every agent's transcript on 2026-10-14. Results:
- No encoder's tool call named another group's files, and no agent opened another encoding of the subject (`commons`, `commonswt`, `canon`, `il`) or the lead's memory, trigger table or scratch directories. The only reads under `~/.claude` are the harness's own saved tool-output files and one encoder grepping its own transcript.
- The hunt opened nothing in the deposit, the plan, the brief or other agents' directories.
- Each test author wrote its expectations document before its first call touching any group module, FRAGMENT or the deposit.
- Processes were stopped by pattern, against the rule, by three encoders (G3, G6 and G7, between about 21:50 and 22:20 +08), each of which disclosed it; every result they report was re-run afterwards, and the mutation runs that those kills interrupted were repeated. No other encoder killed anything.
- The surveyor read the l4-ide `jl4/examples` tree to learn where `@desc` attaches, outside the list the brief allowed, and wrote two throwaway files under `/tmp`. G2 copied a backup of its sources to a scratch directory outside the fleet directory. The overlap agent wrote and deleted one script outside its own directory. Several agents redirected command output to `/tmp` and discarded it.
- The integrator printed another session's command line in a process listing, read nothing from it and touched no process of that session.

### Events during the run

- The session hit its usage limit during the repair stage. Five agents stopped mid-task and were resumed the next morning; the lead re-ran every group in a clean copy before accepting any figure, and the integrator re-ran against the repaired files.
- An encoder asked whether modules of one group may import each other; the lead ruled that only imports across groups are barred and told all eight.
- Group 8 found that `l4 batch` fails on a call to a mixfix operator of three or more arguments defined in an imported module. The lead reproduced it, narrowed it, and filed it as smucclaw/l4-ide#1042 on 2026-10-14. The integration modules' exports are affected in the same way (see "Toolchain notes").

### Not done

- No Hebrew twin of this row.
- No domain expert has read it against the Law (gate HG1 is not sought).
- Comparison with the enacted gazette is limited to what the FRAGMENTs and the survey's trap T41 say was checked (every number, table and list of the schedules, and the passages the encoders name); the rest is read from the Hebrew Wikisource text, revision 2947808 of the Law and 3011135 of the Fees Regulations.
- The draft vintage of the Fees Regulations exists only as a screenshot that shows regulations 1 and 2; its regulations 3 to 5 and the second panel of the SimpLEX table are not visible, so that vintage is silent on them.
- Section 32(2) ("which he will show on demand") is encoded with snapshot flags, which cannot say when a demand came; an event-based model of it is a prototype outside this row, and the choice between its readings is open (see the open questions).
- The row was not compared with the five earlier rows beyond the date logic and the answers named in this file.

### Related material that is not part of the row

- A bilingual working paper (English and Hebrew) on the conflict between Second Schedule Part B items 1 and 5 for the 5-unit certificate, with applicants that turn on the choice, was prepared for the drafters. It is a private page, not a file of this row.
- A prototype of the s.32(2) question as an event log judged twice (at the deadline and on hindsight) lives in the lead's scratch directory.
