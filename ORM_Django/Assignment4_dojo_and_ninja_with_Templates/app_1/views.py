from django.shortcuts import render,redirect
from . import models



def index(request):
    context={
        'data_dojo':models.get_data_dojo(),
        'data_ninja':models.get_data_ninja()
        }
    return render(request,'index.html',context)



def save_data_from_dojo(request):
    models.save_data_dojo(request.POST)
    return redirect('/')



def save_data_from_ninja(request):
    models.save_data_ninja(request.POST)
    return redirect('/')


