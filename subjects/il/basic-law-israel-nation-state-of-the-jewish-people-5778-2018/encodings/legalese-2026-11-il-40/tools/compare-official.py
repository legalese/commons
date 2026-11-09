import re,sys,subprocess,collections
wiki,pdf=sys.argv[1],sys.argv[2]
def strip_templates(s):
    # remove {{ח:הערה|...}} with nesting
    out=[];i=0
    while i<len(s):
        if s.startswith('{{ח:הערה',i):
            d=0;j=i
            while j<len(s):
                if s.startswith('{{',j): d+=1;j+=2
                elif s.startswith('}}',j): d-=1;j+=2;
                else: j+=1
                if d==0: break
            i=j
        else: out.append(s[i]);i+=1
    return ''.join(out)
txt=open(wiki,encoding='utf-8').read()
body=txt.split('{{ח:מפריד}}',1)[1].split('{{ח:חתימות',1)[0]
body=strip_templates(body)
heads=re.findall(r'\{\{ח:סעיף\|([^|}]*)\|([^|}]*)\}\}',body)
body=re.sub(r'\{\{ח:סעיף\|[^}]*\}\}','',body)
body=re.sub(r'\{\{ח:תת?\|?[^}]*\}\}','',body)
def norm(s):
    s=re.sub('[‎‏‪-‮﻿]','',s)
    s=re.sub(r'[”“"״׳\'.,;:()\[\]–\-־—]',' ',s)
    return s.split()
w=collections.Counter(norm(body))
for n,t in heads: w.update(norm(t))
pt=subprocess.run(['pdftotext','-f','2','-l','2','-layout',pdf,'-'],capture_output=True,text=True).stdout
pt=pt.split('התקבל בכנסת ביום')[0]   # drop the footnote
pt=re.split(r'בנימין|ב נימ',pt)[0]    # drop the signature block
p=collections.Counter(w_ for w_ in norm(pt) if not re.fullmatch(r'\d+|א|ב|ג|ד|ה|‫',w_))
# section numbers/letters are dropped from both sides
w2=collections.Counter({k:v for k,v in w.items() if not re.fullmatch(r'\d+|[א-ה]',k)})
print('words in Wikisource body+headings:',sum(w2.values()),' in official page body+headings:',sum(p.values()))
print('in Wikisource, not in official page (multiset):',dict(w2-p))
print('in official page, not in Wikisource (multiset):',dict(p-w2))
