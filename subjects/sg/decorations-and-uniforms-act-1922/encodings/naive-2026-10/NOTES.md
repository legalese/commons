# Decorations and Uniforms Act 1922 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/DUA1922.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on 31
December 2021". The Legislative History (not part of the Act) lists no amending law
after the Law Revision (Penalties Amendment) Ordinance 1952, commenced 30 April 1955;
everything since is a revised edition.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It is requirement **REQ-0132**: tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. The Act has
four sections, so the row takes all of its operative text: ss 2, 3 and 4. Left out:
s 1 (short title), who counts as "authorised" (the Act does not say, so it is an
input), and any subsidiary legislation or case law (none was retrieved).

## What the Act turns out to say

### 1. On stage, a uniform is fine but a medal is not

s 4(2) exempts "the wearing, use or supply of any insignia, decoration or uniform for
the purposes of any bona fide theatrical or similar performance". Everywhere else the
Act lists "decoration, medal, bar, clasp, ribbon, badge, stripe, emblem" as separate
things. Read literally, an actor may wear a military uniform but not a military
medal, ribbon or Armed Forces badge pinned to it. That is a literal reading; a court
might well read "decoration" more widely. Asserted.

### 2. The stage exception does not cover being called "Colonel"

s 2(1) also makes it an offence for an unauthorised person to assume "any title of
rank in the military, naval or air forces", or to use post-nominal letters
"indicating the possession of any order, decoration or medal". s 4 speaks only of
"wearing, use or supply". On its words, an actor billed by a military rank is not
covered by the exception. Police ranks are not named, though police uniforms are.
Asserted.

### 3. Wearing a convincing replica is an offence; selling one is not

s 2(1)(f) catches anyone wearing "anything so nearly resembling" a protected item
"that it is calculated to deceive". The supply offence in s 2(2)(b) lists the genuine
items and does not repeat paragraph (f). So a costume shop that sells deceptive replica
uniforms is not within the supply offence's words, though its customer may commit the
wearing offence. s 3 has no lookalike limb at all, so a deceptive copy of a
foreign civil order is caught by neither section. Both are inferences from what the
text leaves out. Asserted.

### 4. Foreign ribbons and badges: you may not wear them, but anyone may sell them

s 3(1) covers wearing "any foreign insignia, decoration, medal, bar, clasp, ribbon,
badge, stripe, emblem, or foreign uniform". The supply offence in s 3(2)(b) covers only
"foreign insignia, decoration, medal or foreign uniform". Supplying a foreign ribbon,
badge, bar, clasp, stripe or emblem is not an offence. Asserted.

### 5. One small penalty for everything, and "authorised" is never defined

Every offence carries "a fine not exceeding $400 or ... imprisonment for a term not
exceeding 3 months", tried before a Magistrate's Court. s 2(2) and s 3 say "the like
penalties". The text says "or", not "or both", so the encoding reads it as one or the
other; that is an inference. The Act never says who is "authorised". The latest
amending law in the Legislative History is the 1952 Penalties Amendment Ordinance.
Asserted (the limits; the meaning of "authorised" is an input).

### 6. Falsely claiming a medal is an offence even if you never wear one

s 2(2)(a) and s 3(2)(a) apply to "any person" who "falsely represents himself to be a
person who is or has been entitled" to wear a protected item. Nothing has to be worn.
s 4 does not reach it. Asserted.

## What would need doing before this is worth anything

- Who is "authorised" (Armed Forces Council and Presidential instruments, police
  regulations) was not looked for. It decides every case.
- Whether s 2(1)(c) and (e) reach foreign armed forces, overlapping s 3, is unsettled
  here. The cases use foreign civil items to stay clear of it.
- The literal readings in findings 1 to 3 were not tested against any case or
  Parliamentary material.
- The Orders and Decorations instruments that set up the Presidential orders were not
  retrieved.
