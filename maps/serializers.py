from rest_framework import serializers
from .models import Profile


class MapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'vac_propria', 'vac_pais', 'disponibilidade_quarentena']