# Children and Young Persons Act 1993 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 30
of 2019 shown in force. That includes the extended definition of "young person", in
force from 30 December 2025.

**Checks:** two case files, 85 assertions satisfied (40 in `cyp-cases-protection.l4`, 45 in
`cyp-cases-youth-court.l4`), 0 errors, 0 warnings.

## Why this Act, and why scoped

**16 of the 527 Singapore Acts** deposited here cite it. This row takes the protective
definitions and the offences against children (ss 2, 5 to 8). Removal powers, care
orders, the Youth Court, youth offenders, homes, fostering and the publication
restrictions are not encoded.

## What the Act turns out to say

### 1. "Young person" now runs to 18

s 2: a child is under 14 and a young person is 14 to 17. The upper limit was raised from
16 by Act 30 of 2019, in force 30 December 2025. Asserted.

### 2. A parent who knows of the risk and does nothing is guilty too

s 6(1), (2): a carer "knowingly permits" ill-treatment by another if they know **or have
reason to believe** the child is at risk and fail to take the steps reasonably expected
of them. The court takes into account the carer's own experience of being ill-treated
by the same person. s 6(5) allows conviction even if someone else prevented the harm.
The maximum is 14 years if death is caused, 8 otherwise. Asserted.

### 3. Emotional abuse is spelled out

s 5(2) lists what counts as emotional or psychological abuse:
- persistent rejection or degradation
- threats
- isolation
- **confinement in a small space as discipline**
- encouraging maladaptive behaviour
- exposure to violence against someone the child cares about

Each makes a child in need of care or protection. Asserted.

### 4. Sexual offences: 16 and 17 turn on consent or exploitation

s 8(1): any indecent act with or by a person under 16 is an offence regardless of
consent. For 16- and 17-year-olds (s 8(2), (3)) it is an offence if there is no consent
**or** the relationship is exploitative, and consent need not be proved either way for
the second limb. s 8(8) presumes exploitation where the accused is in one of these
roles:
- step-parent or other parental figure
- teacher at the young person's school
- established instructor
- custodial officer
- treating doctor or psychologist
- lawyer or counsellor

s 8(9) disapplies the presumption to a lawful spouse. Asserted.

### 5. Smaller things worth recording

- **s 7(2):** a carer who allowed a child to be where the child was begging is presumed
  to have allowed it for that purpose.
- **s 8(10):** up to 7 years where a child is involved, 5 where a young person is; 10
  and 7 for a repeat offender.

## What would need doing before this is worth anything

- The procedure that follows a s 5 finding (removal, orders, review) is the part
  families meet in practice and is not encoded.
- "Relevant offence" in s 5(1)(h) is defined by a schedule that was not read.
- No case law was searched.

## The Youth Court (added 11 October 2026 for REQ-0266)

