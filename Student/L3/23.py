import requests
import random
import deepl

def get_fact():
    api_url = 'https://api.api-ninjas.com/v1/facts'
    headers = {'X-Api-Key': 'BF0NoHRou+c6gR4NAbDT8g==L5W5JTQqii6A4oFT'}

    response = requests.get(api_url, headers=headers)
    fact = response.json()[0]['fact']

    return fact

def translate_fact(fact, target_lang):
    auth_key = "41c4cbe6-2089-413d-8c8f-0d16d52ce24e:fx"
    deepl_client = deepl.DeepLClient(auth_key)

    result = deepl_client.translate_text(fact, target_lang=target_lang)
    return result.text

languages = ["uk", "es", "de", "fr", "ja", "it", "nl", "pl", "pt", "ru", "zh"]
lang_code = random.choice(languages)

fact = get_fact()
print("Original Fact:", fact)
print("Translated Fact:", translate_fact(fact, lang_code))
print("language code:", lang_code)
