# Encoding guide for Claude sessions

21 October 2026. For any Claude session that helps encode law in `legalese/commons`.
Read it after [`CLAUDE.md`](../CLAUDE.md). Where the two disagree, CLAUDE.md wins and this guide should be fixed.

Commons holds law: deposited sources and their L4 encodings. Tools, pipelines, scenarios and the website live elsewhere (`legalese/workbench`, `legalese/l4-ide`, `legalese/legalese.github.io`). Nothing under `subjects/` may depend on them.

---

## 1. Before you start

1. **Load the L4 skills.** Use `encoding-a-subject` for the workflow and `writing-l4-rules` for the language (see CLAUDE.md for how to install them).
2. **Check with the stable `l4`.** That is the one in the L4 VS Code extension (1.6.98 at the time of writing). It is what Legalese Cloud runs, so an encoding that only a pre-release `l4` accepts cannot be deployed or used on the website. Leave `JL4_LIBRARY_PATH` unset.
3. **Find out what already exists.** Before you write anything for an Act, look in `subjects/<jurisdiction>/<slug>/encodings/`. A second encoding of a law sits beside the others as an equal; it never replaces one.
4. **Take your work from the priorities and the ledger** (sections 6 and 7), not from whatever looks interesting.

## 2. Whose seat

An encoding answers the questions that one kind of person asks about the law that applies to them. That person's position is the **seat**.

**The individual comes first, and is required.** Every Act gets a seat for the individual to whom the law is applied: the employee, the tenant, the driver, the accused, the heir, the applicant, the pensioner.
- **Questions** are phrased as that person asks them: "Must I …?", "Am I entitled to …?", "How much … do I get?", "What is the most I can be fined?".
- **Facts** are ones that person could state.
- **Provisions that address only an official** are encoded for what they mean to the person: what may be done to them, what they must be given, and by when.

**Other seats, where they matter.** Add a further seat for any other party the text puts duties or liabilities on, when that party is important to the Act. Typical cases:
- the employer, under employment law;
- the landlord, under tenancy law;
- the seller or business, under consumer law;
- the insurer's customer and the insurer, under insurance contracts law.

A small business owner or a company is fine.

**Never a seat for an official or the government:** not the regulator, the court, the department, the police or a minister. Their powers appear in the encoding only as what they mean for the person in the seat.

Record every seat in the encoding's `NOTES.md` (a `## Seat` or `## Seats` section) and in `encoding.json` (`"seat"`, or `"seats": [...]`).

## 3. Longer encodings and seat layers

**Never delete or replace an existing encoding to add a seat.** If an Act already has a longer encoding (a whole-Act encoding, a multi-module first pass, a named encoding), add a **seat layer** in the same folder.

A seat layer is one module, `<prefix>-seat.l4` for the individual or `<prefix>-seat-<party>.l4` for another party. It:
- IMPORTs the longer modules and calls their rules, never copying or restating a rule;
- asks the seat's questions, each with `@export` and `@desc`;
- takes **plain inputs**, one per fact the person can state (yes/no, a number, a date, a choice from a list), each with a `@desc` worded from that seat:
  - employee: "How many complete months have you worked for this employer?"
  - employer: "How many complete months has this employee worked for you?"

  It builds the longer encoding's records internally from those inputs. A record field that no rule reads gets a fixed placeholder, with a comment saying so.
- keeps its own names: two seat layers in one folder must never define the same name;
- uses the Act's own figures where the law lets a minister substitute one. The person cannot state "the s 29 proportion". Say in NOTES.md that a substitution would change the answers.
- groups its questions under `§` headings in the encoding's natural order. The website uses them for grouping and order. Where a group only arises in a situation the person may not be in (dismissal, maternity, being stopped by police), say so in the heading's comment, so the form can ask "Has this happened to you?" before showing the group.

Each seat layer gets its own case file. Where an Act has two seats, include **mirror cases**: the same facts asked from both seats, with answers that agree.

Write a separate shorter **baseline** (`encodings/baseline-<date>/`) only where no longer encoding exists. The worked example of two seats over one long encoding is `subjects/sg/employment-act-1968/encodings/naive-2026-10/`.

## 4. The other design defaults

These follow CLAUDE.md, ruled 2026-10-18:

- **Scope:** the Act alone, plus the instruments that set its numbers or dates. Use them if they are deposited; otherwise make the number an input and say so.
- **Actors:** the ones the text names.
- **Judgments left to someone else:** answer them conditionally, as an input ("…, if the Commissioner is satisfied that …"). Never guess them.
- **Definitions:** work the Act's own definitions out from facts. Ask borrowed terms as facts.
- **One case:** the text's natural unit, such as one employment, one vehicle or one act.
- **Terms:** use the Act's own words, each with a plain gloss in a comment.
- **Machinery out:** boards, commencement and regulation-making powers.

