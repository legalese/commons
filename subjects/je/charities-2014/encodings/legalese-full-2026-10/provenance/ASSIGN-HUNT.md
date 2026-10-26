FLEET_DIR = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full

# ASSIGNMENT: CONTRADICTION HUNT (blind)

You are the HUNTER. You read the Charities (Jersey) Law 2014 and nothing else, and you find what is wrong with the text itself.
You have not seen any encoding of the Law and you must not look for one. You do not write L4 and you do not run l4.

## What you may read
FLEET_DIR/BRIEF.md (only to learn the cleanroom rules and the vintage facts), and in FLEET_DIR/inputs: charities-jersey-law-2014-2026-10-02.txt (the text; `src:N` means line N), charities-jersey-law-2014-official-pdf-text-layer.txt, the instruments in amending/, and SOURCE-LICENSE.md. Nothing else: not FLEET_DIR/deposit, not FLEET_DIR/phase1, not FLEET_DIR/work, not FLEET_DIR/skills, not anything outside FLEET_DIR except what you need to quote. Write only under FLEET_DIR/work/hunt/.

## What to hunt
Read the whole Law slowly, three times: once for structure; once as an opposing lawyer looking for a way to win on the words; once as a regulator looking for a case the Law cannot decide. Find every:
- contradiction: two provisions that give different answers to the same facts;
- dangling or wrong cross-reference: a reference to an Article, paragraph or defined term that does not exist, that says something different from what the reference assumes, or that was renumbered (read the Table of Renumbered Provisions in the endnotes and check whether any cross-reference still uses an old number);
- definition problem: circular, over- or under-inclusive, defined but unused, used but undefined, or defined twice;
- connective ambiguity: a list whose 'and' or 'or' can be read two ways;
- scope gap: a case no provision covers, or covers twice;
- power without a procedure, duty without a sanction or sanction without a duty, offence without a stated maximum;
- temporal problem: a provision that cannot apply on the day the endnotes say it commenced, a power exercised before the provision it relies on is in force, an amendment that does not fit the text it amends;
- inconsistency between the consolidated text and the amending instruments, or between the HTML-derived text and the PDF text layer.
Be adversarial and precise. Do not report style complaints.

## What to write
FLEET_DIR/work/hunt/CONTRADICTIONS.md : numbered findings, each with: the provisions (with `src:N` lines), the type (from the list above), a quotation of the exact words (use the text file; do not retype), why it is a problem, a minimal discriminating case (facts, who, when) on which the two readings give different results, severity (blocks a decision / changes an outcome / cosmetic), and your confidence. Order by severity. End with a list of the provisions you read and found clean, so a reader can see what you covered.

## Final report
The number of findings by type and by severity; the five most serious in one line each; the provisions you could not read properly and why; peeked: nothing, or what.
