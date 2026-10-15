# Fair Trading Act 1986 (New Zealand) — encoding notes

Read this first. `BRIEF.md` is the specification. The source is `../registers/source-bundle/act_public_1986_121.txt`, the PCO's version as at 1 July 2026, converted from its XML on 2026-10-13 (`act_public_1986_121.meta.json` beside it).

## 1. What is encoded

**The whole Act**, at the level its rules can be computed: which provision a piece of conduct contravenes and with what consequence, and every rule in the Act with a number, a date or a period in it. Most of Part 1 turns on whether conduct is misleading, deceptive, unconscionable, false, harassing or unfair; that quality is an input (`the conduct has the quality the provision describes`), and the encoding applies the limits the Act puts around it (in trade, the Crown, news media, ss 12A(3) and 12D) and its consequences (offence, fine, infringement offence, s 43 orders, time limits).

**What the converted text lacks.** Paragraph labels are gone; a label in a comment or a name is read from the provision's place in its list.

**Inputs.** Besides the quality of the conduct:
- **working days.** The Act counts in working days (ss 21A, 31A, 33D, 36D, 36L, 36M, 36U, 36V, 36ZA, 36ZF) but does not define them. The encoding counts Monday to Friday, less the weekdays given in a `Working day calendar` (public holidays, and any other days the Legislation Act 2019's definition excludes).
- whether a standard exists and was complied with, whether a notice is in force, and whether a contract is a standard form contract;
- the amounts other Acts fix where this Act refers to them (the Disputes Tribunal Act 1988 and District Court Act 2016 limits) and the prescribed infringement fee;
- whether a gift card was sold after the Fair Trading (Gift Card Expiry) Amendment Act 2024 commenced.

### The top-level goal

`the fair trading position for` a `Conduct case` (`fta-goal.l4`, `@export default`) answers: *for this conduct, does it contravene the Act; is it an offence, and up to what fine; is it an infringement offence; may a party apply for an order under s 43, and by when; and may only the Commission bring proceedings?*

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | Conduct | `the conduct contravenes the provision` (`@export`), `a party may apply for an order under s 43`, `the vendor bid is a false representation about price`, `the recipient takes the unsolicited goods as a gift…`, `is a small trade contract…`, `the term may be declared unfair…` (`@export`) | ss 4, 5C, 5D, Part 1, 46I-46L | `fta-conduct.l4` |
| 2 | Consumer transactions and auctions | `is a layby sale agreement` (`@export`), `the refund on cancelling the layby` (`@export`), `is an uninvited direct sale agreement` (`@export`), `may cancel within the cooling-off period…`, `the gift card expiry date…` (`@export`), `the last day to pay the vendor…` | Part 4A | `fta-transactions.l4` |
| 3 | Information and safety | `supplying the goods breaches the standard…`, `the last day to notify a voluntary recall…`, `the last day a suspension of supply notice may run to…` | Parts 2-4 | `fta-safety.l4` |
| 4 | Enforcement | `the maximum fine for contravening…` (`@export`), `is an infringement offence`, `the last day to apply for a s 43 order…`, `who may make a s 43 order of…` (`@export`), `the court may make a management banning order…` | Part 5, ss 47F, 47J | `fta-enforcement.l4` |

## 2. Coverage table

| provision | disposition |
| --- | --- |
| ss 1-3, 5, 5B, 6 | carried as text |
| s 4 | Goals 1, 4 (the Crown bound only in trade; not prosecuted) |
| ss 5C, 5D | Goal 1 |
| ss 7, 9-14, 16, 17, 19-24, 26A, 26B | Goal 1 (the quality of the conduct is an input) |
| s 8, 12B | carried as text (matters a court considers) |
| ss 12A(3), 12C, 12D | Goal 1 |
| s 14A | Goal 1 |
| s 15 | Goal 1 |
| s 21A | Goal 1 |
| ss 21B, 21C, 21D | Goal 1 (s 21C as a prohibition); s 21B, 21D carried as text |
| ss 25, 26 | carried as text |
| ss 26C, 26D | Goal 1 |
| s 26E | carried as text |
| ss 27, 28A, 29, 30A, 30B, 32-35 | carried as text |
| ss 28, 30, 36 | Goals 3, 4 |
| s 28B | Goal 4 (as a prohibition) |
| s 31 | Goal 3 (s 31(2)); the rest carried as text |
| s 31A | Goal 3 (s 31A(2)) |
| s 33D | Goal 3 |
| s 36A | carried as text |
| ss 36B, 36F, 36H, 36I | Goal 2 |
| ss 36C-36E, 36G, 36J | carried as text (disclosure contents; supplier's grounds are the `Who cancelled the layby` constructors) |
| ss 36K, 36M, 36RA | Goal 2 |
| ss 36L, 36N-36S | carried as text (s 36N(2) is the "materially" in the cooling-off input) |
| ss 36T, 36U, 36W | carried as text |
| s 36V | Goal 2 (the same cooling-off rule) |
| ss 36WA, 36WC | carried as text |
| s 36WB | Goal 2 |
| ss 36X-36Z, 36ZB, 36ZC, 36ZE | carried as text |
| ss 36ZA(3), 36ZD, 36ZF | Goal 2 |
| ss 37-39 | carried as text |
| s 40(1)-(1B) | Goal 4 |
| s 40(2), 40A, 40C-40H | carried as text |
| s 40B | Goal 4 |
| ss 41-43 | carried as text (who may apply is in Goal 1) |
| ss 43A, 43B | Goal 4 |
| ss 44-46B | carried as text |
| ss 46C-46E | Goal 4 |
| ss 46F-46H, 46J, 46M | carried as text |
| ss 47F, 47J | Goal 4 |
| ss 47-51 (other) | carried as text |
| Schedule 1AA cls 1-2 | carried as text |
| Schedule 1AA cl 3 | Goal 2 (an input) |
| Schedules 1-3 | amendments and repeals |

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | throughout | What is a working day? | Monday to Friday, less the weekdays given as non-working | The Act does not define it; the Legislation Act 2019's definition is outside the bundle |
| F2 | ss 36M(1)(a), 36V(1)(a) | "within 5 working days after the date on which the consumer receives a copy" | Up to and including the 5th working day after that date | The period runs from the day after receipt |
| F3 | s 36ZF(1)-(2) | The vendor asks for the proceeds early | The earlier of 10 working days after the sale and 5 working days after the request | (2) only shortens the time ("sooner than 10 working days") |
| F4 | s 36ZA(3)(b) | "before the end of the first working day following the day of the auction" | Accepted on or before that working day | The day ends at its end |
| F5 | s 40, s 4(2) | The fine for the Crown | 0: the Crown is not prosecuted (a High Court declaration is available instead) | s 4(2) |
| F6 | s 26D(3)(b) | The annual value threshold | Reached at "at least the specified amount", so a small trade contract is one below $250,000 (grocery: below $1 million) | "consideration ... of at least the specified amount" |
| F7 | s 46C(1)(a) | "on at least 2 separate occasions within a 10-year period" | Two occasions no more than 10 years apart, the tenth anniversary included | A period of 10 years from the first occasion |
| F8 | s 36I(4) | "made no payments ... during the 3 months immediately before the relevant event" | No payment on or after the day 3 months before the event | The 3 months run back from the event |
| F9 | ss 19(1)-(2), 32 | Which of these need conduct in trade? | s 19(1) and s 32 do; s 19(2) ("Any person who has advertised") does not | The words of each subsection; adopted after the independent pass |

## 4. Tests

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-15:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `fta-tests.l4` (encoder) | 0 | 162 | 0 |
| `tests-independent.l4` | 0 | 239 | 0 |
| the 6 rule modules | 0 | 0 | 0 |
| **total** | 0 | 401 | 0 |

The independent pass (`INDEPENDENT-TEST-REPORT.md`) found 2 disagreements, both resolved in its favour (s 32 needs trade; s 19(2) does not, F9), and 4 gaps now closed: s 36V(2)(a), the s 36Q care period, s 21A(2) as a prohibition, and the scope of the s 31(2) 18 months.

**Known limits.** The s 43 flag assumes the applicant is a party to any contracting-out agreement (s 5D(1)(b) bars only parties); who may apply under ss 41, 42, 46H and 46I(1), the s 4(2) declaration, and the s 40(2) aggregate cap are text; the s 46C function takes two s 40(1)/(1A) occasions only; gift card, "minor failure" and s 46L(4) matters are inputs.

## 5. Open questions for a New Zealand consumer lawyer

1. F1: which days are working days for Part 4A and s 33D?
2. Is s 26A or 26B conduct (using an unfair contract term) an offence under s 40(1), as the words of s 40(1) suggest?
