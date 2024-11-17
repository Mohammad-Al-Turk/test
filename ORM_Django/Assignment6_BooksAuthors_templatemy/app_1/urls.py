from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index),
    path('bookpro', views.book),
    path('authorpro', views.author_save),
    path('authors', views.author),
    path('authors/<int:id>', views.author_id),
    path('books/<int:id>', views.book_id),
    path('joinBooks', views.joinInAuthor),
    # authorForSelect
]
