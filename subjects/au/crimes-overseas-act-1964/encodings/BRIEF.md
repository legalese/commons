# Encoding brief: the Crimes (Overseas) Act 1964 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Crimes (Overseas) Act 1964** (No. 116, 1964), Commonwealth of Australia, compilation of 3 October 2014, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C1964A00116.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the Australian whose act in a foreign country is in question** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Does this Act apply to what I did overseas, so that Jervis Bay criminal law applies to me? Can I be prosecuted without the Minister's consent? By when must the prosecution give me a copy of a certificate it relies on, and by when must I tell it I want the certificate's issuer called?"*

In scope: s 3 (Australian), s 3A, s 4(1), (2), (4), s 8(6), (8)(a). Out of scope: ss 1-2, 3B-3C (the regulations' declarations, which are inputs), s 4(3), (5), ss 5-7 (indictability, arrest, trial), s 8(1)-(5), (7), (8)(b), (9), s 9.

## Inputs

- My status when I acted: an Australian citizen; a non-citizen permitted to remain in Australia indefinitely; neither.
- The ground: diplomatic, consular or international-organisation immunity; immunity under a relevant agreement or arrangement while working under one; working under a declared agreement or arrangement; working for the Commonwealth in a declared foreign country or part; none. Whether I am within any category the regulations specify.
- Whether I am, or will become, subject to local prosecution that an Australian verdict would not end (s 3A(2)).
- Whether I was a Defence Force member, or ASIS, AGO or ASD staff acting properly in its functions (s 3A(10)).
- Whether the act would breach Jervis Bay criminal law; whether the Minister has consented in writing.
- The day the certificate is to be tendered; the day of the hearing at which I want the issuer called.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`co-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
