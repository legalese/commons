# Telecommunications Act 1997, Part 19 — baseline encoding, the seat of the person or business wanting a connection

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill (regulative rules for the duties the Part states).
There is no REFUSE in it. Where the Part gives no answer the encoding says so in the answer's own words (a pending area has no provider; no request has been made yet), and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0092` in `subjects/au/requirements.jsonl`. There was no earlier encoding of this Act to keep. It is scoped to Part 19; the rest of the Act is not encoded.

There are 11 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the order a person meets them (does this count as broadband; who is my provider; am I entitled; how long; what terms; voice; if my provider can no longer serve my area; damages).

**Regulative rules.** Part 19 states duties with deadlines, so three rules are written as `PARTY … MUST … WITHIN … HENCE … LEST BREACH … BECAUSE`, and the seat questions that give numbers read the same named periods:

| Rule | Parties | Clock | Seat questions reading the same definitions |
|---|---|---|---|
| `s 360P(1), (11A), (12) -- the provider must answer my retailer's request, connect me or give reasons, and my retailer must pass the reasons on` | the statutory infrastructure provider, then (on a refusal) my carriage service provider | business days from receipt of the request | `How many business days does the provider have to answer` (`the period to answer`); `How long until I must have the refusal reasons` (the two 5-day periods) |
| `s 360SA(2) -- my retailer must tell me of the provider's notice within 5 business days` | my carriage service provider | business days from receipt of the s 360R notice | `Must I be told question` |
| `s 360VE -- the provider must decide on liability, then pay me or tell me it will not` | the statutory infrastructure provider | days from when it has reason to believe it is liable | `How many days until the provider must pay or refuse` (`the days to decide`, 98 days) |

The first and third rules branch on what the party did (fulfil or refuse; accept or not), with a `HENCE IF … THEN … ELSE` on the bound action. The case file asserts every question, asserts each rule's fulfilled traces with `EVALTRACE … EQUALS FULFILLED`, and `#TRACE`s each breach with an `-- expect:` line. On the stable `l4`, comparing a breached trace with EQUALS gives neither TRUE nor FALSE (both the assertion and its negation fail), so a breach cannot be asserted.

## Edition

The compilation registered as **C2026C00224** (Compilation No. 117, compilation date 4 June 2026, including amendments up to Act No. 75, 2025), retrieved from the Federal Register of Legislation on 13 October 2026, as deposited at `../../registers/source-bundle/C2004A05145.txt`. Part 19 is at lines 7320–8500 of the deposit.

**No instrument is deposited.** Part 19 leaves a great deal to the Minister and the ACMA: exclusions from the connection obligation (s 360P(3)), when a fixed-line connection is taken not to be reasonable (s 360P(10)), a longer response period (s 360P(11B)), fixed wireless conditions (s 360AA(2)), standards, benchmarks and rules (ss 360U, 360V), which of them are "designated compensable", the relevant number of days (ss 360U(3C), 360V(1C)), and the compensation rules (s 360VH). Each is asked as a fact or an input. A Ministerial instrument would change the answers; the Act's own figures (10 and 5 business days, 14 days, 14 weeks, 2 years, 25/5 Mbps) are used.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ta97-connection.l4` | `ta97-cases-connection.l4` | 46 written, 46 satisfied; 7 traces, each as its `-- expect:` line says |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The end-user**: the person or business at premises who wants them connected to a network that can carry broadband. "Am I entitled to be connected? Who has to do it? What do I have to ask for, and through whom? How long can they take? What if they refuse? What if my estate's provider goes under? Can I get compensation?"

Part 19 is addressed to statutory infrastructure providers (NBN Co and others) and to carriage service providers (retailers). Those duties are encoded as what they mean for the end-user: whether a provider must connect me, what I must be told and by when, what I can recover. No question is asked from the seat of the provider, the retailer, the Minister or the ACMA. A seat for the retailer (a business with duties under ss 360P(12)(d), 360SA) would be a natural second seat; it is not written.

The 2026-10-18 defaults:

- **The Part alone**, with the instruments that set its numbers asked as inputs (none deposited).
- **The actors the text names:** the statutory infrastructure provider, NBN Co, the carriage service provider, the end-user, the customer, the Minister, the ACMA (the last two only as the source of facts).
- **Judgments handed to others are answered conditionally:** whether a request is "reasonable", whether a fixed-line connection is "reasonable" (s 360P(1)(b), (10)), whether a Ministerial determination applies, whether a contravention "relates to" me (s 360VD(1)(c)). Each is an input; none is guessed.
- **The Act's own definitions are worked out from facts:** qualifying carriage service (s 360A, s 360AA), which service area the premises are in and who its provider is (ss 360C, 360F, 360G, 360K, 360KA, 360KB, 360L), the pending area (s 360F(2)), the period to answer (s 360P(11A)(b)), the damages after credits (s 360VD(4)), the last day to sue (s 360VD(7)). Borrowed terms ("carriage service provider", "listed carriage service", "building unit") are asked as facts with a gloss.
- **One case:** one set of premises, one request.
- **The Act's own terms**, each with a plain gloss in a comment.
- **Machinery out:** the declaration and notice machinery in Division 2, the register, audits, information-gathering, delegation.

## Scope

