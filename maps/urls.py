from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/save/', views.api_forms),
    path('api/pais/', views.api_pais),
    path('api/feed', views.api_feed),

]