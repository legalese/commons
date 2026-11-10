# Copied on 2026-11-10 (row il-62) from row il-60, which copied it from the session's working copy of the Hebrew-calendar routine; not changed.
# Run it through tools/datepairs.py, which converts the date pairs this row uses and the routine's own control first.
# Hebrew calendar (Calendrical Calculations), month numbering: Nisan=1 ... Adar=12 (Adar II =13 in leap), Tishri=7
import datetime,sys
def leap(y): return (7*y+1)%19<7
def elapsed_days(y):
    m=(235*y-234)//19
    p=12084+13753*m
    d=29*m+p//25920
    if (3*(d+1))%7<3: d+=1
    return d
def new_year_delay(y):
    ny0=elapsed_days(y-1); ny1=elapsed_days(y); ny2=elapsed_days(y+1)
    if ny2-ny1==356: return 2
    if ny1-ny0==382: return 1
    return 0
def new_year(y): return elapsed_days(y)+new_year_delay(y)
def days_in_year(y): return new_year(y+1)-new_year(y)
def last_day(y,m):
    if m in (2,4,6,10,13): return 29
    if m==12 and not leap(y): return 29
    if m==8 and days_in_year(y)%10!=5: return 29
    if m==9 and days_in_year(y)%10==3: return 29
    return 30
EPOCH=datetime.date(1,1,1).toordinal()  # R.D. day 1 = Gregorian 0001-01-01; Hebrew epoch R.D. -1373427
HEB_EPOCH=-1373427
def to_rd(y,m,d):
    t=new_year(y)+HEB_EPOCH  # RD of 1 Tishri... (elapsed days measured from epoch)
    # RD of Tishri 1
    rd=HEB_EPOCH+new_year(y)
    # months in order from Tishri(7)
    last=13 if leap(y) else 12
    order=list(range(7,last+1))+list(range(1,7))
    # fix: for non-leap, months go 7..12 then 1..6
    for mm in order:
        if mm==m: break
        rd+=last_day(y,mm)
    return rd+d-1
def greg(rd): return datetime.date.fromordinal(rd)
def conv(y,m,d): return greg(to_rd(y,m,d))
if __name__=='__main__':
    # sanity: 1 Tishri 5787
    print('1 Tishri 5787', conv(5787,7,1))
    print('7 Shvat 5787', conv(5787,11,7), '(Shvat=11)')
    print('2 Shvat 5781', conv(5781,11,2))
    print('4 Shvat 5773', conv(5773,11,4))
    print('22 Tevet 5787', conv(5787,10,22))
    print('20 Tevet 5784', conv(5784,10,20))
    print('30 Kislev 5785', conv(5785,9,30))
