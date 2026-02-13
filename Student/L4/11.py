from datetime import datetime, timedelta

# print(datetime.now().year)

print(datetime.now().hour)




hour = datetime.now().hour

if hour >= 22 or hour < 6:
    print("ніч")
else:
    print("день")

now = datetime.now()
delta = timedelta(7)
future = now + delta
print(future)



a = datetime(2025, 1, 1)
b = datetime.now()

print((b-a).days)

