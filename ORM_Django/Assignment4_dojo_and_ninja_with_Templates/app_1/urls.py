from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index),
    path('dojopro', views.save_data_from_dojo),
    path('ninjapro', views.save_data_from_ninja),
]