**In:** ss 360A (the definitions used), 360AA; ss 360C, 360F, 360G, 360K, 360KA, 360KB, 360L (as facts about the area); s 360P(1), (2), (8), (9), (10), (11A), (12); s 360Q(1A), (1B); ss 360R(1)–(3) (as the trigger), 360SA; ss 360VB, 360VD, 360VE; s 360W(2), (4).

**Out:** the rest of the Act; ss 360AB–360AE (control and associates); ss 360H–360J, 360LA–360NA (how areas are declared and exempt projects); s 360P(3A), (4)–(7); s 360Q(1), (2)–(13) except (1A), (1B) (the wholesale supply request, which is the retailer's); s 360RA, 360RB, 360S, 360SB, 360U, 360V (their content is in instruments), 360VF–360VH, 360X onwards.

## What the Act turns out to say

1. **The end-user cannot ask the provider directly.** The connection obligation arises "on reasonable request by a carriage service provider on behalf of an end-user" (s 360P(1)). A person who rings NBN Co is told "not yet": a retailer must make the request. Asserted.
2. **"Broadband" means at least 25/5 Mbps peak.** Each qualifying carriage service must have a peak download speed of at least 25 Mbps and a peak upload speed of at least 5 Mbps (s 360A, s 360AA(1)(d), (e)), and a public mobile service never counts. Fixed wireless must also be marketed as fixed wireless and be a listed carriage service meeting any Ministerial conditions. Asserted, including the boundary at exactly 25/5.
3. **The obligation is to connect to a fixed-line network first;** fixed wireless or satellite only "if it is not reasonable" to connect by fixed line (s 360P(1)(b)), which the Minister may deem for classes of premises (s 360P(10)). Asserted.
4. **There is a gap in new estates: a "pending area" has no provider.** An area named in an anticipatory notice (ss 360HA, 360HC) is taken out of the general service area (s 360F(1)(aa), (2)), so NBN Co is not its provider, but becomes an anticipated service area only when a building unit in it is completed and occupied (s 360KA(1)(c)). Until then no statutory infrastructure provider exists for premises there, so no s 360P obligation can arise. Premises that NBN Co already serves are carved out (s 360F(2)(c)). Asserted.
5. **The provider has 10 business days to say yes or no, and a refusal must come with reasons,** to the retailer within 5 business days, and from the retailer to the end-user within 5 business days of receiving it (s 360P(11A), (12)). The retailer's clock runs from receipt; the traces assume receipt on the day the provider gives the notice. A Ministerial "longer period" can only lengthen the 10 days (s 360P(11A)(b)(ii)). Asserted; the duties are traced.
6. **The Act sets no connection deadline of its own.** The maximum period to connect is whatever the provider's published terms say (s 360W(2)), subject to any standard (ss 360U(1)(f), 360W(4)). The encoding takes it as an input; its trace counts it from the "will fulfil" answer, which is a simplification (the published period runs "following the making of a request"). Not asserted beyond the trace.
7. **The terms are the provider's published ones at the time of the request,** unless an agreement between the provider and the retailer covers the connection; and the retailer can insist on an agreement on the published terms (s 360P(8), (9)). These are wholesale terms; the end-user's own contract is with the retailer. Asserted.
8. **Voice calls must be possible except on satellite** (s 360Q(1A), (1B)). Asserted.
9. **Notice that an area's provider can no longer serve it is owed only by providers other than NBN Co** (s 360R(1) covers nominated, anticipated and designated service areas only), and reaches the end-user through the retailer within 5 business days, if the matter is likely to change or disrupt their service (s 360SA). Asserted.
10. **Damages for a breach of a designated compensable standard or rule are owed to the "customer", which "includes prospective customer"** (s 360VB), reduced by credits for the same event "(but not below zero)" (s 360VD(4)), and must be sued for within 2 years (s 360VD(7)). Whether an end-user, rather than the retailer, is the provider's customer is not settled by the Part; it is asked as a fact. The amount is set by compensation rules that are not deposited. Asserted.
11. **The provider must decide on liability within 14 days and then pay, or say no in writing, within 14 weeks** (s 360VE(1), (3)–(5)): at most 112 days from when it first has reason to believe it is liable, unless a different number of days is declared for the standard or rule. Asserted; the duties are traced.

## Raised in the ledger

Nothing new raised. The instruments Part 19 relies on (the s 360P(3) and (10) determinations, the ss 360U and 360V standards and rules, the compensation rules) would make several inputs into computed answers; they could be raised as `supplied-fact` entries when a scenario asks for them.

## Links

- **Telecommunications (Consumer Protection and Service Standards) Act 1999 baseline** (`subjects/au/telecommunications-consumer-protection-and-service-standards-act-1999/encodings/baseline-2026-10/`): its finding 1 says broadband for premises is this Part's, not the universal service obligation's, and names `REQ-0092`. Read the two together: that encoding for the standard telephone service, this one for a broadband connection. Not joined in L4 (IMPORT does not cross folders).
- Not yet entered in `docs/au-baseline-links.md`, which covers the 118 baselines of 21 October 2026.

## What would need doing before this is worth relying on

- **The instruments**: the Telecommunications (Statutory Infrastructure Provider) determinations, standards and rules, and the compensation rules, deposited and brought in.
- **The register of statutory infrastructure providers** (s 360Z), or a way to ask the area facts from an address.
- **Case law** on "reasonable request" and "not reasonable" to connect by fixed line; none was read.
- A retailer's seat, and an independent test pass and a human review.
