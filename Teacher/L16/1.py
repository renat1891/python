import requests

city_name = "London"
API_key = "1954bdc71a2b87b31d8815f9073ae54c"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

response = requests.get(url)
data = response.json()

print(data)