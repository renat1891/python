import requests

api_url = 'https://api.api-ninjas.com/v1/facts'
headers = {'X-Api-Key': 'BF0NoHRou+c6gR4NAbDT8g==L5W5JTQqii6A4oFT'}

response = requests.get(api_url, headers=headers)
fact = response.json()[0]
print(fact)

