from datetime import datetime, timedelta

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"Поточний час: {current_time}")




minutes_since_midnight = now.hour * 60 + now.minute
print(f"Хвилин від початку дня: {minutes_since_midnight} хвилини")




time_until_midnight = timedelta(days=1) - timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
hours, remainder = divmod(time_until_midnight.seconds, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"Час до опівночі: {hours}:{minutes:02}:{seconds:02}")