# Encoding brief: the Commonwealth Volunteers Protection Act 2003 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Commonwealth Volunteers Protection Act 2003** (Act No. 2 of 2003), Commonwealth of Australia. The source is the compilation prepared on 19 April 2011 (amendments up to Act No. 5 of 2011; register id C2011C00290), from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A01087.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the volunteer** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in the volunteer's words: *"Did I do the work on a voluntary basis; am I protected from civil liability for what I did; if not me, who bears the liability; must I help the Commonwealth defend the claim; and does an indemnity I gave have any effect?"*

The operative Act is in scope: s 4(2)-(4) (voluntary basis), s 5 (application), s 6 (protection and its exceptions), s 7 (the Commonwealth or authority incurs the liability), s 8 (duty to assist), s 9 (indemnities void). Sections 1-3, 10-11 are machinery or cross-references.

## Inputs

- Whom the work was for (the Commonwealth or a Commonwealth authority) and whether it organised it (organised includes directed and supervised).
- Remuneration: none beyond reimbursement of reasonable expenses, or less than the prescribed amount; or continued pay from the usual employer with nothing else, where the work is usually done by unpaid (or low-paid) people.
- Whether the work was done under a court order; whether in good faith; whether after the Act commenced.
- The kind of liability (compulsory third-party motor vehicle insurance, defamation, or other).
- Whether the volunteer's ability was significantly impaired by a recreational drug (including alcohol); whether they knowingly (or ought to have known) acted outside the authorised activities or contrary to instructions.
- For an authority, whether another Act already protects it from the liability (s 7(2)).
- Whether the Commonwealth or authority requested assistance. (Whether an indemnity was given is not an input: the answer says whether s 9 would void one.)

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, give NOTHING (or `REFUSE`); never `FALSE`.
- `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`cvp-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
