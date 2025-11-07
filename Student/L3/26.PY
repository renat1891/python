import requests
import random
import deepl

api_url = 'https://api.api-ninjas.com/v1/facts'
headers = {'X-Api-Key': 'BF0NoHRou+c6gR4NAbDT8g==L5W5JTQqii6A4oFT'}

response = requests.get(api_url, headers=headers)
fact = response.json()[0]['fact']

languages = {
    'uk': 'Українська',
    'es': 'Іспанська',
    'de': 'Німецька',
    'fr': 'Французька',
    'ja': 'Японська'
}
lang_code, lang_name = random.choice(list(languages.items()))
try:
    auth_key = "41c4cbe6-2089-413d-8c8f-0d16d52ce24e:fx"
    deepl_client = deepl.DeepLClient(auth_key)
    print(deepl_client.get_usage())
except Exception as e:
    print(f"Помилка ініціалізації клієнта DeepL: {e}")

try:
    result = deepl_client.translate_text(fact, target_lang=lang_code.upper())
    translated = result.text
except Exception as e:
    print(f"Помилка перекладу тексту: {e}")
    translated = "Переклад недоступний."

print(f"Мова: {lang_name}")
print(f"Факт: {translated}")
