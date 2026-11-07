# Wills Act 2000 (NT) -- baseline encoding, the will-maker and the family

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The rules are in one module (`wills-rules.l4`), the
dates in another (`wills-dates.l4`, built-in date functions only, no daydate), and the questions in two seat modules that
import the rules and never restate one: `wills-seat.l4` (the will-maker) and `wills-seat-family.l4` (the family and
beneficiaries after a death, and a relative seeking a will for someone without capacity). Each seat has its own case file.

The focus was the Act as one of the wills Acts behind claims on estates. The Act is small enough to take nearly whole:
Parts 2 and 3 (capacity, execution, revocation, alteration, revival, Court-authorised wills, informal wills,
rectification), the Part 4 rules on gifts that fail, Part 5 and 5A (wills made under another law, international wills),
Part 6 (deposit) and Part 7 (seeing a will, maintenance in the first 30 days). Family provision claims are under the
Family Provision Act 1970, a separate subject (`subjects/au/nt/family-provision-act-1970`), not this Act.

## Edition

- **Act:** Wills Act 2000 (NT), Act No. 59, 2000, reprint REPW007 as in force at 1 January 2022 (the current reprint
  when read on 6 November 2026), deposited at
  `../../registers/source-bundle/Wills-Act-2000-NT-current-reprint-REPW007.txt` (text sha256 e67f2236...9df3453213 per its
  `.meta.json`), converted from the register's Word reprint. Not checked against the authorised PDF.
- **Numbers set elsewhere:** the deposit fee (s 50(3), (4)) and its waiver rules, and any prescribed person (s 49), are
  set by Regulations that are not deposited. No question needs the fee amount; the Public Trustee is the default
  prescribed person (s 49(3)).
- **Commencement:** 1 March 2001 (from the endnotes). Every question assumes a will executed on or after it, and for
  s 15 a divorce or annulment after it (s 5).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file, since deleted, and showed as an error, "assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `wills-dates.l4` | 0 | 0 | 0 | 0 |
| `wills-rules.l4` | 0 | 0 | 0 | 0 |
| `wills-seat.l4` | 0 | 0 | 0 | 0 |
| `wills-seat-family.l4` | 0 | 0 | 0 | 0 |
| `wills-cases.l4` | 0 | 0 | 106 | 106 |
| `wills-cases-family.l4` | 0 | 0 | 89 | 89 |

Every exported question has cases, with the edges: age 17 and 18 (ss 7, 18); one and two witnesses, a witness who signed
but was not present at the signing (s 8(1)(c)); one and two witnesses who take nothing (s 12(2)(a)); one witness for an
international will; every way of ending a marriage and every part of a will under s 15; a beneficiary dying on the same
day, before, on the 30th and on the 31st day after the will-maker, and across 29 February 2028 (ss 34, 40); a maintenance
payment on the day of death, the 30th day, the 31st day and the day before the death (s 55); an application to rectify on
the day of death, on the last day of the six months, and the day after, with a death on 31 August (last day 29 February
2028) (s 27(2)); age 17 and 18 for getting a deposited will back (s 51(2)); every constructor of every choice.

**No mirror cases.** The two seats ask different questions; no rule is asked from both.

## Seats

**1. The will-maker** (`wills-seat.l4`): the individual making, changing, revoking or depositing a will in the Northern
Territory, including a minor and a person whose will was made by Court order. "Can I leave this property by will?", "Is
my will valid as to my age?", "Is my will properly signed and witnessed?", "Is my will made overseas, or as an
international will, valid?", "Have I revoked my will?", "Does my marriage revoke my will?", "What does my divorce
revoke?", "Is my change effective?", "Is my revoked will revived?", "Can I deposit my will, at what fee, and get it
back?".

**2. The person with an interest in a deceased person's will** (`wills-seat-family.l4`): a beneficiary, the surviving
spouse, a child or other relative, a person who would take on intestacy, a creditor, the executor named in the will
(only as a person asking for the will), and the relative applying for a Court-authorised will for someone who lacks
capacity. "Can I see the will?", "Can I have the deposited will?", "Can the Court accept an unsigned document as the
will?", "I witnessed the will: is my gift void?", "Can the will be rectified, and by when must I apply?", "What becomes
of a gift to someone who died within 30 days?", "Can the executor pay me maintenance now?", "Can the Court give leave
for a will for my relative?".

