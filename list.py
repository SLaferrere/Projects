import requests

request = requests.get("https://api.mercadolibre.com/sites/MLA/search?category=MLA1051").json()

def average_price():
    count = 0
    amount = 0
    for number_of_models in request["results"]:
        count += 1
        price_of_module = number_of_models["price"]
        amount += price_of_module
    average = round(amount / count, 2)
    return average
        
print(average_price())
