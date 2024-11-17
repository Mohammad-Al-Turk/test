from django.shortcuts import *
from django.contrib import messages
from .models import *
from . import models
import bcrypt


def main(request):
    return render(request,'index.html')
 
 
def saveData(request):
    if request.method=='POST':
        errors = Register.objects.mng(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            models.save_data(request.POST)
            if 'user_id' not in request.session:
                em = request.POST.get('email')
            user = Register.objects.get(email=em)
            request.session['user_fname']=user.fname
            return redirect('/success')

    else:
        return HttpResponse("Error")
    
    
def success(request):
    context={
        'data': request.session['user_fname']

    }
    return render(request,'success.html',context)
        

# def checkLogin(request):
#     if request.method=='POST':
#         em=request.POST['email']
#         pw=request.POST['password']
#         user = Register.objects.get(email=request.POST['email'])
#         if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
#             print("password match")
#             context={
#                 'data' : models.login(),
#               }
#         else:
#             print("failed password")
#         return render(request,'success.html',context)
#     else:
#         return HttpResponse("Error")

def checkLogin(request):
    if request.method == 'POST':
        
        em = request.POST.get('email')
        pw = request.POST.get('password')
        user = Register.objects.get(email=em)
        request.session['user_fname']=user.fname


        try:
            if bcrypt.checkpw(pw.encode(), user.password.encode()):
                messages.success(request, "Login successful!")
                return redirect('/success')
            else:
                messages.error(request, "Invalid password. Please try again.")
                return redirect('/')
        except Register.DoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect('/')
    else:
        return HttpResponse("Error")
    
    
    
    
    
    
def clearSession(request):
    request.session.clear()
    return redirect('/')

