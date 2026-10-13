import datetime as dt, calendar
D=dt.date
SAT=lambda d: d.weekday()==5
FRISAT=lambda d: d.weekday() in (4,5)
NONE=lambda d: False
def s10a(n,d): return d+dt.timedelta(days=n)                      # (a): the day itself is not counted; the period ends on D+N
def s10b(n_months,d):                                              # (b): same day number, or the month's last day
    y=d.year+(d.month-1+n_months)//12; m=(d.month-1+n_months)%12+1
    return D(y,m,min(d.day,calendar.monthrange(y,m)[1]))
def c(last,rest):                                                   # (c), reading A: first day from the nominal last day that is not a rest day
    while rest(last): last+=dt.timedelta(days=1)
    return last
def wd(d): return d.strftime('%a')
if __name__=='__main__':
    for lab,d in [('pub',D(2025,1,14)),('regs commence',D(2025,7,16)),('CD+18m',s10b(18,D(2025,7,16))),('CD+3y',s10b(36,D(2025,7,16))),
                  ('pub+3m',s10b(3,D(2025,1,14))),('CD readingA',s10b(3,D(2025,7,16))),('CD A +18m',s10b(18,D(2025,10,16))),('CD A +3y',s10b(36,D(2025,10,16))),
                  ('reg5 9Jul+7',s10a(7,D(2025,7,9))),('s16 1Mar26+30',s10a(30,D(2026,3,1))),('s17c 31Mar30+3m',s10b(3,D(2030,3,31))),
                  ('s8 5y 2025-01-15',s10b(60,D(2025,1,15))),('s8 5y 2025-09-01',s10b(60,D(2025,9,1))),('s9 1y 2026-01-10',s10b(12,D(2026,1,10)))]:
        print('%-18s %s %s'%(lab,d,wd(d)))
