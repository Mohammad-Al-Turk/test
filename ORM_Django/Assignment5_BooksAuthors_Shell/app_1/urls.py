from django.urls import path 
from . import models

urlpatterns = [    
    path('Book', models.Book),
    path('Author', models.Author),
]
