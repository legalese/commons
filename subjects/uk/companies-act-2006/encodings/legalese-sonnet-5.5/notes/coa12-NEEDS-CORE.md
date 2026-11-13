# NEEDS-CORE: what coa12 wanted from the core and did not find

The core (`coa-core.l4`, the keel's, read-only) lacks the constructors and helpers below.
Each was replaced by a stand-in or defined under the `coa12` prefix so that nothing here collides with another part; the lead hoists what it wants at the merge and the stand-ins are then replaced.
Every claim below was read from `coa-core.l4` and the layer-1 sources of this folder when the file was written.

## Constructors of `Party` (core lines 85 to 101)

| wanted | stand-in used | sections that need it | where |
| --- | --- | --- | --- |
| `Appropriate audit authority` (the body that receives an auditor's statement and a company's notice: the Secretary of State, a delegate, the Financial Reporting Council Limited, a supervisory body or the Independent Supervisor, by s 525(1)) | `Competent authority` (as the recipient of the action) | ss 522(1) and 523(2) | `coa12-ch4b-resignation.l4`, the two deontic rules of ss 522(1) and 523(2) |
| `Person proposed to be appointed as auditor` (the person the company must send a copy of a proposed resolution or special notice to, besides the outgoing auditor) | `Auditor`, which stands for the outgoing auditor only; the person proposed is named in the action text and is not a recipient of the rule | s 514(3) and s 515(3) | `coa12-ch4a-removal.l4`, the deontic rules of s 514(3) and s 515(3) |

The other parties of the Chapters (the senior statutory auditor of s 503 and s 504, the Attorney General of s 508, the Lord Advocate of s 509, the Financial Reporting Council Limited, a supervisory body, the Independent Supervisor) are not parties to any deontic rule of this part, so they are not constructors of `Party` here: s 525(1) answers "who is the appropriate audit authority" with the type `s 525(1) audit authority` of this part, and ss 508 and 509 are encoded as decision functions.
If the lead prefers one `Party` constructor per authority, `s 525(1) audit authority` is the list of what would be wanted.

## Helpers (defined in `coa12-logic.l4`; wanted as shared helpers)

| name | signature | used by | what it is |
| --- | --- | --- | --- |
| `coa12 either answer holds` | `MAYBE BOOLEAN` x `MAYBE BOOLEAN` to `MAYBE BOOLEAN` | ss 510(2), 519(2A), 519A(1), 519A(3), 523(1), 532(4), 539 | three-valued OR: `JUST TRUE` if either is; else `NOTHING` if either is; else `JUST FALSE` |
| `coa12 both answers hold` | the same | ss 510(2), 518(1), 519(2B), 519A(1), 519A(3), 520(1), 521(A1), 534(2), 539 | three-valued AND: `JUST FALSE` if either is; else `NOTHING` if either is; else `JUST TRUE` |
| `coa12 the opposite answer` | `MAYBE BOOLEAN` to `MAYBE BOOLEAN` | ss 519A(1), 523(1), 539 | swaps `JUST TRUE` and `JUST FALSE`, keeps `NOTHING` |
| `coa12 the answer for the fact` | `BOOLEAN` to `MAYBE BOOLEAN` | the seat layer (every yes/no fact passed to a `MAYBE BOOLEAN` input) | `JUST TRUE` or `JUST FALSE` |
| `coa12 the largest fine the penalty allows, in pounds` | `Penalty` x `NUMBER` (the statutory maximum) x `NUMBER` (level 3) to `MAYBE NUMBER` | the penalty questions of the seat layer | the pound value of a penalty's fine limit; `NOTHING` where the penalty states none |
| `coa12 the act was done within the number of days after the day` | `MAYBE DATE` x `DATE` x `NUMBER` to `BOOLEAN` | ss 518(5), 520(2), 520(4), 520(5), 521(1), 521(2), 522(1), 523(3) | counts both ends in (fork F9); `NOTHING` as the date means "not done" |

The core's `Penalty` has `Fine limit` constructors for "the statutory maximum" and "level 3" but not their pound values (the Act does not state them), so the pound conversion takes both as inputs.

## Types of this part that other parts could share

| name | what it is | sections |
| --- | --- | --- |
| `s 529(3) time` | a date and an hour of the day (a `DATETIME` comparison did not check on either stable build) | s 529(3); any "not later than the time" rule |
| `s 525(1) audit authority` | the five authorities of s 525(1) | ss 522 to 524 |
| `s 506(1) kind of copy of the report`, `s 519A(3) reason for ceasing to hold office`, `s 495(3A) what the auditors do with the provision`, `s 532(3) where the provision is contained`, `s 534(3)(b) section of the Unfair Contract Terms Act 1977` | types local to one section | their own sections |
