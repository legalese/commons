#!/usr/bin/env python3
"""Coverage table for the Misrepresentation Act 1967 (Singapore) deposit.

Reads the deposited text (MA1967.txt), checks that every row's line range exists and that EVERY
non-blank line of the text falls in at least one row, checks that each row quotes words that really
are on its lines, and prints the table (markdown) and the counts.

Usage: python3 -I coverage.py RAW [--md]      (--md prints the markdown table; without it, counts only)
Exit status 1 if any non-blank line is in no row, a range is outside the file, or a row's key words
are not on its lines.

A row is (id, first line, last line, key words that must appear on those lines, provision, disposition, where / why).
Disposition is exactly one of: encoded, inert, fork, repealed-or-blank.  Rows may share a line (one line can
carry two provisions); no line may be left out.
"""
import re, sys

E, I, F, B = 'encoded', 'inert', 'fork', 'repealed or blank in this text'

ROWS = [
 # ---- front matter ------------------------------------------------------------------------------
 ('R01', 1, 14, 'MISREPRESENTATION ACT 1967', 'Title page: the statute series, the Act title, "2020 Revised Edition", the revision statement, the publisher block', I, 'reason 1: not operative (title, edition statement, publisher)'),
 ('R02', 16, 16, 'Misrepresentation Act 1967', 'Running title above the arrangement of sections', I, 'reason 1: not operative (title)'),
 ('R03', 18, 25, 'ARRANGEMENT OF SECTIONS', 'Arrangement of Sections (five entries). The converter has put each section number on a different line from its heading (lines 19-25), so the printed arrangement is misaligned; it is a table of contents and is not corrected', I, 'reason 1: not operative (table of contents / headings); the true headings are those printed above each section'),
 ('R04', 27, 27, 'An Act to amend the law relating to innocent misrepresentations', 'Long title', I, 'reason 1: not operative (long title, no rule)'),
 ('R05', 29, 29, '12 November 1993', 'Date line "[12 November 1993]"', I, 'reason 1: not operative (date of enactment / commencement line). s 4 states the same date in its own words and is encoded from there'),
 # ---- s 1 ---------------------------------------------------------------------------------------
 ('R06', 31, 32, 'Removal of certain bars', 'Heading to s 1: "Removal of certain bars to rescission for innocent misrepresentation"', I, 'reason 1: not operative (heading)'),
 ('R07', 34, 35, 'Where a person has entered into a contract', 's 1 chapeau: "Where a person has entered into a contract after a misrepresentation has been made to him, and"', E, '`s 1 the person is entitled to rescind notwithstanding the matters mentioned in paragraphs (a) and (b)` (ma-s01-rescission.l4), input `he has entered into a contract after a misrepresentation has been made to him`'),
 ('R08', 37, 37, 'the misrepresentation has become a term of the contract', 's 1(a): the misrepresentation has become a term of the contract', E, '`s 1(a) or (b) one or both of the matters mentioned in paragraphs (a) and (b) holds` (ma-s01-rescission.l4)'),
 ('R09', 39, 39, 'the contract has been performed', 's 1(b): the contract has been performed', E, '`s 1(a) or (b) one or both of the matters mentioned in paragraphs (a) and (b) holds` (ma-s01-rescission.l4)'),
 ('R10', 41, 42, 'or both, then, if otherwise he would be entitled', 's 1: "or both, then, if otherwise he would be entitled to rescind the contract without alleging fraud, he shall be so entitled"', E, '`s 1 the person is entitled to rescind notwithstanding ...` (ma-s01-rescission.l4); "or both" in the helper; the "if" is the input `otherwise he would be entitled to rescind the contract without alleging fraud`'),
 ('R11', 42, 43, 'subject to the', 's 1: "subject to the provisions of this Act"', F, 'F1 in NOTES.md; chosen reading: the s 1 rule answers on its own text and every other section is answered by its own rule (ma-s01-rescission.l4 header; seat comment on the s 1 question)'),
 ('R12', 43, 44, 'notwithstanding the matters mentioned in', 's 1: "notwithstanding the matters mentioned in paragraphs (a) and (b)"', E, '`s 1 the person is entitled to rescind notwithstanding the matters mentioned in paragraphs (a) and (b)` (ma-s01-rescission.l4)'),
 ('R13', 46, 49, '31.12.2021', 'Page furniture: page number "1", the date "31.12.2021", the running head "2 Misrepresentation Act 1967 2020 Ed."', I, 'reason 1: not operative (page header/footer of the printed edition)'),
 # ---- s 2 ---------------------------------------------------------------------------------------
 ('R14', 51, 51, 'Damages for misrepresentation', 'Heading to s 2: "Damages for misrepresentation"', I, 'reason 1: not operative (heading)'),
 ('R15', 53, 55, 'Where a person has entered into a contract after a', 's 2(1) where-limbs: "Where a person has entered into a contract after a misrepresentation has been made to him by another party thereto and as a result thereof he has suffered loss"', E, '`s 2(1) the person making the misrepresentation is liable to damages` (ma-s02-damages.l4), inputs `he has entered into a contract after a misrepresentation has been made to him by another party to it` and `as a result of it he has suffered loss`'),
 ('R16', 55, 57, 'if the person making', 's 2(1) "then, if the person making the misrepresentation would be liable to damages in respect thereof had the misrepresentation been made fraudulently"', E, 'same rule; input `the person making the misrepresentation would be liable to damages in respect of it had it been made fraudulently` (the law of deceit is not among the sources)'),
 ('R17', 57, 59, 'that person shall', 's 2(1) "that person shall be so liable notwithstanding that the misrepresentation was not made fraudulently"', F, 'F2 in NOTES.md; chosen reading: fraud is not a condition of the s 2(1) liability (the rule never asks it); implemented in the same rule'),
 ('R18', 59, 61, 'unless he proves', 's 2(1) proviso: "unless he proves that he had reasonable ground to believe and did believe up to the time the contract was made that the facts represented were true"', F, 'F3 in NOTES.md; chosen reading: the proviso turns on what has been PROVED, both limbs; `s 2(1) he proves reasonable ground to believe and belief up to the time the contract was made` and the same rule (ma-s02-damages.l4)'),
 ('R19', 63, 64, 'Where a person has entered into a contract after a', 's 2(2) where-limb: "Where a person has entered into a contract after a misrepresentation has been made to him"', E, '`s 2(2) the court or arbitrator may declare the contract subsisting and award damages in lieu of rescission` (ma-s02-damages.l4), input `he has entered into a contract after a misrepresentation has been made to him`'),
 ('R20', 64, 65, 'otherwise than', 's 2(2) "otherwise than fraudulently"', F, 'F4 in NOTES.md (QE); chosen reading: a limb of the same "Where" clause as the entitlement to rescind, so a fraudulent misrepresentation answers JUST FALSE (s 2(2) gives no power on these facts); input `the misrepresentation was made otherwise than fraudulently`'),
 ('R21', 65, 66, 'and he would be entitled, by reason of the', 's 2(2) "and he would be entitled, by reason of the misrepresentation, to rescind the contract"', E, 'same rule; input `he would be entitled, by reason of the misrepresentation, to rescind the contract` (the ground of rescission is not stated in the Act: s 1 removes two bars, the general law supplies the right)'),
 ('R22', 66, 68, 'then, if it is claimed', 's 2(2) "then, if it is claimed, in any proceedings arising out of the contract, that the contract ought to be or has been rescinded"', E, 'same rule; input `it is claimed, in proceedings arising out of the contract, that the contract ought to be or has been rescinded`'),
 ('R23', 68, 69, 'the court or arbitrator may declare', 's 2(2) "the court or arbitrator may declare the contract subsisting and award damages in lieu of rescission"', F, 'F5 in NOTES.md; chosen reading: the power is the named court or arbitrator only, any other body is NOTHING; rule above, the regulative rule `s 2(2) the permission of the court or arbitrator to declare the contract subsisting and award damages in lieu of rescission`, and `s 2(2) the body is a "court" (Interpretation Act s 2(1))` (ma-reading.l4)'),
 ('R24', 69, 70, 'if of', 's 2(2) "if of opinion that it would be equitable to do so"', E, 'same rule; the judgment is the court\'s or arbitrator\'s and is a plain input `it is of opinion that it would be equitable to declare the contract subsisting and award damages in lieu of rescission` (Guide section 4: a judgment handed to someone else is never guessed)'),
 ('R25', 70, 73, 'having regard to the nature', 's 2(2) "having regard to the nature of the misrepresentation and the loss that would be caused by it if the contract were upheld, as well as to the loss that rescission would cause to the other party"', F, 'F6 in NOTES.md; chosen reading: a matter not regarded makes the answer NOTHING; `s 2(2) the opinion was formed having regard to the three matters the text names` and the rule above (ma-s02-damages.l4)'),
 ('R26', 75, 76, 'Damages may be awarded against a person under subsection (2)', 's 2(3) first limb: "Damages may be awarded against a person under subsection (2) whether or not he is liable to damages under subsection (1)"', F, 'F7 in NOTES.md; chosen reading: liability under (1) is not a condition of the power in (2), the other conditions of (2) remain; `s 2(3) damages may be awarded under subsection (2) whether or not he is liable to damages under subsection (1)` (ma-s02-damages.l4)'),
 ('R27', 76, 78, 'but where', 's 2(3) second limb: "but where he is so liable any award under subsection (2) shall be taken into account in assessing his liability under subsection (1)"', E, '`s 2(3) an award under subsection (2) is to be taken into account in assessing his liability under subsection (1)` (the "where" and the duty) (ma-s02-damages.l4)'),
 ('R28', 77, 78, 'taken into', 's 2(3) "shall be taken into account in assessing his liability"', F, 'F8 in NOTES.md; chosen reading: the award itself is the amount taken into account and no net figure is worked out; `s 2(3) the amount of the award under subsection (2) that is to be taken into account` (ma-s02-damages.l4)'),
 # ---- s 3 ---------------------------------------------------------------------------------------
 ('R29', 80, 81, 'Avoidance of provision excluding liability', 'Heading to s 3: "Avoidance of provision excluding liability for misrepresentation"', I, 'reason 1: not operative (heading)'),
 ('R30', 83, 83, 'If a contract contains a term which would exclude or restrict', 's 3 chapeau: "If a contract contains a term which would exclude or restrict"', E, '`s 3(a) or (b) the contract contains a term of a kind that section 3 reaches` (ma-s03-exclusion.l4)'),
 ('R31', 85, 87, 'any liability to which a party', 's 3(a): "any liability to which a party to a contract may be subject by reason of any misrepresentation made by him before the contract was made"', E, '`s 3(a) or (b) ...`, input `the term would exclude or restrict any liability to which a party to a contract may be subject by reason of a misrepresentation made by him before the contract was made`'),
 ('R32', 88, 88, '2020 Ed.', 'Page furniture: running head "2020 Ed. Misrepresentation Act 1967 3" inside s 3', I, 'reason 1: not operative (page header of the printed edition)'),
 ('R33', 90, 91, 'any remedy available to another party', 's 3(b): "any remedy available to another party to the contract by reason of such a misrepresentation"', E, '`s 3(a) or (b) ...`, input `the term would exclude or restrict any remedy available to another party to the contract by reason of such a misrepresentation`'),
 ('R34', 93, 95, 'that term shall be of no effect', 's 3 "that term shall be of no effect except in so far as it satisfies the requirement of reasonableness as stated in section 11(1) of the Unfair Contract Terms Act 1977"', E, '`s 3 the term is of no effect` and `s 3 the term is of no effect, it being for those claiming that it satisfies the requirement to show that it does` (ma-s03-exclusion.l4); the reasonableness test is the plain input `the term satisfies the requirement of reasonableness as stated in section 11(1) of the Unfair Contract Terms Act 1977` (that Act is not among the sources)'),
 ('R35', 93, 94, 'except in so far as', 's 3 "except in so far as it satisfies the requirement"', F, 'F9 in NOTES.md (QA); chosen reading: the bar question answers JUST FALSE once the exception is met, and the rule is asked of the term or the part of it in question'),
 ('R36', 95, 96, 'it is for those claiming', 's 3 "and it is for those claiming that the term satisfies that requirement to show that it does"', F, 'F10 in NOTES.md; chosen reading: a burden placed on those claiming, answered by its own rule `s 3 it is for those claiming that the term satisfies that requirement to show that it does` and also read with the bar in `s 3 the term is of no effect, it being for those claiming that it satisfies the requirement to show that it does` (a showing not made means the term is of no effect); `s 3 the term is of no effect` keeps the requirement as a fact (ma-s03-exclusion.l4)'),
 # ---- s 4, s 5 ----------------------------------------------------------------------------------
 ('R37', 98, 98, 'Saving for past transactions', 'Heading to s 4: "Saving for past transactions"', I, 'reason 1: not operative (heading)'),
 ('R38', 100, 101, 'Nothing in this Act applies', 's 4 "Nothing in this Act applies in relation to any misrepresentation or contract of sale made before 12 November 1993"', E, '`s 4 nothing in this Act applies in relation to the misrepresentation or contract of sale` and the helpers `s 4 the misrepresentation or contract of sale was made before 12 November 1993`, `s 4 the date on which it was made is before 12 November 1993` (ma-s04-saving.l4)'),
 ('R39', 100, 101, 'contract of sale', 's 4 "any misrepresentation or contract of sale"', F, 'F12 in NOTES.md; chosen reading: the second limb reaches a contract of sale only'),
 ('R40', 101, 101, 'made before 12 November 1993', 's 4 "made before 12 November 1993" (the period or scope limit)', F, 'F11 in NOTES.md; chosen reading: a date the text fixes in its own words (ruling (a)), so JUST FALSE (s 4 does not bar the Act) for a thing made on or after that day; the day itself, 12 November 1993, is not "before"'),
 ('R41', 101, 103, 'except in so far as it', 's 4 "except in so far as it was applicable by virtue of section 5 of the Civil Law Act 1909 in force before that date"', F, 'F13 in NOTES.md (QA); chosen reading: JUST FALSE once the exception is met; the fact is the plain input `it was applicable by virtue of section 5 of the Civil Law Act 1909 in force before that date` (the Civil Law Act 1909 is not among the sources)'),
 ('R42', 105, 105, 'Short title', 'Heading to s 5: "Short title"', I, 'reason 1: not operative (heading)'),
 ('R43', 106, 106, 'This Act may be cited', 's 5: "This Act may be cited as the Misrepresentation Act 1967."', I, 'reason 2: machinery (short title). No function; the row in Jural relations is "none"'),
 ('R44', 108, 108, '31.12.2021', 'Page furniture: the date "31.12.2021" under s 5', I, 'reason 1: not operative (page footer of the printed edition)'),
 # ---- legislative history ----------------------------------------------------------------------
 ('R45', 109, 110, 'LEGISLATIVE HISTORY', 'Legislative History: heading and Act title', I, 'reason 1: not operative (heading of a service the text says is not part of the Act)'),
 ('R46', 112, 113, 'It is not part of the Act', 'Legislative History: "This Legislative History is a service provided by the Law Revision Commission on a best-efforts basis. It is not part of the Act."', I, 'reason 1: not operative (the text says it is not part of the Act)'),
 ('R47', 115, 122, 'Commencement', 'Legislative History item 1: U.K. 1967, c. 7; Commencement 22 April 1967; Application 12 November 1993; note on the Application of English Law Act 1993', I, 'reason 1: not operative (not part of the Act); the Act\'s own commencement is machinery (reason 2) and affects no one now. s 4 uses the 12 November 1993 date from its own words'),
 ('R48', 124, 126, '1994 Revised Edition', 'Legislative History item 2: 1994 Revised Edition (Chapter 390), Operation 20 May 1994', I, 'reason 1: not operative (not part of the Act)'),
 ('R49', 128, 128, 'Abbreviations', 'Heading of the table of abbreviations', I, 'reason 1: not operative (heading)'),
 ('R50', 130, 130, 'C.P.', 'Abbreviation "C.P." (Council Paper)', I, 'reason 1: not operative (abbreviation table, not part of the Act)'),
 ('R51', 132, 132, 'G.N. No. S (N.S.)', 'Abbreviation "G.N. No. S (N.S.)"', I, 'reason 1: not operative (abbreviation table)'),
 ('R52', 134, 134, 'G.N. No.', 'Abbreviation "G.N. No."', I, 'reason 1: not operative (abbreviation table)'),
 ('R53', 136, 136, 'G.N. No. S', 'Abbreviation "G.N. No. S"', I, 'reason 1: not operative (abbreviation table)'),
 ('R54', 138, 138, 'G.N. Sp. No. S', 'Abbreviation "G.N. Sp. No. S"', I, 'reason 1: not operative (abbreviation table)'),
 ('R55', 140, 140, 'L.A.', 'Abbreviation "L.A."', I, 'reason 1: not operative (abbreviation table)'),
 ('R56', 142, 144, 'L.N.', 'Abbreviation "L.N."', I, 'reason 1: not operative (abbreviation table)'),
 ('R57', 146, 146, 'M. Act', 'Abbreviation "M. Act"', I, 'reason 1: not operative (abbreviation table)'),
 ('R58', 148, 148, 'M. Ordinance', 'Abbreviation "M. Ordinance"', I, 'reason 1: not operative (abbreviation table)'),
 ('R59', 150, 150, 'Parl.', 'Abbreviation "Parl."', I, 'reason 1: not operative (abbreviation table)'),
 ('R60', 152, 153, 'S.S.G.G. (E) No.', 'Abbreviation "S.S.G.G. (E) No."', I, 'reason 1: not operative (abbreviation table)'),
 ('R61', 155, 155, 'S.S.G.G. No.', 'Abbreviation "S.S.G.G. No."', I, 'reason 1: not operative (abbreviation table)'),
 ('R62', 157, 157, '31.12.2021', 'Page furniture: the date "31.12.2021" at the end of the file', I, 'reason 1: not operative (page footer of the printed edition)'),
]

