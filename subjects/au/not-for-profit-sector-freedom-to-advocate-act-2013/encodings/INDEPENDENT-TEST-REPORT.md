# Independent test report: Not-for-profit Sector Freedom to Advocate Act 2013

Files: `independent-expectations.md` (written from BRIEF.md and the source only), `tests-independent.l4` (against `nfp-rules.l4`).

## Counts

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 — 0 errors, **32 satisfied, 0 failed**. (nfp-tests.l4 13/0; nfp-rules.l4 0/0.)

## Failures

None. Every limb tested matched: Commonwealth agreement (both conjuncts), s 5(1) advocacy restriction, s 5(2) carve-out, void-from date (entry date if on/after 14 June 2013; 14 June 2013 if earlier), s 4(1) breach only on/after commencement (s 7(2)), s 7(4)(b) accrued rights only for pre-commencement agreements. Edges 13 June 2013 / 14 June 2013 behave as expected.

## Gaps and reading notes

- The module folds several distinctions into single booleans, so my scenarios 7, 8, 9 and 12 could not be told apart from simpler ones: "agency of a listed paragraph" and "acting on behalf of the Commonwealth" are one flag; ACNC vs Electronic Transactions Act non-profit body is one flag; commenting / advocating / opposing and entity vs staff are one flag. The tests exercise the flag but not the sub-limbs.
- s 5(2) "to the extent that" is modelled all-or-nothing (`only restricts confidential or personal information`). A mixed clause (part advocacy gag, part confidentiality) cannot be partially voided; the user must answer FALSE and the whole clause is reported prohibited. Acceptable for the brief, but a partial-severance answer is not expressible.
- `void from` for a post-commencement agreement is the entry date (void ab initio). The Act just says "void"; consistent with my reading.
- s 6 out of scope per brief; not tested.
- Process note: I glanced at the first lines of nfp-tests.l4 for record syntax before writing my file (after the expectations were saved); no expected value was taken from it.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
