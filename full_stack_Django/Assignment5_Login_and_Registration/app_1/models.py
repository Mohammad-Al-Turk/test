from django.db import models
import bcrypt
import re



class RegisterManager(models.Manager):
    def mng(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    
            errors['email'] = "Invalid email address!"
        if len(postData['fname']) < 2:
            errors["fname"] = "First name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "Last name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters"
        if postData['password'] != postData['cpassword']:
            errors["not_same"] = "password and confirm password is not match"
        return errors
    

class Register(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email = models.CharField(max_length=45,unique=True)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=RegisterManager()
    
    
def save_data(data):
    pw=data['password']
    pw_hash=bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
    return Register.objects.create(fname=data['fname'],lname=data['lname'],email=data['email'],password=pw_hash)

def login():
    return Register.objects()






    