# NOTES -- Soldatenarbeitszeitverordnung §§ 5(2), 6(1) and 12 (the ordinary working-time regime) under the 2025 amendment and without it, with the citation test of Art. 80(1) sentence 3 GG; L4 encoding by one Opus agent working alone

This encodes three provisions of the Soldiers' Working Time Regulation (SAZV) that Art. 5 of the Regulation of 6 March 2025 (BGBl. 2025 I Nr. 78) changed: § 5(2) (Art. 5 No. 1: how the regular weekly working time is distributed over the days of the week), § 6(1) (Art. 5 No. 3: the 13-hour limit on the regular daily working time and when it may be exceeded) and § 12 (Art. 5 No. 4: compensation for on-call duty, Rufbereitschaft).
Each is answered under two readings: **as printed**, the 2025 wording; and **if the 2025 amendment is void**, the wording it replaced.
It also encodes the citation test of Grundgesetz Art. 80(1) sentence 3 for those three instructions: they rest on SG § 30c(5) sentence 1 no. 1 (regular working time), and the 2025 preamble cites, of § 30c(5), only sentence 1 no. 2.
It decides nothing about whether the instructions are void: one input, `an exception to the citation requirement applies`, carries that judgment (fork F1).
This candidate is weaker than the annex case the sibling encoding treats, for the reason given in finding 4.

The point comes from the sibling encoding's NOTES.md, finding 7(b) (`../legalese-sonnet-5.5/NOTES.md`), which a blind check also raised.
The sources are in `../../registers/source-bundle/`.
The 2025 wording is the consolidated text of gesetze-im-internet.de read on 2026-11-02 (`sazv-5`, `sazv-6`, `sazv-12`) and the gazette (`bgbl-2025-i-78`).
The earlier wording is three new deposits, `sazv-5-before-2025`, `sazv-6-before-2025` and `sazv-12-before-2025`: transcriptions of buzer.de's comparison pages, an aid and not authoritative, because the 2015 gazette (BGBl. I S. 1995) was not read.
Where the 2025 gazette's own instruction determines the earlier words (a struck phrase, an insertion), the transcription agrees with it; where the instruction replaces a sentence without quoting it, the earlier words rest on buzer alone (Method).
The target is `main`; the build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02).
Modules: `sazwt-law.l4` (the law layer), `sazwt-seat.l4` (the seat), `sazwt-tests.l4` and `sazwt-cases-seat.l4`.

## Seat

The seat is **a soldier serving within the remit of the Federal Ministry of Defence**, to whom SAZV § 1(1) applies.
Four things are assumed of the seat, not asked:

