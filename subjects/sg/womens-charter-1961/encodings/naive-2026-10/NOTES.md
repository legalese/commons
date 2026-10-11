# Women's Charter 1961 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021),
informal consolidation, version in force from 17/8/2026. The latest amendment
annotated in the deposit is Act 21 of 2025 wef 17/08/2026.

**Checks:** three case files, 149 assertions satisfied, 0 errors, 0 warnings (54 at first encoding; 23 added on 11 Oct 2026 for requirements REQ-0005 and REQ-0006; 42 in `wc-cases-maintenance-enforcement.l4` for REQ-0269 and 30 in `wc-cases-divorce-assets.l4` for REQ-0270, also 11 Oct 2026).

## Why this Act, and why scoped

Chosen for its **everyday-life relevance** to ordinary people in Singapore: it
decides who may marry, who must maintain whom, who may seek protection from family
violence, and when a divorce is granted. (An automated count found 0 of the 527
deposited Singapore Acts citing it by its slug title; that count undercounts Acts
cited by short titles and is not a measure of importance.)

The Act runs to several hundred pages, so this row takes void marriages (ss 9, 11,
11A, 12, 13), marrying again during a spouse's lifetime (s 6A), the licence waiting
period and consents for under-21s (ss 17(2), 21A), the notice of marriage and its lapse
(ss 14, 15), who solemnises and how (ss 22, 23, 40), maintenance of a wife, an
incapacitated husband and children (s 69), protection orders (ss 60, 60A, 63C), and
divorce jurisdiction, the three-year bar and irretrievable breakdown (ss 93, 94, 95,
95A). Not encoded: the prohibited degrees (s 10, First Schedule), the Second Schedule
list of whose consent is needed, the declarations, licence conditions and caveats (ss 16, 18-20), special licences,
registration, family violence
assessment and enforcement powers, custody, post-divorce maintenance, judicial separation,
nullity procedure, and the Part 10A mediation and parenting provisions. Maintenance
enforcement (ss 71, 80-83, 91B-91R) and the division of matrimonial assets (s 112) were
added on 11 October 2026; see their sections below.

## What the Act turns out to say

### 1. Six months back together kills an adultery claim, but not a behaviour claim

s 95A(2)(b): if the applicant lives with the respondent "for more than 6 months"
after knowing of the adultery, the applicant "may not rely on that act of
adultery". For behaviour, s 95A(3) only says that 6 months or less is to be
ignored; on the words, a longer period is not a bar. For desertion and living apart,
up to 6 months together keeps the period continuous, but that time "does not count
towards the length" (s 95A(4), (5)), so 24 months of desertion with 3 months back
together is not enough, and 27 months is. The encoding treats more than 6 months
together as breaking the period entirely, which is a simplification. Asserted.

### 2. A married 17-year-old cannot, on the literal words, apply for her own protection order

s 60(2) lists who may apply for family violence against Y: if Y is below 18, a
family member, guardian or carer; only "in any other case" Y. s 60(3) says a person
below 18 may not apply "unless the person is married or was previously married",
which reads as though a married minor might apply for herself, but (2)(a) does not
list Y. The encoding follows the literal words (a married 17-year-old victim may not
apply herself; a family member may). This is a reading, not tested law; the Family
Justice Rules and the protector route (s 60(1)) were not examined beyond the text.
Asserted.

### 3. Two ages for marriage: 18 for validity, 21 for consents

A marriage where either party is below 18 is void unless a special marriage licence
authorised it (s 9). Separately, a "minor" for the consent rules is a person "below
21 years of age" (s 21A(5)), and the Registrar must not issue a licence to a
never-married minor without the Second Schedule consents (or the court's consent in
lieu, or dispensation). A previously married or widowed minor needs none (s
21A(4)). Asserted.

### 4. A husband can claim maintenance only if incapacitated