No seat for the Supreme Court, the Registrar, the prescribed person (the Public Trustee) or the personal representative
as decision-maker. Their satisfactions, orders, waivers and choices are asked as facts. The personal representative's
protections (ss 27(5), 55(2)) would belong to a further seat; see Scope.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; the Regulations setting the deposit fee are not
  deposited, and no question needs the amount.
- **The actors the text names.** Followed: the testator (the will-maker), witnesses, the spouse and former spouse,
  beneficiaries and issue, the Court, the Registrar, the prescribed person, the personal representative, the executor,
  the applicant, the authorised person for an international will, the person in possession of a will.
- **Judgments answered conditionally.** Followed: "the Court is satisfied" (ss 10, 12(2)(c), 13(f), 18(2), 21, 27(1)),
  "if the Court thinks it is just" (s 27(3)), testamentary capacity (common law), "wholly or substantially dependent"
  (s 55) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "minor" and the s 15(2) ways a marriage ends are
  worked out; recognition under the Family Law Act 1975, conformity with a foreign law (s 46), entitlement on intestacy,
  letters of administration and whether a later will revokes are asked.
- **One case.** One will (or one gift, one document, one application), seen by one person.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input ("testator" glossed as the will-maker).
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3 (minor); s 6 (what may be left); s 7 (minors); s 8, s 9, s 11 (execution, witnesses); s 10 (informal wills);
s 12 (gifts to witnesses); s 13 (revocation); s 14 (marriage); s 15 (divorce and annulment); s 16 (alteration); s 17
(revival); s 18(1), (2), (4) (minors' wills by Court order); ss 19(3), 21 (leave for a will for a person without
capacity); s 25(2) with s 51(1), (2) (getting a deposited will back); s 27(1)-(4) (rectification and its time limit, with
s 27(2) as a regulative rule); ss 30, 34, 40, 41(2) (failed gifts, 30-day survival, substitution of issue, fractional
shares); s 46(1), (2) (wills made under another law); ss 48B-48F and Annex Arts 1-5 (international wills); s 50(2), (4)
(deposit); s 51(3), (4) (the deposited will after death); s 54 (who may see a will); s 55(1) (maintenance in the first 30
days).

**Regulative rule:** one. s 27(2): the applicant DOes the application WITHIN the days from the death to the last day of
the six months (day 0 the day of death), LEST BREACH, the breach being the loss of the right to apply without an
extension (s 27(3), (4)). Run by EVALTRACE inside an exported question that takes only dates and facts. No other
provision sets a duty with a period for the individual; s 54's duty to allow inspection has no period and is asked as an
entitlement.

**Out, and why:**
- ss 1, 2, 4, 5, 56-58 and the Schedule (title, commencement, purpose, application, regulations, repeal, savings):
  machinery. s 5 is taken as an assumption (a will executed after 1 March 2001).
