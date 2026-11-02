# NOTES: Mishnah Kinnim, L4 encoding `legalese-opus-5.5` (solo)

This encodes the whole of Mishnah Kinnim: the levels of the altar and what a pair of birds is offered as (1:1), how many birds of a mixture may be offered when the priest asks first (1:2–1:4), birds that fly from one nest to another and pairing by species (chapter 2), and what a priest who did not ask has validly offered, with what the owners must bring again (chapter 3).
Its centre is 3:2's "the majority is valid", encoded as Moshe Koppel and Philip Reiss read it (the smallest majority of a subset sum), with the three older readings beside it and a search over every apportionment that checks the formula case by case.
It states the law as the Mishnah and its commentators give it, and claims nothing about practice: Temple offerings have not been brought since 70 CE.

The sources are in `../../registers/source-bundle/`: the Hebrew text from he.wikisource, with Bartenura, Tiferet Yisrael on chapter 3 and Maimonides' code as aids (`../../SOURCE-LICENSE.md`, copied here as `SOURCE-LICENSE.md`).
The target is `main`; the build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02).
Modules: `kn-nouns.l4`, `kn-ch1.l4`, `kn-ch2.l4`, `kn-majority.l4` (the counting core), `kn-ch3.l4`, `kn-seat.l4`, `kn-tests.l4`, `kn-cases-seat.l4`; the solver obligations in `prove/`.
The six rule modules are generated from `tools/*.l4.in` by `tools/render.py`, which pastes each quotation from the bundle; the tests, the seat cases and `prove/` are written directly.

## Seat