s 69(1) lets a wife claim on proof of neglect; s 69(1A) gives the same claim to "an
incapacitated husband", defined in s 2 as one incapacitated from earning a
livelihood by disability or illness and unable to maintain himself. An able husband
has no claim under s 69. Child maintenance stops at 21 unless disability, national
service, education or training, or special circumstances justify it (s 69(5), (6));
a child of 21 or over may apply in person, and a sibling of 21 or over may apply
for a child below 21 (s 69(3)). Asserted.

### 5. Marrying again is punished harder when the first marriage was concealed

s 6A: up to 10 years and liable to a fine up to $15,000 where the former marriage
was concealed from the new spouse; up to 7 years and $10,000 otherwise. The
exception for a spouse absent and unheard of for 7 years applies only if the new
partner is told "the real state of facts". Asserted.

### 6. Divorce: three years' marriage, then one of six facts, then "just and reasonable"

No divorce application may be filed until 3 years after the marriage, save with
permission for "exceptional hardship" or "exceptional depravity" (s 94). The court
must be satisfied of one of the six s 95A facts (including, since the Act 3 of 2022
amendment wef 1 July 2024, a written agreement that the marriage has broken down,
which the court must not accept if reconciliation remains reasonably possible), and
that granting the divorce is "just and reasonable" (s 95(2)(c)). Jurisdiction needs
domicile or 3 years' habitual residence of either party (s 93). Asserted.

### 7. The earliest wedding day is day 22, not day 21 (added for REQ-0005)

s 17(2)(a): a licence issues only "after the expiry of 21 days from the date of the notice
of marriage". s 13 requires a valid licence. So for a notice given on 20 April 2029, the 21
days expire at the end of 11 May, and the earliest solemnisation is **12 May 2029**. REQ-0005
expected "21 days after notice", one day earlier. The notice lapses once "3 months ... have
elapsed" without solemnisation (s 15(1)(a)), read as 20 July 2029. That is an inference about
the boundary day. If the notice lapses, any licence issued on it is void and a fresh notice
is needed (s 15(3)). Asserted.

### 8. Witnesses make a wedding lawful, not valid (added for REQ-0006)

s 22: only the Registrar or a licensed solemniser may solemnise. s 23: the parties, the
solemniser and at least two credible witnesses must be present together (or linked by video
with the Registrar's permission, s 24), and both parties must freely consent. But s 13 voids
a marriage only for want of a valid licence or an authorised solemniser. Holding the
ceremony with fewer than two witnesses is the solemniser's **offence** under s 40(1)(b) (3
years and a fine of up to $5,000), and the Act as read does not make the marriage void for
it. REQ-0006 expected the witnesses as a condition of validity. Asserted.

## Enforcing a maintenance order (added 11 October 2026 for REQ-0269)

Module `wc-maintenance-enforcement.l4`, cases `wc-cases-maintenance-enforcement.l4` (42
assertions; the first twelve are the requirement's own facts). The question: a father ordered to
pay $600 a month for his child misses three payments; what may the court do, and may it attach
his wages?

1. **Yes, the court may attach his wages, and much more.** Once the court "is satisfied that
   the maintenance order ... has been breached" (s 81(1)(a)) it may make any of the seven
   "maintenance enforcement orders" in s 91B(1): (a) a warrant to levy the arrears as for a
   Magistrate's Court fine; (b) imprisonment for the arrears; (c) attachment of a debt under the
   Family Justice Rules; (d) a banker's guarantee against future default; (e) financial
   counselling; (f) community service; (g) an attachment of earnings order, directed to his
   employer (s 76(1)). On the facts all seven are open. Asserted.
2. **It must also declare and schedule the arrears.** Where breach is shown, there is no consent
   order and the application is not dismissed or struck out, the court "must" declare the arrears
   ($1,800), order them paid in a lump sum or instalments, require him to prove payment on set
   dates, and specify a default term of imprisonment for failing to prove payment (s 81(2)),
   unless special circumstances such as age or health make a term inappropriate (s 81(7), (8)).
   The expectation ("the court may order the arrears paid") understates this: the payment order is
   mandatory, not discretionary. Asserted.
3. **The limits.** Imprisonment for the arrears: at most one month for each month's worth "(or
   any part thereof)", so 3 months for $1,800 at $600 (s 91P(1)(a); 6 months for a lump-sum
   order, (b)). It cannot be imposed after a show-payment order on the same application (s 91P(4)),
   nor on a consent order (s 81(4)(b)). The default term under s 81(2)(d) is capped at 6 months for
   each failure to prove payment of arrears plus one month per month's worth of unproved payable
   maintenance (s 81(5)), and is served only if he shows "no good cause" (s 91O(1)). A banker's
   guarantee: at most 3 years and at most 3 months' maintenance, $1,800 (s 91L(2)). Community
   service: at most 40 hours, and only if supervised arrangements can be made (s 91N). Jail does
   not wipe the debt (ss 91O(5), 91P(5)). Asserted.
