# PLAN: the EU Artificial Intelligence Act (Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744) in L4 (stable): the keel, and what the nine parts build on it

Status (2026-11-17). The signatures in sections 3 and 7, the part ranges in section 6 and the pattern code in section 7 are copied from the files by a script (`work/build_plan.py`, outside the deposit), not retyped.
Every module and test named here compiles with no error or warning on the stable binary 1.6.110 and reads the same on 1.6.109: `check.sh` printed 14 modules, 666 assertions satisfied, 0 failed, 0 refused; every `#TRACE` (31) was compared by hand on both builds.
The keel's readings are assumed, not ruled; where the text reads two ways the reading taken is in `NOTES.md`, fork register.

## 1 Purpose and how to read this plan

The text is about 61,000 words and nine part agents will encode it in parallel, in separate sandboxes, each with its own line ranges (section 6) and with the keel's modules as read-only files.
A part cannot talk to the keel or to another part, so this plan is the only thing they share beyond the modules.
Read it in this order: section 2 (how to name things), section 3 (what you may call), section 7 (the time axis: every part uses it, and three worked patterns show how), section 8 (the seat layer), section 9 (what your `NOTES.md` must contain), then section 6 (your row), section 4 (your seams) and section 5 (traps).
The keel's own modules are `aia-core.l4`, `aia-timeline.l4`, `aia-annex-x.l4`, `aia-definitions.l4`, `aia-scope.l4` and `aia-literacy.l4`, each with a `-tests.l4`; `aia-pattern-a-decision.l4`, `aia-pattern-b-regulative.l4` and `aia-pattern-c-seat.l4` are illustrations that are run by `check.sh` but are not imported by anything.
The keel's coverage table, fork register and the rest are in `NOTES.md`.
Commencement is IN for this Regulation: assumed, not ruled (the Guide's section 4 would put it out; the brief for this Act says otherwise).
The consolidated text is a rendering with no legal effect; the as-enacted wording of an amended provision is in `eu-ai-act-2024-1689.txt`.

## 2 Naming rule

- A name defined in two modules imported together cannot be used at all, so no two parts may define the same name. Every top-level name (function, constant, type, constructor not in the core) a part defines **begins with the label of the provision it implements**, in the Regulation's own numbering: `Art 5(1)(a) ...`, `Art 4a(2) ...`, `Art 75b(1)(c) ...`, `Annex III point 4(a) ...`. Parentheses inside a backtick name parse fine on the stable binary. **That covers every type and every constructor**, not only functions: write `` DECLARE `Art 6(3) classification` IS ONE OF `Art 6(3) derogation applies`, ... ``, never a bare `Not entitled`.
- The function's name carries the section it implements and does not claim more than the section says: `Art 26(1) the deployer has used the system in accordance with the instructions for use`, not `is the system used properly`. A name never begins with "is" or "may I", and a field name never starts with `is ` or `has `.
- Types and constructors shared across parts live only in the core and the keel's modules (section 3). A part may not edit the keel's modules and never waits for them. If a part needs a type or constructor they lack, it defines it in its own module under its own prefix, records it in `NEEDS-CORE.md` in its sandbox, and the lead hoists it at the merge.
- The keel's own names follow the same rule for the provisions the keel encodes (Articles 1 to 4, 111, 113, Annex X; the Omnibus's Article 4 as `Omnibus Art 4 ...`), and no part encodes those provisions, so no collision arises. The core's shared nouns (`Provider`, `Route to high-risk`, `Provision group` ...) begin with no label; a part must not define a name that begins with `Art 1 `, `Art 2(`, `Art 3(`, `Art 4(`, `Art 111`, `Art 113`, `Omnibus` or `Annex X `.
- File names: every module of part `Pn` begins with `Pn-` (the part's id), and every module of the keel begins with `aia-`. Seat files are `Pn-seat-<slug>.l4` and `Pn-cases-seat-<slug>.l4` (section 8).
- `IMPORT` finds only modules in the importing file's own folder. A part imports `prelude`, `daydate`, `` `aia-core` ``, `` `aia-timeline` `` and any other keel module it needs, and its own modules. It never imports another part.
- Dates are `Date day month year`, day first. Never define a `YMD` (a second definition collides with the `daydate` of builds that have one).

## 3 The core and the keel's modules

**How a part uses them.** Import them; call their functions; never restate a date of Article 113 or Article 111, never write your own version or applicability test, never restate a definition of Article 3.
A definition that uses another defined term takes that term as a `BOOLEAN` input named for it; compute that input with the function of the other definition.

**`aia-core.l4`**: `DECLARE` and two constants only; imports `prelude` and `daydate` only. What it declares:

- `Version of the Regulation` is one of: `as enacted`, `as amended`.
- `Provision group` is one of: `Chapter I`, `Chapter II`, `Article 5 additions`, `Notified bodies, GPAI, governance, penalties and Art 78`, `Chapter III Sections 1 to 3`, `Articles 102 to 110`, `General`.
- `Route to high-risk` is one of: `Route Article 6(1) and Annex I`, `Route Article 6(2) and Annex III`, `Route neither`.
- `Role` is one of: `Provider`, `Deployer`, `Authorised representative`, `Importer`, `Distributor`, `Product manufacturer`, `Operator`, `Notified body`, `Affected person`.
- `Place of a party` is one of: `Established or located in the Union`, `Established or located in a third country`.
- `Party` has: `natural person` (BOOLEAN), `public authority, agency or other body` (BOOLEAN), `place` (Place of a party).
- `AI system` has: `date placed on the market or put into service` (DATE), `route` (Route to high-risk), `significantly changed in its design since the date of application of Chapter III` (BOOLEAN).
- `AI model` has: `date placed on the market` (DATE), `cumulative compute used for its training, in floating-point operations` (NUMBER).
- `Article reference` has: `number` (NUMBER), `letter` (STRING), `paragraph` (NUMBER).
- `the date to pass when no AI system is in question` returns (a constant).
- `the route to pass when no AI system is in question` returns (a constant).

The membership test for the core: could a witness of ordinary competence testify to this fact, or does answering it need the Regulation? Only the first kind is in the core. Money is a `NUMBER` of euros; a number the Regulation leaves to an act of the Commission is an input.
`Operator` stands for any of the six roles of Article 3(8): a person states the role they hold, never `Operator`. `Notified body` and `Affected person` are roles but not operators.
`Article reference`: `number` 0 means no number; `paragraph` 0 means the whole Article; `letter` is `""` or `"a"` to `"d"` (Article 4a is number 4, letter "a"; Article 60a is 60, "a"; Article 75d is 75, "d").

**Which provision group is a provision in?** (Article 113 as amended, with Article 111(2) saving Article 5; details of the groups: `NOTES.md`, fork F-113-groups.) Pass the group as the first argument of the applicability function (section 7).
An Annex takes the group of the Article that gives it effect (assumed, not ruled).

| group (`Provision group`) | Articles | Date from (as amended) |
| --- | --- | --- |
| `Chapter I` | 1 to 4a | 2 February 2025 |
| `Chapter II` | 5, except 5(1) first subparagraph points (ba) and (bb), 5(1a), 5(1b) | 2 February 2025 |
| `Article 5 additions` | 5(1) first subparagraph points (ba) and (bb); 5(1a); 5(1b) | 2 December 2026 |
| `Notified bodies, GPAI, governance, penalties and Art 78` | Chapter III Section 4 (28 to 39); Chapter V (51 to 56); Chapter VII (64 to 70); Chapter XII except 101 (99, 100); 78 | 2 August 2025 |
| `Chapter III Sections 1 to 3` | 6 to 27, except 6(5) | 2 December 2027 for a system high-risk under Article 6(2) and Annex III; 2 August 2028 under Article 6(1) and Annex I; no date for a system that is not high-risk |
| `Articles 102 to 110` | 102 to 110 | 27 July 2026 |
| `General` | every other provision: 6(5); Chapter III Section 5 (40 to 49); Chapter IV (50); Chapter VI (57 to 63, including 60a); Chapter VIII (71); Chapter IX except 78 (72 to 94, including 75a to 75d); Chapters X and XI (95 to 98); 101; 111 to 113 | 2 August 2026 |

As enacted the dates differ (`NOTES.md`; section 7 has them all): there was no `Article 5 additions` group, `Articles 102 to 110` applied from 2 August 2026, and Chapter III Sections 1 to 3 applied from 2 August 2026 (Article 6(2) route) or 2 August 2027 (Article 6(1) route).
The chapter and article boundaries above come from the chapter headings and `HEADINGS.md`, not from reading the text of the other parts' ranges.

**`aia-timeline.l4`**: Articles 111 and 113 as enacted and as amended, and the entry into force of the Omnibus (its Article 4). Imports the core. Section 7 gives the exported names with their signatures and three worked patterns. Everything it defines:

- `Art 113 the Regulation was published` returns (a constant).
- `Art 113 the Regulation enters into force` returns (a constant).
- `Omnibus Art 4 the Omnibus was published` returns (a constant).
- `Omnibus Art 4 the Omnibus enters into force` returns (a constant).
- `Omnibus Art 4 the version in force` returns `Version of the Regulation`. Inputs, in order: the date asked (DATE).
- `Art 113 the Regulation is in force` returns BOOLEAN. Inputs, in order: the date asked (DATE).
- `Art 113 second paragraph the general date of application` returns (a constant).
- `Art 113(a) Chapters I and II apply from` returns (a constant).
- `Art 113(a) the Article 5 additions apply from` returns (a constant).
- `Art 113(b) the group of Chapter III Section 4, Chapters V, VII, XII and Article 78 applies from` returns (a constant).
- `Art 113(c)(i) Chapter III Sections 1 to 3 apply to Annex III systems from` returns (a constant).
- `Art 113(c)(ii) Chapter III Sections 1 to 3 apply to Annex I systems from` returns (a constant).
- `Art 113(d) Articles 102 to 110 apply from` returns (a constant).
- `Art 113 as enacted the general date of application` returns (a constant).
- `Art 113(c) as enacted Article 6(1) and the corresponding obligations apply from` returns (a constant).
- `Art 113 as enacted the date of application` returns MAYBE DATE. Inputs, in order: the provision group (Provision group); the route to high-risk (Route to high-risk).
- `Art 113 as amended the date of application` returns MAYBE DATE. Inputs, in order: the provision group (Provision group); the route to high-risk (Route to high-risk).
- `Art 111(2) as enacted the date before which a placed system is saved` returns (a constant).
- `Art 111(2) the provision group can be saved` returns BOOLEAN. Inputs, in order: the provision group (Provision group).
- `Art 111(2) as enacted the system is saved` returns BOOLEAN. Inputs, in order: the provision group (Provision group); the route to high-risk (Route to high-risk); the date the AI system was placed on the market or put into service (DATE); the AI system has been significantly changed in its design since the date of application of Chapter III.
- `Art 111(2) as amended the system is saved` returns BOOLEAN. Inputs, in order: the provision group (Provision group); the route to high-risk (Route to high-risk); the date the AI system was placed on the market or put into service (DATE); the AI system has been significantly changed in its design since the date of application of Chapter III.
- `Art 113 the date of application has come` returns BOOLEAN. Inputs, in order: the date of application (MAYBE DATE); the date asked (DATE).
- `Art 113 as enacted the provision group applies` returns BOOLEAN. Inputs, in order: the provision group (Provision group); the date asked (DATE); the route to high-risk (Route to high-risk); the date the AI system was placed on the market or put into service (DATE); the AI system has been significantly changed in its design since the date of application of Chapter III.
- `Art 113 as amended the provision group applies` returns BOOLEAN. Inputs, in order: the provision group (Provision group); the date asked (DATE); the route to high-risk (Route to high-risk); the date the AI system was placed on the market or put into service (DATE); the AI system has been significantly changed in its design since the date of application of Chapter III.
- `Art 113 the provision group applies` returns BOOLEAN. Inputs, in order: the provision group (Provision group); the date asked (DATE); the route to high-risk (Route to high-risk); the date the AI system was placed on the market or put into service (DATE); the AI system has been significantly changed in its design since the date of application of Chapter III.
- `Art 111(1) the date by which the AI system must be brought into compliance` returns MAYBE DATE. Inputs, in order: the date asked (DATE); the date the AI system was placed on the market or put into service (DATE); the AI system is a component of a large-scale IT system established by a legal act listed in Annex X.
- `Art 111(1) the requirements of this Regulation are to be taken into account in the evaluation` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the evaluation of the large-scale IT system is being undertaken as provided for in the legal acts listed in Annex X; the legal acts listed in Annex X are being replaced or amended.
- `Art 111(2) as enacted the date by which providers and deployers of high-risk AI systems intended for public authorities must comply` returns MAYBE DATE. Inputs, in order: the AI system is a high-risk AI system intended to be used by public authorities.
- `Art 111(2) as amended the date by which providers and deployers of high-risk AI systems intended for public authorities must comply` returns MAYBE DATE. Inputs, in order: the AI system is a high-risk AI system intended to be used by public authorities.
- `Art 111(2) the date by which providers and deployers of high-risk AI systems intended for public authorities must comply` returns MAYBE DATE. Inputs, in order: the date asked (DATE); the AI system is a high-risk AI system intended to be used by public authorities.
- `Art 111(3) the date by which the provider of a general-purpose AI model already on the market must comply` returns MAYBE DATE. Inputs, in order: the date asked (DATE); the date the general-purpose AI model was placed on the market (DATE).
- `Art 111(4) the date by which the provider of an AI system generating synthetic content must comply with Article 50(2)` returns MAYBE DATE. Inputs, in order: the date asked (DATE); the date the AI system was placed on the market (DATE); the AI system generates synthetic audio, image, video or text content.
- `Art 111 act` is one of: `Art 111(1) bring the AI system into compliance with this Regulation`, `Art 111(2) take the necessary steps to comply with the requirements and obligations`, `Art 111(3) take the necessary steps to comply with the obligations laid down in this Regulation`, `Art 111(4) take the necessary steps to comply with Article 50(2)`.
- `Art 111(1) the duty to bring the AI system into compliance` returns DEONTIC Role `Art 111 act`. Inputs, in order: the date asked (DATE); the date the AI system was placed on the market or put into service (DATE); the AI system is a component of a large-scale IT system established by a legal act listed in Annex X.
- `Art 111(2) the provider's duty to take the necessary steps` returns DEONTIC Role `Art 111 act`. Inputs, in order: the date asked (DATE); the AI system is a high-risk AI system intended to be used by public authorities.
- `Art 111(2) the deployer's duty to take the necessary steps` returns DEONTIC Role `Art 111 act`. Inputs, in order: the date asked (DATE); the AI system is a high-risk AI system intended to be used by public authorities.
- `Art 111(3) the duty of the provider of a general-purpose AI model already on the market` returns DEONTIC Role `Art 111 act`. Inputs, in order: the date asked (DATE); the date the general-purpose AI model was placed on the market (DATE).
- `Art 111(4) the duty of the provider of an AI system generating synthetic content` returns DEONTIC Role `Art 111 act`. Inputs, in order: the date asked (DATE); the date the AI system was placed on the market (DATE); the AI system generates synthetic audio, image, video or text content.

**`aia-annex-x.l4`**: Annex X (twelve acts, seven points) as a table, with `Annex X the large-scale IT system is established by a listed legal act`, whose result is the input of the `Art 111(1)` functions. Everything it defines:

- `Annex X entry` has: `point` (NUMBER), `letter` (STRING), `system` (STRING), `act` (STRING).
- `Annex X the entries` returns (a constant).
- `Annex X the act is listed` returns BOOLEAN. Inputs, in order: the act (STRING).
- `Annex X the large-scale IT system the act establishes` returns MAYBE STRING. Inputs, in order: the act (STRING).
- `Annex X the large-scale IT system is established by a listed legal act` returns BOOLEAN. Inputs, in order: the AI system is a component of a large-scale IT system; the act that establishes that large-scale IT system (STRING).

**`aia-definitions.l4`**: Article 3, every definition ((1) to (68), (14a), (14b)), one function each, plus the record builders and the two reading rules of (47) and (48). Every definition says "means", so each returns a `BOOLEAN` (a `FALSE` is the text's own no). Only (14) takes `the date asked` (the Omnibus replaced it), and (14a), (14b) (inserted). Definitions are not gated by Article 113 (`NOTES.md`, fork F-3-gate). A borrowed term (a "harmonised standard", "personal data", "critical infrastructure") is an input named for the instrument it comes from. Everything it defines:

- `Art 3(1) the system is an AI system` returns BOOLEAN. Inputs, in order: the system is machine-based; the system is designed to operate with varying levels of autonomy; for explicit or implicit objectives, the system infers from the input it receives how to generate outputs such as predictions, content, recommendations or decisions; those outputs can influence physical or virtual environments.
- `Art 3(2) risk` has: `probability of an occurrence of harm` (NUMBER), `severity of that harm` (NUMBER).
- `Art 3(2) the risk is the combination of probability and severity` returns `Art 3(2) risk`. Inputs, in order: the probability of an occurrence of harm (NUMBER); the severity of that harm (NUMBER).
- `Art 3(3) the party is a provider` returns BOOLEAN. Inputs, in order: the party develops an AI system or a general-purpose AI model; the party has an AI system or a general-purpose AI model developed; the party places it on the market, or puts the AI system into service; the party does so under its own name or trademark.
- `Art 3(4) the party is a deployer` returns BOOLEAN. Inputs, in order: the party uses an AI system under its authority; the AI system is used in the course of a personal non-professional activity.
- `Art 3(5) the party is an authorised representative` returns BOOLEAN. Inputs, in order: the party is located or established (Place of a party); the party has received and accepted a written mandate from a provider of an AI system or a general-purpose AI model; the mandate is to perform and carry out on the provider's behalf the obligations and procedures established by this Regulation.
- `Art 3(6) the party is an importer` returns BOOLEAN. Inputs, in order: the party is located or established (Place of a party); the party places an AI system on the market; the AI system bears the name or trademark of a natural or legal person established in a third country.
- `Art 3(7) the party is a distributor` returns BOOLEAN. Inputs, in order: the party is in the supply chain; the party is the provider of the AI system; the party is the importer of the AI system; the party makes the AI system available on the Union market.
- `Art 3(8) the role is an operator` returns BOOLEAN. Inputs, in order: the role (Role).
- `Art 3(9) the supply is a placing on the market` returns BOOLEAN. Inputs, in order: the supply is a making available of an AI system or a general-purpose AI model on the Union market; it is the first making available of that AI system or model on the Union market.
- `Art 3(10) the supply is a making available on the market` returns BOOLEAN. Inputs, in order: the supply is of an AI system or a general-purpose AI model for distribution or use on the Union market; the supply is in the course of a commercial activity.
- `Art 3(11) the supply is a putting into service` returns BOOLEAN. Inputs, in order: the supply is of an AI system for first use; the supply is directly to the deployer; the supply is for own use in the Union; the first use is for the intended purpose of the AI system.
- `Art 3(12) the use is the intended purpose` returns BOOLEAN. Inputs, in order: the use is the use for which the provider intends the AI system, including the specific context and conditions of use; it is specified in the instructions for use; it is specified in promotional or sales materials and statements; it is specified in the technical documentation.
- `Art 3(13) the use is a reasonably foreseeable misuse` returns BOOLEAN. Inputs, in order: the use is in a way that is not in accordance with the intended purpose of the AI system; the use may result from reasonably foreseeable human behaviour or interaction with other systems, including other AI systems.
- `Art 3(14) the component is a safety component` returns BOOLEAN. Inputs, in order: the date asked (DATE); the component is a component of a product or of an AI system; it fulfils a safety function for that product or AI system; its failure or malfunctioning endangers the health and safety of persons or property; its intended purpose is to prevent or mitigate risks to health and safety of persons or property.
- `Art 3(14a) the enterprise is a micro, small and medium-sized enterprise` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the enterprise is a micro, small or medium-sized enterprise as defined in Article 2 of the Annex to Recommendation 2003/361/EC.
- `Art 3(14b) the enterprise is a small mid-cap enterprise` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the enterprise is a small mid-cap enterprise as defined in point (2) of the Annex to Recommendation (EU) 2025/1099.
- `Art 3(15) the information is instructions for use` returns BOOLEAN. Inputs, in order: the information is provided by the provider; it is provided to inform the deployer of the intended purpose and proper use of the AI system.
- `Art 3(16) the measure is a recall of an AI system` returns BOOLEAN. Inputs, in order: the measure aims to achieve the return of an AI system to the provider; the measure aims to take an AI system out of service; the measure aims to disable the use of an AI system; the AI system was made available to deployers.
- `Art 3(17) the measure is a withdrawal of an AI system` returns BOOLEAN. Inputs, in order: the measure aims to prevent an AI system in the supply chain being made available on the market.
- `Art 3(18) the quality is the performance of an AI system` returns BOOLEAN. Inputs, in order: the quality is the ability of an AI system to achieve its intended purpose.
- `Art 3(19) the authority is a notifying authority` returns BOOLEAN. Inputs, in order: the authority is a national authority; it is responsible for setting up and carrying out the necessary procedures for the assessment, designation and notification of conformity assessment bodies and for their monitoring.
- `Art 3(20) the process is a conformity assessment` returns BOOLEAN. Inputs, in order: the process is a process of demonstrating whether requirements have been fulfilled; the requirements are those set out in Chapter III, Section 2; they relate to a high-risk AI system.
- `Art 3(21) the body is a conformity assessment body` returns BOOLEAN. Inputs, in order: the body performs third-party conformity assessment activities.
- `Art 3(22) the body is a notified body` returns BOOLEAN. Inputs, in order: the body is a conformity assessment body; it is notified in accordance with this Regulation; it is notified in accordance with other relevant Union harmonisation legislation, or no other such legislation is relevant.
- `Art 3(23) the change is a substantial modification` returns BOOLEAN. Inputs, in order: the change is to an AI system after its placing on the market or putting into service; the change is foreseen or planned in the initial conformity assessment carried out by the provider; as a result of the change the compliance of the AI system with the requirements set out in Chapter III, Section 2 is affected; the change results in a modification to the intended purpose for which the AI system has been assessed.
- `Art 3(24) the marking is a CE marking` returns BOOLEAN. Inputs, in order: the marking is a marking by which a provider indicates something; it indicates that an AI system is in conformity with the requirements set out in Chapter III, Section 2; it indicates conformity with other applicable Union harmonisation legislation providing for its affixing.
- `Art 3(25) the activities are a post-market monitoring system` returns BOOLEAN. Inputs, in order: the activities are all carried out by providers of AI systems; they collect and review experience gained from the use of AI systems the providers place on the market or put into service; they are for the purpose of identifying any need to immediately apply any necessary corrective or preventive actions.
- `Art 3(26) the authority is a market surveillance authority` returns BOOLEAN. Inputs, in order: the authority is a national authority; it carries out the activities and takes the measures pursuant to Regulation (EU) 2019/1020.
- `Art 3(27) the standard is a harmonised standard` returns BOOLEAN. Inputs, in order: the standard is a harmonised standard as defined in Article 2(1), point (c), of Regulation (EU) No 1025/2012.
- `Art 3(28) the set is a common specification` returns BOOLEAN. Inputs, in order: the set is a set of technical specifications as defined in Article 2, point (4) of Regulation (EU) No 1025/2012; it provides means to comply with certain requirements established under this Regulation.
- `Art 3(29) the data is training data` returns BOOLEAN. Inputs, in order: the data is used for training an AI system through fitting its learnable parameters.
- `Art 3(30) the data is validation data` returns BOOLEAN. Inputs, in order: the data is used for providing an evaluation of the trained AI system; the data is used for tuning the non-learnable parameters and the learning process of the AI system.
- `Art 3(31) the data set is a validation data set` returns BOOLEAN. Inputs, in order: the data set is a separate data set; the data set is part of the training data set, as a fixed or variable split.
- `Art 3(32) the data is testing data` returns BOOLEAN. Inputs, in order: the data is used for providing an independent evaluation of the AI system; it is used to confirm the expected performance of that system before its placing on the market or putting into service.
- `Art 3(33) the data is input data` returns BOOLEAN. Inputs, in order: the data is provided to an AI system; the data is directly acquired by an AI system; the system produces an output on the basis of it.
- `Art 3(34) the data is biometric data` returns BOOLEAN. Inputs, in order: the data is personal data; it results from specific technical processing; it relates to the physical, physiological or behavioural characteristics of a natural person.
- `Art 3(35) the recognition is a biometric identification` returns BOOLEAN. Inputs, in order: the recognition is the automated recognition of physical, physiological, behavioural, or psychological human features; it is for the purpose of establishing the identity of a natural person; it is by comparing the biometric data of that individual to biometric data of individuals stored in a database.
- `Art 3(36) the verification is a biometric verification` returns BOOLEAN. Inputs, in order: the verification is automated; it is one-to-one; it is a verification, including authentication, of the identity of natural persons; it is by comparing their biometric data to previously provided biometric data.
- `Art 3(37) the category is a special category of personal data` returns BOOLEAN. Inputs, in order: the category is referred to in Article 9(1) of Regulation (EU) 2016/679; the category is referred to in Article 10 of Directive (EU) 2016/680; the category is referred to in Article 10(1) of Regulation (EU) 2018/1725.
- `Art 3(38) the data is sensitive operational data` returns BOOLEAN. Inputs, in order: the data is operational data; it is related to activities of prevention, detection, investigation or prosecution of criminal offences; its disclosure could jeopardise the integrity of criminal proceedings.
- `Art 3(39) the AI system is an emotion recognition system` returns BOOLEAN. Inputs, in order: the AI system is an AI system; it is for the purpose of identifying or inferring emotions or intentions of natural persons; it does so on the basis of their biometric data.
- `Art 3(40) the AI system is a biometric categorisation system` returns BOOLEAN. Inputs, in order: the AI system is an AI system; it is for the purpose of assigning natural persons to specific categories; it does so on the basis of their biometric data; it is ancillary to another commercial service; it is strictly necessary for objective technical reasons.
- `Art 3(41) the AI system is a remote biometric identification system` returns BOOLEAN. Inputs, in order: the AI system is an AI system; it is for the purpose of identifying natural persons; it does so without their active involvement; it does so through the comparison of a person's biometric data with the biometric data contained in a reference database.
- `Art 3(42) the AI system is a real-time remote biometric identification system` returns BOOLEAN. Inputs, in order: the AI system is a remote biometric identification system; the capturing of biometric data, the comparison and the identification all occur without a significant delay, instant or after limited short delays in order to avoid circumvention.
- `Art 3(43) the AI system is a post-remote biometric identification system` returns BOOLEAN. Inputs, in order: the AI system is a remote biometric identification system; the AI system is a real-time remote biometric identification system.
- `Art 3(44) the place is a publicly accessible space` returns BOOLEAN. Inputs, in order: the place is a physical place; it is accessible to an undetermined number of natural persons.
- `Art 3(45)(a) the body is a law enforcement authority as a public authority` returns BOOLEAN. Inputs, in order: the body is a public authority; it is competent for the prevention, investigation, detection or prosecution of criminal offences or the execution of criminal penalties, including the safeguarding against and the prevention of threats to public security.
- `Art 3(45)(b) the body is a law enforcement authority as another entrusted body` returns BOOLEAN. Inputs, in order: the body is any other body or entity; it is entrusted by Member State law to exercise public authority and public powers for the purposes of the prevention, investigation, detection or prosecution of criminal offences or the execution of criminal penalties, including the safeguarding against and the prevention of threats to public security.
- `Art 3(45) the body is a law enforcement authority` returns BOOLEAN. Inputs, in order: the body is a law enforcement authority as a public authority; the body is a law enforcement authority as another entrusted body.
- `Art 3(46) the activities are law enforcement` returns BOOLEAN. Inputs, in order: the activities are carried out by law enforcement authorities; the activities are carried out on behalf of law enforcement authorities; they are for the prevention, investigation, detection or prosecution of criminal offences or the execution of criminal penalties, including safeguarding against and preventing threats to public security.
- `Art 3(47) the function is the AI Office` returns BOOLEAN. Inputs, in order: the function is the Commission's function; it is a function of contributing to the implementation, monitoring and supervision of AI systems and general-purpose AI models, and AI governance; it is provided for in Commission Decision of 24 January 2024.
- `Art 3(47) the body a reference to the AI Office is read as` returns MAYBE STRING. Inputs, in order: the reference in the Regulation is to the AI Office.
- `Art 3(48) the authority is a national competent authority` returns BOOLEAN. Inputs, in order: the authority is a notifying authority; the authority is a market surveillance authority.
- `Art 3(48) the authority a reference to national competent authorities or market surveillance authorities is read as` returns MAYBE STRING. Inputs, in order: the AI system is put into service or used by Union institutions, agencies, offices and bodies.
- `Art 3(49) the event is a serious incident` returns BOOLEAN. Inputs, in order: the event is an incident or malfunctioning of an AI system; it directly or indirectly leads to the death of a person, or serious harm to a person's health; it directly or indirectly leads to a serious and irreversible disruption of the management or operation of critical infrastructure; it directly or indirectly leads to the infringement of obligations under Union law intended to protect fundamental rights; it directly or indirectly leads to serious harm to property or the environment.
- `Art 3(50) the data is personal data` returns BOOLEAN. Inputs, in order: the data is personal data as defined in Article 4, point (1), of Regulation (EU) 2016/679.
- `Art 3(51) the data is non-personal data` returns BOOLEAN. Inputs, in order: the thing is data; the data is personal data.
- `Art 3(52) the processing is profiling` returns BOOLEAN. Inputs, in order: the processing is profiling as defined in Article 4, point (4), of Regulation (EU) 2016/679.
- `Art 3(53) what a real-world testing plan describes` has: `objectives` (BOOLEAN), `methodology` (BOOLEAN), `geographical scope` (BOOLEAN), `population scope` (BOOLEAN), `temporal scope` (BOOLEAN), `monitoring` (BOOLEAN), `organisation` (BOOLEAN), `conduct` (BOOLEAN).
- `Art 3(53) the document is a real-world testing plan` returns BOOLEAN. Inputs, in order: the thing is a document; what the document describes of testing in real-world conditions (Art 3(53) what a real-world testing plan describes).
- `Art 3(54) what a sandbox plan describes` has: `objectives` (BOOLEAN), `conditions` (BOOLEAN), `timeframe` (BOOLEAN), `methodology` (BOOLEAN), `requirements` (BOOLEAN).
- `Art 3(54) the document is a sandbox plan` returns BOOLEAN. Inputs, in order: the thing is a document; it is agreed between the participating provider and the competent authority; what the document describes for the activities carried out within the sandbox (Art 3(54) what a sandbox plan describes).
- `Art 3(55) the framework is an AI regulatory sandbox` returns BOOLEAN. Inputs, in order: the framework is a controlled framework; it is set up by a competent authority; it offers providers or prospective providers of AI systems the possibility to develop, train, validate and test an innovative AI system, where appropriate in real-world conditions; it does so pursuant to a sandbox plan; it does so for a limited time; it does so under regulatory supervision.
- `Art 3(56) the things are AI literacy` returns BOOLEAN. Inputs, in order: the things are skills, knowledge and understanding; they allow providers, deployers and affected persons, taking into account their respective rights and obligations in the context of this Regulation, to make an informed deployment of AI systems; they allow them to gain awareness about the opportunities and risks of AI and possible harm it can cause.
- `Art 3(57) the testing is testing in real-world conditions` returns BOOLEAN. Inputs, in order: the testing is temporary testing of an AI system for its intended purpose; it is in real-world conditions outside a laboratory or otherwise simulated environment; it is with a view to gathering reliable and robust data and to assessing and verifying the conformity of the AI system with the requirements of this Regulation; all the conditions laid down in Article 57 or 60 are fulfilled.
- `Art 3(57) the testing does not qualify as placing on the market or putting into service` returns MAYBE BOOLEAN. Inputs, in order: the testing is testing in real-world conditions; all the conditions laid down in Article 57 or 60 are fulfilled.
- `Art 3(58) the person is a subject for the purpose of real-world testing` returns BOOLEAN. Inputs, in order: the person is a natural person; the person participates in testing in real-world conditions.
- `Art 3(59) how a subject expressed willingness` has: `freely given` (BOOLEAN), `specific` (BOOLEAN), `unambiguous` (BOOLEAN), `voluntary` (BOOLEAN), `to participate in a particular testing in real-world conditions` (BOOLEAN), `after being informed of all aspects of the testing relevant to the decision to participate` (BOOLEAN).
- `Art 3(59) the expression is an informed consent` returns BOOLEAN. Inputs, in order: the person is a subject; the expression is by the subject of willingness (Art 3(59) how a subject expressed willingness).
- `Art 3(60) the content is a deep fake` returns BOOLEAN. Inputs, in order: the content is AI-generated or manipulated; it is image, audio or video content; it resembles existing persons, objects, places, entities or events; it would falsely appear to a person to be authentic or truthful.
- `Art 3(61) the act or omission is a widespread infringement` returns BOOLEAN. Inputs, in order: the act or omission is contrary to Union law protecting the interest of individuals; the number of Member States, other than those named in (a)(i) to (iii), in which individuals residing there have been harmed or are likely to be harmed in their collective interests (NUMBER); the harm to the collective interests of individuals has been caused, is caused or is likely to be caused; the infringement has common features, including the same unlawful practice or the same interest being infringed; it is occurring concurrently, committed by the same operator; the number of Member States in which it is occurring (NUMBER).
- `Art 3(62) the infrastructure is critical infrastructure` returns BOOLEAN. Inputs, in order: the infrastructure is critical infrastructure as defined in Article 2, point (4), of Directive (EU) 2022/2557.
- `Art 3(63) the model is a general-purpose AI model` returns BOOLEAN. Inputs, in order: the model is an AI model; it displays significant generality; it is capable of competently performing a wide range of distinct tasks; it can be integrated into a variety of downstream systems or applications; it is used for research, development or prototyping activities before it is placed on the market.
- `Art 3(64) the capabilities are high-impact capabilities` returns BOOLEAN. Inputs, in order: the capabilities match the capabilities recorded in the most advanced general-purpose AI models; the capabilities exceed the capabilities recorded in the most advanced general-purpose AI models.
- `Art 3(65) the risk is a systemic risk` returns BOOLEAN. Inputs, in order: the thing is a risk; it is specific to the high-impact capabilities of general-purpose AI models; it has a significant impact on the Union market due to the reach of those models; it has a significant impact due to actual or reasonably foreseeable negative effects on public health, safety, public security, fundamental rights, or the society as a whole; it can be propagated at scale across the value chain.
- `Art 3(66) the AI system is a general-purpose AI system` returns BOOLEAN. Inputs, in order: the AI system is an AI system; it is based on a general-purpose AI model; it has the capability to serve a variety of purposes, both for direct use and for integration in other AI systems.
- `Art 3(67) the operation is a floating-point operation` returns BOOLEAN. Inputs, in order: the operation is a mathematical operation or assignment; it involves floating-point numbers.
- `Art 3(68) the party is a downstream provider` returns BOOLEAN. Inputs, in order: the party is a provider of an AI system, including a general-purpose AI system; the AI system integrates an AI model.

**`aia-scope.l4`**: Articles 1 and 2. Article 1 creates no rule (inert). Every paragraph function takes `the date asked` first and returns `MAYBE BOOLEAN`: `NOTHING` is "not covered" (before Chapter I applies, or the paragraph does not speak to these facts), `JUST TRUE` the Regulation applies (Art 2(1)), `JUST FALSE` the paragraph says it does not apply or does not affect a thing. `Art 2 the Regulation applies given the answers of the paragraphs` combines a list of those answers (an exclusion first, then an inclusion, otherwise `NOTHING`). Everything it defines:

- `Art 2 Chapter I has begun to apply on the date asked` returns BOOLEAN. Inputs, in order: the date asked (DATE).
- `Art 2(1)(a) the Regulation applies to the provider` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the party is a provider; the party places an AI system on the market or puts it into service in the Union; the party places a general-purpose AI model on the market in the Union.
- `Art 2(1)(b) the Regulation applies to the deployer in the Union` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the party is a deployer of an AI system; the party's place (Place of a party).
- `Art 2(1)(c) the Regulation applies to the provider or deployer in a third country whose output is used in the Union` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the party is a provider or a deployer of an AI system; the party's place (Place of a party); the output produced by the AI system is used in the Union.
- `Art 2(1)(d) the Regulation applies to the importer or distributor` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the party is an importer of AI systems; the party is a distributor of AI systems.
- `Art 2(1)(e) the Regulation applies to the product manufacturer` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the party is a product manufacturer; it places an AI system on the market or puts it into service together with its product; it does so under its own name or trademark.
- `Art 2(1)(f) the Regulation applies to the authorised representative of a provider not established in the Union` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the party is an authorised representative of a provider; the provider it represents is established in the Union.
- `Art 2(1)(g) the Regulation applies to the affected person in the Union` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the person is an affected person; the person's place (Place of a party).
- `Art 2(2) the provision applies to the high-risk AI system under Article 6(1) with Section B products` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the route to high-risk (Route to high-risk); the products are covered by Union harmonisation legislation listed in Section B of Annex I; the requirements for high-risk AI systems under this Regulation have been integrated in that Union harmonisation legislation; the provision (Article reference).
- `Art 2(3) the Regulation applies to the matter outside the scope of Union law` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the matter is an area outside the scope of Union law, or a competence of the Member States concerning national security.
- `Art 2(3) the Regulation applies to the AI system used exclusively for military, defence or national security purposes` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the AI system is placed on the market, put into service or used, with or without modification, exclusively for military, defence or national security purposes.
- `Art 2(3) the Regulation applies to the AI system not placed on the market in the Union whose output is used exclusively for military, defence or national security purposes` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the AI system is not placed on the market or put into service in the Union; its output is used in the Union exclusively for military, defence or national security purposes.
- `Art 2(4) the Regulation applies to the third-country public authority or international organisation` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the party is a public authority in a third country or an international organisation falling within the scope of this Regulation pursuant to paragraph 1; it uses AI systems in the framework of international cooperation or agreements for law enforcement and judicial cooperation with the Union or with one or more Member States; the third country or international organisation provides adequate safeguards with respect to the protection of fundamental rights and freedoms of individuals.
- `Art 2(5) the Regulation affects the application of the provision on the liability of providers of intermediary services` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the provision is a provision on the liability of providers of intermediary services as set out in Chapter II of Regulation (EU) 2022/2065.
- `Art 2(6) the Regulation applies to the AI system or model developed for the sole purpose of scientific research and development` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the thing is an AI system or an AI model, including its output; it was specifically developed and put into service; it was so developed and put into service for the sole purpose of scientific research and development.
- `Art 2(7) Union law on the protection of personal data, privacy and the confidentiality of communications applies to the personal data` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); personal data is processed in connection with the rights and obligations laid down in this Regulation.
- `Art 2(7) the Regulation affects the data protection instrument through the provision` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the instrument is Regulation (EU) 2016/679, Regulation (EU) 2018/1725, Directive 2002/58/EC or Directive (EU) 2016/680; the provision of this Regulation (Article reference).
- `Art 2(8) the Regulation applies to the research, testing or development activity` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the activity is a research, testing or development activity regarding AI systems or AI models; it is prior to their being placed on the market or put into service; it is testing in real world conditions.
- `Art 2(8) the activity must be conducted in accordance with applicable Union law` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the activity is a research, testing or development activity regarding AI systems or AI models; it is prior to their being placed on the market or put into service; it is testing in real world conditions.
- `Art 2(9) the Regulation prejudices the rules of the other Union legal act` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the legal act is another Union legal act related to consumer protection or product safety.
- `Art 2(10) the Regulation applies to the obligations of the natural person deployer using AI systems for a purely personal non-professional activity` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the party is a deployer who is a natural person; it uses AI systems in the course of a purely personal non-professional activity.
- `Art 2(11) the Regulation precludes the more favourable law or collective agreement` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the law, regulation, administrative provision or collective agreement is more favourable to workers in terms of protecting their rights in respect of the use of AI systems by employers.
- `Art 2(12) the Regulation applies to the AI system released under a free and open-source licence` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the AI system is released under a free and open-source licence; it is placed on the market or put into service as a high-risk AI system; it falls under Article 5; it falls under Article 50.
- `Art 2(13) the application of the requirement or obligation may be limited` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the route to high-risk (Route to high-risk); the requirement or obligation (Article reference); Union harmonisation legislation listed in Section A of Annex I lays down requirements or obligations providing an equivalent or higher level of protection of health, safety or fundamental rights as the requirement or obligation concerned; such limitation does not reduce the overall level of protection provided for by this Regulation.
- `Art 2(13) the date by which the Commission is to adopt the delegated acts` returns (a constant).
- `Art 2(13) body` is one of: `Commission`.
- `Art 2(13) act` is one of: `Art 2(13) adopt delegated acts in accordance with Article 97 specifying the high-risk AI systems concerned, the requirements or obligations that may be limited, the conditions under which such limitation applies, and the scope of the limitation`.
- `Art 2(13) the Commission's duty to adopt the delegated acts` returns DEONTIC `Art 2(13) body` `Art 2(13) act`. Inputs, in order: the date asked (DATE).
- `Art 2 the Regulation applies given the answers of the paragraphs` returns MAYBE BOOLEAN. Inputs, in order: the answers of the paragraphs (LIST OF MAYBE BOOLEAN).

**`aia-literacy.l4`**: Article 4 as enacted and as replaced. The duty of providers and deployers is a regulative rule with no time limit and no consequence (no breach path). Everything it defines:

- `Art 4 Chapter I has begun to apply on the date asked` returns BOOLEAN. Inputs, in order: the date asked (DATE).
- `Art 4(1) the party owes the duty to take measures regarding AI literacy` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the party is a provider of an AI system; the party is a deployer of an AI system.
- `Art 4(1) the measures meet the duty to take measures regarding AI literacy` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the measures concern the AI literacy of the party's staff and other persons dealing with the operation and use of AI systems on its behalf; the measures take into account the technical knowledge, experience, education and training of those persons and the context the AI systems are to be used in; the measures consider the persons or groups of persons on whom the AI systems are to be used; the measures are to ensure, to the party's best extent, a sufficient level of AI literacy; the measures are to support the development of AI literacy.
- `Art 4(1) the party must guarantee a specific level of AI literacy of an individual` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the party is a provider of an AI system; the party is a deployer of an AI system.
- `Art 4(1) act` is one of: `Art 4(1) take measures regarding AI literacy`.
- `Art 4(1) the provider's duty to take measures regarding AI literacy` returns DEONTIC Role `Art 4(1) act`. Inputs, in order: the date asked (DATE).
- `Art 4(1) the deployer's duty to take measures regarding AI literacy` returns DEONTIC Role `Art 4(1) act`. Inputs, in order: the date asked (DATE).
- `Art 4(2) the Commission and the Member States must support and facilitate the efforts of the party to fulfil the obligation under paragraph 1` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE); the party is a provider or a deployer of AI systems.
- `Art 4(2) the Commission must publish practical examples of how to comply with the obligation under paragraph 1` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE).
- `Art 4(3) the Board must adopt recommendations to support the promotion of AI literacy` returns MAYBE BOOLEAN. Inputs, in order: the date asked (DATE).