- the soldier serves within the Ministry's remit (SAZV § 1(1));
- the soldier is not posted, for international or supranational tasks, to an establishment in the annex to SAZV § 1(2) (the sibling encoding's subject);
- the work in question is not an activity listed in SG § 30c(4), which takes subsections (1) to (3) away;
- the soldier is below pay grade B 6, so SAZV § 19(1), which lifts "die Regelungen dieses Abschnitts zur regelmäßigen wöchentlichen Arbeitszeit" and others for B 6 and above in listed posts (`sazv-19.txt:2`), does not arise.
  Which Abschnitt § 19 sits in was not checked.

The questions, in `sazwt-seat.l4`, under `§` groups, each asked once per reading:

- Over which days of the week may my regular weekly working time be distributed? (§ 5(2) sentences 1 and 2)
- If I apply, may an individual distribution of my weekly hours over Monday to Friday be approved? (§ 5(2) sentence 3)
- Is the regular daily working time fixed for me today allowed, and on which ground may it exceed 13 hours? (§ 6(1))
- How many hours of compensation am I owed for this month's on-call duty, and in what form? (§ 12)
- Does the 2025 preamble cite the power these changes rest on, and does it name § 93(2) no. 6? (Art. 80(1) sentence 3 GG)

Each question "if the 2025 amendment is void" takes, last, `an exception applies`: false gives the earlier wording, true the 2025 wording.
The inputs are facts the soldier can state: the part-time reduction in percent, the hours fixed for the day, the area of service, what has happened, the on-call hours and the hours actually called on, the working-time arrangement.
Three inputs are judgments that belong to the soldier's superiors, asked conditionally: whether service reasons call for a departure from Monday to Friday or for more than 13 hours, whether service reasons stand against an individual distribution, and how many hours of compensation compelling service reasons stand against.
Three are characterisations asked as facts: whether an extraordinary event or an accident is behind the day's work, whether it leads to an excessive workload that could not be foreseen, and whether the activity is one in which the continuity of the service must be ensured.
The Ministry (it makes the Regulation) and the soldier's superiors (they fix the working time and decide on applications) are the other people the text addresses; neither has a seat.

## Method

One agent, working alone, from the deposited sources and the sibling's finding 7(b).
The expected value of every test was written from the German text before any module was run, and every assertion held the first time it ran: 118 on the first run of the suite, and four tests added afterwards for two more areas of service on theirs.
So five deliberate mutations were run on scratch copies as a positive control (Checks run).

The earlier wording was fetched from buzer.de, which keeps earlier versions, on 2026-11-02, with the commons User-Agent, after reading its robots.txt, and converted by a script that keeps buzer's unchanged blocks and its "Text alte Fassung" column and drops its sentence numbers, labels and highlighting (each `.meta.json` says how).
What the gazette determines, checked mechanically against the transcriptions:

- § 5(2) sentence 1: Art. 5 No. 1(a) strikes "mit einer Verkürzung der Arbeitszeit um weniger als 10 Prozent" (`bgbl-2025-i-78.txt:134`); the earlier sentence 1 is the current one with those words after "Teilzeitbeschäftigung", as buzer has it.
- § 12(1) sentence 2: Art. 5 No. 4 inserts ", soweit nicht zwingende dienstliche Gründe entgegenstehen" (`:161-162`); the earlier sentence is the current one without it, as buzer has it.
  The only other change since 2015, Art. 2 No. 5 of BGBl. 2022 I Nr. 34, touched sentence 4 (`bgbl-2022-i-34-flow.txt:225-226`).
- Every other paragraph of the three sections is word for word the current text.

What rests on buzer alone: the earlier § 5(2) sentence 2 ("auf Montag bis Samstag", `sazv-5-before-2025.txt:10`), which Art. 5 No. 1(b) replaces without quoting, and the earlier § 6(1) sentence 3 with its seven-item list (`sazv-6-before-2025.txt:2-9`), which Art. 5 No. 3 recasts without quoting.

`sazwt-law.l4` holds the readings, the facts (three records, one per question's natural unit: the working week, the working day, the calendar month), the rules, and the citation test.
The citation test enumerates the powers the 2025, 2022 and 2015 preambles cite exactly as the sibling's `saz-law.l4` does, with the power these instructions need added: `SG 30c(5) sentence 1 no. 1 with 93(2) no. 6`.
`sazwt-seat.l4` holds no rule: it builds the law layer's records from plain inputs and calls the law layer; fields a question does not read get a fixed placeholder, commented.
Every rule has an `@ref` with locators; `srcrefs.py` checked 85 quote lines and 39 locators, 0 problems, in both `--refs` and `--strict` mode.

## Coverage table

| provision | disposition | where, or why |
|---|---|---|
| SAZV § 5(2) sentence 1, as printed and before 2025 | encoded | `section 5(2) sentence 1 reaches the soldier under the reading` |
| SAZV § 5(2) sentence 2, as printed and before 2025 | encoded | `the days the regular weekly working time may be distributed over under the reading` |
| SAZV § 5(2) sentence 3 (as printed only) | encoded | `an individual distribution over Monday to Friday may be approved on application under the reading`; `NOTHING` before 2025 |
| SAZV § 5(1), (3), (4), (5) | out-of-scope | not changed by the 2025 instructions in question; the length of the week is not asked |
| SAZV § 6(1) sentence 1 | inert | a duty on the superiors to fix the daily working time; the seat takes the hours fixed as an input |
| SAZV § 6(1) sentence 2 | encoded | `the regular daily working time fixed for the day is within section 6(1) under the reading` |
| SAZV § 6(1) sentence 3 as printed (nos. 1 to 3, letters a to i) | encoded | `the ground on which the regular daily working time may exceed 13 hours under the reading` and the lists above it |
| SAZV § 6(1) sentence 3 before 2025 (nos. 1 to 7) | encoded | the same rule, `the areas the list before 2025 names` |
| SAZV § 6(2) | inert | part-time: fixed individually within the limits of (1), which are encoded |
| SAZV § 12(1) sentence 1 | inert | on-call time is not working time: the premise of sentence 2 |
| SAZV § 12(1) sentence 2, as printed and before 2025 | encoded | `the hours of compensation owed for the month's Rufbereitschaft under the reading`, `the months within which the compensation must be given` |
| SAZV § 12(1) sentences 3 and 4 | encoded | `the form of the compensation` |
| SAZV § 12(2) | encoded | `the hours of Rufbereitschaft that count`; sentence 2 defines the input "hours actually called on" |
| SAZV § 1(1), (2) | out-of-scope | seat assumptions; the sibling encoding encodes them |
| SAZV § 19 | out-of-scope | seat assumption (below B 6) |
| SAZV § 5a and the other sections | out-of-scope | not part of the question |
| BGBl. 2025 I Nr. 78, preamble | encoded | `the powers cited in the preamble of the 2025 amending regulation` |
| BGBl. 2025 I Nr. 78, Art. 5 Nos. 1, 3, 4 | encoded | `Instruction of Art. 5`, `the power the instruction rests on`, `the reading to apply to the instruction` |
| BGBl. 2025 I Nr. 78, Art. 5 Nos. 2, 5, 6, 7 and Arts. 1 to 4, 6 | out-of-scope | other amendments (No. 7, the annex, is the sibling's) |
| BGBl. 2025 I Nr. 78, Art. 7(1), (2) | inert | quoted on `Reading`: No. 4 took effect from 1 January 2025 (finding 2); no date is asked |
| BGBl. 2022 I Nr. 34, preamble | encoded | `the powers cited in the preamble of the 2022 amending regulation` |
| SAZV Eingangsformel (2015) | encoded | `the powers cited in the original preamble of the SAZV` |
| SG § 30c(5) sentence 1 no. 1 | encoded | the power the three instructions rest on |
| SG § 30c(5) sentence 1 no. 2 | encoded | as cited, with § 30c(4) and § 93(2) no. 6 |
| SG § 30c(5) sentences 2 to 6 | out-of-scope | data, deletion periods, long-term accounts, leave |
| SG § 30c(4) | inert | seat assumption; nos. 3 and 5 quoted for fork F12 |
| SG § 93(2) no. 6 | encoded | `the cited power names section 93(2) no. 6 of the Soldiers Act` |
| SG § 30d(1) with § 93(2) no. 8 | inert | cited in 2025; raises the maximum average week for § 5a, does not reach §§ 5(2), 6(1), 12 |
| Grundgesetz Art. 80(1) sentence 3 | encoded | `the preamble cites the power`, `the instruction is void for want of citation` |
| BVerfG 2 BvF 3/90 paras. 151 to 158; BVerwG 3 B 51.18 para. 35 | inert | the text for each side of fork F1 |

## Fork register

Each fork gives the readings, the one taken, and the text that licenses each.

**F1. Does citing § 93(2) no. 6 count as citing the whole of § 30c(5)?**
This is the input `an exception to the citation requirement applies`.
Taken: neither; the input decides.
The 2025 preamble cites "§ 30c Absatz 5 Satz 1 Nummer 2 in Verbindung mit Absatz 4 und in Verbindung mit § 93 Absatz 2 Nummer 6" (`bgbl-2025-i-78.txt:38`); the three instructions rest on Nummer 1 (F12).

- *It does, and the 2025 wording stands.*
  § 93(2) no. 6 makes the Ministry the maker of the regulations on "die regelmäßige Arbeitszeit und die Maßnahmen zur Gewährleistung eines bestmöglichen Arbeits- und Gesundheitsschutzes bei besonderen Tätigkeiten nach § 30c Absatz 5" (`sg-93.txt:19`): its words name the subject of sentence 1 no. 1 as well as no. 2, and the preamble cites it whole and records its recast (`bgbl-2025-i-78.txt:43-45`).
  The Ministry made its 2022 working-time changes (to § 5(1) and § 12(1) among others) citing nothing but "§ 93 Absatz 2 Nummer 6 und 7" (`bgbl-2022-i-34-flow.txt:9-13`).
  BVerwG 3 B 51.18 para. 35 reads the requirement by its purpose: subdivisions need not be listed "wenn sie alle in Anspruch genommen werden", and it was enough that the addressee "die vom Verordnungsgeber herangezogenen Rechtsgrundlagen ... erkennen und ihre Einhaltung ... nachprüfen" could (`bverwg-3b51-18-excerpt.txt:7`).
  BVerfG 2 BvF 3/90 para. 156: not every provision needs to say which power it rests on (`bverfg-2bvf3-90-paras-151-158.txt:54-56`).
- *It does not, and the instructions are void.*
  The preamble does not cite § 93(2) no. 6 alone: it joins it to "Satz 1 Nummer 2 in Verbindung mit Absatz 4", and names "Satz 1 Nummer 2" again in its amendment history (`bgbl-2025-i-78.txt:38-40`), so it says which part of § 30c(5) was used.
  A regulation must cite every power it uses, "vollständig" (para. 151, `bverfg-2bvf3-90-paras-151-158.txt:6-9`); the citation must show whether the maker meant to use a power at all (para. 154, `:26-29`), and the power claimed must arise "gerade aus den von ihr selbst angeführten Vorschriften" (`:33-37`); what must be named is "die einzelne Vorschrift des Gesetzes ..., in welcher die Ermächtigung enthalten ist" (para. 157, `:58-60`), which is § 30c(5), where the content, purpose and extent are set; § 93(2) assigns the competence.
  BVerwG 3 B 51.18's relief covers a paragraph named whole whose parts are all used; here the paragraph is named by one part, and not the one used.
  A defect makes the regulation void (para. 158, `:65-71`).

**F2. How far does voidness go?**
(a) The three instructions (Art. 5 Nos. 1, 3, 4), the parts that rest on § 30c(5) sentence 1 no. 1.
Taken.
(b) The whole 2025 regulation, as para. 158 speaks of "die Verordnung" (`bverfg-2bvf3-90-paras-151-158.txt:70-71`).
For these three provisions both give the same answers: the earlier wording.

**F3. Whom does the earlier § 5(2) sentence 2 reach?**
(a) The soldiers sentence 1 reaches, full-time and part-time reduced by less than 10 %: it is the exception to sentence 1's rule.
Taken: for a part-timer reduced by 10 % or more, the earlier § 5(2) gives no answer (`NOTHING`).
(b) Every soldier: the sentence names no group (`sazv-5-before-2025.txt:10`).
On (b), such a part-timer with service reasons would get Monday to Saturday.

**F4. Sundays under the earlier § 5(2).**
(a) Sentence 2 states the whole departure the service may make, "auf Montag bis Samstag".
Taken: `Monday to Saturday`.
(b) "in der Regel" in sentence 1 leaves room for other departures; the text would then answer "at least Monday to Saturday" and say no more.

**F5. "soweit dienstliche Gründe nicht entgegenstehen" in the 2025 § 5(2) sentence 3.**
"Soweit" allows a distribution to be approved in part.
The input asks whether service reasons stand against the distribution applied for, and the answer is yes or no; a partial approval is not modelled.

**F6. "insbesondere in folgenden Bereichen" in the earlier § 6(1) sentence 3.**
(a) The list is illustrative: the only condition is that service reasons require the departure, in any area.
Taken.
(b) The list confines the departure to the named areas and comparable ones.
On (b), an area the list does not name would need a judgment of comparability, and finding 1's § 6 comparison would narrow.

**F7. Letters a to i of the 2025 § 6(1) sentence 3 no. 3.**
(a) An area named there satisfies no. 3 without more: they are the examples "insbesondere" gives of activities in which the continuity of the service must be ensured.
Taken.
(b) The activity must also be one in which continuity must be ensured.
On (b), the named areas would need the continuity input too.

**F8. The relative clause in the 2025 no. 2.**
"außergewöhnlichen Ereignissen sowie im Zusammenhang mit Unfällen, die zu einem übermäßigen, nicht vorhersehbaren Arbeitsanfall führen" (`sazv-6.txt:4`).
(a) "die ... führen" qualifies the events and the accidents.
Taken.
(b) It qualifies only the accidents, so any extraordinary event would do.

**F9. Several grounds at once.**
The first in the text's order is reported (no. 1, then no. 2, then no. 3).
Whether the time is allowed does not depend on which is reported.

**F10. "soweit nicht zwingende dienstliche Gründe entgegenstehen" in the 2025 § 12(1) sentence 2.**
(a) A reduction by the hours of compensation compelling service reasons stand against, as the sibling reads the "soweit" of SG § 30c(2) sentence 5 (its fork F6).
Taken.
(b) All or nothing.
Whether blocked hours are lost or only deferred is not encoded: the answer is the hours to be given within the twelve months.

**F11. Time actually called on (§ 12(2)).**
It is working time and "nicht als Zeit der Rufbereitschaft anzurechnen" (`sazv-12.txt:3`), so it is subtracted before the 10-hour threshold.
Taken; the text leaves no other reading visible to me.

**F12. Which power do the three instructions rest on?**
(a) § 30c(5) sentence 1 no. 1, "zur Regelung der Arbeitszeit", with § 93(2) no. 6: § 5(2) is "Möglichkeiten ihrer flexiblen Ausgestaltung", § 6(1) "zu ihrer Dauer", § 12(1) "zum Zeitausgleich" (`sg-30c.txt:24-28`).
Taken.
(b) Sentence 1 no. 2, health protection "bei den Tätigkeiten nach Absatz 4" (`sg-30c.txt:29`), which the preamble cites.
Against (b): § 30c(4) takes its activities out of subsections (1) to (3), and the 2025 § 6(1) list names one-day variants, "eintägige Seefahrten" and "eintägige Ausbildungs- und Übungsvorhaben" (`sazv-6.txt:8`, `:12`), of activities § 30c(4) lists as multi-day, "mehrtägigen Seefahrten" and "mehrtägigen Übungs- und Ausbildungsvorhaben" (`sg-30c.txt:18`, `:20`).
The regime regulates work outside § 30c(4).

**F13. One area per day.**
The seat asks for one area of service; a day that spans two areas is answered for the one the soldier gives.

## What the law turns out to say

1. **Voidness does not always favour the soldier.**
   For § 12 it does: the earlier sentence 2 has no reduction for compelling service reasons, so 34 hours on call with three hours blocked give 0 hours as printed and 3 if the amendment is void (`sazwt-cases-seat.l4`, Case E).
   For § 6(1) it does the opposite: the earlier sentence 3 asked only that service reasons require the departure, "insbesondere in folgenden Bereichen" (`sazv-6-before-2025.txt:2`), while the 2025 sentence 3 adds that the work fall under one of three heads (`sazv-6.txt:2-5`).
   Fifteen hours on permanent operational tasks, with service reasons and nothing else, are not allowed as printed and are allowed if the recast is void (Case C).
   This holds on fork F6(a).
   For § 5(2) it cuts both ways: the earlier sentence 2 allowed departures only "auf Montag bis Samstag", which keeps Sunday free; but the earlier text had no sentence 3, so an application for an individual distribution has nothing to rest on, and its sentence 1 did not reach part-timers reduced by 10 % or more.
   A soldier who relies on the citation argument for one provision relies on it for all three, because they rest on the same power, § 30c(5) sentence 1 no. 1.
   Asserted.
2. **Art. 5 No. 4 (§ 12) took effect retroactively from 1 January 2025**, not 1 April: "Artikel 5 Nummer 4 tritt mit Wirkung vom 1. Januar 2025 in Kraft" (`bgbl-2025-i-78.txt:303`), in a regulation dated 6 March and promulgated 11 March 2025.
   So "as before 1 April 2025" is right for Nos. 1 and 3 and three months out for No. 4, and the reading here is named by voidness, not by a date.
   As printed, on-call months from January to March 2025 fall under the restriction retroactively; whether that retroactivity is itself lawful is a separate question, not encoded and not decided.
3. **The 2025 preamble narrows its citation of § 30c(5) to sentence 1 no. 2, twice.**
   "§ 30c Absatz 5 Satz 1 Nummer 2 in Verbindung mit Absatz 4" in the citation and "§ 30c Absatz 5 Satz 1 Nummer 2 durch Artikel 6 Nummer 11 ..." in its amendment history (`bgbl-2025-i-78.txt:38`, `:40`).
   No other line of the preamble (`:13-50`) names any part of § 30c(5) sentence 1 no. 1.
   Asserted.
4. **Why this candidate is weaker than the annex case.**
   In the annex case, nothing the 2025 preamble cites touches the exemption power: neither § 30c(6) nor § 93(2) no. 7 (sibling finding 2).
   Here the preamble does cite § 93(2) no. 6, whose words name "die regelmäßige Arbeitszeit ... nach § 30c Absatz 5" (`sg-93.txt:19`, asserted), so the addressee is pointed at the Absatz and the ministerial competence these instructions use; within that Absatz the preamble names sentence 1 no. 2, and these instructions rest on no. 1.
   A court reading the requirement by its purpose, as BVerwG 3 B 51.18 para. 35 does, has more to work with here than in the annex case.
5. **The Ministry's own citations point both ways.**
   The 2015 Regulation was made "Auf Grund des § 30c Absatz 5 in Verbindung mit § 93 Absatz 2 Nummer 5" (`sazv-eingangsformel.txt:2`), the whole Absatz.
   The 2022 amendment cited only "§ 93 Absatz 2 Nummer 6 und 7" and no part of § 30c (`bgbl-2022-i-34-flow.txt:9-13`): if a citation of § 93(2) no. 6 without § 30c(5) were not enough, its working-time changes would have the same gap in a plainer form.
   The 2025 preamble is the only one of the three that names a single part of § 30c(5); it names sentence 1 no. 2, and these instructions rest on no. 1.
   Asserted (the three lists).
6. **The 2025 recast of § 6(1) changed the list's areas, not only its form.**
   Dropped: "Dauereinsatzaufgaben".
   Narrowed: "Einsatzausbildung" to "eintägige Ausbildungs- und Übungsvorhaben im Rahmen der Einsatzausbildung", and "Dienst in kurativen Sanitätseinrichtungen" to "Pflege- oder Behandlungsdienste" there.
   Added: Feldjäger- and Personenschutzdienste, Basisausbildung, Flugsicherung, airports and ports, events of considerable public interest, rescue services, and two general heads (extraordinary events and accidents; continuity of the service).
   Compare `sazv-6.txt:2-14` with `sazv-6-before-2025.txt:2-9`.
   Asserted area by area in `sazwt-tests.l4`.
7. **The earlier § 5(2) sentence 1 left part-timers reduced by 10 % or more outside the Monday-to-Friday rule** ("Teilzeitbeschäftigung mit einer Verkürzung der Arbeitszeit um weniger als 10 Prozent", `sazv-5-before-2025.txt:10`); the 2025 strike brings every part-timer in.
   Asserted at 9 % and 10 %.

## Answer table

§ 5(2), over which days the regular weekly working time may be distributed:

| soldier | as printed | if the 2025 amendment is void |
|---|---|---|
| full-time, or part-time reduced by less than 10 %; no service reasons | Monday to Friday | Monday to Friday |
| the same; service reasons call for a departure | any days of the week | Monday to Saturday |
| part-time reduced by 10 % or more | as for full-time | not answered (`NOTHING`; F3) |
| applies for an individual distribution over Monday to Friday; service reasons do not stand against it | may be approved | not answered (`NOTHING`: no such sentence) |
| the same; service reasons stand against it | may not be approved | not answered (`NOTHING`) |

§ 6(1), the ground for a regular daily working time above 13 hours where service reasons require it (without service reasons, 13 hours hold under both readings):

| area of service, nothing out of the ordinary, continuity not required | as printed | if the 2025 recast is void |
|---|---|---|
| guard, special or orderly duty | no. 1 | named (old no. 4) |
| military police duty or close protection | no. 1 | not named; service reasons suffice |
| general basic training | no. 3, letter a | named (old no. 1) |
| Basisausbildung | no. 3, letter a | not named; service reasons suffice |
| post or career training | no. 3, letter b | named (old no. 2) |
| deployment training, a one-day project | no. 3, letter c | named (old no. 2) |
| deployment training, other | **none: 13 hours hold** | named (old no. 2) |
| permanent operational tasks | **none: 13 hours hold** | named (old no. 3) |
| military air traffic control | no. 3, letter d | not named; service reasons suffice |
| nursing or treatment in a curative medical facility | no. 3, letter e | named (old no. 5) |
| other service in a curative medical facility | **none: 13 hours hold** | named (old no. 5) |
| nursing or treatment in a rescue service | no. 3, letter e | not named; service reasons suffice |
| operating an airport or a port | no. 3, letter f | not named; service reasons suffice |
| a one-day sea voyage of a seagoing navy unit | no. 3, letter g | named (old no. 6) |
| a long-haul flight as aircraft crew | no. 3, letter h | named (old no. 7) |
| preparing or running an event of considerable public interest | no. 3, letter i | not named; service reasons suffice |
| another area | **none: 13 hours hold** | not named; service reasons suffice |
| any area, an accident or extraordinary event causing an excessive unforeseeable workload | no. 2 (no. 1 first where it applies) | as the area's row |
| any area where the continuity of the service must be ensured | no. 3 (unless an earlier ground applies) | as the area's row |

§ 12, hours of compensation for a calendar month's on-call duty, to be given within twelve months, as time off (fixed working time) or a credit to the flexitime account (Gleitzeit):

| on-call hours that count | hours compelling service reasons stand against | as printed | if the 2025 amendment is void |
|---|---|---|---|
| 10 or fewer | any | 0 | 0 |
| 11 | 0 | 0.125 | 0.125 |
| 18 (or 26 with 8 actually called on) | 0 | 1 | 1 |
| 26 | 0 | 2 | 2 |
| 26 | 0.5 | 1.5 | 2 |
| 34 | 3 | 0 | 3 |

Art. 80(1) sentence 3 GG: the 2025 preamble does not cite § 30c(5) sentence 1 no. 1 (asserted); it names § 93(2) no. 6 (asserted); the three instructions are void unless an exception applies (asserted both ways).

## Checks run

`./check.sh` in this folder, target `main`, on 2026-11-02 (the `l4` is a dev build, sha256 25a091f4..., the same binary the sibling used; the main build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02)):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sazwt-cases-seat.l4                            0        28       0        0         0 |      0        28       0        0  same
sazwt-law.l4                                   0         0       0        0         0 |      0         0       0        0  same
sazwt-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
sazwt-tests.l4                                 0        94       0        0         0 |      0        94       0        0  same
TOTAL (4 modules)                              0       122       0        0           |      0       122       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Exit status 0.
Assertions written equal assertions satisfied: 94 in `sazwt-tests.l4`, 28 in `sazwt-cases-seat.l4`.
`l4 run` on every module, with both builds, prints no `DiagnosticSeverity_Warning`.
No assertion is expected to fail.
The encoding has no regulative rule and no `#TRACE`, so the trace blind spot of `check.sh` does not arise.

`python3 -I srcrefs.py check --refs ../../registers/source-bundle/sazv-6.txt sazwt-law.l4`: 85 src: lines, 22 runs, 39 locators, 0 problems; `--strict` the same.
The other three modules carry no quotations.

Positive control, because every assertion passed on the first run: five mutations of `sazwt-law.l4`, each on a scratch copy, each turned assertions red (tests / cases failed):
the earlier § 5(2) "weniger als 10 Prozent" read as "at most 10" (1 / 0); the earlier sentence 2's Saturday read as any day (2 / 1); the 13-hour limit read as "less than 13" (2 / 0); one eighth read as one quarter (10 / 5); the 2022 preamble given the no. 1 power (1 / 0).
Run on the final modules; the copies were deleted and the deposited modules are untouched by the control.

## Before this is worth relying on

- Read the 2015 gazette (BGBl. I S. 1995) for the earlier § 5(2) sentence 2 and § 6(1) sentence 3, which rest on buzer.de alone, and replace the transcriptions with it.
- Decide F1 with someone who knows German constitutional and administrative law; F6 and F7 change the § 6(1) rows of the answer table and should be decided with it.
- Look for the Ministry's reasons for the 2025 regulation (the Begründung), which may say which power Art. 5 Nos. 1, 3 and 4 were made under.
- Check which Abschnitt SAZV § 19 governs, and whether the retroactive effect of Art. 5 No. 4 (finding 2) raises a question of its own.
- Run the independent test pass (`encoding-a-subject` step 8): the tests here were written by the encoder.
- Have a domain expert read the encoding against the German text (the pipeline's HG1).
