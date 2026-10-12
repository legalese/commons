# Administration of Muslim Law Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 4
of 2024 (latest commencement annotated 1 October 2025) and Act 5 of 2025 (9 March
2025) shown. The Third Schedule amounts carry the annotation S 144/2016.

**Checks:** two case files, 161 assertions satisfied (117 + 44), 0 errors, 0 warnings.

## Why this Act, and why scoped

**10 of the 527 Singapore Acts** deposited here cite it. Most of the Act sets up
institutions (the Majlis, the Syariah Court, wakaf and mosque administration). This
row takes the rules an ordinary Muslim, employer or wedding party meets: Mosque
Building and Mendaki Fund contributions and the opt-out (ss 78, 79, Third Schedule),
halal certificate offences (s 88A(5)), who may solemnise a marriage and when (ss 94B,
95 to 97, Fourth Schedule), attending the Syariah Court after a divorce (s 102(5)),
and the Part 9 offences (ss 129 to 140). Divorce grounds and orders, the Court's
jurisdiction, inheritance (Part 7), Haj regulation, appeals, the betrothal claim (s 94)
and the marriage preparation programme (s 94A, whose class is set by rules) are not
encoded.

## What the Act turns out to say

### 1. An under-18 exception exists for a girl, not for a boy, and only a Kadi can use it

s 96(4) bars a marriage where "either party is below 18 years of age". s 96(5) lets
"a Kadi" in special circumstances solemnise the marriage of "a girl who is below 18
years of age but has attained the age of puberty". There is no matching exception for
a man below 18, and neither a Naib Kadi nor the wali may use it. Asserted.

### 2. Part 9 offences reach only Muslims, so cohabitation is an offence for one partner and not the other

s 134 makes it an offence for a man or a woman to cohabit with someone "whether a
Muslim or not" to whom they are not married. But s 129: "this Part only applies to
Muslims". Where one partner is not Muslim, only the Muslim partner can commit the
offence. Only a woman can be sent to "a place of safety" for up to 12 months instead
of being sentenced (s 134(3)). The halal offence (s 88A(5)) and the Fund offences
(s 78) sit outside Part 9 and reach anyone. Asserted.

### 3. A man who is already married can marry again only through a Kadi

s 96(2): if the man is married to someone else, the marriage may be solemnised only by
a Kadi, or by the wali "with the written consent of a Kadi". A Naib Kadi, who can
otherwise solemnise at the wali's request, cannot; and a Naib Kadi's consent does not
let the wali proceed. Since 22 October 2018 a wali may solemnise any marriage only
with a Kadi's or Naib Kadi's written consent and one of them present (s 95(2)). A Kadi
alone may proceed where there is no wali or the wali refuses on grounds the Kadi finds
unsatisfactory (s 95(1)(c)). Asserted.

### 4. The Mosque Building and Mendaki Fund contribution is opt-out

s 78(1): every employer of a Muslim employee "must pay" monthly by the Third Schedule
($3 on wages up to $1,000, rising to $26 above $10,000), and may recover it from the
wages (s 78(2)). The employee may opt out by certificate (s 79), and liability revives
when the certificate lapses. An employer that deducted the money and did not pay it
over faces up to $2,000, four times the $500 for simply not paying (s 78(3), (4)).
Asserted.

### 5. The iddah does not bar remarrying the last husband; the triple talak does

s 97(1)(a) forbids a janda's marriage before her iddah expires only "to any person
other than the husband from whom she was last divorced". s 97(1)(c): after a divorce
"by 3 talak" she may not remarry that husband unless an intervening marriage was
consummated and lawfully dissolved. She must always produce one of the listed
certificates first (s 97(1)(b)). Asserted.

### 6. The penalties are small, except for two

Most Part 9 offences carry a fine up to $500 or six months. Not paying fitrah: $50 or
one month (s 137(2)), and conviction does not extinguish the debt (s 137(3)). False
doctrine: $2,000 or 12 months, with the court to presume a doctrine contrary to Muslim
law on the Mufti's evidence (s 139(2)). Enticing an unmarried woman from her wali:
up to three years and a fine with no stated maximum (s 135). Using a halal mark
without approval: $10,000 or 12 months (s 88A(5)). Asserted (the uncapped fine is
encoded as -1).

### 7. Whose consent a minor needs depends on legitimacy and custody

s 94B and the Fourth Schedule: for a legitimate minor, both parents if they live
together; the custodial parent after divorce; the deserted parent where one deserted
the other. For an illegitimate minor, the mother (or whoever a court gave custody);
the father is not named. A Kadi MUST dispense with an absent person's consent when
someone else's consent is also required, and MAY when no one else's is (s 94B(2)).
"Minor" is not defined in s 2 of the deposit. Asserted.

## What would need doing before this is worth anything

- The rules under ss 81 and 145 (prescribed times for contributions and registration,
  exemptions, the marriage preparation class) were not retrieved.
