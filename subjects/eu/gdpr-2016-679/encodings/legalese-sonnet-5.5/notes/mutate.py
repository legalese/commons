#!/usr/bin/env python3
# notes/mutate.py -- P2's mutation spot-check.  For each mutation (module, old text, new text) it copies the keel and the module with
# its tests to notes/mut/, applies the mutation to the one copy, runs the tests with the main build and reports whether any
# assertion failed or any error appeared (the mutation was caught) or not (the tests did not notice).  notes/mut/ is removed at the end.
import os, re, shutil, subprocess, sys
L4 = os.environ.get("L4", "l4")
env = {k: v for k, v in os.environ.items() if k != "JL4_LIBRARY_PATH"}
KEEL = ["gdpr-core.l4", "gdpr-core-2.l4", "gdpr-definitions.l4", "gdpr-definitions-2.l4"]
MUT = [
 (12, "IF `the date the controller provided the information on action taken` AT MOST (`add months`", "IF `the date the controller provided the information on action taken` LESS THAN (`add months`", "12(3) one month inclusive"),
 (12, "    THEN 3\n    ELSE 1", "    THEN 2\n    ELSE 1", "12(3) three months"),
 (12, "WITHIN 1\n         HENCE FULFILLED\n         LEST BREACH BY controller BECAUSE \"the data subject was not informed of the extension", "WITHIN 2\n         HENCE FULFILLED\n         LEST BREACH BY controller BECAUSE \"the data subject was not informed of the extension", "12(3) notice deadline"),
 (12, "IF `Art 11(2) Articles 15 to 20 are disapplied` EQUALS NOTHING\n        THEN NOTHING", "IF `Art 11(2) Articles 15 to 20 are disapplied` EQUALS JUST TRUE\n        THEN NOTHING", "12(2) outside Art 11(2)"),
 (13, "AND (IF `the controller has designated a data protection officer` THEN held `Art 13(1)(b) the contact details of the data protection officer` ELSE TRUE)", "", "13(1)(b) officer"),
 (13, "WITHIN 0\n         HENCE FULFILLED\n         LEST BREACH BY controller BECAUSE \"the information was not provided at the time", "WITHIN 1\n         HENCE FULFILLED\n         LEST BREACH BY controller BECAUSE \"the information was not provided at the time", "13(1) at the time"),
 (14, "THEN IF `the controller has taken appropriate measures", "THEN IF NOT (`the controller has taken appropriate measures", "14(5)(b) measures (mutated syntax; expect a type error)"),
 (14, "LESS THAN afterCommunication\n       THEN `the months", "LESS THAN 5\n       THEN `the months", "14(3) earliest limit"),
 (15, "IF item EQUALS `Art 15(1)(g) any available information as to the source of the personal data` AND NOT (`the personal data are not collected from the data subject`)", "IF item EQUALS `Art 15(1)(g) any available information as to the source of the personal data` AND `the personal data are not collected from the data subject`", "15(1)(g) source"),
 (16, "IF `the personal data concerning the data subject are incomplete` AND `completion is called for, taking into account the purposes of the processing`", "IF `the personal data concerning the data subject are incomplete`", "16 completion"),
 (17, "THEN JUST FALSE\n        -- FALSE-kind (the text says no in its own words, \"shall not apply\"): \"Paragraphs 1 and 2 shall not apply to the extent that processing is necessary\"", "THEN NOTHING\n        -- FALSE-kind (the text says no in its own words, \"shall not apply\"): \"Paragraphs 1 and 2 shall not apply to the extent that processing is necessary\"", "17(1) paragraph 3 bar"),
 (17, "IF `the data subject withdraws consent on which the processing is based according to point (a) of Article 6(1) or point (a) of Article 9(2)` AND NOT (`there is another legal ground for the processing`)", "IF `the data subject withdraws consent on which the processing is based according to point (a) of Article 6(1) or point (a) of Article 9(2)`", "17(1)(b) no other ground"),
 (18, "OR `the data subject consents to the processing`\n", "\n", "18(2) consent"),
 (19, "IF `communicating it proves impossible or involves disproportionate effort`\n        THEN JUST `the duty does not arise`", "IF NOT (`communicating it proves impossible or involves disproportionate effort`)\n        THEN JUST `the duty does not arise`", "19 unless impossible"),
 (20, "IF NOT (`the processing is carried out by automated means`)\n        THEN JUST FALSE", "IF NOT (`the processing is carried out by automated means`)\n        THEN NOTHING", "20(1)(b) automated"),
 (21, "OR `the controller demonstrates compelling legitimate grounds for the establishment, exercise or defence of legal claims`\n        THEN JUST FALSE", "\n        THEN JUST FALSE", "21(1) legal claims"),
 (22, "IF `Art 9(2)(a) point (a) applies` EQUALS JUST FALSE AND `Art 9(2)(g) point (g) applies` EQUALS JUST FALSE\n        THEN JUST TRUE", "IF `Art 9(2)(a) point (a) applies` EQUALS JUST FALSE AND `Art 9(2)(g) point (g) applies` EQUALS JUST FALSE\n        THEN JUST FALSE", "22(4) bar stands"),
 (22, "IF NOT (`suitable measures to safeguard the data subject's rights and freedoms and legitimate interests are in place`)\n        THEN JUST TRUE", "IF NOT (`suitable measures to safeguard the data subject's rights and freedoms and legitimate interests are in place`)\n        THEN NOTHING", "22(4) no measures, the bar stands (R2)"),
 (13, "IF NOT (`the information was provided at the time when the personal data were obtained` OR null `the items of information that the controller provides`)", "IF FALSE", "13(1) provided at the time (R4)"),
 (13, "WHEN `Art 13(1)(b) the contact details of the data protection officer` THEN `the controller has designated a data protection officer`", "WHEN `Art 13(1)(b) the contact details of the data protection officer` THEN TRUE", "13(1) per item: the officer (R10)"),
 (14, "WHEN `Art 14(1)(f) the intended transfer to a recipient in a third country or international organisation and the adequacy decision or the safeguards` THEN `the controller intends to transfer personal data to a recipient in a third country or international organisation`", "WHEN `Art 14(1)(f) the intended transfer to a recipient in a third country or international organisation and the adequacy decision or the safeguards` THEN TRUE", "14(1) per item: the transfer (R10)"),
 (19, "IF `Art 11(2) Articles 15 to 20 are disapplied` EQUALS JUST TRUE\n        THEN JUST `the duty does not arise`\n        -- FALSE-kind (the text says no in its own words, Article 11(2)): \"Articles 15 to 20 shall not apply except where the data subject\" (Article 19 is among", "IF `Art 11(2) Articles 15 to 20 are disapplied` EQUALS NOTHING\n        THEN JUST `the duty does not arise`\n        -- FALSE-kind (the text says no in its own words, Article 11(2)): \"Articles 15 to 20 shall not apply except where the data subject\" (Article 19 is among", "19 second sentence: Art 11(2) (R9)"),
 (18, "IF `Art 18(1) the data subject has the right to obtain from the controller restriction of processing` EQUALS JUST TRUE\n    THEN PARTY controller\n         MUST", "IF `Art 18(1) the data subject has the right to obtain from the controller restriction of processing` EQUALS JUST FALSE\n    THEN PARTY controller\n         MUST", "18(1) the controller must restrict (R8)"),
 (20, "IF `Art 20(2) the data subject has the right to have the personal data transmitted directly from one controller to another, where technically feasible` EQUALS JUST TRUE\n    THEN PARTY controller\n         MUST", "IF `Art 20(2) the data subject has the right to have the personal data transmitted directly from one controller to another, where technically feasible` EQUALS JUST FALSE\n    THEN PARTY controller\n         MUST", "20(2) the controller must transmit (R8)"),
 (12, "`Art 12(3) the months within which the data subject is to be informed of the extension` MEANS\n    1\n", "`Art 12(3) the months within which the data subject is to be informed of the extension` MEANS\n    2\n", "12(3) notice months (R10)"),
 (23, "IF `the restriction respects the essence of the fundamental rights and freedoms` AND `the restriction is a necessary and proportionate measure in a democratic society`", "IF `the restriction respects the essence of the fundamental rights and freedoms` OR `the restriction is a necessary and proportionate measure in a democratic society`", "23(1) essence and proportionate"),
]
os.makedirs("notes/mut", exist_ok=True)
caught = 0
BASE = {}
for (art, old, new, label) in MUT:
    for f in os.listdir("notes/mut"):
        os.remove(os.path.join("notes/mut", f))
    for f in KEEL + ["P2-art-%d.l4" % art, "P2-tests-art-%d.l4" % art]:
        shutil.copy(f, "notes/mut/" + f)
    p = "notes/mut/P2-art-%d.l4" % art
    s = open(p, encoding="utf-8").read()
    if s.count(old) != 1:
        print("MUTATION NOT APPLIED (%d matches): %s" % (s.count(old), label)); continue
    open(p, "w", encoding="utf-8").write(s.replace(old, new))
    out = subprocess.run([L4, "run", "P2-tests-art-%d.l4" % art], cwd="notes/mut", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env).stdout
    bad = out.count("assertion failed") + out.count("DiagnosticSeverity_Error")
    sig = [" ".join(b.split("Message:", 1)[1].split()) for b in re.split(r"(?m)^File:\s+", out)[1:] if "eval/result" in b]
    base = BASE.get(art)
    if base is None:
        shutil.copy("P2-art-%d.l4" % art, "notes/mut/P2-art-%d.l4" % art)
        o2 = subprocess.run([L4, "run", "P2-tests-art-%d.l4" % art], cwd="notes/mut", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env).stdout
        base = BASE[art] = [" ".join(b.split("Message:", 1)[1].split()) for b in re.split(r"(?m)^File:\s+", o2)[1:] if "eval/result" in b]
        open(p, "w", encoding="utf-8").write(s.replace(old, new))
    how = "assertion or error" if bad else ("trace result" if sig != base else None)
    print("%s: %s%s" % ("CAUGHT" if how else "NOT CAUGHT", label, " (by %s)" % how if how else ""))
    caught += 1 if how else 0
shutil.rmtree("notes/mut")
print("%d of %d mutations caught" % (caught, len(MUT)))
