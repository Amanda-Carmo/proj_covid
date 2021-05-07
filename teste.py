import requests

url = "https://covid-19-data.p.rapidapi.com/country"

querystring = {"name":"italy","format":"json"}

headers = {
    'x-rapidapi-key': "67213a5abfmsh326035097963877p182cbcjsn8d7706e91f9e",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)