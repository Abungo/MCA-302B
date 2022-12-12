import datetime

date1 = datetime.date(2022,11,23)
date2 = datetime.date(2023,1,15)
days = date2-date1
print("Number of Days between",date2.strftime("%d %b %Y"), "and" ,date1.strftime("%d %b %Y"),"are ",days.days)