

import requests


def get_data_info():
    url = "https://api.monobank.ua/bank/currency"
    r = requests.get(url)
    data = r.json()

    if not isinstance(data, list):
        raise ValueError(f"Unexpected response from API: {data}")

    return data


def sort_data():
    data = get_data_info()
    currencies = {}

    for item in data:
        code_a = item.get("currencyCodeA")
        code_b = item.get("currencyCodeB")

        if code_b != 980:
            continue

        if code_a == 840:
            buy = item.get("rateBuy") or item.get("rateCross")
            sell = item.get("rateSell") or item.get("rateCross")
            currencies["USD"] = (buy, sell)
        elif code_a == 978:
            buy = item.get("rateBuy") or item.get("rateCross")
            sell = item.get("rateSell") or item.get("rateCross")
            currencies["EUR"] = (buy, sell)
        elif code_a == 826:
            currencies["GBP"] = item.get("rateCross")
        elif code_a == 756:
            currencies["CHF"] = item.get("rateCross")
        elif code_a == 985:
            currencies["PLN"] = item.get("rateCross")

    return currencies


if __name__ == "__main__":
    currencies = sort_data()
    print(currencies)