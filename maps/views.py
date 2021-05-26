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
    return render(request, 'maps/index.html')


def mapa(request):
    print("!!!!!!!!!!!!!!!!!!!!!!")
    print(request)
    print(request.POST)
    vac_propria = request.POST.get('resp_1')
    vac_pais = int(request.POST.get('resp_2'))
    disponibilidade_quarentena = request.POST.get('resp_3')
    continente = request.POST.get('resp_4')
    idade = int(request.POST.get('resp_5'))

    Profile.objects.create(vac_propria = (vac_propria == "True") , 
                                vac_pais = vac_pais, 
                                disponibilidade_quarentena =(disponibilidade_quarentena == "True"), 
                                idade = idade)
    porcentagem = vac_pais
    pais = "Brazil"
    


    return render(request, 'maps/map.html',{'vac_propria':vac_propria,
                                            'vac_pais':vac_pais,
                                            'disponibilidade_quarentena':disponibilidade_quarentena,
                                            'continente':continente,
                                            'idade':idade})


@api_view(['GET', 'POST'])
def api_forms(request):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(request.data)
    # {'vac_propria': 'True', 'vac_pais': '54', 'continente': 'sa', 'idade': '54'}
    vac_propria = (request.data['vac_propria'] == "True")
    idade = float(request.data['idade'])
    porcentagem = float(request.data['vac_pais'])
    pais = request.data['continente'].capitalize()
    try:
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
        if vac_propria== 'True':
            if idade < 60:
                delta += ((60 - idade)/(10)) **2 #meses
        porcent_ja_vac = (pop_vacinada/pop_atual)*100
        if porcentagem  > porcent_ja_vac:
            dif = porcentagem - porcent_ja_vac
            delta += tempo_vacinando*(dif/porcent_ja_vac)

        resp = delta
    except Exception as e: 
        print(e)
        resp ="Dados Nao Encontrados, Tente Digitar novamente o nome do pais"
    return Response(resp)

