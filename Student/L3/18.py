# import requests

# city = "London"  
# api_url = f'https://api.api-ninjas.com/v1/weather?city={city}'
# headers = {'X-Api-Key': 'BF0NoHRou+c6gR4NAbDT8g==L5W5JTQqii6A4oFT'}

# response = requests.get(api_url, headers=headers)

# if response.status_code == 200:
#     data = response.json()
#     print(f"Weather in {city}:")
#     print("Temperature:", data.get("temp"), "°C")
#     print("Wind Speed:", data.get("wind_speed"), "m/s")
#     print("Humidity:", data.get("humidity"), "%")
# else:
#     print(f"Could not fetch weather for {city}. Status code:", response.status_code,response.text)


import requests

city_name = "London"
API_key = "1954bdc71a2b87b31d8815f9073ae54c"


url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

response = requests.get(url)
data = response.json()


print(data["weather"][0]['description'])
