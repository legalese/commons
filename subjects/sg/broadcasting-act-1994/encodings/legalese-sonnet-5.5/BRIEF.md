# Encoding brief: Singapore's Telecommunications Act 1999, Broadcasting Act 1994 and the instruments made under them, in L4 (stable)

You are producing an L4 encoding of two Singapore Acts and the subsidiary legislation made under them, to answer one question with every step cited to the text in force at the time.
This brief is the whole specification. Read it fully before opening any source.
You are one of two solo encoders, one per Act (see "Division of work"): no subagents. You do all of your Act in one context and check your own work with the diagnostics.
A second, independent reviewer will afterwards re-derive the answer from the sources without seeing your conclusion (see "Quarantine").

## The question

> Does Singapore law require a licence to possess, or to use, an analogue terrestrial television receiver (one that takes broadcast signals through an aerial or antenna, not a satellite dish; receive-only; no decoder)?
> Is it an offence for an individual to possess or use one with no licence of their own?

Answer it at three dates, each from the text in force at that date:

1. **Before the television and radio receiver licence ended.** Find out what that licence was, under which instrument, and the date it ended.
2. **Between that end date and 2019.** Test at least one date well inside the period, and the day before, the day of and the day after each change you find.
3. **Today**, taken as the date of the 2020 Revised Edition consolidations deposited in commons (`TA1999.txt`: as at 2026-10-01; check its `meta.json` for the exact date).

For each date the encoding must say one of: it is an offence (under which section, with what maximum fine and imprisonment, and what conviction means); it is not an offence (which instrument, class licence, exemption order, licence condition or technical specification covers the person); or the sources do not answer it.

**Either answer is a good result. Do not lean towards the interesting one.**
Hypotheses to test, each to be confirmed or refuted by quoted text and none to be assumed:

- H1. A receiver licence obligation existed, and it ended around 2011.
- H2. When it ended, nothing was put in its place, so possession or use of an ordinary analogue terrestrial receiver became an offence under the Telecommunications Act, with a maximum of $10,000 and 3 years.
- H3. Some instrument (a class licence, an exemption order, the radio-communication regulations, a notification, an IMDA technical specification given legal effect through a regulation) covers that person, so H2 is false.
- H4. Low-power FM transmitters (88–108 MHz) being lawful is what covers FM radio receivers.
- H5. A type-approval or technical-specification regime for digital TV receivers (named by H-claimants as "IMDA TS DVB-T2 IRD") covers digital sets from 2019.
- H6. Satellite receivers (TVRO) are individually licensed under the Broadcasting Act.

H2 and H3 cannot both be true. If the text supports neither, say so and say what is missing.
Where a section is not on any of these paths but you meet it while reading, it still gets its coverage row (below).

## Interpretation Act s 9A

A court may prefer the purposive reading of a provision (Interpretation Act 1965 s 9A(1)), and may look at material outside the written law (Hansard, the Gazette) to confirm the ordinary meaning or, where that meaning is ambiguous or leads to a result that is manifestly absurd or unreasonable, to find the meaning (s 9A(2)).
Singapore's Interpretation Act is already encoded in this repository at `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/`, s 9A included. **Cite it; do not re-encode it.** (Stable `l4` cannot IMPORT across folders, so there is no code link: say so in NOTES.md.)

Encode s 9A's effect as what it is: **a question a court may weigh, not a rule that flips the answer.**
Your decision functions return the answer on the text as it reads (the literal answer). A separate function, taking the literal answer, returns whether it is in the territory s 9A(2)(b)(ii) names, and never changes the literal answer.
In `TV-QUESTION.md` say plainly whether the literal reading is absurd and why, and leave the purposive outcome open. Hansard and the Gazette are extrinsic material: use them for purpose and for dates, never as the rule, and mark every such citation as extrinsic.

## The subject and the sources