def main():
    raw = open(sys.argv[1], encoding='utf-8').read().split('\n')
    if raw and raw[-1] == '':
        raw = raw[:-1]
    n = len(raw)
    nonblank = [i for i, l in enumerate(raw, 1) if l.strip()]
    covered = set()
    problems = []
    seen = set()
    for (rid, a, b, key, prov, disp, why) in ROWS:
        if rid in seen: problems.append(f'{rid}: duplicate id')
        seen.add(rid)
        if disp not in (E, I, F, B): problems.append(f'{rid}: bad disposition {disp!r}')
        if not (1 <= a <= b <= n): problems.append(f'{rid}: range {a}-{b} outside the file ({n} lines)'); continue
        block = re.sub(r'\s+', ' ', ' '.join(raw[a-1:b]))
        if re.sub(r'\s+', ' ', key) not in block:
            problems.append(f'{rid}: key words {key!r} are not on lines {a}-{b}')
        covered.update(range(a, b + 1))
    uncovered = [i for i in nonblank if i not in covered]
    for i in uncovered:
        problems.append(f'line {i} is in no row: {raw[i-1].strip()[:70]!r}')
    counts = {d: sum(1 for r in ROWS if r[5] == d) for d in (E, I, F, B)}
    inert1 = sum(1 for r in ROWS if r[5] == I and r[6].startswith('reason 1'))
    inert2 = sum(1 for r in ROWS if r[5] == I and r[6].startswith('reason 2'))
    inert3 = sum(1 for r in ROWS if r[5] == I and r[6].startswith('reason 3'))
    if '--md' in sys.argv:
        print('| row | lines | provision | disposition | where it is encoded, or why not |')
        print('| --- | --- | --- | --- | --- |')
        for (rid, a, b, key, prov, disp, why) in ROWS:
            rng = f'{a}' if a == b else f'{a}-{b}'
            esc = lambda s: s.replace('|', '\\|')
            print(f'| {rid} | {rng} | {esc(prov)} | {disp} | {esc(why)} |')
    print(f'coverage: {len(nonblank)} non-blank lines of {n} lines; {len(nonblank) - len(uncovered)} covered by at least one row; {len(uncovered)} in no row')
    print(f'coverage: {len(ROWS)} rows: ' + ', '.join(f'{counts[d]} {d}' for d in (E, I, F, B)) + f' (inert: {inert1} reason 1, {inert2} reason 2, {inert3} reason 3)')
    for p in problems: print('PROBLEM', p)
    sys.exit(1 if problems else 0)

main()
