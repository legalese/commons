#!/usr/bin/env python3
# compare-texts.py DOCX.txt SH.pdf LS2.pdf : compare the WORDS (as multisets) of the Knesset's unofficial text (docx, via textutil), the
# Sefer HaChukim PDF's text layer (pdftotext -raw: words intact, line order reversed) and the second/third-reading PDF's law text.
# Word ORDER is not compared by this script (the official page images were read by eye, NOTES.md section 3).
# Page 3 of the official PDF carries every word TWICE in its text layer (a doubled overprint; the page image shows it once),
# so its counts are halved, and the script lists any word whose page-3 count is odd.
import re,sys,subprocess,collections
docx,sh,ls2=sys.argv[1:4]
def norm(s):
    s=re.sub('[‎‏‪-‮⁦-⁩﻿]','',s)
    s=re.sub('[֑-ׇ]','',s)
    s=re.sub(r'[”“"״׳\'.,;:()\[\]–\-־—*]',' ',s)
    return s.split()
def clean(ws): return collections.Counter(w for w in ws if not re.fullmatch(r'\d+|[א-ה]',w))
d=open(docx,encoding='utf-8').read().split('בנימין נתניהו')[0]
D=clean(norm(d))
def page(n): return subprocess.run(['pdftotext','-f',str(n),'-l',str(n),'-raw',sh,'-'],capture_output=True,text=True).stdout
def drop_lines(t,pat): return '\n'.join(l for l in t.split('\n') if not re.search(pat,l))
# running heads and footnotes, dropped by line (their words are not in the docx)
p2=drop_lines(page(2),r'ספר|רשומות|החוקים|התקבל|בכנסת|1192|עמ')
p3=drop_lines(page(3),r'ספר|החוקים|3550|דיני מדינת ישראל|רפס')
p4=drop_lines(page(4),r'ספר|החוקים|3550|ס"ח|רפס')
p4=p4.split('ן‫י‬‫נימ‬')[0] if 'ן‫י‬‫נימ‬' in p4 else p4
p4=re.split(r'(?m)^.*נתניהו.*$|^.*‫ו‬‫ה‬‫ני‬.*$',p4)[0]
P2=clean(norm(p2)); P3=clean(norm(p3)); P4=clean(norm(p4))
print('page 3 words with an odd count:',{k:v for k,v in P3.items() if v%2})
P3h=collections.Counter({k:v//2 for k,v in P3.items()})
P=P2+P3h+P4
print('docx words:',sum(D.values()),' official PDF words (p2 + p3/2 + p4):',sum(P.values()))
print('in docx, not in PDF:',dict(D-P))
print('in PDF, not in docx:',dict(P-D))
t=subprocess.run(['pdftotext','-layout',ls2,'-'],capture_output=True,text=True).stdout
t=re.sub('[‪-‮‎‏⁦-⁩]','',t)
i=t.index("פרק א' :חוות דעת"); j=t.index('***************')
L=clean(norm(t[i:j]))
L=L-collections.Counter({'13':0})
print('LS2 law words:',sum(L.values()))
print('in docx, not in LS2:',dict(D-L))
print('in LS2, not in docx:',dict(L-D))
