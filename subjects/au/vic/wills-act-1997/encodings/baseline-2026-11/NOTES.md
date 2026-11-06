# Wills Act 1997 (Vic) -- baseline encoding, the will-maker and the family

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The rules are in one module (`wills-rules.l4`), the
dates in another (`wills-dates.l4`, built-in date functions only, no daydate), and the questions in two seat modules that
import the rules and never restate one: `wills-seat.l4` (the will-maker) and `wills-seat-family.l4` (the family and
beneficiaries after a death). Each seat has its own case file.

The focus asked for: making, altering and revoking wills; informal wills; rectification. Those are Parts 2 and 3 of the
Act. The rules a beneficiary meets when a gift fails (ss 35, 39, 45, 46(3)), the domestic partner definition and who may
see a will (s 50) are added because a claim on an estate starts from them. Family provision claims are under Part IV of
the Administration and Probate Act 1958, not this Act; it is not deposited.

## Edition

- **Act:** Wills Act 1997, Act No. 88/1997, Version No. 036, incorporating amendments as at 26 April 2021 (the current
  version when read on 6 November 2026), deposited at `../../registers/source-bundle/wills-act-1997.txt` (sha256
  84edc4ea...7d385a3bd as committed, per its `.meta.json`), a plain-text conversion of the Word file the owner saved by hand
  on 6 November 2026 (see that file's `.meta.json` and `subjects/au/vic/README.md`). Not checked against the authorised
  PDF, which was not saved.
- **Numbers set elsewhere:** none of the Act's own tests needs a number from a regulation. The Registrar's estate limit
  under s 9(5) is set by the Court, not in a deposited instrument, and is asked. No class of special witness is prescribed
  in a deposited instrument (s 3, "prescribed class" is offered as a choice). The commencement of s 49A (1 November 2017)
  is read from the deposited endnotes, which are not part of the Act (finding 6).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch copy, since deleted, and showed as "assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `wills-dates.l4` | 0 | 0 | 0 | 0 |
| `wills-rules.l4` | 0 | 0 | 0 | 0 |
| `wills-seat.l4` | 0 | 0 | 0 | 0 |
| `wills-seat-family.l4` | 0 | 0 | 0 | 0 |
| `wills-cases.l4` | 0 | 0 | 111 | 111 |
| `wills-cases-family.l4` | 0 | 0 | 84 | 84 |

Every exported question has cases, with the edges: age 17 and 18 (ss 5, 20); one and two witnesses, a second witness who
was not present at the signing (s 7(1)(c)); every missing step of the remote procedure (s 8A); a will executed on 31
October and on 1 November 2017 (ss 49A, 56); a beneficiary dying on the 30th and the 31st day after the will-maker, on the
same day, before, and across 29 February 2028 (ss 39, 45); an estate at, just under and just over the Registrar's limit
(s 9(5)); an application on the last day of the six months, the day after, on the day of the grant, a grant on 31 August
(last day 29 February 2028) and on 31 March (last day 30 September) (s 31(2)); every constructor of every choice.

**No mirror cases.** The two seats ask different questions; no rule is asked from both, so there are no facts to mirror.

## Seats

**1. The will-maker** (`wills-seat.l4`): the individual making, changing or revoking a will in Victoria, including a minor
and a person whose will was made by Court order who has regained capacity. "Is my will valid as to my age?", "Is my will
properly signed and witnessed, in person or by video link?", "Is my change effective?", "Have I revoked my will?", "Does
my marriage revoke my will?", "What does my divorce revoke?", "Is my revoked will revived?", "Is my executor's charging
clause valid?".

**2. The person with an interest in a deceased person's will** (`wills-seat-family.l4`): a beneficiary, the spouse,
domestic partner, child or other relative, a person who would take on intestacy, a creditor; and the relative applying
for a Court-authorised will for someone who lacks capacity. "Was I the deceased's domestic partner?", "Can I see the
will?", "Can the Court accept an unsigned document as the will?", "Can the will be rectified, and by when must I apply?",
"What becomes of a gift to someone who died within 30 days?", "Can the Court authorise a will for my relative?".

No seat for the Supreme Court, the Registrar, or the personal representative (executor or administrator). The Court's and
the Registrar's satisfactions and orders are asked as facts. The personal representative's protections (ss 31(4), 39(4),
(5), 47(3)) would belong to a further seat; see Scope.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; no deposited instrument sets a number here.
- **The actors the text names.** Followed: the testator (the will-maker), witnesses, the special witness, the substitute
  signatory, the spouse, divorced spouse and domestic partner, beneficiaries and issue, the Court, the Registrar, the
  personal representative, the applicant, the attorney, guardian and administrator.
- **Judgments answered conditionally.** Followed: "the Court is satisfied" (ss 9, 12(2)(g), 20, 21B, 31), "if it appears
  that the testator did not want" (s 14(2)), "in the opinion of the Court, a genuine interest" (s 21C), "on a genuine
  domestic basis" (s 3), "reasonably satisfied" (s 8A(7)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "minor", "domestic partner", "special witness",
  "divorce" (s 14(4)) are worked out; "registered relationship" (Relationships Act 2008), "remuneration clause"
  (Administration and Probate Act 1958), "document" for s 9 (Interpretation of Legislation Act 1984), testamentary capacity
  (common law) and whether execution conforms to a foreign law are asked.
- **One case.** One will (or one gift, one document, one application), seen by one person.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input ("testator" is glossed as the will-maker).
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3 (minor, domestic partner, special witness); ss 5, 6 (minors); s 7(1), (5)-(7), s 8, s 8A, s 10, s 11
(execution, remote execution, witnesses); s 17(1), (2)(b) (wills made under another law); s 12 (revocation), s 13
(marriage), s 14 (divorce), s 15 (alteration), s 16 (revival); s 19E(2) (no remote execution for international wills);
s 20(1)-(5) (minors' wills by Court order); ss 21, 21B, 21C, 24, 25(1), (2), (5) (Court-authorised wills for a person
without testamentary capacity); s 9(1), (2), (5) (informal wills and revocations); s 31(1)-(3) (rectification and its time
limit, with s 31(2) as a regulative rule); ss 35, 39(1)-(3), 45, 46(3) (failed gifts, 30-day survival, substitution of
issue); s 49A with s 56 (remuneration clauses); s 50 (who may see a will).

**Regulative rule:** one. s 31(2): the applicant DOes the application WITHIN the days from the grant to the last day of the
six months (day 0 the day of the grant), LEST BREACH, the breach being the loss of the right to apply without an extension
(s 31(3)). Run by EVALTRACE inside an exported question that takes only dates and facts, through the helper the County
Court Act 1958 encoding uses. No other provision sets a duty with a period for the individual.

**Out, and why:**
- ss 1, 2, 50A, 51 and Part 6 (purpose, commencement, regulations, repeal, transitional): machinery. s 52 makes most of
  the Act apply only to wills made after its commencement; that date is not in the deposited text, and every question
  assumes a will made after it (and, for s 14, a divorce after it). s 57 (wills witnessed under the 2020 COVID-19
  regulations stay valid) is noted, not encoded.
- s 4 (what property may be disposed of by will): no test the will-maker meets; a definition of reach.
- s 8B (which document is the will after remote execution), s 8C (recording), s 8D: evidence and procedure; s 8C(2) is
  noted in the remote execution rule.
- ss 16A, 17(2)(a), (c), (d), (3), 18, 19 (vessels, revoking and power-of-appointment wills, which foreign system applies):
  conflict-of-laws detail for the Court; s 17(1) and (2)(b) are in.
- ss 19A-19D and the Schedule (international wills under the Washington Convention): a separate form with an authorised
  person and a certificate; worth its own question later.
- s 20(6)-(9), s 25(3), (4) (the Registrar as witness, deposit and withdrawal): Registrar machinery; s 20(6) is in the
  question's description.
- ss 21A, 21D, 22 (information the Court may require, separate representation, how it hears the application): the Court's
  procedure. s 30 (statutory wills made elsewhere): recognition, noted.
- s 31(4), s 39(4), (5), s 47(3) (the personal representative's protection when distributing): the personal
  representative's seat, not the individual's here. s 32 (the order attached to the grant): the Court's duty.
- Part 4's other construction rules (ss 33, 34, 36-38, 40-44, 46(1), (2), 47, 48, 49): rules for reading a will, applied by
  the Court and the personal representative; outside the focus. ss 35, 39, 45 and 46(3) are in.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 5, 6 -- `ss 6, 20 -- I may revoke my will although a minor` -- a minor outside s 6 and without an order:
  NOTHING (s 5 speaks of making a will, not revoking) -- JUST FALSE (the s 6 grants imply no other minor may revoke). A
  minor's alteration is not encoded; it would follow making.
- **F2** ss 7(1)(c), (d), 10 -- `s 7(1), 10 -- my will is validly executed in person` -- a person unable to see the
  signing is not counted at all, and the attesting witnesses are counted only among those present at the signing --
  counting every person present and applying s 10 only to the attesting witnesses.
- **F3** s 8A, with s 7(7) -- `ss 7(5), 8A, 19E(2) -- my will is validly executed by the remote execution procedure` -- any
  step of s 8A missed ("must", not done): JUST FALSE, since presence by audio visual link counts only "in accordance with
  the remote execution procedure" -- NOTHING (the will may still meet s 7(1) through the witnesses physically present, or
  be admitted under s 9).
- **F4** s 12(2)(da) "by a later will" -- `s 12 -- my will is revoked by what I did` -- whether a later will revokes the
  earlier (an express clause or inconsistency, common law) is asked as a fact -- every valid later will revokes.
- **F5** s 14(1)(b), (c) "other than" -- `ss 12, 14 -- my divorce revokes this part of my will` -- the excepted power of
  appointment and trusteeship are not revoked: JUST FALSE (s 12(2) closes the ways a will is revoked) -- NOTHING.
- **F6** s 15(2) -- `s 15 -- my alteration is effective` -- an obliterating alteration: NOTHING (s 15(2) disapplies s 15(1)
  and says no more) -- JUST TRUE, as a revocation of that part under s 12(2)(g).
- **F7** ss 39(1), 45(1)(b) -- `ss 39, 45 -- the beneficiary did not survive the will-maker by 30 days` -- the day of the
  will-maker's death excluded; death on the 30th day after is "within 30 days" and is not surviving "for thirty days"; the
  two sections counted alike -- the 30th day counted as surviving.
- **F8** s 31(2) "within 6 months from the date of the grant" -- `s 31(2) -- the last day to apply for rectification` --
  the day of the grant excluded (Interpretation of Legislation Act 1984 s 44(1), borrowed), ending on the same day-number
  six calendar months later, or the last day of a shorter month; no roll-forward for a weekend or holiday -- counting the
  day of the grant, or rolling to the next day the registry is open.
- **F9** ss 35(2), 39(2), 45(3), 46(4) -- `ss 35, 39, 45, 46 -- what becomes of the gift` -- one input for a contrary
  intention displacing all four (s 35(2) allows one shown "elsewhere"; the others only "in the will") -- one input per
  section.
- **F10** s 14(4)(a), (b) -- `ss 12, 14 -- my divorce revokes this part of my will` -- "a decree of dissolution ...
  becoming absolute" read as a divorce order taking effect under the Family Law Act 1975 as now worded, and "the Family
  Court of Australia" as including its successor (finding 3) -- the words read literally.
- **F11** s 31(3) -- `s 31(2), (3) -- where my rectification application stands` -- where the Court has extended the time,
  the answer is "extended" whatever the distribution input (the extension is taken to have been made before the final
  distribution) -- an extension is ineffective if the estate was finally distributed first.
- **F12** s 49A "is void unless" -- `s 49A -- the remuneration clause in my will is not void` -- answered as "not void"
  (JUST TRUE) when both consents hold; the Act does not say the clause is otherwise valid -- NOTHING when both hold.

Sites decided without a fork line: s 11, s 17 when no law is met, s 20 for an adult, s 24 without regained capacity,
s 9(2) for an executed writing, s 15 before execution and s 49A before 1 November 2017 answer NOTHING (limited by their own
wording or silent); s 21C and s 50 outside their lists answer NOTHING (lists not closed with "only").

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "is not valid" (s 5), "is not valid unless" (ss 7(1), 25), "may not be revoked except" (s 12(2), a closed
list), "is not effective unless" (s 15(1)), "is void unless" (s 49A), "must not make an order ... deceased" (s 21(3)),
"must be satisfied" before an order (ss 20(5), 21B), "cannot be used for international wills" (s 19E(2)), the "means"
definitions of minor, domestic partner and divorce, the "if" conditions of ss 9(1), 9(2), 31(1), 39(1), and the "where" of
s 9(5) give `JUST FALSE`; the period of s 31(2) gives the deadline; the sites listed under the fork register give `NOTHING`.

## What the Act turns out to say

1. **A widowed or divorced minor can revoke but not make.** s 6(c) lets a minor "who has been married" revoke a will made
   while married or in contemplation of that marriage, but s 6(b) covers only a minor "who is married", so after the
   marriage ends s 5 again invalidates any new will (unless made in contemplation of another marriage, or by Court order).
   A 17-year-old widow may revoke the will she made as a wife and is then left intestate until 18. Asserted.
2. **Domestic partners are spouses for some purposes but not for revocation.** s 13 revokes a will on marriage and s 14
   revokes gifts to a former spouse on divorce, but neither speaks of a domestic partner, and s 12(2) closes the ways a will
   is revoked. Starting a domestic relationship does not revoke a will, and ending one leaves the former partner's gifts
   and executorship in place, though ss 11, 31(4), 39(4) and 50 put domestic partners beside spouses. Asserted.
3. **s 14(4) names a court and a decree that have since changed.** "A decree of dissolution of the marriage becoming
   absolute" is the Family Law Act 1975's wording before 2005 (now a divorce order taking effect), and "the Family Court of
   Australia" became the Federal Circuit and Family Court of Australia (Division 1) on 1 September 2021, after this version
   (26 April 2021). Nullity decrees made by other courts with family jurisdiction are not named at all. Read as covering the
   current forms (F10); a lawyer should confirm. Not separately asserted.
4. **Two meanings of "document".** s 3 defines a document as "paper or material on which there is writing" (plus an
   electronic document only under the remote procedure), but s 9(6) gives s 9 the Interpretation of Legislation Act 1984
   meaning, which reaches electronic records. So a will must be on paper to be formally valid, but an unsent text message or
   a video can be admitted as an informal will. Noted in the s 9 question.
5. **The rectification clock and the executor's safe harbour run together.** s 31(2) gives six months from the grant;
   s 31(3) lets the Court extend it "but not if the final distribution of the estate has been made"; and s 31(4)(b)
   protects a personal representative who distributes at least six months after the grant without notice of an
   application. A beneficiary who misses the six months can lose the remedy by the executor distributing. Asserted (the
   distributed case).
6. **s 49A's start date is only in the endnotes.** s 56 confines s 49A to wills executed "on or after the commencement of
   that section" but the Act does not say when that was; the endnotes give 1 November 2017 (No. 41/2017 ss 28-30), and the
   endnotes do not form part of the Act. Used, and asserted at 31 October and 1 November 2017.
7. **Surviving "within 30 days" and "for thirty days".** s 39(1) speaks of a beneficiary "who dies within 30 days after the
   death of the testator", s 45(1)(b) of issue who "do not survive the testator for thirty days", and s 45(4)(b) of one who
   "did not survive the testator by 30 days". The three are read alike (F7). Asserted at the 30th and 31st day.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- The Administration and Probate Act 1958 (family provision under Part IV, the Registrar, remuneration clauses, the
  deposit of wills), the Relationships Act 2008, the Interpretation of Legislation Act 1984 (s 44, time) and any
  regulations under s 50A (special witness classes, remote execution), none deposited.
- A lawyer's view on findings 2, 3 and 4 and forks F3, F5, F6 and F8; an independent test pass and a human gate.
