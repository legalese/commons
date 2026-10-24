# UK Network and Information Systems Regulations 2018: answers decided from the source alone

Independent test author, 2026-10-24.
Written BEFORE opening anything else under `encodings/solo-2026-10/` and before reading the subject's NOTES.md.
Not for use as advice.

Sources read, whole: `registers/source-bundle/uksi-2018-506.txt` (972 lines) and `eur-2018-151.txt` (17 lines), with both `.meta.json` files.
Both are role `aid`: Lex (i.AI) re-serves of legislation.gov.uk revised text (Lex valid date 2026-09-30); the official register refused this session's encoder with a WAF challenge.
So every answer below is an answer **on the deposited text**, not on the official text.
Pins are `reg N(p)` with the deposited file's line number (`txt:L`).

Seat: a company that provides an AI model as a service (an API, or a chat product) and asks what the Regulations require of it.

## (1) Do the Regulations apply to me: OES, RDSP, or neither?

**OES: no, on any input an AI model provider could state.**
An OES is a person deemed designated under reg 8(1) or (2A) or designated under reg 8(3) (reg 1(2) "OES", txt:105).
Reg 8(1) needs "an essential service of a kind referred to in ... Schedule 2" plus a threshold (txt:231-233); reg 8(3) also needs "an essential service of a kind specified in ... Schedule 2" (txt:238); reg 8(2A) is integrated care boards only (txt:236).
Schedule 2 paragraphs 1-10 list only electricity, oil, gas, air, water and rail and road transport, healthcare, drinking water, and digital infrastructure; digital infrastructure is TLD name registries, DNS resolvers, DNS authoritative hosting and IXPs (txt:958-973).
Supplying an AI model is none of these. An AI provider that ALSO runs, say, a DNS resolver over the 500,000-IP threshold would be an OES for that service only, never for the model.

**RDSP: yes, if and only if all of these hold** (reg 1(3)(e), txt:117-119):
- (a) it "provides a digital service in the United Kingdom"; "digital service" is an Information Society service "of any the following kinds— online marketplace; online search engine; cloud computing service" (reg 1(2), txt:94);
- (b) "the head office for that provider is in the United Kingdom or that provider has nominated a representative who is established in the United Kingdom" (txt:118);
- (c) it "is not a micro or small enterprise as defined in Commission Recommendation 2003/361/EC" (txt:119; the Recommendation is not deposited, so its thresholds cannot be checked here).

Fork F-A (the decisive input): is an AI model service a "cloud computing service", "a digital service that enables access to a scalable and elastic pool of shareable computing resources" (txt:89)?
- Reading 1: a model API sells access to inference capacity on shared, elastic compute, so yes.
- Reading 2: the customer gets model outputs, not access to computing resources, so no.
The text does not decide it; I take it as an input. A chat product that searches "in principle, all websites ... and returns links" could alternatively be an "online search engine" (txt:107); also an input.
Not-a-digital-service → neither route: no NIS duty at all.

**Neither:** not a Schedule 2 operator AND (not a digital service of the three kinds, OR small/micro, OR head office outside the UK with no UK representative; see (6)).

## (2) Must I notify an incident, and to whom?

RDSP: **yes, the Information Commission, in writing**, about "any incident having a substantial impact on the provision of any of the digital services mentioned in paragraph (1) that it provides" (reg 12(3), txt:332).
- "incident" = "any event having an actual adverse effect on the security of network and information systems" (reg 1(2), txt:103). A model misbehaving with no effect on availability, authenticity, integrity or confidentiality (reg 1(3)(g), txt:121) is not an incident.
- The paragraph (1) services are those provided "within the United Kingdom" (txt:319).
- Gate, reg 12(4) (txt:333): "applies only if the RDSP has access to information which enables it to assess whether the impact of an incident is substantial." No access → no duty.
- Substantiality: no number in the text. Reg 12(7) lists five parameters (users affected, duration, geographical area, extent of disruption, impact on economic and societal activities) and guidance (txt:344-351); EU Reg 2018/151 Art 3 elaborates the parameters (eur:1-13); its Art 4 "Substantial impact of an incident" is a row of dots in the deposited text (eur:15-16).
So: substantial impact = input; not substantial → no duty.

OES (not my seat, for completeness): the designated competent authority for the OES, in writing, about "any incident which has a significant impact on the continuity of the essential service" (reg 11(1), txt:285).
An OES reliant on an RDSP must also notify its competent authority of a significant impact caused by an incident affecting the RDSP, "without undue delay" with no hour limit (reg 12(9), txt:353).

## (3) By when?

RDSP: "without undue delay and in any event no later than 72 hours after the RDSP is first aware that an incident has occurred" (reg 12(6)(a), txt:342).
OES: "without undue delay and in any event no later than 72 hours after the operator is aware that a NIS incident has occurred" (reg 11(3)(b)(i), txt:299).

