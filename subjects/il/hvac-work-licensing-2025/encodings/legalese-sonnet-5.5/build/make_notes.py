#!/usr/bin/env python3
"""Generate deposit/NOTES.md.  The coverage counts, the file list and the check.sh output are computed
here, not typed, so that they cannot drift from the files they describe."""
import pathlib, subprocess, collections, datetime

W = pathlib.Path(__file__).resolve().parent.parent
DEP = W / 'deposit'
L4 = '/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-41dd7a67/bin/l4'

# (id, provision, heading / what it is, disposition, where)
M = {
    'nouns': 'hvac-nouns.l4',
    'fees': 'hvac-fees-regs.l4',
    's63': 'hvac-law-s63-commencement.l4',
    's6': 'hvac-law-s6-second-schedule.l4',
    's8': 'hvac-law-s8-validity.l4',
    's23': 'hvac-law-s2-s3-licensing-duty.l4',
    's79': 'hvac-law-s7-s9-exemption-and-temporary-licence.l4',
    's1617': 'hvac-law-s16-s17-duties-of-licensee.l4',
}
E, I, X, R = 'encoded', 'inert', 'out-of-scope', 'refused'
rows = []


def row(prov, what, disp, where):
    rows.append((prov, what, disp, where))


# ---- the Law
row('Law s 2, "מערכת קירור או מיזוג אוויר", "מערכת"', 'system: purpose is removal of heat, by a refrigerant', E, M['s23'])
row('Law s 2, "עבודה במערכת קירור או מיזוג אוויר"', 'work: an act of a type fixed in the First Schedule', E, M['s23'])
row('Law s 2, "רישיון", "רישיון דרגה 1/2/3"', 'the three grades by cooling output (18 kW, 70 kW, any)', E, M['s23'])
row('Law s 2, "תעודת גמר" (1)', 'Division certificate, exam passed incl. theory and practical', E, M['s23'])
row('Law s 2, "תעודת גמר" (2)', 'Ministry of Education climate-control certificate', E, M['s23'])
row('Law s 2, the other 13 definitions', 'אגף להכשרה מקצועית, בעל רישיון, חוק ההנדסאים והטכנאים המוסמכים, חוק החשמל, חוק העונשין, המועצה, מפקח, המפקח הבכיר, מרשם ההנדסאים והטכנאים המוסמכים, המשרד, קרר, הרשם, השר: offices and cross-references, not rules', I, M['nouns'])
row('Law s 3(a)', 'duty to hold a licence of the appropriate type (rule and prohibition)', E, M['s23'])
row('Law s 3(b)', "Minister's exemption order: a fact on the piece of work", E, M['nouns'] + ', ' + M['s23'])
row('Law s 3(c)', "Minister's power to amend the First Schedule", I, M['s23'] + ' (comment)')
row('Law s 6(a) chapeau', 'the Registrar shall give a licence', E, M['s6'])
row('Law s 6(a)(1)', 'an adult', E, M['s6'])
row('Law s 6(a)(2)', 'Israeli citizen or resident', E, M['s6'])
row('Law s 6(a)(3)', 'no conviction or pending indictment that makes unfit, in the Registrar\'s opinion', E, M['s6'])
row('Law s 6(a)(4)', 'one of the qualifying conditions, all per the Second Schedule', E, M['s6'])
row('Law s 6(a)(4)(a)', 'holds a final certificate', E, M['s6'])
row('Law s 6(a)(4)(b)', 'registered in the registry of practical engineers and technicians', E, M['s6'])
row('Law s 6(a)(4)(c)', 'completed supplementary studies, if required', E, M['s6'])
row('Law s 6(b)', "Minister's power to amend the Second Schedule", I, M['s6'] + ' (comment)')
for part, items in (('A (Grade 1)', 3), ('B (Grade 2)', 6), ('C (Grade 3)', 8)):
    for n in range(1, items + 1):
        extra = ' (three-year row)' if (part[0], n) in (('A', 2), ('B', 4), ('C', 5)) else ''
        row('Second Schedule Part %s, item %d%s' % (part, n, extra), 'columns A, B' + (' and C' if extra else ''), E, M['s6'])
row('Law s 7(a)', 'exemption from the electrical chapter', E, M['s79'])
row('Law s 7(b)', 'exemption from the working-at-heights chapter', E, M['s79'])
row('Law s 7(c)', 'duty to publish instructions', E, M['s79'])
row('Law s 8', 'validity: first period encoded; renewal conditions encoded; renewed period REFUSED', E, M['s8'])
row('Law s 9(a)(1)', 'invited to work on a system above 70 kW', E, M['s79'])
row('Law s 9(a)(2)', 'authorised abroad, similar work in the six years before the application', E, M['s79'])
row('Law s 9(a)(3)', 'recognised by the Registrar as reputed and renowned', E, M['s79'])
row('Law s 9(a)', 'the Registrar may give a temporary Grade 3 licence, up to one year', E, M['s79'])
row('Law s 9(b)', 'the Registrar may renew for two further periods of up to one year', E, M['s79'])
row('Law s 16', 'tell the Registrar of a change in details within 30 days', E, M['s1617'])
row('Law s 17(a)', 'at least eight hours of refresher training in the last year of validity', E, M['s1617'])
row('Law s 17(b)', "the Registrar's additional specific requirement", E, M['s1617'])
row('Law s 17(c)', 'extension of validity, up to three months', E, M['s1617'])
row('Law s 17(d)', 'the duty is deemed a licence condition', E, M['s1617'])
row('Law s 17(e)', "the Registrar shall ensure trainings exist and are available", E, M['s1617'])
row('Law s 17(f)', 'the Registrar shall publish trainings a reasonable time before', E, M['s1617'])
row('Law s 63(a)(1)', 'commencement for listed flammable refrigerants; the Commencement Day', E, M['s63'])
row('Law s 63(a)(2)', 'commencement for any other refrigerant: 18 months later', E, M['s63'])
row('Law s 63(b)', 'commencement of Chapter 6', E, M['s63'])
# ---- the Fees Regulations
row('Fees Regs preamble (authority ss 59-60; approvals)', 'enabling words', I, M['fees'] + ' (comment)')
row('Fees Regs reg 1, as made', 'definition of the practical exam', E, M['fees'])
row('Fees Regs reg 1, as amended (12383 s 1)', 'adds the theory exam definition', E, M['fees'])
row('Fees Regs reg 1, draft', 'both definitions (screenshot, partly legible)', E, M['fees'])
for lab in ('(a)', '(b)', '(c)', '(d)'):
    row('Fees Regs reg 2%s, as made' % lab, 'fee', E, M['fees'])
