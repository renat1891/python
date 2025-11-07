import requests

api_url = 'https://api.api-ninjas.com/v1/quotes'
headers = {'X-Api-Key': 'BF0NoHRou+c6gR4NAbDT8g==L5W5JTQqii6A4oFT'}

response = requests.get(api_url, headers=headers)
quote_data = response.json()[0]
quote = quote_data["quote"]
author = quote_data.get("author", "Unknown")

print(f'"{quote}" — {author}')


