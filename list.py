import requests
import pandas as pd

request = requests.get("https://api.mercadolibre.com/sites/MLA/search?category=MLA1051").json()

# toma los primeros 25 resultados de celulares y devuelve el promedio de precios
def average_price():  
    count = 0
    amount = 0
    for number_of_models in request["results"]:
        if count <= 25:
            price_of_model = number_of_models["price"]
            amount += price_of_model
            count += 1
        else:
            average = round(amount / count, 2)
            return average

# genera un excel con los primeros 25 modelos, condicion y precio de cada uno
def get_models():
    count = 0
    models = {"Models": [],
              "Condition": [],
              "Price": []}
    for models_names in request["results"]:
        if count <= 25:
            models["Models"].append(models_names["title"])
            models["Condition"].append(models_names["condition"])
            models["Price"].append(models_names["price"])
            count += 1
        else:
            df = pd.DataFrame(models)
            df.to_excel("Models.xlsx", index = False)

get_models()
print(average_price())