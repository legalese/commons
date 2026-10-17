# Consumer Guarantees Act 1993 (New Zealand) — encoding notes

Read this first. `BRIEF.md` is the specification. The source is `../registers/source-bundle/act_public_1993_91.txt`, the PCO's version as at 24 January 2026, converted from its XML on 2026-10-13 (`act_public_1993_91.meta.json` beside it).

## 1. What is encoded

**The whole Act**: ss 1-56. Sections 48-55 amend other Acts and have no operative text here.

**What the converted text lacks.** Paragraph labels are gone; a label in a comment or a name is read from the provision's place in its list.

**Inputs.** The Act turns on what "a reasonable consumer" would expect or accept, what is "reasonable", "substantial", "significant" or "reasonably foreseeable", and on facts about who acquired what for what purpose. These are taken as given: the encoding works out who is answerable and which remedies follow, not whether goods are of acceptable quality. In particular:
- whether goods or services are of a kind ordinarily acquired for personal, domestic or household use, and the acquirer's purpose (s 2);
- whether a guarantee has failed, and which one;
- whether the failure can be remedied, whether the supplier (or manufacturer) refused, neglected or failed to remedy it, each limb of ss 21 and 36, each limb of s 20, and the causes in ss 17, 26 and 33;
- whether a contracting-out clause is fair and reasonable (s 43(2)(d), (3)).

### The top-level goal

`the consumer guarantees position for` a `Consumer case` (`cga-goal.l4`, `@export default`) answers: *for this supply to this consumer and this failure, does the Act give redress, which remedies does the consumer have against the supplier and against the manufacturer, and what are the damages for the reduction in value?*

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | Scope, courts, assignees | `is a consumer` (`@export`), `the Act gives redress for the supply to…` (`@export`), `the forums for a claim of` (`@export`), `the clause validly contracts out under s 43(2)` | ss 2, 7B, 41, 43, 46, 47, 56 | `cga-scope.l4` |
| 2 | Goods and the supplier | `the remedies against the supplier for` (`@export`), `the goods failure is of a substantial character`, `the right to reject still applies to`, `the supplier's damages…` | ss 5-11, 16-23 | `cga-goods.l4` |
| 3 | Goods and the manufacturer | `the remedies against the manufacturer for` (`@export`), `the manufacturer is answerable under Part 3 for`, `the manufacturer's damages…` | ss 12-14, 25-27, 42 | `cga-goods.l4` |
| 4 | Services | `the remedies against the supplier for the service failure` (`@export`), `the service failure is of a substantial character`, `the refund on cancelling…`, `the day the cancellation takes effect…` | ss 28-39 | `cga-services.l4` |

## 2. Coverage table

| provision | disposition |
| --- | --- |
| ss 1, 1A, 3, 4 | carried as text (s 1(2), 1 April 1994, is used through s 56) |
| s 2 consumer, goods (c) | Goal 1 |
| s 2 other definitions, s 2(2)-(3) | inputs (who is a supplier or manufacturer, when supply happens) |
| ss 5-10, 7A, 7B | Goal 2 (which guarantee failed is an input; s 7B decides which guarantee fits gas and electricity) |
| s 11 | Goal 2 |
| ss 12-14, 42 | Goal 3 |
| s 15 | carried as text |
| ss 16-21, 23 | Goal 2 |
| ss 22, 23A, 24 | carried as text (how rejection is made; collateral credit; gifts) |
| ss 25-27 | Goal 3 |
| ss 28-33, 35-37 | Goal 4 |
| s 34 | carried as text |
| s 38(1)(a) | Goal 4 |
| ss 38(1)(b)-(2), 39, 39A, 40 | carried as text (the court's or Tribunal's orders are inputs) |
| s 41 | Goal 1 |
| s 43, 43A | Goal 1 (s 43(5) offence and (6)-(8) carried as text) |
| ss 44, 45 | carried as text |
| s 46 | Goal 1 (s 46(3)-(4) carried as text) |
| s 46A | carried as text |
| s 47 | Goal 1 |
| ss 48-55 | amendments to other Acts |
| s 56 | Goal 1 |

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | ss 18(2)-(3), 32(a)-(b) | A failure that can be remedied but is of a substantial character | Both sets of remedies are open: require a remedy, or reject (cancel) or claim damages at once | (2) applies "Where the failure can be remedied"; (3) "Where the failure cannot be remedied or is of a substantial character" — the conditions overlap |
| F2 | s 5A(2) | Delivery failure that is not substantial | Only damages under s 18(4), and only if there is foreseeable loss | s 5A(4) limits the redress to s 5A(2) |
| F3 | s 27(2) | Consequential damages from a manufacturer before it was asked to repair under an express guarantee | Not reached: s 27(2) bars only "an action ... under subsection (1)(a)" (value), so consequential damages under (1)(b) stay open | The words of s 27(2) |
| F4 | s 41(2) | Does a charity's supply for the recipient's benefit also bar redress against the manufacturer? | No: only redress "against a charitable organisation" | The words of s 41(2); adopted after the independent pass |
| F5 | s 36(c) | "where section 29 applies" | Where the s 29 guarantee is engaged (a purpose or result made known), whichever guarantee failed | As s 21(c) "where section 8(1) applies"; adopted after the independent pass |
| F6 | s 32(a)(ii)(B) | Cancelling when there is no contract between supplier and consumer | Not available | There must be a contract to cancel; s 2 "supplier" reaches consumers who are not parties; adopted after the independent pass |

Also read, without a fork: a remedy open under two limbs is listed once; the s 2 repair limb of "consumer" applies only to goods; a guarantee that does not fit what was supplied (s 6 on electricity, s 7A on goods) gives no remedies, and a goods failure on a supply of services is answered as goods (ss 15, 34); the s 11 and s 31 price guarantees give only the right to refuse to pay more than a reasonable price; the s 47 limits are inclusive ("does not exceed").

## 4. Tests

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-15:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `cga-tests.l4` (encoder) | 0 | 115 | 0 |
| `tests-independent.l4` | 0 | 153 | 0 |
| the 5 rule modules | 0 | 0 | 0 |
| **total** | 0 | 268 | 0 |

The independent pass (`INDEPENDENT-TEST-REPORT.md`) found 8 disagreements, all resolved in its favour: s 41(2) and manufacturers (F4); remedies listed twice (goods and services); cancellation without a contract (F6); s 36(c) (F5); the repair limb applied to services; and two refusals that should have been empty answers. **The encoder's own tests that encoded the rejected readings were changed** and marked in `cga-tests.l4`.

**Known limits.** Whether each guarantee is engaged and failed is an input, as are the s 2 definitions beyond the building rule; ss 19, 22, 23 (mechanics), 23A, 24, 27(3), 37(3), 38(1)(b)-(c), 39, 39A, 43(4)-(7), 43A, 44-46A and the s 47(3), (5) order limits are carried as text.

## 5. Open questions for a New Zealand consumer lawyer

1. F1: is a remediable failure of a substantial character subject to the supplier's right to remedy first?
2. F3: may a consumer claim consequential loss from a manufacturer without first requiring repair under an express guarantee?

## Legislation Act 2019 s 55 (reviewed 2026-10-17)

At the user's direction, every New Zealand encoding was reviewed for Legislation Act 2019 s 55 (a thing to be done on a day or within a period may be done on the next working day if that day is not a working day). This Act sets no fixed day or period for doing anything in the encoded provisions: its time limits are "a reasonable time" (for example ss 20, 23, 32, 35), and the one date computed — when a cancellation takes effect (s 37) — is not a deadline. Nothing changed.