The seat is **the person who brought the birds**: a woman after childbirth, a man or woman after a discharge, or anyone who vowed or gave a bird offering.
The tractate speaks of women ("to this one ... to that one"); Maimonides, in his commentary on the Mishnah, explains that women bring these offerings in every case men do and after childbirth as well (Reiss n. 12).
The questions, in `kn-seat.l4`, in the tractate's order under `§` groups: was my offering made at the right level; did my words make a vow or a gift; must I replace a vowed bird that died; how many of a mixture may still be offered; what now that a bird of my pair flew; how many of my pairs in a row survive a bird's round trips; what must I bring again for a pair of two species; must I as heir bring the other offering; at least how many offerings counted when the priest did not ask (with the readings, and Maimonides' attribution); how many pairs must we bring again between us; and how many more birds I must bring for the vow of 3:6.
The priest is an official and has no seat: what he did is a fact the owner states.
One question is asked by an heir (2:5), and one is labelled as going beyond the text (the worst case for a split the text does not name).

## Method

One agent (Claude Opus 5.5), working alone in one session, with no subagents and **no independent test pass**.
The Hebrew was read directly; every English word in the encoding is the encoder's gloss.
Quotations were pasted by script (`tools/render.py` calls `srcrefs.py quoteid`), never retyped.
Every expected value in the tests is taken from a source, which the comment above it names.
Because a green run proves nothing about the tests, two mutants were run against `kn-tests.l4` in a scratch copy: making each middle nest in 2:3 lose one pair a round trip instead of two failed 6 assertions; replacing Koppel's formula by Tiferet Yisrael's failed 9.

## Sources, and what each contributed

| source | read? | what it gave |
| --- | --- | --- |
| Mishnah Kinnim, he.wikisource printed text, standard numbering | deposited, read in full | the law |
| Maimonides' recension of the Mishnah (he.wikisource) | deposited | the numbering crosswalk; variants (1:3 reads הממועט where the printed text has המועט) |
| Bartenura on Kinnim 1–3 (he.wikisource) | deposited, read in full | the readings of 1:2, 2:2, 2:3 (the decree), 2:4, 2:5 (which offering sets the species), 3:1 (two women; joint replacement), 3:4, 3:5, 3:6 (the shortfalls) |
| Tiferet Yisrael on Kinnim 3 (he.wikisource, OCR) | deposited, Yakhin on 3:2 read | his "majority" rule and its examples (1 2 4; 3 4 5; 1 2 9; 1 2 5 7; the halvable cases) |
| Maimonides, Pesulei ha-Mukdashin 8 (he.wikisource) | deposited, read in full | his reading of 3:2 (8:6–7) and of 3:3–3:4 (8:9–11) |
| Philip Reiss, "A Mathematical Proof of Kinnim 3:2", *Torah u-Madda Journal* 9 (2000) 58–75, JSTOR 40914641 | read in full, from a mirror of the PDF yutorah.org lists (file id 2000/1053/703972), the file the gloss below links; JSTOR showed only a preview | the three senses of "valid" (§4); the smallest-majority theorem and its proof (§6); the cases 4-6-7, 1-3-5-6-13, R. Heller's 1-2-3-4-5; the commentators' positions (nn. 12–29); the account of Koppel (n. 29) |
| William Gewirtz, "Kinnim (3:2): An Intuitive Mathematical Approach", *Ḥakirah* 30 (2021) 269–279 | read in full | the same theorem by "containers"; his cases a) to d) (2-4-6-8-10, 2-4-6-8, the Mishnah's, 8-12-14 birds) and 2-4-8 birds; the two-container fallacy and its counterexamples 8-10-10-10-14-14 and 6-6-6-10-10 birds |
| Eliyahu Beller, "משנת קנים כפשוטה", *Higayon* 5, pp. 155–157 (a response) | read in full, from a copy held locally under the Asif library's personal-study terms; not deposited | **the only account read of Koppel's own article**: Koppel's definition (the most even division into two groups, its larger side), that Koppel found it implicit in Tiferet Yisrael, and that he proved it equals the halakhic worst case; Beller's objection that the plain sense is two women only; the case 2-3-4 |
| Moshe Koppel, "משפט קומבינטורי במסכת קינים" (the journal's index spells it קנים), *Higayon* 2, pp. 96–102 | **not obtained**: the Asif library has no file for it | known through Reiss n. 29 and Beller only (finding 1 on its page range) |
| Moshe Koppel, *Seder Kinnim: A Mathematical Commentary on Tractate Kinnim* (Jerusalem, 1998) | **not obtained** | known through Reiss n. 29 (pp. 4, 37–43, 40 and 64–68 cited) and through kinin-lean's numbering |
| Moshe Koppel, "Resolving Uncertainty: A Unified Overview of Rabbinic Methods", *Tradition* 37:1 (2003), from Koppel's site | read for Kinnim | it does not mention Kinnim; it frames *rov* and *kavu'a*, which 1:2's "even one in ten thousand" sets aside (fork F9) |
| Dov Gabbay and Moshe Koppel, "Uncertainty Rules in Talmudic Reasoning", author's proof for *History and Philosophy of Logic* (2010) | searched for Kinnim | it does not mention Kinnim (a text search of the PDF) |
| Two Higayon articles of Koppel's on *rov* and *kavu'a* (vol. 1 and vol. 4) | **not read** | they are scans with no text layer |
| Aryeh Shebson, `kinin-lean`, commit `0a57b7bd`, MIT | read after the encoding's own tests were written | prior art: a Lean 4 formalization in Koppel's 4+6+6 numbering, with a general smallest-majority theorem (`generalized_smallest_majority`) and a numbering crosswalk; nothing copied |
| "Gemini" gloss, `~/src/higayon/says-gemini.txt` | read | **secondary and unverified** (section "Formal treatments"): its four treatments shaped the solver obligations; the claims that rest on it alone are listed there |

Sefaria (API and site) answered with a Cloudflare human-verification challenge and was not used; Mechon Mamre was read once for orientation and not deposited (its `robots.txt` reserves AI use).

## Numbering

The encoding cites the standard numbering of the printed text, which he.wikisource and Bartenura use (4, 5 and 6 units).
Maimonides' recension divides 5, 6 and 5 (its own bracketed numbers on he.wikisource, checked).
Koppel's *Seder Kinnim* divides 4, 6 and 6, as kinin-lean's `SOURCES.md` reports from the bookmarks of a scan of the book (not checked: the book was not obtained).

| standard (here) | Maimonides' recension | Koppel (per kinin-lean) | topic |
| --- | --- | --- | --- |
| 1:1 | 1:1–1:2 | 1:1 | levels; what a pair is; vow and gift |
| 1:2 | 1:3 | 1:2 | designated birds mixed |
| 1:3 | 1:4 | 1:3 | obligations mixed: half, or the fewest |
| 1:4 | 1:5 | 1:4 | one reason or two; Rabbi Yose |
| 2:1–2:4 | 2:1–2:4 | 2:1–2:4 | flights |
| 2:5 | 2:5 and 2:6 | 2:5 and 2:6 | sin, burnt and the middle; species; heirs |
| 3:1–3:2 | 3:1 | 3:1–3:2 | the priest who did not ask; the majority |
| 3:3–3:6 | 3:2–3:5 | 3:3–3:6 | designated birds; 3:5; the vow |

kinin-lean also reports Sefaria's segmentation, which divides chapter 2 differently (its 2:4 holds both the designated-pair case and the three-place case, and its 2:5 the species); Sefaria could not be read to check it.

## Coverage table

| unit | provision | disposition | where |
| --- | --- | --- | --- |
| 1:1 | sin offering below, burnt above for a bird; the reverse for a beast; changed, invalid | encoded | `the level prescribed for`, `an offering made at this level is valid` |
| 1:1 | the obligation one sin, one burnt; vows and gifts all burnt | encoded | `sin offerings in a pair brought as`, `burnt offerings in a pair brought as` |
| 1:1 | what is a vow, what a gift | encoded | `what words of dedication make the offering` |
| 1:1 | vows replaced if they die or are stolen, gifts not | encoded | `the owner must replace it if it died or was stolen` (NOTHING for an obligation: the text is silent) |
| 1:2 | designated sin and burnt mixed: all die | encoded | `the most birds that may be offered as this kind from the mixture` (0) |
| 1:2 | a designated bird among an obligation: the obligation's number of that kind | encoded | the same, and the every-world definition beside it |
| 1:3 | equal obligations mixed: half; unequal: the fewest; whatever the reasons or owners | encoded | the same rules; reason and owner are not inputs |
| 1:4 | one reason and two reasons defined | encoded | `the two obligations are of one reason` |
| 1:4 | Rabbi Yose: bought jointly or price given to the priest | encoded | `the priest may assign each bird to whichever woman he wishes`; the seat answers "all may be offered" |
| 2:1 | a bird of an unassigned pair flies: take a mate, or it invalidates one | encoded | `what follows when a bird of an unassigned pair goes` |
| 2:2 | two and two: one lost going, one returning, then none | encoded | `nests still offerable when two women had two nests each` |
| 2:3 | one to seven: the three tables; "some say"; from the dead into all | encoded | `the nests left after round trips` (Bartenura's reading, checked against the tables); `the nests left when a bird from among those that must die flew into every nest` |
| 2:4 | unassigned and designated pair | encoded | `what follows a flight between an unassigned and a designated pair` |
| 2:5 | sin here, burnt there, unassigned between | encoded | `what follows a flight from the middle` |
| 2:5 | turtledoves and young pigeons; Ben Azzai | encoded | `what she must bring again when her pair was of two species` |
| 2:5 | the heirs | encoded | `her heirs must bring the other offering of her pair` |
| 3:1 | the asking priest is chapters 1–2; equal obligations, not asking: half every way | encoded | `the fewest offerings certainly valid when nests were mixed and the priest did not ask` |
| 3:2 | 1, 2, 3, 10, 100: half, half, the majority; the general principle | encoded | the same rule, and `kn-majority.l4` throughout |
| 3:3 | a sin for one, a burnt for another: half, half, both invalid | encoded | `the fewest offerings certainly valid in a mixture with designated birds, the priest not asking` |
| 3:4 | sin, burnt, unassigned and designated: half, half, only the unassigned, divided | encoded | the same; `the unassigned nest counts one offering for each of the two women` |
| 3:5 | a designated bird among an obligation already partly offered | encoded | `the birds that may be offered when a designated bird falls among an obligation's remaining birds` |
| 3:6 | the vow for a son: 1/2, 3/4, 5/6, 4+2+1 (Ben Azzai 4+2+2) | encoded | `the more birds she must bring`; the first two cases also derived (`the birds that make good every possible shortfall`) |
| 3:6 | Rabbi Yehoshua's ram, "some say" the wool; Rabbi Shimon ben Akashya | inert | aggadah; quoted, no rule |

No unit is `deferred`.

## Fork register

Each fork gives the readings, the one taken, and the text that licenses each.

**F1. What chapter 3 counts.**
Reiss (§4) distinguishes three senses of "valid": an offering valid in itself (1:1); the most that may be offered before the fact (chapters 1–2); and the fewest known to be valid after the fact (chapter 3).
Taken: all three, as different rules with different names, never one boolean.
Reiss n. 17: a view drawn from Rava (Zevahim 73b) holds that rejected birds stay rejected even after the fact, which would undo chapter 3; the Mishnah's author can answer that live animals are not permanently rejected, as Maimonides codifies (Pesulei ha-Mukdashin 6:1, 17).
The encoding follows the Mishnah.

**F2. "And" or "or" in 1:3 and 3:2 ("one to this, and two to that, and three ...").**
Two women only: Bartenura (Reiss n. 13), and, as Beller reads them (p. 156), Ravad, Rosh, Maimonides 8:7 and the commentary printed with the Talmud.
Any number of women together: Tiferet Yisrael (Reiss n. 13), Koppel and Reiss.
For 1:3 the readings give the same number wherever both speak (the fewest), so the encoding takes any number of owners.
For 3:2 they differ in scope for two owners and in substance beyond them; see F3.

**F3. "The majority is valid" (3:2).**
(a) **Koppel and Reiss** (taken): the smallest sum of some owners' pairs that is at least half the total; equivalently, in Koppel's own wording as Beller reports it (p. 155), the larger side of the most even division of the owners into two groups.
Koppel also found the reading in R. David of Dubno's *David ha-Levi* (1845), in an article by Z. H. Yaffe in *Talpiot* (1895) and in R. A. Y. Weiss's *Shenei Ofarim* (1997) (Reiss n. 29(1)), and remarked that it is implicit in Tiferet Yisrael (Beller p. 155).
Taken because Meng asked for an encoding informed by Reiss and Koppel, and because it is the only one of the four readings that equals the worst case for any number of owners; every commentator read takes the worst case as the rule (Gewirtz n. 4: "I know of no instance where this rule is disputed"; Beller p. 155).
(b) **Bartenura**: the larger woman's number, two women only; NOTHING for more.
(c) **Tiferet Yisrael**: one woman's number if it exceeds all the others together, otherwise the others'; wrong on R. Heller's 1-2-3-4-5 (ten, against eight), and, as encoded, on Gewirtz's two counterexamples too (26 against 17, and 14 against 10).
(d) **Maimonides** (8:6–7): for two nests the larger is valid, because all the larger owner's offerings count; his reason attributes the count to her, which the others do not.
Reiss n. 28 calls it "radically different" and records that its formulation mystified Ravad and R. Yosef Karo.
All four are encoded (`Reading of the majority`), and the seat can ask under any of them.
Beller's objection to (a) is about the plain sense (peshat), not the result: he concludes (p. 157) that the law that follows from Tiferet Yisrael's reading, which he takes to be Koppel's, is certainly true as halakha.

**F4. What the general principle adds.**
Ravad: some cases in which the priest offered unequal numbers above and below; R. Zerahiah ha-Levi objects that those lie beyond the mishnah (Reiss n. 21), though he suggests that the second half may govern innumerable other mixtures (n. 23); Tosefot Yom Tov: no new cases (n. 21).
Taken: the principle's two clauses are encoded as the rule for half above and half below, for any number of owners (F2, F3).

**F5. A priest who put some other number above.**
The text names all above, all below, and half and half.
Taken: NOTHING for any other split; a separate rule, labelled "beyond the text", gives the worst case (Ravad's extension; Beller's example, one and two with four above: three of the six birds).
Koppel's general solution for an arbitrary split is mentioned but not stated by Reiss (n. 29(2)), who judges it "too convoluted" to be read into "the majority".

**F6. 2:3: the decree, and "some say".**
The text gives three tables and no rule.
Bartenura: every nest the bird leaves loses a pair, the middle ones twice a round trip, by a decree that applies alike even where strict counting would spare a pair (he raises that objection himself).
Taken as a reading, and checked against all three tables.
"Some say" (Bartenura: on the third round trip the seventh nest keeps five) is encoded as an option, false by default: Bartenura says the halakha is not as they say.

**F7. 2:5: which offering sets the species.**
The first view: the sin offering's species, whether it was set aside first or last (Bartenura: "the sin offering is the main one").
Ben Azzai: whichever was set aside first, sin offering or burnt offering.
Taken: both, the first view by default (Bartenura: the halakha follows it).

**F8. 3:6: what "specified" and "fixed" mean, and why the numbers.**
Bartenura: "specified her vow" means she said which birds were for the vow; "fixed her vow" means she named its species when vowing, and does not remember it.
The text's numbers are encoded as given; Bartenura's possible shortfalls for the first two cases, covered (for each species and offering, the most any way could leave her short), reproduce 1, 2, 3 and 4.
The last two cases' derivations depend on more of Bartenura's assumptions and are not encoded as derivations.
Ben Azzai's "two sin offerings" in the last case is an option.

**F9. Majority and probability.**
1:2 ("even one in ten thousand, all of them die") and Bartenura ("living creatures are not nullified") exclude settling a mixture by its majority.
Nothing in the encoding weighs likelihood: every count is what holds in every possible world (chapters 1–2) or the fewest over every possible world (chapter 3).
Koppel's *Tradition* paper analyses *rov* and *kavu'a* in general; it does not discuss Kinnim.

**F10. Where the subject is filed.**
Assumed, not ruled: `subjects/religious/halakhah/mishnah-kinnim/`, a grammar proposed in `subjects/religious/README.md`.
The proposal (that README and the subject's row in `subjects/README.md`) is in a commit of its own, so it can be reverted alone; moving the subject is a `git mv` of its one directory, plus the two places inside it that name its path (`subject.json`'s `authority`, and this fork).

## Answer table: 3:2, priest not asking, half above and half below

Pairs per owner, and the valid offerings of each kind (so many sin offerings, and as many burnt offerings), as `the valid offerings of each kind under the reading` evaluates them on main 1.6.108.
The Koppel-and-Reiss column is asserted in `kn-tests.l4` for every row, and the definition (the search) agrees with it on every row; the other columns are asserted only where a source states the number.

| owners' pairs | half-able? | Koppel and Reiss | Tiferet Yisrael | Bartenura | Maimonides | source of the case |
| --- | --- | --- | --- | --- | --- | --- |
| 1, 2, 3, 10, 100 | no | 100 | 100 | NOTHING | NOTHING | the Mishnah; Reiss §4; Gewirtz c) |
| 1, 3, 5, 6, 13 | yes | 14 | 14 | NOTHING | NOTHING | Reiss §5 |
| 4, 6, 7 | no | 10 | 10 | NOTHING | NOTHING | Reiss §§5–6; Gewirtz d) |
| 1, 2, 3, 4, 5 | no | 8 | **10** | NOTHING | NOTHING | R. Heller via Reiss §5; Gewirtz a) |
| 1, 2, 3, 4 | yes | 5 | 5 | NOTHING | NOTHING | Gewirtz b) |
| 4, 5, 5, 5, 7, 7 | no | 17 | **26** | NOTHING | NOTHING | Gewirtz, against filling both containers (34 birds, not 36) |
| 3, 3, 3, 5, 5 | no | 10 | **14** | NOTHING | NOTHING | Gewirtz, the smallest such case (20 birds, not 22) |
| 2, 3, 4 | no | 5 | 5 | NOTHING | NOTHING | Beller p. 156 (the plain sense gives 4) |
| 1, 2 | no | 2 | 2 | 2 | 2 | Gewirtz; Bartenura on 3:1 |
| 2, 3 | no | 3 | 3 | 3 | 3 | Bartenura on 3:1; Maimonides 8:6 (4 and 6 birds) |

