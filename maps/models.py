from django.db import models


class Profile(models.Model):
    vac_propria = models.BooleanField(default=False)
    vac_pais = models.FloatField(default = 50.0)
    disponibilidade_quarentena = models.BooleanField(default= False)
    # nome_user = models.CharField(max_length=20, unique=True, default= "")
    idade = models.PositiveIntegerField(blank=True,default=None)