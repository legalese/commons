#!/usr/bin/env python3
# srcquote.py FILE.l4 ... : replace each marker line `-- SRC <tag> <N>` with `-- <tag>:<N> | <line N of that deposited source,
# wiki templates stripped>`.  Idempotent: a replaced line no longer matches.  Run with python3 -I.
import re,sys,os
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','registers','source-bundle')
T={'bl':'basic-law-israel-nation-state-of-the-jewish-people-5778-2018.he.wiki.txt',
   'il':'aids/interpretation-law-5741-1981.he.wiki.txt','jer':'aids/basic-law-jerusalem-capital-of-israel.he.wiki.txt',
   'decl':'aids/declaration-on-the-flag-1948.he.wiki.txt','ord':'aids/law-and-administration-ordinance-5708-1948.he.wiki.txt',
   'order':'aids/palestine-order-in-council-1922-to-1947.he.wiki.txt','flag':'aids/flag-emblem-and-anthem-law-5709-1949.he.wiki.txt',
   'mdl':'aids/memorial-day-law-5723-1963.he.wiki.txt','hdl':'aids/holocaust-and-heroism-remembrance-day-law-5719-1959.he.wiki.txt',
   'idl':'aids/independence-day-law-5709-1949.he.wiki.txt'}
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
