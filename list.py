import requests
import pandas as pd

# toma los primeros 25 resultados de celulares y devuelve el promedio de precios
def average_price():  
    request = requests.get("https://api.mercadolibre.com/sites/MLA/search?category=MLA1051").json()
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
    request = requests.get("https://api.mercadolibre.com/sites/MLA/search?category=MLA1051").json()
    count = 0
    models = []
    for models_names in request["results"]:
        if count <= 25:
            model = {}
            model["Model"] = models_names.get("title", "")
            model["Condition"] = models_names.get("condition", "")
            model["Price"] = models_names.get("price", "")
            models.append(model)
            count += 1
        else:
            pd.DataFrame(models).to_excel("Models.xlsx", index = False)

get_models()
print(average_price())