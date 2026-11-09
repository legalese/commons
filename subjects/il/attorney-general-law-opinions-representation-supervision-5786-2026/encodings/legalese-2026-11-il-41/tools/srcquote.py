#!/usr/bin/env python3
# srcquote.py FILE.l4 ... : replace each marker line `-- SRC <tag> <N>` with `-- <tag>:<N> | <line N of that deposited source, wiki templates stripped>`.
# Idempotent: a replaced line no longer matches.  Run with python3 -I.  Hebrew in the modules is only ever put there by this tool or checked by hebcheck.py.
import re,sys,os
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','registers','source-bundle','aids')
T={'lsh':'knesset-unofficial-text-25_lsh_14184774.he.txt',          # the Law itself (aid; compared with the official pages: NOTES.md section 3)
   'nl':'attorney-general-law-opinions-representation-supervision-5786-2026.he.wiki.txt',
   'cp':'civproc-state-as-litigant-5718-1958.he.wiki.txt',
   'ord':'ordinance-appearance-of-the-attorney-general-new-version.he.wiki.txt',
   'app':'civil-service-appointments-law-5719-1959.he.wiki.txt',
   'com':'state-representatives-complaints-commissioner-law-5776-2016.he.wiki.txt'}
def clean(s):
    s=re.sub(r'\{\{ח:הערה\|.*\}\}','',s)
    s=re.sub(r'^\{\{ח:תת*\|?[^}]*\}\}\s*','',s)
    s=re.sub(r'\{\{ח:(?:פנימי|חיצוני)\|[^|}]*\|([^}]*)\}\}',r'\1',s)
    return s.strip()
for f in sys.argv[1:]:
    out=[]
    for ln in open(f,encoding='utf-8').read().split('\n'):
        m=re.fullmatch(r'-- SRC (\w+) (\d+)',ln)
        if m:
            L=open(os.path.join(B,T[m.group(1)]),encoding='utf-8').read().split('\n')[int(m.group(2))-1]
            out.append('-- %s:%s | %s'%(m.group(1),m.group(2),clean(L)))
        else: out.append(ln)
    open(f,'w',encoding='utf-8').write('\n'.join(out))