NOTHING means that the reading, on the commentator's own terms, says nothing of more than two owners.
The pairs the owners must bring again between them (Bartenura on 3:1; Ravad, Reiss n. 14) are the total less the valid count: 16 in the Mishnah's case (Reiss: "16 olot and 16 hatta'ot").

## Formal treatments, and the backends

Meng asked (relayed by the higayon session on 2026-11-02; Meng's words checked in that session's transcript) that the encoding be shaped for extraction to the formal backends, for the treatments that a gloss (`~/src/higayon/says-gemini.txt`) attributes to Koppel.
**The gloss is secondary and unverified**: it is a Gemini summary, and it cites as Koppel's a PDF (`download.yutorah.org/2000/1053/703972/05.-a-mathematical-proof-of-kinnim-32.pdf`) that is Philip Reiss's paper (the same file id was read; its title page names Reiss).
Its four treatments, and where they are in the encoding:

| treatment (as the gloss names it) | in the encoding | what supports it besides the gloss |
| --- | --- | --- |
| 1. sets: partitions, unions, intersections | the first clause of 3:2's principle as a partition of the owners (`the nests can be divided so that no woman's are both above and below`, by subset sum); `prove/` section A | the Mishnah's general principle; Tiferet Yisrael; Reiss §5; Beller's account of Koppel's "optimal division". Unions, intersections and complements: **gloss only**; nothing in the text calls for them |
| 2. the priest's acts as a function, with upper and lower bounds | before the fact, the most that may be offered (an upper bound, chapter 1); after it, the fewest known valid (a lower bound, chapter 3); `prove/` B (upper), C and D (lower), each lower bound with a witness that it is reached | Reiss §4 (three senses of valid), §6 (an algorithm attaining the bound); Reiss n. 29 ("a more algebraic proof"). "An algorithm or function" as Koppel's own framing: **gloss only** |
| 3. min-max: the worst case | `the fewest offerings certainly valid in the mixture`, a search over every apportionment; 3:3's "for I say" | the Mishnah (3:3); Bartenura; Reiss §6; Gewirtz; Beller p. 155 (the minimum number of valid birds, the worst case, decides) |
| 4. strict deduction, not probability | every count holds in every world (F9); `prove/` states each as a universal claim | the Mishnah (1:2); Bartenura on 1:2. That Koppel "contrasts standard mathematical probability with what he calls 'Rabbinic logic'" in Kinnim: **gloss only**. The gloss cites for it a paper titled "Probabilistic Foundations of Rabbinic Methods for Resolving Uncertainty", not read under that title; Koppel's *Tradition* paper on resolving uncertainty and the Gabbay–Koppel paper do not mention Kinnim |

The gloss's "thesis" that the tractate may be theoretical is not gloss-only: Reiss n. 29(3) cites *Seder Kinnim* p. 4 and p. 40 for it.

**What each backend did with it (run 2026-11-02 on nye; nothing here is merged):**

- **`l4 prove` (Z3)**, draft legalese/l4-ide#784 at `193690e14`, z3 4.16.0, via `prove/prove.sh`: **PASS**.
  8 universal obligations proved: 1-2-3-10-100 cannot be halved (all 32 divisions); one burnt offering is safe in 1:3's mixture; the lower bounds 200, 20, 16 and 20 birds for the Mishnah's, Reiss's, R. Heller's and Gewirtz's cases; 3:4's two; and section F, below.
  5 ground witnesses satisfied: each of the four bounds is reached, and 1-3-5-6-13 can be halved.
  5 false claims refuted, each with a counterexample:
  - that two burnt offerings are safe in 1:3's mixture: `X1 = 2` (both of them the first woman's);
  - that 201 of 232 are valid: `A5 = 116` (the hundred's birds all above);
  - Tiferet Yisrael's 20 birds on 1-2-3-4-5: `H = 2, 3, 2, 8, 0`, eighteen;
  - filling both containers on 3-3-3-5-5 (22 birds): `G = 0, 0, 0, 10, 9`, twenty;
  - section F's control (below): `P = 2, U = 4`.

  **What the solver checks, and what it does not.**
  The solver's fragment has no lists and no recursion, so the rules that give the encoding's chapter-3 answers cannot be handed to it: the smallest-majority formula, which answers 3:2 (`kn-ch3.l4:52`), and the search over apportionments, which answers the designated mixtures and the splits the text does not name (`kn-ch3.l4:77`, `:118–122`), both take a list of owners.
  The obligations are written by hand instead, one per case, with a free number for each owner's birds above, and the sum over that case's owners written out.
  Each owner's count is the plain-number rule `the valid offerings of a nest of pairs with so many of its birds above`.
  The search scores a nest with a different rule, `the valid offerings of an obligation with so many of its birds above`, on the record `a nest of pairs` builds; section F proves the two equal for every number of pairs and of birds above, and its control (a nest owing one burnt offering more) is refuted, so the per-nest count the solver reasons about is the one the search uses.
  Not proved: that each case's written-out sum is the set of apportionments the search ranges over.
  That link rests on evaluation and on reading the two: on these four cases `kn-tests.l4` asserts that the search equals twice the smallest majority, and that 3:2's rule gives 200, 20, 16 and 20 birds, the bounds the solver shows are least.
  The general theorem over any list of owners is not stated to the solver at all.
- **Lean 4** (`l4-ee export lean --check`, l4-verify `da31bb0` on l4-ide `9359ae64d`, Lean 4.35.0).
  On `prove/kn-obligations.l4` (as it stood before section F was added), 5 of 17 theorems proved, the 5 ground witnesses, agreeing with the evaluator.
  **None of the 7 universal obligations proved**: the `ASSUME`s became Lean `variable`s, so each theorem is stated universally, but `grind` did not unfold the encoding's definitions.
  On `prove/kn-refutations.l4`, 0 of 4 proved (correctly; Lean gives no counterexample).
  On `kn-tests.l4` the export skipped 15 decisions (most for "a type the typechecker did not pin down", the rest because they use one of those) and the 57 assertions that use them; Lean then reported 5 "fail to show termination" errors on the recursive decisions and 95 `grind` failures, and the run broke without a verdict.
  So at this build the Lean backend handles none of this encoding's list-recursive rules; kinin-lean shows that a general Lean proof can be written by hand.
- No other backend was run.

## What `check.sh` prints

Run from this folder with a dev build of `l4` (sha256 `25a091f4…`) as your `l4`:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
kn-cases-seat.l4                               0        49       0        0         0 |      0        49       0        0  same
kn-ch1.l4                                      0         0       0        0         0 |      0         0       0        0  same
kn-ch2.l4                                      0         0       0        0         0 |      0         0       0        0  same
kn-ch3.l4                                      0         0       0        0         0 |      0         0       0        0  same
kn-majority.l4                                 0         0       0        0         0 |      0         0       0        0  same
kn-nouns.l4                                    0         0       0        0         0 |      0         0       0        0  same
kn-seat.l4                                     0         0       0        0         0 |      0         0       0        0  same
kn-tests.l4                                    0       157       0        0         0 |      0       157       0        0  same
TOTAL (8 modules)                              0       206       0        0           |      0       206       0        0
```

