# Korea AI Framework Act and Enforcement Decree: answers decided from the source alone

Independent test author, 2026-10-24.
Written BEFORE opening anything else under `encodings/solo-2026-10/` and before `NOTES.md`.
Not for use as advice.

Sources read, whole, in Korean (authoritative): `registers/source-bundle/kr-ai-act-ko.txt` (405 lines: Articles 1-43 and the addenda of Act No. 20676, No. 21065 and No. 21311), `kr-ai-decree-ko.txt` (406 lines: Articles 1-33 and the addenda of Decree No. 36053, No. 36506 and No. 36580), `kr-ai-decree-annex2-ko.txt` (Annex 2, fines), and the four `.meta.json` files.
Locators below are `act:N`, `decree:N`, `annex2:N`: line N of those text files.
No English text was deposited; no MSIT notice (고시) was deposited.
Every answer is "on the deposited text".
I also grepped the two `.html` originals for the words searched in (2), to check the text extraction dropped nothing: the only extra hits are page-chrome (`조문체계도`, "article structure diagram", which contains 계도).

Seat: an AI business operator (인공지능사업자, Act Art 2(7)).

## (1) Does the Art 32 safety obligation bind me?

Art 32(1) (act:333): an 인공지능사업자 "must implement" (이행하여야 한다) the two items for an AI system whose cumulative training compute (학습에 사용된 누적 연산량) is at or above the Decree's standard.
Decree Art 24(1) (decree:302-305) defines that system as one that meets ALL (모두 충족) of:

1. cumulative compute used in training of 10^26 floating-point operations or more (10의 26승 부동소수점연산 이상, decree:303). The unit is a count of operations, not operations per second. 이상 is "at or above": exactly 10^26 satisfies it; 10^26 minus anything does not.
2. it is built and operated applying the most advanced (최첨단) AI technology among the technologies currently used in AI systems, considering the state of development (decree:304).
3. its risk is such that there is a concern of broad and serious (광범위하고 중대한) impact on human life, bodily safety and fundamental rights (decree:305).

The criteria are cumulative: compute at or above 10^26 with criterion 2 or 3 failing does not bind.
Who decides: no decider is named. There is no designation, confirmation or notification step for Art 32 systems (contrast Art 33 and Decree 25, a confirmation procedure for high-impact AI only). The operator must apply the criteria itself; MSIT's route is Art 40 (investigation, then order).
How compute is counted: delegated to an MSIT notice (decree:306, 구체적인 산정 방식 ... 고시); not deposited, and the bundle's aid evidence says law.go.kr lists no such notice.
Exclusion: Act Art 4(2) with Decree Art 2 (act:38, decree:18-40): AI developed and used only for designated defence/intelligence/police tasks is outside the Act.

Forks:
- F1 (addressee). Art 32(1) says "인공지능사업자" without limiting it to the developer (개발사업자). Reading A (literal): any AI business operator in relation to such a system, including a 이용사업자 offering a service built on another's frontier model. Reading B: only the operator who trains/controls the system. The text does not settle it.
- F2 (delegation). The Act delegates only "a standard of cumulative compute" (누적 연산량이 대통령령으로 정하는 기준 이상). The Decree adds two non-compute criteria. Reading A (as written): all three. Reading B: the Decree's criteria 2 and 3 go beyond the delegation and compute alone decides. I take A, the Decree's text.
- F3 (criteria 2 and 3 are evaluative). "최첨단" and "광범위하고 중대한 영향" have no test in the text; they are facts the operator states.

## (2) Is there ANY duty on me to report an AI incident, accident or malfunction?

**No. On the deposited text, no provision of the Act, the Decree or Annex 2 requires an AI business operator to report an AI incident, accident, malfunction or harm to MSIT or to anyone.**

Where I looked: every Article of the Act (1-43, and the three addenda) and of the Decree (1-33, and the three addenda), and Annex 2. Word searches over the three text files, and over the two HTML originals:

| Word | Hits | What they are |
| --- | --- | --- |
| 사고 (accident) | 1: act:335 | Art 32(1)2: a duty to BUILD a risk-management system that monitors and responds to AI-related safety accidents. A duty to have a system, not to report an accident. |
| 장애 | act:36, decree:6, 13 | 장애인 (disabled persons); not "failure". |
| 오작동, 사건 | 0 | |
| 침해 | act:305; decree:26-38 | Art 28(2)2 (a voluntary private ethics committee may research safety and rights infringement); Decree Art 2 (security tasks). No duty. |
| 보고 (report) | decree:85-86 (state bodies report to the Committee on recommendations), decree:230 (cluster agency reports its plan) | not addressed to an operator |
| 신고 | act:354 (Art 36: report the domestic representative's designation), act:379 (Art 40(1)2: MSIT may act on someone's report or complaint OF a violation) | neither is an incident report |
| 통보, 알려 | decree:47 (MSIT notifies a plan), decree:318 (MSIT tells a requester of an extension) | addressed to MSIT |
| 제출 (submit) | act:336 (Art 32(2)), act:355 (Art 36(1)1), act:377 (Art 40(1)); decree:307, 319 (high-impact confirmation request) | Art 32(2) is the only standing submission duty on an operator: results of implementation, not incidents |