- ss 18(3), (5), (6), 19(1), (2), (4), 20, 22-24, 25(1), (3), 26 (the Court's conditions and procedure, the Registrar's
  duties, what the leave application must contain, recognition of minors' and statutory wills made elsewhere): the
  Court's and Registrar's procedure. s 20(2)'s list of what to file is not encoded.
- s 27(5), (6), s 55(2)-(5) (the personal representative's protection, the order attached to the will, deduction and
  administration expense): the personal representative's seat; s 55(3)-(5) are in the question's description.
- Part 4's other construction rules (ss 28, 29, 31-33, 35-39, 41(1), 42-44): rules for reading a will, applied by the
  Court and the personal representative; ss 30, 34, 40 and 41(2) are in.
- ss 46(3)-(6), 47, 48 (immovables, revocations, powers of appointment, which foreign system applies): conflict-of-laws
  detail for the Court. Annex Arts 5(2), 6-15 (a testator unable to sign, placing of signatures, date, certificate,
  safekeeping, revocation, interpretation): outside the Arts 2-5 that decide validity in form (finding 6).
- s 49, ss 52, 53 (who is prescribed, examination, failure to retain): the prescribed person's machinery. s 51(5), (6):
  copies and directions.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 7 -- `ss 7, 18 -- I may revoke my will although a minor` -- a minor outside s 7(2) and without an order:
  NOTHING (s 7(1) speaks of a will "made", not revoked) -- JUST FALSE (the s 7(2) grants imply no other minor may revoke).
- **F2** ss 8(1)(b), (c), 11 -- `ss 8, 11 -- my will is validly executed` -- a person unable to see the signing is not
  counted at all, and the attesting witnesses are counted only among those present at the signing -- counting every person
  present and applying s 11 only to the attesting witnesses.
- **F3** s 13(c) "by a later will" -- `s 13 -- my will is revoked by what was done` -- whether a later will revokes the
  earlier (an express clause or inconsistency, common law) is asked as a choice -- every valid later will revokes.
- **F4** s 15(2)(a), (b) -- `s 15 -- my divorce revokes this part of my will` -- "a decree of dissolution ... becomes
  absolute" read as a divorce order taking effect under the Family Law Act 1975 as now worded, and "the Family Court" as
  including its successor (finding 4) -- the words read literally.
- **F5** s 16(1)(e), (3) -- `s 16 -- my change to my will is effective` -- an obliterating alteration: NOTHING ((3)
  disapplies the section, (1)(e) lists it) -- JUST TRUE under (1)(e).
- **F6** ss 34(1), 40(1)(d), 55(1) -- `ss 34, 40 -- the beneficiary did not survive the will-maker by 30 days` and `s 55 --
  the personal representative may pay me maintenance now` -- the day of the will-maker's death excluded; death on the
  30th day after is "within 30 days" and is not surviving "for 30 days"; the 30th day is still "before the 30 day period
  expires" -- counting the day of death, or ending the period at the start of the 30th day.
- **F7** s 27(2) "within 6 months after the date of the death" -- `s 27(2) -- the last day to apply for rectification` --
  the day of death excluded (Interpretation Act 1978 (NT), borrowed, not deposited), ending on the same day-number six
  calendar months later, or the last day of a shorter month; no roll-forward for a weekend or holiday -- counting the day
  of death, or rolling to the next day the registry is open.
- **F8** ss 30(2), 34(2), 40(3), 41(3) -- `ss 30, 34, 40, 41 -- what becomes of the gift` -- one input for a contrary
  intention displacing all four (s 30(2) allows one shown "elsewhere"; the others only "in the will") -- one input per
  section.
- **F9** s 19(3) with s 21 -- `ss 19(3), 21 -- the Court may give leave for a will for my relative` -- the person being
  alive (a condition of the order) is required for leave too -- leave tested on s 21 alone.
- **F10** s 27(3), (4) -- `s 27(2)-(4) -- where my rectification application stands` -- where the Court has extended the
  time, the answer is "extended" whatever the distribution input (the extension taken to have been made before the final
  distribution) -- an extension is ineffective if the estate was finally distributed first.
- **F11** ss 25(2)(a), (3), 51(2) -- `ss 25(2), 51(1), (2) -- I can get my deposited will back` -- a statutory will, a
  revocation order, the person still without capacity: NOTHING -- JUST FALSE under s 51(2), or JUST TRUE under s 25(3).
- **F12** s 50(4) "unless" once met -- `s 50(4) -- I must pay the deposit fee` -- no fee: JUST FALSE -- NOTHING (the
  exemption removes the duty but says nothing more).
- **F13** s 15(3) with s 13 -- `s 15 -- my divorce revokes this part of my will` -- a part that does not concern the
  former spouse: JUST FALSE (s 13 closes the ways a will is revoked with "but only") -- NOTHING.
- **F14** s 46(1) "is properly executed if" -- `s 46 -- my will is properly executed under another place's law` -- no
  head met: NOTHING (s 8 and s 10 remain) -- JUST FALSE for s 46's own route.
- **F15** Annex Art 1(1), (2) -- `Part 5A, Annex Arts 1-5 -- my will is valid in form as an international will` -- a
  failure: NOTHING (Art 1(2)) -- JUST FALSE as an international will.

Sites decided without a fork line: s 6 outside its heads, s 10 for an executed document, s 16 before execution, s 17 by
another way, s 18(2) for an adult, s 51(1) without a written application, s 51(3) for others, and s 54 outside its list
answer NOTHING (silent, limited by their own wording, or lists not closed with "only").

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "is not valid" (s 7(1)), "is not valid unless" (ss 8(1), 18(4)), "may be revoked but only" (s 13, a closed
list), "is not effective unless" (s 16(1)), "is void" (s 12(1)), "may not" (ss 6(4), 25(2)), "must refuse leave ...
unless" (s 21), "must not make an order ... unless" (s 19(3)), "must be satisfied" before an order (s 18(2)), "is not to
be deposited unless" (s 50(2)), "does not apply" (s 15(4)), "does not revoke" (s 15(5)), the definition of when a marriage
ends (s 15(2), closed by "but only"), the "if" conditions of ss 10(2), 27(1), 55(1), and the 30-day period of s 55 give
`JUST FALSE`; the period of s 27(2) gives the deadline; the sites listed under the fork register give `NOTHING`.

## What the Act turns out to say

1. **s 16 lists obliteration and then disapplies itself to it.** s 16(1)(e) counts an alteration that "obliterates words
   in the will so that their effect is no longer apparent" as effective, and s 16(3) says the section "does not apply to an
   alteration to a will if the words or effect of the will are no longer apparent because of the alteration". Either way
   s 16 does not invalidate an obliteration; whether the obliterated words are revoked falls to s 13(f) or the common law.
   Answered NOTHING (F5). Asserted.
2. **Only marriage counts.** s 14 revokes a will on marriage and s 15 revokes gifts to a former spouse on divorce or
   annulment, but neither speaks of a de facto relationship, and s 13 closes the ways a will is revoked. Starting a de
   facto relationship revokes nothing; ending one leaves the former partner's gifts and executorship in place; separation
   from a spouse without a divorce does too. Asserted (separation).
3. **s 12 reaches only the witness.** A gift to a witness's spouse or partner is not touched, and s 12(2)(a) saves the
   gift whenever at least two witnesses take nothing, so a beneficiary who is a third witness keeps the gift. Asserted (2
   and 3 non-benefiting witnesses).
4. **s 15(2) names a decree and a court that have since changed.** "A decree of dissolution ... becomes absolute" is the
   Family Law Act 1975's wording before 2005 (now a divorce order taking effect), and "the Family Court" became the Federal
   Circuit and Family Court of Australia (Division 1) on 1 September 2021, before this reprint (1 January 2022), though s 15
   was amended by Act No. 28 of 2021. Nullity decrees by other courts with family jurisdiction are not named. Read as the
   current forms (F4); a lawyer should confirm. Not separately asserted.
5. **Who may see a will is narrower than who may claim on the estate.** s 54 does not name a de facto partner (unless
   named in the will or entitled on intestacy, which is decided by another Act), nor a person entitled to letters of
   administration with the will annexed, though s 51(3) lets that person take the deposited will itself. Asserted
   (NOTHING for both).
6. **An international will's validity turns on Articles 2 to 5 only.** Art 1(1) makes validity in form depend on
   "Articles 2 to 5"; Arts 6-10 (signatures at the end, numbered sheets, the date, the certificate) are framed as "shall"
   but are outside that test, and Art 13 says a missing or irregular certificate does not affect formal validity. Encoded
   so (F15).
7. **A statutory will can be locked in.** s 25(2) lets a Court-authorised will for a person without capacity be withdrawn
   after a revocation order, and s 25(3) has the prescribed person comply with the order, but s 51(2) withholds a deposited
   will from a testator who "lacks testatmentary capacity". Answered NOTHING (F11). Asserted. The deposited text spells it
   "testatmentary" (a typing error in the reprint).
8. **A widowed or divorced minor can revoke but not make.** s 7(2)(c) lets a minor who "has been married" revoke a will
   made while married, but s 7(2)(b) covers only a minor who "is married", so after the marriage ends s 7(1) again
   invalidates any new will unless made in contemplation of another marriage or by Court order. Asserted.
9. **The rectification clock runs from death, and matches the executor's safe harbour.** s 27(2) gives six months after
   the date of death (not from a grant), and s 27(5)(b) protects a personal representative who distributes at least six
   months after the death without notice of an application for rectification or for family provision. A beneficiary who
   misses the six months can lose the remedy when the executor distributes (s 27(4)). Asserted (the distributed case).
10. **"His or her death" in s 55(1).** "An entitlement ... that does not become absolute until 30 days after his or her
    death" is read as the deceased's death (the survivor's death would make no sense). Not separately asserted.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- The Wills Regulations (the deposit fee, waivers, any prescribed person), the Interpretation Act 1978 (NT) (time), the
  Administration and Probate Act (NT) (intestacy, letters of administration), the Family Law Act 1975 (Cth)
  (recognition of overseas divorces), none deposited here.
- A lawyer's view on findings 1, 4, 5 and 7 and forks F2, F4, F5, F7 and F11; an independent test pass and a human gate.
