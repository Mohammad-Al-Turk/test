from django.urls import path 
from . import views
urlpatterns = [
    path('', views.Gen_num),
    path('guess',views.guess),
    path('playagain',views.playAgain)
]