Nearest provisions, for the crosswalk: Art 32(1)2 (monitor and respond to safety accidents), Art 32(2) (submit implementation results), Art 32(3) (MSIT notice on the submission, not deposited), Art 40(1)2 (MSIT may investigate on a third party's report or complaint).

Fork F4. Reading A (mine): the 32(2) "이행 결과" is the result of implementing items 1 and 2 (that the risk process and the monitoring system exist and operate); it is triggered by nothing that happens and is not an incident report. Reading B: an MSIT notice under 32(3) could require incident information inside the results submission. No such notice is in the bundle, so on the deposited text the answer is still "no duty".

## (3) What must I submit to MSIT under Art 32, and by when?

What: the results of implementing (이행 결과) Art 32(1) item 1 (identification, assessment and mitigation of risks across the AI lifecycle, act:334) and item 2 (a risk-management system that monitors and responds to AI-related safety accidents, act:335). To: the Minister of Science and ICT (act:336).
By when: **no period is stated** in the Act or the Decree. No frequency (once, yearly, on change) is stated either, and no form.
Art 32(3) (act:337): MSIT "must" fix by notice (고시) the specific implementation method and the matters needed for the submission. Not deposited.
What the Decree adds for Art 32: only Art 24 (the three criteria; the compute method is delegated to a notice). Nothing on content, timing or form of the submission.
Decree Art 25 is NOT about Art 32: it is the high-impact (Art 33) confirmation procedure. Its day counts (decree:318-322): MSIT replies within 30 days of the request, extendable once by up to 30 days with written reasons; an operator who objects may ask for re-confirmation within 10 days of receiving the reply; MSIT replies to that within 30 days. These are the only operator-facing day counts in the Decree.
Who submits for a foreign operator with a domestic representative: the representative acts for the 32(2) submission (act:355).

## (4) Domestic representative (Act Art 36, Decree Art 29)

Who must appoint: an AI business operator with NO address or business office in Korea (국내에 주소 또는 영업소가 없는, act:354) that meets ANY ONE (어느 하나, decree:352) of:

1. total revenue (매출액) in the previous year (previous business year for a corporation) of KRW 1 trillion (1조원) or more (decree:353);
2. revenue of the AI-service segment in the previous year of KRW 10 billion (100억원) or more (decree:354);
3. domestic users of its AI products and services, averaged per day over the 3 months immediately before the end of the previous year, of 1,000,000 (100만명) or more (decree:355);
4. it has been fined under Act Art 43(1)3 (failure to comply with an Art 40(3) order) (decree:356).

Revenue is converted to won at the previous year's average exchange rate (decree:357). All thresholds are 이상 (at or above).
An operator with a Korean address or office has no Art 36 duty, whatever its size.
What: designate IN WRITING (서면으로) a representative to act for (i) the Art 32(2) submission, (ii) an Art 33(1) high-impact confirmation request, (iii) support for implementing Art 34(1) measures, including checking the item-5 documents are current and accurate (act:355-357); AND report (신고) the designation to MSIT (act:354).
The representative must have an address or office in Korea (act:358). The representative's violations in those matters are deemed the operator's (act:359).
By when: **no period stated**.
Penalty: Art 43(1)2 (act:388): an administrative fine up to KRW 30 million for one who "violates Art 36(1) and does not designate" a representative. Annex 2 나 (annex2:37-39): KRW 20 million (2,000만원) for the 1st, 2nd and 3rd-or-later violation alike.
Not fined: failing to REPORT (신고) a designation that was made. Art 43(1)2 names only failing to designate.
Art 36(1) is not among Art 40(1)'s investigation triggers.

Fork F5. Whether a written designation that was never reported to MSIT is "지정하지 아니한 자". Reading A (mine, literal): no; designation and report are separate verbs, and only non-designation is fined. Reading B: an unreported designation is no designation as far as MSIT is concerned.

## (5) What can MSIT do to me, and the route from a failure to a fine

- Art 40(1) (act:377-379): when MSIT discovers or suspects a violation of Art 31(2), 31(3), 32(1), 32(2) or 34(1), or receives a report or complaint of one, it MAY require the operator to submit relevant materials, or have officials investigate.
- Art 40(2) (act:380): for that investigation, officials may enter the operator's offices and premises and examine books, documents and other materials; otherwise the Framework Act on Administrative Investigations applies.
- Art 40(3) (act:381): if the investigation finds the operator violated "this Act", MSIT MAY order the measures needed to stop or correct the violation.
- Art 43(1) (act:386-389): administrative fine (과태료) up to KRW 30 million (3천만원) on one who (1) fails to give the Art 31(1) prior notice; (2) violates Art 36(1) by not designating a domestic representative; (3) fails to comply with an Art 40(3) stop or correction order. Art 43(2): imposed and collected by MSIT, per the Decree.
- Art 42 (act:385), the only criminal penalty, reaches committee members who leak secrets (Art 7(9)); not an operator.

Three classes:

| Failure | Direct fine? | Investigation trigger (Art 40(1))? | Route to a fine |
| --- | --- | --- | --- |
| Art 31(1) prior notice | yes, 43(1)1 | no | direct |
| Art 36(1) designate a representative | yes, 43(1)2 | no | direct |
| Art 31(2), 31(3), 32(1), 32(2), 34(1) | no | yes | investigation, then a 40(3) order, then non-compliance, then 43(1)3 |
| Art 40(3) order not complied with | yes, 43(1)3 | (it is the order) | direct |

So for the Art 32 operator: failing to implement 32(1) or to submit under 32(2) carries no fine by itself; the fine comes only from not complying with an order made after an investigation.

Amounts, Annex 2 (unit 만원 = KRW 10,000; annex2:31-42), by count of the same violation:

| Violation | 1st | 2nd | 3rd or later |
| --- | --- | --- | --- |
| 가. Art 31(1) notice (43(1)1) | 500 (KRW 5,000,000) | 1,000 (KRW 10,000,000) | 1,500 (KRW 15,000,000) |
| 나. Art 36(1) representative (43(1)2) | 2,000 (KRW 20,000,000) | 2,000 | 2,000 |
| 다. Art 40(3) order (43(1)3) | 1,000 (KRW 10,000,000) | 2,000 (KRW 20,000,000) | 3,000 (KRW 30,000,000) |

Counting (annex2:3-10): the higher tier applies when the same violation was fined within the last 2 years, measured from the date of the earlier fine to the date the new violation was detected; the tier is the one after the highest earlier tier in that window.
Adjustments (annex2:11-29): the fining authority MAY reduce by up to one half (SME/venture/small business; minor carelessness; efforts to cure; other), not for one in arrears; MAY increase by up to one half (serious harm; violation lasting 6 months or more; other), never above the statutory ceiling of KRW 30 million.

Fork F6 (scope of an order). Art 40(3): "조사 결과 ... 이 법을 위반한 사실이 있다고 인정되면". Reading A (literal): an investigation opened on a listed trigger may end in an order about ANY violation of the Act it finds (e.g. Art 33(1) pre-review, Art 36(1)). Reading B: the order is confined to the Art 40(1) list.
Fork F7. An order is discretionary (명할 수 있다); so is investigating. No duty on MSIT to act.

## (6) Grace period

**None in the Act, the Decree or Annex 2.** Searched 유예, 계도 (0 hits in the text; the HTML hits are page-chrome 조문체계도), 경과 (only commencement, act:392, and the Decree's committee transitional provisions, decree:391-397), 기간.
No transitional provision for an operator's duties or fines appears in any addendum.
Commencement: Act No. 20676 addendum Art 1 (act:392): in force "공포 후 1년이 경과한 날" from promulgation on 2025-01-21, i.e. 2026-01-22; Act No. 21311's addendum (act:405) also commences on 2026-01-22. Exception: the digital-medical-device part of Art 2(4)라 from 2026-01-24. Decree: in force 2026-01-22 (decree:388), the Annex 1 digital-medical-device part from 2026-01-24.
Act No. 21311's deferred list (from six months after promulgation on 2026-01-20; act:405) touches none of Arts 2(7), 4, 31, 32, 36, 40, 43.
Edges: 2026-01-21 not in force; 2026-01-22 in force.

## (7) Who is an AI business operator, and foreign reach

Art 2(7) (act:24-26): one who carries on business related to the AI industry (Art 2(6): developing, manufacturing, producing or distributing AI products, or providing AI services) and is either (가) an AI development business operator: one who develops and provides AI; or (나) an AI utilisation business operator: one who provides AI products or services using AI provided by a (가) operator. It covers corporations, organisations, individuals and state bodies (국가기관등).
A mere user (이용자, Art 2(8): one who receives AI products or services) is not an operator.
Foreign reach: Art 4(1) (act:37): the Act applies to acts done abroad if they affect the domestic market or domestic users. Art 36 (a duty for operators with no Korean address or office) confirms foreign operators are addressed.

Forks:
- F8. A business that uses AI only internally and offers no AI product or service: Reading A (mine): not within (나), which requires providing AI products or services. Reading B: "인공지능산업과 관련된 사업" is wide enough. (Decree 23(4)2 exempts internal-use-only from transparency notices, which suggests the drafters thought internal users could be operators.)
- F9. Art 4(1) "영향을 미치는 경우" has no test: a fact the operator states.

## (8) What the Act and the Decree do NOT contain

- No duty on an operator to report an AI incident, accident, malfunction or harm, to anyone.
- No period, frequency or form for the Art 32(2) submission.
- No period for designating a domestic representative or reporting the designation.
- No fine for failing to report (신고) a designation; no direct fine for failures under Art 31(2), 31(3), 32(1), 32(2), 34(1).
- No designation or confirmation step for Art 32 systems, and no duty to notify MSIT that a system crosses the threshold.
- No compute-counting method (delegated to an undeposited notice).
- No grace period.
- No criminal penalty on an operator; no power to suspend, withdraw or ban an AI system; no power to publish an operator's name.
- No MSIT notice under Art 32(3) or Decree 24(2) in the bundle.

## (9) Added AFTER opening the baseline: Article 31(1) prior notice

The baseline exports a question on Art 31(1), which the eight questions above did not ask.
This section was written after reading the baseline's names and before reading `kr-ai-tests.l4` or `NOTES.md`, from the source alone; it is not "answers first" in the strict sense.

Art 31(1) (act:329): an operator who intends to provide a product or service using high-impact AI or generative AI must notify users IN ADVANCE that it is operated on that AI.
Decree 23(1) (decree:287-291) gives the methods (on the product, contract, manual or terms; on the user's screen or device; posted at the place of provision; another method MSIT accepts).
Decree 23(4) (decree:298-301): "제1항부터 제3항까지의 규정 중 전부 또는 일부를 적용하지 않을 수 있다" in three cases: (1) the use of high-impact or generative AI is obvious from the product or service name, the user screen, the product surface, or text marked on the output; (2) used only for the operator's internal business; (3) cases MSIT fixes by notice (none deposited).
Neither high-impact nor generative: no 31(1) duty.
Not giving the notice: direct fine, Art 43(1)1.

Fork F10. "적용하지 않을 수 있다" ("may not apply"): Reading A (taken for the tests): an exception the operator may rely on when the case is met. Reading B: a discretion (whose is not said) to disapply. The text names no one who exercises it.
Fork F11. Art 31(1) is not an Art 40(1) trigger, but 31(2) and 31(3) are; a 31(1) failure goes straight to a fine.
