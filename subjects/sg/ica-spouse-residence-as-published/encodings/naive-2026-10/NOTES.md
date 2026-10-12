# ICA: a citizen's foreign spouse (LTVP, PR, citizenship) -- naive encoding (as published)

**This is administrative policy as published, not law.**
Everything here is what the Immigration & Checkpoints Authority (ICA) says on its website, as read on 12 October 2026.
ICA can change any figure without legislation and without notice.
The pages give a "Last updated" date but no effective date, so each figure is dated by its page (below) and nothing has a dated arm.

## Method

NAIVE. One pass, straight from the pages, by an assistant session working without the writing-l4-rules skill (it was not available).
There was no pipeline, no coverage table, no independent test pass and no human gate.
The pages were fetched with WebFetch and with curl, then reduced to text.
Only short phrases are quoted.

The policy sits on two pieces of law, and each has its own row; the statutory tests are left there:

- **Constitution, Art 123(2)**: registration of a citizen's wife. **Art 126** is the oath and **Art 128** is renunciation by a Singapore citizen. Row: `constitution-of-the-republic-of-singapore/encodings/naive-2026-10`. Art 123(2) says the Government "may" register, so registration is discretionary.
- **Immigration Act 1959, s 10 and s 55(1)(c)**: entry permits (that is, PR) and passes made by regulations. Row: `immigration-act-1959/encodings/naive-2026-10`. The Immigration Regulations are not deposited.

## Sources (all read 12 October 2026)

| Page | URL | Last updated |
|---|---|---|
| Apply for Singapore Citizenship | https://www.ica.gov.sg/reside/citizenship/apply | 30 June 2026 |
| Singapore Citizenship (landing) | https://www.ica.gov.sg/reside/citizenship | not recorded |
| Oath-taking for Minors | https://www.ica.gov.sg/reside/citizenship/minor-oath-taking | 29 June 2026 |
| Apply for Permanent Residence | https://www.ica.gov.sg/reside/PR/apply | 13 March 2026 |
| Apply for Long-Term Visit Pass | https://www.ica.gov.sg/reside/LTVP/apply (and /reside/LTVP) | 08 April 2026 |
| LTVP, spouse of a Singapore citizen | https://www.ica.gov.sg/reside/LTVP/apply/spouse-of-a-singapore-citizen-(sc) | 06 April 2026 |
| Pre-Marriage LTVP Assessment | https://www.ica.gov.sg/reside/PMLA | 27 October 2025 |
| Renunciation (of Singapore citizenship) | https://www.ica.gov.sg/enter-depart/for-singapore-citizens/renunciation | 13 March 2026 |
| Citizenship document checklist (PDF) | https://www.ica.gov.sg/docs/default-source/ica/ipses/sc-document-checklist | none in the text (file dated 8 July 2024) |
| Terms of Use | https://www.ica.gov.sg/terms-of-use | (licence only) |

ICA's FAQ link (https://www.ica.gov.sg/faqs) redirects to ask.gov.sg. That is outside ica.gov.sg, so it was not read.
Guessed URLs for a citizenship completion-of-formalities page and a Singapore Citizenship Journey page all returned 404.

## Checks

`l4 run icasp-cases-spouse-residence.l4`, counted with `runcases.py`: **45 written, 45 satisfied, 0 errors, 0 warnings.**
The first ten assertions answer the requirements on their own facts. The other 35 test the boundaries, the fees and the minor's ORAL.

## Findings

1. **REQ-0291, the first half: yes, she may apply, but the grant is discretionary.**
   ICA's spouse category asks for at least 2 years as a PR and at least 2 years married to a Singapore citizen, with the citizen spouse sponsoring. Two years as a PR and nine years married meets both.
   ICA lists assessment factors and gives an In-Principle Approval, not a right. Art 123(2) agrees that the Government "may" register.
   At 35 she must also complete the Singapore Citizenship Journey (ages 16 to 60). The fees are $100 on submission and $70 + $10 on completion, $180 in all.
   The scenario date is 20 July 2033. This answer is on the policy as published in October 2026.
   The ledger expects "registered". The encoding says "may apply", which is not the same as registered. Whether she is registered is a decision, not a test the pages state.

2. **REQ-0291, the second half: not answered from ICA's pages.**
   None of the pages read says that an adult applicant (spouse or otherwise) must renounce foreign citizenship or take an oath.
   The citizenship page says only that successful applicants become citizens once they have "fulfilled the necessary conditions", and it does not list them beyond the Singapore Citizenship Journey.
   The Renunciation page covers renouncing Singapore citizenship, not a foreign one, and the document checklist does not mention either.
   The only published trace is on the minors' oath page. A person registered as a minor takes the Oath of Renunciation, Allegiance and Loyalty (ORAL) between ages 21 and 22, and a "Foreign Citizenship Renunciation Certificate" is among the documents. That is encoded, but it is not the adult rule.
   The ledger's assumption ("Malaysian citizenship renounced") is therefore neither confirmed nor contradicted here. The oath belongs to Art 126 in the Constitution row.
   Because of this half, the commit says the row **addresses** REQ-0291 rather than satisfying it.

3. **ICA's test and Art 123(2) differ in form.**
   The Constitution row encodes Art 123(2) as 2 years' continuous residence, among other conditions. ICA asks for 2 years as a PR **and** 2 years of marriage.
   Neither is decided against the other here. The marriage period is ICA's addition.

4. **REQ-0286 (helped, stays open).**
   ICA lists "spouse of a Singapore citizen" as an LTVP category, with the citizen sponsoring, and says marriage does not guarantee approval.
   The LTVP fees are $45 + $60, plus $30 for a multiple journey visa. It takes up to 6 months, or 6 weeks if the couple did the free PMLA, whose letter can be used within a year.
   For PR, a citizen's or PR's spouse may apply, and **no minimum period of marriage or residence is stated**. The fees are $100 + $20 + $50 + $50 = $220, with a 5-year re-entry permit, processed within 6 months.
   So the published answer to "after how long" is: ICA states no period.
   LTVP+ is mentioned only in a page description ("considered for LTVP+"); its requirements are not on the pages read.
   The legal basis of the pass remains the undeposited Immigration Regulations.

## What would need doing

- Find ICA's (or MHA's) published statement of the conditions of In-Principle Approval for an adult new citizen: renouncing foreign citizenship, the oath and the deadline. It may be in the IPA letter or on ask.gov.sg, which this row did not read. Then close the second half of REQ-0291.
- Find the LTVP+ criteria and the LTVP validity periods, if ICA publishes them.
- Re-read the pages when their "Last updated" date changes; the figures have no other dating.
- Deposit the Immigration Regulations to give REQ-0286 its legal basis.
