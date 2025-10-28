import requests

api_url = 'https://api.api-ninjas.com/v1/facts'

headers={'X-Api-Key': 'cWEJhgDJpd5ffzMoDFYaNA==Ygf3nSgC9lIAd6JD'}

response = requests.get(api_url, headers=headers)

print(response.json()[0]['fact'])