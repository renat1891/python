import requests

TOKEN = "7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U"
chanel_id = "-1003275784278"

text = "<i>Hello</i>, <b>World!</b>"
url_photo = "https://ireland.apollo.olxcdn.com:443/v1/files/t9bznmvtu1oc1-UA/image;"
url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chanel_id}&text={text}'

url_photo = f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={chanel_id}&photo={url_photo}&caption={text}&parse_mode=HTML'

response = requests.get(url_photo)
print(response.json())