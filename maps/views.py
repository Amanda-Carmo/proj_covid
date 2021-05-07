from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Profile
from .serializers import MapsSerializer
import requests
from django.forms.models import model_to_dict

def index(request):
    raise Http404()


@api_view(['GET', 'POST'])
def api_forms(request):
    if request.method == 'POST':
        new_note_data = request.data
        Profile.objects.create(vac_propria = new_note_data['resp_1'], vac_pais = float(new_note_data['resp_2']), disponibilidade_quarentena =new_note_data['resp_3'])
    serialized_note = MapsSerializer(Profile.objects.latest('id'))
    return Response(serialized_note.data)
    

@api_view(['GET', 'POST'])
def api_pais(request, pais,forms_id):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
    print(pais)
    if request.method == 'GET':
        url = "https://covid-19-data.p.rapidapi.com/country"
        querystring = {"name":pais,"format":"json"}
        headers = {
            'x-rapidapi-key': "af765fe219msha36798338e049f0p1d1272jsn67587def0601",
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
            }

        forms = Profile.objects.get(id=forms_id)
        dict_forms = model_to_dict(forms)

        response = requests.request("GET", url, headers=headers, params=querystring)
        
        #FALTA TODA A CONTA
        #PEGAR API COM DADOS DE VACINA POR PAIS


        return Response(response)


@api_view(['GET', 'POST'])
def api_feed(request):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
    if request.method == 'GET':
        url = "https://covid-19-data.p.rapidapi.com/help/countries"
        headers = {
        'x-rapidapi-key': "af765fe219msha36798338e049f0p1d1272jsn67587def0601",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers)
        lista_paises = [e["name"] for e in response.json() ]
        print(len(lista_paises))
        return Response(lista_paises)
