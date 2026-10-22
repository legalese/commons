# NOTES — sg-miles-card, row `legalese-2026-10`

Written 2026-10-21 by one model agent in one session.
Revised 2026-10-22 by a second session, which added one document and changed the Standard Chartered Smart modules (section 8).
Nothing here has been reviewed by a person (`encoding.json` says `draft`, with `not_reviewed`).
The sentences below say what was checked and how; where a statement could not be checked it says so.

## 0. What this row is

A second encoding row of the subject, beside `legalese` (2026-09-21), which is left as it was.
The earlier row has fourteen modules over ten documents.
This row has twenty-two files over 29 documents, and adds the Standard Chartered Smart, Trust Freedom, UOB Preferred Visa, UOB Visa Signature, UOB PRVI Miles, UOB Lady's Savings Account Rewards and Citi PremierMiles terms that the earlier row did not hold.

**Row name.** `legalese-2026-10` is the name this run gave it. Assumed, not ruled.
**Base.** `origin/main` of this repository at `6f3153f94`. Both predecessor pull requests (the sources-by-link change and its l4-ide counterpart) were already merged, so nothing here sits on an unmerged branch.
**Seat.** The cardholder: the person who holds the cards and asks what a purchase earns.
**Target compiler.** On 2026-10-21 the modules were checked on `unstable` only.
`l4 --version` printed `dev`; the binary was `~/.cabal/bin/l4`, built 2026-10-20 19:20, and the l4-ide checkout it was assumed to come from was `origin/unstable` at `d52683bc4` (the binary's provenance was not verified).
The default target for this repository is `main`.
On 2026-10-22 `check.sh` was run with that default: every module had the same four counts on the `main` build as on the `unstable` binary (`fetch-main-l4.sh` fetched build 99, `1.6.99 (main, 6cc2c91, 2026-10-21)`).
The `unstable` binary that day was `~/.cabal/bin/l4`, a symlink into the cabal store dated 2026-10-21 23:01 (local time), with `l4 --version` printing `dev`; its date differs from that of the build named for 2026-10-21, and its provenance was not verified.

## 1. The documents

29 documents, each pinned in `registers/source-bundle.json` by URL and sha256, none vendored.
`source/fetch.sh` re-fetches all 29 and refuses any digest mismatch; run 2026-10-21 (28 documents) and again 2026-10-22 (29, after the PDF was added) it reported `ok` for every one and exited 0.
Five are held by the digest of the clause text between two marker lines, because the page's bytes change on every request: the Standard Chartered Smart promotion terms (web page) and retail exclusions, two Trust Bank pages, and the HeyMax article.
The Standard Chartered Smart promotion terms are held twice, as that web page and as a PDF headed 'Version 13 November 2025'.
They differ in the EV-charging footnote and in one row of the cl.7 table (fork `F-sc-ev`; `registers/source-bundle.json` says where).

Roles in the bundle: 19 `current` issuer terms, 7 `guidance` (FAQs, and the HeyMax article), 2 `historical` (the PAssion terms of 2025 and the Standard Chartered Smart terms of August 2024), 1 `instrument` (the DBS Rewards Programme terms).
Five documents fetched during the work are not in the bundle: the Citi ThankYou Rewards terms (16 December), the HSBC Everyday+ Rewards Programme terms, the PRVI foreign-currency campaign terms (expired 30 June 2026), the Trust credit cards landing page, and a second copy of the Standard Chartered Smart promotion terms marked INTERNAL.
The Version 13 November 2025 PDF of those terms was added to the bundle on 2026-10-22; whether it is the copy marked INTERNAL in that list was not established, and both Standard Chartered PDFs held carry an INTERNAL header.
The working session left them out as not needed for an earn rule; that judgment was not re-checked in this write-up, so treat them as candidates if a gap shows.

**Added at the owner's instruction:** `heymax-trust-welcome-bonus-tnc` (help.heymax.ai).
It is not an issuer document, and its own cl.7.2 says Trust Bank's terms govern eligibility and Qualified spend.
No other non-issuer source is held: no blog and no card-maximiser page.

**Finding.** Citi PremierMiles earn terms *are* held: the Cardmember's Agreement, Program Terms and Conditions cl.3.1, gives 1.2 Citi Miles per S$1 locally and 2.2 overseas.
The earlier row held no PremierMiles terms; the agreement does state them.

## 2. The modules

| file | document set | what it encodes |
| --- | --- | --- |
| `cards-domain.l4`, `earn-kernel.l4`, `fixtures.l4` | none | the shared ontology (22 cards, purchases, holders, months, the `Earn answer` record), rounding and bracketing helpers, test fixtures |
| `dbs-yuu.l4` | DBS yuu Card terms | Base 1 / 0.5, cl.7(a) and (b) Bonus, the S$800 and four-merchant floor, the 28,800-point cap, Appendix 1 carve-outs |
| `dbs-rewards.l4`, `dbs-womans.l4` | DBS Rewards Programme, Woman's Card | exclusions; online Bonus, 9X/7X, S$1,000 cap |
| `posb-passion.l4` | PAssion terms of 29 April 2026 | 3X Base, Tier 1 and Tier 2 bonus, caps, Participating Stores, promotion to 31 December 2026 |
| `citi-exclusions.l4`, `citi-10x.l4`, `citi-visa-wind-down.l4`, `citi-premiermiles.l4` | Citi exclusion list, 10X terms and FAQ, Visa FAQ, PremierMiles agreement | exclusions; two limbs of the bonus; the Visa wind-down; the flat rate |
| `hsbc-revolution.l4` | Revolution terms of 1 April 2026 and FAQ | whitelist, contactless-or-online gate, 9 bonus points, 9,000 cap |
| `uob-ladys.l4`, `uob-ladys-savings.l4` | Lady's Cards terms, Lady's Savings Account Rewards | two elected categories, 9X Bonus UNI$, the savings uplift |
| `uob-preferred-visa.l4`, `uob-visa-signature.l4`, `uob-prvi.l4` | UOB Ver 3.0, Ver 2.1, Ver 3.4 | the pots, hurdles, local and overseas rates, travel partner rates |
| `sc-exclusions.l4`, `sc-smart.l4` | Standard Chartered exclusions and Smart promotion (web page and PDF) | the 0.5% / 8% / 10% tiers by statement-month spend; the EV-charging window to 31 December 2026; the exclusions, including recurring payments |
| `trust-freedom-miles.l4`, `trust-spend-and-get.l4` | Trust page, redemption terms, Spend & Get, HeyMax | 1.3 Trust Miles per S$1 awarded per S$5; the welcome-bonus tiers as lumps on crossing |
| `cards.l4` | none | the composer: one call asks all twelve programmes what a purchase earns |

Every module's header names its document, the clauses it reads, and its numbered forks.
Every answer is a floor, a ceiling, the conditions it depends on, the pot it draws on, and the clause it rests on.
Miles are `NOTHING` where no held document converts the unit (HSBC points, Citi ThankYou points, Standard Chartered points); that is not zero miles.

## 3. Forks

28, in `registers/fork-register.json`; it validates against `registers/external-modifications.json` and `registers/source-bundle.json` with the pipeline's register validator, run 2026-10-21 and again 2026-10-22 after the revision (all three: ok each time).
They were written after the modules, from the module headers, by the agent that wrote the modules.
Most are floor/ceiling forks: the module returns both ends and names `A reading of the text is open (see the fork register)` rather than taking a reading.
The ones that matter most for a reader:

- `F-yuu-stack`: cl.7(a) and cl.7(b) add (10.08 mpd) or the second replaces the first (7.56).
- `F-uob-per-five`: UNI$ "per S$5" in whole blocks or pro rata.
- `F-singtel-base`, `F-bill-payments`: whether a Singtel or other bill paid straight on the card is a "bill payment".
- `F-trust-tier-additivity`: **a flagged conflict, not a choice.** The Trust product page prints three Max Miles figures joined by OR (20,000; 50,000; 100,000, which sum to 170,000) without saying whether they accumulate. HeyMax cl.3.1 prints codes of 20,000, a further 30,000 and a further 50,000, capped at 100,000. Each tier is encoded as a lump on crossing: the HeyMax code is the floor and the page's figure the ceiling, and a purchase that crosses only the first tier carries no conflict because both say 20,000.
- `F-trust-sprint-exclusions`, `F-trust-ongoing-exclusions`: HeyMax lists 32 excluded MCCs for the welcome bonus and says the list "also applies to Trust Freedom Card ongoing rewards"; the issuer's page excludes nothing. Floor 0 at a listed code, ceiling the full earn.
- `F-citi-visa-date`, `F-pm-visa`: held text against a secondary source's later report (`registers/external-modifications.json`).
- `F-sc-ev`: **two held Standard Chartered documents disagree, and the module takes one.**
  The PDF headed 'Version 13 November 2025' says the EV-charging bonus is applicable to 31 December 2026; the web page says 31 December 2025.
  `sc-smart.l4` takes the PDF.
  This is not a floor/ceiling fork: the other reading stays live in the register and is a one-constant change.
  Assumed, not ruled (section 6).
- `F-sc-recurring`: the exclusions page excludes recurring payments (charges under a standing instruction), while the Smart promotion names Netflix and Spotify as Bonus Merchants.
  Not resolved: a subscription charge at a named Bonus Merchant is bracketed, floor nothing, ceiling the Bonus Merchant answer.

## 4. Checks

`L4=$HOME/.local/bin/l4 L4_TARGET=unstable ./check.sh`, run 2026-10-21: exit 0, 22 files, 821 assertions satisfied, 0 failed, 0 refused, 0 other errors.
Run 2026-10-22 on `origin/main` at `aaaf0d704` before any edit, with the binary named in section 0: 821 satisfied on `unstable`, the same per-module counts as 2026-10-21, and 821 on the `main` build too.
Run 2026-10-22 after the revision, `L4=$(which l4) ./check.sh` with the default target: exit 0, 22 files, 860 assertions satisfied, 0 failed, 0 refused, 0 other errors, every module `same` on the `main` build.
The same revision on `L4_TARGET=unstable` gave the same 860.
The 39 added assertions are in `sc-smart.l4` (35 to 49) and `sc-exclusions.l4` (47 to 72); no other module's count moved.
The two edited modules give no linter warning before or after.
A prose-only edit pass followed an earlier run of the same script on the same binary and target; the per-module counts before and after were identical.
The linter reports "AND and OR operators appear at the same indentation level" as a warning in several modules; none was fixed in this run.

## 5. Not done

- **The pipeline's phases p3 to p9 were not run against this row.** The pipeline reads a sidecar whose paths point at the earlier row, and running it here would have needed an uncommitted local sidecar variant. So: no goldens, no `registers/roadmap.json`, no `COMPLETION.md`, no report, and no gate; `encoding.json` says `hg1` is not signed.
- The `main` compiler comparison was not done on 2026-10-21; it was done on 2026-10-22 (section 0, section 4).
- The lowering of the encoding into app data.
- Allocation: which purchase to put on which card so that the caps fill. The composer returns answers; it does not choose.
- The linter warnings (§4).
- The `Trust Freedom` card's own terms and the "Trust / NTUC Link credit card product terms" are not held, so every Trust answer says the unheld terms may exclude the spend.

## 6. Assumed, not ruled

Each of these is a choice this run made that a reader could reasonably make differently.

1. The row name `legalese-2026-10`.
2. The shared kernel module, `earn-kernel.l4`, and its helpers (the floor/ceiling `Earn answer`, the brackets).
3. A merchant category code that is not known is bracketed between an excluded and an ordinary code, not guessed.
4. A merchant indicator that is not known is bracketed, not guessed.
5. In every floor/ceiling fork the floor is the reading that pays less.
6. HeyMax's MCC list is treated as a bracket for Trust (floor 0), not as a fact about Trust's own terms.
7. The Trust fixtures use 22 September 2026 as the approval date, inside HeyMax's stated window (21 September to 31 October 2026); the earlier fixture date was outside it.
8. `F-sc-ev`: the Standard Chartered PDF (Version 13 November 2025) governs over the undated web page where they disagree about the end of the EV-charging bonus.
   The reason is that the PDF states a version date and the page states none, and the page still prints a row that the PDF has dropped.
   That the page is the older text is inferred.
9. `F-sc-recurring`: the floor for a subscription charge at a named Bonus Merchant is nothing (the recurring-payment sentence applies), and the ceiling is the Bonus Merchant answer.
10. ATM transactions are read as cash advances.
    `SingPost-SAM` is left out of the AXS and SAM exclusion because the page does not name it (`sc-exclusions.l4`).

## 7. For a successor

- L4 gotchas met: parenthesise a genitive argument (`f (x's y)`); `NOT` reaches to the end of a line; each mixfix function needs a unique leading phrase and its calls must stay on one line; a non-last `LIST OF` parameter goes on its own line; `l4 run`'s exit status is unreliable, so count `assertion satisfied` and `assertion failed`.
- Fixtures must carry every fact a rule reads: PRVI's overseas rule reads the payment gateway, and an in-person tap abroad with the default Singapore gateway was answered at the local rate until the fixture carried an overseas gateway.
- Before relying on a cap's date basis, read the document: Visa Signature, Preferred Visa and Citi state a period and no date basis.

## 8. Revision of 2026-10-22

A second session revised the row to check Standard Chartered's EV-charging bonus against the issuer's own documents.
What it did:

- Held a second rendering of the Smart promotion terms: the PDF headed 'Version 13 November 2025' (`sc-smart-promo-tnc-2025-11`), found through the link in a MileLion article.
  It differs from the web page in the EV-charging footnote (to 31 December 2026 against 31 December 2025; credited within 4 months against 3) and in one row of the cl.7 table that the page still prints and the PDF has dropped.
  Nothing else differs, compared sentence by sentence and by word counts.
- Revised fork `F-sc-ev`: `sc-smart.l4` now takes the PDF, so an EV charge posted to 31 December 2026 is a Bonus Merchant Transaction.
  The web page's reading stays live in the register.
  Assumed, not ruled (section 6, item 8).
- Read `sc-exclusions.l4` against the exclusions page text.
  It asserted that an AXS statement line is not excluded, while the page excludes "AXS, SAM or ATM transactions made using your Card"; that assertion is reversed and SAM added.
  Insurance premiums and betting payments, which the page excludes, were not encoded and now are, through two new `Item` constructors in `cards-domain.l4`.
  All thirty-five listed MCCs are now asserted.
- Added fork `F-sc-recurring`, found on that reading: the page excludes recurring payments, and the Smart promotion names streaming subscriptions as Bonus Merchants.
  It is bracketed, not resolved.
- Corrected the web page's clause count in `registers/source-bundle.json` from 1-18 to 1-21 (the page's numbered lists run to 21, as the PDF's do).

What it did not do:

- It did not check a statement line against either reading of `F-sc-ev`.
  SC credits the EV bonus within 3 months (the page) or 4 months (the PDF) of the transaction, so a charge posted in 2026 would show the bonus on a statement within that time if the PDF governs and would not if the page does.
  That would settle the fork.
- It did not touch the earlier row, `../legalese`, which holds no Standard Chartered terms.
- The fraud, rolled-over-amount and tax-refund classes and the closing catch-all of the exclusions page are not encoded (`sc-exclusions.l4` header).
- `registers/source-bundle.json` note (3) still says four web pages where `source/fetch.sh` says five; not changed here.