## 4 Seams

A part cannot import another part (separate sandboxes until the merge). Where a provision in one part needs the answer of a provision in another, the dependent part takes that answer as an INPUT fact, named for the section it comes from, and the lead wires it at the merge.
List of seams: asking provision, answering provision, and the name and type of the input.
**Which seams were seen only from headings.** The keel read in full only its own ranges (Articles 1 to 4, 111, 113, Annex X). Every provision of another part named in a row was seen only as a title in `HEADINGS.md`, except where the keel's own text cites it: Article 5 (cited by Art 2(12), Art 113(a), Art 111(1) and (2)), Article 6 (Art 2(2), Art 2(13), Art 111(2), Art 113(c)), Articles 9 to 15 and 17 to 25 (Art 2(13)), Article 50 (Art 2(12), Art 111(4)), Articles 57 to 59 and 60a (Art 2(2)), Articles 57 and 60 (Art 3(57)), Articles 4a, 10(5), 59 (Art 2(7)), Article 62(3)(b) (Art 4(2)), Article 97 (Art 2(13)), Annex I Sections A and B (Art 2(2), Art 2(13)), Chapter III Section 2 (Art 3(20), (23), (24)). So the input names in S3, S5, S6, S11 and the asking side of S1, S4 and S12 are the names the keel expects the parts to need, and each part corrects them in its own `NOTES.md` if the text says otherwise; S2, S7, S9, S10 and S13 to S16 are certain on the keel's side.

