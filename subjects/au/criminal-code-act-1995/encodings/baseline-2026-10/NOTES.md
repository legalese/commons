# Criminal Code Act 1995 — baseline encoding, the accused's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it; the one case outside the encoding (conduct before 15 December 2001 for an offence outside the Code) answers `not covered`, and a test asserts it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0082` in `subjects/au/requirements.jsonl`. There was no earlier encoding of this Act to keep.

Every question is a function named as the accused would ask it, with `@export` and a `@desc` on every input. There are 18 exported questions, grouped under `§§` headings: whether Chapter 2 applies, what the prosecution must prove, the Part 2.3 defences (each heading naming its situation: "if you were a child", "if you were intoxicated", "if you made a mistake", "if someone else made you do it, or you were defending yourself"), who must prove what, and the two offences.

## Edition

The compilation registered as **C2026C00243** (Compilation No. 174, compilation date 30 June 2026, including amendments up to Act No. 53, 2026), retrieved from the Federal Register of Legislation on 13 October 2026, as deposited at `../../registers/source-bundle/C2004A04868.txt`. Chapter 2 is at lines 75–500 of the deposit, s 135.1 at 8933, s 474.17 at 17161.

Nothing else is brought in. "Carriage service" takes its meaning from the Telecommunications Act 1997 (Dictionary), asked as a fact.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `cc-accused.l4` | `cc-cases-accused.l4` | 90 written, 90 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The accused person**: someone charged with a Commonwealth offence, asking what has to be proved against them and whether a defence excuses them. The questions are the ones that person asks: "What do they have to prove?", "I didn't mean it", "I was drunk", "I thought it was mine", "I was threatened", "I was defending myself", "I was 13", "Is what I posted a crime?", "Is this Centrelink business fraud?".

Chapter 2 speaks of "a person", "the prosecution", "the defendant" and "the tribunal of fact". It is encoded as what it means for the accused: what must be proved against me, by whom and to what standard, and whether I am criminally responsible. No question is asked from the seat of the prosecution or the court.

The 2026-10-18 defaults:

- **The Act alone.** The Criminal Code (the Schedule to the Act); no instrument is needed.
- **The actors the text names:** the person, the prosecution, the defendant, the tribunal of fact, a Commonwealth entity.
- **Judgments handed to others are answered conditionally.** Every matter the Code makes "one of fact" or leaves to the tribunal is an input worded "the court finds …": whether a risk was unjustifiable (s 5.4(3)), negligence (s 5.5), whether a response was reasonable as the person perceived it (s 10.4(2)), whether reasonable persons would regard a use of a carriage service as menacing, harassing or offensive (ss 474.17(1)(b), 473.4), whether conduct was dishonest by ordinary standards (s 130.3(a)). The person's own beliefs and awareness are asked as facts about them.
- **The Act's own definitions are worked out from facts:** the fault elements (ss 5.2–5.5), the defaults (s 5.6), self-induced intoxication (s 8.1), basic intent (s 8.2(2)), dishonest (s 130.3). Borrowed terms ("carriage service", "Commonwealth entity" in its detail, "mental impairment" as a diagnosis) are asked as facts.
- **One case:** one physical element, one defence, or one charge.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** Chapter 1 beyond codification, the geographical jurisdiction rules (Part 2.7).

## Scope