- s 102(5)'s "within 7 days beginning on the date of the divorce" is encoded as the
  divorce date plus six days; that reading is an inference.
- The Fourth Schedule's case of one dead parent with a guardian appointed by that
  parent, and the meaning of "minor", are not encoded.
- No Syariah Court or High Court decisions were searched.

## Source refreshed after encoding (10 Oct 2026)

This row was encoded against the deposit as it stood before the source refresh: the SSO consolidation current at the
earlier retrieval, still in git at commit da331074. The deposit has since been replaced by the consolidation current as at
9 October 2026, whose text differs. **The row has not been re-checked against the refreshed text.** Its assertions do not
read the source, so they still pass; whether the encoded provisions changed is an open question.

## Wills and inheritance (added 12 October 2026 for REQ-0282)

Module `amla-wills-inheritance.l4`, cases `amla-cases-wills-inheritance.l4` (44 assertions). ss 110 to 116 and 118, numbered
from the BODY of the deposit: the arrangement table at its head is out of step from s 111 (it lists "113. Inheritance
certificate" and "115. [Repealed]"); in the body s 115 is the inheritance certificate and s 117 is the repealed section. The
ledger's numbers (s 111, s 115) match the body.

### 1. The answer: the will is valid only so far as his school allows; the Act states no "one third"

s 111(1): no Muslim domiciled in Singapore may, after 1 July 1968, dispose of property by will "except in accordance with the
provisions of and subject to the restrictions imposed by the school of Muslim law professed by him or her", despite English
law or any other written law. The Act does not say what those restrictions are. The ledger's "valid up to one third to a
non-heir" is a rule of Muslim law (a school's rule), not a provision of the Act; nothing in the deposit states it. The
encoding takes the school's answer, or its fraction, as an input. On the ledger's assumption that his school allows a
one-third gift to a non-heir, the gift to the charity stands; a share above the supplied limit does not. Asserted both ways.

### 2. The two thirds pass by Muslim law as a partial intestacy

s 112(1) and (2): the estate of a Muslim domiciled in Singapore dying intestate is distributed "according to the Muslim law as
modified, where applicable, by Malay custom", and this applies where he "dies partly intestate". So the part of Haziq's estate
not disposed of by the will goes to the heirs by Muslim law. Who the heirs are and their shares is again Muslim law, not the
Act. Asserted.

### 3. No certificate is required by the Act; the inheritance certificate is available, not compulsory

s 115(1): in proceedings on the administration or distribution of an estate to be distributed by Muslim law, where a court or
authority must determine the persons entitled or their shares, the Syariah Court "may", on a request by that court or
authority, or on the application of a person claiming to be a beneficiary, and on payment of the prescribed fee, certify its
opinion on who is entitled and in what shares. Nothing in the deposit makes the certificate a condition of distribution or
puts a duty on the family to obtain one. The ledger's "must obtain" goes beyond the text; whether a court or authority in practice
asks for one is a matter of practice or rules, not the Act (not retrieved; inference that it may). Asserted as a constant FALSE plus the
conditions under which the Court may certify. Reading: the fee is treated as due on both routes; the text could be read as
attaching it to the beneficiary's application only.

### 4. The Syariah Court certifies on law, never on facts

s 115(1), (2): the opinion rests on facts found by the court or authority or on hypothetical facts; the Syariah Court may hear
the parties on a question of law but "is not to hear evidence or make findings on any question of fact". s 115(3): in a case of
special difficulty it may refer the question to the Legal Committee of the Majlis and, if that opinion is given, must certify
in accordance with it. Asserted.

### 5. Other points encoded

- s 113: the probate or administration affidavit for a deceased Muslim must state the Mazhab professed.
- s 111(2): the restriction does not affect the Wills Act 1838 (except its s 3), the Insurance Act 1966, the Probate and
  Administration Act 1934, or the will of a Muslim who died before 1 July 1968. The date test is encoded on the date of death
  from (2)(d); s 111(1)'s "after 1 July 1968, dispose" could be read as the date of making the will (inference).
- s 112(3): for "a Malay dying intestate" the court may divide harta sepencarian; its reach to partial intestacy rests on
  s 112(2) (inference).
- s 116: letters of administration on intestacy may go to any next-of-kin or anyone entitled to a share under Muslim law.
- s 118: a married woman may, with or without her husband's concurrence, by will dispose of her own property, subject to s 111.

### What the full answer still needs

- The rule of the school professed (for most Singapore Muslims, by inference, the Shafi'i school) on the bequeathable third and
  bequests to heirs; s 114 lets the court take it from the listed books. Not in the Act.
- The Administration of Muslim Law rules on the inheritance certificate fee and form (s 145(2)(e), (f)); not retrieved.
- Whether the High Court or Public Trustee in practice requires a certificate before granting or distributing (Probate and
  Administration Act 1934, Rules of Court, practice); not retrieved.
- No Syariah Court or High Court decisions were searched.
