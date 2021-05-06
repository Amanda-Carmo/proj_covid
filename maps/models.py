from django.db import models


class Profile(models.Model):
    vac_propria = models.BooleanField(default=False)
    vac_pais = models.FloatField(default = 25.0)
    disponibilidade_quarentena = models.BooleanField(default= False)
    