`check.sh` exit status 0; no failing assertion is expected.
`srcrefs.py check --refs`: 98 quote lines, 28 runs, 51 locators, 0 problems; `--strict` reports 8, all of one kind: a later rule cites an earlier quote run in its file, which plain `--refs` allows.
Bartenura, whose lines are whole paragraphs, is cited by file and line in prose, not quoted.
`prove/` is not run by `check.sh`: plain `l4 run` reports its `ASSUME` assertions as errors on both compilers.
Run `prove/prove.sh` with an `l4` that has `prove`.

## Findings

1. **Reiss's citation of Koppel's article gives the wrong pages.**
   Reiss n. 29 cites "A Combinatorics Theorem in Masekhet Kinnim", *Higayon* 2 (1992): 66–71.
   The journal's own index (printed p. 116, read 2026-11-02) lists "משפט קומבינטורי במסכת קנים" at vol. 2 pp. 96–102, and pp. 66–71 hold another article of Koppel's ("משה בבית מדרשו של ר' עקיבא: על תורת מסיני ותורת המספרים"); Beller's note 1 also gives pp. 96–102.
   This encoding cites pp. 96–102.
2. **The gloss misattributes Reiss's paper to Koppel** (section "Formal treatments").
3. **The definition and the formula agree** on all ten cases that `kn-tests.l4` checks them on (a search over every apportionment, against Koppel's and Reiss's smallest majority), and the solver proves the bound universally for four of them.
   Tiferet Yisrael's rule agrees with Koppel's on every example Tiferet Yisrael gives, and fails on R. Heller's and on Gewirtz's two counterexamples.
