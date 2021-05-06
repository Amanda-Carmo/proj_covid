from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Profile
from .serializers import MapsSerializer

def index(request):
    return render(request, 'maps/index.html')


    # path('api/<str:resp_1>/<int:resp_2>/<str:resp_3>/', views.api_maps),


@api_view(['GET', 'POST'])
def api_maps(request):
    prof = Profile.objects.all()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(request.data)
    if request.method == 'POST':
        new_note_data = request.data
        prof.vac_propria = new_note_data['resp_1']
        prof.vac_pais = new_note_data['resp_2']
        prof.disponibilidade_quarentena = new_note_data['resp_3']
        Profile.objects.create(vac_propria = new_note_data['resp_1'], vac_pais = float(new_note_data['resp_2']), disponibilidade_quarentena =new_note_data['resp_3'])
    serialized_note = MapsSerializer(prof)
    return Response(serialized_note.data)
    