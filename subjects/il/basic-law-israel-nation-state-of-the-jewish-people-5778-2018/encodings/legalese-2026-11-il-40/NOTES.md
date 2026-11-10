# Basic Law: Israel as the Nation-State of the Jewish People, in L4 (row IL-40, draft)

Status: draft.
No domain expert has read this encoding against the source, and no independent tester has run.
Target compiler: `main`.
Written by one agent (Sonnet 5.5) on 2026-11-09 from the lead's brief.

## 1. Seat

The seat is the individual to whom the Basic Law is applied: a resident, a person asked to use or receive a notice in a language, a person asked whether a change to the Basic Law was validly made.
There is no seat for an official.
The Basic Law puts most of its duties on the State, so each question is asked as what the text means for the person ("What status does the Basic Law give to my language?", "Do I have the right to keep the days of rest on my own Sabbath and festivals?", "Was a change to the Basic Law made as s 11 requires?").
The questions are in `il40-seat.l4`, each with `@export` and `@desc`, and call the rules in the other modules without restating them.

## 2. Edition, sources and what each is worth

The official text is Sefer HaChukim 5778 no. 2743, 14 Av 5778 (26 July 2018), p. 898, the Knesset's PDF `fs.knesset.gov.il/20/law/20_lsr_504220.pdf` (sha256 in `registers/source-bundle/SOURCES.json`).
It was read from the page image (`official/sefer-hachukim-5778-no-2743-p898.page-image.png`).
Its footnote reads (read from the page image) that the Law was passed in the Knesset on 7 Av 5778 (19 July 2018), in a sitting that began on 5 Av 5778 (17 July 2018), and that the proposal and explanatory notes were published in Hatza'ot Chok HaKnesset 768 of 26 Adar 5778 (13 March 2018), p. 134.
The Wikisource consolidation is an aid.
The vote on 19 July 2018 (62 for, 55 against, 2 abstaining) is from press reports, not from a Knesset record: the Knesset's legislation database answered with a script-based bot challenge and was not read (section 9).
Every other instrument is labelled in `SOURCES.json` as official (read from an image) or an aid.
Only the pages the row cites are deposited as PDFs; `SOURCES.json` keeps the whole file's URL, sha256 and size as downloaded for provenance.
The deposited extracts are printed p. 2759 of Laws of Palestine vol. 3 (the Order in Council, an image-only PDF) and p. 3 of Iton Rishmi no. 2, Supplement A (the Ordinance).
A finding that rests only on an aid is labelled CONSOLIDATION-ONLY wherever it is written.

## 3. Wikisource against the official page

`tools/compare-official.py` strips the consolidation's templates and editorial notes and compares the words of every section and heading, as a multiset, with the words of the official page.
Result: 293 words on the consolidation side (digits and sub-section letters dropped on both sides), 301 on the official side; nothing is in the consolidation that is not on the page, and the only words on the page and not in the consolidation are the eight words of the Law's title line, which the consolidation carries in its header.
Punctuation, the order of the sections and the section numbers were compared by eye against the page image, with no difference found.
So: no substantive difference between the consolidation's body and the official page.
The nine `ח:הערה` notes ("ראו ...") are the consolidator's and are not on the official page.
Raw word-multiset comparison cannot see a word moved between two sections; the by-eye comparison did.

## 4. What the official text refers to, and what s 4 turns out to say

The official text cites no enactment by name.
It says "in law" (בחוק) at ss 2(e), 4(b), 8 and 10, "this Basic Law" and "a Basic Law" at s 11, and "before the commencement of this Basic Law" at s 4(c).
The consolidation prints eleven pointers (nine notes) that look like cross-references; they are typed in `il40-references.l4` with `it is in the official text` FALSE, and a test counts them.
The cross-reference sweep tool (`xref-sweep.py`, which sees link targets and sub-citations in a consolidation) found no repealed or missing target, because the only link targets in the text are inside those editorial notes.

Findings on s 4 (none of them turns on a payment, a penalty or a deadline):