4. **There is no fine, and the old "per month" regime is gone.** The expectation listed a fine
   per month in arrears. That was the pre-2025 s 71. The Family Justice Reform Act 2023 (Act 18 of
   2023, wef 16 January 2025) replaced it: s 71 is now only the power to make an attachment of
   earnings order when making a maintenance order "or at any time thereafter" to secure FUTURE
   payments, and no s 71 application may be made while Part 9 enforcement is pending (s 71(3)).
   Enforcement on default is Part 9, ss 76 to 91T. The only fines in Part 9 are on employers who
   disobey an attachment of earnings order ($2,000 or 12 months, s 91K) and on misuse of
   information (s 91S). Asserted.
5. **Preconditions are breach, not wilfulness.** The Act's trigger for the s 91B orders is that
   the order "has been breached"; there is no "wilful neglect" or "without reasonable cause" test
   at that stage. "Good cause" appears only at the later show-payment stage (s 91O(1)(b)).
   Imprisonment needs arrears owing "as at the time the maintenance enforcement application ... is
   made" (s 91B(1)(b)), even if paid since (s 91P(3)(a)). Asserted.
6. **Credit bureau.** Once arrears are declared under s 81(2)(a) and any remain unpaid, the payee,
   a caregiver, an authorised representative or an MEO may lodge an arrears report with a
   designated credit bureau (s 83). It is the payee's step, not a court order, and not on the
   s 91B list. Asserted.
7. **Old arrears: a bar, not a leave requirement.** Arrears that "accrued due more than 3 years
   before the commencement of the proceedings" are not recoverable unless earlier proceedings were
   begun in time or "the court, under special circumstances, otherwise allows" (s 91R(4)). Read in
   whole months, 36 months being not "more than 3 years" (an inference about the boundary). Three
   months' arrears are well within it. Asserted.