Counting: the unit is **hours**, elapsed from awareness. No calendar days, no business days, no day-0 rule, no time zone, no definition of "aware".
"No later than 72 hours after" is inclusive of the 72nd hour:

| Notified at (after awareness T) | 72-hour limb |
| --- | --- |
| T + 0h | within |
| T + 71h59m | within |
| T + 72h00m | within ("no later than") |
| T + 72h01m | outside: late |
| T + 73h | outside: late |

Fork F-B (undue delay): the primary standard is "without undue delay"; 72 hours is only the outer limit ("in any event"). A notification at T + 71h can still breach if the delay was undue; the text gives no test of "undue". So "within 72 hours" means "not out of time on the 72-hour limb", not "compliant".

Fork F-C (trigger differs): the RDSP clock starts when it is "first aware that an incident has occurred" (any incident, before substantiality is assessed); the OES clock starts when it is "aware that a NIS incident has occurred" (an incident already of significant impact). Reading 1 (literal, mine): an RDSP's 72 hours can start before it knows the impact is substantial. Reading 2: read the RDSP clock as starting on awareness of a notifiable (substantial) incident, as for an OES.

## (4) What must the notification contain?

RDSP, reg 12(5) (txt:334-340): (a) the RDSP's name and the digital services it provides; (b) the time the incident occurred; (c) its duration; (d) information concerning its nature and impact; (e) information concerning any, or any likely, cross-border impact; (f) any other information that may be helpful to the Information Commission.
Plus reg 12(6)(b) (txt:343): "sufficient information to enable the Information Commission to determine the significance of any cross-border impact."
In writing (reg 12(3)). No form or manner is prescribed for an RDSP.
No RDSP equivalent of reg 11(4)'s limit to information "within the knowledge" of the notifier; EU Reg 2018/151 Art 3(6) (eur:12) only says RDSPs need not collect information they lack for the substantiality parameters.
No staged (initial / final) reports; a single notification.

OES, reg 11(3)(a)(i)-(vi) (txt:291-297), same six items with "the operator's name and the essential services it provides"; form and manner as the competent authority determines (11(3)(b)(ii)); limited by reg 11(4) (txt:301).

## (5) Enforcement and penalty exposure for failing to notify

Enforcement notice: the Information Commission "may serve an enforcement notice upon a RDSP" if it has reasonable grounds to believe the RDSP failed to "(b) notify an incident under regulation 12(3)" or "(c) comply with the notification requirements stipulated in regulation 12(5)" (reg 17(2), txt:471-474), after informing the RDSP of the alleged failure and how to make representations (17(2A), txt:481-483).
The RDSP must comply with the notice (17(3A), txt:492); non-compliance can lead to civil proceedings for an injunction or specific performance, not before 28 days from service (reg A20(1)(b), (5), (6), txt:19, 26-30).

Penalty: the Commission may serve a notice of intention to impose a penalty for failure "to comply with a duty referred to in regulation 17(2) or the duty set out in regulation (3A)" if it "considers that a penalty is warranted" (reg 18(2), txt:502), then a penalty notice (18(3B), txt:511), irrespective of any enforcement notice (18(3C), txt:512).
The amount must be "appropriate and proportionate" (18(5)(a), txt:525) and (18(6), txt:527-531):
- not exceed **£1,000,000** for a contravention the authority determines was **not** material;
- not exceed **£8,500,000** for a material contravention not meeting (d);
- not exceed **£17,000,000** for a material contravention the authority determines "has or could have created a significant risk to, or significant impact on, or in relation to, the service provision by the OES or RDSP".
- 18(6)(b) is a row of dots (omitted).
"Material contravention" (18(7)(a), txt:533-539): (i) failing to take, within the period, the steps an enforcement notice required to rectify a failure in 17(2)(a)-(d); or (ii) where no enforcement notice was served, or it required no steps, a failure in 17(2)(a)-(d) itself.
So failure to notify (17(2)(b)):
- no enforcement notice → material → max £8.5m, or £17m if the significant-risk/impact determination is made;
- enforcement notice requiring steps, steps not taken in time → material → same;
- enforcement notice requiring steps, steps taken in time → the original failure is in neither limb → not material → max £1m.
Every penalty is discretionary ("may", "warranted", reg 23 reasonable and proportionate, txt:576-582); the figures are maxima, not amounts.
Failures under 17(2)(da) (reg 14A), (e) and (f) are outside "(a) to (d)", so never material: max £1m. (Fork F-D: I read the inserted (da) as after (d) and so outside "(a) to (d)"; the other reading puts it inside.)