| # | asking provision | answering provision | input: name (type) | seen from |
| --- | --- | --- | --- | --- |
| S1 | every provision that speaks of high-risk AI systems: Chapter III Sections 1 to 3 (P2, P3), Section 4 and 5 (P4, P5), Articles 60, 60a, 71 (P7), 72, 73, 79 (P8), 80 to 83, 99 (P9) | Article 6 with Annexes I and III (P1) | `the route by which the AI system is high-risk` (`Route to high-risk`: `Route Article 6(1) and Annex I`, `Route Article 6(2) and Annex III`, `Route neither`); the AI system is high-risk iff the route is not `Route neither` | headings and the brief; the core type and Art 113, Art 111(2) are the keel's |
| S2 | every provision that names a role | Article 3 (keel) | none: call `Art 3(3) the party is a provider` and the others of section 3 | the keel's text |
| S3 | Article 99 (P9: penalties) | Article 5 (P1) | `the AI practice is prohibited under Article 5` (`BOOLEAN`) | headings only |
| S4 | Article 99 (P9); Article 2(12) and Article 111(4) (keel, which already take it as an input) | Article 50 (P6) | `the AI system falls under Article 50` (`BOOLEAN`) | the keel's text for 2(12) and 111(4); headings for 99 |
| S5 | Articles 55 (P6), 88 to 94 and 101 (P9) | Article 51 (P6) | `the general-purpose AI model is classified as a general-purpose AI model with systemic risk under Article 51` (`BOOLEAN`) | headings only |
| S6 | Article 16 (P3), Article 71 (P7) | Articles 43, 47, 48, 49 (P5) | `the conformity assessment procedure of Article 43 has been completed`, `the EU declaration of conformity of Article 47 has been drawn up`, `the CE marking of Article 48 has been affixed`, `the AI system has been registered under Article 49` (each `BOOLEAN`) | headings only |
| S7 | Article 3(57) (keel) | Articles 57 and 60 (P7) | `all the conditions laid down in Article 57 or 60 are fulfilled` (`BOOLEAN`; the keel's `Art 3(57)` functions take it) | the keel's text |
| S8 | Article 3(20), (23), (24) (keel: the definitions refer to the requirements of Chapter III Section 2) | Articles 8 to 15 (P2) | `the high-risk AI system complies with the requirements set out in Chapter III, Section 2` (`BOOLEAN`) | the keel's text; the answering Articles from headings |
| S9 | Articles 40 to 42 (P5), 8 to 15 (P2) | Article 3(27), (28) (keel) | `the standard is a harmonised standard as defined in Article 2(1), point (c), of Regulation (EU) No 1025/2012` (`BOOLEAN`, borrowed) | the keel's text |
| S10 | Article 73 (P8: serious incidents) | Article 3(49) (keel) | none: call `Art 3(49) the event is a serious incident` | the keel's text |
| S11 | Articles 80 to 83 (P9) | Article 79 (P8) | `the market surveillance authority has found under Article 79 that the AI system presents a risk` (`BOOLEAN`) | headings only |
| S12 | Articles 62, 63 (P7) and Article 99 (P9: fines for SMEs) | Article 3(14a), (14b) (keel) | `the enterprise is a micro, small or medium-sized enterprise as defined in Article 2 of the Annex to Recommendation 2003/361/EC` (`BOOLEAN`, borrowed), and the SMC fact of (14b) | the keel's text |
| S13 | every part | Articles 111 and 113 (keel) | `the date asked`, `the date the AI system was placed on the market or put into service`, `the AI system has been significantly changed in its design since the date of application of Chapter III` (section 8 gives their exact @desc) | the keel's text |
| S14 | every provision Article 2(2) can cut off: Articles 57 to 59, 60a (P7), Articles 102 to 112 (P9), and any provision of a high-risk system under Article 6(1) with Section B products | Article 2(2) (keel) | the `Article reference` of the provision; the inputs of `Art 2(2) the provision applies to the high-risk AI system under Article 6(1) with Section B products`. Where it answers `JUST FALSE` the part's function answers `JUST FALSE` (a flat "only ... shall apply"); where `NOTHING`, Article 2(2) does not speak and the part answers on its own provision | the keel's text |
| S15 | Articles 9 to 15 and 17 to 25 (P2, P3) | Article 2(13) (keel) | `Art 2(13) the application of the requirement or obligation may be limited`, with the `Article reference` of the requirement | the keel's text |
| S16 | the provisions of Article 5 (P1) that use the terms defined in Art 3(34) to (46) (biometric data to law enforcement), if any (assumed) | Article 3(34) to (46) (keel) | none: call the functions of section 3 | the keel's text; Article 5 from its title only |

## 5 Traps on the stable binary that you met

These are the traps the keel met or designed around; the list is sorted by how they show up. **Silent** failures return a wrong answer with no error; **loud** ones error.

**Silent.**
- **The as-enacted branch can be dead.** A group that applies on or after 27 July 2026 (Chapter III Sections 1 to 3, `General`, `Articles 102 to 110`) never reaches its as-enacted branch through the applicability gate: the text as enacted was replaced before any such group began to apply, so the dispatcher answers `NOTHING` on every date the old text was in force. Only `Chapter I`, `Chapter II` and the 2 August 2025 group can answer from the text as enacted. So keep each text in its own function with no date and no gate, test the old text through it, and let the dispatcher call it (pattern (a), rule 4).
- **`NOTHING` is never `FALSE`.** The applicability function returns `FALSE` for "does not apply on the date asked" (not yet, or saved by Article 111(2)); a layer-1 function turns that into `NOTHING`, never `JUST FALSE` (`NOTES.md`, fork F-111-2-nothing).
- **The applicability function has no "Annex X component" argument.** A component of a large-scale IT system under Annex X is outside Article 111(2) and has its own date (31 December 2030). A part that meets one calls the stand-alone `Art 111(1)` functions as well (fork F-111-annex-x-flag).
- **The route is the keel's enumeration and a system can be both.** A system high-risk under both Article 6(1) and Article 6(2) passes the route the question is about; the keel does not choose (fork F-111-2-date).
- **A trace difference between builds is invisible to `check.sh`.** `#TRACE` prints `FULFILLED` or `BREACH`, never an assertion line. Run each trace on both builds and compare by hand (the keel did, with a `-- EXPECT` comment above each `#TRACE` and a script outside the deposit).
- **`Date` rolls an impossible date forward** (`Date 29 2 2023` is 1 March 2023); `Date 31 6 2026` is 1 July 2026. Write real dates.
- **A date before 1 August 2024 is "as enacted" and "not in force".** `Omnibus Art 4 the version in force` answers `as enacted` for every date before 27 July 2026, including dates before the Regulation existed; `Art 113 the Regulation is in force` is the test for existence, and the applicability function includes it.
- **A mixed-up argument order passes the type checker when two arguments are both `BOOLEAN` or both `DATE`.** Name the inputs in the order of the keel's signatures (section 7) and test one case on each side of every date.

**Loud.**
- `JUST x's field` is read as `(JUST x)'s field`: write `JUST (x's field)`. The error is `check/not-a-function`.
- The list functions are `count`, `any`, `all`, `filter`, `elem`, `map`; there is no `length`.
- `NOT a AND b` parses as `NOT (a AND b)`: parenthesise every `NOT`. Keep each `#ASSERT` on one line. `WAIT UNTIL` is spelled `WAITUNTIL`. `AFTER ... WITHIN` is rejected: write a computed `WITHIN (Day <date>) MINUS (Day <start>)`, which the keel ran and which gives the same trace on both builds.
- No `REFUSE`; no sets; no `TYPICALLY`; no section `GIVEN`; no opaque `DECLARE`; an input named in a `MUST` action degrades on main (use a `PROVIDED` guard); `MAY ... LEST` degrades on main. These are from the brief; the keel did not need them.
- `srcrefs.py check --strict` wants each `@ref` locator directly below its own quote run: a second function under the same article repeats the quote lines (`-- src:N | ...`), or carries an `@ref` with no locator. Quote the as-enacted wording with `quoteid` against `eu-ai-act-2024-1689.txt` (`-- src:eu-ai-act-2024-1689:N | ...`).
- A name defined in two imported modules cannot be used: that is why section 2 prefixes every name.

## 6 One row per part

Ranges are copied unchanged from `inputs/PARTS.md`. "Groups" are the values of `Provision group` the part's provisions fall in (section 3). All parts use `Omnibus Art 4 the version in force`, `Art 113 the provision group applies`, the core's types and the `Art 3(N)` functions of the roles they name.
Which articles are in each part: `HEADINGS.md`. Seams: section 4.

### P1
Ranges: `170-261, 1671-1754`.
Provisions: Article 5 (prohibited AI practices), Article 6 (classification as high-risk), Article 7 (amendments to Annex III), Annexes I, II, III. The title of Annex II says it lists the criminal offences referred to in Article 5(1), first subparagraph, point (h)(iii).
Groups: `Chapter II` for Article 5, except points (ba), (bb) of 5(1) first subparagraph, 5(1a), 5(1b) which are `Article 5 additions`; `Chapter III Sections 1 to 3` for Articles 6 and 7; `General` for Article 6(5); Annex II follows Article 5; Annexes I and III follow Article 6 and are what decide the route.
Expect from the keel: `Route to high-risk` (this part computes it), `Art 3(34)` to `Art 3(46)` (biometric data and identification, publicly accessible space, law enforcement) if Article 5 uses them, `Art 3(9)` to `Art 3(11)` (placing on the market, making available, putting into service), `Art 3(14)` (safety component, both versions: Article 6(1) is about products and safety components), `Art 3(60)` (deep fake).
Seams: provides S1 and S3; takes S16 from the keel.

### P2
Ranges: `156-169, 262-373, 1755-1782`.
Provisions: Article 4a (special categories of personal data for bias detection), Articles 8 to 15 (requirements for high-risk AI systems), Annex IV.
Groups: `Chapter I` for Article 4a; `Chapter III Sections 1 to 3` for Articles 8 to 15; Annex IV follows Article 11.
Expect from the keel: `Art 2(13)` (limiting the application of Articles 9 to 15), `Art 2(2)`, `Art 2(7)` (reserves Article 4a), `Art 3(29)` to `Art 3(33)` (data), `Art 3(34)`, `Art 3(37)`, `Art 3(50)`, `Art 3(27)`, `Art 3(28)`.
Seams: takes S1, S9, S14, S15; provides S8.

### P3
Ranges: `374-526`.
Provisions: Articles 16 to 27 (obligations of providers and deployers of high-risk AI systems and other parties; quality management; documentation; logs; corrective actions; authorised representatives; importers; distributors; responsibilities along the value chain; deployers; fundamental rights impact assessment).
Groups: `Chapter III Sections 1 to 3`.
Expect from the keel: `Art 3(3)` to `Art 3(8)` (roles), `Art 3(23)` (substantial modification), `Art 3(15)` (instructions for use), `Art 2(13)`, `Art 3(24)`, `Art 3(25)`.
Seams: takes S1, S6, S8, S14, S15; the seats provider, deployer, importer, distributor, rep, manufacturer, person all appear here.

### P4
Ranges: `527-635, 1800-1839, 1958-2010`.
Provisions: Articles 28 to 39 (notifying authorities and notified bodies), Annex VII, Annex XIV.
Groups: `Notified bodies, GPAI, governance, penalties and Art 78` for Articles 28 to 39; the Annexes follow the Article that gives them effect.
Expect from the keel: `Art 3(19)` to `Art 3(22)` (notifying authority, conformity assessment, body, notified body), `Art 3(26)`, `Art 3(48)`.
Seams: takes S1 where the text speaks of high-risk systems; provides what Article 43 needs (S6 is asked of P5).

### P5
Ranges: `636-748, 1783-1799, 1840-1886`.
Provisions: Articles 40 to 49 (standards, conformity assessment, certificates, registration), Annexes V, VI, VIII, IX.
Groups: `General` for Articles 40 to 49 (Chapter III Section 5 is not dated by any point of Article 113 as amended, so the second paragraph's general date reaches it: assumed, see fork F-113-groups); Annexes follow Articles 47, 43, 49.
Expect from the keel: `Art 3(20)`, `Art 3(24)`, `Art 3(27)`, `Art 3(28)`, `Art 3(22)`, `Art 3(23)`.
Seams: provides S6; takes S1, S9.

### P6
Ranges: `749-842, 1908-1957`.
Provisions: Article 50 (transparency obligations), Articles 51 to 56 (general-purpose AI models), Annexes XI, XII, XIII.
Groups: `General` for Article 50; `Notified bodies, GPAI, governance, penalties and Art 78` for Articles 51 to 56; Annexes XI and XII follow Article 53(1), points (a) and (b) (their titles say so), Annex XIII follows the Article its title refers to (cut off in `HEADINGS.md`).
Expect from the keel: `Art 3(60)` (deep fake), `Art 3(63)` to `Art 3(68)` (general-purpose AI), `Art 3(67)`, the `AI model` record, `Art 111(3)` (models placed before 2 August 2025), `Art 111(4)` (synthetic content, Article 50(2)).
Seams: provides S4 and S5; takes S13 (placement date of a model).
The core's `AI model` record has the compute field Article 51 needs; the 10^25 threshold is for the part to encode (see `eu-ai-act-2024-1689.formulas.md`).

### P7
Ranges: `843-1112`.
Provisions: Articles 57 to 63 (sandboxes, real-world testing, measures for SMEs; including 60a), Articles 64 to 70 (governance: the Board, advisory forum, scientific panel, national competent authorities), Article 71 (EU database).
Groups: `General` for Articles 57 to 63 and 71; `Notified bodies, GPAI, governance, penalties and Art 78` for Articles 64 to 70.
Expect from the keel: `Art 3(53)` to `Art 3(59)` (plans, sandbox, real-world testing, subject, informed consent), `Art 3(14a)`, `Art 3(14b)`, `Art 2(2)` (Articles 57 to 59, 60a are on its list), `Art 3(47)`, `Art 3(48)`.
Seams: provides S7; takes S1, S6, S12, S14.

### P8
Ranges: `1113-1313`.
Provisions: Articles 72 to 79 (post-market monitoring, serious incidents, enforcement, market surveillance, the AI Office's powers (75a to 75d), testing supervision, powers of authorities protecting fundamental rights, confidentiality, national-level procedure).
Groups: `General` for Articles 72 to 77 and 79, including 75a to 75d; `Notified bodies, GPAI, governance, penalties and Art 78` for Article 78.
Expect from the keel: `Art 3(49)` (serious incident), `Art 3(25)` (post-market monitoring system), `Art 3(26)`, `Art 3(19)`, `Art 3(48)`, `Art 3(16)`, `Art 3(17)` (recall, withdrawal), `Art 3(38)` (sensitive operational data).
Seams: provides S11; takes S1, S10.

### P9
Ranges: `1314-1617, 1628-1653`.
Provisions: Articles 80 to 98 (procedures, remedies, right to explanation, supervision of general-purpose AI providers, codes of conduct, guidelines, delegation, committee), Articles 99 to 101 (penalties and fines), Articles 102 to 110 (amendments of other acts), Article 112 (evaluation and review).
Groups: `General` for Articles 80 to 98, 101 and 112; `Notified bodies, GPAI, governance, penalties and Art 78` for Articles 99 and 100; `Articles 102 to 110` for 102 to 110.
Expect from the keel: `Art 3(61)` (widespread infringement), `Art 3(14a)`, `Art 3(14b)` (SME fines), `Art 3(65)` (systemic risk), `Art 2(2)` (Articles 102 to 112 are on its list as amended).
Seams: takes S1, S3, S4, S5, S11 and the infringement inputs; provides none.

## 7 The time axis

**The dates** (each is a constant in `aia-timeline.l4`, copied from the text with its quote line; `aia-timeline-tests.l4` has a case on each side of each).

| date | what it is | name in `aia-timeline.l4` | text |
| --- | --- | --- | --- |
| 12.7.2024 | publication of the Regulation | `Art 113 the Regulation was published` | consolidated line 4 |
| 1.8.2024 | entry into force of the Regulation: publication plus 20 days | `Art 113 the Regulation enters into force` | line 1656 |
| 2.2.2025 | Chapters I and II apply | `Art 113(a) Chapters I and II apply from` | line 1660 |
| 2.8.2025 | Chapter III Section 4, Chapters V, VII, XII except Article 101, and Article 78 apply | `Art 113(b) ...` | line 1662 |
| 24.7.2026 | publication of the Omnibus | `Omnibus Art 4 the Omnibus was published` | line 9 |
| 27.7.2026 | entry into force of the Omnibus: publication plus 3 days; Articles 102 to 110 apply; the text as amended begins | `Omnibus Art 4 the Omnibus enters into force`, `Art 113(d) ...` | Omnibus line 764; line 1668 |
| 2.8.2026 | the general date of application; as enacted, the date before which a placed system is saved by Article 111(2) | `Art 113 second paragraph the general date of application`, `Art 111(2) as enacted the date before which a placed system is saved` | lines 1657; base line 2159 |
| 2.12.2026 | the Article 5 additions apply; Article 111(4)'s deadline | `Art 113(a) the Article 5 additions apply from` | lines 1660, 1627 |
| 2.8.2027 | as enacted, Article 6(1) and the corresponding obligations; the placement bound of Article 111(1); Article 111(3)'s deadline; the Commission's delegated acts (Article 2(13)) | `Art 113(c) as enacted Article 6(1) and the corresponding obligations apply from` | base line 2206; lines 1620, 1625, 58-61 |
| 2.12.2027 | Chapter III Sections 1 to 3 apply to a system high-risk under Article 6(2) and Annex III | `Art 113(c)(i) ...` | line 1664-1666 |
| 2.8.2028 | the same, under Article 6(1) and Annex I | `Art 113(c)(ii) ...` | line 1664-1666 |
| 2.8.2030 | Article 111(2): high-risk systems intended for public authorities | `Art 111(2) ... must comply` | line 1623 |
| 31.12.2030 | Article 111(1): components of Annex X systems | `Art 111(1) the date by which the AI system must be brought into compliance` | line 1620 |

**The version function** (one):

```
GIVEN `the date asked` IS A DATE
GIVETH A `Version of the Regulation`
`Omnibus Art 4 the version in force`
```
Answers `as enacted` before 27.7.2026 and `as amended` from then.

**The applicability function** (one):

```
GIVEN `the provision group` IS A `Provision group`
      `the date asked` IS A DATE
      `the route to high-risk` IS A `Route to high-risk`
      `the date the AI system was placed on the market or put into service` IS A DATE
      `the AI system has been significantly changed in its design since the date of application of Chapter III` IS A BOOLEAN
GIVETH A BOOLEAN
`Art 113 the provision group applies`
```
`TRUE` only if the Regulation is in force on the date asked, the group's date of application has come (for the group and route, in the version in force), and Article 111(2) does not save the system.
For a question that is not about one AI system pass `` `the route to pass when no AI system is in question` ``, `` `the date to pass when no AI system is in question` `` and `FALSE` (the core's constants): for every group except `Chapter III Sections 1 to 3` the answer then depends only on the date asked. For `Chapter III Sections 1 to 3` the route is needed (no route, no date).
A `FALSE` means "does not apply on the date asked"; the caller answers `NOTHING`, never `JUST FALSE`.

**The stand-alone rules of Article 111** (each a date function and a regulative rule; each takes `the date asked` first; they answer `NOTHING` or `FULFILLED` where nothing is owed):
- `Art 111(1) the date by which the AI system must be brought into compliance` (`the date asked`, the placement date, `the AI system is a component of a large-scale IT system established by a legal act listed in Annex X`) gives `MAYBE DATE`; the rule `Art 111(1) the duty to bring the AI system into compliance` has the same arguments and is `PARTY Operator`. The second subparagraph: `Art 111(1) the requirements of this Regulation are to be taken into account in the evaluation`.
- `Art 111(2) the date by which providers and deployers of high-risk AI systems intended for public authorities must comply` (`the date asked`, `the AI system is a high-risk AI system intended to be used by public authorities`); the rules `Art 111(2) the provider's duty to take the necessary steps` and `Art 111(2) the deployer's duty to take the necessary steps`. Its first sentence is in the applicability function.
- `Art 111(3) the date by which the provider of a general-purpose AI model already on the market must comply` (`the date asked`, `the date the general-purpose AI model was placed on the market`); the rule `Art 111(3) the duty of the provider of a general-purpose AI model already on the market`.
- `Art 111(4) the date by which the provider of an AI system generating synthetic content must comply with Article 50(2)` (as amended only; `the date asked`, the placement date, `the AI system generates synthetic audio, image, video or text content`); the rule `Art 111(4) the duty of the provider of an AI system generating synthetic content`.
A regulative rule's deadline is a computed `WITHIN (Day <deadline>) MINUS (Day <start>)`, and its trace clock is a day number: `AT (Day (Date 2 8 2027))`.

**Three worked patterns, run on the stable binary.** Each is a file in the deposit that `check.sh` runs on both builds (pattern (a): 14 assertions satisfied; pattern (b): 6 traces, compared by hand on both builds, 3 reach `BREACH`; pattern (c): 11 assertions satisfied). The provision is fictitious (`Art N(1)`, `Art N(2)`); copy the shape, give it your provision's own label, and quote the real text above each branch (the as-enacted branch quotes the base file with `quoteid`).

**(a) A layer-1 decision function gated by applicability and dispatching on version, with a test** (`aia-pattern-a-decision.l4`):

```
§ `Step 1: each text in its own function`

-- VERSION as enacted. Fictitious text: "The provider of a high-risk AI system shall have registered the system."
GIVEN `the provider has registered the AI system` IS A BOOLEAN
GIVETH A BOOLEAN
`Art N(1) as enacted the provider has met the duty to register` MEANS
    `the provider has registered the AI system`
    -- FALSE-kind (the text says no in its own words): "The provider of a high-risk AI system shall have registered the system" (a bare "shall" not done, taken case by case)

-- VERSION as amended. Fictitious text: the same, "except for a micro, small or medium-sized enterprise".
GIVEN `the provider has registered the AI system` IS A BOOLEAN
      `the provider is a micro, small or medium-sized enterprise` IS A BOOLEAN
GIVETH A BOOLEAN
`Art N(1) as amended the provider has met the duty to register` MEANS
    `the provider has registered the AI system` OR `the provider is a micro, small or medium-sized enterprise`
    -- FALSE-kind (the text says no in its own words): "shall have registered the system, except for a micro, small or medium-sized enterprise"

§ `Step 2: the dispatcher, gated by Art 113 (with Art 111(2)) and dispatching on the version`

-- The provision group the provision belongs to (here Chapter III Sections 1 to 3: the date depends on the route), the date asked, the route to
-- high-risk, the date the system was placed on the market or put into service, and whether it has been significantly changed in its design,
-- go to the keel's applicability function. A provision outside Chapter III passes `Route neither` and the core's two constants.
GIVEN `the date asked` IS A DATE
      `the route to high-risk` IS A `Route to high-risk`
      `the date the AI system was placed on the market or put into service` IS A DATE
      `the AI system has been significantly changed in its design since the date of application of Chapter III` IS A BOOLEAN
      `the provider has registered the AI system` IS A BOOLEAN
      `the provider is a micro, small or medium-sized enterprise` IS A BOOLEAN
GIVETH A MAYBE BOOLEAN
`Art N(1) the provider has met the duty to register` MEANS
    IF NOT (`Art 113 the provision group applies` `Chapter III Sections 1 to 3` `the date asked` `the route to high-risk` `the date the AI system was placed on the market or put into service` `the AI system has been significantly changed in its design since the date of application of Chapter III`)
    THEN NOTHING  -- NOTHING-kind (limited by its own wording): the group applies from the date Art 113(c) gives, and Art 111(2) saves a system placed earlier and not significantly changed
    ELSE CONSIDER `Omnibus Art 4 the version in force` `the date asked`
         WHEN `as enacted` THEN JUST (`Art N(1) as enacted the provider has met the duty to register` `the provider has registered the AI system`)  -- VERSION as enacted
         WHEN `as amended` THEN JUST (`Art N(1) as amended the provider has met the duty to register` `the provider has registered the AI system` `the provider is a micro, small or medium-sized enterprise`)  -- VERSION as amended

§ `Tests: a case before, on and after the application date, and one on each side of 27 July 2026`

`the Annex III route` MEANS `Route Article 6(2) and Annex III`

-- Chapter III Sections 1 to 3 apply to an Annex III system from 2 December 2027 (Art 113(c)(i)). Placed on 2 December 2027, so Art 111(2) saves nothing.
-- args: date asked, route, date placed, significantly changed, registered, SME
#ASSERT `Art N(1) the provider has met the duty to register` (Date 1 12 2027) `the Annex III route` (Date 2 12 2027) FALSE FALSE FALSE EQUALS NOTHING
#ASSERT `Art N(1) the provider has met the duty to register` (Date 2 12 2027) `the Annex III route` (Date 2 12 2027) FALSE TRUE FALSE EQUALS JUST TRUE
#ASSERT `Art N(1) the provider has met the duty to register` (Date 2 12 2027) `the Annex III route` (Date 2 12 2027) FALSE FALSE FALSE EQUALS JUST FALSE
#ASSERT `Art N(1) the provider has met the duty to register` (Date 3 12 2027) `the Annex III route` (Date 2 12 2027) FALSE FALSE FALSE EQUALS JUST FALSE
-- As amended, the invented exemption holds.
#ASSERT `Art N(1) the provider has met the duty to register` (Date 2 12 2027) `the Annex III route` (Date 2 12 2027) FALSE FALSE TRUE EQUALS JUST TRUE
-- Art 111(2): a system placed before the date of application and not significantly changed is saved, so the answer is NOTHING; changed, it is covered.
#ASSERT `Art N(1) the provider has met the duty to register` (Date 2 12 2030) `the Annex III route` (Date 1 1 2027) FALSE TRUE FALSE EQUALS NOTHING
#ASSERT `Art N(1) the provider has met the duty to register` (Date 2 12 2030) `the Annex III route` (Date 1 1 2027) TRUE TRUE FALSE EQUALS JUST TRUE
-- Not a high-risk system: no date for Chapter III Sections 1 to 3 (NOTHING-kind, silent).
#ASSERT `Art N(1) the provider has met the duty to register` (Date 2 12 2030) `Route neither` (Date 1 1 2027) FALSE TRUE FALSE EQUALS NOTHING
-- Each side of 27 July 2026: the version in force changes, and the dispatcher answers NOTHING on both, because the group is not yet applicable (the trap, rule 4).
#ASSERT `Art N(1) the provider has met the duty to register` (Date 26 7 2026) `the Annex III route` (Date 2 12 2027) FALSE TRUE FALSE EQUALS NOTHING
#ASSERT `Art N(1) the provider has met the duty to register` (Date 27 7 2026) `the Annex III route` (Date 2 12 2027) FALSE TRUE FALSE EQUALS NOTHING
-- So the text as enacted is tested through its own function (rule 1), and so is the text as amended.
#ASSERT `Art N(1) as enacted the provider has met the duty to register` TRUE
#ASSERT NOT (`Art N(1) as enacted the provider has met the duty to register` FALSE)
#ASSERT `Art N(1) as amended the provider has met the duty to register` FALSE TRUE
#ASSERT NOT (`Art N(1) as amended the provider has met the duty to register` FALSE FALSE)
-- The two texts differ for an unregistered SME (the three assertions above): as enacted FALSE, as amended TRUE. That is the whole point of keeping both.
```

**(b) A regulative rule gated the same way, with a `#TRACE` that reaches `BREACH`** (`aia-pattern-b-regulative.l4`):

```
DECLARE `Art N(2) act` IS ONE OF
    `Art N(2) register the AI system`

§ `The rule`

GIVEN `the date asked` IS A DATE
      `the route to high-risk` IS A `Route to high-risk`
      `the date the AI system was placed on the market or put into service` IS A DATE
      `the AI system has been significantly changed in its design since the date of application of Chapter III` IS A BOOLEAN
GIVETH A DEONTIC Role `Art N(2) act`
`Art N(2) the provider's duty to register the AI system` MEANS
    IF NOT (`Art 113 the provision group applies` `Chapter III Sections 1 to 3` `the date asked` `the route to high-risk` `the date the AI system was placed on the market or put into service` `the AI system has been significantly changed in its design since the date of application of Chapter III`)
    THEN FULFILLED  -- nothing is owed: the group does not apply on the date asked, or Art 111(2) saves the system
    ELSE CONSIDER `Omnibus Art 4 the version in force` `the date asked`
         WHEN `as enacted` THEN                                                  -- VERSION as enacted (fictitious: 15 days)
             PARTY Provider
             MUST `Art N(2) register the AI system`
             WITHIN 15
             HENCE FULFILLED
             LEST BREACH BY Provider BECAUSE "the AI system was not registered within 15 days"
         WHEN `as amended` THEN                                                  -- VERSION as amended (fictitious: 30 days)
             PARTY Provider
             MUST `Art N(2) register the AI system`
             WITHIN 30
             HENCE FULFILLED
             LEST BREACH BY Provider BECAUSE "the AI system was not registered within 30 days"

§ `Traces: the breach path, on the days either side of the deadline`

`the Annex III route` MEANS `Route Article 6(2) and Annex III`

-- Applicable (2 December 2027, Annex III route, placed on 2 December 2027), the text as amended (30 days). The duty arises on day 0.
-- EXPECT FULFILLED
#TRACE `Art N(2) the provider's duty to register the AI system` (Date 2 12 2027) `the Annex III route` (Date 2 12 2027) FALSE AT 0 WITH
    PARTY Provider DOES `Art N(2) register the AI system` AT 30
-- EXPECT BREACH
#TRACE `Art N(2) the provider's duty to register the AI system` (Date 2 12 2027) `the Annex III route` (Date 2 12 2027) FALSE AT 0 WITH
    PARTY Provider DOES `Art N(2) register the AI system` AT 31
-- EXPECT BREACH
#TRACE `Art N(2) the provider's duty to register the AI system` (Date 2 12 2027) `the Annex III route` (Date 2 12 2027) FALSE AT 0 WITH
    WAITUNTIL 31
-- Not yet applicable (the day before the group applies): nothing is owed, so even a long wait does not breach.
-- EXPECT FULFILLED
#TRACE `Art N(2) the provider's duty to register the AI system` (Date 1 12 2027) `the Annex III route` (Date 2 12 2027) FALSE AT 0 WITH
    WAITUNTIL 400
-- Saved by Art 111(2): placed before the date of application and not significantly changed. Nothing is owed.
-- EXPECT FULFILLED
#TRACE `Art N(2) the provider's duty to register the AI system` (Date 2 12 2030) `the Annex III route` (Date 1 1 2027) FALSE AT 0 WITH
    WAITUNTIL 400
-- The same system after a significant change in its design: the duty arises, and a missed deadline is a breach.
-- EXPECT BREACH
#TRACE `Art N(2) the provider's duty to register the AI system` (Date 2 12 2030) `the Annex III route` (Date 1 1 2027) TRUE AT 0 WITH
    WAITUNTIL 31
```

**(c) A seat question that takes `the date asked` and its @desc, and the applicability question for a provision group** (`aia-pattern-c-seat.l4`; it imports pattern (a) as a real seat imports the part's layer-1 module):

```
§ `Under Article N(1): the seat's question about the duty`

-- Article N(1) (fictitious). The duty to have registered an AI system, as the text stands on the date asked.
@export Under Article N(1), as a provider of an AI system, have I met the duty to register the AI system?
GIVEN `the date asked` IS A DATE @desc On what date do you want the answer? Give today's date for the Regulation as it stands today, or an earlier or later date for the Regulation as it stood or will stand then.
      `the route by which the AI system is high-risk` IS A `Route to high-risk` @desc Is the AI system high-risk because of Article 6(1) with Annex I, because of Article 6(2) with Annex III, or neither?
      `the date the AI system was placed on the market or put into service` IS A DATE @desc On what date was the AI system first placed on the market or put into service in the Union? If that has not happened yet, give the date you expect.
      `the AI system has been significantly changed in its design since the date of application of Chapter III` IS A BOOLEAN @desc Since the date from which Chapter III of the Regulation applies to your AI system, has its design been significantly changed? Answer no if you do not know of a significant change.
      `the AI system is registered` IS A BOOLEAN @desc Have you registered the AI system?
      `I am a micro, small or medium-sized enterprise` IS A BOOLEAN @desc Is your organisation a micro, small or medium-sized enterprise?
GIVETH A MAYBE BOOLEAN
DECIDE `Under Article N(1), as a provider of an AI system, have I met the duty to register the AI system` IS
    `Art N(1) the provider has met the duty to register` `the date asked` `the route by which the AI system is high-risk` `the date the AI system was placed on the market or put into service` `the AI system has been significantly changed in its design since the date of application of Chapter III` `the AI system is registered` `I am a micro, small or medium-sized enterprise`

§ `Under Article 113: the applicability question for a provision group`

-- One question for each provision group of the part's range, for each seat the group addresses. The group here is Chapter III Sections 1 to 3.
@export Under Article 113, as a provider of an AI system, does Chapter III Sections 1 to 3 apply on the date asked?
GIVEN `the date asked` IS A DATE @desc On what date do you want the answer? Give today's date for the Regulation as it stands today, or an earlier or later date for the Regulation as it stood or will stand then.
      `the route by which the AI system is high-risk` IS A `Route to high-risk` @desc Is the AI system high-risk because of Article 6(1) with Annex I, because of Article 6(2) with Annex III, or neither?
      `the date the AI system was placed on the market or put into service` IS A DATE @desc On what date was the AI system first placed on the market or put into service in the Union? If that has not happened yet, give the date you expect.
      `the AI system has been significantly changed in its design since the date of application of Chapter III` IS A BOOLEAN @desc Since the date from which Chapter III of the Regulation applies to your AI system, has its design been significantly changed? Answer no if you do not know of a significant change.
GIVETH A MAYBE BOOLEAN
DECIDE `Under Article 113, as a provider of an AI system, does Chapter III Sections 1 to 3 apply on the date asked` IS
    JUST (`Art 113 the provision group applies` `Chapter III Sections 1 to 3` `the date asked` `the route by which the AI system is high-risk` `the date the AI system was placed on the market or put into service` `the AI system has been significantly changed in its design since the date of application of Chapter III`)

-- A group that has no route (Chapter I, Chapter II, the 2 August 2025 group, the General group) takes no route, no placement date and no change:
-- the question passes the core's constants, and the seat does not ask for them.
@export Under Article 113, as a provider of an AI system, does Chapter I apply on the date asked?
GIVEN `the date asked` IS A DATE @desc On what date do you want the answer? Give today's date for the Regulation as it stands today, or an earlier or later date for the Regulation as it stood or will stand then.
GIVETH A MAYBE BOOLEAN
DECIDE `Under Article 113, as a provider of an AI system, does Chapter I apply on the date asked` IS
    JUST (`Art 113 the provision group applies` `Chapter I` `the date asked` `the route to pass when no AI system is in question` `the date to pass when no AI system is in question` FALSE)

§ `Cases (a Pn-cases-seat-provider.l4 file would hold these): the facts a real provider would state`

`the route Annex III` MEANS `Route Article 6(2) and Annex III`

-- The duty, before and on the day Chapter III Sections 1 to 3 begin to apply to an Annex III system (2 December 2027).
#ASSERT `Under Article N(1), as a provider of an AI system, have I met the duty to register the AI system` (Date 1 12 2027) `the route Annex III` (Date 2 12 2027) FALSE TRUE FALSE EQUALS NOTHING
#ASSERT `Under Article N(1), as a provider of an AI system, have I met the duty to register the AI system` (Date 2 12 2027) `the route Annex III` (Date 2 12 2027) FALSE TRUE FALSE EQUALS JUST TRUE
#ASSERT `Under Article N(1), as a provider of an AI system, have I met the duty to register the AI system` (Date 2 12 2027) `the route Annex III` (Date 2 12 2027) FALSE FALSE FALSE EQUALS JUST FALSE
-- The applicability question on each side of 2 December 2027, for the Annex III route; and for the Annex I route, whose date is 2 August 2028.
#ASSERT `Under Article 113, as a provider of an AI system, does Chapter III Sections 1 to 3 apply on the date asked` (Date 1 12 2027) `the route Annex III` (Date 2 12 2027) FALSE EQUALS JUST FALSE
#ASSERT `Under Article 113, as a provider of an AI system, does Chapter III Sections 1 to 3 apply on the date asked` (Date 2 12 2027) `the route Annex III` (Date 2 12 2027) FALSE EQUALS JUST TRUE
#ASSERT `Under Article 113, as a provider of an AI system, does Chapter III Sections 1 to 3 apply on the date asked` (Date 2 12 2027) `Route Article 6(1) and Annex I` (Date 2 12 2027) FALSE EQUALS JUST FALSE
#ASSERT `Under Article 113, as a provider of an AI system, does Chapter III Sections 1 to 3 apply on the date asked` (Date 2 8 2028) `Route Article 6(1) and Annex I` (Date 2 8 2028) FALSE EQUALS JUST TRUE
-- Saved by Art 111(2) (placed earlier, unchanged): the group does not apply to this system; changed, it does.
#ASSERT `Under Article 113, as a provider of an AI system, does Chapter III Sections 1 to 3 apply on the date asked` (Date 2 12 2030) `the route Annex III` (Date 1 1 2027) FALSE EQUALS JUST FALSE
#ASSERT `Under Article 113, as a provider of an AI system, does Chapter III Sections 1 to 3 apply on the date asked` (Date 2 12 2030) `the route Annex III` (Date 1 1 2027) TRUE EQUALS JUST TRUE
-- Chapter I, on each side of 2 February 2025.
#ASSERT `Under Article 113, as a provider of an AI system, does Chapter I apply on the date asked` (Date 1 2 2025) EQUALS JUST FALSE
#ASSERT `Under Article 113, as a provider of an AI system, does Chapter I apply on the date asked` (Date 2 2 2025) EQUALS JUST TRUE
```

## 8 The seat layer

**The nine seats and their slugs**: a person affected by an AI system [person]; a provider of an AI system (in particular of a high-risk AI system) [provider]; a deployer of an AI system [deployer]; an importer [importer]; a distributor [distributor]; an authorised representative of a provider [rep]; a product manufacturer that places an AI system on the market together with its product [manufacturer]; a provider of a general-purpose AI model (with or without systemic risk) [gpai]; a notified body [notified].
There is never a seat for the Commission, the AI Office, the AI Board, the scientific panel, a market surveillance authority, a notifying authority or any other official: their powers and duties appear only as what they mean to one of the nine.
A provision belongs to a seat only when the text addresses that role. A person may hold several roles; each seat asks the facts that role could state.

**File names**: `Pn-seat-<slug>.l4` and `Pn-cases-seat-<slug>.l4` for each seat the part's ranges address (slugs as above). A seat module imports the part's layer-1 modules and the keel's, calls their functions, and never restates a rule. Each question has `@export` and `@desc` and is grouped under `§` headings in the text's order.

**The question-name form**: `Under Article N, as <role phrase>, ...` (for an Annex, `Under Annex N point M, as ...`). The role phrases, to be written exactly (lower case after "as"):

| seat | role phrase |
| --- | --- |
| person | `as a person affected by an AI system,` |
| provider | `as a provider of an AI system,` |
| deployer | `as a deployer of an AI system,` |
| importer | `as an importer,` |
| distributor | `as a distributor,` |
| rep | `as an authorised representative,` |
| manufacturer | `as a product manufacturer,` |
| gpai | `as a provider of a general-purpose AI model,` |
| notified | `as a notified body,` |

A question's name asks the question its body answers, in the same direction. No two seats, no two parts and no two questions may share a name.
**The applicability question** (one for each provision group of the part's range and each seat the group addresses): `Under Article N, as <role phrase>, does <group> apply on the date asked?`, where N is the first Article of the part's range that falls in that group (or `Annex N point M` if the part has only an Annex in the group), so that two parts never write the same name. It answers `JUST TRUE` or `JUST FALSE` from `Art 113 the provision group applies`. (Pattern (c) uses `Article 113` because the keel is the author.)

**The three shared inputs, with the same name and the same @desc in every question of every seat** (exactly as pattern (c) writes them):
- `the date asked` is a `DATE`. @desc: *On what date do you want the answer? Give today's date for the Regulation as it stands today, or an earlier or later date for the Regulation as it stood or will stand then.*
- `the date the AI system was placed on the market or put into service` is a `DATE`. @desc: *On what date was the AI system first placed on the market or put into service in the Union? If that has not happened yet, give the date you expect.* (For a general-purpose AI model: `the date the general-purpose AI model was placed on the market`, @desc *On what date was the general-purpose AI model first placed on the market in the Union?*)
- `the AI system has been significantly changed in its design since the date of application of Chapter III` is a `BOOLEAN`. @desc: *Since the date from which Chapter III of the Regulation applies to your AI system, has its design been significantly changed? Answer no if you do not know of a significant change.*
- `the route by which the AI system is high-risk` is a `Route to high-risk` (an enumeration: one of the keel's own choices). @desc: *Is the AI system high-risk because of Article 6(1) with Annex I, because of Article 6(2) with Annex III, or neither?*
A question about a provision of a group other than `Chapter III Sections 1 to 3` asks only `the date asked` (and, where Article 111 applies, the other two); it passes the core's constants for the route and placement date. A question whose function takes the route asks `the route by which the AI system is high-risk`.

**The shared way a seat states the role facts.** A seat module assumes its role: the person asking holds it. The role facts are asked once, in a question of their own that calls the keel's definition, and the other questions do not re-ask them:

| seat | the role question calls | facts a person could state |
| --- | --- | --- |
| provider | `Art 3(3) the party is a provider` | develops or has developed an AI system or model; places it on the market or puts it into service under its own name or trademark |
| deployer | `Art 3(4) the party is a deployer` | uses an AI system under its authority; not in a personal non-professional activity |
| importer | `Art 3(6) the party is an importer` | place; places on the market an AI system bearing a third-country name or trademark |
| distributor | `Art 3(7) the party is a distributor` | in the supply chain; not provider or importer; makes the AI system available on the Union market |
| rep | `Art 3(5) the party is an authorised representative` | place; written mandate received and accepted |
| manufacturer | `Art 2(1)(e) the Regulation applies to the product manufacturer` | places an AI system on the market together with its product under its own name |
| gpai | `Art 3(3) the party is a provider` with the model facts, then `Art 3(63)` | develops a general-purpose AI model; places it on the market |
| notified | `Art 3(22) the body is a notified body` | conformity assessment body; notified under this Regulation |
| person | `Art 2(1)(g) the Regulation applies to the affected person in the Union` | affected person; located in the Union |

Each such question is named `Under Article 3, as <role phrase>, ...` or `Under Article 2, as <role phrase>, ...` and belongs to the keel's scope; a part that needs it writes its own with its own Article number and calls the same function.
Question inputs are plain: a yes/no, a date, a number, or one of the keel's own choices. A seat builds any record the function expects inside the question, in a `WHERE`, from the answers.

**How a seat takes a seam input.** As a plain input named for the section it comes from (section 4), with an @desc that asks the question in the seat's words. The classification seam (S1) is not a yes/no: ask `the route by which the AI system is high-risk`, the keel's enumeration. A `BOOLEAN` seam is asked like this: `` `the conformity assessment procedure of Article 43 has been completed` IS A BOOLEAN @desc Has the conformity assessment procedure of Article 43 been completed for your AI system? ``.

**Mirror cases.** Where two seats are asked the same relation (a provider's duty and the importer's check of it; a deployer's duty and the affected person's right), write the same facts asked from both seats, with answers that agree, in the case files, marked `-- MIRROR`.

## 9 Rules with no breach path and the split sites

Restated from the brief; each part writes these sections in its own `NOTES.md`, with these headings. The keel's own are in `NOTES.md` as the model.

- **`## Coverage table`**: every provision of the part's ranges has a row with exactly one disposition: `encoded` (a rule, definition or table in layer 1, with a test, citing the provision with `@ref`), `inert` (only for: 1 not operative; 2 machinery; 3 text shown repealed or blank), `fork` (the row points at the fork-register entry and at the rule that encodes the chosen reading, or at the explicit "not covered" value), or `repealed or blank in this text`. There is no `out-of-scope` and no `deferred` row. These are not reasons for `inert`: "addresses an official"; "an interpretive canon" or "open-textured"; "refers to another instrument that is not among the sources"; "no input from which an answer would differ"; "the earlier brief said it need not be coded". Keep it on disk and update it after each section.
- **`## Fork register`**: one entry per site where the text reads two or more ways with different outcomes: the provision, the function, the answer taken, the other reading, the text that licenses each.
- **`## Jural relations`**: a table with one row per provision that creates a relation, giving the party holding the right, privilege, power or immunity, the party bearing the correlative duty, no-right, liability or disability, the section, and the L4 rule; a provision that creates none (a definition, a counting rule) is listed once as `none`. State each relation once, neutrally, never from both sides.
- **`### Reading a result: FALSE and NOTHING`** (under the fork register or in its own section): what a "no" is in the part's rows, and what "not covered" is. `JUST FALSE`, or a constructor meaning "the text says no", only where the text says no in its own words (a definition that says "means"; a condition introduced by "if", "only if", "as long as" or "unless" and their plain variants; a list closed with "only"; a flat negative). Everywhere else `NOTHING` or a named "... not covered" constructor: the text lists without closing, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside it. Before a provision applies the function answers `NOTHING`. Every "no" branch carries `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`; every "not covered" branch carries `-- NOTHING-kind (<why>)` with <why> one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- **`## Marginal readings for a lawyer`**: every branch that rests on reading (a) (a failed "if" counts as the text's no, clause by clause, within the provision that holds it; flat negatives count as the text saying no) or reading (b) (a prohibition or grant limited by its own wording does not), with the other reading stated.
- **`## Split sites (your part)`**: count the sites of (i) an unmet element of an infringement (`JUST FALSE` or `NOTHING`?) and (ii) a "may" gated by "where", "when", "upon", "on application", "with the consent of" and the like (`JUST FALSE`, the periods ruling's rule (b), or `NOTHING`, the grant ruling?), with the answer taken at each, and point at each fork line. The Guide's rulings of 2026-11-05 and 2026-11-12 govern what they cover; decide the rest site by site on the text's own words and do not change an answer to match another part. The keel's count: (i) 0 sites, (ii) 1 site (Article 2(13), fork F-2-13, answer `JUST FALSE`).
- **`## Rules with no breach path (your part)`**: every regulative rule that is a `MUST` with no time limit and no stated consequence (no trace can show it breached: a late action reads `FULFILLED`), with its provision. Do not invent a deadline or a consequence the text does not state. For every other rule write at least one `#TRACE` that reaches `BREACH` (a prohibition: a trace in which the forbidden act occurs; a duty with a time limit or consequence: a trace in which it is missed), and compare each trace on both builds by hand.
- **`## What the stable binary does not accept`** (a finding): where the skills describe a construct the stable binary rejects, the binary governs; list what you met.
- A status header saying how each kind of claim was verified; the statement that the consolidated text is a rendering with no legal effect; commencement IN, assumed, not ruled; the seat layer's description.
