from django.urls import path
from . import views    



urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new' , views.addShow),
    path('shows/create',views.createShow , name="createShow"),
    path('shows/<int:id>',views.show_id),
    path('shows/<int:id>/destroy',views.destroy_show),
    path('shows/<int:id>/Edit',views.edit_show),
    path('confirmupdate',views.update_show)
]
