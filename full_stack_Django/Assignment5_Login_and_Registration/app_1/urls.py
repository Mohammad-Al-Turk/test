from django.urls import path 
from . import views
urlpatterns = [
    path('', views.main),
    path('savedata', views.saveData),
    path('checklogin', views.checkLogin),
    path('success', views.success),
    path('clearsession', views.clearSession),
    
]