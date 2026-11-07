# Dust Diseases Tribunal Act 1989 (NSW) -- baseline encoding, the claimant

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 15 November 2024). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Three regulative rules (the s 12A permission
with no deadline; conduct money tendered a reasonable time before a subpoena's day, s 20(6); the unrepresented party's
duty to give the Registrar claim information, s 32I(4)), each run by `EVALTRACE` inside an exported question that takes
only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched.

## Edition

- **Act:** Dust Diseases Tribunal Act 1989 No 63, corpus document `nsw_legislation:2024-11-15/act-1989-063` (in force
  15 November 2024), deposited at `../../registers/source-bundle/act-1989-063.txt` (text sha256 062491...3c6db8 per its
  `.meta.json`), taken from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au
  returned a bot challenge. Not the authorised text.
- **Not deposited here, asked as facts:** the Dust Diseases Tribunal Regulation and the Tribunal's rules (conduct money,
  the claims resolution process, what claim information is required and when, the time to appeal); the Limitation Act
  1969, the Law Reform (Miscellaneous Provisions) Act 1944, the Workers Compensation Act 1987 (ss 151AB, 151AC), the Civil
  Procedure Act 2005 and the Corporations Act 2001, which are separate subjects (some encoded in Commons) and cannot be
  imported across folders; the commencement dates of ss 11A, 12A-12D and 25A-25B (inserted by amending Acts whose dates
  are not in the text).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ddt-dates.l4` | 0 | 0 | 0 | 0 |
| `ddt-claims.l4` | 0 | 0 | 0 | 0 |
| `ddt-cases.l4` | 0 | 0 | 151 | 151 |

Every expected value was worked by hand from the text, with the edges: every Schedule 1 shape of answer and both
"means" exclusions; each limb of s 11(1) failing in turn; a claim 51 years after exposure and one filed on the day the
cause arose (s 12A); the conduct-money tender on the last day (23 November for a 30 November subpoena with 7 days'
reasonable time), the day after, a dollar short and over the prescribed amount (s 20(6)); the claim information on the
28th day and the 29th, given and not given (s 32I(4)); an appeal from a final decision involving exactly $20,000 and
$19,999 (s 32(4)(c)); service on none, one and all of those jointly liable (s 17(1)); the interim payment ceiling with
assessed and unassessed damages and a nil proportion (s 43(4)).

## Seat

**The claimant**: the person suffering, or who has suffered, from a dust-related condition, or, after that person's
death, their executor, administrator or other legal personal representative, or a relative claiming through them under
the Compensation to Relatives Act 1897. Every exported question is one that person would ask ("Is my condition a
dust-related condition?", "Must my claim go to the Tribunal?", "Can a limitation period stop my claim?", "Can the estate
recover for the pain and suffering?", "Does my settlement bar recovery from the others?", "Can my damages be reduced for
my dust diseases compensation?", "Can my evidence be taken early?", "Can I get interim payments?", "Can I appeal?"). The
Tribunal, its registrar, the Supreme Court and the insurers get no seat: their leave, opinions and discretions are
inputs, answered conditionally. A defendant seat (contribution under s 11(1A), the settling tortfeasor under s 12C(2),
the designated insurer under Part 6) could be added.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed as far as deposited: the Act's own figure
  ($20,000 in s 32(4)(c)) is encoded; the rules' and regulations' amounts and times are inputs.
- **The actors the text names.** Followed: the Tribunal, the registrar, the Supreme Court, the designated insurer, the
  joint tortfeasors, the Australian legal practitioner, the Registrar's officers.
- **Judgments answered conditionally.** Followed: the Tribunal's leave (ss 19, 25(3), 25A, 25B), its satisfaction
  (s 43(3)(c)), its estimate and "reasonable proportion" (s 43(4)), "a reasonable time" (s 20(6)), and "would, but for this
  Act, have been entitled to bring an action" (s 11(1)(c)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** "Dust-related condition" (s 3, Sch 1), "damages for
  non-economic loss" (s 12D(3)) and "settlement" (s 3) are worked out; "joint tortfeasor", "inter-insurer dispute",
  "designated insurer" (Workers Compensation Act 1987) and "Australian legal practitioner" are asked.
- **One case.** One claimant, one condition, one set of proceedings.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3 (dust-related condition, settlement); Sch 1; s 10(1), (6), (7); s 11(1)-(5); s 11A; s 12; s 12A with Sch 3
cl 7(2); s 12B; s 12C(1); s 12D; s 13(5); s 14(1)-(3); s 17(1), (2), (4); s 19; s 20(1), (6); s 22(2), (4); s 24;
s 25(3); s 25A; s 25B(1)-(3); s 32(1), (4); s 32I(1), (2), (4), (8); s 40; s 41; s 43; s 44; s 45; s 46 (by its silence).

**Out, and why:**
- ss 1, 2 (name, commencement); Part 2, ss 4-9 (the Tribunal, its members, President and staff); Sch 2 (members): machinery.
- s 10(2)-(5): other jurisdiction, the Tribunal's powers and the effect of its decisions; reflected only through s 14.
- s 11(1A) (a tortfeasor's contribution proceedings) and s 12C(2), (3) (the settling tortfeasor's contribution): the
  defendants', not the claimant's.
- s 13(1)-(4), (6), (7), s 17(3), (5), s 20(2)-(5), (7), s 21, s 22(1), (3), s 25(1), (2), s 25B(1A), (4), s 26: the
  Tribunal's own procedure and powers; no fact the claimant states settles them.
- s 32(2), (3) (what the Supreme Court may do on appeal); the time to appeal (in rules not deposited).
- Part 3A (the Rule Committee), s 32G, s 32H (regulations for claims resolution), s 32I(3), (5), (6) (the practitioner's
  conduct, the Registrar's database and reports), ss 33-37: rule- and regulation-making, fees, Schedule amendments,
  offences procedure, savings: machinery. The claims resolution process the regulations set up is not deposited.
- Part 5 (arbitration of disputes between insurers under s 151AC of the 1987 Act): a dispute between insurers, conducted
  under rules not deposited; s 38(4)'s period to set aside a determination is "prescribed by the rules".
- s 45(2)(b), (c), s 46(2)-(5): orders between insurers and other parties.
- Sch 3: transitional, except cl 7(2), which is in. Clauses 8 (s 12B's reach to proceedings pending in 1998) and 11, 12
  (ss 25A, 25B and proceedings pending in 1998) are spent for any claim brought now.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 3 "dust-related condition means ... (b) any other pathological condition of the lungs, pleura or peritoneum"
  -- `Is my condition a dust-related condition` -- a condition of another organ attributable to dust is `JUST FALSE` --
  none (a closed "means" list), recorded because the Workers' Compensation (Dust Diseases) Act 1942's "dust disease"
  differs (finding 1).
- **F2** s 11(1)(c), (5), s 17(4) -- `Must my claim be brought in the Dust Diseases Tribunal` -- an executor or
  administrator is "a person claiming through" the person -- they bring the person's own action under s 17(4) only.
  Either way the answer is the same.
- **F3** s 11A(1) "This section applies to proceedings ... in which" -- `Can I be awarded provisional damages` -- outside
  the scope, `NOTHING` -- `JUST FALSE`.
- **F4** s 12(1), (2) -- `Must my case be transferred to the Tribunal` -- proceedings pending at commencement whose hearing
  had begun answer `NOTHING` -- `JUST FALSE` under para (a), or `JUST TRUE` under para (b) read literally (finding 3).
- **F5** s 12B(1) "provided proceedings commenced by the person were pending" -- `Can the estate recover these damages`
  -- where the proviso fails, `JUST FALSE` (s 2(2)(d) of the 1944 Act applies) -- `NOTHING` (s 12B is silent; the 1944
  Act, a separate subject, decides).
- **F6** s 12C(1) "unless the terms of the settlement otherwise provide" -- `Does my settlement bar recovery from the
  others` -- the "unless" met: `JUST TRUE` -- `NOTHING` (the terms and the general law decide).
- **F7** s 19(2) "Only an Australian legal practitioner is entitled" -- `Can my representative charge a fee` -- the
  practitioner `JUST TRUE` -- `NOTHING` (the "only" closes the class; whether a practitioner is entitled is the general
  law's).
- **F8** s 20(6) -- `Must the person I subpoenaed comply` -- the tender is a condition written with DO, the last day
  (compliance day less the reasonable time) counted in; a subpoena the Tribunal directed is `JUST TRUE` -- `NOTHING`
  for a directed subpoena; the last day not counted.
- **F9** s 43(4) "one or more payments of such amounts as it thinks just but not exceeding" -- `What is the most the
  interim payments can be` -- the ceiling is on the total -- on each payment.
- **F10** s 32I(4) "as and when an Australian legal practitioner ... would be required" -- `Have I given the claim
  information in time` -- the regulations' period is an input in days, its last day counted in -- the regulations' own
  counting (not deposited).
- **F11** s 25(3), s 25A "may, with the leave" -- `Can evidence from another case be used in mine`, `Can material from
  another case be used in mine` -- without leave or consent, `NOTHING` -- `JUST FALSE`.
- **F12** s 10(6), (7) -- `Whose leave do I need to sue the company` -- the Tribunal's leave is needed in place of the
  supervising Court's -- no leave is needed at all (the Note to (6) says only that the supervising Court's leave is not
  required).

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 11(1) | the claimant | disability: no other court may entertain the claim | `Must my claim be brought ...` |
| s 11A | the claimant | power of the Tribunal to award provisional damages | conditional questions |
| s 12 | the registrar | duty to transfer | `Must my case be transferred ...` |
| s 12A | the claimant | liberty: no limitation period | MAY rule with no WITHIN |
| s 12B, 12C(1), 12D | the estate; the claimant | immunities from the 1944 Act bar, from settlement as a bar, from deduction | yes/no questions |
| s 19 | the claimant | liberty to appear; disability without leave | `Can this person appear for me` |
| s 20(6) | the person subpoenaed | no duty unless tendered conduct money in time | DO rule (a condition) |
| s 32 | the claimant | power to appeal, by leave in four cases | `Can I appeal ...` |
| s 32I(4) | the unrepresented claimant | duty; offence, 5 penalty units | MUST rule |
| s 32I(8) | the Registrar's officers | duty not to record or divulge; offence, 50 penalty units | `Can my claim information be ...` |
| s 43, 45 | the designated insurer; the claimant | liability to interim payment; liability to repay | conditional questions |

## What the Act turns out to say

1. **"Dust-related condition" is wider than the 1942 Act's "dust disease".** Both use the same 19 Schedule 1 names, but
   this Act's para (b) takes in any condition of the lungs, pleura or peritoneum "attributable to dust", where the 1942
   Act needs dust "that may also cause a disease so specified". A claimant can be in this Tribunal's exclusive
   jurisdiction without a statutory compensation claim. Asserted.
2. **s 10(1) points at a repealed section.** The exclusive jurisdiction is "except as provided by sections 29 and 32";
   ss 27-31 are repealed. Similarly s 33(4)(b1) speaks of interest "awarded under section 15", and ss 15 and 16 are
   repealed.
3. **s 12's two paragraphs disagree.** Para (a) transfers proceedings pending at commencement only if the hearing "has
   not begun"; para (b) transfers proceedings that "after that commencement ... are pending", which literally includes
   the same proceedings with the hearing begun. Fork F4; asserted `NOTHING`. Spent in practice (1989).
4. **No limitation period, ever.** s 12A sets none and displaces every statute of limitations; the encoding writes it as
   a permission with no `WITHIN`, which is fulfilled whenever the claim is brought (asserted 51 years on). The one
   exception is a cause of action already determined before s 12A commenced (Sch 3 cl 7(2)).
5. **s 12B needs the person to have started the case and to die with it pending in the Tribunal.** Where a person dies
   before filing, the estate loses the non-economic damages (the 1944 Act's s 2(2)(d) applies); the operative words in
   (2) carry the same condition as the purpose clause's proviso. Fork F5.
6. **s 12D shields non-economic damages only from 1942 Act compensation.** Other compensation (for example under the
   Workers Compensation Act 1987) is not mentioned; the general law decides. Gratuitous services count as non-economic
   loss only while unpaid.
7. **The $20,000 appeal threshold is fixed and unindexed** (s 32(4)(c)), and "involves (directly or indirectly) a claim
   for, or a question relating to" an amount is wide; the claimant states the amount.
8. **Much of the claims process is not in the Act.** The claims resolution process, compulsory mediation, offers and
   costs (s 32H), the claim information (s 32I), conduct money (s 20(6)), the time to appeal and the procedure for
   provisional damages (s 33(4)(b1)) are left to regulations and rules that are not deposited.
9. **s 43(4) does not say whether its ceiling is per payment or in total.** Fork F9.
10. **s 32I(4) is the one offence a claimant can commit under the Act** (5 penalty units, the value of a unit set
    elsewhere); a represented claimant's practitioner bears the duty, the solicitor where a barrister also acts.

## Questions (exported)

`ddt-claims.l4` (30), in the Act's order: `Is my condition a dust-related condition`, `Must my claim be brought in the
Dust Diseases Tribunal`, `Can I include this other claim in my Tribunal proceedings`, `Whose leave do I need to sue the
company`, `Can I be awarded provisional damages`, `Can I be awarded further damages for another condition`, `Must my case
be transferred to the Tribunal`, `Can a limitation period stop my Tribunal claim`, `Can the estate recover these
damages`, `Does my settlement bar recovery from the others`, `Is this damages for non-economic loss`, `Can my
non-economic damages be reduced for this compensation`, `What does my money judgment become`, `Is service on some of
those jointly liable enough`, `Can this person appear for me`, `Can my representative charge a fee`, `Must the person I
subpoenaed comply`, `Am I entitled to a certified copy`, `Can the evidence be taken early`, `Can evidence from another
case be used in mine`, `Can material from another case be used in mine`, `Can a decided general issue be reargued in my
case`, `Can I appeal and do I need leave`, `Who must give the Registrar my claim information`, `Have I given the claim
information in time`, `Can my claim information be recorded or divulged`, `Can I get interim payments`, `What is the most
the interim payments can be`, `Is the interim payment an admission of liability`, `Could I be ordered to repay an
interim payment`.

## Before relying on it

- Replace the corpus text with the current official text and re-check every quotation and figure.
- Deposit the Dust Diseases Tribunal Regulation and the Tribunal's rules (conduct money, claim information, claims
  resolution, time to appeal).
- Link to the Workers' Compensation (Dust Diseases) Act 1942, Limitation Act 1969, Law Reform (Miscellaneous Provisions)
  Act 1944, Compensation to Relatives Act 1897 and Civil Procedure Act 2005 encodings.
- Have a lawyer review forks F4, F5, F9 and F12.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
