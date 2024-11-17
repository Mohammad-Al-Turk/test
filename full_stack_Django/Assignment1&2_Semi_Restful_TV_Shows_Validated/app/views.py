from django.shortcuts import render , redirect , HttpResponse
from django.contrib import messages
from .models import Show
from .models import ShowManager
from . import models

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows' : models.get_all_shows()
    }
    return render(request,'shows.html',context)

def addShow(request):
    return render(request,"show_add.html")

def createShow(request):
    if request.method == 'POST':
        errors = Show.objects.basic_validation(request.POST)
        if len(errors) > 0:
            for key,value in errors.items(): 
                messages.error(request,value)
            return redirect('/shows/new')
        else:
            models.create_show(request.POST)
            messages.success(request, "Show successfully updated")
            return redirect('/shows')
    else:
        return HttpResponse("somthing.html")
    
def show_id(request,id):
    context = {
        'show': models.get_show_by_id(id)
    }
    return render(request,'show_id.html',context)

def destroy_show(request,id):
    models.destroy_show(id)
    return redirect('/shows')

def edit_show(request,id):
    context = {
        'show': models.get_show_by_id(id)
    }
        
    return render(request,'show_edit.html',context)

def update_show(request):
    if request.method == 'POST':
        errors = Show.objects.basic_validation(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect(f'/shows/{int(request.POST["id"])}/Edit')
        else:
            models.update_show(request.POST)
        return redirect('/shows')
    else:
        return HttpResponse("somthing wrong")