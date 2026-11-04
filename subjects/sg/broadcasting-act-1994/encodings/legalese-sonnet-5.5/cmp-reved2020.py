"""cmp-reved2020.py: compare the 2020 Revised Edition (BA1994.20211231.txt) with the 2024 consolidation (BA1994.txt) on
s 2(1) "broadcasting apparatus", s 20(1) to (4), s 47 and the First Schedule, after dropping page furniture and amendment notes.
Run as: python3 -I cmp-reved2020.py   (it finds the source bundle from its own location; it reads two files and writes nothing)."""
import re,difflib
import os
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','registers','source-bundle')+os.sep
def norm(t):
    return re.sub(r'[‘’“”]','"',t).replace('‑','-').replace('—','-').replace('–','-')
def L(f): return norm(open(B+f,encoding='utf-8').read().replace('\f','\n')).split('\n')
E=L('BA1994.20211231.txt'); C=L('BA1994.txt')
def clean(ls):
    out=[]
    for x in ls:
        n=re.sub(r'\s+',' ',x).strip()
        if not n: continue
        if re.match(r'^(Informal Consolidation.*|\d+ +Broadcasting Act 1994 +2020 Ed\.?|2020 Ed\.? +Broadcasting Act 1994 +\d+|2020 Ed\.? +Broadcasting Act 1994|Broadcasting Act 1994 +\d+|\d+ +2020 Ed\.?.*|2020 Ed\.? *\d*|[0-9.]{6,}|\d+)$',n): continue
        if re.match(r'^\[[^\]]*\]?$',n) and ('wef' in n or re.match(r'^\[\d+',n)): continue
        out.append(n)
    return ' '.join(out)
def first(Ls,pat,after=0):
    for i in range(after,len(Ls)):
        if re.search(pat,Ls[i]): return i
    raise SystemExit('no '+pat)
w=lambda s:re.findall(r'\S+',s)
blocks={}
for nm,Ls in (('2020',E),('2024',C)):
    i=first(Ls,r'^\s*"broadcasting apparatus" means any apparatus capable of'); b2=clean(Ls[i:i+3])
    i=first(Ls,r'^\s*20\.-\(1\) Subject to this section'); j=first(Ls,r'^Application of certain provisions of Act to broadcasting',i); b20=clean(Ls[i:j])
    i=first(Ls,r'^\s*47\. Any person who contravenes section 20'); j=first(Ls,r'^Offences relating to unauthorised decoders',i); b47=clean(Ls[i:j])
    i=first(Ls,r'^\s*FIRST SCHEDULE\s*$',3000 if nm=='2024' else 1500); j=first(Ls,r'SECOND SCHEDULE',i); bs=clean(Ls[i:j])
    blocks[nm]=(b2,b20,b47,bs)
for k,nm in enumerate(['s 2(1) "broadcasting apparatus"','s 20(1) to (4)','s 47','First Schedule']):
    a,b=blocks['2020'][k],blocks['2024'][k]
    sm=difflib.SequenceMatcher(None,w(a),w(b),autojunk=False)
    print('==',nm,'words 2020/2024:',len(w(a)),len(w(b)),'IDENTICAL' if a==b else 'DIFFERENT')
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op!='equal': print('    ',op,'2020:',' '.join(w(a)[i1:i2])[:110],'| 2024:',' '.join(w(b)[j1:j2])[:110])
