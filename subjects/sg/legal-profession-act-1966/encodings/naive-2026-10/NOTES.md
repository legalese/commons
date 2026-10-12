# Legal Profession Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 37 of
2023).

**Checks:** two case files, 96 assertions satisfied (lp-cases-clients.l4 52, lp-cases-admission.l4 44), 0 errors, 0 warnings.

## Why this Act, and why scoped

**36 of the 527 Singapore Acts** deposited here cite it, mostly s 2 (22). The Act is
636,000 characters, most of it the regulation of lawyers and law practices. This
row takes what a client, or a non-lawyer offering a legal-adjacent service,
meets: who may practise, what a non-lawyer may not do for a fee, fee
arrangements, suing for and challenging a bill, and the grounds for discipline.

## What the Act turns out to say

### 1. Anyone may charge to write a will; a non-lawyer may not charge to write a tenancy

s 33(2)(a): an unauthorised person who draws "any document or instrument relating to
any movable or immovable property" commits an offence unless they prove it was not
done for a fee. s 33(10): "'document' and 'instrument' do not include -- (a) **a
will** or other testamentary document". A will-writing service may lawfully charge;
a property agent who charges to draft a tenancy agreement commits an offence. But
preparing **probate** papers for a fee is caught (s 33(2)(b)). Asserted.

### 2. A debt collector's threat of legal action is an offence; "we will pass this to a solicitor" is not

s 33(2)(d): an unauthorised person who, for a fee, sends a letter "threatening legal
proceedings other than a letter or notice that the matter will be handed to a
solicitor for legal proceedings" commits an offence. The same demand framed as
referral is lawful. Asserted.

### 3. Anyone may represent a party in arbitration

s 35(1)(b): ss 32 and 33 do not extend to "any person representing any party in
arbitration proceedings" governed (or that would be governed if seated here) by the
Arbitration Act or International Arbitration Act, nor to advice and documents in
them -- "except for the right of audience in court proceedings". A non-lawyer may
charge to represent in an arbitration, not in court. Asserted.

### 4. No percentage of the damages, ever

s 107(1)(b): a solicitor must not agree to be paid "only in the event of success",
except by a conditional fee agreement under Part 8A (s 107(3AA)). s 115B: such an
agreement is allowed only in **prescribed** proceedings, must be in writing and
signed, and "must not provide for the remuneration or costs to be payable as a
percentage or proportion of the amount of damages". An uplift on success is
possible; a contingency share is not. The prescribed proceedings are in regulations
not retrieved. Asserted.

### 5. Paying a bill gives up the right to have it assessed

s 122: after 12 months from delivery "**or after payment** of the bill", no order for
assessment is to be made except "under special circumstances". A client who pays
first and disputes later has lost assessment as of course. s 118: a solicitor cannot
sue for fees within a month of delivering a signed bill, without leave. Asserted.

### 6. A foreign reprimand is due cause here

s 83(2)(k): due cause for discipline includes having been "disbarred, struck off,
suspended, ordered to pay a penalty, censured **or reprimanded**" as a lawyer "in any
other jurisdiction". The sanctions available here (s 83(1)) run to striking off, five
years' suspension, and a $100,000 penalty. Asserted.

### 7. Smaller things worth recording

- **s 32:** an admitted lawyer without a current practising certificate is an
  "unauthorised person".
- **s 33(2):** for the property-document, probate, demand-letter and personal-injury
  offences, the **defendant** must prove no fee was involved.
- **s 36(2):** a client who paid an unauthorised person for an act that was an offence
  can recover the payment.
- **s 34(1)(e), (i):** a person acting for themselves, and an accountant drawing
  documents in professional practice, are outside s 33.

## What would need doing before this is worth anything

- **Retrieve the Legal Profession (Conditional Fee Agreement) Regulations** and the
  Professional Conduct Rules.
