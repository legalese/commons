#!/usr/bin/env python3
"""Token and list-price accounting for the sub-agents of the Jersey fleet.
usage: cost.py [RATES.json]     (without RATES.json: counts only)
Agents are the transcripts under the session's subagents/ directory whose first user message names 'je-full' (the HVAC fleet's say 'full-run').
Messages are de-duplicated by message id (streaming writes the same id several times; the last record has the final output_tokens).
RATES.json: {"claude-sonnet-5-5": {"input":..,"cache_write_1h":..,"cache_write_5m":..,"cache_read":..,"output":..}, ...}  in dollars per million tokens."""
import json,glob,os,re,sys,collections
T="/Users/mengwong/.claude/projects/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/subagents"
rates=json.load(open(sys.argv[1])) if len(sys.argv)>1 else None
ROLES=[("SKILL-REWRITER","skill-rewriter"),("SURVEYOR","surveyor"),("HUNTER","hunt"),("INTEGRATOR","integrator"),("COMPARATOR","comparator"),("COMPARER","comparator"),("OVERLAP","overlap")]
def role(first):
    m=re.search(r"ENCODER (G\d)",first)
    if m: return "enc-"+m.group(1).lower()
    m=re.search(r"INDEPENDENT TEST AUTHOR `?ind-([abc])",first)
    if m: return "ind-"+m.group(1)
    for k,n in ROLES:
        if k in first: return n
    return None
def first_user(ev):
    for d in ev:
        if d.get("type")=="user":
            c=d["message"]["content"]
            return c if isinstance(c,str) else " ".join(x.get("text","") for x in c if isinstance(x,dict))
    return ""
rows=collections.OrderedDict()
for f in sorted(glob.glob(T+"/agent-*.jsonl")):
    ev=[]
    for line in open(f):
        try: ev.append(json.loads(line))
        except: pass
    fu=first_user(ev)
    if "je-full" not in fu: continue
    r=role(fu) or os.path.basename(f)
    best={}
    for d in ev:
        if d.get("type")!="assistant": continue
        m=d["message"]; u=m.get("usage") or {}; mid=m.get("id") or d.get("uuid")
        cur=best.get(mid)
        if cur is None or (u.get("output_tokens") or 0)>=(cur[0].get("output_tokens") or 0): best[mid]=(u,m.get("model"))
    agg=collections.defaultdict(lambda:[0,0,0,0,0,0])  # req,in,cw1h,cw5m,cr,out
    for u,model in best.values():
        if not model or model=="<synthetic>": continue
        cc=u.get("cache_creation") or {}
        w1=cc.get("ephemeral_1h_input_tokens"); w5=cc.get("ephemeral_5m_input_tokens")
        tot=u.get("cache_creation_input_tokens") or 0
        if w1 is None and w5 is None: w1,w5=tot,0
        a=agg[model]; a[0]+=1; a[1]+=u.get("input_tokens") or 0; a[2]+=w1 or 0; a[3]+=w5 or 0; a[4]+=u.get("cache_read_input_tokens") or 0; a[5]+=u.get("output_tokens") or 0
    if r in rows:
        for model,a in agg.items():
            b=rows[r][model]
            for i in range(6): b[i]+=a[i]
    else: rows[r]=agg
tot=collections.defaultdict(lambda:[0,0,0,0,0,0]); cost=collections.defaultdict(float); grand=0.0
print("%-16s %-20s %6s %10s %10s %10s %12s %9s %s"%("agent","model","reqs","input","cache_w1h","cache_w5m","cache_read","output","list $"))
for r,agg in rows.items():
    for model,a in agg.items():
        c=None
        if rates and model in rates:
            R=rates[model]; c=(a[1]*R["input"]+a[2]*R["cache_write_1h"]+a[3]*R["cache_write_5m"]+a[4]*R["cache_read"]+a[5]*R["output"])/1e6
            cost[model]+=c; grand+=c
        for i in range(6): tot[model][i]+=a[i]
        print("%-16s %-20s %6d %10d %10d %10d %12d %9d %s"%(r,model,*a,"" if c is None else "%.2f"%c))
print("-"*110)
for model,a in tot.items():
    print("%-16s %-20s %6d %10d %10d %10d %12d %9d %s"%("TOTAL",model,*a,"" if model not in cost else "%.2f"%cost[model]))
if rates: print("TOTAL list price: $%.2f"%grand)
