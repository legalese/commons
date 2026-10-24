# Korea, AI Framework Act (Act No. 20676 of 2025, as amended) and its Enforcement Decree, row `solo-2026-10`

**Not for use as advice.**
This is a draft encoding.
No domain expert and no lawyer qualified in Korea has read it against the source.
Status `draft`; human gates HG1 and HG2 not sought.

인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 (약칭 인공지능기본법), "Framework Act on the Development of Artificial Intelligence and Establishment of Trust" (the brief's English; the Korea Legislation Research Institute's translation calls it "Framework Act on the Development of Artificial Intelligence and the Creation of a Foundation for Trust").
Encoded from the **Korean** text as consolidated on law.go.kr (the Ministry of Government Legislation's National Law Information Center), with its Enforcement Decree (시행령) and the Decree's Annex 2.
law.go.kr says of itself that its texts have no legal effect and that the Official Gazette (관보) does; **the Official Gazette was not consulted.**
An English translation of the Act (not of the Decree, whose English was not sought) was read beside the Korean for Articles 2(7), 4, 31(1), 32, 33, 36, 40 and 43; its licence is undetermined and it is not deposited.

**The answer to the brief's main question, as of 2026-10-24:** no provision of the Act or the Decree requires an AI business operator to report a serious AI incident, to anyone, within any period.
The nearest duty is Article 32: an operator whose AI system meets the Decree's three criteria (at least 10^26 floating-point operations of training compute, the most advanced technology, and a risk of broad and serious effect) must build a risk-management system that monitors and responds to AI safety incidents (32(1) item 2), and must submit the results of its Article 32(1) measures to the Minister of Science and ICT (32(2)), with no period stated.
The notice that Article 32(3) says the Minister "must" make on how to submit them is listed by law.go.kr as not made.
A draft notice with a seven-day incident-reporting clock is reported by secondary sources; it was **not fetched or read**, and nothing in this encoding rests on it (finding 3).

## Seat

The seat is **an AI business operator** (인공지능사업자, Act Article 2(7)): a corporation, association, individual or state body carrying on a business related to the AI industry that either develops and provides AI (인공지능개발사업자) or provides AI products or services using AI a developer provided (인공지능이용사업자).
A company or a small business owner.
Questions are phrased as that operator would ask them ("Does Article 32 apply to my AI system?", "Must I report a serious AI incident? To whom? By when?", "Must I designate a domestic representative?", "What can the Minister do to me, and what is the fine?"), with facts it can state.
The Minister of Science and ICT has no seat; Articles 40 and 43 and Annex 2 are encoded for what they mean to the operator.
Where the text hands a judgement to nobody in particular (Decree Article 24(1) items 2 and 3: "the most advanced technology", "broad and serious effect"), the operator is asked it as a fact (fork F4).
Where Annex 2 leaves a choice to the Minister (to increase or reduce a fine by up to one half), the answer gives the range, not a guess.

## What is encoded, and what is not

Encoded as rules (`kr-ai-operator.l4`), with the Korean quoted line by line above each rule:

- Act Article 2(7) (who is an AI business operator) and Article 4 with Decree Article 2 (reach abroad; the defence and security exclusion);
- Act Article 32 with Decree Article 24 (the safety obligation for high-performance AI: who is bound, the three criteria, the duties, the submission to the Minister, and its period, which is "nothing stated");
- the incident-reporting answer: no duty, no recipient, no period, and the nearest duty, by case;
- Act Article 36 with Decree Article 29 (the domestic representative: who must designate one, and the report to the Minister, period "nothing stated");
- Act Article 31(1) with Decree Article 23(4) items 1 and 2 (prior notice to users that a product or service runs on high-impact or generative AI, the one transparency duty the Act fines);
- Act Article 40(1) to (3) (which suspected breaches open a fact-finding investigation; corrective orders);
- Act Article 43 with Decree Article 32 and Annex 2 (the three finable failures, the fine by order of violation, the 1.5x increase capped at 30,000,000 won, the one-half reduction and its arrears exception), and that a failure under Article 32 is not itself finable;
- the grace-period question (none in the Act, the Decree or Annex 2);
- commencement (2026-01-22, both sides).

`kr-ai-baseline.l4` asks the seat's eleven questions with `@export` and `@desc`.
Everything else in the Act and the Decree is a row of the coverage table below, with a disposition and, where it touches a private actor, what it does to one.

**A deliberate scope cut against the Japan sibling.** `subjects/jp/ai-promotion-act-2025` carries an L4 provisions table with one row per article and computes its absence answers from that table.
This encoding has no such module: the coverage table here is in NOTES.md only, and the incident-reporting answer's "no duty" is a constant grounded in the reading and search recorded below ("What the Act and the Decree do not contain"), not computed from a table.
The reason is time (a two-hour brief); a provisions table is the first thing to add (see "Before this is worth relying on").

I read **every Article of the Act (1 to 43, with 17-2, 22-2 and 22-3) and all three addenda** in the deposited Korean.
In the Decree I read in full Articles 2, 23, 24, 25, 27, 29, 32 and 33, the addenda, and Annex 2; I read in context every line the mechanical search below hit (in Articles 3, 5, 7, 10, 13, 16-4, 18, 19 and 20); the other Decree articles were read by heading only, not line by line.
Annex 1 of the Decree (recognition of equivalent measures under Article 34(3)) and the request form were not deposited or read.

## Sources and edition

| id | what | status | where it came from |
| --- | --- | --- | --- |
| `kr-ai-act-ko` | the Act, law.go.kr consolidation [시행 2026. 7. 21.] [법률 제21311호, 2026. 1. 20., 일부개정], HTML and a rendering one paragraph per line | **authoritative** | law.go.kr `lsInfoR.do?lsiSeq=282791`, fetched 2026-10-24T01:33:01Z |
| `kr-ai-decree-ko` | the Enforcement Decree, consolidation [시행 2026. 8. 20.] [대통령령 제36580호, 2026. 8. 18., 타법개정] | **authoritative** | law.go.kr `lsInfoR.do?lsiSeq=288781`, fetched 2026-10-24T01:33:46Z |
| `kr-ai-decree-annex2-ko` | Decree Annex 2 (과태료의 부과기준), PDF and `pdftotext -layout` text | **authoritative** | law.go.kr `flDownload.do?flSeq=168105401`, fetched 2026-10-24T01:34:10Z |
| `law-go-kr-absence-evidence` | law.go.kr's delegated-rule popups for Act Art 32(3) and Decree Art 24(2), and an administrative-rule title search for 인공지능 | aid (evidence) | law.go.kr, fetched 2026-10-24T01:36:15Z and 01:43:11Z |
| (not deposited) | English translation by the Korea Legislation Research Institute, served by law.go.kr, headed "[Enforcement Date 22. Jan, 2026.] [Act No.21311, 20. Jan, 2026., Partial Amendment]" | aid, read only | `engLsInfoR.do?lsiSeq=282791&chrClsCd=010203`, fetched 2026-10-24; licence UNDETERMINED |

All deposited files are under `../../registers/source-bundle/`, with sha256 and provenance in the `.meta.json` files; `law-go-kr-render.py` made the two `.txt` renderings.

**Edition.**
The Act was promulgated as Act No. 20676 on 2025-01-21 and took effect on 2026-01-22 ("공포 후 1년이 경과한 날", addendum Art 1; Act No. 21311's addendum names the date, "2026년 1월 22일부터 시행한다", kr-ai-act-ko.txt:405).
Act No. 21311 (2026-01-20) amended it from the same day, except a list of provisions deferred to six months after promulgation (law.go.kr: 2026-07-21): Art 3(5), 6(2) items 7 and 8, part of 16(3)-(5), 17-2, 18, 22-3 and the second sentence of 35(1).
Act No. 21065 (2025-10-01) changed only a ministry's name in Art 38(1).
Of the provisions encoded, only Article 2 carries an amendment mark (<개정 2026. 1. 20.>, in force from 2026-01-22); Articles 4, 31, 32, 33, 34, 36, 40 and 43 carry none.
So for everything encoded the text has been one text since the Act took effect, and the encoding has one edition and a commencement date, not vintages.
The Decree (No. 36053, 2026-01-21) took effect on 2026-01-22 and was amended from 2026-07-21 (No. 36506) and 2026-08-20 (No. 36580); of the Decree provisions encoded only Article 2 (the defence and security list) carries amendment marks, and the encoding reads only its opening words.

**Where the text corrects or sharpens the brief.**

- Act No. 20676, promulgation in January 2025 and commencement on 22 January 2026: **verified** (kr-ai-act-ko.txt:391-392, 404-405). The current consolidation is Act No. 21311.
- The compute threshold of 10^26 floating-point operations: **verified, but it is one of three criteria that must all be met** (Decree Art 24(1), "모두 충족"): items 2 (the most advanced technology now used) and 3 (a risk of broad and serious effect on life, physical safety and fundamental rights) also apply. The threshold is in the Decree, not a notice; the counting method is delegated to a notice that is not made (Decree Art 24(2)).
- Article numbers 31, 32, 33-35, 36, 40 and 43: **verified**.
- The fine ceiling of 30,000,000 won: **verified** (Act Art 43(1)). It reaches three failures only: not giving the Article 31(1) prior notice, not designating a domestic representative under Article 36(1), and not carrying out a suspension or corrective order under Article 40(3). **Failing to submit the Article 32 results is not among them** (finding 4).
- Article 43(1) item 2 fines failing to **designate** a domestic representative, not failing to report the designation (fork F9).
- A grace period: **not in the Act, the Decree or Annex 2** (finding 6).
- A final notice with a seven-day incident-reporting clock: **not found** (finding 3).

## Method

The solo `encoding-a-subject` workflow, from a pinned brief, target compiler `main`.
Sources fetched from law.go.kr with the fetcher User-Agent (robots.txt allows all), deposited, rendered one paragraph per line.
Nouns first (`kr-ai-domain.l4`), then the operator's rules (`kr-ai-operator.l4`), then the seat questions (`kr-ai-baseline.l4`), then tests written by hand from the source (`kr-ai-tests.l4`).
Every quotation was generated with the skill's `srcrefs.py quoteid`, through a small script that substitutes quote markers in a template, never retyped, and checked with `srcrefs.py check --strict` (output below).
Identifiers are English; the Korean behind each rule is quoted above it.
The English translation of the Act was compared with the Korean for Articles 2(7), 4, 31(1), 32, 33, 36, 40 and 43 only, and no difference of meaning was noticed there beyond wording (it calls 국내대리인 a "domestic agent", and once, in Art 40(3), calls the operator an "artificial intelligence business entity"); the Decree's English was not sought.
The English renderings in identifiers and `@desc` are the encoder's own, not the translation's; Article 36's 국내대리인 is "domestic representative" here and "domestic agent" in the Korea Legislation Research Institute's English.

## Coverage table: the Act

"rule" = an operative rule in `kr-ai-operator.l4`; "row" = recorded here with what it does to a private actor.

| provision | heading (Korean) | disposition | what it means for an AI business operator |
| --- | --- | --- | --- |
| Art 1 | 목적 | inert | none |
| Art 2(1)-(3), (6), (8)-(12) | 정의 | inert, except as read by the rules | definitions the encoded rules read only through the facts asked |
| Art 2(4) | 정의: 고영향 인공지능 | asked as a fact (Art 31(1) question) | whether a product uses high-impact AI is asked, not computed from the list in items 가-카 (deferred: the list as a rule); the digital-medical-device part of item 라 took effect on 2026-01-24, not 2026-01-22 (Act No. 20676 addendum Art 1 proviso) |
| Art 2(5) | 정의: 생성형 인공지능 | asked as a fact | as above |
| Art 2(7) | 정의: 인공지능사업자 | **rule** | who is an operator |
| Art 3 | 기본원칙 및 국가 등의 책무 | inert | principles; 3(2) is an entitlement of affected persons, with no duty stated on the operator |
| Art 4 | 적용범위 | **rule** (with Decree Art 2) | reach abroad; defence and security exclusion (fork F7) |
| Art 5 | 다른 법률과의 관계 | inert | other laws with special provisions prevail; not encoded (fork F10) |
| Arts 6-7 | 기본계획; 국가인공지능전략위원회 | out-of-scope (machinery) | none, except Art 7(9), a secrecy duty on committee members, enforced by Art 42; not the operator's |
| Art 8 | 위원회의 기능 | row | 8(2): the Committee may make recommendations or express opinions to AI business operators on correct use, ethics, safety and trustworthiness; no duty to follow is stated (8(3) binds only state bodies) |
| Arts 9-11 | 제척ㆍ기피; 분과위원회; 인공지능정책센터 | out-of-scope (machinery) | 9(2): a party to an agenda item may apply to disqualify a member; none otherwise |
| Art 12 | 인공지능안전연구소 | row | the AI Safety Institute may support Art 32 safety (12(2) item 6); no duty on the operator |
| Arts 13, 15-21, 22, 22-3, 23-25 | promotion and support | out-of-scope (machinery) | support the government may give; no duty on the operator |
| Art 14 | 인공지능기술의 표준화 | row | 14(2): the government may publish standards and recommend that businesses comply; no duty stated |
| Art 22-2 | 인공지능연구소의 설립 및 지원 등 | out-of-scope (another private actor) | a university or company that sets up an AI research institute needs the Minister's permission, and the Minister may order correction or cancel it (22-2(10)); a consequence for a private actor, but not one this seat's questions reach |
| Art 26 | 한국인공지능진흥협회의 설립 | out-of-scope (machinery) | none |
| Art 27 | 인공지능 윤리원칙 등 | row | ethics principles the government may publish; no duty on the operator |
| Art 28 | 민간자율인공지능윤리위원회 | row | an operator **may** set up a private ethics committee, which "autonomously" investigates safety and rights infringements internally; no reporting duty |
| Art 29 | 신뢰 기반 조성을 위한 시책 | row | government support for operators' self-regulatory codes; no duty |
| Art 30 | 검ㆍ인증등 지원 | row | 30(3): an operator providing high-impact AI is to **endeavour** (노력하여야 한다) to obtain verification or certification in advance; no consequence stated |
| Art 31(1) | 인공지능 투명성 확보 의무 | **rule** (with Decree Art 23(4) items 1, 2) | prior notice to users; finable (Art 43(1) item 1) |
| Art 31(2), (3) | same | row | marking generative output; notice or marking of realistic synthetic output; not encoded as rules (not a notification to an authority, and not finable); a suspected breach opens an Art 40 investigation (rule) |
| Art 31(4) | same | row | delegation to the Decree (Decree Art 23) |
| Art 32(1), (2) | 인공지능 안전성 확보 의무 | **rule** (with Decree Art 24) | the safety obligation and the submission of results; period not stated |
| Art 32(3) | same | **rule** (as the reason the period is NOTHING) | the Minister "must" notify the method and the submission details; law.go.kr lists no such notice (finding 2) |
| Art 33 | 고영향 인공지능의 확인 | row | the operator must review in advance whether its AI is high-impact, and **may** ask the Minister to confirm; Decree Art 25 sets the Minister's 30-day reply (extendable once by 30 days) and the operator's **10-day** window to ask for re-confirmation. Not encoded: it is a request procedure, not a reporting duty (deferred) |
| Art 34 | 고영향 인공지능과 관련한 사업자의 책무 | row | measures for high-impact AI (risk management, explanation, user protection, human oversight, documents); Decree Art 27(1) requires posting their main contents and 27(2) keeping evidence for **5 years**; no reporting to an authority; a suspected breach of 34(1) opens an Art 40 investigation (rule) |
| Art 35 | 고영향 인공지능 영향평가 | row | an operator is to **endeavour** to assess the impact on fundamental rights in advance; no consequence stated (second sentence in force from 2026-07-21) |
| Art 36 | 국내대리인 지정 | **rule** (with Decree Art 29) | designation in writing and report to the Minister; period not stated; 36(3): the representative's breach is deemed the operator's (row) |
| Arts 37-39 | 재원; 실태조사; 권한의 위임 | out-of-scope (machinery) | 38(2) asks public bodies, not operators, for materials |
| Art 40 | 사실조사 등 | **rule** | which suspected breaches open an investigation; on-site entry; corrective orders |
| Art 41 | 벌칙 적용에서 공무원 의제 | out-of-scope (machinery) | none |
| Art 42 | 벌칙 | row | criminal penalty for a committee member's breach of secrecy (Art 7(9)); not an operator's |
| Art 43 | 과태료 | **rule** (with Decree Art 32 and Annex 2) | the three finable failures and the ceiling |
| Addendum, Act No. 20676 | 부칙 | **rule** (commencement) | Art 1: in force one year after promulgation; Arts 2-3 machinery |
| Addendum, Act No. 21065 | 부칙 (정부조직법) | out-of-scope (amends a name) | none |
| Addendum, Act No. 21311 | 부칙 | **rule** (commencement) | in force 2026-01-22, listed provisions from six months after promulgation |

No row is `deferred` except the three marked so (Art 2(4)'s list as a rule; Art 33 with Decree Art 25's clocks; and the provisions table as an L4 module).

## Coverage table: the Decree and Annex 2

| provision | heading | disposition | note |
| --- | --- | --- | --- |
| Art 1, 1-2 | 목적; 인공지능취약계층의 범위 | inert | none |
| Art 2 | 법의 적용 제외 인공지능 | **asked as a fact** (Art 4 rule) | the list of defence and security tasks is put to the operator in one question, not encoded item by item |
| Arts 3-22 | committee, centres, support, research institutes, clusters, association, ethics, certification | out-of-scope (machinery) | read by heading and by the search below; Art 7 and Art 18 carry reporting duties of state bodies and of the designated cluster agency (which may be a private body), not of AI business operators as such |
| Art 23(1)-(3) | 인공지능 투명성 확보 의무 | row | the methods of notice and marking |
| Art 23(4) | same | **rule** (items 1, 2) | exceptions; item 3 (cases the Minister notifies) not encoded: law.go.kr lists no notice under Art 23 (fork F8) |
| Art 24 | 인공지능 안전성 확보 의무 | **rule** | the three criteria; 24(2) counting method delegated to a notice not made (fork F3) |
| Arts 25-26 | 고영향 인공지능의 확인 절차; 전문위원회 | row | the confirmation clocks (Coverage table: the Act, Art 33) |
| Art 27 | 고영향 인공지능과 관련한 사업자의 책무 | row | posting and 5-year retention (Art 34 row) |
| Art 28 | 고영향 인공지능 영향평가 | row | contents of the impact assessment |
| Art 29 | 국내대리인 지정 사업자의 기준 | **rule** | the four criteria and the exchange-rate rule |
| Arts 30-31 | 실태조사; 업무의 위탁 | out-of-scope (machinery) | none |
| Art 32 | 과태료의 부과기준 | **rule** | points to Annex 2 |
| Art 33 | 규제의 재검토 | row | the Minister reviews the Art 18, Art 24 and Art 29 criteria every three years from 2026-01-01 |
| Addenda | 부칙 | **rule** (commencement, Decree No. 36053 Art 1) | in force 2026-01-22 |
| Annex 1 | 이행조치 인정 기준 및 절차 | not deposited, not read | equivalence of measures under other laws (Act Art 34(3)) |
| Annex 2 | 과태료의 부과기준 | **rule** | general criteria 가-라; individual criteria 가-다 |

## What the Act and the Decree do not contain

Searched by reading (the Act whole; the Decree as stated above) and by a mechanical search of the three deposited texts on 2026-10-24.
Counts are of lines in `kr-ai-act-ko.txt` (405 lines), `kr-ai-decree-ko.txt` (406) and `kr-ai-decree-annex2-ko.txt` (44).

| searched for | Korean searched | Act | Decree | Annex 2 |
| --- | --- | --- | --- | --- |
| an incident or accident | 사고 | 1 (line 335: Art 32(1) item 2, the risk-management system) | 0 | 0 |
| a report to an authority | 보고 | 0 | 3 (lines 85, 86: Art 7, state bodies report to the Committee; 230: Art 18, a cluster agency reports its plan) | 0 |
| a filing | 신고 | 2 (354: Art 36(1), reporting the domestic representative; 379: Art 40(1) item 2, a report of a breach received by the Minister) | 0 | 0 |
| a notification | 통보, 통지 | 0, 0 | 1, 0 (47: Art 3, the Minister notifies agencies of the Basic Plan) | 0 |
| a submission | 제출 | 6 (55, 366: public bodies; 336, 337, 355: Art 32(2), (3) and Art 36(1) item 1, the safety results; 377: Art 40(1), materials on investigation) | 9 (none an incident report: Arts 5, 10, 13, 19, 20, 25) | 0 |
| a period | 이내, 기한, 지체 없이, 즉시 | 2, 0, 0, 0 (60: committee size; 256: a research institute's six months) | 5, 0, 0, 0 (85: Art 7's three months, state bodies; 206: Art 16-4, the number of founding members; 318, 319, 322: Art 25's 30 days and 10 days, high-impact confirmation) | 0 |
| a grace period | 유예, 계도 | 0, 0 | 0, 0 | 0, 0 |

**Not found, in the Act or the Decree as deposited:** any duty on an AI business operator to report an AI incident or accident to any authority; any period for doing so; any period for submitting the Article 32 results; any period for designating or reporting a domestic representative; any grace period or suspension of investigations or fines.
These statements are about this Act and this Decree only.
Other Korean laws (for example sectoral or personal-information laws), MSIT notices other than those searched for, guidelines, and the financial-sector AI guidelines the Arcadia paper mentions were not read.

## Findings

1. **No incident-reporting duty.**
   사고 occurs once in the Act, in Article 32(1) item 2, where the duty is to build "a risk-management system that monitors and responds to AI-related safety incidents" (인공지능 관련 안전사고를 모니터링하고 대응하는 위험관리체계 구축).
   Article 32(2) requires submitting "the results of implementing" (이행 결과) the Article 32(1) measures to the Minister.
   Neither is a duty to report an incident; the encoding does not infer one (fork F1).
   Asserted (tests section 5).
2. **Article 32(3)'s notice is listed as not made, and so is Decree Article 24(2)'s.**
   Article 32(3) says the Minister "must" (고시하여야 한다) notify the specific implementation methods and what is needed to submit the results.
   On 2026-10-24 law.go.kr marked the delegation link in both Act Art 32(3) and Decree Art 24(2) as having no linked administrative rule, and its popup reads "훈령·예규·고시 등의 행정규칙이 제정되지 아니하였거나 내부공문 및 업무지침 등의 형식으로 운용 중입니다" (deposited).
   A title search of current and scheduled administrative rules for 인공지능 returned 27 rules, none of them on AI safety or on the Article 32 results; searches for "인공지능 안전성" and "인공지능 발전과 신뢰" returned none.
   So the submission duty exists in the Act with no method and no period, and this encoding answers the period with NOTHING.
   law.go.kr's own wording allows that rules may be operated as internal guidance, so this is evidence of absence, not proof.
3. **The seven-day clock is in a draft, and the draft was not read.**
   The brief's secondary sources (a Mondaq / Baker Botts piece; the Arcadia paper, arXiv 2608.19278) report a draft Safety Assurance Notice with a seven-day serious-incident report, and a draft notification under consultation.
   **Secondary source, not checked:** neither the draft nor any MSIT consultation page was fetched (time), so this encoding does not deposit, quote or encode it.
   If a final notice is made under Article 32(3) with a reporting clock, it would be law (a 고시 under the Act), and the reporting answer would change.
4. **Failing to submit the Article 32 results, or to carry out Article 32(1), is not itself finable.**
   Article 43(1) lists only Article 31(1), Article 36(1) and Article 40(3).
   The route is: a suspected or reported breach of 32(1) or 32(2) opens an investigation (Art 40(1)); the Minister may order the breach stopped or corrected (40(3)); not carrying out the order is fined under 43(1) item 3 (Annex 2: 10, 20, 30 million won by order).
   Asserted (tests sections 8-10).
5. **Article 40(1)'s list leaves out Articles 31(1) and 36(1), the two other finable duties.**
   An investigation under Article 40 is opened only by suspected or reported breaches of 31(2), 31(3), 32(1), 32(2) and 34(1).
   So a suspected breach of 31(1) or 36(1), both finable directly, cannot by itself open an Article 40 investigation, while a suspected breach of 31(2), 31(3) or 34(1), none finable directly, can.
   This is about what **opens** an investigation only: once one is open, Article 40(3) lets the Minister order the stopping or correction of any breach of "이 법" (this Act) the investigation finds (kr-ai-act-ko.txt:381), so a 31(1) or 36(1) breach found in an investigation opened on a listed ground can be the subject of an order (fork F13).
   Asserted for the opening list (tests section 8); no exported question asks about the scope of an order.
6. **No grace period in law.**
   유예 and 계도 do not occur in the Act, the Decree or Annex 2, and the addenda fix commencement only.
   A one-year moratorium on fact-finding investigations and fines is reported by secondary sources as a government plan; **secondary source, not checked**: no MSIT announcement was fetched.
   If it exists, it is policy, not law, and the encoding keeps it out.
7. **Article 32 binds every AI business operator, not only developers.**
   The addressee is 인공지능사업자, which Article 2(7) defines to include a utilization operator (이용사업자) that provides products or services on another developer's AI (fork F5).
8. **The domestic-representative duty states no period, and its fine tops out at the ceiling.**
   Neither Article 36 nor Decree Article 29 states when the designation must be made or reported.
   Annex 2 sets 20,000,000 won for every order of the violation; increased by one half it reaches 30,000,000 won, exactly Article 43(1)'s ceiling.
   Decree Article 29(1) item 4 makes any operator once fined under 43(1) item 3 a criterion case, whatever its size.
9. **The law.go.kr consolidation is Act No. 21311, not Act No. 20676.**
   The brief's Act No. 20676 is the Act as enacted; it was amended twice before or on commencement, and the provisions encoded were unchanged by either amendment except Article 2's definitions (in force from the same day).

## Fork register

| fork | where | readings | taken | the text that licenses each |
| --- | --- | --- | --- | --- |
| F1 | Art 32(1) item 2, 32(2) | (a) a "risk-management system that monitors and responds to incidents" plus "submit the results" implies reporting incidents; (b) it is a duty to build a system and to submit results of implementation, not to report incidents | (b): the text says 구축 (build) and 이행 결과 (results of implementation); nothing names an incident report, a recipient or a period | kr-ai-act-ko.txt:335-336 |
| F2 | Art 32(2), (3): the period | (a) no period until the Minister notifies one; (b) "without delay" or a period borrowed from a draft | (a): NOTHING; the notice is listed as not made (finding 2) | kr-ai-act-ko.txt:336-337; law-go-kr-delegated-rule-act-art32.html |
| F3 | Decree Art 24(1) item 1: counting compute | (a) the operator's own count until the Minister notifies a method; (b) the criterion cannot be applied until then | (a), stated in the `@desc`; on (b) no system would be bound at all, which the text does not say | kr-ai-decree-ko.txt:303, 306 |
| F4 | Decree Art 24(1) items 2, 3 | (a) facts the operator states in good faith; (b) a determination someone else makes | (a), asked as facts; the text names no one to decide | kr-ai-decree-ko.txt:304-305 |
| F5 | Art 32(1): who is bound | (a) every AI business operator, including a utilization operator; (b) only the developer who trained the system | (a), the text's word; (b) is how the duties would make most practical sense, and is a question for an expert. Support for (a), found by the independent test pass: Decree Art 27(3) relieves a utilization operator of Art 34(1) items 1-3 where its developer carried them out and it made no major change of function, which presupposes that duties addressed to 인공지능사업자 reach utilization operators; the Decree gives no such relief for Art 32 | kr-ai-act-ko.txt:24-26, 333; kr-ai-decree-ko.txt:339 |
| F6 | Annex 2 general criterion 나: order | (a) next after the highest order fined for the same violation within two years; (b) count of fines within two years plus one | (a), as the text says; the operator states the highest earlier order | kr-ai-decree-annex2-ko.txt:8-10 |
| F7 | Art 4(1): conduct in Korea | (a) the Act reaches conduct in Korea, and 4(1) extends it abroad; (b) only conduct affecting the Korean market or users, wherever it happens | (a): 4(1) says "even if" (라도) the conduct is abroad, which presupposes domestic conduct is covered | kr-ai-act-ko.txt:37 |
| F8 | Decree Art 23(4): "may not apply" (적용하지 않을 수 있다) | (a) exceptions the operator may rely on; (b) a discretion of the Minister | (a); item 3 is the only one the Minister fixes, and no notice under it is listed | kr-ai-decree-ko.txt:298-301 |
| F9 | Art 43(1) item 2 | (a) fines only not designating; (b) also not reporting the designation | (a): the item says 지정하지 아니한 자; Annex 2 item 나 says the same | kr-ai-act-ko.txt:388; kr-ai-decree-annex2-ko.txt:39-41 |
| F10 | Art 5(1) | another law's special provision on AI prevails | not encoded: no other law was read; every answer is "under this Act" | kr-ai-act-ko.txt:39 |
| F11 | Annex 2 increase and reduction | (a) the range is base x 0.5 to min(base x 1.5, 30,000,000); (b) both may apply together | (a); the text gives each as a separate discretion; the answer gives the range and leaves the grounds to the Minister | kr-ai-decree-annex2-ko.txt:11-25 |
| F12 | Act Art 32(1) and Decree Art 24(1): the delegation | (a) the Decree as written: all three criteria; (b) Act Art 32(1) delegates only "a standard of cumulative training compute" (누적 연산량이 대통령령으로 정하는 기준), so Decree items 2 and 3, which are not about compute, go beyond the delegation and compute alone decides | (a), the Decree's text; whether items 2 and 3 are within the delegation is for a lawyer to decide. On (b) every system at or above 10^26 would be bound, and the tests on items 2 and 3 would turn over. Raised by the independent test pass | kr-ai-act-ko.txt:333; kr-ai-decree-ko.txt:302-305 |
| F13 | Act Art 40(3): the scope of an order | (a) an investigation opened on a listed ground may end in an order about any breach of "this Act" it finds, including 31(1), 33(1) or 36(1); (b) an order is confined to the breaches Art 40(1) lists | (a), the text's words "이 법을 위반한 사실"; the operator module's comment takes it; finding 5 is worded to fit. No exported question asks it. Raised by the independent test pass | kr-ai-act-ko.txt:377-381 |

## Answer table: the reporting clocks

| question | answer | provision |
| --- | --- | --- |
| Must I report a serious AI incident? | **No duty is stated** in the Act or the Decree (as of 2026-10-24) | none; finding 1 |
| To whom? Within how many days? | No recipient; no period (NOTHING) | none |
| What is the nearest duty? | If Art 32 binds my system: build a risk-management system that monitors and responds to safety incidents, and submit the results of the Art 32(1) measures to the Minister of Science and ICT | Art 32(1) item 2, 32(2) |
| By when must I submit the Art 32 results? | **No period stated**; the Art 32(3) notice that would fix it is listed as not made | Art 32(2), (3); finding 2 |
| Does a draft notice set seven days? | Reported by secondary sources; **not read, not encoded** | finding 3 |
| Must I designate a domestic representative, and report it? By when? | Yes, if I have no address or office in Korea and meet a Decree Art 29(1) criterion; **no period stated** | Art 36(1); Decree Art 29 |
| By when must I ask the Minister to re-confirm a high-impact finding? | Within 10 days of the reply (Decree Art 25(4)); **not encoded** (deferred) | Decree Art 25 |
| What if I fail? | Art 32: no direct fine; via an Art 40(3) order, 10 / 20 / 30 million won by order. Art 36(1): 20 million won. Art 31(1): 5 / 10 / 15 million won. Each may be increased by up to one half to at most 30 million won, or reduced by up to one half | Art 43; Annex 2 |
| Is there a grace period? | **None in law**; a reported moratorium is policy, not checked | finding 6 |
| From when? | 2026-01-22 | Act No. 21311 addendum; Decree No. 36053 addendum Art 1 |

## Checks

Target compiler: `main`.
The `l4` used for every run: `L4=/Users/mengwong/.cache/l4-main/99/l4`, whose `--version` prints `1.6.99 (main, 6cc2c91, 2026-10-21)`; `JL4_LIBRARY_PATH` unset.
`check.sh` compared it with the main build `fetch-main-l4.sh` supplied, the same build.

```
$ L4=/Users/mengwong/.cache/l4-main/99/l4 ./check.sh
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.99 (main, 6cc2c91, 2026-10-21)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
kr-ai-baseline.l4                              0         0       0        0         0 |      0         0       0        0  same
kr-ai-domain.l4                                0         0       0        0         0 |      0         0       0        0  same
kr-ai-operator.l4                              0         0       0        0         0 |      0         0       0        0  same
kr-ai-tests.l4                                 0       109       0        0         0 |      0       109       0        0  same
tests-independent.l4                           0       117       0        0         0 |      0       117       0        0  same
TOTAL (5 modules)                              0       226       0        0           |      0       226       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

```
$ python3 -I srcrefs.py check --strict ../../registers/source-bundle/kr-ai-act-ko.txt *.l4
srcrefs check: 96 src: lines, 17 runs, 24 locators, 0 problems
```

`check.sh` exit status 0 and `srcrefs.py` exit status 0, run 2026-10-24 at about 09:58 SGT.
No warnings: `l4 check` on every module printed no `Warning`.
(`srcrefs.py` is the encoding-a-subject skill's copy, from `legalese/l4-ide` at `a27a409a4`.)

**A main-build trap met here:** the prelude's `EXPONENT 10 26` evaluates in floating point on `main` to 100000000000000004764729344, so a threshold written that way would have answered "not bound" at exactly 10^26.
The threshold is a literal (`kr-ai-operator.l4`), and the tests take 10^26 - 1, 10^26 and 2 x 10^26 as literals.

**Negative controls**, run on copies in scratch and discarded: moving the threshold literal to 10^26 + 1 failed 8 assertions in `kr-ai-tests.l4`; to 10^26 - 1 failed 5; replacing Article 36's "no address or office in Korea" condition with TRUE failed 2.

What the checks do not show: that a quotation is the right one for its rule (a person holding the text checks that); that the English names mean what the Korean says; that the encoding means what the text says.
Tests written by the model that wrote the encoding show consistency, not faithfulness.

## Tests

`kr-ai-tests.l4`, 109 assertions, expected values written by hand from the deposited Korean:

1. Art 2(7): developer and utilization operator are operators; outside the AI industry, or neither kind, are not;
2. Art 4: in Korea; abroad affecting Korea; abroad not affecting Korea; defence-only;
3. Decree Art 24(1): 10^26 - 1, 10^26, 2 x 10^26; and each qualitative criterion false;
4. Art 32: every field of the answer, both sides of the threshold, a foreign developer serving Korea and one not, a defence-only developer, and a utilization operator (fork F5);
5. the incident-reporting answer: no duty, no recipient, no period, and each of the three nearest-duty answers;
6. Decree Art 29(1): each of the four criteria on both sides; Art 36(1) for a foreign developer serving Korea, one below every criterion, a Korean developer meeting all criteria, and a foreign developer not serving Korea;
7. Art 31(1) with Decree Art 23(4): generative, high-impact, neither, obvious, internal-only, and out of reach;
8. Art 40(1): all eight duty provisions;
9. Annex 2: the order for earlier orders 0, 1, 2, 3 and 5; each failure at each order; the 1.5x increase, including where it meets the ceiling (item 2) and where the ceiling caps it (item 3, third order: 30,000,000, not 45,000,000); the reduction, and no reduction in arrears;
10. Art 32 not finable directly; no grace period;
11. commencement on 2026-01-21, 2026-01-22 and 2026-10-24;
12. every baseline question called with plain inputs.

`tests-independent.l4`, 117 assertions, by a separate session (next section).

## Independent test pass

**Method.**
A separate model agent, which had not seen this encoding being built, read the deposited Korean sources (`kr-ai-act-ko.txt`, `kr-ai-decree-ko.txt`, `kr-ai-decree-annex2-ko.txt` and the `.meta.json` files) and wrote its answers to the seat's questions in `tests-independent-answers-first.md` before, by its own account, opening anything in this folder.
Its section 9, on Article 31(1), was written after it opened the baseline to learn the names, and says so.
It then read the baseline for names and inputs and wrote `tests-independent.l4`.
It did not read the English translation.
This encoding did not edit either file; they are as their author left them (commit `4ea061bd7`).

**Result.**
`tests-independent.l4`: 117 assertions, 0 errors, **117 satisfied**, 0 failed, 0 refused, with the same counts on the main build; all five modules together, 226 satisfied (output under Checks).
No answer the baseline exports disagrees with the answers decided from the source.
The author was a model agent, not a person qualified in Korean law, so agreement shows two readings of the same text are consistent, not that either is faithful.

**What it raised that no assertion could test,** and what changed:

- the delegation question (now fork F12);
- the scope of an Article 40(3) order, and finding 5's wording, which overstated what the Act's fact-finding power cannot reach (now fork F13; finding 5 reworded);
- support for fork F5 from Decree Art 27(3) (added to F5);
- Decree Article 5(1) lets the National AI Strategy Committee request materials or opinions from corporations and associations (kr-ai-decree-ko.txt:74), and an operator may be one; no duty to comply is stated, so the "no reporting duty" answer stands.

**Negative controls,** run by the tester on scratch copies of `kr-ai-operator.l4` and discarded: the threshold literal moved to 10^26 + 1 failed 10 of its assertions; Annex 2 item 1's first-order amount changed from 5,000,000 to 50,000,000 failed 5; Article 36's no-office condition replaced by TRUE failed 2; 32(2) dropped from Article 40(1)'s list failed 1.

## Not exposed by the baseline

The tester listed these as untestable through the exported questions; each is true of the text and not asked:

- the Article 32, 36 and 31(1) questions, and the incident question, take no date, so they give the same answer for a day before 2026-01-22, when no duty under them was yet in force; only the commencement question takes a date;
- that failing to **report** (신고) a domestic representative's designation is not itself fined: Article 43(1) item 2 fines only failing to designate one (kr-ai-act-ko.txt:388; fork F9);
- Article 36(3): a domestic representative's breach in the matters it acts for is deemed the operator's (kr-ai-act-ko.txt:359);
- Decree Article 25's clocks: the Minister replies within 30 days, extendable once by 30, and the operator may ask for re-confirmation within 10 days of the reply (kr-ai-decree-ko.txt:318-322);
- the 2026-01-24 start of the digital-medical-device part of Article 2(4)(라) (kr-ai-act-ko.txt:392);
- Decree Article 5(1)'s power to request materials (kr-ai-decree-ko.txt:74).

## Open questions for a domain expert

- Does Article 32 bind a utilization operator that deploys another developer's frontier model, or only the developer (F5)?
- Are Decree Article 24(1) items 2 and 3 within the Act's delegation of a compute standard (F12)?
- May an Article 40(3) order reach a breach that could not itself have opened the investigation (F13)?
- Until the Minister notifies a counting method under Decree Article 24(2), can the 10^26 criterion be applied at all (F3)?
- Is there an MSIT notice under Article 32(3), final or draft, that law.go.kr does not list, and does it set an incident-reporting clock (finding 3)?
- Is the reported one-year moratorium on investigations and fines a formal act (a 고시, a 훈령) or a policy statement (finding 6)?
- Does Decree Article 23(4)'s "may not apply" create an exemption the operator may rely on (F8)?
- Does Article 5(1) let a sectoral law (for example the financial-sector AI guidelines' incident reporting, which the Arcadia paper mentions as voluntary) displace or add to these answers (F10)?

## Before this is worth relying on

- An independent test pass has been done (above), but by a model agent reading the same deposited text; it is not a review.
- A reader qualified in Korean law checks the rules against the Korean, especially forks F1, F3, F5 and F8, and confirms the coverage table's "no duty" rows.
- The Official Gazette text of Act No. 21311 and of the Decree is compared with the law.go.kr consolidation.
- MSIT's notices under Act Art 32(3) and Decree Art 24(2), if any are made, and any draft under consultation, are fetched and deposited (a draft as `aid`, labelled "draft notice, not law").
- An L4 provisions table with one row per article, as the Japan sibling has, so that the absence answers are computed rather than stated.
- Decree Article 25's confirmation clocks (30 days, extendable once by 30; 10 days to ask for re-confirmation) are encoded, with a ruling on how the days are counted.
