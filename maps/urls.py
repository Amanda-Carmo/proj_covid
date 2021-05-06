from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('api/save/', views.api_maps),
]