**Late RDSP notification (made, but after 72 hours).** Reg 17(2) names 12(3) (notify) and 12(5) (content). It does not name 12(6), which holds the 72-hour limit and the cross-border sufficiency requirement.
Contrast OES: 17(1)(c) names 11(3), which contains both the content (11(3)(a)) and the 72-hour limit (11(3)(b)(i)); so an OES's late notification is plainly an enforceable failure.
Fork F-E:
- Reading A (literal, mine): a late RDSP notification is still a notification "under regulation 12(3)", and lateness breaches only 12(6), which no limb of 17(2) names; so no enforcement notice and, because 18(2) penalties hang off 17(2) duties (and 17(3A)), **no penalty for lateness alone**. The OES contrast supports this reading (the draftsman named 11(3) whole but only 12(5) for RDSPs).
- Reading B (purposive): 12(6)(a) qualifies the 12(3) duty ("The notification under paragraph (3) must ... be made ... no later than 72 hours"), so a late notification is a failure to notify under 12(3) → 17(2)(b) → material → up to £8.5m / £17m.
An information notice (reg 15(3)(c), txt:398) can still be used to "identify any failure of the RDSP to comply with any duty", whichever reading.
A notification that omits 12(6)(b) cross-border sufficiency is in the same position as lateness.

Text defects noticed: 18(2) says "the duty set out in regulation (3A)" with no "17" (txt:502); 14A(5) says "A nomination under paragraph (1)" though the nomination is in 14A(2) (txt:13); 21(6)(b) refers to 18(7)(b), which is a row of dots (txt:565, 540).

## (6) A provider outside the UK

Territorial extent is reg 1(6) (txt:126-129: the UK, its territorial sea and continental shelf areas); reg 1(3)(e)(i) is the head-office/representative condition of the RDSP definition.

Reg 14A applies to a digital service provider that (a) "has its head office outside the United Kingdom, but which offers digital services within the United Kingdom" and (b) "is not a small or micro enterprise" (txt:3-5).
It must (2)(a) nominate in writing a representative in the UK and (b) notify the Information Commission of the representative's name and contact details (txt:6-8), within three months of the Regulations coming into force (if already offering services then), otherwise within three months of first offering digital services in the UK (14A(3), txt:9-11).
(Fork F-F: 14A(3)(a) says "these regulations" in lower case; on its face that is the NIS Regulations, in force 10 May 2018 (reg 1(1), txt:87); if it meant the amending instrument that inserted 14A, the date differs and the deposited text does not say which. Counting of "three months" is not stated.)

- **With a UK representative** (and not small/micro, providing a digital service in the UK): an RDSP by reg 1(3)(e)(i); everything in (2)-(5) applies. The Commission may contact the representative instead of or as well as the provider (14A(4)).
- **Without a UK representative**: NOT an RDSP (1(3)(e)(i) fails), so reg 12(3)'s duty to notify does not attach. Reg 14A's duty to nominate does attach (it addresses a "digital service provider"). But enforcement of 14A is 17(2)(da), and 17(2) and 18(2) act only "upon a RDSP"; a provider that never nominates is never an RDSP.
  Fork F-G: Reading A (literal, mine): the text as drafted gives no enforcement notice or penalty against a non-UK provider that fails to nominate; Reading B: read "RDSP" in 17(2)(da) purposively to include the 14A provider, else (da) does nothing.
- Small or micro, outside the UK: 14A does not apply (14A(1)(b)), and not an RDSP: nothing.

## (7) What the text does NOT contain

- No duty specific to AI, AI models, or AI incidents; the words "artificial intelligence" and "model" do not occur.
- No numeric threshold for "substantial impact" (RDSP) or "significant impact" (OES): reg 11(2) and 12(7) give factors only, and EU Reg 2018/151 Art 4 is omitted (dots) in the deposited text, so the deposited bundle cannot answer a numeric-threshold question at all (whether the official text has one was not checked).
- No staged reporting (no early warning, no intermediate or final report); one notification.
- No business-day or calendar-day count; no definition of "aware" or "undue delay"; no form prescribed for an RDSP notification.
- No duty on the provider to tell users or the public, except that the Commission may "direct the RDSP ... to" inform the public (12(12), txt:358-360), enforceable under 17(2)(d).
- No criminal offence, no personal liability of directors, no fine beyond the reg 18 civil penalty.
- Reg 19 is a row of dots; 18(6)(b), 18(7)(b), 12(10), 12(17) are omitted; Schedule 3, if any, is absent from the deposited text.

## Ambiguities, collected

| Fork | Question | Readings | Mine |
| --- | --- | --- | --- |
| F-A | Is an AI model service a "cloud computing service" (or "online search engine")? | yes / no | input |
| F-B | Is a notification within 72h compliant? | only if not unduly delayed / yes | 72h is an outer limit only |
| F-C | When does the RDSP clock start? | first aware of any incident / aware of a substantial one | first aware of any incident (literal) |
| F-D | Is 17(2)(da) inside "(a) to (d)" for materiality? | outside / inside | outside |
| F-E | Is a late (or cross-border-insufficient) RDSP notification enforceable? | no, 12(6) not named in 17(2) / yes, via 12(3) | no (literal); B stated |
| F-F | 14A(3)(a): which "these regulations"? | NIS Regs 2018 / the inserting instrument | open |
| F-G | Can 14A be enforced against a non-UK provider with no representative? | no, not an RDSP / yes, purposively | no (literal) |