**In:** s 2.2 (application of Chapter 2); ss 3.1, 3.2, 4.1, 4.2 (elements, voluntariness); ss 5.1–5.6 (fault elements and defaults); ss 6.1, 6.2 (strict and absolute liability); ss 7.1, 7.2, 7.3(1), (3), (5), (6) (age, mental impairment); ss 8.1–8.5 (intoxication); ss 9.1–9.5 (mistake of fact and law, claim of right); ss 10.1–10.5 (intervening conduct, duress, sudden emergency, self-defence, lawful authority); ss 13.1–13.5 (burden and standard of proof); s 130.3 (dishonest); s 135.1(1)–(6) (general dishonesty, gain and loss forms); s 473.4 (offensiveness matters, as the tribunal's input); s 474.17(1) (using a carriage service to menace, harass or cause offence).

**Out:** s 4.3 (omissions, beyond voluntariness); s 7.3(4), (7)–(9) beyond the comment; Part 2.4 (attempt, complicity and common purpose, commission by proxy, incitement, conspiracy); Part 2.5 (corporate criminal responsibility); s 13.6 (averments); Part 2.7 (geographical jurisdiction); every other offence in Chapters 4 to 10, including s 135.1(7) (influencing a Commonwealth public official), s 135.2 and the rest of Part 7.3, and the other telecommunications offences in Part 10.6. Sentencing for Commonwealth offences is in the Crimes Act 1914 baseline, and the rules of evidence in the Evidence Act 1995 baseline; neither is restated here.

## What the Act turns out to say

1. **Chapter 2 governs every Commonwealth offence, not only the Code's** — the Code's offences always, and every other Commonwealth offence for conduct on or after 15 December 2001 (s 2.2). Before that day an offence outside the Code was governed by the common law, which is not encoded: `not covered`. Asserted.
2. **Where an offence states no fault element, the default is intention for conduct and recklessness for a circumstance or result** (s 5.6), and recklessness is also proved by intention or knowledge (s 5.4(4)). Strict liability removes the fault element but keeps the reasonable-mistake defence (s 6.1); absolute liability removes both (s 6.2). Asserted.
3. **Knowledge and recklessness are defined only for circumstances and results** (ss 5.3, 5.4); for conduct, only intention is defined (s 5.2(1)). The encoding answers "no" to knowledge or recklessness as to conduct unless intention is proved and the fault is recklessness. Asserted.
4. **The deposited text has no rule that intention, knowledge or recklessness satisfies negligence.** Section 5.4(4) says proof of intention, knowledge or recklessness satisfies recklessness; s 5.5 has no equivalent. The encoding decides negligence on the tribunal's s 5.5 finding alone. Asserted (a case where intention is proved and negligence is not found answers "no"). Whether the courts read one in was not checked.
5. **Self-induced intoxication counts for some fault and not others.** It cannot be considered on voluntariness (s 4.2(6)) or on basic intent — intention as to conduct (s 8.2) — but may be on intention as to a circumstance or result, knowledge and recklessness, on whether conduct was accidental, and on a mistaken belief if the person had considered the facts (s 8.2(3)–(5)). For negligence and reasonable-belief defences the standard is a sober reasonable person (ss 8.3(1), 8.4(2)). Intoxication that was not self-induced (a spiked drink) excuses entirely if the conduct resulted from it (s 8.5). Asserted.
6. **A mistake of fact under s 9.1 need not be reasonable;** it excuses if it negates the fault element, and reasonableness is only something the tribunal "may consider" (s 9.1(2)). Under strict liability the mistake must be reasonable and the person must have considered whether the facts existed (s 9.2). Under absolute liability — for example that the payer in a s 135.1(5) charge was a Commonwealth entity — mistake is no defence (ss 6.2, 135.1(6)). Asserted.
7. **Ignorance of an Act is no excuse; ignorance of an unpublished instrument is** — if it had not been made available to the public or to those likely to be affected so that due diligence would have found it (s 9.4(2)(c)). Asserted.
8. **Self-defence is judged on the person's actual belief and the circumstances as they perceived them** (s 10.4(2)), but never covers intentionally inflicting death or really serious injury to protect property or deal with a trespasser (s 10.4(3)), nor resisting conduct the person knew was lawful (s 10.4(4)). Defending a person is not limited by s 10.4(3). Duress and sudden emergency, by contrast, need reasonable beliefs (ss 10.2(2), 10.3(2)). Asserted.
9. **The accused bears only an evidential burden for a defence or an exception** (s 13.3) — pointing to evidence of a reasonable possibility, which may come from the prosecution's case — after which the prosecution must disprove it beyond reasonable doubt (s 13.1(2)). A legal burden on the accused arises only where the law says so expressly (s 13.4), and is on the balance of probabilities (s 13.5). Mental impairment is proved on the balance of probabilities by whichever side relies on it (s 7.3(3)), and a child's knowledge of wrongness is for the prosecution (s 7.2(2)). Asserted.
10. **Section 474.17 states no fault element, and which default applies to "in a way ... that reasonable persons would regard as ... menacing, harassing or offensive" is an interpretive choice.** This encoding reads it as a circumstance, so recklessness applies (s 5.6(2)): the person must have been aware of a substantial risk that reasonable persons would so regard it. Whether reasonable persons would so regard it is the tribunal's, with the s 473.4 matters. The maximum is 5 years. Asserted on the encoding's reading. Raised in the ledger as a case-law question.
11. **General dishonesty does not require knowing that the victim was a Commonwealth entity** (s 135.1(2), (4)); for the s 135.1(5) form that element is of absolute liability (s 135.1(6)). "Dishonest" has two limbs — dishonest by ordinary standards, and known by the defendant to be so (s 130.3) — so a person who honestly believed they were entitled is not dishonest. The maximum is 10 years. Asserted.
12. **The age of criminal responsibility is 10, with a rebuttable bar to 14** (ss 7.1, 7.2). Asserted.

## Raised in the ledger

- **The fault element for s 474.17(1)(b)** (case law): whether the "reasonable persons would regard" element is a circumstance carrying recklessness, and what awareness that requires. Finding 10 turns on it.

## What would need doing before this is worth relying on

- **Part 2.4** (attempt, complicity, common purpose, incitement, conspiracy), which an accused often meets.
- **More offences** a member of the public meets: Part 7.3 fraud (ss 134.1, 134.2, 135.2), Part 7.2 theft, Part 10.6 telecommunications offences beyond s 474.17, Part 9.1 drug offences.
- **Case law.** No case was read; finding 4 and finding 10 are readings of the text, and every "one of fact" question is left to the tribunal.
- An independent test pass and a human review.