8. **Who may apply.** The person who applied for the order, a payee with custody or care and
   control of the child, a trustee payee (with co-trustees' consent), a payee nominated by a
   Minister's appointee, or anyone with a right under another written law (s 80). The ex-partner
   qualifies if she applied for the order or has care and control. Asserted.

Not settled by the Act: the amount of an attachment of earnings order ("a sum that seems
reasonable to the court", s 91C, no cap or protected minimum); the attachment-of-debt procedure
(Family Justice Rules); the "prescribed circumstances" for varying the order on an enforcement
application and the credit-bureau procedure (regulations under s 91A); which credit bureau is
designated (Ministerial designation, s 83(5)(b)).

## Divorce by consent and the division of matrimonial assets (added 11 October 2026 for REQ-0270)

Module `wc-divorce-assets.l4` (imports `wc-family.l4` for ss 93, 94, 95A), cases
`wc-cases-divorce-assets.l4` (30 assertions; the first nine are the requirement's own facts).
The question: a couple divorcing by consent after three years apart, who rented throughout and own
nothing jointly; is there a matrimonial asset, and what order is made when there is none?

1. **If they truly own nothing, there is no matrimonial asset and no s 112 order; but "nothing
   jointly" does not establish that.** s 112(10) defines "matrimonial asset" by WHEN and HOW an
   asset was acquired, not by whose name it is in: "any other asset of any nature acquired during
   the marriage by one party or both parties". Savings from salary in one spouse's sole name, a car,
   shares, an insurance policy, all acquired during the marriage, are matrimonial assets. A rented
   flat is not an asset of either (inference: the landlord owns it). So the expectation "no
   matrimonial assets; no division order" holds only if neither spouse acquired anything of value
   during the marriage; on the more realistic facts with a sole-name bank balance, s 112 applies
   and the court divides it "in such proportions as the court thinks just and equitable". Both
   versions asserted.
2. **What the court does when there is nothing.** The Act names no particular order: the s 112(1)
   power is to divide "any matrimonial asset", and with none it has nothing to bite on. The
   encoding returns "no matrimonial asset: no division order" (an inference; in practice the
   court records no order for division). Maintenance of the wife (s 113) and of any child (s 127)
   are separate questions and may still be ordered. Asserted.
3. **The ground is s 95A(1)(d), and Chapter 4A is the wrong chapter.** "Three years apart with
   consent" is s 95A(1)(d): lived apart "for a continuous period of 3 or more years immediately
   before the application" and both "consent to a divorce being granted". Four years apart needs
   no consent ((e)); since 1 July 2024 a written agreement that the marriage has broken down is a
   sixth fact ((f)), refused if reconciliation remains reasonably possible (s 95A(6)). Up to 6
   months together does not break the period but does not count (s 95A(5)). The jurisdiction
   (s 93), three-year bar (s 94) and "just and reasonable" (s 95(2)(c)) rules from `wc-family.l4`
   are reused. The requirement named "Part 10 Chapter 4A"; Chapter 4A (ss 121A onward) is financial
   relief after a FOREIGN divorce. The division power for a Singapore divorce is s 112 in Chapter 4.
   Asserted, on assumed facts: both domiciled in Singapore, six years married.
4. **The definition in full.** A matrimonial asset is (a) an asset acquired before the marriage
   that the family ordinarily used for shelter, transport, household, education, recreational,
   social or aesthetic purposes, or that the OTHER spouse (or both) substantially improved during
   the marriage; or (b) any asset acquired during the marriage; excluding an asset acquired by gift
   or inheritance (at any time) unless it is a matrimonial home or was substantially improved by
   the other spouse or both. So an inherited flat that became the matrimonial home is in; an
   inheritance kept in a separate account is out; untouched pre-marriage shares are out. Asserted.
5. **The court's weighing is an input.** The eight s 112(2) matters (direct contributions, debts,
   children's needs, indirect contributions, agreements, rent-free occupation, assistance, and the
   s 114(1) matters) are carried as a list; the proportion is supplied, and the encoding only
   multiplies the pool. How the courts turn those matters into a percentage is case law, not the
   Act. Asserted (arithmetic only).

Not settled by the Act as read: what a "matrimonial home" is (undefined in Part 10); how CPF
balances and HDB flats are divided (CPF Act and Housing and Development Act provisions); whether a
tenancy deposit counts (on the words of (b), probably yes, since it is an asset acquired during the
marriage: an inference); the weighting of contributions (case law).

## What would need doing before this is worth anything

- The prohibited degrees, the Second Schedule consents and the 1 October 2016 start
  date of s 11A are not modelled.
- Periods of more than 6 months together are treated as resetting desertion or
  separation to zero; the text does not say that.
- No Family Justice Rules, subsidiary legislation or case law were read; finding 2
  in particular needs checking against practice.
- Part 10 is thin: s 112 is now encoded as a definition and a power (REQ-0270), but
  not the weighing of contributions, custody or post-divorce maintenance, where most
  contested divorces are actually fought.