1. **s 4(c) names no provision.**
   Its words are "אין באמור בסעיף זה כדי לפגוע במעמד שניתן בפועל לשפה הערבית לפני תחילתו של חוק־יסוד זה" (read from the page image): nothing in the section is to harm "the status given *in practice*" to Arabic before the Basic Law came into force.
   It does not say "by law" and does not name article 82 of the Palestine Order in Council 1922 or section 15(b) of the Law and Administration Ordinance 5708-1948.
   The pointer from s 4 to article 82 is the consolidator's note only.
   The two provisions that the bundle shows as giving Arabic a standing before the Basic Law are typed in `il40-s4-saving.l4`, each with `the Basic Law names it` FALSE.
   Whether a standing given by an enactment is a status "given in practice" is fork F1; it is declined by default.
2. **The Basic Law has no commencement section.**
   "Before its commencement" therefore has no day in the text.
   The Interpretation Law fixes the hour (s 21: 00:01 of the commencement day, consolidation line 124) and not the day.
   The Interpretation Ordinance's chapter on the commencement of enactments reads "(בוטל)" in the consolidation (CONSOLIDATION-ONLY), and its s 17 (publication day as default) is for subsidiary legislation only.
   Two days are candidates: 19 July 2018 (passed) and 26 July 2018 (published in Sefer HaChukim 2743).
   A rule of case law that fills this gap may exist; none is in a deposited source.
   Fork F2, declined by default; a status held between the two days is answered NOTHING.
3. **s 4(b) says the regulation of the use of Arabic in or before State institutions "shall be in law" (בחוק).**
   The Interpretation Law s 3 defines "חוק" as a law of the Knesset or an Ordinance (consolidation line 39), and lists "דבר המלך במועצתו" (an Order in Council) under "דין" (line 35), apart from "חוק".
   Read together, article 82, which is in an Order in Council, is a "דין" and not a "חוק" (fork F4).
   The encoding answers `s 4(b) counts as law an instrument of the kind` FALSE for an Order in Council, a regulation, a Government decision and an administrative direction.
4. **Which provisions of the Interpretation Law on saving earlier law bear on s 4(c)?**
   My reading, for a domain expert to overrule: none supplies what s 4(c) leaves open.
   s 22 (the effect of a repeal on earlier acts and rights) speaks of the repeal of a "דין"; the body of the Basic Law has no word of repeal (a search of the body for בטל, מבוטל, יבוטל finds none), so s 22 is not engaged by the text.
   s 19 (giving a power or imposing a duty under one enactment does not by itself derogate from another) is about powers and duties; s 4(b) gives no power and imposes no duty on a person.
   s 25 (a reference to an enactment means it as worded when resorted to) applies to a reference to an enactment; s 4(c) refers to none, so s 25 cannot be used to read article 82 "as it now stands".
   s 1 makes the Law apply to every enactment unless another provision or the context is inconsistent.
