from datetime import datetime, timedelta

print(datetime.now())
print(datetime.now().day)
print(datetime.now().year)
print(datetime.now().hour)

now = datetime.now()
delta = timedelta(days=300)
print(now - delta)

myday = datetime(1997, 12, 7)
bth = now - myday
print(bth.days/365.2425)