# Reference graph for the Singapore television and radio receiver provisions

This folder holds a graph of which Singapore texts point at which other texts, built for a lay reader's diagram.
Every arrow in `edges.tsv` carries a verbatim fragment of a deposited text, at most 25 words, and the lines it sits on.
This graph records references between texts; it states no answer to the question.

The question the picture serves is whether licences are needed for television receivers, radio receivers, vehicle receivers and satellite dishes, and what follows without one.
The graph does not say, and no gloss, note or reason in it says.

Paths below are relative to the worktree root.
"Deposit" means a text under `subjects/sg/*/registers/source-bundle/*.txt`.
A bare file name in a note, or in this README, stands for the one deposit of that name.
The licence notes for the deposits are `SOURCE-LICENSE.md` in the parent folder and `SOURCE-LICENSE-GAZETTE.md` in the source-bundle folders; only short fragments are quoted here.

## Files

- `nodes.tsv` has one row per provision or instrument.
- `edges.tsv` has one row per arrow, each backed by a quotation.
- `edges-uncited.tsv` lists arrows that were looked for and could not be backed by a quotation; nothing in it is drawn.
- `tv-path.tsv` has one row per node, giving the quotation behind its `on_tv_path` value.
- `renumbering.tsv` has one row per Telecommunications Act section whose 2000 Revised Edition number is used, each citing a row of the printed Comparative Table.
- `check-graph.py` is run as `python3 -I check-graph.py` and prints counts and problems; it exits 0 only when there are no problems.
- `README.md` is this file.

## Columns

`nodes.tsv` columns, tab-separated, one header row:

- `id` is the node id used in `edges.tsv`.
- `short_label` is what a lay reader sees on the box, six words at most.
- `full_citation` is the full name of the text.
- `kind` is one of Act, section, regulations, schedule, order, notification, technical-specification.
- `made` is the day the instrument was made, or the Act was assented to.
- `published` is the day the Gazette first published it, with the time (`2012-10-31 17:00 SGT`) where the Gazette's own header gives one.
- `in_force` is the day it came into operation.
- `deemed_from` is the day a retrospective instrument is deemed to operate from, else empty.
- `revoked` is the day it ceased, else empty.
- `source` is the `path:line` (or `path:first-last`) that states the dates, or, for a section, the line where the section begins in the consolidated text.
- `added_for_arrow` is empty, or the edge id that needed this node.
- `note` is empty, or one sentence of fact; it may carry `file.txt:line` pointers to the other lines that state a date.
- `on_tv_path` is the last column: `yes`, `not-decided` or `no`; see "On the television path".

`edges.tsv` columns:

- `edge_id` is E01, E02 and so on.
- `from` and `to` are node ids; the arrow points from the text that does the act to the text acted on or relied on.
- `kind` is one of the eight kinds below.
- `published` is the day the arrow became readable by the public; `effective` is the day it takes effect; `deemed_from` is the retrospective date, else empty.
- `source` is `path:first_line-last_line`, the lines that hold the words that make the arrow.
- `quote` is a verbatim fragment of those lines, whitespace collapsed, at most 25 words.
- `gloss` is one plain sentence that names no conclusion about the question.
- `basis` is the last column: `named` or `by-description`; see "Named and by-description arrows".

`tv-path.tsv` columns are `id`, `on_tv_path` (the same value as in `nodes.tsv`), `source` and `quote` (for a `yes` row, a verbatim fragment of a deposit that names the receiver, the apparatus or the licence; empty for any other row) and `why` (one sentence of fact).

