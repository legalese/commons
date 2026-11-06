# Disability Discrimination Act 1992 (Cth) -- baseline encoding, the person at work

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The rules are in one module (`dda-rules.l4`), the
questions in a seat module that imports them and never restates a rule (`dda-seat.l4`), and the cases in `dda-cases.l4`.

The focus asked for is the provisions a claimant meets, in the employment area. The Act's claims machinery for work is
Part 1 (the definitions of disability, associate, carer and aid, and of discrimination), Part 2 Division 1 (work), the
work limb of Division 3 (harassment in employment), Division 4's victimisation and advertisement offences, the Division 5
exemptions that reach work, Division 6 (victimisation), and Part 7's liability rules. Those are encoded whole, except as
listed under Scope.

The Act sets no time limit and no remedy of its own. A complaint goes to the Australian Human Rights Commission, and from
there to the Federal Court or the Federal Circuit and Family Court, under Part IIB of the Australian Human Rights
Commission Act 1986; s 125 says this Act gives no right of action itself. The time limits a claimant meets are in that
Act, not this one, and are not encoded here.

## Edition

- **Act:** Disability Discrimination Act 1992, No. 135, 1992, Compilation No. 40 (compilation date 1 July 2026, register
  id C2026C00276), deposited at `../../registers/source-bundle/C2004A04426.txt` (text sha256
  a77792d79d7cbf2dd38254960b2e86835ef2203bc6067da69ec927d26a000a8a as committed, per its `.meta.json`), a plain-text
  conversion of the Word file from the Federal Register of Legislation, retrieved 13 October 2026.
- **Caveat from the deposit:** "The version in force from 2026-10-08 has no registered compilation yet; this text is the
  latest compilation (No. 40, in force from 2026-07-01), so amendments commencing on or after that date may be missing."
  The endnotes show that the Treasury Laws Amendment (Genetic Testing Protections in Life Insurance and Other Measures)
  Act 2026, Schedule 1 items 5 and 6, commenced on 8 October 2026 and that s 46 was amended in 2026 (finding 3). **s 46 as
  encoded may be out of date for life insurance from 8 October 2026.**
- **Numbers set elsewhere:** the Act's own tests need none from a regulation. The Disability Discrimination Regulations
  (not deposited) prescribe animal training organisations (s 9(2)(b)), laws (s 47(2)) and combat duties (s 53); each is
  asked as a fact. The value of a penalty unit (s 44) is set by the Crimes Act 1914, not deposited; the answer is in
  penalty units.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read; two
deliberately wrong assertions were run once in a scratch copy, since deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `dda-rules.l4` | 0 | 0 | 0 | 0 |
| `dda-seat.l4` | 0 | 0 | 0 | 0 |
| `dda-cases.l4` | 0 | 0 | 192 | 192 |

Every exported question has cases, with the edges: each head of the disability and associate definitions and the two
unnamed relations; each limb of s 9(2) alone and the half-trained animal; each limb of ss 5 and 6 with each of its
defeaters (unjustifiable hardship, a reasonable requirement); every position against a listed and an unlisted act; a
partnership of 2 and of 3 (s 18); every head of s 12, s 12(5) and (6) tried outside their sections, and s 20 with no head;
s 21A against every limb of s 21A(4), including deciding who is offered promotion and a partner's denied benefit; each
Division 5 exemption and each of its limits (s 45(2)(a), (b), s 46 with and without data, s 8(3) for s 48, s 7(3) for
s 53, s 54A only with an assistance animal); s 15(3) against s 15(1)(a), (b) and (c); harassment by each kind of person,
by a customer, and outside the reach; victimisation for each kind of act, for a believed act, and without a detriment or
the ground; s 123(5).

## Seat