for lab in ('(a)', '(a1)', '(b)', '(c)', '(d)'):
    row('Fees Regs reg 2%s, as amended' % lab, 'fee' + (' (12383 s 2(1), inserted)' if lab == '(a1)' else (' (12383 s 2(2), amended)' if lab == '(b)' else '')), E, M['fees'])
for lab in ('(א)', '(ב)', '(ג)', '(ד)', '(ה)'):
    row('Fees Regs reg 2%s, draft' % lab, 'fee (screenshot)', E, M['fees'])
row('Fees Regs reg 3(a) incl. its three definitions, as made and as amended', 'annual update by the index, rounded', E, M['fees'])
row('Fees Regs reg 3(b), as made and as amended', 'the Director General publishes the updated text', E, M['fees'])
row('Fees Regs reg 3, draft', 'only the heading "עדכוני אגרות" is shown; the body is not', R, M['fees'] + ' (named refusals)')
row('Fees Regs reg 4, as made and as amended', 'full payment as a condition of a licence, exam or objection', E, M['fees'])
row('Fees Regs reg 4, draft', 'text not shown; encoded from the SimpLEX panel gloss, for exams only', E, M['fees'] + ' (fork F-D1)')
row('Fees Regs reg 5, as made', 'commencement seven days from publication', E, M['fees'])
row('Fees Regs reg 5, as amended', '12383 has no commencement provision', R, M['fees'] + ' (named refusal)')
row('Fees Regs reg 5, draft', 'not shown', R, M['fees'] + ' (named refusal)')
row('Fees Regs signature blocks and footnotes (all vintages)', 'dates of signature, footnote citations', I, '(none)')
# ---- the SimpLEX panel
row('SimpLEX table row 5', 'registration for a theory exam: registration approved (reg 2(א))', E, 'hvac-tests-simplex.l4')
row('SimpLEX table row 6', 'registration for a practical exam: registration approved (reg 2(ב))', E, 'hvac-tests-simplex.l4')
row('SimpLEX table row 7', 'an appeal with payment (40): the appeal is examined (reg 2(ג))', E, 'hvac-tests-simplex.l4')
row('SimpLEX table row 8', 'registration without payment: service suspension (reg 4)', E, 'hvac-tests-simplex.l4')
row('SimpLEX worked example', 'candidate registers for a theory exam and does not pay', E, 'hvac-tests-simplex.l4, hvac-tests-red.l4')
row('SimpLEX second panel, "תרחישי בדיקה לעדכוני אגרות ומדד"', 'cut off after its header row: no scenario is visible', X, '(not transcribed)')

count = collections.Counter(r[2] for r in rows)
TABLE = '| # | provision | what it is | disposition | where |\n| --- | --- | --- | --- | --- |\n' + '\n'.join(
    '| %d | %s | %s | %s | %s |' % (i + 1, p, w, d, wh) for i, (p, w, d, wh) in enumerate(rows))
COUNTS = ', '.join('%s: %d' % (k, count[k]) for k in (E, I, R, X)) + ', deferred: 0 (total %d rows)' % len(rows)

# ---- file list
files = sorted(p.name for p in DEP.glob('*.l4'))
FLIST = '\n'.join('- `%s` (%d lines)' % (f, len((DEP / f).read_text(encoding='utf-8').split('\n'))) for f in files)

# ---- check.sh output, computed
chk = subprocess.run([str(DEP / 'check.sh'), str(DEP)], capture_output=True, text=True).stdout.rstrip()

tot = [l for l in chk.split('\n') if l.startswith('TOTAL')][0].split()
NASSERT = str(int(tot[-3]) + int(tot[-2]) + int(tot[-1]))
tpl = (W / 'build' / 'notes_template.md').read_text(encoding='utf-8')
out = (tpl.replace('@@TABLE@@', TABLE).replace('@@COUNTS@@', COUNTS).replace('@@FILES@@', FLIST)
          .replace('@@CHECK@@', chk).replace('@@NASSERT@@', NASSERT).replace('@@DATE@@', datetime.date.today().isoformat()))
(DEP / 'NOTES.md').write_text(out, encoding='utf-8')
print('wrote NOTES.md;', COUNTS)
