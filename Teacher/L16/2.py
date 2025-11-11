import deepl

auth_key = "41c4cbe6-2089-413d-8c8f-0d16d52ce24e:fx"
deepl_client = deepl.DeepLClient(auth_key)
print(deepl_client.get_usage())

result = deepl_client.translate_text("Hello, world!", target_lang="UK")
print(result.text)