**The person at work** (`dda-seat.l4`): the job seeker, employee, commission agent, contract worker, partner or would-be
partner, holder of or applicant for a professional or trade authorisation, applicant or member of a registered union or
employer organisation, or employment agency client, who has a disability, or whose associate has one, or who has a carer,
assistant, assistance animal or disability aid. "Do I have a disability under the Act?", "Is this person my associate?",
"Does the Act count what helps me?", "Did they discriminate against me?", "Which section covers what was done to me?",
"Does the Act reach it?", "Does the inherent requirements exception apply?", "Is what was done to me unlawful?", "Is the
harassment unlawful?", "Was I victimised?", "What can they be sentenced to?", "Is my employer answerable for its
people?", "Is the person who caused it answerable?", "What is the penalty for the advertisement?", "Am I barred from
complaining under this Act?".

No seat for the Commission, the Commissioner, a tribunal or a court. No employer seat was written; one would ask the same
rules from the other side.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; the regulations are not deposited and their
  three prescriptions are asked.
- **The actors the text names.** Followed: the aggrieved person, the discriminator, employer, principal, commission
  agent, contract worker, partners, qualifying body, registered organisation, employment agency, associate, carer,
  assistant, the Commission.
- **Judgments answered conditionally.** Followed: less favourable treatment and the comparator (s 5), unjustifiable
  hardship (ss 5(2), 6(2), 11, 21B), reasonableness of a requirement (s 6(3)), inherent requirements (s 21A), "reasonably
  intended" (s 45), reasonableness under s 46, "reasonably necessary" (ss 48, 54A), "harass" (s 35), whether a provision
  gives effect to a treaty (s 12(8)), "could reasonably be understood as indicating" (s 44), and due diligence (s 123)
  are inputs, worded "have they proved" where the Act puts the burden on them (ss 6(4), 11(2), 123).
- **The Act's definitions worked out; borrowed terms asked.** Followed: disability, associate, carer or assistant,
  assistance animal, disability aid, discriminate, reasonable adjustment, the s 12 reach and its definition of Territory
  are worked out; "harass", trading or financial corporation, registered organisation, disability support pension, fair
  work instrument and Commonwealth employee are asked.
- **One case.** One act (or proposed act) against one person, by one other person.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input ("aggrieved person" is "you").
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 4 (disability, associate, relative, employment, reasonable adjustment, Territory); ss 5, 6, 7(1), (3), 8(1),
(3), 9, 10, 11 (folded into the hardship input); s 12 (the reach of the limited application provisions); s 13(4); ss 15,
16, 17, 18, 19, 20, 21(1), 21A, 21B; s 35; s 42 with s 123(5); s 44; ss 45, 46, 47, 48, 52, 53, 54, 54A(4), (6), 58;
s 58A; ss 122, 123(2), (4).

**Regulative rule:** one. s 58A(1) as a prohibition (`SHANT`) on the other person, with `LEST BREACH ... BECAUSE` naming
s 58A and the s 42 offence; run by EVALTRACE inside "Was I victimised?", which takes only plain facts. No other provision
puts a duty with a period on anyone the person meets: the work provisions say "It is unlawful", without a period.

**Out, and why:**
- Part 2 Division 2 (ss 22-30: education, premises, goods and services, accommodation, land, clubs, sport, Commonwealth
  laws and programs, requests for information): other areas, outside the employment focus; worth their own seat later.
- Division 2A (ss 31-34, disability standards): the standards are not deposited and none is about work.
- ss 37, 39 (harassment in education and services): outside the focus.
- s 43 (incitement offence): an offence by third parties the person rarely meets; s 122 covers their civil liability.
- s 49 (charities' governing rules), s 51 (pensions under listed Acts), s 54A(2), (5), (7) (control of the animal,
  evidence may be asked for, damage): not about work, or permissions rather than exemptions from a claim.
