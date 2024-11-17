from django.db import models

class Dojo(models.Model):
    name= models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Ninja(models.Model):
    fname = models.CharField(max_length=45)
    secname = models.CharField(max_length=45)
    dojoselector = models.CharField(max_length=45)
    dojo=models.ForeignKey(Dojo,related_name="ninjas",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

    
def save_data_dojo(data):
    Dojo.objects.create(name=data['name'],city=data['city'],state=data['state'])

def save_data_ninja(data):
    Ninja.objects.create(fname=data['fname'],secname=data['secname'],dojoselector=data['doojoo'],dojo=Dojo.objects.get(id=data["doojoo"]))
    
    
def get_data_dojo():
    data_dojo=Dojo.objects.all()
    return data_dojo
    
    
def get_data_ninja():
    data_ninja=Ninja.objects.all()
    return data_ninja