## 5. Writing L4 that the stable binary accepts

- **No `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`** (except `LEST BREACH … BECAUSE`, which is accepted). For a case outside the encoding, return an explicit "not covered" value, either a constructor or `NOTHING`, and assert it.
- **Parenthesise every `NOT`.** `NOT a AND b` parses as `NOT (a AND b)`.
- **Keep each `#ASSERT` on one line.** A continuation line is rejected.
- **Bracket arithmetic that crosses a line break.** `x DIVIDED BY w` at the end of a line, followed by `TIMES 100` on the next, divides by `w × 100`. Chained `MINUS` is left-associative.
- **`IMPORT` finds only modules in the importing file's own folder** (and the libraries). One encoding cannot import another from a different subject, and a file in a `cases/` subfolder cannot reach the modules above it. A name defined in two imported modules cannot be used at all. Cross-encoding links go in `docs/au-baseline-links.md` style registers, not code, until the language allows them.
- **Smaller gaps:** `YMD` is missing from the stable prelude, so add a local shim (`YMD y m d MEANS Date d m y`). `WAIT UNTIL` is spelled `WAITUNTIL`. `TYPICALLY` on a record field is not accepted.
- **`@export` and `@desc` on every question** in a seat or baseline. Legalese Cloud publishes those, and the website's Interact form asks them.
- **Expected values are hand-written from the text,** never copied from the encoding's own output.
- **Checks before committing:** `l4 run` on every file shows no `DiagnosticSeverity_Error` or `_Warning`, and every case file has assertions written equal to assertions satisfied. A test that fails on purpose is allowed only where NOTES.md records it as a finding, as the HVAC worked example does.

## 6. Priorities

The current breadth-and-depth chart is at https://claude.ai/artifact/KSy93JyfrV1jbDdnRcijSt. Michael edits it, and it takes precedence over this table. Depth runs from one Act, through tax and benefits, the 20 categories, and everything the scenario lives hit (including regulations), to all Acts and relevant regulations, all Acts and regulations, and finally all Acts, regulations and relevant cases.

| Jurisdictions | Where it is now | Where it is going |
|---|---|---|
| Singapore | All Acts and relevant regulations | All Acts, regulations and relevant cases |
| Commonwealth of Australia, Western Australia, South Australia, New Zealand | Everything the three WA lives hit, including regulations (South Australia and New Zealand are behind) | All Acts, regulations and relevant cases |
| UK, US federal, California, Canada federal, British Columbia, Ireland | Sources sampled; little encoded | The 20 categories |
| The other Australian states and territories (not WA or SA), the US states and Canadian provinces, and the other English-language jurisdictions | Samples | Tax and benefits |
| Every other jurisdiction recognised by the UN | Mostly nothing | One Act |

**The 20 categories** are:
- pay and working time
- losing a job
- work injury and workplace safety
- pensions and retirement savings
- social security and benefits
- personal income tax
- consumer rights and purchases
- renting a home
- buying and owning a home
- insurance claims
- debt, credit and bankruptcy
- immigration, visas and work permits
- travel (customs, passports, passenger rights)
- births, identity and citizenship
- marriage, divorce and children
- wills, inheritance and incapacity
- health care and health insurance
- education
- driving and road traffic
- crime, police and courts

**"Tax and benefits"** means a connected sample on two topics, social security and benefits and personal income tax, chosen so that a member of the public gets useful answers.

Leave the existing Israel, Brazil and Vietnam encodings alone unless you are asked to work on them.

## 7. The requirement ledgers, and running scenarios

Each jurisdiction that runs scenarios keeps a **requirement ledger** beside its subjects. It is one JSON object per line, and it records every question the law could not yet answer:

| Ledger | Jurisdiction |
|---|---|
| `subjects/sg/requirements.jsonl` | Singapore |
| `subjects/au/requirements.jsonl` | Commonwealth of Australia |
| `subjects/au/wa/requirements.jsonl` | Western Australia |
| `subjects/nz/requirements.jsonl` | New Zealand (empty so far) |

A question goes in the ledger of the law that answers it. Refer across ledgers by folder prefix, as in `au/wa:REQ-0012`. The format, the nine kinds and the lifecycle are in [`docs/ledger/LEDGER.md`](ledger/LEDGER.md). The working rules are in [`docs/ledger/NOTE-TO-ENCODER.md`](ledger/NOTE-TO-ENCODER.md).