Module `cyp-youth-court.l4`, cases `cyp-cases-youth-court.l4` (45 assertions, the first ten on REQ-0266's own facts).
Raised by the Jun Hao scenario, event j023: a fifteen-year-old charged with theft from a shop.

### 1. The answer: the Youth Court, and probation is one of eleven orders

s 39(1): no child or young person may be charged or tried by a court of summary jurisdiction "except a Youth Court".
Theft is not triable only by the High Court (s 39(2)), there is no adult co-accused (s 39(3)), and at 15 he is below the
16 at which s 39(2A) can send a Second Schedule offence elsewhere. Theft is not in the Second Schedule in any case (the
Penal Code entries there are extortion, robbery, cheating, fraud, house-breaking and others, not ss 378 to 382).

On proof or admission, s 49(1) gives the Youth Court power to:
- (a) discharge;
- (b) discharge on a good-behaviour bond;
- (c) commit to a relative or fit person;
- (d) order the parent to execute a bond for proper care;
- (e) make a **probation order**, 6 months to 3 years;
- (f) order community service, at most 240 hours;
- (g) detain in a place of detention, at most 6 months (3 if combined with probation, s 49(3));
- (h) weekend detention, at most 26 weekends;
- (i) send to a juvenile rehabilitation centre, at most 3 years;
- (j) fine, damages or costs;
- (k) reformative training, but only at 18 or over, or at 14 to 17 with a previous JRC order or too unruly for a JRC or
  place of detention. Not available to Jun Hao on a first offence.

The ledger's expected answer is right on both points. Asserted.

### 2. Where the text differs from the ledger's framing

- **The section numbers.** The powers on proof are **s 49**, not within ss 38 to 48 as the ledger has it. The deposit's
  arrangement table lists them against s 48, but the body numbers them 49 (s 48 is the presumption as to age).
- **"Instead of recording a conviction."** s 46(1) says the words "conviction" and "sentence" "cease to be used" for
  children and young persons dealt with by a Youth Court; s 46(2) reads references elsewhere to a conviction as a "finding
  of guilt". s 49 does not say whether a finding of guilt is recorded: its orders follow proof or admission. The one
  provision that expressly allows an order **without** a finding of guilt is s 44(3): an order on the **parent** to pay
  damages or costs or give security for good behaviour. A fine is not in that list. Asserted.
- s 41: a conviction or finding of guilt of a child or young person is disregarded for any Act imposing a disqualification
  on convicted persons. Not asserted.

### 3. The law encoded is the law from 30 December 2025, not 2021

Event j023 is dated 20 November 2021. The deposit is the version in force from 1 July 2026, with amendments by Acts 30 of
2019, 31 of 2022 and 21 of 2025 in force 30 December 2025 (s 39(2A) to (2F), s 42(2A), (3), (4), and the extended
"young person"). The 2021 text is not deposited. **Inference, not checked:** at 15 he was a young person under both
definitions. s 39(1) carries only the note [27/2014]. s 49(1) carries a note "[Act 21 of 2025 wef 30/12/2025]" that does not
say which paragraphs it touched; perhaps (k), which names ages 14 to 17. So the Youth Court answer probably holds for 2021,
but the 2021 list of orders should be checked against the earlier text before it is relied on.

### 4. Other provisions encoded

- **s 36:** a person apparently below 18 who is arrested and not released goes before a Youth Court, or a Magistrate within
  48 hours. The court must release on a bond unless one of the six s 36(3) circumstances exists, such as a risk of absconding.
- **s 38:** a judge acting on a written report sits with 2 advisers, or with 1 or none if an adjournment would be inexpedient.
- **s 39:**
  - a High Court-only charge stays in the High Court unless the Public Prosecutor applies **and** the defence consents;
  - a 16- or 17-year-old charged with a Second Schedule offence goes to another court on the Prosecutor's fiat;
  - a charge joint with an adult goes to another court;
  - so does anyone who is 18 when the hearing starts.
- **s 42:**
  - a child is never imprisoned;
  - a 14- or 15-year-old only if certified unruly;
  - a 16- or 17-year-old also when convicted in the High Court or of a relevant offence in another court;
  - no corporal punishment at 14 or 15 except by the High Court.
- **s 44(1):** a fine, damages or costs "must" be ordered against the parent unless the parent cannot be found or did not
  conduce to the offence by neglect.
- **s 49(2):** the combinations allowed:
  - any of (b) to (f) and (j) together;
  - detention with (d), (e) or (j);
  - weekend detention with (c) to (f) or (j), or consecutive to detention;
  - JRC with (d) or (j).

  Discharge and reformative training combine with nothing.

### 5. Needs other instruments

- **Penal Code 1871:** the theft offence itself (ss 378 to 380), and the minimum age of criminal responsibility (provision not read).
- **Criminal Procedure Code 2010:** s 305 (reformative training) and the corporal-punishment provisions, for those below 14.
- **Children and Young Persons regulations:** the "prescribed requirements" for community service orders (s 49(1)(f)) and
  juvenile case conferences (s 50).
- **Probation of Offenders Act 1951:** may bear on probation alongside s 49(1)(e). Not read.
- **No case law was searched:** for example, on sentencing principles for juvenile theft.