5. **Article 82, the instrument the consolidation points at, has no official consolidated text; the current text is a composite.**
   Read from the page image (Laws of Palestine vol. 3, p. 2759, the Knesset's scan, which carries a strike-through of the word for "in English" and underlines on some words): the first sentence says that official ordinances, notices and forms "shall be published ~~in English~~ in Arabic and Hebrew", and that the three languages may be used in debates in the Legislative Council and, subject to regulations, in government offices and courts.
   The consolidation's article 82 substitutes "הממשלה" for "הנציב העליון", drops the Legislative Council clause, and adds a second paragraph making the English text prevail on a conflict (CONSOLIDATION-ONLY for all three; the 1939 amending instrument and the 5708 adaptation are not in the bundle, so which instrument made each change is not traced).
   Section 15(b) of the Law and Administration Ordinance, read from the page image of Iton Rishmi no. 2, Supplement A, 21.5.1948, p. 3, says "כל הוראה בחוק הדורשת את השימוש בשפה האנגלית, בטלה"; it names no article.
   The residue: the first sentence names two languages once English goes, and the text still says "the three languages" (expected-red R3).
   This is a finding about the cross-referenced instrument, not the Basic Law.
6. **s 2(b) and the Declaration on the State Flag use different colour words.**
   Basic Law s 2(b): the two stripes are "תכלת" and the Magen David "תכול".
   The Declaration (Iton Rishmi no. 32, 12.11.1948, p. 62, read from the page image): the stripes are "תכלת כהה" and the Magen David is "ששה פסי תכלת".
   The Basic Law does not cite the Declaration; s 2(e) leaves the details to a law, and the Flag, Emblem and Anthem Law s 1(a) (CONSOLIDATION-ONLY) fixes the flag by the Declaration.
   Expected-red R1 and R2.
   Both texts were read from official page images, so this finding is not CONSOLIDATION-ONLY.

Checks that came out clean: s 3 and s 1 of Basic Law: Jerusalem, Capital of Israel say the same words (the Jerusalem Law is CONSOLIDATION-ONLY); s 9(a) agrees with the Independence Day Law s 1(a) and (c) (the national holiday, a day of rest; CONSOLIDATION-ONLY); s 8 agrees with the Hebrew Date Use Law ss 2 and 3 (CONSOLIDATION-ONLY); s 10 agrees with the Law and Administration Ordinance s 18A (CONSOLIDATION-ONLY); s 9(b) spells the two memorial days with a plene yod (זיכרון) where the two Laws have none (זכרון), and the Memorial Day Law was first titled "חוק יום הזכרון לחללי מלחמת הקוממיות וצבא־הגנה לישראל" (from its header) before the title the Basic Law uses.

## 5. Coverage table

| provision | heading | disposition |
| --- | --- | --- |
| 1(a), (b), (c) | עקרונות יסוד | inert: declaratory statements of principle; quoted in the source and typed only as the pointers of the consolidation; no right or duty of a person is stated |
| 2(a) | the name of the State | encoded only as the pointer to the Flag, Emblem and Anthem Law; the name is quoted, and not tested against that Law's s 1(d) |
| 2(b) | the flag | encoded: colour words, checked against the Declaration (R1, R2) |
| 2(c) | the emblem | inert: the Declaration on the Emblem is a drawing, so no words can be compared; the pointer is typed |
| 2(d) | the anthem | inert: quoted only |
| 2(e) | details by law | encoded as the pointer to the Flag, Emblem and Anthem Law |
| 3 | the capital | encoded: equality with Basic Law: Jerusalem s 1 |
| 4(a), (b) | language | encoded: `the status the Basic Law gives to`; `s 4(b) counts as law an instrument of the kind` |
| 4(c) | saving | encoded: typed provisions, forks F1 and F2, `s 4(c) leaves unharmed the status` |
| 5 | ingathering of exiles | encoded as a typed State duty; no entitlement of a person |
| 6(a) | the State's duty toward Jews and citizens in distress | encoded: `s 6(a) puts on the State the duty ...` (fork F7) |
| 6(b), (c) | the State's work in the Diaspora | encoded as typed State duties |
| 7 | Jewish settlement | encoded as a typed State duty |
| 8 | the calendar | encoded |
| 9(a), (b) | Independence Day and the memorial days | encoded |
| 10 | the days of rest | encoded (fork F8) |
| 11 | entrenchment | encoded (fork F5) |

No row is left deferred.

## 6. Fork register

Each fork has one switch, default declined (NOTHING).

- **F1** (s 4(c), `A reading of what s 4(c) saves`): "a status given in practice".
  Readings: only a status given in practice (taken as one of the two named readings); a status given in practice and a status an enactment gave; declined (default).
  Reading rejected: none rejected; the two are kept by name.
- **F2** (s 4(c), `A reading of the day the Basic Law commenced`): the day passed (19 July 2018), the day published (26 July 2018), declined (default).
- **F3** (s 4(a)): whether "the language of the State" excludes another language from also being one.
  The text is silent, so every language but Hebrew and Arabic is NOTHING.
- **F4** (s 4(b)): "בחוק" read through the Interpretation Law s 3 (a law of the Knesset or an Ordinance).
  Rejected: any enactment, regulations included, because s 3 defines "חיקוק" as "חוק או תקנה" separately from "חוק".
  Whether an Order in Council is within "פקודה" (an ordinance given before the State was established) is not settled by the text; I take "דבר המלך במועצתו" (listed separately under "דין") as not within it.
  The Interpretation Law's encoding could not be copied in (its modules use `REFUSE`, which `main` does not read): its effect is carried as typed values and the text is quoted (F10).
- **F5** (s 11): "a majority of the members of the Knesset" is more than half of the members; the number of members is an input because Basic Law: The Knesset is not deposited.
  Rejected: a majority of those voting.
- **F6** (s 9(b)): the plene spelling is read as the same days as the Laws' titles.
- **F7** (s 6(a)): "because of their Jewishness or their citizenship" qualifies both groups.
  Rejected: only the citizens.
- **F8** (s 10): who is a Jew is a fact the person states.
- **F9** (article 82): the composite is CONSOLIDATION-ONLY.
- **F10**: the Interpretation Law was not copied in (reason under F4); its source commit is `4bd41d992`, and the consolidation deposited here is a byte-for-byte copy of its `law.wiki` (sha256 `df3abac9015b4cd919eddece40d46565a97cdf123f78bbe925b687a5f5f0d2ab`).

Sites decided case by case (ruling of 2026-11-05) carry the fork number in the `@ref` line of the rule.
The rulings of 2026-11-04 and 2026-11-05 on `JUST FALSE` and `NOTHING` are followed: a flat negative ("shall not be changed except by") and a "means" definition answer `FALSE`; an unclosed list, silence and a scope limit with no "only" answer `NOTHING`.

## 7. What `check.sh` prints

Run on 2026-11-09 with `~/.local/bin/l4` (a dev build) and the newest main build, 1.6.109 (main, 4c887e0, 2026-11-04), fetched by `fetch-main-l4.sh`.
Twelve modules; total errors 3, satisfied 100, failed 3, refused 0; the main columns are the same for every module.
The three errors are the three declared failed assertions of `il40-tests-expected-red.l4` (R1, R2, R3); there is no other error.
Per module: `il40-tests-s4.l4` 38 satisfied, `il40-tests-s11.l4` 15, `il40-tests-days.l4` 24, `il40-tests-references.l4` 8, `il40-tests-seat.l4` 15, `il40-tests-expected-red.l4` 0 satisfied and 3 failed; the six rule modules carry no assertions.
Target: `main`.
`tools/hebcheck.py` checked that every Hebrew string literal occurs verbatim in a deposited source (30 literals, none missing).
No mutation check was run.

## 8. Open questions for a domain expert

- Does a status given by an enactment count as one "given in practice" in s 4(c)?
- On which day did the Basic Law commence?
- Is an Order in Council within "פקודה" in the Interpretation Law s 3, for the purpose of s 4(b)?
- Which instrument made each change to the consolidation's article 82 (the 1939 Order, the 5708 adaptation)?
- What is the number of members of the Knesset that s 11 should be read against (the encoding takes it as an input)?

## 9. Not reached

- The Knesset legislation database (main.knesset.gov.il) answers with a script-based bot challenge; recorded, not got round.
  The vote, the dates of the readings other than those in the official footnote, and any amendment of the Basic Law could not be checked there.
  No amendment is recorded in the consolidation's header, which lists only the Sefer HaChukim 898 publication (CONSOLIDATION-ONLY).
- The Wikisource revision ids of the deposited aids were not recorded.
- The Declaration on the Emblem (an image), Basic Law: The Knesset, the Flag, Emblem and Anthem Law's official text and the 1939 amending Order were not read from official instruments.
- The Interpretation Law was not re-read in the official PDFs for this row.