**Working the queue:**
1. Run `python docs/ledger/check-ledger.py <ledger>`. It validates the file and prints the open queue in order: priority 1 first (raised by a scenario), then 2, 3, 4; within a priority, the higher count first.
2. **Claim** the first open entry: set `status` to `claimed`, with `claimed_by` and `claimed_on`, and commit that change alone before starting, so no other session takes it.
3. For a priority-1 entry, the entry's `expected.assertion` is the encoding's first test, in the scenario's own facts.
4. **Close it in the same commit as the encoding:** set `status` to `satisfied`, with `resolution` (`on`, `subject`, the encoding folder, `commit`). An encoding without its ledger line closed, or a closed line without its encoding, is a defect.
5. If it cannot be done (not law, no source deposited, the instrument doesn't exist), set `declined` with a reason. Never delete, renumber or reorder entries, and never move another entry's priority to put your own first.
6. When an Act leaves the answer to a regulation, an order or a case, **raise a new entry** for it (`raised.by: "encoder"`). Use priority 1 if a scenario needs it, otherwise 2.

**Running scenarios in a jurisdiction.** Michael runs the scenarios; their requirements come into these Commons ledgers, and an encoding session works them from here. The cradle-to-grave lives are kept in the private `legalese/workbench` repository under `scenarios/<jurisdiction>/` (for example `scenarios/sg/cradle-to-grave-simone/`, and `scenarios/au/wa/cradle-to-grave-{chloe,jake,daniel}/`). Each life has `SCENARIO.md`, `facts.json`, `GAPS.md` and `ABRIDGED.md`. Its author changes them; an encoding session does not. If you run a scenario against Commons:
- every question the law cannot answer becomes a **priority-1 entry** in the ledger of the law that should answer it, with the life's facts and the answer the life expected;
- an encoding written for a life includes at least one case per life event it answers, in that life's facts, naming the event id (for example `c074`) in a comment;
- where an encoding finds that a life cites the wrong section or states a wrong figure, say so in the encoding's NOTES.md, under a finding that ends "Asserted." where the case asserts it. Report it to the scenario's author, or, if you have access and are asked, record it in the life's corrections file. Never change an encoding to agree with a life the text contradicts.
- `python scenarios/check-status.py <life folder>` in the workbench compares a life's claimed status for each Act with the encodings that exist.

## 8. Sources

- **Encode only from a deposited source:** `subjects/<jurisdiction>/<slug>/registers/source-bundle/*.txt`, with its `.meta.json` and the subject's `SOURCE-LICENSE.md`.
- **Never alter a deposited text.** A correction or a newer version goes beside it as a new file. A formula that was lost in conversion is transcribed into a `<source-id>.formulas.md` sidecar, citing the authorised rendering it came from.
- **When fetching:**
  - use the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, and never put an email address in it;
  - obey robots.txt and each site's rate limits. The Federal Register of Legislation refuses after about 23 requests in a window, so send at most 20 per batch, at least 20 seconds apart;
  - treat a 403, a CAPTCHA, a bot challenge or a geo-block as a no. Never work around one; record it and move on;
  - put downloads in their own directory, and run any Python that reads them with `-I`.
- **Licences:**
  - Open licences are fine.
  - Non-commercial terms are fine, because Commons counts as non-commercial.
  - "No modification" terms, "personal use only" terms, or anything that needs permission go to Michael before anything is deposited. Such a source is indexed without its text.

## 9. Files, notes and commits

- **Where an encoding goes:** `subjects/<jurisdiction>/<slug>/encodings/<name>/` (for example `naive-2026-10`, `baseline-2026-10`, `legalese-aswathy`). It holds the `.l4` modules, the case files, `encoding.json` (with the seat, scope, edition and checks), `NOTES.md`, and a copy of `SOURCE-LICENSE.md`. The layout is ruled in [`docs/directory-conventions.md`](directory-conventions.md).
- **NOTES.md says:**
  - the method;
  - the edition encoded;
  - the checks run;
  - the seat or seats, and each default followed or departed from;
  - what is in and out of scope;
  - numbered findings ("What the Act turns out to say");
  - what would need doing before the encoding is worth relying on.
- **One encoding per commit,** with its ledger line. The message starts `<jurisdiction>/<slug>: …` and ends with the co-author line your session's instructions give. Members of the `legalese` organisation commit to `main`; others fork and open a pull request.
- **When talking to Michael,** name the encoding (for example "the Employment Act's employer seat"); don't call it a "row".

## 10. Using it: Legalese Cloud and the website

- **What gets deployed:** an encoding's seat or baseline module is deployed to Legalese Cloud, for example `sg-employment-act-1968-employee` (deployment names are at most 36 characters). The website's "Ask your questions" form for that Act then asks its questions.
- **What the form needs:**
  - clear `@export` questions and seat-worded `@desc` inputs;
  - the encoding's natural order;
  - `§` groups, with situations marked.

  It works out from the deployed rules which questions still matter, so writing rules whose structure follows the text (visible AND/OR, a fact asked only where the text needs it) makes it ask fewer, better questions.
- **Deploying is done by a person** with Legalese Cloud access. Changing a question's inputs is a breaking change, and the deployment must be updated under the same name.
