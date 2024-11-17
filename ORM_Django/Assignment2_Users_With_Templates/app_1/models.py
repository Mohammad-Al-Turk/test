from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
   
def add_user(data): #بنجيب البيانات من ملف الاتش تي ام ال وبنخزنها في الداتا بيس
    # fname=data.POST['fname']
    # lname=data.POST['lname']
    # email=data.POST['email']
    # age=data.POST['age']
    # User.objects.create(fname=fname,lname=lname,email=email,age=age)
    User.objects.create(fname=data['fname'],lname=data['lname'],email=data['email'],age=data['age'])
    
    
def get_data(): #بنجيب جميع البيانات الي في الداتا بيس
    users = User.objects.all()
    return users
    
        
    