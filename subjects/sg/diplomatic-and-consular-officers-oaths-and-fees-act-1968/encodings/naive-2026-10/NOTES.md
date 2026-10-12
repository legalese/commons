# Diplomatic and Consular Officers (Oaths and Fees) Act 1968 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/DCOOFA1968.txt`. It "incorporates all amendments up to
and including 1 December 2021 and comes into operation on 31 December 2021". No later
amendment is annotated.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is requirement **REQ-0168** in `subjects/sg/requirements.jsonl`: Tier 3 of
the remaining Singapore Acts, ordered by everyday-life relevance. The requirement
asks what the Act decides for a person or business it applies to; no scenario has
asked a sharper question yet. The person it reaches is a Singaporean abroad who needs
a document sworn, declared or notarised at an embassy or consulate.

The Act has 11 sections, so the whole operative text (ss 2-11) is encoded. Not
encoded: the fees themselves, which are fixed by Ministerial order under s 4 (not
retrieved); how they are levied and accounted for (s 4(b)); which Powers and
countries a President's order under s 3(3) covers; and what notarial acts a notary
public can do in Singapore (s 3(1)(c) points to that, but the Notaries Public Act was
not read).

## What the Act turns out to say

### 1. Failing to display the fee table is a duty with no offence

s 5 says every officer entrusted with consular duties "shall exhibit" the fee order
prominently and "shall permit" anyone to inspect it at any reasonable time. But s 7
lists only false swearing, forgery and using a forged affidavit, and s 6(2) only the
improper fee. Nothing in the Act makes a breach of s 5 an offence. Asserted.

### 2. An officer who charges a fee not fixed by order commits a crime

s 6(1): "Subject to any order made under section 4", the officer "shall not ask for or
take any fee or reward" for anything done in the execution of the office. Merely
asking is enough. s 6(2) makes it an offence "without prejudice to any other
liability", and s 8 gives the same penalty as forgery. That charging more than the
fixed amount is also caught is an inference from "subject to any order"; the Act does
not say so in terms. Asserted (with the inference).

### 3. A document sworn abroad is as good as one sworn in Singapore, and proves itself

s 3(1): an oath, affidavit or notarial act done before a Singapore diplomatic or
consular officer exercising functions outside Singapore, "in that country", is "as
effectual as if" done before lawful authority in Singapore. s 3(2): a document bearing
the officer's seal and signature is admitted in evidence without proof of either or of
the officer's official character. "Affidavit" includes statutory declarations,
acknowledgments and attestations (s 2). Asserted.

### 4. Where Singapore has no mission, another country's diplomat can stand in, for notarial acts only

s 3(3): the President may by order extend s 3(2) to persons in the foreign service of
a Power that represents Singapore where Singapore has no diplomatic or consular
representatives. The extension covers only "the proof of notarial acts", not oaths or
affidavits, and only for persons named in the order. Asserted.

### 5. A Constitution oath abroad needs a citizen officer

s 3(4): an oath required for the purposes of the Constitution counts only if taken
before an officer "who is himself a citizen of Singapore". Asserted.

### 6. The offences reach conduct anywhere, but only with the Public Prosecutor's consent

s 8: a fine up to $5,000, imprisonment up to 3 years, or both. s 11: an offence may be
tried in Singapore "as if the offence had been committed in Singapore"; s 10: no
prosecution without the Public Prosecutor's consent. Using a forged affidavit is an
offence only when the user knows it is forged (s 7(c)). Asserted.

### 7. Everything done before the Act is deemed done under it

s 9 deems every oath, affidavit and notarial act done by an officer abroad before
6 January 1969 (the commencement date in the deposit) to have been done under the Act.
Asserted.

## What would need doing before this is worth anything

- The s 4 fees order(s) were not retrieved; the fee rule is tested with made-up figures.
- No President's order under s 3(3) was retrieved.
- The s 2 definitions are inclusive ("includes"); the encoding treats only the named
  offices as officers, which is an inference.
- The Notaries Public Act was not read, so the reach of s 3(1)(c) is unencoded.
- No case law was searched.
