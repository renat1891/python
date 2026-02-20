from datetime import datetime, timedelta

now = datetime.now()
result = now.strftime("%A %B %y")

print(result)


# days = [
#     "Понеділок",
#     "Вівторок",
#     "Середа",
#     "Четвер",
#     "П'ятниця",
#     "Субота",
#     "Неділя"
# ]

# print(days[now.weekday()])