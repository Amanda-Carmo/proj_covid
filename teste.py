import requests
import pandas as pd

delta = 0
idade = 21
porcentagem = 50.5
if True:
    if idade < 60:
        delta += ((60 - idade)/(10)) **1.75 #meses

print("Resultdado para {} == {:.2f} meses".format(idade, delta))



# data =  pd.read_csv("https://github.com/owid/covid-19-data/raw/master/public/data/vaccinations/country_data/Austria.csv")
# print(data.shape)

# linha = data.tail(1)
# teste = linha['people_fully_vaccinated'].values[0]
# print(teste)


# url = "https://countriesnow.space/api/v0.1/countries/population"

# payload = {"country": "Austria"}
# headers = {}

# response = requests.request("POST", url, headers=headers, data=payload)
# final = response.json()["data"]["populationCounts"][-1]['value']
# print(final)

# print((teste/final)*100)