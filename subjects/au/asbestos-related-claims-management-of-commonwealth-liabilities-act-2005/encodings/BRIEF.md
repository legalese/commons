# Encoding brief: the Asbestos-related Claims (Management of Commonwealth Liabilities) Act 2005 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Asbestos-related Claims (Management of Commonwealth Liabilities) Act 2005** (No. 122, 2005), Commonwealth of Australia, compilation of 1 July 2014, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2005A00122.txt` (CC BY 4.0). Parts 2 and 3 commenced on 26 October 2005.

## Seat

The encoding is written from the seat of **the person with an asbestos-related condition who claims compensation or damages** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Is mine an asbestos-related claim under this Act? May I claim against Comcare? Who is liable to me now, and from when?"*

In scope: s 3(1) (asbestos-related claim, asbestos-related condition, liability, the excluded bodies in Commonwealth authority), s 5, s 6(1)-(2). Out of scope: s 4 (declarations, which are folded into the inputs), ss 6(3)-(6), 7-16 (consequences of transfer, finance, records, directions, compensation, regulations).

## Inputs

- My condition: asbestosis; an asbestos-induced carcinoma; an asbestos-related non-malignant pleural disease; mesothelioma; another condition caused by asbestos; a condition not caused by asbestos.
- Who breached the duty of care: the Commonwealth; a Commonwealth authority at the time of the breach; Comcare, Australia Post, Telstra, a body declared not to be an authority, or their subsidiary; someone else.
- What the liability arises under: the breach (not settled or finally decided); a contract of insurance; a judgment not stayed or under appeal at commencement; a written settlement made before commencement.
- Whom I claimed against (the Commonwealth or authority, Comcare, no one yet), and when.
- Whether the Minister declared the liability transferred back (s 6).

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`arc-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
