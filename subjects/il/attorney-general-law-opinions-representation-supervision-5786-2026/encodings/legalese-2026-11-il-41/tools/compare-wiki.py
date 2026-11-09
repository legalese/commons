#!/usr/bin/env python3
# compare-wiki.py WIKI.txt DOCX.txt : the words (as multisets) of the Wikisource page of the new Law, against the Knesset's unofficial text.  Digits and sub-section letters are dropped on both sides.
import re,sys,collections
wiki,docx=sys.argv[1:3]
def norm(s):
    s=re.sub('[‎‏‪-‮⁦-⁩﻿]','',s)
    s=re.sub(r'[”“"״׳\'.,;:()\[\]–\-־—*]',' ',s)
    return s.split()
def clean(ws): return collections.Counter(w for w in ws if not re.fullmatch(r'\d+|[א-ה]',w))
t=open(wiki,encoding='utf-8').read()
body=t.split('{{ח:מפריד}}',1)[1].split('{{ח:חתימות',1)[0]
# keep the section headings, drop footnote templates and every other template
heads=re.findall(r'\{\{ח:סעיף\|[^|}]*\|([^|}]*)',body)
body=re.sub(r'\{\{ח:הערה\|(?:[^{}]|\{\{[^{}]*\}\})*\}\}','',body)
body=re.sub(r'\{\{ח:(?:פנימי|חיצוני)\|[^|}]*\|([^}]*)\}\}',r'\1',body)
body=re.sub(r'\{\{ח:סעיף\|[^}]*\}\}','',body)
body=re.sub(r'\{\{[^{}]*\}\}','',body)
body=re.sub(r"'''?",'',body)
W=clean(norm(body)); W.update(clean(norm(' '.join(heads))))
d=open(docx,encoding='utf-8').read().split('בנימין נתניהו')[0]
D=clean(norm(d))
print('words: Wikisource body+headings',sum(W.values()),' Knesset unofficial text',sum(D.values()))
print('in Wikisource, not in the Knesset text:',dict(W-D))
print('in the Knesset text, not in Wikisource:',dict(D-W))
