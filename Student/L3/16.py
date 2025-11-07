import requests

api_url = 'https://api.api-ninjas.com/v1/bitcoin'

headers={'X-Api-Key': 'cWEJhgDJpd5ffzMoDFYaNA==Ygf3nSgC9lIAd6JD'}

response = requests.get(api_url, headers=headers)
BTC = float(response.json()["price"])
print(BTC)