- ss 55-57 (the Commission's exemption power, review, notice): Commission machinery; s 58 (the effect of an exemption)
  is in.
- s 7(2), 8(2) (how references are read): applied in the wording of the inputs; ss 7 and 8 combined (an associate's
  carer or aid) is not a separate ground (fork F10).
- s 12(10) (folded into (9)); s 12(14) (folded into (13)).
- s 13(1)-(3), (5); s 14; s 12A: concurrency, the Crown, criminal responsibility.
- s 21(2), (3): an agency need not police employers; noted in s 122.
- s 123(1), (3), (7)-(9) (state of mind): evidence rules; the deeming in (2) and (4) is in.
- s 124: Commonwealth employees' employer is the Commonwealth; glossed in the reach question.
- s 125: no civil action from this Act; stated above.
- Parts 3-6 and ss 121, 126-132: action plans, the Commission's functions, the Commissioner, delegation, immunities,
  secrecy, regulations. Action plans enter only as a s 11(1)(e) factor inside the hardship input.

## Negatives (rulings of 2026-11-04 and 2026-11-05)

Copied word for word from `docs/ENCODING-GUIDE.md` section 5, as the guide requires of each row with `NOTHING-kind` tags:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> **Periods, "where" and scope limits** ... (a) a period the text fixes in its own words ...: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`.

> **Questions with no convention: decide case by case** ... Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule.

How they fall here:
- `JUST FALSE`: "disability ... means" outside (a)-(g); "discriminate has the meaning given by sections 5 and 6"; s 9(1)
  "is one of the following"; s 9(2), (3) "is ... that"; s 12(4) "and not otherwise" (outside every head of reach); every
  exception and exemption ("does not render it unlawful"); s 58A(2) "commits an act of victimisation if"; s 13(4) "if".
- `NOTHING`: the associate list ("includes"); an act ss 15-21 do not list for the position, and a partnership under 3
  (scope limits of the prohibitions' own wording); an act that is not discrimination or not on a covered ground (the
  prohibition does not reach it, and the Act does not say it is lawful); s 35 outside its six relations or without
  harassment in relation to the disability; s 44 and s 122 outside their terms; s 123 outside actual or apparent
  authority.

### Forks

- **F1** s 4 "disability" (h)-(k), `s 4 -- the condition is a disability`: not asked, since they widen when, never what;
  other reading: ask them, and answer NOTHING for none.
- **F2** s 4 "associate", `s 4 -- the person is my associate`: a person I care for who is not my relative answers
  NOTHING; other reading: "includes" is wide enough to take them in (JUST TRUE).
- **F3** s 17(b), `s 17 -- the paragraph`: a contract worker not allowed to start work is "not allowing the contract
  worker to work"; other reading: s 17 does not reach recruitment of contract workers (NOTHING).
- **F4** s 19(c), `s 19 -- the paragraph`: "varying the terms or the conditions upon which it is held" is asked as "the
  terms or conditions of my work or position"; other reading: none, but the two answer choices overlap.
- **F5** s 18(1), (2), `s 18 -- the paragraph`: a would-be partner gets "s 18(1)(a) or (2)(a)" without asking whether the
  partnership exists yet; the number entered is the persons proposing (s 18(1)) or the partners (s 18(2)).
- **F6** s 123(2), (4) "unless ... establishes", `s 123 -- the employer is taken to have done it`: the unless met answers
  JUST FALSE; other reading: NOTHING (the employer may still be liable on its own conduct or under s 122).
- **F7** s 6(2)(c), `s 6(2) -- ...`: the disadvantage of "the failure to make reasonable adjustments" is asked with the
  same input as the requirement's disadvantage under s 6(1)(c); other reading: two inputs.
- **F8** s 58A(1), `s 58A(1) -- the other person must not victimise me`: the prohibition has no period; `WITHIN 1` stands
  for the one period the question is asked about, so that a trace with no act ends FULFILLED.
- **F9** Division 5 and s 35: none of the exemptions is applied to harassment; most are framed as "discriminate", and
  s 47's and s 58's "anything done" / "an act" could in theory excuse harassment; other reading: apply ss 47 and 58.
- **F10** ss 7 and 8 combined: an associate's carer, assistant, animal or aid is not offered as a ground; other reading:
  add it (the note to s 7 says the Act applies).
- **F11** s 12(8) for s 35, `s 12 -- the Act reaches what was done`: the treaty head is applied to harassment though it
  speaks of "discrimination against a person with a disability"; other reading: not for Division 3.
- **F12** s 54A(4), `Division 5 -- the exemption that applies`: applied to any ground where the person has an assistance
  animal; s 54A(6) only to the ground of having it, as its words say.
- **F13** s 13(4), `s 13(4) -- I am barred ...`: no State complaint answers JUST FALSE (the "if" fails); the right to
  complain itself is in the Australian Human Rights Commission Act 1986, not answered here.
- **F14** s 42, `s 42 -- the most months of imprisonment`: no victimisation answers JUST 0 rather than NOTHING; for a body
  corporate the 6 months is converted to a fine by the Crimes Act 1914 (not deposited), not computed.

## What the Act turns out to say

1. **The work provisions do not reach every employer.** They are "limited application provisions" (s 12(1)) and have
   effect only as s 12 provides "and not otherwise" (s 12(4)). "Territory" in s 12(3) excludes the ACT and the Northern
   Territory (s 4(1)), so an act there is reached only through another head. An unincorporated employer (a sole trader,
   a partnership) in a State, when no other head of s 12 applies (Commonwealth power, banking or insurance, interstate or
   overseas trade, matters outside Australia), is reached only if a court accepts the treaty head in s 12(8). Section 20 (registered organisations) and s 58A (victimisation) are not limited and reach
   everywhere. Asserted.
2. **"Associate" runs one way for carers.** Head (d) makes "a carer of the person" their associate; it does not name the
   person a carer cares for. An unrelated carer treated badly because of the disability of the person they care for is
   not within a named head and depends on the open word "includes". Asserted (NOTHING).
3. **The endnotes disagree on the 2026 amending Act.** Endnote 3 lists the Treasury Laws Amendment (Genetic Testing
   Protections in Life Insurance and Other Measures) Act 2026 as No. 35, 2026, Schedule 1 items 5 and 6 commencing 8
   October 2026; endnote 4 records s 46 as "am No 36, 2026". One number is wrong, and the s 46 text deposited (compiled to
   1 July 2026) may not show the amendment.
4. **The inherent requirements and unjustifiable hardship exceptions do not reach harassment or victimisation.** ss 21A
   and 21B say "This Division" (Division 1); harassment is Division 3 and victimisation Division 6. Asserted (harassment
   is unlawful with no s 21A or s 21B input to take it out).
5. **"Reasonably" qualifies only a past assertion of rights.** s 58A(2)(f) and s 42(2)(f): "has reasonably asserted, or
   proposes to assert". Proposing to assert rights unreasonably is still protected. Asserted.
6. **s 21A(4) treats partners differently from employees.** It takes s 15(2)(b) (an employee's denied benefits) out of the
   inherent requirements exception, but not s 18(3)(a) (a partner's denied benefits); only s 18(3)(c) is taken out.
   Asserted.
7. **s 35 is narrower than "harassment at work".** Its six relations are employer, co-employee, prospective employer,
   principal, fellow agent or contract worker of the same principal, and prospective principal. Harassment by a customer
   or client is outside it, and "harass" is not defined. Asserted (NOTHING for a customer).

## Before relying on it

- Check s 46 against the text in force from 8 October 2026 when a compilation is registered, and settle finding 3.
- Deposit the Disability Discrimination Regulations and work out the prescribed organisations, laws and combat duties.
- Encode the Australian Human Rights Commission Act 1986 Part IIB (complaint, termination, time limits, court
  application, remedies), which is where a claim under this Act is made; link it here.
- An independent test pass and a human gate; a lawyer's view on forks F2, F6, F9 and F11.
- An employer seat, and Division 2 for the other areas.