4. **Bartenura's decree reproduces 2:3**: one rule (each departure costs a pair; the middle nests twice a round trip) gives all three of the text's tables, and the "some say" variant gives five.
5. **The cover reproduces 3:6's first numbers**: Bartenura's possible shortfalls, covered species by species, give 1, 2, 3 and 4.
6. **1:3's count needs neither reason nor owner**: the text's "whether for one reason or two, one woman or two" is borne out by a rule that takes neither as an input.

## Open questions for a domain expert

- Is Bartenura's reading of 2:3 (a uniform decree) the one to encode, or is there a reading of the tables by strict worst-case counting?
- 3:4: is "a sin offering and a burnt offering, unassigned and designated" Bartenura's two women and three nests, or Maimonides' three heaps (8:10–11)? The count is the same here (two); the attribution may not be.
- Maimonides' reading of 3:2 (F3(d)): what does he hold of the smaller owner, and of three or more owners where no one owner must straddle the line?
- 3:6's last two cases: which derivation of five, six and seven (eight) is right?
- Should the filing grammar (F10) stand?

## Before relying on it

No domain expert has read this encoding against the text.
No independent test author has written tests from the sources without seeing it (the encoding-a-subject skill's step 8), and Koppel's own article and book were not obtained.
The status is `draft`.
