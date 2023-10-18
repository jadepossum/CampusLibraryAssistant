from datetime import date, timedelta

date1 = date.fromisoformat("2023-10-15")
tdelta = timedelta(days=15)
returndate = date1 + tdelta
curdate = date.today()
if(curdate > returndate):
    print("fined ",(curdate - returndate).days," rupees as of today")
else:
    print("not fined until",returndate)