- **No case law was searched.** The reach of s 33(2)(a) ("any document ... relating to
  ... property") has been litigated.
- The rest of the Act -- practising certificates, foreign lawyers, accounts and the
  disciplinary procedure -- is not encoded.

## Admission and practising certificates (added 12 October 2026 for REQ-0283)

Module `lp-admission.l4`, cases `lp-cases-admission.l4` (44 assertions). Source: the
deposit `LPA1966.txt`, version in force from 17 April 2025, Parts 2AA, 2A, 2B and 3
as recast by Act 37 of 2023 wef 17 July 2024.

### 1. The answer: two admissions by the court, then a practising certificate every April-to-March year

Before he may practise, the graduate must (a) be an **eligible person**, which since
17 July 2024 means first being **admitted by the court as a lawyer (NP)** (s 2(1),
ss 11A, 11B) unless the Minister approves him under s 14(1); (b) be **admitted by the
court as an advocate and solicitor** (s 12), which puts his name on the roll (s 16(2));
and (c) hold a **practising certificate** in force (s 32(1)). For the certificate he
applies to the Registrar "in every year before he or she does any act in the capacity
of an advocate and solicitor" (s 25(1)), and it is in force only "to the end of the
year", the year being 1 April to 31 March (s 25(3), (6)). That certificate is what he
renews each year. Asserted.

### 2. Where the text differs from the ledger's assumption

The ledger assumed he is "admitted on application after training". That is half
right. Admission is on application, but it is the **court's discretion** ("may, in
its discretion", s 12(1)): the Attorney-General, the Law Society and the Institute
may object (s 12(4)), and the court may adjourn or make other orders having regard to
his conduct and character (s 12(5A)). s 13 lists conditions without which he must
**not** be admitted (21, good character, the practice training period served,
prescribed courses completed and examinations passed); meeting them does not entitle
him to admission. The encoding says only that nothing in ss 12 and 13 bars it.
The ledger also left out the **lawyer (NP)** step, which is now the gateway: a law
graduate who has not been admitted as a lawyer (NP) is not an eligible person and
cannot be admitted as an advocate and solicitor. Asserted both ways.

### 3. The Act does not say six months, and does not name a Bar course

The length of the practice training period is left to the Institute's rules
(s 10(2)(b), "including different durations for different classes"), as are the
courses and examinations for each admission (s 10(2)(c), (d), (da), (db)), their
period of validity (s 10(2)(fa)) and the admission procedure and fees (s 10(2)(g),
(h)). Whether Haziq's six months satisfies s 13(c) depends on those rules; the
encoding takes the applicable period as an input and the cases assume six. Reading
"completed the Bar course" as completing the prescribed courses and examinations is
an assumption, labelled in the case file.

### 4. The annual certificate dies on 31 March, whenever issued

s 25(3) and (6): a certificate issued on 1 August 2026 or on 15 February 2027 alike
expires on 31 March 2027. s 25(5): one issued in April counts as in force from
1 April. Asserted.

### 5. What he must declare and who may not apply

s 25(1): the application carries declarations of his practice, that he is not
disqualified, that Law Society subscriptions, levies and Compensation Fund
contributions and Academy moneys are paid or arranged, professional indemnity
compliance, any Institute-prescribed declaration (s 25(1)(ca); [inference] probably
the continuing professional development declaration, since s 10(2)(i) gives CPD
rules to the Institute), an accountant's report or Council certificate, and the
prescribed fee. s 26(1): he may not apply unless practising or intending to practise
in a Singapore law practice (or under s 36E, or as a locum), nor while an undischarged
bankrupt, in a composition with creditors, with $100,000 or more of judgments unpaid
for 6 months, or lacking capacity. The Registrar "must ... thereupon issue" subject to
ss 25A, 25AA and 25B. Asserted.

### 6. Between training and admission: the provisional practising certificate

A lawyer (NP) serving training with a Singapore law practice, who has served the
prescribed part of it, must get a provisional practising certificate before acting
as an advocate and solicitor under supervision (s 18(1), (2), s 32(1A)). It lasts
12 months from issue or until admission, whichever is earlier (s 18(6)). The
encoding reads 12 months as 365 days [inference]; the prescribed period is an input.

### 7. Needs other instruments

The Institute's admission rules and the Minister's qualified-person rules (titles not given in the deposit; who is a
qualified person, the courses, examinations, practice training period and its
length, admission procedure and time limits), the Law Society's rules on practising
certificates and provisional practising certificates (ss 18(9), 25(7)), the CPD rules
(s 10(2)(i)), and the fees under s 189. None was retrieved. No case law was searched.
