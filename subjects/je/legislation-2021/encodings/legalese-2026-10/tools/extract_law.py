#!/usr/bin/env python3
"""Extract a jerseylaw.je consolidated-law HTML page to one line per paragraph, indented by level.
usage: extract_law.py HTML OUT
Mechanical: reads the page's own paragraph classes (iLAWS...), decodes entities, squeezes whitespace. Nothing is typed from memory."""
import re,sys,html,unicodedata
src,out=sys.argv[1],sys.argv[2]
s=open(src,encoding='utf-8',errors='replace').read()
LEVEL={'iLAWS200PartHeading':0,'iLAWS210PartSubHeading':0,'iLAWS300Article':0,'iLAWS310Paragraph':1,'iLAWS311ParagraphContinued':1,
 'iLAWS320SubParagraph':2,'iLAWS321SubParagraphContinued':2,'iLAWS330Clause':3,'iLAWS301Paragraphunnumbered':1,'iLAWS370NormalText':1,
 'iLAWS400ScheduleHeading':0,'iLAWS403SchedulePartHeading':0,'iLAWS404SchedulePartSubHeading':0,'iLAWS405SchedulePartSubSubHeading':0,'iLAWS401ScheduleSubHeading':0,'iLAWS402ScheduleSubSubHeading':0,'iLAWS410ScheduleParagraph':1,
 'iLAWS129LongTitle':0,'iLAWS129Commencement':0,'iLAWS104CoverShortTitle':0,'iLAWS600EndnotesTitle':0,'iLAWS602EndnotesHeading':0}
SKIP={'iLAWS120ShortTitleContents','iLAWS130Contents','iLAWS140ContentsHeading','iLAWS101CrestLarge','iLAWS115CrestSmall','iLAWS803SectionBreak','iLAWS102VersionCommencement','iLAWS103CoverVersion'}
def clean(t):
    t=re.sub(r'(?is)<sup[^>]*>(.*?)</sup>',lambda m:'['+re.sub(r'<[^>]+>','',m.group(1)).strip().strip('[]')+']' if re.sub(r'<[^>]+>','',m.group(1)).strip().strip('[]').isdigit() else re.sub(r'<[^>]+>','',m.group(1)),t)
    t=re.sub(r'<[^>]+>','',t); t=html.unescape(t).replace(' ',' ')
    t=re.sub(r'\s+',' ',t).strip()
    return unicodedata.normalize('NFC',t)
lines=[]; unknown={}
for m in re.finditer(r'<p class="(iLAWS[^"]*)"[^>]*>(.*?)</p>',s,flags=re.S):
    cls,body=m.group(1),m.group(2)
    if cls in SKIP: continue
    txt=clean(body)
    if not txt: continue
    if cls not in LEVEL: unknown[cls]=unknown.get(cls,0)+1; lvl=1
    else: lvl=LEVEL[cls]
    lines.append('  '*lvl+txt)
# endnotes: table cells, taken from the visible text after the 'Endnotes' heading
vis=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>','',s)
vis=re.sub(r'(?i)<br\s*/?>','\n',vis); vis=re.sub(r'(?i)</(p|div|li|tr|td|th|h[1-6])>','\n',vis)
vis=html.unescape(re.sub(r'<[^>]+>','',vis)).replace(' ',' ')
vl=[re.sub(r'\s+',' ',l).strip() for l in vis.split('\n')]; vl=[l for l in vl if l]
i=max(j for j,l in enumerate(vl) if l=='Endnotes')
k=next(j for j in range(i,len(vl)) if vl[j].startswith('Page Last Updated'))
lines.append('ENDNOTES (taken from the page footer tables)')
lines+=['  '+l for l in vl[i+1:k]]
open(out,'w',encoding='utf-8').write('\n'.join(lines)+'\n')
print(len(lines),'lines; unknown classes:',unknown)
