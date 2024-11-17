from django.shortcuts import render, redirect
from . import models
def index(request):
    context={
        'users':models.get_data()
    }
    return render(request,'index.html',context)


def process(request):
    models.add_user(request.POST)#بنحدد نوع الركويست الي هو بوست, بدون بوست رح يزبط
    return redirect('/')