- **Telecommunications Act 1999** (2020 Rev Ed), `subjects/sg/telecommunications-act-1999/`, text `registers/source-bundle/TA1999.txt`, whose `TA1999.meta.json` lists SSO's historical version dates (the in-force dates of every consolidation).
- **Broadcasting Act 1994** (2020 Rev Ed), `subjects/sg/broadcasting-act-1994/`, text `registers/source-bundle/BA1994.txt`, the same.
- **The instruments made under them**: regulations, notifications, exemption orders, class licences, and any IMDA technical specification or code that has legal effect through them. Deposit each one you rely on as a new subject (or as a new file in an existing subject's `registers/source-bundle/`), laid out as the existing rows are, with its own `SOURCE-LICENSE.md`, `meta.json` (URL, retrieval date, sha256, in-force date, how you got it) and `subject.json` naming its parent Act and the empowering section. Read `docs/directory-conventions.md` first.
- **Predecessor and ending instruments**: the receiver licence is likely to have been created by an instrument older than the 1999 Act (the Telecommunication Authority of Singapore Acts, the Singapore Broadcasting Corporation Act, regulations made under them) and ended by one you must find. The text of 1999 Act's own savings and transitional sections says what carried across. Find the instrument that ended the licence and the date.
- **Possible leads (recollections to verify, not facts):** Telecommunications (Radio-communication) Regulations; Telecommunications (Class Licences) Regulations; Telecommunications (Dealers) Regulations; Broadcasting (TVRO System) Regulations; Broadcasting (Class Licence) Notification; Broadcasting (Exemption) Orders (the numbered series and S 121/2008, S 211/2022); any "Telecommunications (… ) (Exemption) Notification"; IMDA's technical specifications ("IMDA TS SRD", "IMDA TS DVB-T2 IRD" are names a claimant used; check what they are and what, if anything, gives them legal effect).
- **Point-in-time text matters here**, because the question is about dates. For each Act and instrument you rely on, deposit the text as it stood at each date that matters, as a new file beside the current text (`TA1999.<yyyymmdd>.txt` with its own `.meta.json`; **never edit a deposited text**). Where you cannot get the text as it stood, say so in NOTES.md and in TV-QUESTION.md, name the date and the instrument, and make that answer "the sources do not answer" for that date. Do not reconstruct a past text from the present one.

### Where to get them

- **Singapore Statutes Online (sso.agc.gov.sg) answered scripts with 403** (probed 2026-10-20 by GM and again 2026-11-03 by me). A 403 is a no: do not work around it. SSO's terms (`SOURCE-LICENSE.md` cl.13(d)(i)) confine automated extraction to 03:00–07:00 Singapore time at the published crawl-delay; if you try it at all, try once, inside that window, and record the result.
- **The `lawplain` MCP server** is a Singapore corpus: `corpus` is one of statutes, subsidiary_legislation, hansard, bills, judgments, practice_directions. Its tools (`mcp__lawplain__search`, `mcp__lawplain__get_document`) are deferred: load both with `ToolSearch` query `select:mcp__lawplain__search,mcp__lawplain__get_document`. It passes `params` through, so look for how to ask for a version (`as_at`, `version`, `kind`). It returned `act_current` and `act_revised` rows for TA1999 and **no subsidiary legislation under parent_act_id TA1999** on 2026-11-03; it does hold the Broadcasting Act's (BA1994-RG3 the TVRO Regulations, BA1994-N1 the class licence notification, BA1994-OR1..3, S 121/2008, S 211/2022 and more). **Check which version of a text it serves before citing it, and record that in each deposit's `meta.json`.** It is a secondary source: an aid, not the authoritative text. Say so.
- **Gazette**: egazette.gov.sg publishes the Government Gazette (the legislation supplements carrying amending and ending instruments). Hansard: parliament.gov.sg, and lawplain's `hansard`. IMDA's own site (imda.gov.sg) for the technical specifications and the licensing pages. Fetch rules: User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, never an email address; obey robots.txt and rate limits; a 403, a CAPTCHA or a bot challenge is a no; put downloads in their own directory (never in the repository, never in `/tmp`); run any Python that reads them with `-I`.
- **Do not use web.archive.org or any mirror to get around a refusal.** If a decisive text is reachable only that way, stop and tell me (the orchestrator) in your report; I will ask.
- Licence: SSO's terms are in the existing `SOURCE-LICENSE.md` files; copy their attribution into each new deposit. Anything needing permission goes to the orchestrator before it is deposited.
- Never probe a live service beyond fetching published law. Never print environment variables.

## Scope — the whole of both Acts and every instrument (ruled 2026-11-03)

Meng ruled on 2026-11-03, through the GM session: **both Acts are encoded in full, with every instrument found, and no deferred rows.**
The 2026-10-22 whole-Act rule stands as it was applied to the Interpretation Act, and NOTES.md records no departure from it.
The TV question is still the first thing the work answers: do the path to it first (below), tell the orchestrator when it is solid (the checkpoint, below), then complete the rest of the Act without stopping.

**Whole means** that every provision of the text (every section, subsection, paragraph, schedule item, table row and defined term) has a row in the coverage table, and each row has exactly one disposition:

- `encoded`: a rule, definition or table in layer-1 L4, with a test, citing the provision with `@ref`.
- `inert`: allowed ONLY for these three reasons: (1) not operative (title, long title, enacting words, headings, a purpose clause that creates no rule); (2) machinery per the Guide §4 (boards and offices and their staffing, the Act's own commencement, short title, regulation-making and rule-making powers, savings and transitional provisions that affect no one now, amendments of other Acts); (3) text shown repealed or blank.
- `fork`: the text can be read two or more ways with different outcomes; the row points at the fork-register entry (every reading, and the text that licenses each) and at the rule that encodes the chosen reading, or at the explicit "not covered" value.
- `repealed or blank in this text`: say what the text shows.
- `source not obtained`: **for an instrument only.** The row names the instrument, the section it is made under, where you looked and what each place answered or refused. It is the one way an instrument without a text gets a row; it never applies to a provision of the two Acts.

There is no `out-of-scope` row and no `deferred` row. These are NOT reasons for `inert`: "addresses an official" (encode what it means for the individual); "an interpretive canon or open-textured" (encode the rule and take the judgment as a plain input); "refers to another Act or instrument not among the sources" (encode as stated, ask the borrowed fact as an input); "no input would change the answer" (a rule with one answer is still a rule); "the naive encoding did not cover it".
A definition is encoded: a function that returns the term's meaning as the Act states it, with a test for each entry.

**Order of work inside the scope.**

1. Enumerate first: build the coverage table by script from the text, for the whole Act and a row per instrument you find under it (whether or not you could deposit it); check that every non-blank line of the text falls in some row.
2. **The TV path first.** Do these provisions and instruments before the rest: whatever bears on whether a person may possess, use, install, sell, supply or hold a telecommunication or radio-communication apparatus or receive broadcasts; licensing, class licences and exemption from licensing; the offences and penalties that attach, **including the general penalty section** (which the earlier naive encoding did not read), composition, presumptions and evidence; the definitions those use; the savings and transitional provisions that carried the receiver licence across; and the instruments that decide the question, in the vintages that matter. Then the seat layer and `TV-QUESTION.md` on that path.
3. **Checkpoint.** When the TV path is solid, meaning its modules and tests run under `check.sh` with no unexplained error, the sources for the three dates are deposited (or their absence recorded), and `TV-QUESTION.md` is complete, send ONE message to `main` with `SendMessage` (to: `main`): your answer to (1)–(3) at the three dates with the decisive sections, H1–H6, what you could not source, and the `check.sh` numbers so far. Then carry on with the rest of the Act in the same context. (The checkpoint may state your conclusion: only the files named under "Quarantine" may not.)
4. Complete the whole Act, section by section in the Act's own order, moving each row of the coverage table as you land it, and keep `PROGRESS.md` current. Split the modules along the Act's Parts.
5. The earlier **naive encodings are never edited**: `subjects/sg/telecommunications-act-1999/encodings/naive-2026-10/` and `subjects/sg/broadcasting-act-1994/encodings/naive-2026-10/`. Read their NOTES.md for what they cover; your work is a new row beside each.

## Division of work: two encoders, one per Act

Two solo encoders run at the same time, each in its own folder. Neither touches the other's folder, and neither imports from it (stable `l4` cannot).

- **Encoder TA** (named `sg-tv-encoder`): the Telecommunications Act 1999 and every instrument made under it, in `subjects/sg/telecommunications-act-1999/encodings/legalese-sonnet-5.5/`, modules prefixed `sgta-`. It owns the TV question: `TV-QUESTION.md`, `sgta-tv-seat.l4`, `sgta-tv-cases.l4`.
- **Encoder BA**: the Broadcasting Act 1994 and every instrument made under it, in `subjects/sg/broadcasting-act-1994/encodings/legalese-sonnet-5.5/`, modules prefixed `sgba-`. Its seat is the same person asking about a satellite dish, a decoder or a broadcast licence of their own, in `sgba-seat.l4` and `sgba-cases-seat.l4`. What it concludes about H6 and anything else on the TV path goes only in `TV-QUESTION-BA.md` and `sgba-tv-*.l4` (quarantined as below).
- Where the TV question needs a Broadcasting Act fact, Encoder TA reads the Act's text itself, takes the fact as a plain input and cites the section; it does not wait for Encoder BA.
- Instruments are encoded in the folder of the Act they are made under, and deposited under `subjects/sg/<slug>/` as new subjects. If both Acts rely on one instrument, the TA encoder deposits it and the BA encoder cites the deposit rather than depositing a second copy.
- Neither encoder commits or touches git state.

## Layout and deliverables

Two new encodings, each its own folder named in the house style:

- `subjects/sg/telecommunications-act-1999/encodings/legalese-sonnet-5.5/` (this folder; TA modules prefixed `sgta-`)
- `subjects/sg/broadcasting-act-1994/encodings/legalese-sonnet-5.5/` (BA modules prefixed `sgba-`)

Stable `l4` IMPORT finds only modules in the importing file's own folder, so **each instrument is encoded in the folder of the Act it is made under**, and a rule is never copied between folders. Where the TV question needs a Broadcasting Act fact (for instance whether the person holds a BA licence), the TA module takes it as a plain input and cites the BA encoding. State the cross-folder links in a register in NOTES.md.

In each folder:

1. `.l4` modules, ASCII names, split along the source's own structure: nouns first (one module of `DECLARE` only, which the others import), then one module per Part or natural group (instruments in their own modules), then tests. Isomorphic: one source provision, one recognisable place in the L4, with the source's numbering and an `@ref` on every rule. Quote the source on `-- src:N | text` lines and put locators on the `@ref` as `references/source-locators.md` in the `encoding-a-subject` skill describes; `assets/srcrefs.py` checks them (run it with `--refs` and `--strict` and report).
2. **Vintages are inputs, never merged**: a decision takes the date as an input (`Date day month year`) and the module for each vintage of a rule is its own function; a vintage silent on something answers "not covered", never a figure borrowed from another vintage. Use the rule-version mechanism if the stable `l4` reads it (`references/dialects.md`), otherwise explicit date inputs.
3. Tests from the text, never from the code: both sides of every date edge, one per route through each licensing and exemption provision, the penalty arithmetic, and worked cases for each hypothesis H1–H6. A failing assertion is a finding. A test meant to fail goes in its own file with the count stated.
4. `NOTES.md` (method; editions encoded and where each text could not be had; the checks; the seat; scope (the whole Act and every instrument, ruled 2026-11-03), with the coverage table and no deferred row; the fork register with every reading and the text that licenses each; numbered findings "What the Act turns out to say"; open questions), `encoding.json` (seat, scope, edition(s), checks, `target: "main"`, `status: "draft"`, `not_reviewed`), `SOURCE-LICENSE.md` (pointing at the subject-level one), `PROGRESS.md` (keep it current so you can resume after a context compaction).
5. `check.sh` and `fetch-main-l4.sh` copied from `/Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/assets/`, run with the build named below. Paste its output, main columns included, into NOTES.md.

### The seat

Commons requires the individual's seat (`docs/ENCODING-GUIDE.md` §2–3): **a person who owns a television (or a satellite dish) in Singapore and asks "Do I need a licence?", "Am I committing an offence?", "What is the most I can be punished with?"** Never a seat for IMDA, the Minister or a court.
The seat layer IMPORTs the layer-1 modules and calls their rules; it never restates one. Each question has `@export` and `@desc`, takes plain inputs one person could state (the date; what the receiver is; whether it is only an aerial type; whether they have a licence of their own; which licences or class licences apply to them), worded as that person would be asked, grouped under `§` headings in the text's natural order, with mirror cases where a second seat is added. A second seat (a dealer selling receivers) is welcome only if time allows and only in its own file.

## Quarantine: do not let your conclusion leak into the files the reviewer reads

A second agent will re-derive the answer from the sources and the layer-1 encoding without seeing what you concluded. So:

- Everything that states your answer to the question (what the law is at each date, which section, the penalty, what covers or fails to cover the person, whether the literal reading is absurd, what each hypothesis came to) goes **only** in these files: `TV-QUESTION.md` (in the TA folder), `sgta-tv-seat.l4` and `sgta-tv-cases.l4` (the TA seat layer and its cases), any test file whose name starts `sgta-tv-`; and, in the BA folder, `TV-QUESTION-BA.md` and any file whose name starts `sgba-tv-`. Quarantined files may import anything; **nothing else may import them**.
- `NOTES.md`, the layer-1 modules, the layer-1 tests, the fork register and the findings must not state the answer. They record what each provision says and how you read it. A fork about a provision on the TV path goes in `TV-QUESTION.md`, and `NOTES.md` has a one-line pointer to it.
- `TV-QUESTION.md` has: (1)–(3) at each date, with the decisive sections and the quoted text; the maxima; which instrument covers or fails to cover the person and the date it began; a table of H1–H6 (confirmed, refuted, not answered, with the citation); the s 9A paragraph; what could not be sourced; and, for each date, an honest statement of how sure you are and why.
- Layer-1 tests may assert what a provision says (for example the penalty figure of a section) but not that any particular person in the TV question is or is not caught.

## Rules that matter

- **Encode isomorphically; cite on every rule.**
- **Where the sources do not answer, return `NOTHING` in a `MAYBE` or an explicit "not covered" constructor, and assert it** — never `FALSE`, never `0`, never a plausible default. A gap is a finding.
- **A judgment the text hands to someone else** (the Authority's satisfaction, a licence granted at its discretion) is a conditional input, never guessed.
- **An assertion that fails is a finding.** Never edit an expected value to match what the code computed.
- **Read the diagnostics, not the exit code.** `check.sh` counts errors, satisfied, failed and refused assertions; report its numbers, never "it's green".
- **Expected values are hand-written from the text.**
- **Seat first, never an official's seat; no quoting a person who is not a source.** Do not name, or refer to, the person or people who first asked this question, in any file: write it in neutral terms. (This repository is public.)
- Write plain prose, one sentence per line, in NOTES.md and TV-QUESTION.md. Never write a planned state in the present tense: "proposed, not landed" until it has landed. Cite what you checked (`file:line`, a command), not the principle you inferred.

## Toolchain

**Target compiler: `main`, and the build is 1.6.98 specifically** (the build `docs/ENCODING-GUIDE.md` names; do not use a newer one to check).

- `L4_BIN=$HOME/.cache/l4-main/98/l4`. Its `--version` prints `1.6.98 (main, 7689b0d, 2026-10-19)`; confirm before you start. `~/.local/bin/l4` is a dev build: **do not use it**.
- Run `check.sh` with `L4=$HOME/.cache/l4-main/98/l4 L4_MAIN_BUILD=98` so the main comparison is also build 98.
- Leave `JL4_LIBRARY_PATH` unset.
- `main` rejects, or reads differently, much of what the authoring skill teaches. Read `references/dialects.md` in the `writing-l4-rules` skill first. No `REFUSE`, no `#ASSERT REFUSED`, no `BECAUSE` outside `LEST BREACH`; no `@lang`; no `YMD` of your own (write `Date day month year`, `IMPORT daydate`); parenthesise every `NOT`; one `#ASSERT` per line; `WAITUNTIL`; `TYPICALLY` on a record field is not accepted. Where the skill describes a construct the stable binary rejects, the binary governs; record it in NOTES.md under "What the stable binary does not accept".
- Skills: `encoding-a-subject` and `writing-l4-rules` (installed; load them). Read `CLAUDE.md` and `docs/ENCODING-GUIDE.md` of this repository before writing any L4, and `subjects/il/hvac-work-licensing-2025/encodings/legalese/` and `subjects/sg/employment-act-1968/encodings/naive-2026-10/` as worked examples (a law and its regulations in vintages; a seat layer over a longer encoding).

## Working rules

- Work only in `/Volumes/transcend/src/commonswt/sg-tv-receiver` (a git worktree on branch `sg/tv-receiver-2026-11`). **Do not commit, push, rebase or touch git state**: write files, and the orchestrator commits (commit trailers carry the session's identity). Keep new deposits in their own commits-to-be by keeping them in separate paths from the encodings.
- Put every temporary file in your scratchpad directory, never in `/tmp`. Raw downloads go in a new empty directory of their own under the scratchpad, never in the repository; copy the final text into `registers/source-bundle/` only after you have read it.
- Save as you go; update `PROGRESS.md` after each unit; a crash must lose little.
- **Order of work:** see "Scope" above (enumerate; the TV path first; the checkpoint; then the rest of the Act). Before any of it: read CLAUDE.md, the guide, directory conventions, the skills and the naive NOTES.md of your Act, and probe each source once, recording what it returned. Last: NOTES.md, the `check.sh` output and the `srcrefs` output.

## Report when done

A short report to the orchestrator: your answer to (1)–(3) at the three dates with the decisive sections; H1–H6 each confirmed/refuted/unanswered; what you could not source; the files written; the `check.sh` and `srcrefs` numbers; every place you were unsure; and your own token-relevant facts (number of context compactions you saw). Do not paste the encoding.
