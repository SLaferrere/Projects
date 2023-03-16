import requests

request = requests.get("https://api.mercadolibre.com/sites/MLA/search?category=MLA1051").json()

info = request["results"][1]["price"]

print(info)