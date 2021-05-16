from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.http import Http404, HttpResponse
from rest_framework.response import Response
from .serializers import MapsSerializer
from .models import Profile
import pandas as pd
import requests
import random




def index(request):
    return HttpResponse("Olá mundo! Este é o Servidor para o Projeto 2 de TecWeb \n Por Amanda Carmo e Antonio Fonseca")



@api_view(['GET', 'POST'])
def api_forms(request):
    if request.method == 'POST':
        new_note_data = request.data
        Profile.objects.create(vac_propria = new_note_data['resp_1'], 
                                vac_pais = float(new_note_data['resp_2']), 
                                disponibilidade_quarentena =new_note_data['resp_3'], 
                                nome_user = new_note_data['resp_4'],
                                idade = new_note_data['resp_5'])
    serialized_note = MapsSerializer(Profile.objects.latest('id'))
    return Response(serialized_note.data)
    

@api_view(['GET', 'POST'])
def api_pais(request):
    if request.method == 'POST':
        new_note_data = request.data
        pais = new_note_data['resp_2']
        forms_id = int(new_note_data['resp_1'])
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print([ id['id'] for id in Profile.objects.values('id')])  ##LISTA DE IDS
        print(new_note_data)
        forms = Profile.objects.get(id = forms_id)
        dict_forms = model_to_dict(forms)

        url = "https://covid-19-data.p.rapidapi.com/country"
        querystring = {"name":pais}
        headers = {'x-rapidapi-key': "af765fe219msha36798338e049f0p1d1272jsn67587def0601",'x-rapidapi-host': "covid-19-data.p.rapidapi.com" }
        response = requests.request("GET", url, headers=headers, params=querystring)


        data =  pd.read_csv("https://github.com/owid/covid-19-data/raw/master/public/data/vaccinations/country_data/{}.csv".format(pais))
        linha = data.tail(1)
        pop_vacinada = linha['total_vaccinations'].values[0]
        tempo_vacinando = data.shape[0]/30

        url = "https://countriesnow.space/api/v0.1/countries/population"
        response2 = requests.request("POST", url, headers={}, data={"country": pais})
        pop_atual = response2.json()["data"]["populationCounts"][-1]['value']

        
        
        delta = 0
        idade = dict_forms["idade"]
        porcentagem = dict_forms["vac_pais"]
        if dict_forms["vac_propria"]:
            if idade < 60:
                delta += ((60 - idade)/(10)) **2 #meses
        porcent_ja_vac = (pop_vacinada/pop_atual)*100
        if porcentagem  > porcent_ja_vac:
            dif = porcentagem - porcent_ja_vac
            delta += tempo_vacinando*(dif/porcent_ja_vac)

        resp = {"pais" : pais,"delta" : delta,"porcentagem": porcent_ja_vac} #, "idade": idade, "pop_vacinada": pop_vacinada, "pop_atual":pop_atual, "razao":porcent_ja_vac }
        return Response(resp)
        

@api_view(['GET', 'POST'])
def api_feed(request):
    if request.method == 'GET':

        escolha =  random.sample(range(0, 10), 2)

        url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/news/get-vaccine-news/0"

        headers = {
            'x-rapidapi-key': "af765fe219msha36798338e049f0p1d1272jsn67587def0601",
            'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)
        lista = ['news_id',"imageInLocalStorage","urlToImage","content","imageFileName"]
        final = [response.json()["news"][escolha[0]],
            response.json()["news"][escolha[1]]]
        for e in lista:
            del final[0][e]
            del final[1][e]

        return Response(final)