`renumbering.tsv` columns are `new_2020`, `old_2000`, `source` (one line of the printed 2020 Revised Edition's Comparative Table), `quote` (that whole line) and `used_for`.

`edges-uncited.tsv` columns are `uncited_id`, `from`, `to`, `kind`, `reason`, `looked_in` and `missing`.

## Kinds

- `made-under`: the instrument says it is made under that power.
- `amends`: it changes words of the target but leaves it standing.
- `revokes`: it ends the target.
- `replaces`: it substitutes a new text for the target.
- `saves`: it keeps something alive.
- `carves-out`: it removes a case from the target's reach.
- `defines-by-list`: the target's defining words depend on a list held in another instrument or Schedule.
- `cites`: it refers to the other without any of the above; used only where the reference is on the path.

## Conventions

- For a retrospective instrument the only operation date the text states is the deemed date, so `in_force` and `effective` repeat `deemed_from`, and the gap between that column and `published` is the signal.
- S 588/2023 has a split commencement: it comes into operation on 1 September 2023, except that its paragraphs 2 and 3(a) are deemed to have come into operation on 31 December 2021 (TA1999-N1-S588-2023.txt:19-24).
- Its node therefore carries `in_force` 2023-09-01 and `deemed_from` 2021-12-31; the edge that quotes paragraph 2 (E46) carries the deemed day as both `effective` and `deemed_from`, and its other edges (E45, E47) carry 2023-09-01 and no `deemed_from`.
- The time zone label `SGT` follows the brief's format; the Gazette header itself says only "5:00 pm", "5.00 pm" or "5 pm".
- On an edge whose `from` is an instrument with a stated `made` or `published` date, `published`, `effective` and `deemed_from` are copied from that instrument's node row as above, and the checker insists on it.
- On an edge whose `from` is a section or a schedule, those three columns are empty, because no deposited line states when the current words of that section began.
- On an edge whose `from` is Rg 1, the TVRO regulations (Rg 3) or the Dealers Regulations (Rg 7), those three columns are empty (E01, E05, E07, E31, E37, E38, E39), because the words come from a Revised Edition that prints an edition date and no first-publication line, and the as-made text is not deposited.
- The Telecommunications Act sections are cited by their 2020 Revised Edition numbers, which are the numbers in the scope list; where a quotation or a note uses the 2000 Revised Edition number, "Renumbering used" gives the row of the printed Comparative Table that links the two.
- The Broadcasting Act sections keep the same numbers in the 2003, 2012 and 2020 editions.
- In `TA1999.txt` the arrangement of sections is one number off from the body (the arrangement at line 171 numbers "Exemption from sections 53, 54 and 55" as 55, and the body at line 4935 numbers it 56); every citation here is to the body.
- Line numbers count newline characters only; the deposits contain form feeds at page breaks, which do not start a line.
- Page headers sit inside section bodies in several deposits; each quotation was chosen from a run of lines with no header in it.
- The in-force date of Rg 1, the TVRO regulations (Rg 3) and the Dealers Regulations (Rg 7) is the bracketed date printed under the title or arrangement of the Revised Edition; the text does not label it, and the Order O 3, whose as-made text says "shall come into operation on 12th November 1998" (TA1999-O3-S549-1998.txt:27), prints its own date the same way (TA1999-O3.txt:21).
- S 588/2023 prints some words with stray spaces inside them ("sec tion", "Telec ommunic ations"); quotations from it keep those spaces so that they match the deposit.

## What check-graph.py checks

- The five TSVs have the exact header and every row has the right number of fields.
- Every `source` file exists, is valid UTF-8, and has the cited lines.
- Every `quote` is at most 25 words and is a substring of the cited lines after whitespace is collapsed on both sides.
- Every `from` and `to` is a node id and every `kind` is allowed.
- Every date parses, and `deemed_from` is not later than `effective`.
- Every node date (except `revoked`) is found in the lines cited by `source` and by the `file.txt:line` pointers in the note; a time of day is found there too.
- Every `revoked` date equals the `effective` date of a `revokes` edge into that node.
- Every edge date agrees with its `from` node, as described under Conventions.
- `on_tv_path` is one of the three values, `tv-path.tsv` has one row per node with the same value, and a `yes` row has a quotation that is a substring of its source and contains the word receiver, television, broadcasting apparatus or TVRO.
- `basis` is one of the two values, and where the target is a numbered section a `named` quotation contains that number (the 2020 number or the 2000 number) while a `by-description` quotation does not.
- Each `renumbering.tsv` row cites one line whose whole text, whitespace collapsed, is "new old"; every Telecommunications Act section node except section 2 has a row; every row is used; and any "then section N", "numbered N in the 2000 Revised Edition" or "section N of the 2000 Revised Edition" in a note or gloss names an old number that has a row.
- No label, note, gloss or reason contains a conclusion word such as "offence", "liable" or "lawful".
- The checker was run against deliberately damaged copies (a changed quotation, a shifted line range, a wrong date, a wrong time, an over-long quotation, a conclusion word, a wrong `basis`, a `yes` row with a quotation that names no receiver, a wrong renumbering line, a missing renumbering row, an unknown old number, a wrong split-commencement date) and reported every one.

Two limits.
It cannot check `basis` when the target is not a numbered section; for those arrows the label is the extractor's judgement.
It checks that a `yes` quotation names a receiver, television, broadcasting apparatus or TVRO, not that it ties the node to the path; the `why` column says how it does.

The numbers it prints for the files as delivered are in the last section.

## On the television path

`on_tv_path` is one of `yes`, `not-decided` and `no`.
`yes` means `tv-path.tsv` holds a quotation from a deposited text that names a television receiver, a sound receiver, broadcasting apparatus, or the licence for one, and the `why` column says how that quotation ties the node to the graph.
`not-decided` means no such quotation was found, so the node is neither shown to be on the path nor shown to be off it.
`no` would mean a quotation shows the node to be off the path; no node has it.
The value records what the texts name, and says nothing about whether a licence is needed.
The page that reads this graph styles `not-decided` nodes differently from `yes` nodes.

There are 22 `yes` nodes and 12 `not-decided` nodes.
The `not-decided` nodes, with the reason held in `tv-path.tsv`, are:

- `TA_s85` (Telecommunications Act s 85): Its own words name no receiver or apparatus; the arrows to it are an amendment about a further fine (E15) and a by-description arrow from section 95 (E25).
- `TA_s98_2` (Telecommunications Act s 98(2)): Its own words name no instrument and no receiver; its arrows (E21, E22) are by description.
- `TA_O3` (TAS-era Order O 3): Its text has no hit for television, broadcast, radio or receiver; it exempts from a section of the Telecommunication Authority of Singapore Act whose text is not deposited.
- `TA_Rg7` (Dealers Regulations (Rg 7)): Its text has no hit for television or broadcast; its one hit for receiver is the item Scanning Receivers in the First Schedule (TA1999-DEAL99.txt:654), and no deposited line says whether its lists reach television or sound receivers.
- `BA_s65` (Broadcasting Act s 65): Its own words name no apparatus; it lets the Minister amend the First, Second or Third Schedule and is on the graph as the power S 549/2012 names.
- `BA_s66` (Broadcasting Act s 66): Its own words name no apparatus; it is the power to make regulations that Rg 1, S 333/2004, S 548/2012 and the TVRO regulations name.
- `TA_S185_2003` (Dealers Regulations 2003 (Rg 6)): It is on the graph only because it revokes Rg 7; its one hit for receiver is the item Scanning Receivers (TA1999-RG6-S185-2003.txt:674).
- `TA_S251_2013` (S 251/2013 amending Rg 6): Its item 3 names integrated receiver decoder devices for second generation digital terrestrial television (TA1999-RG6-S251-2013.txt:163-168), but it amends the Dealers Regulations 2003, a not-decided node, and names no specification.
- `TAS_s30` (TAS Act s 30(1)-(5)): The text of the Telecommunication Authority of Singapore Act is not deposited.
- `TAS_s130` (TAS Act s 130): The text of the Telecommunication Authority of Singapore Act is not deposited.
- `TAS_s131` (TAS Act s 131): The text of the Telecommunication Authority of Singapore Act is not deposited.
- `TA_s96` (Telecommunications Act s 96): Its own words give the Minister a power to exempt and name no receiver; it is on the graph as the power that N 1 and S 588/2023 name.

Two `yes` values rest on another text.
The words of Telecommunications Act sections 54 and 55 name telecommunication equipment and radio-communication equipment and no receiver (TA1999.txt:4896-4916), so `TA_s54` and `TA_s55` are `yes` only because Notification N 1 exempts sections 34(1)(b) and 35 of the 2000 Revised Edition, now 54(1)(b) and 55, in respect of the equipment in its Schedule, and that Schedule lists "(e) TV Receivers and Radio Systems" (E43, E44).
That sub-item sits under item 11, headed Remote Control Devices (TA1999-N1-S115-2001.txt:117-126), and the deposited texts say no more about what (e) covers.

## The scope list, one line each

"On the path: yes" and "not decided" are the `on_tv_path` values; "not on the path" is used only for the one item that is not drawn.

- Telecommunications Act s 54: on the path: yes, through N 1 (E43) and the whole-Act words of s 95 (E23); arrows E23, E43.
- Telecommunications Act s 55: on the path: yes, through N 1 (E44) and E24; arrows E24, E44.
- Telecommunications Act s 85: on the path: not decided; arrows E15, E25.
- Telecommunications Act s 95: on the path: yes; arrows E14, E23 to E25, E34.
- Telecommunications Act s 98(2): on the path: not decided; it speaks of "telecommunication matters" (TA1999.txt:7098), and its drawn arrows (E21, E22) go only to the Order O 3 and the Dealers Regulations (Rg 7).
- Broadcasting Act s 2(1): on the path: yes; arrows E27, E29, E35.
- Broadcasting Act s 20: on the path: yes; arrows E29 to E34, E41.
- Broadcasting Act s 47: on the path: yes; arrows E30.
- Broadcasting Act First Schedule: on the path: yes; arrows E19, E27.
- Television and Radio Licensing Regulations (Rg 1): on the path: yes; arrows E01, E08 to E13, E17, E20, E31, E38, E39, E48 to E56.
- S 333/2004: on the path: yes; arrows E02, E08 to E13, E32, E48 to E56.
- S 548/2012: on the path: yes; arrows E03, E17, E20, E33.
- S 549/2012: on the path: yes; arrows E04, E19.
- Broadcasting (TVRO System) Regulations (Rg 3): on the path: yes; arrows E05, E37, E40; the regulations define a licence as "a licence to install or operate one or more TVRO systems" (BA1994-RG3.txt:8).
- Order O 3: on the path: not decided; arrows E06, E21, E26, E28, E36; its words are "All persons shall be exempted from section 30 (1) to (5) of the Act in respect of" (TA1999-O3-S549-1998.txt:30-31), the Act being the Telecommunication Authority of Singapore Act, whose text is not deposited, and the Order and its 1999 Revised Edition contain none of the words television, broadcast, radio or receiver.
- Dealers Regulations (Rg 7) that O 3 points at: on the path: not decided; arrows E07, E18, E22, E28, E36; the text has no hit for television or broadcast, its hits for radio are "radio-communication" and, in the fee schedules, Radio Pager, Trunked Radio Transceiver and Amateur Radio Transceiver, it has one hit for receiver ("1. Scanning Receivers.", TA1999-DEAL99.txt:654, in the First Schedule), and its Fifth Schedule ends with the item "Other equipment as determined by the Authority" (TA1999-DEAL99.txt:859).
- IMDA TS DVB-T2 IRD: not on the path; see the next section.

Three of the `not-decided` scope items (section 98(2), O 3 and Rg 7) are drawn because the scope list names them and no quotation shows them to be outside the path.
With the five nodes that hang off them (`TA_S185_2003`, `TA_S251_2013`, `TAS_s30`, `TAS_s130` and `TAS_s131`) they form a group of 8 nodes, joined to the rest of the graph by no cited arrow.
To drop the group, delete nodes `TA_s98_2`, `TA_O3`, `TA_Rg7`, `TA_S185_2003`, `TA_S251_2013`, `TAS_s30`, `TAS_s130`, `TAS_s131`, edges E06, E07, E18, E21, E22, E26, E28, E36, E61, and rows U04 and U09 of `edges-uncited.tsv`.
That leaves 26 nodes and 51 edges.

## Not on the path

The technical specification named "IMDA TS DVB-T2 IRD" is not drawn, because no deposited text refers to it.
The words "DVB" and "IMDA TS" and the whole word "IRD" have no hit in any of the 711 deposited texts, including all 171 texts named `BA1994*.txt` or `TA1999*.txt`.
The specification itself is in no deposited text; the counts for "DVB", "IMDA TS" and "IRD" are in "What was searched".
Outside the deposits, the independent review read two IMDA documents about the specification: a draft of it (Issue 1, Revision 2) and IMDA's decision paper on it.
They are guidance, not legislation, and they are not deposited here; their URLs, retrieval times and sha256 are recorded in `../../../../telecommunications-act-1999/encodings/legalese-sonnet-5.5/review/README.md`.
No arrow in this graph rests on them.
The nearest deposited text is item 3 of the Fifth Schedule to the Dealers Regulations 2003, inserted by S 251/2013; its first-column words, read down TA1999-RG6-S251-2013.txt:163-168, are "Integrated receiver decoder devices intended for use with second generation digital terrestrial television broadcasting system".
That item names no specification.
It is drawn as E61, an `amends` edge from S 251/2013 to the Dealers Regulations 2003 (`TA_S185_2003`), and both nodes are `not-decided`.
E61 is the nearest text to the specification and nothing more: no deposited text says that the specification applies to those devices or to any other.
The row `U07` in `edges-uncited.tsv` records that no deposited text names the specification.

## Date gaps

These dates are not stated by any deposited line, so the cell is empty.

- The date of assent to the Broadcasting Act (Act 15 of 1994, originally the Singapore Broadcasting Authority Act 1994): the legislative history gives readings on 25 July and 26 August 1994 and commencement on 1 October 1994 (BA1994.txt:4498-4506), not assent.
- The date of assent to the Telecommunications Act 1999 (Act 43 of 1999): the history gives readings and commencement on 1 December 1999 (TA1999.txt:7113-7125), not assent; the node `TA_Act` carries only the commencement.
- The day the current words of each Broadcasting Act and Telecommunications Act section, and of the Broadcasting Act First Schedule, began: every section row and the First Schedule row have empty `made`, `published` and `in_force`.
- The day Rg 1 was made and first published (G.N. S 21/80), the day the TVRO regulations were (G.N. S 126/1991), and the day the Dealers Regulations (Rg 7) were (G.N. S 327/94): none of the as-made texts is deposited.
- The first publication date of the 2004 Revised Edition of Rg 1 and of Rg 3, and of the 1999 Revised Edition of Rg 7: the editions print an edition date but not a first-publication line.
- Any revocation of the Order O 3: no deposited text revokes it; the Gazette's subject index to subsidiary legislation enacted before 1 June 2010 lists it (TA1999-AID-INDEX2010.txt:9717-9720), and the index is an aid, not an instrument.
- Any revocation of Notification N 1: a search for its title near the word "revoked" or "revokes" found no hit in the deposits, and S 588/2023 amends it.
- Any amendment or revocation of the TVRO regulations after 2004: the deposited text ends "[G.N. Nos. S 126/91; S 354/2001]" (BA1994-RG3.txt:49) and says nothing later.
- The dates of the Telecommunication Authority of Singapore Act and of its repeal: its text is not deposited, and the Telecommunications Act calls it the "repealed Act" without a date (TA1999.txt:459-462).

## Nodes added for an arrow

Eighteen nodes are outside the scope list and were added because they sit on a cited arrow; each row says which edge in `added_for_arrow`.

- `BA_s66` (E01) is the power to make regulations that Rg 1, S 333/2004, S 548/2012 and the TVRO regulations name.
- `BA_s65` (E04) is the power to amend the Schedules that S 549/2012 names.
- `BA_s21` (E37) is the section the TVRO regulations cite; it applies sections 10, 12 and 16 to broadcasting apparatus licences.
- `TA_s2` (E35) is where the Telecommunications Act gives broadcasting apparatus the meaning the Broadcasting Act gives it.
- `TA_Act` (E38) is the Telecommunications Act as a whole, cited by Rg 1 without a section number.
- `TA_Act10_2005` (E14) is the amending Act that changed sections 2, 65 (now 85) and 72 (now 95).
- `TA_S185_2003` (E18) is the Dealers Regulations 2003, which revoke Rg 7.
- `TA_S251_2013` (E61) is the 2013 amendment of the Dealers Regulations 2003 that inserts an item for integrated receiver decoder devices into their Fifth Schedule.
- `BA_S354_2001` (E40) is the 2001 amendment of the TVRO regulations, which substituted the regulation whose paragraph (2) E37 quotes; its own text gives the Act's section numbers differently from the 2004 Revised Edition.
- `TAS_s30` (E26), `TAS_s130` (E06) and `TAS_s131` (E07) are sections of the Telecommunication Authority of Singapore Act, named by the Order O 3 and the Dealers Regulations (Rg 7); the Act's text is not deposited.
- `TA_s96` (E42) is the Telecommunications Act section that N 1 and S 588/2023 say they are made under (section 73 in the 2000 Revised Edition).
- `TA_N1` (E43) is the Notification that exempts from sections 34(1)(b) and 35 of the 2000 Revised Edition, now 54(1)(b) and 55, two scope sections.
- `TA_S588_2023` (E46) is the 2023 Notification that renames the sections N 1 exempts from as 53, 54(1)(b) and 55 and replaces the part of N 1's Schedule that holds item 11.
- `TA_S525_2001` (E58), `TA_S1_2008` (E59) and `TA_S726_2014` (E60) are the three other notifications that substitute N 1's Schedule or its item 11.

## Which paragraphs and which amendments are drawn

S 333/2004 has 23 numbered paragraphs: paragraph 1 is its citation and paragraphs 2 to 23 each amend Rg 1 (BA1994-S333-2004.txt:21-248).
A paragraph is drawn when its own text contains the word "receiver" or the word "licence" (counted case-insensitively, as a substring, in the lines of the paragraph), or when it amends a regulation that another edge quotes.
Fifteen paragraphs are drawn, with the counts of "receiver" and "licence" in each:

- Paragraph 2 amends regulation 2 (E08; receiver 4, licence 2).
- Paragraph 4 amends regulation 5 (E48; receiver 0, licence 5).
- Paragraph 5 amends regulation 6 (E49; receiver 2, licence 0).
- Paragraph 6 amends regulation 7 (E09; receiver 0, licence 0), and is drawn because E31 quotes regulation 7.
- Paragraph 7 amends regulation 8 (E50; receiver 2, licence 0).
- Paragraph 10 replaces regulations 16 to 22 with a new regulation 16 (E51; receiver 0, licence 2).
- Paragraph 11 amends regulation 23 (E10; receiver 2, licence 3).
- Paragraph 12 amends regulation 27 (E11; receiver 1, licence 1).
- Paragraph 13 amends regulation 28 (E12; receiver 2, licence 0).
- Paragraph 14 inserts regulation 29A (E13; receiver 3, licence 2).
- Paragraph 15 amends regulation 31 (E52; receiver 1, licence 0).
- Paragraph 17 replaces regulation 33 (E53; receiver 2, licence 2).
- Paragraph 18 replaces the heading to Part VI (E54; receiver 1, licence 1).
- Paragraph 19 replaces regulation 36 (E55; receiver 2, licence 3).
- Paragraph 23 replaces the Second Schedule (E56; receiver 3, licence 4).

Seven are not drawn:

| paragraph | what it amends | why it is not drawn |
| --- | --- | --- |
| 3 | deletes regulations 3 and 4 | its text contains neither word |
| 8 | deletes regulations 12 and 14 | its text contains neither word |
| 9 | replaces regulation 15 with a regulation on information to be furnished to the Authority | its text contains neither word |
| 16 | deletes paragraph (3) of regulation 32 | its text contains neither word |
| 20 | replaces the words "or hospital" in regulation 37(1) with ", hospital or commercial property" | its text contains neither word (receiver 0, licence 0) |
| 21 | deletes regulation 38 | its text contains neither word |
| 22 | replaces "licensing authority" with "Authority" in a list of regulations and in the heading of regulation 37 | its text contains neither word ("licensing" is not "licence") |

The rule for an amending instrument other than S 333/2004 is that it is drawn when its arrow reaches a node of the scope list, or a node whose `on_tv_path` is `yes`, and its own text names a receiver, broadcasting apparatus or the licence for one.
S 588/2023 passes both tests: it amends N 1, and its renumbering words name sections 54(1)(b) and 55, which are scope nodes.
S 251/2013 is drawn as an exception: it passes the second test only, and it is the nearest deposited text to the specification named in the scope list (see "Not on the path").
The edge id E57 is not used; edge ids were kept stable when an edge was removed.

## Notification N 1 and its Schedule

N 1 was first published with a Schedule whose item 11 is headed Remote Control Devices and lists sub-item (e) TV Receivers and Radio Systems (TA1999-N1-S115-2001.txt:117-126).
Four later notifications substitute the Schedule or the item, and each is drawn.
This list gives the day each says it comes into operation, in that order, and what it substitutes; it records what the texts say they do and states no more.

- S 115/2001: first publishes the Schedule, with item 11 at TA1999-N1-S115-2001.txt:117-126, from 2001-03-02 (first published 2001-03-02 17:00 SGT).
- S 525/2001: deletes the Schedule and substitutes a new one, with item 11 at TA1999-N1-S525-2001.txt:106-119, from 2001-10-17 (first published 2001-10-17 17:00 SGT).
- S 1/2008: deletes item 11 and substitutes a new item 11 (TA1999-N1-S1-2008.txt:61-70), from 2008-01-02 (first published 2008-01-02 17:00 SGT).
- S 726/2014: deletes the Schedule and substitutes a First and a Second Schedule, with item 11 in the First (TA1999-N1-S726-2014.txt:140-162), from 2014-11-01 (first published 2014-10-31 17:00 SGT).
- S 588/2023: replaces items 8 to 15 of the First Schedule (TA1999-N1-S588-2023.txt:81), with item 11 at TA1999-N1-S588-2023.txt:108-122, from 2023-09-01 (first published 2023-08-28 17:00 SGT).

Seven other notifications (S 591/2003, S 651/2004, S 265/2006, S 179/2011, S 252/2013, S 415/2014 and S 78/2017) change other items and are not drawn.

## Renumbering used

The 2020 Revised Edition of the Telecommunications Act was renumbered.
The printed edition has a Comparative Table headed "2020 Ed." and "2000 Ed." (TA1999.RevEd2020-printed.txt:5714), introduced by "This Act has undergone renumbering in the 2020 Revised Edition" (TA1999.RevEd2020-printed.txt:5710).
Each row below is one line of that table, checked by `check-graph.py`; the first number is the 2020 section and the second is the 2000 section.
Elsewhere the table lists subsection rows under a section (for example `(5) (3B)` under section 5, TA1999.RevEd2020-printed.txt:5716), and these seven rows are followed by none.

| 2020 | 2000 | line of TA1999.RevEd2020-printed.txt | row as printed |
| --- | --- | --- | --- |
| 53 | 33 | `TA1999.RevEd2020-printed.txt:5850` | 53 33 |
| 54 | 34 | `TA1999.RevEd2020-printed.txt:5851` | 54 34 |
| 55 | 35 | `TA1999.RevEd2020-printed.txt:5852` | 55 35 |
| 85 | 65 | `TA1999.RevEd2020-printed.txt:5901` | 85 65 |
| 95 | 72 | `TA1999.RevEd2020-printed.txt:5911` | 95 72 |
| 96 | 73 | `TA1999.RevEd2020-printed.txt:5912` | 96 73 |
| 98 | 75 | `TA1999.RevEd2020-printed.txt:5914` | 98 75 |

S 588/2023 states the same mapping for sections 33, 34(1)(b) and 35 in its own words (TA1999-N1-S588-2023.txt:29-30).
Section 2 has no row in the table, whose first row is `5—(4) 5—(3A)` (TA1999.RevEd2020-printed.txt:5715); no gloss says "then section 2", and the identification of the two section 2s rests on the definition that Act 10 of 2005 inserts (TA1999.ACT10-2005.txt:42-47) and the definition of the same terms in the 2020 text (TA1999.txt:275-276), which give them the same meaning in different words.
The old numbers are used in E14 (72), E15 (65), E42 (73), E43 (34), E44 (35), E46 (33, 34, 35), in the quotations of E14, E15, E42, E43 and E44, and in the notes of the section nodes.

## Named and by-description arrows

`basis` is `named` when the quotation names the other end by a number (a section, regulation, Schedule or item), by the title or citation of the instrument, or by a short name that the same instrument gives it, such as "the principal Regulations" or "the revoked Regulations".
`basis` is `by-description` when the quotation does not name the other end and the link rests on what the words describe.
The page that reads this graph draws `by-description` arrows dashed.
There are 52 `named` arrows and 8 `by-description` arrows.

The `by-description` arrows are these.

- E21 and E22: section 98(2) names no instrument; it describes subsidiary legislation made under the repealed Act and in force just before 1 December 1999; the header of O 3 names the Telecommunication Authority of Singapore Act (TA1999-O3-S549-1998.txt:8-10 and :20-22), the header of Rg 7 names it too (TA1999-DEAL99.txt:35-37), and the Telecommunications Act calls that Act the "repealed Act" (TA1999.txt:459-462).
- E23, E24 and E25: section 95 says "This Act", so its words reach every section; the edges are drawn to scope sections 54, 55 and 85 and not to 98(2).
- E34: section 95 says "the licensing of ... broadcasting apparatus under the Broadcasting Act 1994" with no section number; the target is section 20 because that is the section headed "Licensing of broadcasting apparatus" (BA1994.txt:1423).
- E35: the Telecommunications Act names the Broadcasting Act, not section 2(1); the target is section 2(1) because that is where "broadcasting apparatus" is defined.
- E41: section 21 says "broadcasting apparatus licences" without naming section 20; the target is section 20 because section 2(1) defines a broadcasting apparatus licence as a licence granted under section 20 (BA1994.txt:281-284, quoted at E29).

E38 and E39 point at the whole Telecommunications Act and are `named`, because the words "ship station licence ... under the Telecommunications Act" fit none of the scope sections, whereas E34 and E35 point at a scope section because the words describe what that section is about.
E20 is `named` because its quotation, "the revoked Regulations", is the short name that S 548/2012 itself gives Rg 1 (E17).

## Seen and not drawn

Each item below names a scope node or sits beside one.
The test applied to each is whether its arrow reaches a node of the scope list or a `yes` node, and whether its own text names a receiver, broadcasting apparatus or the licence for one.
An item that passes both is drawn; an item that fails either is listed here with the reason.

Promoted to the graph:

- Notification N 1 (`TA_N1`): its arrows reach sections 54 and 55 of the scope list (E43, E44) and its Schedule names "(e) TV Receivers and Radio Systems" (TA1999-N1-S115-2001.txt:125-126).
- S 525/2001, S 1/2008 and S 726/2014 (`TA_S525_2001`, `TA_S1_2008`, `TA_S726_2014`): each amends N 1, which is a `yes` node, and each names "(e) TV Receivers/ Radio Systems" in the Schedule or item it substitutes (E58 to E60).
- S 251/2013 (`TA_S251_2013`, `not-decided`): the exception described above (E61).
- S 588/2023 (`TA_S588_2023`): it amends N 1 (E46, E47), its renumbering words name sections 54(1)(b) and 55, which are scope nodes, and its text names "(e) TV Receivers/ Radio Systems" (TA1999-N1-S588-2023.txt:121-122).
- Telecommunications Act section 96 (`TA_s96`): it is the power that N 1 and S 588/2023 name (E42, E45); its own words name no receiver, so it is `not-decided`.
- The nine further S 333/2004 paragraphs listed above (E48 to E56), and the three Schedule-changing notifications of N 1 (E58 to E60).

Kept out:

- The other notifications that amend N 1 (S 591/2003, S 651/2004, S 265/2006, S 179/2011, S 252/2013, S 415/2014, S 78/2017) change other items of its Schedule, and none changes item 11 (TA1999-N1-S591-2003.txt:20-25, TA1999-N1-S651-2004.txt:18-19, TA1999-N1-S265-2006.txt:22-42, TA1999-N1-S179-2011.txt:22-30, TA1999-N1-S252-2013.txt:24-34, TA1999-N1-S415-2014.txt:24-26, TA1999-N1-S78-2017.txt:28-30).
- The 1999 Revised Edition of the Radio-communication Regulations (TA1999-RADIO99.txt, headed "Telecommunication Authority of Singapore Act (Chapter 323) Radio-communication Regulations") has the same sub-item, "(e) TV Receivers/ Radio Systems", in its First Schedule (TA1999-RADIO99.txt:1135-1144); it is made under the Act that the Telecommunications Act calls the "repealed Act" (TA1999.txt:459-462), and no deposited line names it in connection with a node of the scope list, since section 98(2) describes such instruments without naming any, so it is not drawn.
- Telecommunications Act section 56, headed "Exemption from sections 53, 54 and 55" (TA1999.txt:4933-4947): its arrow would reach sections 54 and 55, but its words name telecommunication equipment licensed in a country that is party to a treaty and no receiver.
- The Broadcasting (Composition of Offences) Regulations name section 47: "The offence under section 47 of the Act may be compounded by the Authority in accordance with section 57 (1) of the Act." (BA1994-RG2.txt:5); the text has no hit for receiver, apparatus or licence, and its only hits for broadcast are in its title.
- Act 22 of 2016, section 93, amends other definitions in Broadcasting Act section 2(1) (TA1999.ACT22-2016.txt:3201-3223) and repeals section 67 (TA1999.ACT22-2016.txt:3242); its text there has no hit for apparatus or receiver.
- Act 38 of 2022 (BA1994-ACT38-2022.txt, deposited while this graph was being built) inserts definitions into Broadcasting Act section 2(1) (BA1994-ACT38-2022.txt:52-55); it has no hit for receiver and one for apparatus, the anchor words "broadcasting apparatus," of its amendment to the long title (BA1994-ACT38-2022.txt:47-50).
- S 212/1999 amends regulation 8 of Rg 1 (BA1994-S212-1999.txt:26-31); the text has no hit for receiver, apparatus or licence.
- S 362/2001 amends regulations 15 and 32 and the First Schedule of Rg 7, with regulation 4(a) deemed from 21 January 2000 and first published on 30 July 2001 (TA1999-DEAL99-S362-2001.txt:3 and :25-26); its hits for licence are the Dealer's Individual Licence (TA1999-DEAL99-S362-2001.txt:32-36), and it has no hit for receiver.
- The other nine amending instruments of the Dealers Regulations 2003 (S 48/2004, S 593/2004, S 478/2005, S 396/2007, S 210/2010, S 178/2011, S 414/2014, S 725/2014 and S 589/2023) have no hit for receiver, television or broadcast, and are not drawn.
- Broadcasting Act section 21 names sections 10, 12 and 16 (BA1994.txt:1457), which are not in the scope list.
- The Broadcasting (Amendment) Act 2004 (BA1994-ACT55-2004.txt:43-45) and its commencement notification (BA1994-S750-2004.txt:23-24) concern sections 48 and 48A only; its two hits for apparatus are the definition of a decoder (BA1994-ACT55-2004.txt:67-70).
- The Criminal Procedure Code 2010 amends Broadcasting Act section 55 only (BA1994-ACT15-2010.txt:13743-13747).
- The Statutes (Miscellaneous Amendments) Act 2008 amends Broadcasting Act section 8 (BA1994-ACT4-2008.txt:84-89), and S 738/2024 replaces the Fourth Schedule (BA1994-S738-2024.txt:24); neither is a scope node.
- The commencement notifications S 250/2022, S 29/2023, S 244/2024, S 128/2008 and S 129/2008 have no hit for any of the scope terms.

Nine of the Broadcasting Act deposits (Act 38/2022, Act 4/2008, S 738/2024, S 250/2022, S 29/2023, S 244/2024, S 128/2008, S 129/2008 and the edition `BA1994.20211231.txt`) were added to the folders while this graph was being built; they take the Broadcasting Act family from 39 to 48 texts and the deposits from 702 to 711.
The edition `BA1994.20211231.txt` is a further consolidation of the Act whose sections 2, 20, 47 and First Schedule are those of `BA1994.txt`; it was not used as a source of any quotation.

## What was searched

Searches ran over whitespace-collapsed text of the deposits, counting hits per file.
The Broadcasting Act family is the 48 texts named `BA1994*.txt`; the Telecommunications Act family is the 123 texts named `TA1999*.txt`; "all" is the 711 texts under `subjects/sg/*/registers/source-bundle/`.

| term | Broadcasting family (48 files) | Telecommunications family (123 files) | all (711 files) |
| --- | --- | --- | --- |
| `DVB` | 0 | 0 | 0 |
| `IMDA TS` | 0 | 0 | 0 |
| whole word `IRD` | 0 | 0 | 0 |
| `integrated receiver` (any case) | 0 | 1 hit in 1 file | 1 hit in 1 file |
| `section 20(4)` | 0 | 0 | 11 hits in 6 files, all read, none about the Broadcasting Act |
| `section 20` | 23 hits in 9 files, all read | 17 hits in 7 files, not read one by one | 767 hits in 185 files, not read |
| `section 47` | 3 hits in 2 files, all read | 5 hits in 4 files, not read one by one | 341 hits in 102 files, not read |
| `S 333/2004` or `S 333/04` | 7 hits in 1 file (itself) | 0 | 7 hits in 1 file |
| `S 548/2012` | 2 hits in 1 file (itself) | 0 | 2 hits in 1 file |
| `S 549/2012` | 3 hits in 3 files (itself, the Act's history in BA1994.txt:4645, and the history in BA1994.20211231.txt:2197) | 0 | 3 hits in 3 files |
| `Television and Radio Licensing` | 5 hits in 3 files (Rg 1, S 333/2004, S 548/2012) | 7 hits in 1 file (the 2010 index) | 12 hits in 4 files |
| `TVRO` | 40 hits in 9 files | 4 hits in 1 file (the 2010 index) | 44 hits in 10 files |
| `Specified Equipment` | 0 | 4 hits in 3 files (the two O 3 texts, three hits, and the 2010 index) | 4 hits in 3 files |
| `TV Receiver` (singular or plural, whitespace collapsed) | 0 | 9 hits in 9 files (the N 1 family and the 1999 Radio-communication Regulations) | 9 hits in 9 files |
| `Remote Control Devices` | 0 | 12 hits in 10 files | 12 hits in 10 files |

Results that matter:

- The word "apparatus" occurs in eleven Broadcasting-family deposits: the four Act texts, Act 55 of 2004, S 549/2012, S 333/2004, Rg 1, the TVRO regulations, S 354/2001 and Act 38 of 2022; no class-licence notification, exemption order or other instrument in that family contains it.
- No deposit cites Broadcasting Act section 20(4), the Authority's power to exempt a person or class of apparatus (BA1994.txt:1451-1452), so no instrument is drawn as made under it.
- The nine Broadcasting-family files with a hit for `section 20` are the four Act texts (two each), S 333/2004, Rg 1, S 548/2012, the Criminal Procedure Code 2010 (eleven hits) and the Statutes (Miscellaneous Amendments) Act 2008 (one hit, about the Interpretation Act); the hits in the Act texts and the three instruments are the edges E29 to E33, and the eleven hits in the Code belong to the Code's own section 20, the Coroners Act 2010 and other Acts, while its only entry under the Broadcasting Act amends section 55 (BA1994-ACT15-2010.txt:13743-13747).
- The Broadcasting-family hits for `section 47` are all outside the Act texts: the Composition of Offences Regulations and two in the Criminal Procedure Code 2010 about that Code's own section 47.
- The thirteen Acts listed in the legislative history of the Telecommunications Act (TA1999.txt:7107 onwards), each deposited (Acts 10 of 2005, 19 of 2011, 22 of 2016, 30 of 2016, 15 of 2017, 26 of 2018, 40 of 2018, 15 of 2019, 12 of 2020, 4 of 2021, 25 of 2021, 31 of 2022 and 13 of 2026) were searched for amendments to the 2000-numbered sections 34, 35, 65, 72 and 75; only Act 10 of 2005 matched (sections 65 and 72), and reading it also found its section 2.
- Three more of those Acts have an "Amendment of Telecommunications Act" heading and were read: Act 15 of 2019 amends sections 45 and 60(3) (TA1999.ACT15-2019.txt:6981-6985), Act 40 of 2018 amends sections 32I, 32J and 32L (TA1999.ACT40-2018.txt:20194-20212), and Act 26 of 2018 amends section 58 (TA1999.ACT26-2018.txt:2794-2805), all in 2000 numbering.
- The 2020 consolidation marks sections 85 and 95 with `[10/2005]` (TA1999.txt:5952 and :6996) and shows no amendment marker for sections 54, 55 or 98 (TA1999.txt:4894-4931 and :7088-7104).
- Every Broadcasting Act mention in the other deposited Telecommunications amending texts (Acts 19 of 2011, 26 of 2018, 30 of 2016, 31 of 2022, 13 of 2026 and S 26/2022) was read in context; none touches a scope node.
- The N 1 family has twelve notifications (S 115/2001, S 525/2001, S 591/2003, S 651/2004, S 265/2006, S 1/2008, S 179/2011, S 252/2013, S 415/2014, S 726/2014, S 78/2017 and S 588/2023) and the 2002 Revised Edition; eleven of the twelve name section 73 of the Telecommunications Act as their power (the phrase is in 18 N 1 files, counting Gazette copies, and in one other file, TA1999-RESELL-S77-2007.txt), and S 588/2023 names section 96.
- A search of all the deposits for the title of N 1 within 200 characters of the word "revoked" or "revokes" found no hit.

## Numbers printed by check-graph.py

The numbers below are the output of `python3 -I check-graph.py` on the files as delivered.

```
nodes: 34
edges: 60
edges per kind: amends=25, carves-out=6, cites=12, defines-by-list=2, made-under=9, replaces=1, revokes=2, saves=3
nodes added for an arrow: 18
nodes by on_tv_path: no=0, not-decided=12, yes=22
edges by basis: by-description=8, named=52
renumbering rows: 7
nodes with no edge: 0 []
uncited rows: 9
problems: 0
```

This graph records references between texts; it states no answer to the question.
