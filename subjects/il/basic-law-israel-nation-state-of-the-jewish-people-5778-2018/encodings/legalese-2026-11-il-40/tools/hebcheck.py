#!/usr/bin/env python3
# hebcheck.py FILE.l4 ... : every double-quoted string literal that contains a Hebrew letter must occur verbatim in a deposited
# source (raw text of any file under registers/source-bundle/ aids or the Basic Law consolidation).  Exit 1 and list any that do not.
import re,sys,os,glob
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','registers','source-bundle')
corp=''.join(open(p,encoding='utf-8').read() for p in glob.glob(B+'/*.txt')+glob.glob(B+'/aids/*.txt'))
bad=0;n=0
for f in sys.argv[1:]:
    for i,ln in enumerate(open(f,encoding='utf-8').read().split('\n'),1):
        if ln.lstrip().startswith('--'): continue
        for s in re.findall(r'"([^"]*)"',ln):
            if re.search('[֐-׿]',s):
                n+=1
                if s not in corp: bad+=1; print('NOT IN SOURCES: %s:%d: %s'%(f,i,s))
print('hebcheck: %d Hebrew literals checked, %d not found'%(n,bad)); sys.exit(1 if bad else 0)
