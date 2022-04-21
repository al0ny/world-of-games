import requests

free_currency_api = "47fc2060-92a0-11ec-a7ae-75dd9f87b434"
r = requests.get(url="https://freecurrencyapi.net/api/v2/latest?apikey=" + free_currency_api, verify=False)
